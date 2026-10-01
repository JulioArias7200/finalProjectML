"""Telemetría real persistida del dashboard (A10).

Registro JSONL append-only de peticiones a /api/predict: timestamp, latencia,
estado e insumos crudos (sin identificadores empresariales). Alimenta el
monitoreo de tráfico y el drift real con ventana y N. Sin registros, el
dashboard muestra "sin telemetría" en lugar de series simuladas.
"""

from __future__ import annotations

import json
import threading
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict, List, Optional

import numpy as np
import pandas as pd
from scipy.stats import ks_2samp, wasserstein_distance

PROJECT_ROOT = Path(__file__).resolve().parents[1]
TELEMETRY_PATH = PROJECT_ROOT / "dashboard" / "telemetry.jsonl"
MAX_RECORDS = 5000
MAX_FEATURE_ROWS = 5000

_lock = threading.Lock()


def append_prediction_record(record: Dict[str, Any]) -> None:
    """Añade un registro de petición a /api/predict de forma atómica (append JSONL)."""
    entry = {
        "timestamp": record.get("timestamp") or datetime.now().isoformat(),
        "origen": "predict",
        "status": record.get("status", "200 OK"),
        "latency_ms": float(record.get("latency_ms", 0.0)),
        "features": record.get("features", {}),
    }
    line = json.dumps(entry, ensure_ascii=False)
    with _lock:
        with TELEMETRY_PATH.open("a", encoding="utf-8") as sink:
            sink.write(line + "\n")
    _trim_if_needed()


def _trim_if_needed() -> None:
    """Mantiene el archivo acotado conservando los registros más recientes."""
    try:
        with _lock:
            lines = TELEMETRY_PATH.read_text(encoding="utf-8").splitlines()
            if len(lines) > MAX_RECORDS:
                TELEMETRY_PATH.write_text("\n".join(lines[-MAX_RECORDS:]) + "\n", encoding="utf-8")
    except OSError:
        pass


def load_records(window_hours: Optional[int] = None) -> List[Dict[str, Any]]:
    """Lee la telemetría real; opcionalmente filtrada a una ventana en horas."""
    if not TELEMETRY_PATH.exists():
        return []
    records: List[Dict[str, Any]] = []
    with _lock:
        with TELEMETRY_PATH.open("r", encoding="utf-8") as source:
            for line in source:
                line = line.strip()
                if not line:
                    continue
                try:
                    records.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
    if window_hours is not None:
        cutoff = datetime.now() - timedelta(hours=window_hours)
        filtered = []
        for r in records:
            try:
                if datetime.fromisoformat(r["timestamp"]) >= cutoff:
                    filtered.append(r)
            except (KeyError, ValueError):
                continue
        return filtered
    return records


def traffic_summary(window_hours: int = 24) -> Dict[str, Any]:
    """Resumen real de tráfico con ventana y N visibles; vacío → 'sin telemetría'."""
    records = load_records(window_hours=window_hours)
    if len(records) < 3:
        return {"status": "SIN TELEMETRÍA", "n_ventana": len(records)}
    latencies = [r.get("latency_ms", 0.0) for r in records]
    errores = sum(1 for r in records if str(r.get("status", "")).startswith(("4", "5")))
    by_hour: Dict[str, int] = {}
    for r in records:
        hour_label = str(r.get("timestamp", ""))[:13] + ":00"
        by_hour[hour_label] = by_hour.get(hour_label, 0) + 1
    return {
        "status": "OPERATIVO",
        "ventana_horas": window_hours,
        "n_ventana": len(records),
        "total_requests": len(records),
        "avg_latency_ms": round(float(np.mean(latencies)), 2),
        "p95_latency_ms": round(float(np.percentile(latencies, 95)), 2),
        "error_rate_pct": round(errores / len(records) * 100, 2),
        "by_hour": [{"hour": k, "requests": v} for k, v in sorted(by_hour.items())],
        "fuente": "telemetry.jsonl (peticiones reales a /api/predict)",
    }


def real_drift_check(reference_stats: Dict[str, Dict[str, Any]], window_hours: int = 168) -> Dict[str, Any]:
    """
    Drift REAL (T17): compara la distribución de insumos registrados en telemetría
    contra las estadísticas de referencia versionadas del modelo activo.
    Sin muestras suficientes por variable devuelve 'sin datos' con N=0.
    """
    records = load_records(window_hours=window_hours)
    rows = [r.get("features", {}) for r in records if r.get("features")]
    results: Dict[str, Any] = {
        "__modo__": "real" if len(rows) >= 30 else "sin datos",
        "__nota__": (
            f"Comparación de {len(rows)} registros reales de telemetría (ventana {window_hours}h) "
            "contra la referencia versionada del paquete activo." if len(rows) >= 30
            else "Aún no hay tráfico suficiente (≥30 registros) para medir deriva real."
        ),
        "ventana_horas": window_hours,
    }
    alpha_bonferroni = 0.05 / 5
    if len(rows) < 30:
        return results
    df = pd.DataFrame(rows).apply(pd.to_numeric, errors="coerce")
    for key in ["S01_05_A", "S01_03_C", "S02_09", "S07_09_E", "total_valor_uti"]:
        ref = reference_stats.get(key)
        sample = df[key].dropna().to_numpy(dtype=float) if key in df.columns else np.array([])
        if ref is None or sample.size < 30:
            results[key] = {"label": key, "status": "SIN DATOS", "n_produccion": int(sample.size)}
            continue
        # Referencia: percentiles versionados; producción: insumos reales registrados
        p_points = [0.01, 0.05, 0.10, 0.25, 0.50, 0.75, 0.90, 0.95, 0.99]
        v_points = np.maximum.accumulate(np.array([
            ref.get("p01", ref.get("min", 0.0)), ref.get("p05", ref.get("min", 0.0)),
            ref.get("p10", ref.get("q25", 0.0)), ref.get("q25", ref.get("median", 0.0)),
            ref.get("median", ref.get("mean", 1.0)), ref.get("q75", ref.get("mean", 2.0)),
            ref.get("p90", ref.get("max", 5.0)), ref.get("p95", ref.get("max", 10.0)),
            ref.get("p99", ref.get("max", 20.0)),
        ], dtype=float))
        u = np.linspace(0.01, 0.99, num=max(len(sample), 450))
        base_sample = np.interp(u, p_points, v_points)
        ks_res = ks_2samp(base_sample, sample)
        p_val = float(ks_res.pvalue)
        results[key] = {
            "label": key,
            "n_produccion": int(sample.size),
            "ventana_horas": window_hours,
            "ks_stat": round(float(ks_res.statistic), 4),
            "p_value": round(p_val, 4),
            "wasserstein_dist": round(float(wasserstein_distance(base_sample, sample)), 2),
            "alpha_threshold": alpha_bonferroni,
            "drift_detected": bool(p_val < alpha_bonferroni),
            "status": "DRIFT DETECTADO" if p_val < alpha_bonferroni else "ESTABLE",
        }
    return results
