# Evidencia T15 · A09 · 2026-09-28

Revisor: Codebuff (revisión técnica de esta implementación). Entradas: `dashboard/static/js/app.js` (renderModelsBarComparison, renderCvFoldsChart), `dashboard/templates/index.html` (panel de conformal), `/api/models`, `/api/bitacora_modelos`. Método: verificación en vivo con el paquete RUN-20260928-b3cfc0795ed7.

Resultado esperado: comparaciones y diagnósticos de modelos correctos, sin escalas mezcladas ni cifras de ejecuciones distintas.

## Comparación de modelos sin eje mezclado

- **Antes:** R² (0–1), RMSE(log) y MedAPE/100 compartían un único eje Y — explícitamente prohibido por `03_diseno_graficos.md`.
- **Ahora:** R²(Bs) y RMSE(log) en el eje primario; **MedAPE en eje secundario derecho 0–100%** rotulado, con `showgrid:false`. Verificado en vivo: `plotlyData = [{R², y}, {RMSE(log), y}, {MedAPE (%), y2}]` y `layout.yaxis2` presente. Los tooltips muestran valor completo y métrica.

## Cohorte explícita en CV

El gráfico de pliegues añade al título la cohorte de la comparación: "CV sobre bloque de ajuste n=1891 (calibración 631, prueba 631) · run RUN-20260928-b3cfc0795ed7". La comparación CV vs prueba ya no puede leerse como si proviniera de la misma muestra (contrato 02: cohorte fija de evaluación).

## Panel de incertidumbre corregido (D02)

- El bloque "Calibración Estocástica" que describía `±1.645 × RMSE_log` como el intervalo 90% y citaba 90.33% de una ejecución anterior fue **reescrito**: ahora explica el *split conformal* con conjunto de calibración separado y tolerancia [85%, 95%].
- La cifra mostrada (88.3%) proviene de la bitácora de la ejecución activa; la nota cambia a ⚠ si la cobertura saliera de tolerancia (lógica en `app.js`).
- La "Garantía de auditoría" indica que la referencia nominal viaja rotulada y que la cobertura por quintiles/sectores se publica con N.

## Cifras sin herencias

- Las "razones de decisión" de `bitacora_modelos.json` se generan ahora desde las métricas de **esta ejecución** (`build_razon` en `models/train.py`); verificado en vivo que la tabla ya no contiene 36.20%, 0.7868, 74.07% ni 90.33%.
- Re-empaquetado completo con `models/train.py` (versión v1.20260928.2356, mismo `run_id` por determinismo; ver T09).

Comprobación: inspección en vivo del panel "Modelo & Validez" (capturas de la sesión) y suite 30/30.

Conclusión: comparaciones y diagnósticos cumplen A09.
