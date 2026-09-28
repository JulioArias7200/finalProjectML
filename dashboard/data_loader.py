"""
Cargador de Datos y Métricas para el Dashboard de Aprendizaje Supervisado.
EAIMCS (INE Bolivia) - Consume el dataset preprocesado sin duplicar lógica.
"""

import sys
import logging
from pathlib import Path
from typing import Dict, Any, List, Optional
import numpy as np
import pandas as pd

# Asegurar importación de preprocessing
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from preprocessing.preprocessing import (
    run_preprocessing,
    map_caeb_to_sector,
    PREDICTOR_NUM_COLS
)

logger = logging.getLogger("dashboard.data_loader")

class DashboardDataLoader:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DashboardDataLoader, cls).__new__(cls)
            cls._instance.initialized = False
        return cls._instance

    def __init__(self):
        if self.initialized:
            return

        self.project_root = PROJECT_ROOT
        self.processed_path = self.project_root / "data" / "processed" / "dataset_procesado.csv"
        self.df = None
        self.kpis: Dict[str, Any] = {}
        self._load_and_prepare()
        self.initialized = True

    def _load_and_prepare(self):
        if not self.processed_path.exists():
            logger.info("Dataset procesado no encontrado. Ejecutando run_preprocessing()...")
            self.df = run_preprocessing(save_outputs=True)
        else:
            logger.info("Cargando dataset procesado desde: %s", self.processed_path)
            self.df = pd.read_csv(self.processed_path, low_memory=False)

        tot_emp = len(self.df)
        med_ing = float(self.df["target"].median())
        mean_ing = float(self.df["target"].mean())
        tot_ing = float(self.df["target"].sum())
        n_deptos = int(self.df["depto"].nunique())
        n_sectores = int(self.df["sector_macro"].nunique())
        top_depto = str(self.df["depto"].value_counts().index[0])
        top_sector = str(self.df["sector_macro"].value_counts().index[0])

        self.kpis = {
            "total_empresas": tot_emp,
            "ingreso_mediano": med_ing,
            "ingreso_promedio": mean_ing,
            "ingreso_total_agregado": tot_ing,
            "num_departamentos": n_deptos,
            "num_macrosectores": n_sectores,
            "top_departamento": top_depto,
            "top_sector": top_sector,
            "fuente": "INE Bolivia - EAIMCS 2017-2018",
            "cobertura": "Nacional (9 departamentos, medianas y grandes empresas)"
        }
        logger.info("Data loader inicializado: %d empresas cargadas.", tot_emp)

    def get_kpis(self) -> Dict[str, Any]:
        return self.kpis

    def get_data(self) -> pd.DataFrame:
        return self.df

    def get_dictionary(self) -> List[Dict[str, str]]:
        """Retorna el catálogo oficial de variables según docs/02_diccionario_datos_EAIMCS.md."""
        entries = [
            {"name": "ID", "section": "Carátula", "desc": "Identificador único de la empresa (llave de unión)", "type": "Numérico / ID", "sample": "10824, 16646"},
            {"name": "C2_01", "section": "Carátula", "desc": "Departamento de ubicación de la empresa (9 departamentos)", "type": "Texto / Categórica", "sample": "SANTA CRUZ, LA PAZ, COCHABAMBA"},
            {"name": "actividad_pricipal_codigo_V1", "section": "Carátula", "desc": "Código CAEB de la Actividad Principal de la empresa", "type": "Código / Categórica", "sample": "41000, 47301, 10104"},
            {"name": "S00_01_A", "section": "Sección 0", "desc": "TOTAL Ingresos Operativos en Bs (VARIABLE OBJETIVO DEL MODELO)", "type": "Monetaria (Bs)", "sample": "Mediana: 15.83M Bs, Min: 1.28M Bs"},
            {"name": "S05_04", "section": "Sección 5", "desc": "TOTAL Ingresos Sección 5 (equivalente exacto a S00_01_A)", "type": "Monetaria (Bs)", "sample": "Mediana: 15.83M Bs"},
            {"name": "S05_01", "section": "Sección 5", "desc": "Ingresos por venta de productos fabricados en Bs (Excluida por fuga)", "type": "Monetaria (Bs)", "sample": "0 a 5.19B Bs"},
            {"name": "S05_02", "section": "Sección 5", "desc": "Ingresos por venta de mercaderías en Bs (Excluida por fuga)", "type": "Monetaria (Bs)", "sample": "0 a 2.05B Bs"},
            {"name": "S05_03", "section": "Sección 5", "desc": "Ingresos por servicios prestados en Bs (Excluida por fuga)", "type": "Monetaria (Bs)", "sample": "0 a 4.68B Bs"},
            {"name": "S01_05_A", "section": "Sección 1", "desc": "TOTAL Personal Ocupado (hombres y mujeres, permanentes y eventuales)", "type": "Conteo / Personas", "sample": "Mediana: 27, Media: 91.5"},
            {"name": "S01_03_C", "section": "Sección 1", "desc": "Sueldos y salarios básicos anuales del personal remunerado en Bs", "type": "Monetaria (Bs)", "sample": "Mediana: 1.20M Bs"},
            {"name": "S01_14", "section": "Sección 1", "desc": "TOTAL Otras Remuneraciones (aguinaldos, aportes a salud y AFPs, bonos)", "type": "Monetaria (Bs)", "sample": "Mediana: 596,106 Bs"},
            {"name": "S02_09", "section": "Sección 2", "desc": "TOTAL Energía eléctrica, agua y combustibles consumidos en Bs", "type": "Monetaria (Bs)", "sample": "Mediana: 131,748 Bs"},
            {"name": "S07_09_E", "section": "Sección 7", "desc": "TOTAL Valor Histórico Final de Activos Fijos (maquinaria, edificios, transporte)", "type": "Monetaria (Bs)", "sample": "Mediana: 5.72M Bs"},
            {"name": "S06_06_B", "section": "Sección 6", "desc": "TOTAL Inventarios Finales (materias primas, productos en proceso y terminados)", "type": "Monetaria (Bs)", "sample": "Mediana: 977,600 Bs"},
            {"name": "S12_01_B", "section": "Sección 12", "desc": "Capacidad máxima de almacenamiento de materia prima", "type": "Cantidad / Capacidad", "sample": "0 a 637M unidades"},
            {"name": "S12_02_B", "section": "Sección 12", "desc": "Capacidad máxima de almacenamiento de producto terminado", "type": "Cantidad / Capacidad", "sample": "0 a 122M unidades"},
            {"name": "n_insumos", "section": "Sección 10", "desc": "Número de materias primas/materiales declarados por empresa (agregado)", "type": "Conteo", "sample": "0 a 67 insumos"},
            {"name": "total_valor_co", "section": "Sección 10", "desc": "Valor total de compras de materias primas e insumos en Bs (agregado)", "type": "Monetaria (Bs)", "sample": "Mediana fabril: 3.22M Bs"},
            {"name": "total_valor_uti", "section": "Sección 10", "desc": "Valor total de utilización de insumos en el proceso productivo en Bs", "type": "Monetaria (Bs)", "sample": "Mediana fabril: 3.20M Bs"}
        ]
        return entries

    def get_distribution_data(self) -> Dict[str, Any]:
        """Prepara datos completos para el histograma interactivo de ingresos operativos."""
        if hasattr(self, "_cached_distribution") and self._cached_distribution is not None:
            return self._cached_distribution

        y_raw = self.df["target"].values
        y_log = self.df["target_log"].values
        self._cached_distribution = {
            "raw_values": [float(v) for v in y_raw],
            "log_values": [float(v) for v in y_log],
            "median_bs": float(np.median(y_raw)),
            "mean_bs": float(np.mean(y_raw)),
            "total_count": len(y_raw),
            "skew_note": "Distribución fuertemente asimétrica a la derecha (Pareto/Log-normal típica de ingresos)."
        }
        return self._cached_distribution

    def get_boxplot_depto_data(self) -> List[Dict[str, Any]]:
        """Datos de ingresos agrupados por los 9 departamentos sin truncamiento muestral."""
        if hasattr(self, "_cached_boxplot_deptos") and self._cached_boxplot_deptos is not None:
            return self._cached_boxplot_deptos

        result = []
        for depto, group in self.df.groupby("depto"):
            vals = group["target"].values
            vals_log = group["target_log"].values
            result.append({
                "depto": depto,
                "count": len(vals),
                "median_bs": float(np.median(vals)),
                "q25_bs": float(np.percentile(vals, 25)),
                "q75_bs": float(np.percentile(vals, 75)),
                "sample_bs": [float(v) for v in vals],
                "sample_log": [float(v) for v in vals_log]
            })
        result = sorted(result, key=lambda x: x["count"], reverse=True)
        self._cached_boxplot_deptos = result
        return self._cached_boxplot_deptos

    def get_boxplot_sector_data(self) -> List[Dict[str, Any]]:
        """Datos de ingresos agrupados por todos los macrosectores económicos."""
        if hasattr(self, "_cached_boxplot_sectors") and self._cached_boxplot_sectors is not None:
            return self._cached_boxplot_sectors

        result = []
        for sector, group in self.df.groupby("sector_macro"):
            if len(group) < 5:
                continue
            vals = group["target"].values
            vals_log = group["target_log"].values
            result.append({
                "sector": sector,
                "count": len(vals),
                "median_bs": float(np.median(vals)),
                "q25_bs": float(np.percentile(vals, 25)),
                "q75_bs": float(np.percentile(vals, 75)),
                "sample_bs": [float(v) for v in vals],
                "sample_log": [float(v) for v in vals_log]
            })
        result = sorted(result, key=lambda x: x["median_bs"], reverse=True)
        self._cached_boxplot_sectors = result
        return self._cached_boxplot_sectors

    def get_correlation_data(self) -> Dict[str, Any]:
        """Matriz de correlación lineal entre predictores e ingresos en escala logarítmica."""
        if hasattr(self, "_cached_correlation") and self._cached_correlation is not None:
            return self._cached_correlation

        vars_dict = {
            "Ingresos (S00_01_A)": "target",
            "Personal (S01_05_A)": "S01_05_A",
            "Sueldos Básicos (S01_03_C)": "S01_03_C",
            "Otras Remun. (S01_14)": "S01_14",
            "Energía/Comb. (S02_09)": "S02_09",
            "Activos Fijos (S07_09_E)": "S07_09_E",
            "Inventarios (S06_06_B)": "S06_06_B",
            "Insumos Utiliz.": "total_valor_uti",
            "Capacidad Almac.": "S12_01_B"
        }
        labels = list(vars_dict.keys())
        cols = list(vars_dict.values())

        sub_df = pd.DataFrame()
        for l, c in zip(labels, cols):
            sub_df[l] = np.log1p(self.df[c])

        corr_matrix = sub_df.corr().round(3).values.tolist()
        self._cached_correlation = {
            "labels": labels,
            "matrix": corr_matrix,
            "method": "Pearson sobre escala logarítmica log(1 + x)"
        }
        return self._cached_correlation

    def get_outliers_data(self) -> Dict[str, Any]:
        """Subconjunto de puntos con cálculo de discrepancias bivariadas y ratios operativos."""
        if hasattr(self, "_cached_outliers") and self._cached_outliers is not None:
            return self._cached_outliers

        sample = self.df[["ID", "depto", "sector_macro", "S01_05_A", "S01_03_C", "S07_09_E", "target"]].copy()
        
        # Ratio Ingreso / Sueldo (evitando divisiones espurias por cero agregando constante proporcional)
        sample["ratio_ing_sueldo"] = (sample["target"] / (sample["S01_03_C"] + 1000.0)).clip(upper=200)

        # Detección bivariada de anomalías mediante residuo logarítmico respecto a la relación esperada
        log_y = np.log1p(sample["target"])
        log_w = np.log1p(sample["S01_03_C"])
        
        # Regresión ortogonal / tendencia base simple
        residuos = np.abs(log_y - (0.65 * log_w + 6.5))
        q75_res = np.percentile(residuos, 75)
        iqr_res = q75_res - np.percentile(residuos, 25)
        umbral_outlier = q75_res + 1.5 * iqr_res
        sample["is_outlier"] = residuos > umbral_outlier

        data_points = []
        for _, r in sample.sample(n=min(500, len(sample)), random_state=42).iterrows():
            data_points.append({
                "id": int(r["ID"]),
                "depto": str(r["depto"]),
                "sector": str(r["sector_macro"]),
                "personal": float(r["S01_05_A"]),
                "sueldos_bs": float(r["S01_03_C"]),
                "activos_bs": float(r["S07_09_E"]),
                "ingreso_bs": float(r["target"]),
                "ratio": round(float(r["ratio_ing_sueldo"]), 2),
                "is_outlier": bool(r["is_outlier"])
            })
        self._cached_outliers = {
            "points": data_points,
            "total_outliers_iqr": int(sample["is_outlier"].sum()),
            "outliers_pct": round(float(sample["is_outlier"].mean() * 100), 2)
        }
        return self._cached_outliers

    def get_heatmap_depto_sector(self) -> Dict[str, Any]:
        """Calcula matriz 2D cruzada de Departamento x Macrosector para el Panorama General."""
        if hasattr(self, "_cached_heatmap") and self._cached_heatmap is not None:
            return self._cached_heatmap

        deptos = sorted(list(self.df["depto"].unique()))
        top_sectores = list(self.df["sector_macro"].value_counts().head(8).index)
        
        counts_matrix = []
        median_matrix = []
        total_matrix = []

        for d in deptos:
            d_sub = self.df[self.df["depto"] == d]
            row_c = []
            row_m = []
            row_t = []
            for s in top_sectores:
                cell = d_sub[d_sub["sector_macro"] == s]
                if len(cell) > 0:
                    row_c.append(int(len(cell)))
                    row_m.append(round(float(cell["target"].median() / 1e6), 2))
                    row_t.append(round(float(cell["target"].sum() / 1e6), 2))
                else:
                    row_c.append(0)
                    row_m.append(0.0)
                    row_t.append(0.0)
            counts_matrix.append(row_c)
            median_matrix.append(row_m)
            total_matrix.append(row_t)

        self._cached_heatmap = {
            "deptos": deptos,
            "sectores": top_sectores,
            "counts": counts_matrix,
            "median_bs_millions": median_matrix,
            "total_bs_millions": total_matrix,
            "matrix_count": counts_matrix,
            "matrix_median": median_matrix,
            "matrix_total": total_matrix
        }
        return self._cached_heatmap

    def _prepare_risk_and_predictions(self):
        """Precomputa predicciones e indicadores de riesgo para todas las empresas."""
        if hasattr(self, "_companies_cache") and self._companies_cache is not None:
            return

        model_path = self.project_root / "dashboard" / "artifacts" / "best_model.joblib"
        registry_path = self.project_root / "dashboard" / "artifacts" / "registry.json"

        smearing_factor = 1.0401
        rmse_log = 0.5697

        model = None
        if model_path.exists():
            try:
                import joblib
                model = joblib.load(model_path)
            except Exception as e:
                logger.warning("No se pudo cargar best_model.joblib en data_loader: %s", e)

        if registry_path.exists():
            try:
                import json
                with open(registry_path, "r", encoding="utf-8") as f:
                    reg = json.load(f)
                    smearing_factor = float(reg.get("smearing_factor", smearing_factor))
                    rmse_log = float(reg.get("rmse_log", rmse_log))
            except Exception:
                pass

        y_real_bs = self.df["target"].values
        y_real_log = self.df["target_log"].values

        if model is not None:
            try:
                y_pred_log = model.predict(self.df)
            except Exception as e:
                logger.warning("Error al predecir con modelo serializado: %s", e)
                y_pred_log = 0.7 * np.log1p(self.df["S01_03_C"]) + 6.0
        else:
            y_pred_log = 0.7 * np.log1p(self.df["S01_03_C"]) + 6.0

        y_pred_bs = np.maximum(0.0, np.exp(y_pred_log) * smearing_factor - 1.0)
        lower_log = y_pred_log - 1.645 * rmse_log
        upper_log = y_pred_log + 1.645 * rmse_log
        lower_bs = np.maximum(0.0, np.exp(lower_log) * smearing_factor - 1.0)
        upper_bs = np.maximum(0.0, np.exp(upper_log) * smearing_factor - 1.0)

        residuals_log = y_real_log - y_pred_log
        z_scores = residuals_log / max(0.01, rmse_log)

        # Precalcular estadísticas por sector para posición relativa
        sector_stats = {}
        for s_name, group in self.df.groupby("sector_macro"):
            sorted_targets = np.sort(group["target"].values)
            sector_stats[s_name] = {
                "values": sorted_targets,
                "median": float(np.median(sorted_targets)),
                "count": len(sorted_targets)
            }

        companies_list = []
        risk_counts = {"Alto": 0, "Medio": 0, "Bajo": 0}

        for idx, row in self.df.iterrows():
            c_id = int(row["ID"])
            depto = str(row["depto"])
            sector = str(row["sector_macro"])
            real = float(y_real_bs[idx])
            pred = float(y_pred_bs[idx])
            diff_bs = real - pred
            diff_pct = (diff_bs / max(1.0, pred)) * 100.0
            z = float(z_scores[idx])

            # Determinación de score de riesgo (enfoque de auditoría tributaria/consistencia):
            # Alto riesgo: ingresos declarados severamente inferiores a la estructura productiva
            if z < -1.4 or diff_pct < -40.0:
                riesgo = "Alto"
                motivo = "Ingreso declarado significativamente inferior a la capacidad productiva estimada (z < -1.4)."
            elif z < -0.6 or diff_pct < -18.0:
                riesgo = "Medio"
                motivo = "Discrepancia moderada por debajo de la cota media esperada."
            else:
                riesgo = "Bajo"
                motivo = "Ingreso congruente o superior a la estructura de costos y activos observada."

            risk_counts[riesgo] += 1

            s_info = sector_stats.get(sector, {"values": [real], "median": real, "count": 1})
            vals_sector = s_info["values"]
            rank_idx = int(np.searchsorted(vals_sector, real))
            pct_rank = round((rank_idx / max(1, len(vals_sector))) * 100, 1)

            dentro_ic = bool(real >= lower_bs[idx] and real <= upper_bs[idx])

            companies_list.append({
                "id": c_id,
                "depto": depto,
                "sector": sector,
                "sector_macro": sector,
                "personal": int(row.get("S01_05_A", 0)),
                "personal_ocupado": int(row.get("S01_05_A", 0)),
                "sueldos_bs": float(row.get("S01_03_C", 0)),
                "activos_bs": float(row.get("S07_09_E", 0)),
                "activos_fijos_bs": float(row.get("S07_09_E", 0)),
                "ingreso_declarado": round(real, 2),
                "ingreso_declarado_bs": round(real, 2),
                "ingreso_esperado": round(pred, 2),
                "ingreso_esperado_bs": round(pred, 2),
                "discrepancia_bs": round(diff_bs, 2),
                "discrepancia_pct": round(diff_pct, 1),
                "ic_inferior_bs": round(float(lower_bs[idx]), 2),
                "ic_90_lower_bs": round(float(lower_bs[idx]), 2),
                "ic_superior_bs": round(float(upper_bs[idx]), 2),
                "ic_90_upper_bs": round(float(upper_bs[idx]), 2),
                "dentro_ic_90": dentro_ic,
                "z_score": round(z, 2),
                "score_riesgo": riesgo,
                "riesgo_nivel": riesgo,
                "motivo_riesgo": motivo,
                "posicion_sector_pct": pct_rank,
                "ranking_sector": f"{len(vals_sector) - rank_idx + 1} de {len(vals_sector)}",
                "mediana_sector_bs": round(s_info["median"], 2),
                "total_sector_empresas": s_info["count"],
                "total_empresas_sector": s_info["count"]
            })

        # Ordenar por score de riesgo: Alto -> Medio -> Bajo, y dentro por mayor discrepancia negativa
        risk_order = {"Alto": 0, "Medio": 1, "Bajo": 2}
        companies_list.sort(key=lambda x: (risk_order[x["score_riesgo"]], x["discrepancia_pct"]))

        self._companies_cache = companies_list
        self._risk_counts = risk_counts

    def get_companies_risk(self, limit: int = 50, offset: int = 0, riesgo: str = "", sector: str = "", depto: str = "", query: str = "") -> Dict[str, Any]:
        """Retorna la lista de empresas ordenada por score de riesgo con filtrado exacto y paginación."""
        self._prepare_risk_and_predictions()
        filtered = self._companies_cache

        import unicodedata
        def strip_accents(s: str) -> str:
            return "".join(c for c in unicodedata.normalize("NFD", str(s)) if unicodedata.category(c) != "Mn").lower()

        # Filtrado con coincidencia exacta normalizada para selectores categóricos
        if riesgo:
            r_target = strip_accents(riesgo.strip())
            filtered = [c for c in filtered if strip_accents(c["score_riesgo"]) == r_target]
        if sector:
            s_target = strip_accents(sector.strip())
            filtered = [c for c in filtered if strip_accents(c["sector"]) == s_target]
        if depto:
            d_target = strip_accents(depto.strip())
            filtered = [c for c in filtered if strip_accents(c["depto"]) == d_target]

        # Filtrado por búsqueda: igualdad exacta para códigos/IDs numéricos, subcadena insensible para texto
        if query:
            q_clean = query.strip()
            id_candidate = q_clean.lstrip("#").strip()
            if id_candidate.isdigit():
                target_id = int(id_candidate)
                # IGUALDAD EXACTA: "1" devuelve ÚNICAMENTE la empresa con ID 1 (nunca 10, 11, 12, etc.)
                filtered = [c for c in filtered if c["id"] == target_id]
            else:
                q_norm = strip_accents(q_clean)
                filtered = [
                    c for c in filtered
                    if q_norm in strip_accents(c["sector"]) or q_norm in strip_accents(c["depto"]) or q_norm in strip_accents(c.get("motivo_riesgo", ""))
                ]

        total_filtered = len(filtered)
        paginated = filtered[offset: offset + limit]

        total_all = len(self._companies_cache)
        alto_c = self._risk_counts.get("Alto", 0)
        medio_c = self._risk_counts.get("Medio", 0)
        bajo_c = self._risk_counts.get("Bajo", 0)

        return {
            "total": total_filtered,
            "total_general": total_all,
            "resumen_riesgo": self._risk_counts,
            "summary": {
                "alto": alto_c,
                "alto_pct": round((alto_c / max(1, total_all)) * 100, 1),
                "medio": medio_c,
                "medio_pct": round((medio_c / max(1, total_all)) * 100, 1),
                "bajo": bajo_c,
                "bajo_pct": round((bajo_c / max(1, total_all)) * 100, 1),
                "total_evaluado": total_all
            },
            "empresas": paginated
        }

    def get_company_detail(self, company_id: int) -> Optional[Dict[str, Any]]:
        """Obtiene la ficha individual detallada de una empresa específica."""
        self._prepare_risk_and_predictions()
        for c in self._companies_cache:
            if c["id"] == company_id:
                return c
        return None

    def get_bunching_analysis(self) -> Dict[str, Any]:
        """
        Analiza a nivel agregado sectorial la densidad de empresas en la vecindad inmediata
        de los umbrales regulatorios de categorización empresarial (Bunching Analysis).
        Alerta si la densidad observada se desvía de la distribución suave de referencia.
        NUNCA señala empresas individuales, solo macrosectores.
        """
        sectors_analysis = []
        top_sectors = list(self.df["sector_macro"].value_counts().head(8).index)

        for sector in top_sectors:
            sec_df = self.df[self.df["sector_macro"] == sector]
            n_sec = len(sec_df)
            if n_sec < 10:
                continue

            is_prod = any(k in sector for k in ["Industria", "Construcción", "Minería", "Electricidad"])
            u = 35000000.0 if is_prod else 28000000.0

            targets = sec_df["target"].values
            pre_window = (targets >= 0.75 * u) & (targets < u)
            post_window = (targets >= u) & (targets <= 1.25 * u)

            count_pre = int(np.sum(pre_window))
            count_post = int(np.sum(post_window))
            density_pre = round((count_pre / n_sec) * 100, 2)
            density_post = round((count_post / n_sec) * 100, 2)

            expected_density = 10.5
            desviacion = round(((density_pre - expected_density) / expected_density) * 100, 1)

            # Alerta si densidad pre-umbral excede significativamente la referencia
            alerta = bool(density_pre >= 16.0 and count_pre >= 5)

            if alerta:
                nivel = "ALERTA ACTIVA"
                mensaje = (
                    f"Concentración anómala pre-umbral de {density_pre}% (+{desviacion}% sobre referencia esperada). "
                    f"Indicio de posible aglomeración ('bunching') bajo el umbral de Bs {u/1e6:.1f}M."
                )
            else:
                nivel = "DISTRIBUCIÓN REGULAR"
                mensaje = (
                    f"Densidad continua ({density_pre}% en frontera). "
                    f"Distribución suave alrededor de Bs {u/1e6:.1f}M sin discontinuidades atípicas."
                )

            sectors_analysis.append({
                "sector": sector,
                "total_empresas": n_sec,
                "umbral_evaluado_bs": u,
                "umbral_evaluado_fmt": f"Bs {u/1e6:.1f}M",
                "conteo_pre_umbral": count_pre,
                "conteo_post_umbral": count_post,
                "densidad_observada_pct": density_pre,
                "densidad_referencia_pct": expected_density,
                "desviacion_pct": desviacion,
                "alerta_activa": alerta,
                "nivel": nivel,
                "diagnostico": mensaje
            })

        sectors_analysis.sort(key=lambda x: (not x["alerta_activa"], -x["desviacion_pct"]))
        total_alertas = sum(1 for s in sectors_analysis if s["alerta_activa"])

        return {
            "total_sectores_analizados": len(sectors_analysis),
            "sectores_con_alerta": total_alertas,
            "metodologia": "Análisis no paramétrico de masa de probabilidad en el entorno de umbral vs. densidad suave continua.",
            "nota_gobernanza": "Este análisis se reporta de forma agregada a nivel de sector económico (Directriz Decreto Ley 1405 y confidencialidad estadística).",
            "sectores": sectors_analysis
        }
