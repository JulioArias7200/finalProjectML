"""Pruebas del contrato de API para los endpoints de metadatos y linaje de datos (/api/dataset/*)."""

import unittest
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from dashboard.app import app, PACKAGE_STATE


class DatasetMetadataApiTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app.config["TESTING"] = True
        cls.client = app.test_client()

    def test_00_package_ready(self):
        self.assertTrue(PACKAGE_STATE["ready"], PACKAGE_STATE.get("error"))

    def test_api_dataset_metadata(self):
        res = self.client.get("/api/dataset/metadata")
        self.assertEqual(res.status_code, 200)
        data = res.get_json()

        self.assertIn("datasets", data)
        datasets = data["datasets"]
        self.assertIn("primary", datasets)
        self.assertIn("secondary", datasets)
        self.assertIn("processed", datasets)

        # Dataset Primario
        prim = datasets["primary"]
        self.assertEqual(prim["rows"], 3153)
        self.assertEqual(prim["columns"], 167)
        self.assertEqual(len(prim["sha256"]), 64)
        self.assertIn("ID", prim["key"])

        # Dataset Secundario
        sec = datasets["secondary"]
        self.assertEqual(sec["rows_physical"], 6428)
        self.assertEqual(sec["rows_valid"], 6427)
        self.assertEqual(sec["columns"], 8)
        self.assertEqual(len(sec["sha256"]), 64)

        # Dataset Procesado
        proc = datasets["processed"]
        self.assertEqual(proc["rows"], 3153)
        self.assertEqual(proc["columns"], 184)
        self.assertEqual(len(proc["sha256"]), 64)

        # Resumen general y meta
        self.assertIn("summary", data)
        self.assertEqual(data["summary"]["empresas_totales"], 3153)
        self.assertEqual(data["summary"]["empresas_manufactureras_con_insumos"], 1614)
        self.assertIn("meta", data)

    def test_api_dataset_lineage(self):
        res = self.client.get("/api/dataset/lineage")
        self.assertEqual(res.status_code, 200)
        data = res.get_json()

        self.assertIn("sankey", data)
        sankey = data["sankey"]
        self.assertIn("nodes", sankey)
        self.assertIn("links", sankey)
        self.assertGreaterEqual(len(sankey["nodes"]), 10)
        self.assertGreaterEqual(len(sankey["links"]), 10)

        # Verificar que los índices de los links estén dentro de los límites
        node_ids = {n["id"] for n in sankey["nodes"]}
        for link in sankey["links"]:
            self.assertIn(link["source"], node_ids)
            self.assertIn(link["target"], node_ids)
            self.assertGreater(link["value"], 0)

        # Operaciones del pipeline
        self.assertIn("operations", data)
        self.assertEqual(len(data["operations"]), 7)
        step_numbers = [op["step"] for op in data["operations"]]
        self.assertEqual(step_numbers, [1, 2, 3, 4, 5, 6, 7])


if __name__ == "__main__":
    unittest.main()
