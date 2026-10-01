# Evidencia T18 · A11 · 2026-09-29

**Tarea:** T18 — Ejecutar pruebas integrales y revisión estadística
**Criterio:** A11 — Recorrido completo funciona; documentación de ejecución y límites corresponde a producto; pruebas automatizadas y revisión manual pasan.

## Registro de pruebas automatizadas

Comando: `.python/python.exe -m unittest discover -s tests` (Python 3.13.14, runtime local `.python/`, sin venv).

| Suite | Pruebas | Resultado |
|---|---|---|
| `tests/test_data_contract.py` (A02–A04) | 6 | OK |
| `tests/test_model_evaluation.py` (A05–A07) | 8 | OK |
| `tests/test_api_contract.py` (A07–A08) | 15 | OK |
| `tests/test_dashboard_smoke.py` (A09–A10) | 3 | OK |
| **Total** | **32** | **OK (2.18 s)** |

Ajuste registrado: dos pruebas escritas en G3 asumían el contrato pre-T17 (drift siempre simulado; monitoreo sin telemetría aunque existiera el archivo). Se actualizaron al contrato vigente: el drift reporta `__modo__ ∈ {real, sin datos}` cuando hay telemetría, y "SIN TELEMETRÍA" exige archivo de telemetría en cuarentena además de memoria vacía. Se añadió `test_predict_persists_real_telemetry`, que verifica la persistencia JSONL real de cada predicción (A10).

## Pruebas de integración E2E (requieren servidor activo)

Depósitos reproducibles en `tests/integracion/` (T17):

- `prueba_a10_sin_drift.py`: 120 predicciones con insumos reales del dataset → 5/5 variables ESTABLE (p 0.39–0.68).
- `prueba_a10_drift_detectado.py`: 32 predicciones bimodales → 5/5 DRIFT DETECTADO (p≤0.0015).

## Verificación integral (T18, sin servidor)

Comando: `.python/python.exe tests/integracion/verificacion_integral.py` → **RESULTADO: TODO OK** (14/14 comprobaciones):

1. **Paquete v1.20260929.0054** (`run_id` RUN-20260929-b3cfc0795ed7): 6/6 hashes SHA-256 del manifest coinciden con los archivos reales; `active_version` y `run_id` coherentes entre `manifest.json`, `registry.json` y `models/bitacora_modelos.json`.
2. **Métricas recalculadas desde `test_predictions.csv`** (631 filas de prueba, todas con el `run_id` del paquete): R² log = 0.7824, R² Bs = 0.7396, MedAPE = 35.10 %, cobertura conformal = 88.27 %, cobertura de la referencia nominal ±1,645×RMSE = 90.33 % — idénticas a las reportadas en T07/T08 (reproducibilidad A05).
3. **Umbrales predefinidos**: D06 MedAPE ≤ 40 % → 35.10 % ✅; D02 cobertura conformal ∈ [85, 95] → 88.27 % ✅ ("calibrado" procede).
4. **Referencia de drift**: `_meta` presente con población de casos completos (n=1.614/3.153) y `run_id_pre` PRE-20260928-d004f6ddd436.

## Revisión estadística (consolidada)

- Partición y transformadores ajustados solo en entrenamiento (verificado por suite de modelo, A05).
- Meta aspiracional del marco lógico **MedAPE ≤ 25 %: NO alcanzada** (35.10 %). Registrada la brecha en `models/protocolo_entrenamiento.md` y `models/README.md`; el producto limita la afirmación de desempeño en consecuencia (prototipo validado con la meta D06 operativa, no meta aspiracional).
- Señales de "riesgo" rotuladas como exploración descriptiva, no acusatorias (A08/D04, evidencia T11).
- Sin fuga de objetivo; escalas etiquetadas; intervalo solo se anuncia "calibrado" porque la cobertura empírica satisface el umbral predefinido (A06/D02).

## Revisión manual

- Recorrido completo del panel verificado con navegador en G4 (evidencias T13–T16 con capturas escritorio/móvil).
- Reinicio de servicio probado varias veces durante G4/G5 (carga atómica del paquete nuevo, guard 503 si el paquete estuviera ausente).

## Conclusión

A11 parcialmente cubierto en T18: todas las pruebas automatizadas y de integración pasan, la revisión estadística está consolidada y las métricas del paquete activo son reproducibles. Falta para cerrar A11: guías de ejecución finales y acta de entrega (T19).

**Revisor:** Codebuff (revisión técnica con comandos y salidas en esta misma sesión).
**Fecha de revisión:** 2026-09-29.
