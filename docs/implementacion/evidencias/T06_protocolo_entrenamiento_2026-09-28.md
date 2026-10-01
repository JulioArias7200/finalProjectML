# Evidencia T06 · A05 · 2026-09-28

Revisor: Codebuff (revisión técnica de esta implementación). Entradas: `models/protocolo_entrenamiento.md`, `docs/implementacion/06_decisiones_y_riesgos.md`, `data/processed/dataset_procesado.csv` (`run_id` de preprocesamiento PRE-20260928-d004f6ddd436).

Resultado esperado: partición reproducible, prevención de fuga, escalas etiquetadas en Bs y subgrupos definidos **antes** de entrenar.

Resultado observado:

1. **Protocolo predefinido y fechado** en `models/protocolo_entrenamiento.md` (versión 2026-09-28), redactado antes de la ejecución de esta iteración. Fija: prueba final reservada de 631 empresas (20 % estratificado por quintiles), conjunto de calibración separado de 631 (25 % del bloque de entrenamiento), CV de 5 pliegues solo sobre el bloque de ajuste (1.891), semilla 42, algoritmos e hiperparámetros sin búsqueda.
2. **D06 cerrada antes de entrenar:** umbral de aprobación MedAPE ≤ 40 % y R²(Bs) ≥ 0,70; meta histórica ≤ 25 % conservada como aspiracional no alcanzable. Registrado en `06_decisiones_y_riesgos.md`.
3. **Prevención de fuga:** transformadores (`SimpleImputer(median)` + `StandardScaler` + `OneHotEncoder`) dentro del `Pipeline`, ajustados solo con datos de entrenamiento de cada pliegue y del ajuste final. Los faltantes de materiales preservados por T03 nunca se convierten en cero antes del modelo. Verificado por `tests/test_model_evaluation.py::test_no_leakage_columns_in_model_features` (sin `S05_*`, sin derivadas, sin `S12_*_B`, sin `target`).
4. **Escalas etiquetadas:** todas las métricas se registran por separado en escala `log1p` y en Bs con retransformación de Duan; los umbrales D06 se evalúan en escala Bs.

Comprobación: `./.python/python.exe -m py_compile models/train.py`; partición estable verificada por `test_test_split_is_deterministic_for_frozen_inputs` (la prueba de la ejecución coincide exactamente con la repartición recalculada para la misma semilla y entrada congelada).

Conclusión: protocolo ejecutado tal cual; A05 en su dimensión de protocolo cumplido. Los resultados de la ejecución se detallan en T07.
