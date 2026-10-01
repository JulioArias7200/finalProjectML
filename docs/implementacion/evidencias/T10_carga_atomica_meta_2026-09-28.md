# Evidencia T10 · A07/A08 · 2026-09-28

Revisor: Codebuff (revisión técnica de esta implementación). Entradas: `dashboard/app.py`, `dashboard/artifacts/manifest.json`, `dashboard/README.md`. Método: lectura del mecanismo de carga y prueba automatizada del arranque con el paquete real.

Resultado esperado: carga atómica de contratos y metadatos de API desde el paquete activo; un paquete mezclado o incompleto impide servir datos.

## Carga atómica implementada (A07)

1. `load_dashboard_artifacts()` exige `manifest.json` con `run_id`; verifica el **SHA-256 de los 6 artefactos** declarados y carga todos o ninguno. Cualquier hash incompatible, archivo ausente o `run_id` de `registry.json`/`cv_results.json`/`test_predictions.csv` que no coincida **deja el paquete entero en estado no disponible**.
2. El guard `@require_package` responde **503** `paquete_no_disponible` con detalle en todos los endpoints analíticos mientras el paquete no esté íntegro. Nunca se mezclan ejecuciones.
3. Verificación positiva: el arranque real con el paquete RUN-20260928-b3cfc0795ed7 carga y sirve (`test_00_package_loaded_successfully`).
4. Verificación de rechazo: el escenario de mezcla queda cubierto por `tests/test_model_evaluation.py::test_package_run_id_and_hashes_are_consistent` (fallaría ante edición manual) y la lógica de `load_dashboard_artifacts` (misma condición evaluada al arranque).

## Meta de contrato en respuestas (A08)

`build_meta()` adjunta a las respuestas analíticas: `run_id` (RUN-20260928-b3cfc0795ed7), `preprocessing_run_id` (PRE-20260928-d004f6ddd436), `dataset_id`, `periodo` (EAIMCS 2017 con cierre según actividad), `poblacion` (extracto sin expansión), `n` (3.153), `filtros` aplicados, `unidad`, `escala`, `generated_at` y `limitaciones` (muestra dirigida, sin factor de expansión, corte transversal, señales descriptivas). Endpoints cubiertos: `/api/kpis`, `/api/eda/heatmap_depto_sector`, `/api/models`, `/api/cross_validation`, `/api/mlops`, `/api/mlops/monitoring`, `/api/predict`, `/api/empresas_riesgo`, `/api/bunching_alerta`.

Comprobación: `test_meta_contract_in_analytic_responses` verifica la presencia de cada clave y el prefijo `RUN-` en 5 endpoints representativos.

Conclusión: A07 en su dimensión de servidor cumplido (la verificación de hash/run_id está automatizada y la carga es atómica); A08 parcialmente cubierto junto con T11/T12.
