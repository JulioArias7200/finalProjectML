"""
Módulo de Preprocesamiento de Datos para Aprendizaje Supervisado.
Dataset: EAIMCS 2017-2018 (INE Bolivia) - Estimación de Ingresos Operativos.

Centraliza todas las reglas de negocio, limpieza de centinelas,
agregación de insumos por empresa y prevención de fuga de datos (data leakage).
"""

import logging
import sys
import json
import hashlib
from decimal import Decimal, InvalidOperation
from datetime import datetime
from pathlib import Path
from typing import Tuple, List, Any, Dict
import numpy as np
import pandas as pd

# -----------------------------------------------------------------------------
# CONFIGURACIÓN DE LOGGING
# -----------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger("preprocessing")

# -----------------------------------------------------------------------------
# CONSTANTES DE RUTAS Y REGLAS DE NEGOCIO
# -----------------------------------------------------------------------------
PROJECT_ROOT: Path = Path(__file__).resolve().parents[1]
DEFAULT_RAW_DIR: Path = PROJECT_ROOT / "data" / "raw"
DEFAULT_PROCESSED_DIR: Path = PROJECT_ROOT / "data" / "processed"

# Archivos crudos de entrada
RAW_FILE_GENERAL: str = "MOD_ANUAL_S01-07_12_general_i.csv"
RAW_FILE_MATERIALES: str = "MOD_ANUAL_S10_materiales_i.csv"

# Archivos procesados de salida
PROCESSED_FILE_CSV: str = "dataset_procesado.csv"
PROCESSED_FILE_PARQUET: str = "dataset_procesado.parquet"

# Código citado en reglas metodológicas específicas. No aplicarlo globalmente.
CENTINELA_VAL: float = 99999.0

# Variable Objetivo (Ingresos Operativos Anuales)
# En el extracto actual, 60 pares difieren por redondeo de hasta Bs 1.
TARGET_COL: str = "S00_01_A"
TARGET_ALT_COL: str = "S05_04"
TARGET_RECONCILIATION_TOLERANCE_BS: float = 1.0

# Columnas excluidas para PREVENCIÓN DE FUGA DE DATOS (Data Leakage)
# Incluye componentes de ingresos de Sección 5 y agregados macroeconómicos del INE (VBP, VA, CI)
EXCLUDED_LEAKAGE_COLS: List[str] = [
    "S05_01", "S05_02", "S05_03", "S05_04",  # Componentes de ingresos que reproducen el target
    "VPA", "PC", "ISPOINF", "VIPP", "VBP",   # Variables macroeconómicas que contienen producción
    "EAC", "OGO", "VUMPEEI", "CI", "VA",     # Cuentas de valor agregado y consumo intermedio
    "SSB", "OPP", "PS", "R", "D"             # Ratios y variables calculadas post-encuesta
]

# Variables predictoras numéricas clave de estructura productiva
PREDICTOR_NUM_COLS: List[str] = [
    "S01_05_A",   # Total personal ocupado
    "S01_03_C",   # Sueldos y salarios básicos anuales
    "S01_14",     # Otras remuneraciones (aguinaldos, aportes salud/AFPs, bonos)
    "S02_09",     # Total energía, agua y combustibles
    "S07_09_E",   # Activos fijos: total valor histórico final
    "S06_06_B",   # Total inventarios finales
    # S12_*_B excluidas: cantidades con unidades S12_*_C heterogéneas.
    "n_insumos",  # Variedad de materias primas declaradas (de Sección 10)
    "total_valor_co",   # Valor compras de materias primas en Bs (de Sección 10)
    "total_valor_uti"   # Valor utilización de materias primas en Bs (de Sección 10)
]

# Variables predictoras categóricas
PREDICTOR_CAT_COLS: List[str] = [
    "depto",         # Departamento normalizado (9 departamentos)
    "sector_macro"   # Macrosector económico CAEB normalizado
]

# Semilla fija para reproducibilidad
RANDOM_STATE_SEED: int = 42


# -----------------------------------------------------------------------------
# FUNCIONES DE PREPROCESAMIENTO
# -----------------------------------------------------------------------------
def load_raw_datasets(raw_dir: Path | None = None) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Carga los archivos crudos del Módulo General y de Materiales desde data/raw/.
    
    Args:
        raw_dir: Ruta al directorio de datos crudos (default: data/raw).
        
    Returns:
        Tupla (df_general, df_materiales).
    """
    directory = Path(raw_dir) if raw_dir else DEFAULT_RAW_DIR
    p_gen = directory / RAW_FILE_GENERAL
    p_mat = directory / RAW_FILE_MATERIALES

    if not p_gen.exists():
        raise FileNotFoundError(f"No se encontró el archivo general en: {p_gen}")
    if not p_mat.exists():
        raise FileNotFoundError(f"No se encontró el archivo de materiales en: {p_mat}")

    logger.info("Cargando archivo general: %s", p_gen.name)
    df_gen = pd.read_csv(p_gen, low_memory=False, dtype={TARGET_COL: "string", TARGET_ALT_COL: "string"})

    logger.info("Cargando archivo de materiales: %s", p_mat.name)
    df_mat = pd.read_csv(p_mat, low_memory=False)
    df_mat.attrs["source_rows"] = len(df_mat)
    blank_rows = df_mat.isna().all(axis=1)
    df_mat = df_mat.loc[~blank_rows].copy()
    df_mat.attrs["source_rows"] = int(len(df_mat) + blank_rows.sum())
    df_mat.attrs["blank_rows_excluded"] = int(blank_rows.sum())

    required_general = {"ID", "C2_01", "actividad_pricipal_codigo_V1", TARGET_COL, TARGET_ALT_COL}
    required_materials = {"ID", "materia", "valor_co", "valor_uti"}
    missing_general = required_general - set(df_gen.columns)
    missing_materials = required_materials - set(df_mat.columns)
    if missing_general or missing_materials:
        raise ValueError(f"Columnas obligatorias ausentes: general={sorted(missing_general)}, materiales={sorted(missing_materials)}")
    if df_gen["ID"].isna().any() or df_gen["ID"].duplicated().any():
        raise ValueError("El archivo general requiere un ID único y no nulo por empresa")
    if df_mat["ID"].isna().any():
        raise ValueError("El archivo de materiales contiene ID nulo")

    logger.info("Datos crudos leídos: General=%d filas | Materiales=%d filas", len(df_gen), len(df_mat))
    return df_gen, df_mat


def clean_materials_data(df_mat: pd.DataFrame) -> pd.DataFrame:
    """
    Convierte importes a numérico. Negativos inválidos pasan a ausente.
    El valor exacto 99999 se conserva mientras no exista regla por campo.
    
    Args:
        df_mat: DataFrame con los registros de insumos y materias primas.
        
    Returns:
        DataFrame limpio de materiales.
    """
    df = df_mat.copy()
    
    # No convertir un importe alto en centinela ni un negativo en cero.
    for col in ["valor_co", "valor_uti"]:
        if col in df.columns:
            s = pd.to_numeric(df[col], errors="coerce")
            df[f"{col}_clean"] = s.where(s >= 0)
            
    logger.debug("Valores monetarios negativos convertidos a ausente, sin acotamiento artificial.")
    return df


def target_differences(df: pd.DataFrame) -> pd.Series:
    """Compara montos con Decimal para no perder centavos en importes grandes."""
    def difference(row: pd.Series) -> float:
        left, right = row[TARGET_COL], row[TARGET_ALT_COL]
        if pd.isna(left) or pd.isna(right):
            return np.nan
        try:
            return float(abs(Decimal(str(left)) - Decimal(str(right))))
        except InvalidOperation:
            return np.nan
    return df[[TARGET_COL, TARGET_ALT_COL]].apply(difference, axis=1)


def aggregate_materials_by_enterprise(df_mat_clean: pd.DataFrame) -> pd.DataFrame:
    """
    Agrega la tabla de estructura larga (N registros por empresa) a nivel empresa por 'ID'.
    Calcula: n_insumos (conteo), total_valor_co (compras) y total_valor_uti (utilización).
    
    Args:
        df_mat_clean: DataFrame limpio de materiales.
        
    Returns:
        DataFrame agregado a nivel empresa con una fila por ID.
    """
    agg_df = df_mat_clean.groupby("ID").agg(
        n_insumos=("ID", "size"),
        total_valor_co=("valor_co_clean", lambda s: s.sum(min_count=1)),
        total_valor_uti=("valor_uti_clean", lambda s: s.sum(min_count=1))
    ).reset_index()

    logger.info("Sección 10 agregada: %d empresas únicas con insumos declarados.", len(agg_df))
    return agg_df


def map_caeb_to_sector(code: Any) -> str:
    """
    Mapea el código de actividad económica CAEB (CIIU Rev. 4) al macrosector oficial.
    
    Args:
        code: Código CAEB numérico o string.
        
    Returns:
        Nombre homogéneo del macrosector en español.
    """
    try:
        c_str = str(code).strip()[:2]
        num = int(c_str)
        if 1 <= num <= 3:
            return "Agropecuario y Pesca"
        elif 5 <= num <= 9:
            return "Minería e Hidrocarburos"
        elif 10 <= num <= 33:
            return "Industria Manufacturera"
        elif 35 <= num <= 39:
            return "Electricidad, Gas y Agua"
        elif 41 <= num <= 43:
            return "Construcción"
        elif 45 <= num <= 47:
            return "Comercio Mayorista y Minorista"
        elif 49 <= num <= 53:
            return "Transporte y Almacenamiento"
        elif 55 <= num <= 56:
            return "Alojamiento y Servicios de Comida"
        elif 58 <= num <= 63:
            return "Información y Comunicaciones"
        elif 64 <= num <= 66:
            return "Intermediación Financiera"
        elif 68 <= num <= 68:
            return "Actividades Inmobiliarias"
        elif 69 <= num <= 75:
            return "Servicios Profesionales y Técnicos"
        elif 77 <= num <= 82:
            return "Servicios Administrativos y de Apoyo"
        elif 85 <= num <= 85:
            return "Educación"
        elif 86 <= num <= 88:
            return "Salud y Asistencia Social"
        else:
            return "Otras Actividades de Servicios"
    except Exception:
        return "Otras Actividades de Servicios"


def merge_and_clean_enterprise_data(df_gen: pd.DataFrame, df_mat_agg: pd.DataFrame) -> pd.DataFrame:
    """
    Une la tabla general y los insumos agregados vía Left Join por 'ID'.
    Conserva como ausentes los importes cuando no hay fila de materiales.
    
    Args:
        df_gen: DataFrame de empresas general (MOD_ANUAL_S01-07_12).
        df_mat_agg: DataFrame agregado de materiales por ID.
        
    Returns:
        DataFrame consolidado a nivel empresa.
    """
    merged = df_gen.merge(df_mat_agg, on="ID", how="left", validate="one_to_one")
    
    merged["has_material_record"] = merged["n_insumos"].notna()
    # Cero filas declaradas; los importes desconocidos permanecen ausentes.
    merged["n_insumos"] = merged["n_insumos"].fillna(0)

    # Normalización de categorías geográficas y sectoriales
    merged["depto"] = merged["C2_01"].astype(str).str.strip().str.upper()
    merged["sector_macro"] = merged["actividad_pricipal_codigo_V1"].apply(map_caeb_to_sector)

    # Identificación y verificación de la variable objetivo (S00_01_A)
    target_series = pd.to_numeric(merged[TARGET_COL], errors="coerce")
    alt_series = pd.to_numeric(merged[TARGET_ALT_COL], errors="coerce")
    discrepant = target_differences(merged) > TARGET_RECONCILIATION_TOLERANCE_BS
    if discrepant.any():
        raise ValueError(f"{int(discrepant.sum())} objetivos exceden tolerancia de conciliación de Bs 1")
    merged["target"] = target_series

    # Filtrar únicamente empresas con ingresos positivos válidos
    valid_mask = merged["target"].notnull() & (merged["target"] > 0)
    filtered = merged[valid_mask].copy()

    logger.info("Unión completada: %d empresas válidas con target > 0.", len(filtered))
    return filtered


def apply_feature_transformations(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aplica limpieza de centinelas en predictores numéricos y genera las
    transformaciones logarítmicas log(1 + x) para estabilizar varianzas.
    
    Args:
        df: DataFrame consolidado a nivel empresa.
        
    Returns:
        DataFrame con columnas originales limpias y columnas transformadas log_*.
    """
    res = df.copy()

    # Target logarítmico
    res["target_log"] = np.log1p(res["target"])

    # Preservar faltantes; la imputación se ajusta solo en entrenamiento.
    for col in PREDICTOR_NUM_COLS:
        if col in res.columns:
            cleaned = pd.to_numeric(res[col], errors="coerce")
            res[col] = cleaned.where(cleaned >= 0)
            res[f"log_{col}"] = np.log1p(res[col])
            
    logger.info("Transformación log1p aplicada exitosamente a %d predictores numéricos.", len(PREDICTOR_NUM_COLS))
    return res


def run_preprocessing(
    raw_dir: Path | None = None,
    output_dir: Path | None = None,
    save_outputs: bool = True
) -> pd.DataFrame:
    """
    Ejecuta el pipeline completo de preprocesamiento de extremo a extremo y genera
    automáticamente la bitácora de evolución por etapas (bitacora_preprocesamiento.json):
    1. Validación de claves, tipos y valores negativos; recuento de posibles códigos especiales.
    2. Agregación de Sección 10 a nivel empresarial.
    3. Normalización categórica CAEB y estandarización geográfica.
    4. Políticas anti-leakage y validación de variable objetivo.
    5. Transformación logarítmica log(1 + x) de predictores y target.
    6. Exportación a data/processed/ (CSV y Parquet opcional).
    
    Returns:
        DataFrame completamente preprocesado y listo para modelado.
    """
    logger.info("=== INICIANDO PIPELINE DE PREPROCESAMIENTO ===")
    bitacora_etapas: List[Dict[str, Any]] = []

    # Cargar datos crudos
    df_gen, df_mat = load_raw_datasets(raw_dir)
    
    # -------------------------------------------------------------------------
    # ETAPA 1: Validación y limpieza documentada
    # -------------------------------------------------------------------------
    mat_rows_before, mat_cols_before = df_mat.shape
    centinelas_mat = int((df_mat[["valor_co", "valor_uti"]].isin([CENTINELA_VAL, str(int(CENTINELA_VAL))])).sum().sum())
    centinelas_gen = 0
    for col in PREDICTOR_NUM_COLS:
        if col in df_gen.columns:
            centinelas_gen += int((pd.to_numeric(df_gen[col], errors="coerce") == CENTINELA_VAL).sum())
    total_centinelas_afectados = centinelas_mat + centinelas_gen

    df_mat_clean = clean_materials_data(df_mat)
    mat_rows_after, mat_cols_after = df_mat_clean.shape

    bitacora_etapas.append({
        "etapa": "Validación de valores monetarios",
        "orden": 1,
        "filas_antes": mat_rows_before,
        "columnas_antes": mat_cols_before,
        "filas_despues": mat_rows_after,
        "columnas_despues": mat_cols_after,
        "valores_afectados": int(sum((pd.to_numeric(df_mat[c], errors="coerce") < 0).sum() for c in ["valor_co", "valor_uti"])),
        "descripcion_regla": "Importes negativos pasan a ausente. El valor exacto 99999 se cuenta, pero no se recodifica sin regla específica por variable. No se recortan importes altos."
    })

    # -------------------------------------------------------------------------
    # ETAPA 2: Agregación de la Sección 10
    # -------------------------------------------------------------------------
    agg_rows_before, agg_cols_before = df_mat_clean.shape
    df_mat_agg = aggregate_materials_by_enterprise(df_mat_clean)
    agg_rows_after, agg_cols_after = df_mat_agg.shape

    bitacora_etapas.append({
        "etapa": "Agregación de la Sección 10",
        "orden": 2,
        "filas_antes": agg_rows_before,
        "columnas_antes": agg_cols_before,
        "filas_despues": agg_rows_after,
        "columnas_despues": agg_cols_after,
        "valores_afectados": agg_rows_before,
        "descripcion_regla": f"Transformación de estructura larga ({agg_rows_before} registros de materias primas) a nivel empresarial por 'ID' único ({agg_rows_after} empresas), calculando variedad (n_insumos), compras totales (total_valor_co) y consumo fabril (total_valor_uti)."
    })

    # -------------------------------------------------------------------------
    # ETAPA 3: Normalización categórica CAEB
    # -------------------------------------------------------------------------
    gen_rows_before, gen_cols_before = df_gen.shape
    merged_pre = df_gen.merge(df_mat_agg, on="ID", how="left", validate="one_to_one").copy()
    merged_pre["has_material_record"] = merged_pre["n_insumos"].notna()
    merged_pre["n_insumos"] = merged_pre["n_insumos"].fillna(0)
    merged_pre["depto"] = merged_pre["C2_01"].astype(str).str.strip().str.upper()
    merged_pre["sector_macro"] = merged_pre["actividad_pricipal_codigo_V1"].apply(map_caeb_to_sector)

    zeros_imputed = int((~merged_pre["has_material_record"]).sum())
    norm_rows_after, norm_cols_after = merged_pre.shape

    bitacora_etapas.append({
        "etapa": "Normalización categórica CAEB",
        "orden": 3,
        "filas_antes": gen_rows_before,
        "columnas_antes": gen_cols_before,
        "filas_despues": norm_rows_after,
        "columnas_despues": norm_cols_after,
        "valores_afectados": gen_rows_before + zeros_imputed,
        "descripcion_regla": "Cruce Left Join validado uno a uno; sectores derivados de los códigos CAEB. n_insumos=0 significa sin filas de materiales; importes sin declaración permanecen ausentes."
    })

    # -------------------------------------------------------------------------
    # ETAPA 4: Políticas anti-leakage
    # -------------------------------------------------------------------------
    leakage_rows_before, leakage_cols_before = merged_pre.shape
    target_series = pd.to_numeric(merged_pre[TARGET_COL], errors="coerce")
    alt_series = pd.to_numeric(merged_pre[TARGET_ALT_COL], errors="coerce")
    target_difference = target_differences(merged_pre)
    discrepancy_count = int((target_difference > TARGET_RECONCILIATION_TOLERANCE_BS).sum())
    if discrepancy_count:
        raise ValueError(f"{discrepancy_count} objetivos exceden tolerancia de conciliación de Bs 1")
    merged_pre["target"] = target_series
    valid_mask = merged_pre["target"].notnull() & (merged_pre["target"] > 0)
    filtered = merged_pre[valid_mask].copy()

    leak_cols_present = [c for c in EXCLUDED_LEAKAGE_COLS if c in filtered.columns]
    leakage_rows_after, leakage_cols_after = filtered.shape

    bitacora_etapas.append({
        "etapa": "Políticas anti-leakage",
        "orden": 4,
        "filas_antes": leakage_rows_before,
        "columnas_antes": leakage_cols_before,
        "filas_despues": leakage_rows_after,
        "columnas_despues": leakage_cols_after,
        "valores_afectados": len(leak_cols_present) + int((~valid_mask).sum()),
        "descripcion_regla": f"Objetivo S00_01_A conciliado con S05_04; {len(leak_cols_present)} columnas relacionadas con ingreso marcadas como excluidas del modelo. La selección se aplica en entrenamiento."
    })

    # -------------------------------------------------------------------------
    # ETAPA 5: Transformación logarítmica
    # -------------------------------------------------------------------------
    trans_rows_before, trans_cols_before = filtered.shape
    processed_df = apply_feature_transformations(filtered)
    trans_rows_after, trans_cols_after = processed_df.shape

    bitacora_etapas.append({
        "etapa": "Transformación logarítmica",
        "orden": 5,
        "filas_antes": trans_rows_before,
        "columnas_antes": trans_cols_before,
        "filas_despues": trans_rows_after,
        "columnas_despues": trans_cols_after,
        "valores_afectados": trans_rows_after * (len(PREDICTOR_NUM_COLS) + 1),
        "descripcion_regla": f"log1p para {len(PREDICTOR_NUM_COLS)} predictores no negativos y objetivo; valores ausentes preservados para imputación dentro del pipeline de entrenamiento."
    })

    # -------------------------------------------------------------------------
    # Identificadores de ejecución y bitácora de preprocesamiento en JSON
    # -------------------------------------------------------------------------
    raw_path = Path(raw_dir) if raw_dir else DEFAULT_RAW_DIR
    def sha256(path: Path) -> str:
        digest = hashlib.sha256()
        with path.open("rb") as source:
            for chunk in iter(lambda: source.read(1024 * 1024), b""):
                digest.update(chunk)
        return digest.hexdigest()

    source_sha256 = {RAW_FILE_GENERAL: sha256(raw_path / RAW_FILE_GENERAL), RAW_FILE_MATERIALES: sha256(raw_path / RAW_FILE_MATERIALES)}

    # run_id reproducible: hash de los hashes de entrada; misma entrada produce mismo run_id por fecha.
    run_payload = "|".join(f"{name}:{digest}" for name, digest in sorted(source_sha256.items()))
    run_id = "PRE-" + datetime.now().strftime("%Y%m%d") + "-" + hashlib.sha256(run_payload.encode("utf-8")).hexdigest()[:12]

    bitacora_data = {
        "timestamp": datetime.now().isoformat(),
        "run_id": run_id,
        "dataset_nombre": "EAIMCS 2017-2018 (INE Bolivia)",
        "total_etapas": len(bitacora_etapas),
        "filas_iniciales": gen_rows_before,
        "filas_finales": trans_rows_after,
        "columnas_iniciales": gen_cols_before,
        "columnas_finales": trans_cols_after,
        "etapas": bitacora_etapas
    }

    quality_report = {
        "generated_at": datetime.now().isoformat(),
        "run_id": run_id,
        "source_sha256": source_sha256,
        "general_rows": int(len(df_gen)),
        "general_unique_ids": int(df_gen["ID"].nunique()),
        "materials_rows": int(len(df_mat)),
        "materials_source_rows": int(df_mat.attrs.get("source_rows", len(df_mat))),
        "materials_blank_rows_excluded": int(df_mat.attrs.get("blank_rows_excluded", 0)),
        "materials_unique_ids": int(df_mat["ID"].nunique()),
        "orphan_material_rows": int((~df_mat["ID"].isin(df_gen["ID"])).sum()),
        "target_exact_matches": int((target_difference == 0).sum()),
        "target_rounding_differences": int(((target_difference > 0) & (target_difference <= TARGET_RECONCILIATION_TOLERANCE_BS)).sum()),
        "target_max_difference_bs": float(target_difference.max()),
        "target_excluded_rows": int((~valid_mask).sum()),
        "observed_sectors": int(processed_df["sector_macro"].nunique()),
        "reported_special_code_99999_count": total_centinelas_afectados,
        "monetary_missing_after_join": {c: int(processed_df[c].isna().sum()) for c in ["total_valor_co", "total_valor_uti"]},
        "capacity_policy": "S12_B excluidas de predictores hasta normalizar por S12_C; valores originales conservados para auditoría"
    }
    bitacora_data["quality_report"] = quality_report

    # Guardar dataset procesado
    if save_outputs:
        preprocessing_dir = PROJECT_ROOT / "preprocessing"
        artifacts_dir = PROJECT_ROOT / "dashboard" / "artifacts"
        artifacts_dir.mkdir(parents=True, exist_ok=True)
        for path in [preprocessing_dir / "bitacora_preprocesamiento.json", artifacts_dir / "bitacora_preprocesamiento.json"]:
            with path.open("w", encoding="utf-8") as output:
                json.dump(bitacora_data, output, indent=2, ensure_ascii=False)
        with (preprocessing_dir / "quality_report.json").open("w", encoding="utf-8") as output:
            json.dump(quality_report, output, indent=2, ensure_ascii=False)
        out_dir = Path(output_dir) if output_dir else DEFAULT_PROCESSED_DIR
        out_dir.mkdir(parents=True, exist_ok=True)

        csv_path = out_dir / PROCESSED_FILE_CSV
        logger.info("Guardando dataset procesado en CSV: %s", csv_path)
        processed_df.to_csv(csv_path, index=False, encoding="utf-8")

        # Intentar exportar a Parquet si el motor pyarrow o fastparquet está disponible
        try:
            parquet_path = out_dir / PROCESSED_FILE_PARQUET
            processed_df.to_parquet(parquet_path, index=False)
            logger.info("Guardando dataset procesado en Parquet: %s", parquet_path)
        except (ImportError, ValueError):
            logger.info("Motor Parquet no disponible en el entorno; salida CSV generada correctamente.")

    logger.info(
        "=== PREPROCESAMIENTO COMPLETADO: %d filas x %d columnas ===",
        processed_df.shape[0], processed_df.shape[1]
    )
    return processed_df


if __name__ == "__main__":
    df_final = run_preprocessing(save_outputs=True)
    t = df_final["target"]
    print("\n--- RESUMEN ESTADÍSTICO DE LA VARIABLE OBJETIVO (S00_01_A) ---")
    print(f"Total empresas procesadas: {len(df_final):,}")
    print(f"Mínimo:  Bs {t.min():,.2f}")
    print(f"Mediana: Bs {t.median():,.2f}")
    print(f"Media:   Bs {t.mean():,.2f}")
    print(f"Máximo:  Bs {t.max():,.2f}")
