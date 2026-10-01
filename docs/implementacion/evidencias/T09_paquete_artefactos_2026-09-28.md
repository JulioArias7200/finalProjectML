# Evidencia T09 · A07 · 2026-09-28

Revisor: Codebuff (revisión técnica de esta implementación). Ejecución: iteración **v1.20260928.2256**, `run_id` **RUN-20260928-b3cfc0795ed7**. Entradas: `models/train.py` (empaquetado), `dashboard/artifacts/manifest.json`, `dashboard/artifacts/registry.json`.

Resultado esperado: modelo, registro, CV, predicciones e importancias comparten `run_id`, hashes y cohorte; un paquete inválido (mezcla o ausencia) debe ser rechazado al cargar.

## run_id y trazabilidad

- `run_id` de la ejecución: **RUN-20260928-b3cfc0795ed7**, derivado de `SHA-256(best_model.joblib) + run_id de preprocesamiento + N`. El `run_id` de preprocesamiento enlazado es **PRE-20260928-d004f6ddd436**, de modo que el paquete es rastreable hasta los CSV crudos con sus hashes.
- Identificador presente y único en: `registry.json` (raíz y versión activa), `cv_results.json`, `manifest.json`, `models/bitacora_modelos.json` y la columna `run_id` de `test_predictions.csv` (631 filas, un solo valor).

## Cohorte registrada

`{ajuste: 1.891, calibración: 631, prueba: 631, total: 3.153}`, semilla 42, protocolo `models/protocolo_entrenamiento.md` versión 2026-09-28. La suma de cohortes es exactamente el total del extracto; el número de filas de `test_predictions.csv` coincide con la cohorte de prueba.

## Integridad (hashes SHA-256 en `manifest.json`)

| Artefacto | Verificación |
|---|---|
| best_model.joblib | OK |
| test_predictions.csv | OK |
| cv_results.json | OK |
| feature_importance.json | OK |
| registry.json | OK |
| bitacora_modelos.json | OK |

Recalculo independiente de los 6 hashes contra los archivos reales: **coinciden todos**. El `manifest.json` es la raíz de integridad del paquete activo.

## Sobre iteraciones del mismo run_id

Tras el re-empaquetado con razones de decisión dinámicas, `models/train.py` produjo la versión **v1.20260928.2356** con el **mismo `run_id`** RUN-20260928-b3cfc0795ed7 y métricas idénticas: el pipeline es determinista (semilla 42, entrada congelada), por lo que el `run_id` derivado del modelo serializado se mantiene y las referencias de esta evidencia siguen vigentes. La versión previa del mismo día queda ARCHIVED en `registry.json`.

## Rechazo de mezclas (contrato A07)

La política de carga queda definida: el servidor (T10) debe verificar `run_id` de `registry.json`, `manifest.json` y `test_predictions.csv`, y los hashes del manifest, antes de servir; ante falta o mismatch responde 503 (preparación) en lugar de mezclar ejecuciones. La verificación está automatizada en `tests/test_model_evaluation.py::test_package_run_id_and_hashes_are_consistent`, que fallaría ante cualquier edición manual de un artefacto.

Comprobación: suite completa `python -m unittest discover -s tests` → 14/14 OK (6 de datos + 8 de modelo).

Conclusión: A07 cumplido a nivel de paquete y pruebas. La validación en el momento de la carga HTTP se ejecutará en T10–T12.
