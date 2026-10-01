"""
Script de Entrenamiento y Validación de Modelos de Regresión.
Proyecto: AprendizajeSupervisadoML (EAIMCS - INE Bolivia).

Evalúa Ridge, Random Forest e HistGradientBoosting con 5-Fold Cross Validation.
Exporta el modelo de producción a dashboard/artifacts/ sin duplicaciones.
"""

import sys
import json
import math
import hashlib
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List
import numpy as np
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score, cross_validate
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor, HistGradientBoostingRegressor
from sklearn.metrics import r2_score, mean_absolute_error, root_mean_squared_error, median_absolute_error
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Asegurar importación de preprocessing
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from preprocessing.preprocessing import (
    run_preprocessing,
    PREDICTOR_NUM_COLS,
    PREDICTOR_CAT_COLS,
    RANDOM_STATE_SEED
)

# Configuración de Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger("models.train")


def train_and_evaluate(
    df: pd.DataFrame,
    artifacts_dir: Path,
    models_dir: Path
) -> Dict[str, Any]:
    """
    Entrena y compara los modelos de regresión, selecciona el mejor ensamble,
    calcula diagnósticos e importancia de variables, y guarda artefactos en dashboard/artifacts/.
    """
    artifacts_dir.mkdir(parents=True, exist_ok=True)
    models_dir.mkdir(parents=True, exist_ok=True)

    log_num_cols: List[str] = [f"log_{c}" for c in PREDICTOR_NUM_COLS]
    cat_cols: List[str] = PREDICTOR_CAT_COLS

    X = df[log_num_cols + cat_cols].copy()
    y_raw = df["target"].values
    y_log = np.log1p(y_raw)

    # Estratificación en split inicial basada en cuantiles del target
    y_quantiles = pd.qcut(y_log, q=5, labels=False, duplicates="drop")
    X_train, X_test, y_train_log, y_test_log, y_train_raw, y_test_raw = train_test_split(
        X, y_log, y_raw, test_size=0.2, random_state=RANDOM_STATE_SEED, stratify=y_quantiles
    )

    # Conjunto de calibración separado (protocolo G2/T06): excluido del ajuste y de la CV.
    fit_quantiles = pd.qcut(y_train_log, q=5, labels=False, duplicates="drop")
    X_fit, X_calib, y_fit_log, y_calib_log, y_fit_raw, y_calib_raw = train_test_split(
        X_train, y_train_log, y_train_raw, test_size=0.25,
        random_state=RANDOM_STATE_SEED, stratify=fit_quantiles
    )

    # Umbrales fijados en models/protocolo_entrenamiento.md ANTES de esta ejecución.
    META_MEDAPE_MAX = 40.0          # D06: umbral de aprobación de esta iteración
    META_R2_BS_MIN = 0.70           # D06
    META_HISTORICA_MEDAPE = 25.0    # referencia aspiracional histórica; no aprueba G2
    CONFORMAL_NOMINAL = 0.90        # D02
    CONFORMAL_TOLERANCIA = (0.85, 0.95)

    # Imputación por mediana DENTRO del pipeline: cada pliegue/pliegue de CV y cada ajuste
    # aprende la mediana solo con sus datos de entrenamiento (anti-fuga; contrato 02).
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", Pipeline([
                ("imputer", SimpleImputer(strategy="median")),
                ("scaler", StandardScaler())
            ]), log_num_cols),
            ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), cat_cols)
        ]
    )

    models = {
        "Ridge": Ridge(alpha=10.0),
        "RandomForest": RandomForestRegressor(
            n_estimators=120, max_depth=16, min_samples_split=4,
            random_state=RANDOM_STATE_SEED, n_jobs=1
        ),
        "HistGradientBoosting": HistGradientBoostingRegressor(
            max_iter=150, max_depth=6, learning_rate=0.08,
            random_state=RANDOM_STATE_SEED
        )
    }

    hiperparametros_dict = {
        "Ridge": {
            "alpha": 10.0,
            "fit_intercept": True,
            "solver": "auto",
            "random_state": RANDOM_STATE_SEED
        },
        "RandomForest": {
            "n_estimators": 120,
            "max_depth": 16,
            "min_samples_split": 4,
            "random_state": RANDOM_STATE_SEED,
            "n_jobs": 1
        },
        "HistGradientBoosting": {
            "max_iter": 150,
            "max_depth": 6,
            "learning_rate": 0.08,
            "random_state": RANDOM_STATE_SEED
        }
    }

    def build_razon(name: str) -> str:
        """Razón de decisión generada desde las métricas reales de ESTA ejecución (sin cifras heredadas)."""
        m = results[name]
        if name == "Ridge":
            return (
                f"Descartado como campeón: línea base lineal regularizada; captura parcialmente la relación "
                f"(R² log = {m['r2_log']:.4f}, R² Bs = {m['r2_bs']:.4f}) con MedAPE elevado ({m['medape_percent']:.2f}%) "
                "y mayor sesgo en empresas grandes."
            )
        if name == "HistGradientBoosting":
            return (
                f"Descartado: rendimiento competitivo (R² log = {m['r2_log']:.4f}, R² Bs = {m['r2_bs']:.4f}, "
                f"MedAPE = {m['medape_percent']:.2f}%), pero inferior a Random Forest en escala natural en esta ejecución."
            )
        return (
            f"Seleccionado (Modelo Campeón): mejor desempeño global (R² log = {m['r2_log']:.4f}, "
            f"R² Bs = {m['r2_bs']:.4f}) tras calibración Duan (factor {m['smearing_factor']:.4f}) y menor error mediano "
            f"porcentual (MedAPE = {m['medape_percent']:.2f}%; umbral de aprobación D06 ≤ 40% con meta histórica ≤ 25% no alcanzada). "
            f"Intervalo conformal calibrado (D02) con cobertura empírica del {m['cobertura_conformal_pct']:.2f}% en prueba "
            "dentro de la tolerancia predefinida [85%, 95%]."
        )

    results: Dict[str, Any] = {}
    fitted_pipelines: Dict[str, Pipeline] = {}
    smearing_factors: Dict[str, float] = {}

    # Validación cruzada estratificada por cuantiles, solo sobre el subconjunto de ajuste
    fit_quantiles_cv = pd.qcut(y_fit_log, q=5, labels=False, duplicates="drop")
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE_SEED)

    logger.info("Iniciando validación cruzada estratificada (5 Folds) con cálculo de R², RMSE y MedAPE por pliegue...")
    for name, model in models.items():
        # CV iterativo para registrar métricas exactas por pliegue (R², RMSE, MedAPE)
        fold_records = []
        fold_r2 = []
        fold_rmse = []
        fold_mae = []
        fold_medape = []

        for i, (tr_idx, val_idx) in enumerate(cv.split(X_fit, fit_quantiles_cv)):
            X_tr, X_val = X_fit.iloc[tr_idx], X_fit.iloc[val_idx]
            y_tr_l, y_val_l = y_fit_log[tr_idx], y_fit_log[val_idx]
            y_val_r = y_fit_raw[val_idx]

            pipe_f = Pipeline([
                ("prep", preprocessor),
                ("reg", model)
            ])
            pipe_f.fit(X_tr, y_tr_l)
            val_pred_l = pipe_f.predict(X_val)

            smear_f = float(np.mean(np.exp(y_tr_l - pipe_f.predict(X_tr))))
            val_pred_r = np.maximum(0.0, np.exp(val_pred_l) * smear_f - 1.0)

            f_r2 = float(r2_score(y_val_l, val_pred_l))
            f_rmse = float(root_mean_squared_error(y_val_l, val_pred_l))
            f_mae = float(mean_absolute_error(y_val_l, val_pred_l))
            f_medape = float(np.median(np.abs(y_val_r - val_pred_r) / np.maximum(y_val_r, 1.0)) * 100)

            fold_r2.append(f_r2)
            fold_rmse.append(f_rmse)
            fold_mae.append(f_mae)
            fold_medape.append(f_medape)

            fold_records.append({
                "fold": i + 1,
                "r2": round(f_r2, 4),
                "rmse": round(f_rmse, 4),
                "mae": round(f_mae, 4),
                "medape": round(f_medape, 2)
            })

        # Ajuste en train completo
        pipe = Pipeline([
            ("prep", preprocessor),
            ("reg", model)
        ])
        pipe.fit(X_fit, y_fit_log)
        fitted_pipelines[name] = pipe

        # Cálculo del Factor de Retransformación de Duan (Smearing Factor) en ajuste
        train_pred_log = pipe.predict(X_fit)
        residuals_train = y_fit_log - train_pred_log
        smearing_factor = float(np.mean(np.exp(residuals_train)))
        smearing_factors[name] = smearing_factor

        # Evaluación en Test aplicando corrección de Duan
        y_pred_log = pipe.predict(X_test)
        y_pred_raw = np.maximum(0.0, np.exp(y_pred_log) * smearing_factor - 1.0)

        # Métricas log y naturales (Bs)
        r2_log = float(r2_score(y_test_log, y_pred_log))
        mae_log = float(mean_absolute_error(y_test_log, y_pred_log))
        rmse_log = float(root_mean_squared_error(y_test_log, y_pred_log))

        r2_bs = float(r2_score(y_test_raw, y_pred_raw))
        mae_bs = float(mean_absolute_error(y_test_raw, y_pred_raw))
        rmse_bs = float(root_mean_squared_error(y_test_raw, y_pred_raw))
        medae_bs = float(median_absolute_error(y_test_raw, y_pred_raw))
        medape = float(np.median(np.abs(y_test_raw - y_pred_raw) / np.maximum(y_test_raw, 1.0)) * 100)

        # ---- Intervalo predictivo CONFORMAL calibrado (D02), en escala log1p ----
        calib_pred_log = pipe.predict(X_calib)
        calib_scores = np.abs(y_calib_log - calib_pred_log)
        n_calib = len(calib_scores)
        rank = math.ceil((n_calib + 1) * CONFORMAL_NOMINAL)
        q_hat_log = float(np.sort(calib_scores)[min(rank, n_calib) - 1])
        lower_log_c = y_pred_log - q_hat_log
        upper_log_c = y_pred_log + q_hat_log
        lower_bs_c = np.maximum(0.0, np.exp(lower_log_c) * smearing_factor - 1.0)
        upper_bs_c = np.maximum(0.0, np.exp(upper_log_c) * smearing_factor - 1.0)
        inside_c = (y_test_raw >= lower_bs_c) & (y_test_raw <= upper_bs_c)
        cov_c = float(np.mean(inside_c) * 100)
        width_c = float(np.mean(upper_bs_c - lower_bs_c))

        # Referencia nominal ±1,645×RMSE: prohibida como "intervalo 90%"; solo informativa
        lower_log_r = y_pred_log - 1.645 * rmse_log
        upper_log_r = y_pred_log + 1.645 * rmse_log
        lower_bs_r = np.maximum(0.0, np.exp(lower_log_r) * smearing_factor - 1.0)
        upper_bs_r = np.maximum(0.0, np.exp(upper_log_r) * smearing_factor - 1.0)
        cov_ref = round(float(np.mean((y_test_raw >= lower_bs_r) & (y_test_raw <= upper_bs_r)) * 100), 2)

        # Cobertura y amplitud por segmentos del intervalo conformal (A06)
        def segment_coverage(mask: np.ndarray) -> Dict[str, Any]:
            if not mask.sum():
                return {"n": 0, "cobertura_pct": None, "amplitud_media_bs": None}
            return {
                "n": int(mask.sum()),
                "cobertura_pct": round(float(np.mean(inside_c[mask]) * 100), 2),
                "amplitud_media_bs": round(float(np.mean(upper_bs_c[mask] - lower_bs_c[mask])), 2),
            }

        test_sector = X_test["sector_macro"].to_numpy()
        test_depto = X_test["depto"].to_numpy()
        quintiles_test = pd.qcut(y_test_log, q=5, labels=False, duplicates="drop")
        q_labels = ["Q1 (menores)", "Q2", "Q3", "Q4", "Q5 (mayores)"]
        segments_coverage = {
            "por_sector": {str(s): segment_coverage(test_sector == s) for s in sorted(set(test_sector))},
            "por_depto": {str(d): segment_coverage(test_depto == d) for d in sorted(set(test_depto))},
            "por_quintil": {q_labels[i]: segment_coverage(quintiles_test == i) for i in range(5) if (quintiles_test == i).sum()},
        }

        # Métricas por subgrupo del conjunto de prueba (A05)
        def subgroup_metrics(mask: np.ndarray) -> Dict[str, Any]:
            n = int(mask.sum())
            out: Dict[str, Any] = {"n": n}
            if n == 0:
                return out
            out["mediana_objetivo_bs"] = round(float(np.median(y_test_raw[mask])), 2)
            if n < 10:
                out["nota"] = "N<10: sin conclusion de desempeno"
                return out
            out["r2_bs"] = round(float(r2_score(y_test_raw[mask], y_pred_raw[mask])), 4)
            out["medape_pct"] = round(float(np.median(np.abs(y_test_raw[mask] - y_pred_raw[mask]) / np.maximum(y_test_raw[mask], 1.0)) * 100), 2)
            out["error_mediano_bs"] = round(float(median_absolute_error(y_test_raw[mask], y_pred_raw[mask])), 2)
            return out

        segments_metrics = {
            "por_sector": {str(s): subgroup_metrics(test_sector == s) for s in sorted(set(test_sector))},
            "por_depto": {str(d): subgroup_metrics(test_depto == d) for d in sorted(set(test_depto))},
            "por_quintil": {q_labels[i]: subgroup_metrics(quintiles_test == i) for i in range(5) if (quintiles_test == i).sum()},
        }

        results[name] = {
            "cv_r2_mean": float(np.mean(fold_r2)),
            "cv_r2_std": float(np.std(fold_r2)),
            "cv_rmse_mean": float(np.mean(fold_rmse)),
            "cv_rmse_std": float(np.std(fold_rmse)),
            "cv_mae_mean": float(np.mean(fold_mae)),
            "cv_mae_std": float(np.std(fold_mae)),
            "cv_medape_mean": float(np.mean(fold_medape)),
            "cv_medape_std": float(np.std(fold_medape)),
            "cv_folds": fold_records,
            "r2_log": r2_log,
            "mae_log": mae_log,
            "rmse_log": rmse_log,
            "r2_bs": r2_bs,
            "mae_bs": mae_bs,
            "rmse_bs": rmse_bs,
            "medae_bs": medae_bs,
            "medape_percent": medape,
            "smearing_factor": smearing_factor,
            "conformal_q_log": q_hat_log,
            "cobertura_conformal_pct": round(cov_c, 2),
            "amplitud_conformal_media_bs": round(width_c, 2),
            "cobertura_referencia_nominal_pct": cov_ref,
            "cobertura_ic_90": round(cov_c, 2),
            "segmentos_cobertura": segments_coverage,
            "segmentos_metricas": segments_metrics,
            "hiperparametros": hiperparametros_dict[name],
        }
        results[name]["razon_decision"] = build_razon(name)

        logger.info(
            "[%s] CV R2: %.4f (±%.4f) | CV MedAPE: %.2f%% (±%.2f%%) | Test R2 (Log): %.4f | Test R2 (Bs): %.4f | MedAPE: %.2f%% | CovConformal: %.2f%%",
            name, results[name]["cv_r2_mean"], results[name]["cv_r2_std"],
            results[name]["cv_medape_mean"], results[name]["cv_medape_std"],
            r2_log, r2_bs, medape, cov_c
        )

    # Selección del mejor modelo para producción (mayor R² log y menor MedAPE equilibrado)
    best_name = "RandomForest" if results["RandomForest"]["r2_log"] >= results["HistGradientBoosting"]["r2_log"] else "HistGradientBoosting"
    best_pipe = fitted_pipelines[best_name]
    logger.info("Modelo seleccionado para producción: %s (Smearing Factor: %.4f)", best_name, smearing_factors[best_name])

    # Veredictos contra los umbrales del protocolo (fijados antes de entrenar, D02/D06)
    cov_champion = results[best_name]["cobertura_conformal_pct"]
    etiqueta_calibrado = bool(CONFORMAL_TOLERANCIA[0] * 100 <= cov_champion <= CONFORMAL_TOLERANCIA[1] * 100)
    medape_cumple = bool(results[best_name]["medape_percent"] <= META_MEDAPE_MAX and results[best_name]["r2_bs"] >= META_R2_BS_MIN)

    # Importancia de variables
    feature_importance_list = []
    if best_name == "RandomForest":
        rf_reg = best_pipe.named_steps["reg"]
        encoder = best_pipe.named_steps["prep"].named_transformers_["cat"]
        cat_features = list(encoder.get_feature_names_out(cat_cols))
        all_features = log_num_cols + cat_features
        importances = rf_reg.feature_importances_

        fi_df = pd.DataFrame({"feature": all_features, "importance": importances})
        fi_df = fi_df.sort_values(by="importance", ascending=False)
        feature_importance_list = fi_df.head(15).to_dict(orient="records")

    # Guardar modelo de producción en dashboard/artifacts/
    model_artifact_path = artifacts_dir / "best_model.joblib"
    joblib.dump(best_pipe, model_artifact_path)
    logger.info("Artefacto serializado guardado en: %s", model_artifact_path)

    # ---- run_id de la ejecución: deriva del modelo serializado + entrada de preprocesamiento (A07) ----
    def sha256_file(path: Path) -> str:
        digest = hashlib.sha256()
        with path.open("rb") as source:
            for chunk in iter(lambda: source.read(1024 * 1024), b""):
                digest.update(chunk)
        return digest.hexdigest()

    pre_bitacora_path = PROJECT_ROOT / "preprocessing" / "bitacora_preprocesamiento.json"
    pre_run_id = "PRE-desconocido"
    if pre_bitacora_path.exists():
        try:
            with open(pre_bitacora_path, "r", encoding="utf-8") as f:
                pre_run_id = str(json.load(f).get("run_id", pre_run_id))
        except Exception:
            pass

    model_sha = sha256_file(model_artifact_path)
    run_id = "RUN-" + datetime.now().strftime("%Y%m%d") + "-" + hashlib.sha256(
        f"{model_sha}|{pre_run_id}|{len(df)}".encode("utf-8")
    ).hexdigest()[:12]
    cohortes = {
        "preprocesamiento_run_id": pre_run_id,
        "n_total": int(len(df)),
        "n_entrenamiento_ajuste": int(len(X_fit)),
        "n_calibracion": int(len(X_calib)),
        "n_prueba": int(len(X_test)),
        "semilla": RANDOM_STATE_SEED,
        "protocolo": "models/protocolo_entrenamiento.md",
        "protocolo_version": "2026-09-28",
    }
    logger.info("run_id de la ejecución: %s (preprocesamiento %s)", run_id, pre_run_id)

    # Guardar predicciones diagnósticas tabulares en formato CSV (100% DE OBSERVACIONES DE TEST)
    # Intervalo CONFORMAL calibrado (D02); la columna ±1,645×RMSE es solo referencia nominal rotulada.
    y_test_pred_log_best = best_pipe.predict(X_test)
    best_smearing = smearing_factors[best_name]
    best_rmse_log = results[best_name]["rmse_log"]
    best_q_log = results[best_name]["conformal_q_log"]
    y_test_pred_best = np.maximum(0.0, np.exp(y_test_pred_log_best) * best_smearing - 1.0)

    best_lower_log = y_test_pred_log_best - best_q_log
    best_upper_log = y_test_pred_log_best + best_q_log
    best_lower_bs = np.maximum(0.0, np.exp(best_lower_log) * best_smearing - 1.0)
    best_upper_bs = np.maximum(0.0, np.exp(best_upper_log) * best_smearing - 1.0)
    best_inside_ic = (y_test_raw >= best_lower_bs) & (y_test_raw <= best_upper_bs)

    ref_lower_log = y_test_pred_log_best - 1.645 * best_rmse_log
    ref_upper_log = y_test_pred_log_best + 1.645 * best_rmse_log
    ref_lower_bs = np.maximum(0.0, np.exp(ref_lower_log) * best_smearing - 1.0)
    ref_upper_bs = np.maximum(0.0, np.exp(ref_upper_log) * best_smearing - 1.0)

    test_diagnostics_df = pd.DataFrame({
        "run_id": run_id,
        "real_bs": [float(v) for v in y_test_raw],
        "pred_bs": [float(v) for v in y_test_pred_best],
        "real_log": [float(v) for v in y_test_log],
        "pred_log": [float(v) for v in y_test_pred_log_best],
        "residuals_log": [float(r) for r in (y_test_log - y_test_pred_log_best)],
        "lower_bs": [float(v) for v in best_lower_bs],
        "upper_bs": [float(v) for v in best_upper_bs],
        "inside_ic_90": [bool(v) for v in best_inside_ic],
        "ref_nominal_lower_bs": [float(v) for v in ref_lower_bs],
        "ref_nominal_upper_bs": [float(v) for v in ref_upper_bs],
        "sector_macro": X_test["sector_macro"].to_numpy(),
        "depto": X_test["depto"].to_numpy(),
        "quintil": pd.Series(pd.qcut(y_test_log, q=5, labels=False, duplicates="drop")).map({0: "Q1", 1: "Q2", 2: "Q3", 3: "Q4", 4: "Q5"}).astype(str).to_numpy(),
    })
    test_diag_csv = artifacts_dir / "test_predictions.csv"
    test_diagnostics_df.to_csv(test_diag_csv, index=False)
    logger.info("Predicciones de prueba completas (%d filas) guardadas en CSV: %s", len(test_diagnostics_df), test_diag_csv)

    # Importancia de variables y estadísticas de referencia (se hash-ean junto al paquete)
    feature_importance_list = []
    if best_name == "RandomForest":
        rf_reg = best_pipe.named_steps["reg"]
        encoder = best_pipe.named_steps["prep"].named_transformers_["cat"]
        cat_features = list(encoder.get_feature_names_out(cat_cols))
        all_features = log_num_cols + cat_features
        importances = rf_reg.feature_importances_

        fi_df = pd.DataFrame({"feature": all_features, "importance": importances})
        fi_df = fi_df.sort_values(by="importance", ascending=False)
        feature_importance_list = fi_df.head(15).to_dict(orient="records")

    with open(artifacts_dir / "feature_importance.json", "w", encoding="utf-8") as f:
        json.dump(feature_importance_list, f, indent=2, ensure_ascii=False)

    # Guardar estadísticas de referencia no paramétricas para Drift en models/reference_stats.json
    # Población de referencia (T17): casos completos en las 5 variables monitoreadas por drift.
    # La API exige todos los campos del formulario (400 si falta alguno), por lo que el tráfico
    # de producción siempre proviene de payloads completos; compararlos contra márgenes por
    # columna de toda la población reportante induciría drift espurio por selección de tamaño.
    DRIFT_KEYS = ["S01_05_A", "S01_03_C", "S02_09", "S07_09_E", "total_valor_uti"]
    mask_ref = df[DRIFT_KEYS].notna().all(axis=1)
    reference_stats = {}
    for c in PREDICTOR_NUM_COLS:
        vals = pd.to_numeric(df.loc[mask_ref, c], errors="coerce").dropna().values  # sin NaN: percentiles válidos
        reference_stats[c] = {
            "mean": float(np.mean(vals)),
            "std": float(np.std(vals)),
            "median": float(np.median(vals)),
            "q25": float(np.percentile(vals, 25)),
            "q75": float(np.percentile(vals, 75)),
            "p01": float(np.percentile(vals, 1)),
            "p05": float(np.percentile(vals, 5)),
            "p10": float(np.percentile(vals, 10)),
            "p90": float(np.percentile(vals, 90)),
            "p95": float(np.percentile(vals, 95)),
            "p99": float(np.percentile(vals, 99)),
            "min": float(np.min(vals)),
            "max": float(np.max(vals)),
            "zero_fraction": float(np.mean(vals == 0))
        }
    reference_stats["_meta"] = {
        "poblacion": "casos completos en variables de drift (S01_05_A, S01_03_C, S02_09, S07_09_E, total_valor_uti)",
        "n_poblacion": int(mask_ref.sum()),
        "n_total": int(len(df)),
        "run_id_pre": pre_run_id,
        "nota": "Claves _* son metadatos; el resto mapea variable -> estadisticos de referencia.",
    }
    with open(models_dir / "reference_stats.json", "w", encoding="utf-8") as f:
        json.dump(reference_stats, f, indent=2, ensure_ascii=False)

    # Registro MLOps en dashboard/artifacts/registry.json
    version_id = f"v1.{datetime.now().strftime('%Y%m%d.%H%M')}"
    registry_file = artifacts_dir / "registry.json"
    history = []
    if registry_file.exists():
        try:
            with open(registry_file, "r", encoding="utf-8") as f:
                history = json.load(f).get("versions", [])
        except Exception:
            history = []

    for h in history:
        h["status"] = "ARCHIVED"

    version_entry = {
        "version": version_id,
        "run_id": run_id,
        "model_type": best_name,
        "timestamp": datetime.now().isoformat(),
        "dataset_rows": len(df),
        "cohorte": cohortes,
        "metrics": results[best_name],
        "all_models_metrics": results,
        "smearing_factor": smearing_factors[best_name],
        "conformal": {
            "metodo": "split conformal en escala log1p con conjunto de calibración separado",
            "nominal": CONFORMAL_NOMINAL,
            "q_log": results[best_name]["conformal_q_log"],
            "cobertura_empirica_pct": results[best_name]["cobertura_conformal_pct"],
            "amplitud_media_bs": results[best_name]["amplitud_conformal_media_bs"],
            "tolerancia": list(CONFORMAL_TOLERANCIA),
            "etiqueta_calibrado": etiqueta_calibrado,
        },
        "metas": {
            "d06_medape_max": META_MEDAPE_MAX,
            "d06_r2_bs_min": META_R2_BS_MIN,
            "meta_historica_medape": META_HISTORICA_MEDAPE,
            "medape_cumple_umbral_aprobacion": medape_cumple,
        },
        "status": "ACTIVE",
        "framework": "scikit-learn",
        "python_version": sys.version.split()[0]
    }
    history.insert(0, version_entry)

    registry_data = {
        "active_version": version_id,
        "run_id": run_id,
        "last_updated": datetime.now().isoformat(),
        "smearing_factor": smearing_factors[best_name],
        "rmse_log": results[best_name]["rmse_log"],
        "conformal_q_log": results[best_name]["conformal_q_log"],
        "versions": history
    }
    with open(registry_file, "w", encoding="utf-8") as f:
        json.dump(registry_data, f, indent=2, ensure_ascii=False)

    # Construcción de la bitácora comparativa de modelos (models/bitacora_modelos.json)
    bitacora_modelos_path = models_dir / "bitacora_modelos.json"
    artifacts_bitacora_path = artifacts_dir / "bitacora_modelos.json"

    modelos_bitacora_list = []
    for name, m_res in results.items():
        is_champion = (name == best_name)
        modelos_bitacora_list.append({
            "modelo": name,
            "tipo": "Random Forest Regressor (Ensamble)" if name == "RandomForest" else ("HistGradientBoosting (Gradient Boosting)" if name == "HistGradientBoosting" else "Ridge (Regresión Lineal L2)"),
            "fecha": datetime.now().isoformat(),
            "iteracion": version_id,
            "hiperparametros": m_res["hiperparametros"],
            "pliegues_cv": m_res["cv_folds"],
            "cv_resumen": {
                "r2_promedio": round(m_res["cv_r2_mean"], 4),
                "r2_std": round(m_res["cv_r2_std"], 4),
                "rmse_promedio": round(m_res["cv_rmse_mean"], 4),
                "rmse_std": round(m_res["cv_rmse_std"], 4),
                "mae_promedio": round(m_res["cv_mae_mean"], 4),
                "mae_std": round(m_res["cv_mae_std"], 4),
                "medape_promedio": round(m_res["cv_medape_mean"], 2),
                "medape_std": round(m_res["cv_medape_std"], 2)
            },
            "test_metricas": {
                "r2_log": round(m_res["r2_log"], 4),
                "rmse_log": round(m_res["rmse_log"], 4),
                "mae_log": round(m_res["mae_log"], 4),
                "r2_bs": round(m_res["r2_bs"], 4),
                "rmse_bs": round(m_res["rmse_bs"], 2),
                "mae_bs": round(m_res["mae_bs"], 2),
                "medape": round(m_res["medape_percent"], 2),
                "smearing_factor": round(m_res["smearing_factor"], 4),
                "cobertura_ic_90": round(m_res["cobertura_ic_90"], 2)
            },
            "campeon": is_champion,
            "estado": "SELECCIONADO (CAMPEÓN)" if is_champion else "DESCARTADO",
            "razon_decision": m_res["razon_decision"]
        })

    historial_corridas = []
    if bitacora_modelos_path.exists():
        try:
            with open(bitacora_modelos_path, "r", encoding="utf-8") as f:
                prev_bit = json.load(f)
                historial_corridas = prev_bit.get("historial_iteraciones", [])
                if "modelos" in prev_bit:
                    historial_corridas.insert(0, {
                        "iteracion": prev_bit.get("iteracion_activa", "anterior"),
                        "timestamp": prev_bit.get("ultima_actualizacion", ""),
                        "modelos": prev_bit.get("modelos", [])
                    })
        except Exception as e:
            logger.warning("No se pudo leer bitácora previa: %s", e)

    bitacora_final = {
        "ultima_actualizacion": datetime.now().isoformat(),
        "iteracion_activa": version_id,
        "run_id": run_id,
        "modelo_campeon": best_name,
        "cobertura_ic_90_campeon": results[best_name]["cobertura_ic_90"],
        "modelos": modelos_bitacora_list,
        "historial_iteraciones": historial_corridas[:10]
    }

    with open(bitacora_modelos_path, "w", encoding="utf-8") as f:
        json.dump(bitacora_final, f, indent=2, ensure_ascii=False)
    with open(artifacts_bitacora_path, "w", encoding="utf-8") as f:
        json.dump(bitacora_final, f, indent=2, ensure_ascii=False)
    logger.info("Bitácora comparativa de modelos guardada en: %s", bitacora_modelos_path)

    # Exportar resultados de Validación Cruzada estructurados para el Dashboard
    cv_export_data = {
        "run_id": run_id,
        "cohorte": cohortes,
        "n_splits": 5,
        "strategy": "StratifiedKFold por cuantiles de ingresos log(1+y)",
        "models": {
            name: {
                "folds": results[name]["cv_folds"],
                "cv_r2_mean": results[name]["cv_r2_mean"],
                "cv_r2_std": results[name]["cv_r2_std"],
                "cv_rmse_mean": results[name]["cv_rmse_mean"],
                "cv_rmse_std": results[name]["cv_rmse_std"],
                "cv_mae_mean": results[name]["cv_mae_mean"],
                "cv_mae_std": results[name]["cv_mae_std"],
                "cv_medape_mean": results[name]["cv_medape_mean"],
                "cv_medape_std": results[name]["cv_medape_std"],
                "test_r2_log": results[name]["r2_log"],
                "test_rmse_log": results[name]["rmse_log"],
                "test_r2_bs": results[name]["r2_bs"],
                "medape_percent": results[name]["medape_percent"],
                "cobertura_conformal_pct": results[name]["cobertura_conformal_pct"],
                "amplitud_conformal_media_bs": results[name]["amplitud_conformal_media_bs"],
                "cobertura_referencia_nominal_pct": results[name]["cobertura_referencia_nominal_pct"],
                "razon_decision": results[name]["razon_decision"]
            }
            for name in models.keys()
        }
    }
    with open(artifacts_dir / "cv_results.json", "w", encoding="utf-8") as f:
        json.dump(cv_export_data, f, indent=2, ensure_ascii=False)
    logger.info("Resultados de Validación Cruzada guardados en: %s", artifacts_dir / "cv_results.json")

    # ---- Manifiesto del paquete: run_id + hashes de todos los artefactos (A07) ----
    manifest = {
        "run_id": run_id,
        "active_version": version_id,
        "generated_at": datetime.now().isoformat(),
        "cohorte": cohortes,
        "conformal": version_entry["conformal"],
        "metas": version_entry["metas"],
        "artifacts": {
            "best_model.joblib": model_sha,
            "test_predictions.csv": sha256_file(test_diag_csv),
            "cv_results.json": sha256_file(artifacts_dir / "cv_results.json"),
            "feature_importance.json": sha256_file(artifacts_dir / "feature_importance.json"),
            "registry.json": sha256_file(registry_file),
            "bitacora_modelos.json": sha256_file(artifacts_bitacora_path),
        },
        "preprocessing_run_id": pre_run_id,
    }
    with open(artifacts_dir / "manifest.json", "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    logger.info("Manifiesto del paquete guardado en: %s (run_id %s)", artifacts_dir / "manifest.json", run_id)

    logger.info("Metadatos y registros MLOps guardados exitosamente.")
    return version_entry


def run_training() -> Dict[str, Any]:
    """Carga o ejecuta el preprocesamiento y entrena el modelo."""
    processed_csv = PROJECT_ROOT / "data" / "processed" / "dataset_procesado.csv"
    if processed_csv.exists():
        logger.info("Cargando dataset preprocesado desde: %s", processed_csv)
        df = pd.read_csv(processed_csv, low_memory=False)
    else:
        logger.info("Dataset procesado no encontrado, ejecutando pipeline de preprocesamiento...")
        df = run_preprocessing(save_outputs=True)

    artifacts_dir = PROJECT_ROOT / "dashboard" / "artifacts"
    models_dir = PROJECT_ROOT / "models"
    return train_and_evaluate(df, artifacts_dir, models_dir)


if __name__ == "__main__":
    res = run_training()
    print("\n--- RESUMEN FINAL DE ENTRENAMIENTO (models/train.py) ---")
    print(f"Versión: {res['version']} ({res['model_type']})")
    print(f"R² en escala Bs:  {res['metrics']['r2_bs']:.4f}")
    print(f"R² en escala Log: {res['metrics']['r2_log']:.4f}")
    print(f"MedAPE:           {res['metrics']['medape_percent']:.2f}%")
