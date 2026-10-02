"""Prueba de humo del dashboard (A09/A10): vistas y datos de los gráficos principales."""

import sys
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from dashboard.app import app  # noqa: E402


class DashboardSmokeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app.config["TESTING"] = True
        cls.client = app.test_client()

    def test_00_index_renders(self):
        res = self.client.get("/")
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"<!DOCTYPE html", res.data)

    def test_views_needed_by_frontend_have_expected_shapes(self):
        with self.client.get("/api/eda/heatmap_depto_sector") as res:
            hm = res.get_json()
            self.assertIn("cell_status", hm)
            self.assertIn("min_cell_n", hm)
            self.assertIn("denominador", hm)
        with self.client.get("/api/eda/boxplot_deptos") as res:
            boxes = res.get_json()
            self.assertTrue(isinstance(boxes, list) and boxes)
            for item in boxes:
                self.assertIn("status", item)
                self.assertIn("count_label", item)
                self.assertIn("sample_log", item)
        with self.client.get("/api/cross_validation") as res:
            cv = res.get_json()
            self.assertIn("cohorte", cv)
            self.assertIn("run_id", cv)
        with self.client.get("/api/eda/distribution") as res:
            dist = res.get_json()
            for key in ["raw_values", "log_values", "total_count"]:
                self.assertIn(key, dist)

    def test_monitoring_empty_start_with_telemetry_quarantined(self):
        from dashboard import app as app_module
        from dashboard.telemetry import TELEMETRY_PATH

        backup = None
        if TELEMETRY_PATH.exists():
            backup = TELEMETRY_PATH.with_suffix(".jsonl.bak")
            TELEMETRY_PATH.rename(backup)
        try:
            app_module.REQUEST_LOGS.clear()
            res = self.client.get("/api/mlops/monitoring")
            self.assertEqual(res.status_code, 200)
            body = res.get_json()
            self.assertEqual(body["status"], "SIN TELEMETRÍA")
            self.assertIsNone(body["avg_latency_ms"])
        finally:
            if backup is not None and backup.exists():
                backup.rename(TELEMETRY_PATH)

    def test_frontend_handles_suppression_d04_and_no_telemetry(self):
        js = (PROJECT_ROOT / "dashboard" / "static" / "js" / "app.js").read_text(encoding="utf-8")
        self.assertIn("SIN TELEMETRÍA", js)
        self.assertIn("status === 'suppressed'", js)
        self.assertIn("yaxis2", js)  # MedAPE en eje separado, nunca mezclado con R²
        self.assertIn("D04", js)
        res = self.client.get("/")
        html = res.data.decode("utf-8")
        self.assertNotIn("predCapacidadMP", html)  # campo retirado del simulador (D07)

    def test_predict_form_fields_match_whitelist(self):
        res = self.client.get("/")
        html = res.data.decode("utf-8")
        js = (PROJECT_ROOT / "dashboard" / "static" / "js" / "app.js").read_text(encoding="utf-8")
        for required in [
            "predDepto", "predSector", "predPersonal", "predSueldos", "predRemuneraciones",
            "predEnergia", "predActivos", "predInventarios", "predInsumosCompras",
            "predInsumosUtil", "predNInsumos",
        ]:
            self.assertIn(required, html)
            self.assertIn(required, js)


if __name__ == "__main__":
    unittest.main()
