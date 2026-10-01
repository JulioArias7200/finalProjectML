"""Contratos de calidad y agregación; ejecutar con python -m unittest discover -s tests."""

import unittest

import numpy as np
import pandas as pd

from preprocessing.preprocessing import (
    PREDICTOR_NUM_COLS,
    TARGET_RECONCILIATION_TOLERANCE_BS,
    aggregate_materials_by_enterprise,
    clean_materials_data,
    load_raw_datasets,
    merge_and_clean_enterprise_data,
    run_preprocessing,
    target_differences,
)
from dashboard.aggregation import department_sector_heatmap, select_rows, summarize_kpis


class DataContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.general, cls.materials = load_raw_datasets()

    def test_extract_structure_and_target_reconciliation(self):
        self.assertEqual(self.general.shape, (3153, 167))
        self.assertEqual(self.materials.shape, (6427, 8))
        self.assertEqual(self.materials.attrs["blank_rows_excluded"], 1)
        self.assertTrue(self.general["ID"].is_unique)
        difference = target_differences(self.general)
        self.assertEqual(int((difference > 0).sum()), 60)
        self.assertLessEqual(float(difference.max()), TARGET_RECONCILIATION_TOLERANCE_BS)

    def test_materials_keep_unknown_separate_from_zero(self):
        materials = pd.DataFrame({
            "ID": [1, 1, 2, 3],
            "materia": ["a", "b", "c", "d"],
            "valor_co": [99999, -4, None, 0],
            "valor_uti": [10, None, None, 0],
        })
        cleaned = clean_materials_data(materials)
        self.assertEqual(cleaned.loc[0, "valor_co_clean"], 99999)
        self.assertTrue(np.isnan(cleaned.loc[1, "valor_co_clean"]))
        aggregated = aggregate_materials_by_enterprise(cleaned).set_index("ID")
        self.assertTrue(np.isnan(aggregated.loc[2, "total_valor_co"]))
        self.assertEqual(aggregated.loc[3, "total_valor_co"], 0)

    def test_missing_material_record_is_not_fabricated_monetary_zero(self):
        general = pd.DataFrame({
            "ID": [1, 2], "C2_01": ["LA PAZ", "ORURO"],
            "actividad_pricipal_codigo_V1": [47110, 47110],
            "S00_01_A": [100.0, 200.0], "S05_04": [100.0, 200.0],
        })
        material = pd.DataFrame({"ID": [1], "n_insumos": [1], "total_valor_co": [50.0], "total_valor_uti": [40.0]})
        joined = merge_and_clean_enterprise_data(general, material).set_index("ID")
        self.assertEqual(joined.loc[2, "n_insumos"], 0)
        self.assertFalse(joined.loc[2, "has_material_record"])
        self.assertTrue(np.isnan(joined.loc[2, "total_valor_co"]))

    def test_capacity_requires_unit_and_is_not_model_predictor(self):
        self.assertNotIn("S12_01_B", PREDICTOR_NUM_COLS)
        self.assertNotIn("S12_02_B", PREDICTOR_NUM_COLS)
        self.assertIn("S12_01_C", self.general.columns)
        self.assertIn("S12_02_C", self.general.columns)

    def test_processed_dataset_preserves_cardinality(self):
        processed = run_preprocessing(save_outputs=False)
        self.assertEqual(processed["ID"].nunique(), len(processed))
        self.assertEqual(len(processed), 3153)
        self.assertEqual(processed["sector_macro"].nunique(), 13)
        no_material = ~processed["has_material_record"]
        self.assertTrue(processed.loc[no_material, "total_valor_co"].isna().all())

    def test_filtered_aggregations_share_denominator_and_suppress_small_cells(self):
        df = pd.DataFrame({
            "depto": ["A"] * 6 + ["B"],
            "sector_macro": ["X"] * 5 + ["Y", "X"],
            "target": [10.0] * 7,
        })
        selected = select_rows(df, depto="A")
        kpis = summarize_kpis(selected)
        heatmap = department_sector_heatmap(selected)
        self.assertEqual(kpis["denominador"], heatmap["denominador"])
        self.assertEqual(heatmap["counts"], [[5, None]])
        self.assertEqual(heatmap["cell_status"], [["ok", "suppressed"]])
        with self.assertRaises(ValueError):
            select_rows(df, sector="no existe")


if __name__ == "__main__":
    unittest.main()
