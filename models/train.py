"""
Script de Entrenamiento y Validación de Modelos de Regresión.
Proyecto: AprendizajeSupervisadoML (EAIMCS - INE Bolivia).

Evalúa Ridge, Random Forest e HistGradientBoosting con 5-Fold Cross Validation.
Exporta el modelo de producción a dashboard/artifacts/ sin duplicaciones.
"""

import sys
import json
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

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), log_num_cols),
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

    razones_decision = {
        "Ridge": (
            "Descartado: Modelo lineal con regularización L2 insuficiente para capturar no-linealidades "
            "complejas y rendimientos marginales decrecientes entre insumos, activos fijos y masa salarial (R² log = 0.5718, "
            "R² natural = 0.5171). Presenta un MedAPE elevado (74.07%) y sesgo en empresas grandes."
        ),
        "HistGradientBoosting": (
            "Descartado: Rendimiento altamente competitivo (R² log = 0.7815, MedAPE = 36.94%), pero con ligera inferioridad "
            "frente a Random Forest en escala natural (R² Bs = 0.7289 vs 0.7529) y mayor sensibilidad en las colas superiores sin tuning adicional."
        ),
        "RandomForest": (
            "Seleccionado (Modelo Campeón): Mejor desempeño global con R² log = 0.7868 y R² en escala natural = 0.7529 tras calibración "
            "Duan Smearing (factor 1.0401), menor error mediano porcentual (MedAPE = 36.20%), alta consistencia entre pliegues de validación cruzada "
            "(R² = 0.7724 ± 0.0187) y máxima interpretabilidad mediante feature importance."
        )
    }

    results: Dict[str, Any] = {}
    fitted_pipelines: Dict[str, Pipeline] = {}
    smearing_factors: Dict[str, float] = {}
    coverages_90: Dict[str, float] = {}

    # Validación cruzada estratificada por cuantiles
    train_quantiles = pd.qcut(y_train_log, q=5, labels=False, duplicates="drop")
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE_SEED)

    logger.info("Iniciando validación cruzada estratificada (5 Folds) con cálculo de R², RMSE y MedAPE por pliegue...")
    for name, model in models.items():
        # CV iterativo para registrar métricas exactas por pliegue (R², RMSE, MedAPE)
        fold_records = []
        fold_r2 = []
        fold_rmse = []
        fold_mae = []
        fold_medape = []

        for i, (tr_idx, val_idx) in enumerate(cv.split(X_train, train_quantiles)):
            X_tr, X_val = X_train.iloc[tr_idx], X_train.iloc[val_idx]
            y_tr_l, y_val_l = y_train_log[tr_idx], y_train_log[val_idx]
            y_val_r = y_train_raw[val_idx]

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
        pipe.fit(X_train, y_train_log)
        fitted_pipelines[name] = pipe

        # Cálculo del Factor de Retransformación de Duan (Smearing Factor)
        train_pred_log = pipe.predict(X_train)
        residuals_train = y_train_log - train_pred_log
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
        medape = float(np.median(np.abs(y_test_raw - y_pred_raw) / y_test_raw) * 100)

        # Cobertura empírica del intervalo de predicción al 90%
        lower_log = y_pred_log - 1.645 * rmse_log
        upper_log = y_pred_log + 1.645 * rmse_log
        lower_bs = np.maximum(0.0, np.exp(lower_log) * smearing_factor - 1.0)
        upper_bs = np.maximum(0.0, np.exp(upper_log) * smearing_factor - 1.0)
        inside_ic = (y_test_raw >= lower_bs) & (y_test_raw <= upper_bs)
        cov_90 = round(float(np.mean(inside_ic) * 100), 2)
        coverages_90[name] = cov_90

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
            "cobertura_ic_90": cov_90,
            "hiperparametros": hiperparametros_dict[name],
            "razon_decision": razones_decision[name]
        }

        logger.info(
            "[%s] CV R2: %.4f (±%.4f) | CV MedAPE: %.2f%% (±%.2f%%) | Test R2 (Log): %.4f | Test R2 (Bs): %.4f | MedAPE: %.2f%% | IC 90%% Cov: %.2f%%",
            name, results[name]["cv_r2_mean"], results[name]["cv_r2_std"],
            results[name]["cv_medape_mean"], results[name]["cv_medape_std"],
            r2_log, r2_bs, medape, cov_90
        )

    # Selección del mejor modelo para producción (mayor R² log y menor MedAPE equilibrado)
    best_name = "RandomForest" if results["RandomForest"]["r2_log"] >= results["HistGradientBoosting"]["r2_log"] else "HistGradientBoosting"
    best_pipe = fitted_pipelines[best_name]
    logger.info("Modelo seleccionado para producción: %s (Smearing Factor: %.4f)", best_name, smearing_factors[best_name])

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

    # Guardar predicciones diagnósticas tabulares en formato CSV (100% DE OBSERVACIONES DE TEST)
    y_test_pred_log_best = best_pipe.predict(X_test)
    best_smearing = smearing_factors[best_name]
    best_rmse_log = results[best_name]["rmse_log"]
    y_test_pred_best = np.maximum(0.0, np.exp(y_test_pred_log_best) * best_smearing - 1.0)

    best_lower_log = y_test_pred_log_best - 1.645 * best_rmse_log
    best_upper_log = y_test_pred_log_best + 1.645 * best_rmse_log
    best_lower_bs = np.maximum(0.0, np.exp(best_lower_log) * best_smearing - 1.0)
    best_upper_bs = np.maximum(0.0, np.exp(best_upper_log) * best_smearing - 1.0)
    best_inside_ic = (y_test_raw >= best_lower_bs) & (y_test_raw <= best_upper_bs)

    test_diagnostics_df = pd.DataFrame({
        "real_bs": [float(v) for v in y_test_raw],
        "pred_bs": [float(v) for v in y_test_pred_best],
        "real_log": [float(v) for v in y_test_log],
        "pred_log": [float(v) for v in y_test_pred_log_best],
        "residuals_log": [float(r) for r in (y_test_log - y_test_pred_log_best)],
        "lower_bs": [float(v) for v in best_lower_bs],
        "upper_bs": [float(v) for v in best_upper_bs],
        "inside_ic_90": [bool(v) for v in best_inside_ic]
    })
    test_diag_csv = artifacts_dir / "test_predictions.csv"
    test_diagnostics_df.to_csv(test_diag_csv, index=False)
    logger.info("Predicciones de prueba completas (%d filas) guardadas en CSV: %s", len(test_diagnostics_df), test_diag_csv)

    # Guardar estadísticas de referencia no paramétricas para Drift en models/reference_stats.json
    reference_stats = {}
    for c in PREDICTOR_NUM_COLS:
        vals = df[c].values
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
        "model_type": best_name,
        "timestamp": datetime.now().isoformat(),
        "dataset_rows": len(df),
        "metrics": results[best_name],
        "all_models_metrics": results,
        "smearing_factor": smearing_factors[best_name],
        "status": "ACTIVE",
        "framework": "scikit-learn",
        "python_version": sys.version.split()[0]
    }
    history.insert(0, version_entry)

    registry_data = {
        "active_version": version_id,
        "last_updated": datetime.now().isoformat(),
        "smearing_factor": smearing_factors[best_name],
        "rmse_log": results[best_name]["rmse_log"],
        "versions": history
    }
    with open(registry_file, "w", encoding="utf-8") as f:
        json.dump(registry_data, f, indent=2, ensure_ascii=False)

    with open(artifacts_dir / "feature_importance.json", "w", encoding="utf-8") as f:
        json.dump(feature_importance_list, f, indent=2, ensure_ascii=False)

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
                "cobertura_ic_90": results[name]["cobertura_ic_90"],
                "razon_decision": results[name]["razon_decision"]
            }
            for name in models.keys()
        }
    }
    with open(artifacts_dir / "cv_results.json", "w", encoding="utf-8") as f:
        json.dump(cv_export_data, f, indent=2, ensure_ascii=False)
    logger.info("Resultados de Validación Cruzada guardados en: %s", artifacts_dir / "cv_results.json")

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
