# Evidencia T17 · A10 · 2026-09-29

**Tarea:** T17 — Implementar telemetría y drift real
**Criterio:** A10 — Tráfico, latencia y drift provienen de registros reales con ventana y N; simulación solo en modo rotulado; sin tráfico se muestra "sin telemetría".

## Qué se implementó

1. **`dashboard/telemetry.py` (nuevo):** registro JSONL *append-only* (`dashboard/telemetry.jsonl`) de cada petición a `/api/predict` con timestamp, latencia, estado e insumos crudos (sin identificadores empresariales, cumplimiento D04). Acotado a 5.000 registros (`_trim_if_needed`). Expone `traffic_summary()` (estado, ventana, N, latencia media y p95, tasa de error, serie por hora) y `real_drift_check()` (KS no paramétrico contra la referencia versionada, corrección de Bonferroni α=0.05/5, distancia de Wasserstein, N por variable).
2. **`dashboard/app.py`:** el endpoint `/api/predict` persiste cada llamada real; `/api/mlops/monitoring` sirve `traffic_summary()`; `/api/mlops/drift` sirve `real_drift_check()` con fallback a la simulación de `models/drift.py` **solo cuando n<30**, rotulada en la respuesta (`__modo__: real | simulado | sin datos`).
3. **`models/train.py`:** la referencia de drift (`models/reference_stats.json`) se recalcula sobre **casos completos en las 5 variables monitoreadas** (n=1.614 de 3.153), con metadatos `_meta` (población, n, `run_id_pre`). Justificación: la API exige todos los campos del formulario (400 si falta alguno), de modo que el tráfico de producción siempre proviene de payloads completos; compararlos contra márgenes por columna de toda la población reportante producía *drift espurio* por selección de tamaño (medianas 1,37×–1,78× mayores en casos completos).
4. **`models/drift.py`:** la simulación queda rotulada internamente como modo de demostración; la medición real vive en `telemetry.py`.
5. **UI (`app.js`):** monitoreo muestra "SIN TELEMETRÍA" sin barras fantasma cuando no hay registros; drift muestra modo y N reales.

## Pruebas de integración (paquete v1.20260929.0054, run_id RUN-20260929-b3cfc0795ed7)

Scripts reproducibles depositados en `tests/integracion/` (requieren servidor activo en `127.0.0.1:5055`):

| Escenario | Script | Resultado |
|---|---|---|
| Arranque vacío → sin tráfico | `tests/test_dashboard_smoke.py::test_monitoring_empty_start_with_telemetry_quarantined` | `SIN TELEMETRÍA` con `avg_latency_ms=null`, sin series simuladas. ✅ |
| Tráfico realista → sin drift | `tests/integracion/prueba_a10_sin_drift.py` (120 peticiones muestreadas del dataset procesado, semilla 42) | `modo: real`, **5/5 variables ESTABLE** (p 0.39–0.68): sin falsos positivos. ✅ |
| Tráfico deliberadamente bimodal → drift | `tests/integracion/prueba_a10_drift_detectado.py` (32 peticiones atípicas) | `modo: real`, n=32 por variable, **5/5 DRIFT DETECTADO** (p≈0.0). ✅ |
| Latencia y errores observados | Monitoreo tras tráfico | `OPERATIVO`, latencia media y p95 reales, tasa de error 0 %, ventana y N visibles. ✅ |

Detalle de la corrida final (2026-09-29, 00:57 local): sin drift → S01_05_A p=0.6326, S01_03_C p=0.3949, S02_09 p=0.5962, S07_09_E p=0.6782, total_valor_uti p=0.4908. Con drift → todas las variables p≤0.0015 con KS y Wasserstein reportados.

## Descartes documentados

- **Masa de ceros artificial:** en la primera iteración de la prueba se envió `0.0` por campos no reportados (NaN en el dataset); esa masa de ceros es ajena a la referencia de valores *reportados* y disparaba drift por construcción. Se corrigió el script (no el detector) para muestrear solo casos completos; quedan excluidos del escenario "sin drift".
- **Referencia por márgenes:** la versión anterior de `reference_stats.json` usaba márgenes por columna de toda la población; se descartó por producir drift espurio (documentado arriba).

## Conclusión

A10 **CUMPLE**: todas las señales de monitoreo provienen de `dashboard/telemetry.jsonl` (peticiones reales), con ventana y N visibles; la simulación solo existe como modo rotulado de respaldo; y el arranque sin tráfico muestra "SIN TELEMETRÍA". El detector discrimina correctamente tráfico típico de tráfico atípico.

**Revisor:** Codebuff (revisión técnica con pruebas ejecutables en esta misma sesión).
**Fecha de revisión:** 2026-09-29.
