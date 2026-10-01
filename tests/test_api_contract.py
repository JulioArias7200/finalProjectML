"""Pruebas del contrato de API (A07-A08); ejecutan Flask en modo testing contra el paquete real."""

import json
import sys
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from dashboard.app import app, ACCESO_INDIVIDUAL_HABILITADO, PACKAGE_STATE  # noqa: E402


class ApiContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app.config["TESTING"] = True
        cls.client = app.test_client()

    def test_00_package_loaded_successfully(self):
        # Orden 00: si el paquete local no está íntegro, el resto de la suite no tiene sentido.
        self.assertTrue(PACKAGE_STATE["ready"], PACKAGE_STATE["error"])

    def test_meta_contract_in_analytic_responses(self):
        for endpoint in ["/api/kpis", "/api/eda/heatmap_depto_sector", "/api/models", "/api/cross_validation", "/api/mlops"]:
            res = self.client.get(endpoint)
            self.assertEqual(res.status_code, 200, endpoint)
            payload = res.get_json()
            self.assertIn("meta", payload, endpoint)
            meta = payload["meta"]
            for key in ["run_id", "dataset_id", "periodo", "poblacion", "n", "unidad", "escala", "generated_at", "limitaciones"]:
                self.assertIn(key, meta, f"{endpoint} sin meta.{key}")
            self.assertTrue(str(meta["run_id"]).startswith("RUN-"))
            self.assertIn("sin expansión", meta["poblacion"])

    def test_mlops_window_metadata_matches_active_package(self):
        res = self.client.get("/api/mlops")
        self.assertEqual(res.status_code, 200)
        body = res.get_json()
        self.assertEqual(body["run_id"], PACKAGE_STATE["run_id"])
        self.assertEqual(body["active_version"], body["history"][0]["version"])
        self.assertEqual(body["model_type"], body["history"][0]["model_type"])
        self.assertIsNotNone(body["smearing_factor"])
        self.assertIsNotNone(body["conformal"]["cobertura_empirica_pct"])

    def test_kpis_share_denominator_with_heatmap_for_same_filter(self):
        query = "sector=Comercio%20Mayorista%20y%20Minorista"
        kpis = self.client.get(f"/api/kpis?{query}").get_json()
        heatmap = self.client.get(f"/api/eda/heatmap_depto_sector?{query}").get_json()
        self.assertEqual(kpis["denominador"], heatmap["denominador"])
        self.assertEqual(kpis["meta"]["filtros"], heatmap["meta"]["filtros"])
        # Celdas vacías y suprimidas son null, nunca 0
        for row_status, row_count in zip(heatmap["cell_status"], heatmap["counts"]):
            for status, count in zip(row_status, row_count):
                if status in ("empty", "suppressed"):
                    self.assertIsNone(count)

    def test_invalid_filter_returns_400_with_detail(self):
        res = self.client.get("/api/kpis?depto=MARTE")
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.get_json()["error"], "filtro_invalido")

    def test_predict_happy_path_uses_conformal_interval(self):
        payload = {
            "personal": 45, "sueldos": 3200000.0, "remuneraciones": 900000.0,
            "energia": 210000.0, "activos": 18000000.0, "inventarios": 2100000.0,
            "n_insumos": 8, "total_valor_co": 9500000.0, "total_valor_uti": 9100000.0,
            "depto": "LA PAZ", "sector_macro": "Industria Manufacturera",
        }
        res = self.client.post("/api/predict", json=payload)
        self.assertEqual(res.status_code, 200)
        body = res.get_json()
        self.assertTrue(body["success"])
        self.assertGreater(body["prediction_bs"], 0)
        self.assertLess(body["lower_bound_bs"], body["prediction_bs"])
        self.assertGreater(body["upper_bound_bs"], body["prediction_bs"])
        self.assertIn("conformal", body["interval_label"])
        self.assertTrue(body["meta"]["run_id"].startswith("RUN-"))
        self.assertIn("no constituye evaluación tributaria", body["limitacion_uso"])

    def test_predict_invalid_inputs_return_400(self):
        base = {
            "personal": 45, "sueldos": 3200000.0, "remuneraciones": 900000.0,
            "energia": 210000.0, "activos": 18000000.0, "inventarios": 2100000.0,
            "n_insumos": 8, "total_valor_co": 9500000.0, "total_valor_uti": 9100000.0,
            "depto": "LA PAZ", "sector_macro": "Industria Manufacturera",
        }
        # Categoría desconocida
        bad_sector = dict(base, sector_macro="Criptomineria")
        res = self.client.post("/api/predict", json=bad_sector)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.get_json()["error"], "categoria_invalida")
        # Rango inválido
        bad_range = dict(base, personal=-5)
        res = self.client.post("/api/predict", json=bad_range)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.get_json()["error"], "rango_invalido")
        # Tipo inválido
        bad_type = dict(base, sueldos="millones")
        res = self.client.post("/api/predict", json=bad_type)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.get_json()["error"], "tipo_invalido")
        # Campo faltante
        missing = {k: v for k, v in base.items() if k != "activos"}
        res = self.client.post("/api/predict", json=missing)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.get_json()["error"], "campo_requerido")

    def test_individual_access_gated_by_d04(self):
        self.assertFalse(ACCESO_INDIVIDUAL_HABILITADO)
        res = self.client.get("/api/empresas_riesgo/1")
        self.assertEqual(res.status_code, 403)
        self.assertEqual(res.get_json()["decision"], "D04")

    def test_empresas_riesgo_is_aggregate_with_d04_label_and_meta(self):
        res = self.client.get("/api/empresas_riesgo?limit=5")
        self.assertEqual(res.status_code, 200)
        body = res.get_json()
        self.assertIn("meta", body)
        self.assertFalse(body["acceso_individual"]["detalle_individual_habilitado"])
        self.assertIn("D04", body["acceso_individual"]["politica"])

    def test_empresas_riesgo_validates_params(self):
        res = self.client.get("/api/empresas_riesgo?limit=abc")
        self.assertEqual(res.status_code, 400)
        res = self.client.get("/api/empresas_riesgo?limit=10000")
        self.assertEqual(res.status_code, 400)

    def test_bunching_is_labeled_descriptive(self):
        res = self.client.get("/api/bunching_alerta")
        self.assertEqual(res.status_code, 200)
        body = res.get_json()
        self.assertIn("no constituye evidencia de incumplimiento", body["caracter_descriptivo"])
        self.assertIn("meta", body)

    def test_monitoring_without_traffic_reports_no_telemetry(self):
        from dashboard import app as app_module
        from dashboard.telemetry import TELEMETRY_PATH

        saved = list(app_module.REQUEST_LOGS)
        backup = None
        if TELEMETRY_PATH.exists():
            backup = TELEMETRY_PATH.with_suffix(".jsonl.bak")
            TELEMETRY_PATH.rename(backup)
        app_module.REQUEST_LOGS.clear()
        try:
            res = self.client.get("/api/mlops/monitoring")
            self.assertEqual(res.status_code, 200)
            body = res.get_json()
            self.assertEqual(body["status"], "SIN TELEMETRÍA")
            self.assertIsNone(body["avg_latency_ms"])
        finally:
            app_module.REQUEST_LOGS.extend(saved)
            if backup is not None and backup.exists():
                backup.rename(TELEMETRY_PATH)

    def test_drift_endpoint_reports_mode_real_or_labeled_fallback(self):
        """Contrato T17: modo real cuando hay ≥30 registros reales; fallback simulado solo rotulado con n<30."""
        from dashboard.telemetry import TELEMETRY_PATH

        backup = None
        if TELEMETRY_PATH.exists():
            backup = TELEMETRY_PATH.with_suffix(".jsonl.bak")
            TELEMETRY_PATH.rename(backup)
        try:
            res = self.client.post("/api/mlops/drift", json={"ventana_horas": 24})
            self.assertEqual(res.status_code, 200)
            results = res.get_json()["drift_results"]
            self.assertIn(results["__modo__"], ("real", "sin datos"))
            self.assertIn("ventana_horas", results)
        finally:
            if backup is not None and backup.exists():
                backup.rename(TELEMETRY_PATH)

    def test_predict_persists_real_telemetry(self):
        """A10: cada predicción real persiste un registro en telemetry.jsonl con ventana y N."""
        from dashboard.telemetry import load_records

        before = len(load_records())
        payload = {
            "personal": 45, "sueldos": 3200000.0, "remuneraciones": 900000.0,
            "energia": 210000.0, "activos": 18000000.0, "inventarios": 2100000.0,
            "n_insumos": 8, "total_valor_co": 9500000.0, "total_valor_uti": 9100000.0,
            "depto": "LA PAZ", "sector_macro": "Industria Manufacturera",
        }
        res = self.client.post("/api/predict", json=payload)
        self.assertEqual(res.status_code, 200)
        after = len(load_records())
        self.assertEqual(after, before + 1)
        latest = load_records()[-1]
        self.assertEqual(latest.get("origen"), "predict")
        self.assertIn("S01_05_A", latest.get("features", {}))
        self.assertIn("latency_ms", latest)


if __name__ == "__main__":
    unittest.main()
