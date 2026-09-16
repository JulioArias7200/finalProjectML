# Escenarios de prueba y validación

## 1. Pruebas de estructura y claves

| ID | Escenario | Procedimiento | Resultado esperado |
|---|---|---|---|
| TS-01 | Unicidad de vivienda | Contar `folio` en Vivienda antes del join. | Una fila por folio; excepciones investigadas. |
| TS-02 | Unicidad de persona M1 | Contar `folio+nro` en el universo de anemia válida. | Una fila por mujer; duplicados no resueltos bloquean el entrenamiento. |
| TS-03 | Eventos repetidos M10 | Contar eventos por `folio+nro`. | Varias filas por mujer permitidas; no se eliminan automáticamente. |
| TS-04 | Cardinalidad de joins | Comparar filas antes y después de cada merge. | M1 no debe multiplicar personas; M10 no debe multiplicar eventos. |
| TS-05 | Cobertura de join | Medir porcentaje sin correspondencia. | Se reporta y decide explícitamente si excluir, conservar o imputar contexto. |

## 2. Pruebas de etiquetas

| ID | Escenario | Procedimiento | Resultado esperado |
|---|---|---|---|
| TS-06 | Mapeo de anemia | Tabular `tip_anemia_m` contra `anemia_mujer`. | Sin anemia = 0; leve/moderada/severa = 1; inválidos fuera del entrenamiento. |
| TS-07 | Etiqueta M1 faltante | Buscar nulos de `anemia_mujer`. | Cero nulos en la tabla de entrenamiento. |
| TS-08 | Rango prenatal | Revisar mínimo, máximo y códigos especiales de controles. | Valores no negativos y plausibles; códigos especiales separados. |
| TS-09 | Ceros reales | Confirmar que cero controles no se confundió con “no sabe” o “no aplica”. | Clasificación documentada y verificable. |

## 3. Pruebas de limpieza

| ID | Escenario | Procedimiento | Resultado esperado |
|---|---|---|---|
| TS-10 | Categorías equivalentes | Revisar variantes de Sí/No y espacios. | Una codificación consistente por categoría. |
| TS-11 | Faltante estructural | Revisar una variable condicionada por salto. | No se convierte automáticamente a cero. |
| TS-12 | Rango de edad | Verificar mínimos, máximos y universo de M1. | Solo mujeres en el rango definido y valores plausibles. |
| TS-13 | Valores extremos | Revisar percentiles de variables numéricas. | Extremos investigados; no se eliminan sin regla. |
| TS-14 | Variables casi vacías | Calcular faltantes por predictor. | Exclusión o tratamiento con justificación escrita. |

## 4. Pruebas contra fuga de información

| ID | Escenario | Procedimiento | Resultado esperado |
|---|---|---|---|
| TS-15 | Lista prohibida M1 | Buscar hemoglobina, anemia, IMC, peso y talla en `X`. | Ninguna variable prohibida está presente. |
| TS-16 | Identificadores | Buscar `folio`, `nro`, `upm` y claves derivadas en `X`. | No están en la matriz de predictores. |
| TS-17 | Temporalidad M10 | Revisar cada predictor contra el momento del evento. | No hay variables posteriores al control/parto si se pretende predecir antes. |
| TS-18 | Contaminación test | Verificar ajuste de imputador/escalador. | Se ajustan con train exclusivamente. |

## 5. Pruebas de modelado

| ID | Escenario | Procedimiento | Resultado esperado |
|---|---|---|---|
| TS-19 | Reproducibilidad | Ejecutar dos veces con misma semilla. | Misma partición y métricas equivalentes. |
| TS-20 | Estratificación M1 | Comparar proporción de anemia en particiones. | Proporciones similares a la población analítica. |
| TS-21 | Agrupación M10 | Confirmar que eventos de una mujer no aparecen en train y test. | Separación por grupo cuando existan múltiples eventos. |
| TS-22 | Baseline M1 | Entrenar logística. | AUC y métricas registradas. |
| TS-23 | Baseline M10 | Entrenar lineal. | MAE, RMSE y R² registrados. |
| TS-24 | Bagging y boosting | Entrenar y validar alternativas. | Parámetros, tiempo y métricas comparables. |
| TS-25 | A/B offline | Evaluar A y B en el mismo test. | Comparación final justa y reproducible. |

## 6. Pruebas de resultados responsables

| ID | Escenario | Procedimiento | Resultado esperado |
|---|---|---|---|
| TS-26 | Calibración M1 | Gráfico de calibración y Brier score si se implementa. | Probabilidades interpretables o limitación documentada. |
| TS-27 | Subgrupos M1 | Métricas por área/región/edad con muestra suficiente. | Se identifican posibles brechas. |
| TS-28 | Residuales M10 | Graficar residuales y predicción vs. valor real. | Sesgos, heterocedasticidad o negativos quedan documentados. |
| TS-29 | Privacidad | Inspeccionar outputs. | Ningún identificador aparece en el informe final. |
| TS-30 | Lenguaje de conclusión | Revisar informe. | Usa “riesgo/prioridad/asociación”, no “diagnóstico/causa”. |
