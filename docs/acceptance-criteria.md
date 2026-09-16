# Criterios de aceptación

## A. Criterios de datos

| ID | Criterio verificable | Evidencia requerida |
|---|---|---|
| AC-01 | Las fuentes originales no fueron modificadas. | Comparación de nombres/tamaños o registro de solo lectura. |
| AC-02 | M1 contiene una fila por mujer con etiqueta de anemia válida. | Conteo de filas, duplicados de `folio+nro` y distribución de `anemia_mujer`. |
| AC-03 | M10 contiene una fila por evento/nacimiento válido, no una fila agregada por mujer. | Conteo de eventos y revisión de claves repetidas permitidas. |
| AC-04 | Todo join tiene reporte de filas antes/después, matches y no matches. | Reporte de integración. |
| AC-05 | Faltantes y códigos especiales están clasificados y documentados. | Diccionario técnico y reporte de calidad. |
| AC-06 | No hay identificadores ni fuga de información en las matrices `X`. | Lista de predictores y revisión manual. |
| AC-07 | El conjunto de prueba se separó antes de entrenar imputadores, codificadores, escaladores o modelos. | Código/pipeline reproducible. |

## B. Criterios de modelos

| ID | Criterio verificable | Evidencia requerida |
|---|---|---|
| AC-08 | M1 compara al menos logística, Random Forest y Gradient Boosting. | Tabla de validación con parámetros y métricas. |
| AC-09 | M10 compara lineal, polinomial grado 2, Random Forest y Gradient Boosting. | Tabla de validación con parámetros y métricas. |
| AC-10 | Cada modelo tiene un baseline explícito. | Definición de A en el informe. |
| AC-11 | A y B se evalúan sobre la misma prueba reservada. | Tabla A/B de test y semilla registrada. |
| AC-12 | M1 reporta AUC-ROC, sensibilidad, especificidad, precisión, F1 y matriz de confusión. | Reporte de evaluación. |
| AC-13 | M10 reporta MAE, RMSE y R². | Reporte de evaluación. |
| AC-14 | La selección final no se justifica exclusivamente con accuracy o R². | Discusión de métricas, calibración/error e interpretación. |

## C. Criterios de análisis responsable

| ID | Criterio verificable | Evidencia requerida |
|---|---|---|
| AC-15 | M1 analiza desempeño por subgrupos cuando exista muestra suficiente. | Tabla por área, región o edad; o justificación de tamaño insuficiente. |
| AC-16 | El informe declara que el modelo no diagnostica ni prueba causalidad. | Sección de limitaciones. |
| AC-17 | Las variables más influyentes son interpretadas como asociaciones, no causas. | Gráfico/importancias y discusión. |
| AC-18 | Identificadores personales no aparecen en resultados públicos. | Revisión de tablas, figuras y anexos. |

## D. Definición de terminado

El proyecto se considera terminado si todos los criterios AC-01 a AC-18 tienen estado “cumple” o cuentan con una justificación escrita, verificable y aprobada por el equipo docente. Un modelo con métrica alta no compensa una falla de fuga de información, partición incorrecta o falta de trazabilidad.
