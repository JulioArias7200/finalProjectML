# Contratos de datos, modelo y servicio

## Cadena reproducible

`CSV original + diccionario y reglas` → `preprocesamiento versionado` → `dataset modelable + informe de calidad` → `partición/pruebas + entrenamiento` → `paquete inmutable de artefactos` → `API` → `gráficos` → `telemetría real`.

Cada salida lleva `run_id`, fecha, hash de entrada, versión de esquema y cantidad de filas. El `registry.json` del paquete activo referencia los hashes y rutas de modelo, predicciones de prueba, CV, importancia y bitácoras. El servidor carga el paquete de forma atómica; si un archivo falta o difiere su `run_id`, responde error de preparación en vez de mezclar ejecuciones. El notebook es análisis exploratorio, sin sustituir al generador canónico.

## Contrato estadístico

- Unidad observacional: empresa en el extracto general; materiales pueden tener varias filas por empresa. Unir solo tras comprobar unicidad, cardinalidad y cobertura de claves.
- Objetivo: elegir formalmente `S00_01_A` o `S05_04` en `D01` y guardar ambos en la conciliación. Tolerancia preliminar de Bs 1 para redondeo, sujeta a prueba documental y de datos. No presentar identidad exacta.
- Variables: inventario de 152 campos de encuesta y 15 derivados locales. Para cada predictor registrar disponibilidad en el momento de predicción, unidad, porcentaje de faltantes, tratamiento y posible relación algebraica con el objetivo. Rechazar fuga de información y montos que sean componentes directos del ingreso objetivo salvo justificación formal.
- Capacidad: `S12_*_B` es cantidad; `S12_*_C` identifica unidad. No sumar cantidades heterogéneas ni imputar ausencia con cero sin fundamento.
- Universo: distinguir 13 sectores observados localmente de categorías teóricas del mapeo. Filtrado y resultados se limitan a datos observados. Mostrar N y denominador; “sin datos” se representa con `null`, no con cero.
- Entrenamiento: fijar semilla y partición antes de ajuste de transformadores; comparar modelos con CV sobre entrenamiento. Reservar prueba final intacta. Registrar métricas R²/MAE/RMSE/MedAPE en su escala indicada, conteos y distribución de errores por sector/departamento y rangos de ingreso. Verificar si MedAPE es estable ante objetivos cercanos a cero.
- Incertidumbre: el intervalo predictivo nominal se calcula y calibra con un procedimiento reproducible sobre datos separados de entrenamiento; medir cobertura empírica y amplitud total y por subgrupos. `±1,645 × RMSE(log)` sin calibración no se etiqueta “intervalo 90 %”.
- Bunching, atípicos y “riesgo”: son señales descriptivas o estadísticas; no acusaciones ni evidencia de incumplimiento. Definir fórmula, umbral, sensibilidad y falsos positivos antes de usar etiquetas.

## Contrato mínimo de API

Todas las respuestas analíticas incluyen `meta: {run_id, dataset_id, periodo, poblacion, n, filtros, unidad, escala, generated_at, limitaciones}`. Para datos agregados, los valores ausentes se serializan como JSON `null`; `0` significa cero observado. Cada métrica presenta nombre, valor, unidad/escala y denominador. Una petición con filtros no válidos devuelve 400 y detalle comprensible; fallos de paquete activo devuelven 503.

Endpoints actuales a adaptar: `/api/kpis`, `/api/eda/*`, `/api/models`, `/api/cross_validation`, `/api/predict`, `/api/mlops`, `/api/mlops/monitoring`, `/api/mlops/drift`, `/api/empresas_riesgo*` y `/api/bunching_alerta`. El contrato puede versionarse como `/api/v1/*` con adaptación temporal, sujeto a `D03`. `/api/predict` debe validar tipos, rangos, categorías conocidas y qué variables están realmente disponibles; responder versión, predicción en Bs, incertidumbre y limitación de uso. Las rutas individuales no se habilitan públicamente sin resolver `D04`.

## Regla de consistencia de filtros

Una vista filtrada calcula su numerador, denominador, N de subgrupo y etiquetas desde el mismo conjunto. Los totales, mapas, tablas y exportaciones comparten esta selección. La comparación de modelos y diagnósticos de prueba conserva explícitamente su cohorte fija de evaluación; no se recalcula como si fuera una muestra filtrada de producción.
