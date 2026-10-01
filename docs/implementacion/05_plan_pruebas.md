# Plan de pruebas y evidencias

Las pruebas se escribirán al implementar cada capa. No se presupone que existan ni que pasen ahora. Conservar comandos, fecha, versión, semilla, salida y resumen sin datos individuales identificables en `evidencias/`.

| Nivel | Casos mínimos | Archivo previsto | Criterios |
|---|---|---|---|
| Datos | unicidad de empresa; cardinalidad de materiales; 152+15 campos; tipos/unidades; faltantes vs cero; redondeo entre objetivos; grupos sin datos; mapeo CAEB | `tests/test_data_contract.py` | A02–A04 |
| Modelo | fuga de objetivo y transformadores; partición estable; escalas correctas; métricas idénticas al recalcular predicciones de prueba; incertidumbre y cobertura; segmentos pequeños | `tests/test_model_evaluation.py` | A05–A07 |
| Artefactos/API | mismo `run_id`; hash y ausencia de archivos; filtros; 400 para invalidación; 503 para paquete incompleto; validación de predicción; política de acceso a detalles | `tests/test_api_contract.py` | A07–A08 |
| UI | cada panel carga datos reales; controles de filtros; unidad y N visibles; celdas vacías; pantalla pequeña; teclado y texto alternativo; comparación sin eje mezclado | `tests/test_dashboard_smoke.py` + revisión manual | A09 |
| Operación | tráfico vacío y generado; latencia observada; drift calculado por ventana; simulación rotulada; reinicio de servicio | prueba de integración documentada | A10–A11 |

## Protocolo estadístico

Congelar entrada y semilla antes de comparar modelos. Separar entrenamiento/prueba y, dentro de entrenamiento, ajuste y calibración si el método lo requiere. Seleccionar hiperparámetros con CV interna. La prueba final se consulta una vez para el informe de selección; cambios posteriores inician nueva versión. Registrar intervalos de incertidumbre para estimaciones de desempeño cuando proceda, N de cada subgrupo y límites de lectura para muestras pequeñas. Verificar cuantitativamente cobertura nominal de predicción (global y segmentos) con regla de aceptación fijada antes de mirar la prueba.

No convertir un R² alto en validación de las señales de “riesgo”. Bunching y anomalías requieren evaluaciones separadas de estabilidad y de tasa de falsos positivos; hasta entonces se muestran solo como exploración descriptiva.

## Comprobación de la documentación del plan

Desde la raíz:

```powershell
./scripts/verificar_plan.ps1
```

Retorno 0 significa que el **seguimiento es estructuralmente válido**, aunque las tareas estén pendientes. Para exigir cierre completo:

```powershell
./scripts/verificar_plan.ps1 -RequireComplete
```

Un retorno no cero de este último es esperado mientras el proyecto siga en ejecución. Esta comprobación no sustituye revisión estadística, pruebas del producto ni aprobación de fuentes y acceso.
