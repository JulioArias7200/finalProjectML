# Requisitos del proyecto

## 1. Requisitos funcionales

### RF-01. Conservación de fuentes

Los CSV y SAV originales de EDSA 2023 son fuentes inmutables. Ningún proceso debe sobrescribirlos, recodificarlos en sitio ni eliminar columnas de ellos.

### RF-02. Dos tablas analíticas independientes

El proyecto debe producir una tabla para M1 y otra para M10. Cada una tendrá una sola unidad de análisis, una etiqueta explícita y trazabilidad de las fuentes utilizadas.

### RF-03. Construcción de la etiqueta M1

La tabla M1 debe incluir `anemia_mujer` derivada exclusivamente de `tip_anemia_m`:

| Valor original | Valor derivado |
|---|---:|
| Sin anemia | 0 |
| Anemia leve, moderada o severa | 1 |
| Sin resultado, no aplicable o código no válido | Excluir del universo de entrenamiento |

### RF-04. Construcción de la etiqueta M10

La tabla M10 debe incluir el número de controles prenatales validado desde `ms04_0411` u otra variable formalmente aprobada. Se deben excluir o registrar por separado los valores imposibles, desconocidos o no aplicables.

### RF-05. Uniones controladas

- M1 unirá persona a persona por `folio+nro` y vivienda por `folio`.
- Antes de cada unión se verificará unicidad de la clave esperada.
- M10 se conservará al nivel de evento; no se eliminarán eventos solo porque una mujer tenga más de uno.
- Cada unión debe producir un reporte de coincidencias, no coincidencias y cambio de filas.

### RF-06. Prevención de fuga de información

Los predictores no deben contener el resultado ni información derivada de este. M1 excluirá hemoglobina, categorías de anemia, peso, talla e IMC cuando se modela el riesgo antes de medición. M10 excluirá campos capturados después del momento que se desea anticipar.

### RF-07. Preprocesamiento reproducible

El preprocesamiento debe estar implementado mediante un script, notebook limpio o transformación Pentaho documentada. Debe incluir lectura, validación, limpieza, integración, partición y guardado de resultados.

### RF-08. Modelos mínimos

M1 deberá comparar regresión logística, un método bagging y un método boosting. M10 deberá comparar regresión lineal, regresión polinomial de grado 2, un método bagging y un método boosting.

### RF-09. Comparación A/B offline

Cada modelo debe definir un experimento A/B académico:

- A: modelo base (logístico para M1 y lineal para M10).
- B: mejor alternativa seleccionada en validación.
- Ambos se miden en el mismo conjunto de prueba sin cambios posteriores.

### RF-10. Informe de métricas

M1 reportará como mínimo AUC-ROC, sensibilidad, especificidad, precisión, F1 y matriz de confusión. M10 reportará MAE, RMSE y R². Todos los resultados deben indicar muestra, partición y fecha de ejecución.

## 2. Requisitos de calidad de datos

Un dataset estará apto para modelar solo si cumple simultáneamente lo siguiente:

1. La unidad de análisis está declarada y hay una fila por unidad esperada.
2. La etiqueta no es nula, ambigua ni calculada con un predictor incluido en `X`.
3. Las claves tienen duplicados únicamente cuando estos son válidos para la unidad elegida.
4. Las categorías están normalizadas y sus códigos especiales están documentados.
5. Los faltantes se clasifican como estructurales, no respuesta, no sabe, no aplicable o ausencia real cuando sea posible.
6. Las variables numéricas tienen rangos plausibles y valores extremos revisados.
7. No hay fuga de información, identificadores directos ni variables posteriores al evento.
8. El procesamiento de imputación, codificación y escalado se ajusta solo con entrenamiento.
9. La distribución del objetivo se conoce por partición y, para M1, está estratificada.
10. Existe un reporte reproducible que evidencia todos los controles anteriores.

## 3. Requisitos no funcionales

- **Reproducibilidad:** fijar semilla aleatoria, registrar versiones de bibliotecas y rutas relativas.
- **Trazabilidad:** documentar el origen de toda variable derivada y cada exclusión de filas.
- **Seguridad:** no publicar `folio`, `nro` u otros identificadores de encuestados en visualizaciones o informes públicos.
- **Interpretabilidad:** incluir un modelo base interpretable y explicación de variables relevantes.
- **Equidad:** comparar, cuando haya tamaño suficiente, rendimiento de M1 por área, región y grupos de edad.
- **Alcance:** no implementar más de los dos modelos definidos sin actualizar formalmente este documento.

## 4. Requisitos técnicos sugeridos

- Python 3 con `pandas`, `scikit-learn`, `numpy`, `matplotlib` y `seaborn`.
- Opcional: `xgboost` o `lightgbm` si se encuentran instalados; si no, usar `HistGradientBoosting` de scikit-learn.
- Pipelines de scikit-learn con `ColumnTransformer` para evitar contaminación entre train, validación y test.
- Archivos de salida separados de las fuentes: datos procesados, modelos y reportes.
