# Plan maestro de implementación

## Objetivo y alcance

Entregar un dashboard integrado, reproducible y estadísticamente interpretable para el extracto local EAIMCS 2017: exploración, calidad de datos, comparación y diagnóstico de modelos, predicción con incertidumbre validada y monitoreo real. Mostrar el tamaño de cada subgrupo, unidades, denominadores, periodo, versión de datos/modelo y limitaciones de inferencia. La publicación de registros individuales queda condicionada a la decisión de acceso de `D04`.

El extracto no se debe extrapolar automáticamente a toda Bolivia: la ficha de la encuesta describe selección dirigida de empresas medianas y grandes y ausencia de factor de expansión. El dashboard debe decir a qué población y periodo corresponde cada cifra. La meta de MedAPE ≤25 % sigue siendo un criterio aspiracional; si la validación no la logra, registrar la brecha y limitar la afirmación de desempeño.

## Secuencia, puertas y entregables

| Puerta | Tareas | Resultado exigido | Bloquea |
|---|---|---|---|
| G0 Documentación | T01–T02 | Fuente, periodo, columnas, objetivo y decisiones de uso revisados | G1 |
| G1 Datos | T03–T05 | Limpieza y métricas descriptivas reproducibles; sin unidades incompatibles ni fugas | G2 |
| G2 Modelo | T06–T09 | Evaluación honesta, intervalo calibrado, un paquete de artefactos consistente | G3 |
| G3 Servicio | T10–T12 | API coherente, validada, segura y con métricas provenientes del paquete activo | G4 |
| G4 Interfaz | T13–T16 | Gráficos correctos, accesibles, con filtros coherentes y estados vacíos | G5 |
| G5 Operación | T17–T19 | Monitoreo real, pruebas de extremo a extremo y guía de entrega | Aceptación final |

Se pueden preparar diseños y pruebas en paralelo, pero una puerta posterior no se aprueba antes de sus dependencias. El detalle verificable está en [seguimiento.csv](seguimiento.csv) y [matriz de aceptación](04_matriz_aceptacion.md).

## Cambios propuestos por archivo

| Archivo o nuevo módulo | Intervención prevista | Tareas |
|---|---|---|
| `docs/README.md`, `docs/01_analisis_dataset_EAIMCS.md`, `docs/02_diccionario_datos_EAIMCS.md`, `docs/marco_logico_ingresos_operativos.md` | Corregir enlaces, periodo, universo, objetivo, variable derivada y metas frente a resultados; conservar contexto histórico explícito. | T01–T02 |
| `preprocessing/preprocessing.py` | Hacer explícitas reglas de faltantes/sentinelas, unidades de capacidad, universo sectorial y conciliación del objetivo; validar claves y producir reporte de calidad. | T03–T05 |
| `preprocessing/README.md`, `preprocessing/bitacora_preprocesamiento.json` | Documentar reglas/contajes reales y serializar bitácora con versión de entrada, decisiones y controles. | T03–T05 |
| `models/train.py` | Definir partición reproducible, prevención de fuga, métricas en log y Bs bien etiquetadas, subgrupos, intervalos calibrados y criterios de selección. | T06–T08 |
| `models/drift.py` | Separar prueba simulada de medición real, usar referencia versionada y reportar tamaño/ventana de muestra. | T17 |
| `dashboard/telemetry.py` (nuevo), `dashboard/telemetry.jsonl` (generado) | Telemetría real persistida: registro JSONL de peticiones a predicción, resumen de tráfico con ventana y N, y medición de drift sobre insumos reales. | T17 |
| `models/README.md`, `models/bitacora_modelos.json`, `models/reference_stats.json` | Registrar protocolo, resultados, fecha, cobertura de intervalos y referencia de monitoreo; no mezclar ejecuciones. | T07–T09, T17 |
| `notebooks/comparacion_modelos.ipynb` | Definir función exploratoria o alinear con el entrenamiento canónico; eliminar la competencia de bitácoras para una misma vista. | T09 |
| `dashboard/artifacts/registry.json`, `best_model.joblib`, `cv_results.json`, `test_predictions.csv`, `feature_importance.json`, ambas bitácoras | Empaquetar o generar todo desde una ejecución identificada; validar esquema, hash y consistencia al cargar; no editar artefactos manualmente. | T09–T10 |
| `dashboard/data_loader.py` | Una capa de agregación con filtros y denominadores comunes; `null` para celdas sin observaciones y control de subgrupos pequeños. | T04, T10–T11 |
| `dashboard/app.py` | Contratos de API, validación de predicción, respuestas y errores, procedencia, intervalos calibrados; acceso a detalle individual, retiro de indicadores simulados de vistas reales. | T10–T12, T17 |
| `dashboard/static/js/app.js` | Renderizar gráficos según contratos, unidades y N; controlar filtros, estados y errores; evitar métricas incomparables en un mismo eje. | T13–T16, T17 |
| `dashboard/templates/index.html` | Reorganizar recorrido: resumen y calidad → exploración → modelos y diagnósticos → predicción → monitoreo; títulos, notas, accesibilidad. | T13–T16 |
| `dashboard/static/css/styles.css` | Escalas, leyendas, tablas, señales de muestra pequeña y diseño adaptable; contraste y foco de teclado. | T13–T16 |
| `dashboard/README.md`, `dashboard/requirements.txt`, `dashboard/run_server.py` | Guía de ejecución y configuración, dependencia reproducible y modo de despliegue con mensajes de limitación. | T18–T19 |
| `tests/test_data_contract.py` (nuevo), `tests/test_model_evaluation.py` (nuevo), `tests/test_api_contract.py` (nuevo), `tests/test_dashboard_smoke.py` (nuevo), `tests/integracion/prueba_a10_drift_detectado.py` (nuevo), `tests/integracion/prueba_a10_sin_drift.py` (nuevo) | Pruebas de propiedades estadísticas, integración y vistas principales; crear solo cuando la lógica correspondiente exista. | T05, T08, T12, T16, T17, T18 |
| `docs/implementacion/*`, `scripts/verificar_plan.ps1` | Mantener trazabilidad, evidencia y control de puertas. | Todas |

Si durante la implementación aparece un archivo nuevo, añadirlo a esta tabla y asignarlo a una tarea antes de marcarla completa. No se considera aceptado un cambio aislado de presentación sin revisar la agregación que alimenta la vista.
