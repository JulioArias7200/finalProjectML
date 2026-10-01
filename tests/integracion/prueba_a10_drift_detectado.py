import json
import sys
import time
import urllib.request

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE = "http://127.0.0.1:5055"


def post(path, payload, timeout=10):
    req = urllib.request.Request(
        BASE + path, data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"}, method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.load(r)


def get(path, timeout=10):
    with urllib.request.urlopen(BASE + path, timeout=timeout) as r:
        return json.load(r)


payload = {
    "personal": 45, "sueldos": 3200000.0, "remuneraciones": 900000.0,
    "energia": 210000.0, "activos": 18000000.0, "inventarios": 2100000.0,
    "n_insumos": 8, "total_valor_co": 9500000.0, "total_valor_uti": 9100000.0,
    "depto": "LA PAZ", "sector_macro": "Industria Manufacturera",
}
payload2 = dict(payload, sueldos=5200000.0, activos=45000000.0,
                total_valor_uti=21000000.0, total_valor_co=22000000.0)

t0 = time.time()
for i in range(24):
    try:
        post("/api/predict", payload if i % 2 else payload2)
    except Exception as exc:
        print(f"FALLO predict {i}: {exc}")
        break
print(f"24 predicciones en {time.time() - t0:.1f}s")

mon = get("/api/mlops/monitoring")
print("MONITOREO:", mon["status"], "| n_ventana:", mon.get("n_ventana"),
      "| lat_media:", mon.get("avg_latency_ms"), "| p95:", mon.get("p95_latency_ms"),
      "| errores%:", mon.get("error_rate_pct"), "| fuente:", mon.get("fuente"))

drift_body = post("/api/mlops/drift", {"ventana_horas": 24})
dr = drift_body["drift_results"]
print("DRIFT modo:", dr.get("__modo__"), "|", dr.get("__nota__", "")[:90])
for k in ["S01_03_C", "S07_09_E", "total_valor_uti"]:
    if k in dr:
        print(" ", k, "| n:", dr[k].get("n_produccion"), "| p:", dr[k].get("p_value"), "|", dr[k].get("status"))
