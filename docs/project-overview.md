# Proyecto EDSA 2023: priorización sanitaria con Machine Learning

## Propósito

Este proyecto universitario utiliza los módulos de la Encuesta de Demografía y Salud (EDSA) 2023 para construir y comparar modelos de Machine Learning orientados a la **priorización de seguimiento sanitario**. El trabajo no pretende sustituir una valoración médica, emitir diagnósticos ni establecer relaciones causales. Su resultado es una estimación estadística que puede orientar dónde conviene concentrar mediciones, seguimiento u orientación profesional.

La EDSA es una encuesta transversal y contiene módulos con poblaciones y unidades de observación diferentes. Por esa razón, el proyecto no combinará indiscriminadamente todas las tablas en un único conjunto de datos. Cada modelo tendrá una población, etiqueta, unidad de análisis, conjunto de predictores y métricas propios.

## Alcance acordado

Para conservar un alcance realizable y, al mismo tiempo, demostrar técnicas de clasificación y regresión, se implementarán como máximo dos modelos:

| ID | Modelo | Pregunta analítica | Tipo de aprendizaje |
|---|---|---|---|
| M1 | Priorización de anemia en mujeres | ¿Qué características disponibles antes de medir hemoglobina se asocian con una mayor probabilidad de anemia en mujeres de 12 a 49 años? | Clasificación binaria supervisada |
| M10 | Controles prenatales | ¿Qué características disponibles de la madre y del contexto permiten estimar el número de controles prenatales de un nacimiento registrado? | Regresión supervisada de conteo |

El M1 es el modelo principal, por estar más alineado con el problema de identificación de riesgo de anemia documentado en el proyecto. M10 complementa el trabajo con un problema de regresión y evita forzar regresión lineal o polinomial sobre una etiqueta binaria.

## Fuentes de datos y relaciones

Los archivos fuente se mantienen sin cambios. Las tablas analíticas se crearán como salidas nuevas fuera de las fuentes originales.

| Archivo | Unidad | Uso en el alcance |
|---|---|---|
| `EDSA2023_Peso_talla_hemo.csv` | Persona medida | Etiqueta y universo elegible de M1. |
| `EDSA2023_Mujer.csv` | Mujer entrevistada | Predictores sociodemográficos, reproductivos y de acceso para M1; contexto materno para M10. |
| `EDSA2023_Hogar.csv` | Persona del hogar | Predictores individuales auxiliares para M1. |
| `EDSA2023_Vivienda.csv` | Vivienda | Contexto material y territorial para M1. |
| `EDSA2023_HistorialParidad.csv` | Embarazo/nacimiento | Base de eventos y objetivo numérico de M10. |

Las claves comunes son `folio` (vivienda) y `folio+nro` (persona o mujer). `Vivienda` se une por `folio`; Mujer, Hogar y Peso/Talla/Hemoglobina se unen por `folio+nro`. HistorialParidad puede tener varios eventos por mujer: no se deduplicará si la unidad final es un nacimiento.

## Definición de los modelos

### M1: anemia en mujeres

- **Unidad de análisis:** una mujer de 12 a 49 años con resultado válido de hemoglobina/anemia.
- **Etiqueta original:** `tip_anemia_m` en `Peso_talla_hemo`.
- **Etiqueta derivada:** `anemia_mujer = 0` para “sin anemia”; `1` para anemia leve, moderada o severa.
- **Ponderador descriptivo:** `ponderador_mhm`. Su uso para entrenamiento será documentado y diferenciado de la estimación poblacional.
- **Predictores candidatos:** edad, educación, embarazo, área, región, departamento, afiliación o acceso a salud, estado conyugal, condiciones del hogar, agua, saneamiento, combustible, calidad de vivienda y riqueza.
- **Exclusiones obligatorias por fuga de información:** `tip_anemia_m`, hemoglobina (`hs06_0120`), cualquier derivado directo de hemoglobina, peso, talla, IMC si la priorización ocurre antes de medir; además de `folio`, `nro`, `upm` y otras claves administrativas.

La documentación existente reporta 5.375 mujeres con resultado válido y una prevalencia observada aproximada de anemia de 54,87 %. Un AUC previo cercano a 0,57 debe considerarse una línea base modesta: el objetivo académico es evaluar rigurosamente el proceso, no afirmar capacidad clínica.

### M10: número de controles prenatales

- **Unidad de análisis:** un embarazo o nacimiento registrado desde 2018.
- **Etiqueta candidata:** `ms04_0411`, número de controles prenatales; se validará el significado y rango en el diccionario antes de modelar.
- **Tipo:** variable de conteo no negativa. Se evaluará regresión lineal como base académica y, si la distribución lo exige, un modelo de Poisson como alternativa metodológicamente adecuada.
- **Predictores candidatos:** edad y educación de la madre, área, región, departamento, estado conyugal, antecedentes reproductivos anteriores al evento y variables contextuales válidas temporalmente.
- **Exclusiones:** variables ocurridas durante o después del parto que no estarían disponibles al momento de anticipar los controles; identificadores directos.

## Métodos que se demostrarán

| Familia | M1 clasificación | M10 regresión | Propósito |
|---|---|---|---|
| Modelo base | Regresión logística | Regresión lineal | Referencia simple e interpretable. |
| Regresión no lineal | No corresponde usar regresión polinomial para etiqueta binaria | Regresión polinomial de grado 2 | Evaluar curvatura sin sobreajustar. |
| Árbol | Árbol de decisión | Árbol de regresión | Reglas o segmentos fáciles de explicar. |
| Bagging | Random Forest Classifier | Random Forest Regressor | Ensamble de árboles con reducción de varianza. |
| Boosting | Gradient Boosting / XGBoost si está disponible | Gradient Boosting Regressor | Capturar patrones no lineales e interacciones. |

El llamado “A/B testing” será una **comparación experimental offline**: A será el modelo base y B un modelo alternativo, evaluados con el mismo conjunto de prueba congelado. No se realizará un experimento sobre pacientes ni se asignarán intervenciones sanitarias.

## Entregables previstos

1. Tablas analíticas reproducibles para M1 y M10.
2. Diccionario técnico de variables, transformaciones, universo y motivo de exclusión.
3. Reporte de calidad de datos por modelo.
4. Pipelines reproducibles de preprocesamiento y entrenamiento.
5. Comparación de modelos y métricas en validación y prueba.
6. Informe de resultados, limitaciones, sesgos potenciales y recomendaciones de uso responsable.

## Límites éticos y metodológicos

- Un resultado del modelo es una prioridad o probabilidad, no un diagnóstico.
- La encuesta es transversal: asociación no significa causalidad.
- Los faltantes de la encuesta suelen ser estructurales por saltos del cuestionario; no equivalen automáticamente a cero.
- Las métricas deben informarse por subgrupos territoriales y sociodemográficos cuando el tamaño muestral lo permita.
- Los identificadores se conservarán únicamente en auditoría; no ingresarán a la matriz de características.
