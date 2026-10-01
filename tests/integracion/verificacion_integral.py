"""Verificación integral E2E (T18 · A11).

Ejecución (desde la raíz, con el paquete activo):
    venv/Scripts/python.exe tests/integracion/verificacion_integral.py

Comprueba, sin servidor:
1. Integridad del paquete (manifest.json vs SHA-256 reales, mismo run_id, versión activa).
2. Recálculo de métricas desde test_predictions.csv (R² log/Bs, MedAPE, cobertura conformal).
3. Umbrales predefinidos: D06 (MedAPE <= 40) y D02 (cobertura en [85, 95]).
4. Referencia de drift coherente con la población de tráfico (casos completos, _meta presente).
"""
import hashlib
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.metrics import median_absolute_error, r2_score

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[2]
ART = ROOT / "dashboard" / "artifacts"

fallos = 0


def check(nombre: str, cond: bool, detalle: str = "") -> None:
    global fallos
    print(f"{'PASS' if cond else 'FAIL'}  {nombre}" + (f"  [{detalle}]" if detalle else ""))
    if not cond:
        fallos += 1


# ---- 1. Integridad del paquete -------------------------------------------------
manifest = json.loads((ART / "manifest.json").read_text(encoding="utf-8"))
run_id = manifest["run_id"]
print(f"Paquete: version={manifest.get('active_version')} run_id={run_id}")
for name, expected in manifest.get("artifacts", {}).items():
    p = ART / name
    if not p.exists():
        check(f"hash {name}", False, "archivo ausente")
        continue
    digest = hashlib.sha256(p.read_bytes()).hexdigest()
    check(f"hash {name}", digest == expected)

registry = json.loads((ART / "registry.json").read_text(encoding="utf-8"))
check("registry.active_version == manifest.active_version",
      registry.get("active_version") == manifest.get("active_version"))
check("registry.run_id == manifest.run_id", registry.get("run_id") == run_id)

bitacora = json.loads((ROOT / "models" / "bitacora_modelos.json").read_text(encoding="utf-8"))
check("bitacora.run_id == manifest.run_id", bitacora.get("run_id") == run_id)

# ---- 2. Recálculo de métricas --------------------------------------------------
preds = pd.read_csv(ART / "test_predictions.csv", low_memory=False)
check("run_id en todas las filas", set(preds["run_id"].unique()) == {run_id})
real_log = preds["real_log"].to_numpy(dtype=float)
pred_log = preds["pred_log"].to_numpy(dtype=float)
real_bs = preds["real_bs"].to_numpy(dtype=float)
pred_bs = preds["pred_bs"].to_numpy(dtype=float)
r2_log = r2_score(real_log, pred_log)
r2_bs = r2_score(real_bs, pred_bs)
medape = float(np.median(np.abs(real_bs - pred_bs) / real_bs) * 100)
cov = float(preds["inside_ic_90"].mean() * 100)
ref_cov = float(((preds["real_bs"] >= preds["ref_nominal_lower_bs"]) &
                 (preds["real_bs"] <= preds["ref_nominal_upper_bs"])).mean() * 100)
print(f"Métricas recalculadas: R2log={r2_log:.4f} R2Bs={r2_bs:.4f} MedAPE={medape:.2f}% "
      f"cobertura_conformal={cov:.2f}% cobertura_referencia={ref_cov:.2f}%")

# ---- 3. Umbrales predefinidos (D02/D06) -----------------------------------------
check("D06: MedAPE <= 40%", medape <= 40.0, f"{medape:.2f}%")
check("D02: cobertura conformal en [85, 95]", 85.0 <= cov <= 95.0, f"{cov:.2f}%")

# ---- 4. Referencia de drift ------------------------------------------------------
ref = json.loads((ROOT / "models" / "reference_stats.json").read_text(encoding="utf-8"))
meta = ref.get("_meta", {})
check("referencia drift con _meta (poblacion casos completos)",
      bool(meta) and meta.get("n_poblacion") == 1614 and meta.get("run_id_pre") is not None,
      f"n={meta.get('n_poblacion')}/{meta.get('n_total')}")

print("=" * 60)
print(f"RESULTADO: {'TODO OK' if fallos == 0 else f'{fallos} fallos'}")
sys.exit(0 if fallos == 0 else 1)
