# Evidencia T12 · A08 · 2026-09-28

Revisor: Codebuff (revisión técnica de esta implementación). Entradas: `tests/test_api_contract.py` (12 casos), `dashboard/app.py`, `dashboard/README.md` (catálogo de endpoints). Método: pruebas de integración con el cliente de Flask en modo testing contra el paquete real RUN-20260928-b3cfc0795ed7.

Resultado esperado: API validada con errores de contrato correctos y predicción con validación estricta de entradas.

## Matriz de comprobaciones

| Comprobación del criterio A08 | Resultado |
|---|---|
| Respuestas con metadatos mínimos (`meta`) | OK en 5 endpoints representativos |
| Filtro con valor inexistente → **400** con detalle | `?depto=MARTE` → `filtro_invalido` (OK) |
| Entrada de predict: categoría desconocida → **400** | `categoria_invalida` con valores válidos listados (OK) |
| Entrada de predict: rango inválido → **400** | `personal=-5` → `rango_invalido` (OK) |
| Entrada de predict: tipo inválido → **400** | `sueldos="millones"` → `tipo_invalido` (OK) |
| Entrada de predict: campo faltante → **400** | `campo_requerido` identificando el campo (OK) |
| Fallo de paquete → **503** | Guard `@require_package` en endpoints analíticos; carga atómica que falla cerrada (T10) |
| Acceso individual cumple D04 | Ficha individual → **403** con referencia a D04; listado rotulado agregado (OK) |
| Ninguna señal presentada como acusación | `caracter_descriptivo` en bunching; `limitacion_uso` en predict (OK) |
| Predicción en Bs con intervalo conformal calibrado (D02) | `interval_label: "90% (conformal calibrado)"`, límites coherentes, cobertura y referencia nominal rotulada incluidas (OK) |
| KPI y heatmap comparten denominador con el mismo filtro | `kpis.denominador == heatmap.denominador` y `meta.filtros` idénticos (OK) |
| Celdas vacías/suprimidas como `null`, nunca 0 | Verificado fila a fila sobre la respuesta del heatmap con filtro sectorial (OK) |

## Notas de la ruta de predicción

- El payload ya no acepta `capacidad_mp/capacidad_pt` (excluidas por D07); enviar campos no reconocidos no altera el modelo (lista blanca de 9 campos + 2 categóricos).
- El intervalo devuelto es el **conformal calibrado** de la ejecución activa (q̂ log = 0,9025); la referencia ±1,645×RMSE viaja rotulada como `reference_nominal_*`.
- La telemetría de `/api/predict` se registra con `origen: "predict"` para alimentar monitoreo real (base de T17).

Comprobación: `./.python/python.exe -m unittest discover -s tests` → **26/26 OK** (6 datos + 8 modelo + 12 API).

Conclusión: A08 cumplido. Decisión **D03 cerrada**: se mantienen las rutas existentes con `meta` completo en lugar de introducir `/api/v1` (los consumidores actuales del frontend no se rompen y el contrato queda documentado en `dashboard/README.md`); si en el futuro se requiere coexistencia, se añadirá `/api/v1/*` como alias sin cambiar semántica.
