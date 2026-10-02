"""Pruebas de evaluación del modelo (A05–A07); ejecutar con python -m unittest discover -s tests."""

import hashlib
import json
import unittest
from pathlib import Path

import numpy as np
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = PROJECT_ROOT / "dashboard" / "artifacts"

EXCLUDED_FOR_LEAKAGE = [
    "S05_01", "S05_02", "S05_03", "S05_04", "S12_01_B", "S12_02_B",
    "VPA", "PC", "ISPOINF", "VIPP", "VBP", "EAC", "OGO", "VUMPEEI",
    "CI", "VA", "SSB", "OPP", "PS", "R", "D", "target", "target_log",
]


def get_file_hashes(path: Path) -> set:
    """Calcula hashes SHA-256 tolerando normalización de saltos de línea (CRLF/LF en ambas direcciones)."""
    raw = path.read_bytes()
    hashes = {hashlib.sha256(raw).hexdigest()}
    if path.suffix.lower() in {".csv", ".json", ".txt", ".md"}:
        raw_lf = raw.replace(b"\r\n", b"\n")
        raw_crlf = raw_lf.replace(b"\n", b"\r\n")
        hashes.add(hashlib.sha256(raw_lf).hexdigest())
        hashes.add(hashlib.sha256(raw_crlf).hexdigest())
    return hashes


class ModelEvaluationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(ARTIFACTS / "manifest.json", "r", encoding="utf-8") as f:
            cls.manifest = json.load(f)
        with open(ARTIFACTS / "registry.json", "r", encoding="utf-8") as f:
            cls.registry = json.load(f)
        with open(ARTIFACTS / "cv_results.json", "r", encoding="utf-8") as f:
            cls.cv_results = json.load(f)
        cls.test_predictions = pd.read_csv(ARTIFACTS / "test_predictions.csv")
        cls.active = cls.registry["versions"][0]

    def test_package_run_id_and_hashes_are_consistent(self):
        run_id = self.manifest["run_id"]
        self.assertTrue(run_id.startswith("RUN-"))
        self.assertEqual(self.registry["run_id"], run_id)
        self.assertEqual(self.cv_results["run_id"], run_id)
        self.assertEqual(self.active["run_id"], run_id)
        self.assertEqual(set(self.test_predictions["run_id"].unique()), {run_id})
        for name, expected_hash in self.manifest["artifacts"].items():
            self.assertIn(expected_hash, get_file_hashes(ARTIFACTS / name), name)

    def test_cohortes_partition_all_rows_exactly_once(self):
        cohorte = self.manifest["cohorte"]
        self.assertEqual(
            cohorte["n_entrenamiento_ajuste"] + cohorte["n_calibracion"] + cohorte["n_prueba"],
            cohorte["n_total"],
        )
        self.assertEqual(cohorte["n_prueba"], len(self.test_predictions))
        self.assertEqual(cohorte["semilla"], 42)
        self.assertEqual(cohorte["preprocesamiento_run_id"], self.manifest["preprocessing_run_id"])

    def test_test_metrics_are_recomputable_from_test_predictions(self):
        real = self.test_predictions["real_bs"].to_numpy()
        pred = self.test_predictions["pred_bs"].to_numpy()
        r2 = float(1 - np.sum((real - pred) ** 2) / np.sum((real - real.mean()) ** 2))
        medape = float(np.median(np.abs(real - pred) / np.maximum(real, 1.0)) * 100)
        metrics = self.active["metrics"]
        self.assertAlmostEqual(r2, metrics["r2_bs"], places=3)
        self.assertAlmostEqual(medape, metrics["medape_percent"], places=2)

    def test_conformal_interval_meets_predefined_tolerance(self):
        coverage = float(self.test_predictions["inside_ic_90"].mean() * 100)
        self.assertGreaterEqual(coverage, 85.0)
        self.assertLessEqual(coverage, 95.0)
        conformal = self.active["conformal"]
        self.assertEqual(conformal["nominal"], 0.9)
        self.assertEqual(conformal["tolerancia"], [0.85, 0.95])
        self.assertTrue(conformal["etiqueta_calibrado"])
        self.assertAlmostEqual(coverage, conformal["cobertura_empirica_pct"], places=2)
        inside_ref = (
            (self.test_predictions["real_bs"] >= self.test_predictions["ref_nominal_lower_bs"])
            & (self.test_predictions["real_bs"] <= self.test_predictions["ref_nominal_upper_bs"])
        )
        self.assertAlmostEqual(
            float(inside_ref.mean() * 100),
            metrics_ref := self.active["metrics"]["cobertura_referencia_nominal_pct"],
            places=2,
        )

    def test_no_leakage_columns_in_model_features(self):
        import joblib

        pipeline = joblib.load(ARTIFACTS / "best_model.joblib")
        feature_names = list(pipeline.named_steps["prep"].feature_names_in_)
        for excluded in EXCLUDED_FOR_LEAKAGE:
            self.assertNotIn(excluded, feature_names)
            self.assertNotIn(f"log_{excluded}", feature_names)
        self.assertIn("log_S01_03_C", feature_names)
        self.assertIn("sector_macro", feature_names)

    def test_subgroup_metrics_report_n_and_suppress_small_segments(self):
        por_sector = self.active["metrics"]["segmentos_metricas"]["por_sector"]
        self.assertEqual(len(por_sector), 13)
        for name, row in por_sector.items():
            self.assertIn("n", row)
            if row["n"] < 10:
                self.assertNotIn("r2_bs", row)
                self.assertIn("nota", row)
            else:
                self.assertIn("r2_bs", row)
                self.assertIn("medape_pct", row)
        por_quintil = self.active["metrics"]["segmentos_cobertura"]["por_quintil"]
        self.assertEqual(len(por_quintil), 5)
        for row in por_quintil.values():
            self.assertIn("cobertura_pct", row)
            self.assertGreater(row["n"], 0)

    def test_champion_meets_d06_threshold_and_meta_is_labeled(self):
        metas = self.active["metas"]
        metrics = self.active["metrics"]
        self.assertEqual(metas["d06_medape_max"], 40.0)
        self.assertEqual(metas["meta_historica_medape"], 25.0)
        cumple = metrics["medape_percent"] <= metas["d06_medape_max"] and metrics["r2_bs"] >= metas["d06_r2_bs_min"]
        self.assertEqual(cumple, metas["medape_cumple_umbral_aprobacion"])
        self.assertLessEqual(metrics["medape_percent"], metas["d06_medape_max"])
        self.assertGreaterEqual(metrics["r2_bs"], metas["d06_r2_bs_min"])
        self.assertGreater(metrics["medape_percent"], metas["meta_historica_medape"])

    def test_test_split_is_deterministic_for_frozen_inputs(self):
        df = pd.read_csv(PROJECT_ROOT / "data" / "processed" / "dataset_procesado.csv", low_memory=False)
        y_log = np.log1p(df["target"].to_numpy(dtype=float))
        quantiles = pd.qcut(y_log, q=5, labels=False, duplicates="drop")
        from sklearn.model_selection import train_test_split

        _, X_test_idx = train_test_split(
            np.arange(len(df)), test_size=0.2, random_state=42, stratify=quantiles
        )
        recomputed = np.sort(df["target"].to_numpy(dtype=float)[X_test_idx])
        observed = np.sort(self.test_predictions["real_bs"].to_numpy(dtype=float))
        np.testing.assert_allclose(recomputed, observed, rtol=0, atol=0.5)


if __name__ == "__main__":
    unittest.main()
