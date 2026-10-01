"""Prueba A10 complementaria: trafico REALISTA (muestreado del dataset procesado).

Espera: el drift NO debe dispararse (la mayoria de variables en ESTABLE),
demostrando que el detector no produce falsos positivos ante trafico tipico.
"""
import json
import sys
import urllib.request
from pathlib import Path

import pandas as pd

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE = "http://127.0.0.1:5055"
ROOT = Path(__file__).resolve().parents[2]
df = pd.read_csv(ROOT / "data/processed/dataset_procesado.csv", low_memory=False)

need = ["S01_05_A", "S01_03_C", "S01_14", "S02_09", "S07_09_E", "S06_06_B",
        "n_insumos", "total_valor_co", "total_valor_uti", "depto", "sector_macro"]
# Escenario SIN drift: solo empresas que reportan todos los campos (casos completos).
# Enviar 0.0 por campos no reportados inyectaria una masa de ceros ajena a la
# referencia (que representa valores REPORTADOS) y dispararia drift por construccion.
sample = df[need].dropna(subset=["S01_05_A", "S01_03_C", "S02_09", "S07_09_E", "total_valor_uti"]).sample(n=120, random_state=42)

ok = 0
for _, row in sample.iterrows():
    payload = {
        "personal": max(1.0, float(row["S01_05_A"])),
        "sueldos": max(0.0, float(row["S01_03_C"])),
        "remuneraciones": max(0.0, float(row["S01_14"] or 0.0)),
        "energia": max(0.0, float(row["S02_09"] or 0.0)),
        "activos": max(0.0, float(row["S07_09_E"] or 0.0)),
        "inventarios": max(0.0, float(row["S06_06_B"] or 0.0)),
        "n_insumos": max(0.0, float(row["n_insumos"] or 0.0)),
        "total_valor_co": max(0.0, float(row["total_valor_co"] or 0.0)),
        "total_valor_uti": max(0.0, float(row["total_valor_uti"] or 0.0)),
        "depto": str(row["depto"]).strip().upper(),
        "sector_macro": str(row["sector_macro"]),
    }
    req = urllib.request.Request(
        f"{BASE}/api/predict", data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"}, method="POST")
    try:
        urllib.request.urlopen(req, timeout=15).read()
        ok += 1
    except Exception as exc:  # registrar y continuar
        print("FALLO:", exc)

print(f"Peticiones OK: {ok}/120")

req = urllib.request.Request(
    f"{BASE}/api/mlops/drift", data=json.dumps({"ventana_horas": 24}).encode(),
    headers={"Content-Type": "application/json"}, method="POST")
dr = json.load(urllib.request.urlopen(req, timeout=30))["drift_results"]
print("DRIFT modo:", dr.get("__modo__"))
print("Nota:", dr.get("__nota__"))
estables, en_drift, sin_datos = [], [], []
for key in ["S01_05_A", "S01_03_C", "S02_09", "S07_09_E", "total_valor_uti"]:
    r = dr.get(key)
    if not r or r.get("status") == "SIN DATOS":
        sin_datos.append(key)
    elif r.get("drift_detected"):
        en_drift.append(f"{key}(p={r.get('p_value')})")
    else:
        estables.append(f"{key}(p={r.get('p_value')})")
print("ESTABLE:", ", ".join(estables) or "-")
print("DRIFT:", ", ".join(en_drift) or "-")
print("SIN DATOS:", ", ".join(sin_datos) or "-")
