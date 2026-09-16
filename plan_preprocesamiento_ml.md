# Plan de preprocesamiento para Machine Learning

## 1. Objetivo del proyecto

El objetivo principal es construir modelos que ayuden a **priorizar la medicion y el seguimiento de personas con riesgo de anemia y riesgo metabolico**, en respuesta al arbol de problemas del proyecto.

El modelo no debe diagnosticar por si solo. Debe producir una prioridad de seguimiento para que el personal responsable confirme el resultado mediante medicion y criterio clinico.

Se trabajara con varios modelos separados por poblacion y objetivo:

1. Riesgo de anemia en mujeres de 12 a 49 anos.
2. Riesgo de anemia en ninas/os de 6 meses a menores de 6 anos.
3. Riesgo metabolico en mujeres con medicion antropometrica valida.
4. Riesgo metabolico en hombres con medicion antropometrica valida.
5. Riesgo de problemas de salud en personas del hogar.
6. Cobertura de vacunacion, lactancia y desarrollo en primera infancia.
7. Acceso a salud, salud sexual y reproductiva en mujeres.
8. Salud sexual, reproductiva y violencia en hombres.

No se recomienda entrenar un unico modelo que mezcle mujeres, hombres, ninas/os, viviendas y eventos reproductivos, porque sus unidades de observacion, edades, cuestionarios y universos son diferentes. El proyecto tendra un conjunto de modelos coordinados, con una tabla de resultados comun: `folio`, `nro`, poblacion, objetivo, probabilidad, nivel de prioridad y fecha de generacion.

## 2. Bases que sirven y bases que no deben mezclarse directamente

| Base | Uso recomendado | Decision |
|---|---|---|
| `EDSA2023_Peso_talla_hemo.csv` | Resultados objetivo de anemia, IMC, peso, talla y hemoglobina. Incluye ponderadores especificos. | **Base principal** para M1-M4. |
| `EDSA2023_Mujer.csv` | Edad, educacion, embarazo, SUS, enfermedades declaradas, actividad, salud sexual y reproductiva, area y region. | **Predictores** para anemia femenina y riesgo metabolico femenino. |
| `EDSA2023_Hogar.csv` | Caracteristicas de personas, educacion, seguro, visitas a salud y elegibilidad. | **Predictores auxiliares**, unido por `folio+nro`. |
| `EDSA2023_Vivienda.csv` | Agua, saneamiento, combustible, materiales, calidad y riqueza de la vivienda. | **Predictores contextuales**, unido por `folio`. |
| `EDSA2023_PrimeraInfancia.csv` | Lactancia, vacunacion, nutricion, desarrollo, enfermedades y cuidados infantiles. | **Modelo infantil auxiliar**; unir solo con la poblacion infantil correspondiente. |
| `EDSA2023_MujerCalendario.csv` | Uso mensual de metodos anticonceptivos entre 2018 y 2023. | Util para un modelo de planificacion familiar, no para mezclarlo con anemia sin una pregunta especifica. |
| `EDSA2023_HistorialParidad.csv` | Controles prenatales, parto y puerperio de nacimientos desde enero de 2018. | Util para un modelo materno-infantil o de atencion prenatal. No es una tabla de personas unica. |
| `EDSA2023_HistorialHijos.csv` | Historial de nacimientos, supervivencia y mortalidad infantil. | Util para fecundidad/mortalidad. Mantener en formato largo; no usar como tabla individual sin agregar antes. |
| `EDSA2023_Hombre.csv` | Salud, actividad, reproduccion, violencia y anticoncepcion masculina. | Usar para un modelo masculino separado; no introducirlo en el modelo de mujeres. |

### Modelos que se deben desarrollar

| Modelo | Poblacion | Objetivo | Base objetivo | Salida |
|---|---|---|---|---|
| M1 | Mujeres de 12-49 anos | Anemia | `tip_anemia_m` | Probabilidad de anemia y prioridad de medicion |
| M2 | Ninas/os de 6 meses a menores de 6 anos | Anemia infantil | `tip_anemia` | Probabilidad de anemia y prioridad de seguimiento |
| M3 | Mujeres con IMC valido | Sobrepeso/obesidad | `categaimc_m` | Riesgo metabolico femenino |
| M4 | Hombres con IMC valido | Sobrepeso/obesidad | `categaimc_h` | Riesgo metabolico masculino |
| M5 | Personas del hogar | Problema de salud reciente | `hs03_0033` | Probabilidad de reportar un problema reciente |
| M6 | Ninas/os de primera infancia | Vacunacion completa | `pobvacin`, `vac_valid` y variables `ps05_0502_*` | Riesgo de esquema incompleto |
| M7 | Ninas/os de primera infancia | Desarrollo infantil | `idit` | Probabilidad de hitos no alcanzados |
| M8 | Mujeres entrevistadas | Registro/uso de SUS | `ms05_0506`, `ms05_0507` | Probabilidad de brecha de acceso |
| M9 | Hombres entrevistados | Uso de condon o acceso a salud sexual | `vs04_0417`, `vs04_0432` o variable definida | Prioridad de educacion y acceso |
| M10 | Mujeres con nacimiento desde 2018 | Control prenatal y atencion del parto | variables de `HistorialParidad` | Riesgo de atencion prenatal insuficiente |

Los modelos M5 a M10 son modelos de apoyo al diagnostico social y de gestion, no instrumentos clinicos. Cada uno requiere definir previamente su universo y una variable objetivo binaria o multicategoria.

### Reglas de union

- `Vivienda` se une con `Hogar` por `folio`.
- `Mujer`, `Hombre`, `PrimeraInfancia` y `Peso_talla_hemo` se unen por `folio+nro`, verificando primero que no se multipliquen filas.
- `HistorialHijos` y `HistorialParidad` son tablas uno-a-muchos. No se deben deduplicar. Si se necesitan como predictores individuales, primero hay que crear agregados como numero de hijos, ultimo ano de nacimiento o numero de controles prenatales.
- `folio`, `nro`, `upm` y otros identificadores se conservan para auditoria y union, pero se eliminan de `X` antes de entrenar.

## 3. Variables objetivo

### 3.1 Anemia femenina

Base de resultado: `Peso_talla_hemo`.

- Resultado original: `tip_anemia_m`.
- Positivo: `2. LEVE`, `3. MODERADA` o `4. SEVERA`.
- Negativo: `1. SIN ANEMIA`.
- Excluir del modelo las filas sin resultado valido.
- Ponderador poblacional: `ponderador_mhm`.
- No usar como predictor `hs06_0120`, `tip_anemia_m` ni variables calculadas directamente a partir de hemoglobina.

En el perfil realizado hay 5,375 mujeres con resultado valido y 54.87% presentan alguna anemia. El modelo inicial obtuvo AUC 0.57; por tanto, esta fase debe considerarse una linea base y no una herramienta clinica terminada.

### 3.2 Anemia infantil

- Resultado original: `tip_anemia`.
- Positivo: anemia leve, moderada o severa.
- Negativo: `1. SIN ANEMIA`.
- Ponderador: `ponderador_nhm`.
- No usar `hs06_0127`, `tip_anemia` ni variables derivadas del mismo resultado como predictores.
- Usar edad en meses, lactancia, alimentacion, vacunacion, enfermedades, desarrollo, area y contexto del hogar.

### 3.3 Riesgo metabolico

Se pueden construir dos objetivos, sin mezclarlos:

- Mujeres: `categaimc_m` o un indicador de `TOTAL SOBREPESO OBESA`.
- Hombres: `categaimc_h` o un indicador de `TOTAL SOBREPESO OBESO`.

Los modelos deben ser separados por sexo porque las variables y ponderadores cambian:

- Mujeres: `ponderador_mpt`.
- Hombres: `ponderador_vpt`.

No usar `imc_m`, `imc_h`, `categimc_m`, `categimc_h` ni el peso/talla usado para calcular el IMC si el objetivo es predecir el propio IMC. Eso seria fuga de informacion. Si el objetivo es detectar riesgo antes de medir, las mediciones antropometricas deben quedar fuera de `X`.

### 3.4 Personas del hogar: problemas de salud recientes

Base: `EDSA2023_Hogar.csv`.

- Objetivo sugerido: `hs03_0033`, que identifica si la persona tuvo un problema de salud en los ultimos tres meses.
- Positivo: `1. SI`; negativo: `2. NO`.
- Predictores posibles: edad, sexo, educacion, seguro, area, region, afiliacion, discapacidad, atencion recibida y caracteristicas de vivienda.
- No usar como predictor `hs03_0034_*` si el objetivo es anticipar la existencia del problema, porque esas variables describen el tipo de problema posterior a la respuesta objetivo.
- Para un segundo modelo se puede predecir el tipo de problema, pero debe ser multiclasificacion y entrenarse solo entre quienes respondieron positivamente.
- Ponderador: `ponderadorhviv` o el factor correspondiente definido para el analisis del hogar.

### 3.5 Primera infancia: vacunacion y desarrollo

Base: `EDSA2023_PrimeraInfancia.csv`.

- Vacunacion: construir `vacunacion_incompleta` a partir del carnet, `pobvacin`, `vac_valid` y las variables `ps05_0502_*`; separar claramente ausencia de carnet de vacuna no recibida.
- Desarrollo: usar `idit` como resultado solo cuando tenga valor valido; `1. HITOS ALCANZADOS` es negativo y `0. HITOS NO ALCANZADOS` es positivo.
- Predictores: edad en meses, sexo, cuidador principal, educacion del cuidador, tiempo de cuidado, actividades de estimulacion, libros, lactancia, alimentacion, enfermedades y caracteristicas del hogar.
- No usar como predictor los mismos hitos que componen `idit` cuando el objetivo sea predecir el indice completo.
- Ponderador: `ponderador`.
- La edad en meses es obligatoria para comparar desarrollo y vacunacion con el esquema que corresponde a cada edad.

### 3.6 Mujeres: acceso a SUS y salud reproductiva

Base: `EDSA2023_Mujer.csv`, con apoyo de `Hogar` y `Vivienda`.

- Acceso al SUS: definir modelos separados para registro (`ms05_0506`) y atencion recibida desde 2018 (`ms05_0507`); no combinar ambas respuestas en una sola etiqueta.
- Predictores: area, region, departamento, edad, educacion, afiliacion, riqueza, calidad de vivienda, distancia o dificultades de acceso, embarazo y tipo de atencion recibida.
- Salud sexual y reproductiva: usar `ms03_0312` y las variables `ms03_0313_*` para uso actual de anticoncepcion, recordando que son respuestas multiples y deben convertirse en indicadores binarios por metodo.
- Ponderador: `ponderadorm`.
- No usar variables de resultado o de seguimiento posteriores al evento que se intenta anticipar.

### 3.7 Hombres: salud sexual y violencia

Base: `EDSA2023_Hombre.csv`.

- Definir un objetivo por estudio: uso de condon en la ultima relacion (`vs04_0417`), conocimiento/acceso a condones (`vs04_0432`), violencia de pareja o agresion sexual, segun la pregunta de investigacion aprobada.
- Predictores: edad, educacion, actividad laboral, estado conyugal, area, region, conocimiento de VIH/ITS, acceso a servicios y caracteristicas del hogar.
- No mezclar respuestas de violencia masculina con las de mujeres; son cuestionarios distintos y sus variables no son equivalentes automaticamente.
- Ponderador: identificar y documentar el ponderador masculino disponible en el archivo antes de estimar resultados poblacionales.

### 3.8 Historial reproductivo y atencion prenatal

Bases: `HistorialParidad.csv`, `HistorialHijos.csv`, `Mujer.csv` y, cuando corresponda, `PrimeraInfancia.csv`.

- Mantener el historial en formato largo.
- Para un modelo por nacimiento, cada fila representa un embarazo/nacimiento y el resultado debe ser definido a ese nivel.
- Para un modelo por mujer, agregar primero: numero de nacimientos, ultimo ano de nacimiento, numero de controles prenatales promedio o del ultimo nacimiento, atencion profesional y lugar del parto.
- No unir directamente una tabla de eventos a una tabla de mujeres sin agregar, porque se duplicarian las mujeres y se sesgaria el entrenamiento.
- Variables posibles: `ms04_0407`, `ms04_0411`, `ms04_0427_*`, `ms04_0429`, `ms04_0436` y los derivados documentados `per_aten_prenat`, `lugar_parto`, `per_aten_parto`.
- Ponderador: `ponderadorm`, aplicado de acuerdo con la unidad final de analisis.

## 4. Diagnostico inicial de calidad

El perfil de los CSV muestra:

- `Mujer`: 14,545 filas, 1,341 variables y aproximadamente 72.9% de celdas faltantes.
- `Hombre`: 5,878 filas, 997 variables y aproximadamente 67.0% de faltantes.
- `Hogar`: 54,008 filas, 235 variables y aproximadamente 66.7% de faltantes.
- `Peso_talla_hemo`: 46,581 filas, 44 variables y aproximadamente 55.1% de faltantes.
- `PrimeraInfancia`: 5,529 filas, 490 variables y aproximadamente 58.7% de faltantes.
- `Vivienda`: 19,059 filas, 73 variables y aproximadamente 28.1% de faltantes.
- `MujerCalendario`: 14,545 filas, 77 variables y aproximadamente 2.9% de faltantes.

Estos porcentajes no justifican borrar automaticamente las columnas. En una encuesta con saltos, un valor faltante puede significar que la pregunta no correspondia a la persona.

### Tipos de problemas que se deben registrar

1. **Faltante estructural (`NA`):** la pregunta no aplicaba por edad, sexo, embarazo, elegibilidad o respuesta anterior.
2. **No sabe:** categoria explicita, por ejemplo `8. NO SABE`.
3. **No responde/no especificado:** categorias como `999. SIN ESPECIFICAR`.
4. **No medido:** rechazo, ausencia u otro resultado de medicion.
5. **Error de codificacion:** etiquetas textuales, caracteres alterados o valores fuera de rango.
6. **Duplicacion valida:** varias filas para una persona en historiales o varias personas dentro de un hogar.

## 5. Flujo correcto de preprocesamiento

### Paso 1. Congelar las fuentes

- Trabajar con los CSV originales como solo lectura.
- Crear una carpeta de salida, por ejemplo `datos_procesados/`.
- Guardar un registro de fecha, archivo de origen, filas, columnas y transformaciones aplicadas.
- No reemplazar los CSV originales.

### Paso 2. Crear un diccionario tecnico

Para cada variable registrar:

| Campo | Ejemplo |
|---|---|
| `dataset` | `EDSA2023_Mujer` |
| `variable` | `ms01_0101a` |
| `significado` | Edad en anos cumplidos |
| `tipo_original` | Numerica |
| `tipo_modelo` | Numerica |
| `universo` | Mujeres entrevistadas |
| `faltante_estructural` | Si/No |
| `transformacion` | Sin cambios, recodificacion o eliminacion |
| `motivo_exclusion` | Identificador, fuga, demasiada ausencia o irrelevante |

Los diccionarios organizados del proyecto son la fuente de los significados; el CSV es la fuente de los valores observados.

### Paso 3. Validar claves y duplicados

- Comprobar que `folio+nro` sea unico en `Mujer`, `Hombre`, `Hogar`, `PrimeraInfancia` y `MujerCalendario`.
- Comprobar que `folio` sea unico en `Vivienda`.
- En `Peso_talla_hemo`, verificar si existen varias mediciones o registros por persona antes de unir; no asumir que una fila por clave implica error.
- En historiales, conservar las filas repetidas y validar el numero de evento o nacimiento.

### Paso 4. Eliminar solo atributos que no sirven como caracteristicas

Eliminar de `X`, pero conservar en una tabla de auditoria:

- `folio`, `nro`, `upm`, identificadores de cuestionario y numeros de orden.
- Variables constantes o casi constantes sin significado analitico.
- Variables derivadas directamente del objetivo.
- Variables que solo se conocen despues de la medicion que el modelo pretende anticipar.

No eliminar un identificador antes de hacer las uniones.

### Paso 5. Normalizar nombres y etiquetas

- Mantener los nombres oficiales de columnas en una tabla de trazabilidad.
- Crear nombres internos simples solo para el modelo, por ejemplo `edad`, `area`, `region`, `educacion`.
- Corregir problemas de codificacion de caracteres en una copia normalizada.
- Separar codigo y etiqueta: `1. SI` debe convertirse en `1` y guardar la etiqueta `SI` en el diccionario.
- No convertir automaticamente todas las variables numericas a numeros: algunos numeros son codigos categoricos.

### Paso 6. Recodificar variables

Usar reglas diferentes según el tipo:

- Binarias: `1. SI` -> `1`, `2. NO` -> `0`.
- No sabe/no responde: conservar como categoria separada o convertir en faltante controlado, documentando la decision.
- Categorias sin orden, como departamento o tipo de vivienda: **One-Hot Encoding**.
- Categorias ordinales, como quintil de riqueza o nivel educativo: conservar orden numerico solo si el diccionario lo justifica.
- Respuestas multiples: una columna binaria por alternativa; no convertirlas en una sola etiqueta.
- Fechas: convertir a ano, mes, edad o tiempo transcurrido solo cuando tenga sentido para la pregunta.

### Paso 7. Tratar faltantes por variable y universo

No se debe imputar el resultado objetivo. Para los predictores:

- Numericas: mediana calculada solo en train, preferentemente por grupos justificados como sexo o area.
- Categoricas: categoria `DESCONOCIDO` o moda calculada solo en train.
- Variables con salto estructural: crear una categoria `NO APLICA` si el hecho de no aplicar contiene informacion; no confundirla con `NO SABE`.
- Variables con mas de 60% de faltantes: revisar primero el universo. Se eliminan solo si son irrelevantes, no aplicables al modelo o no tienen suficiente informacion util.
- Variables con menos de 5% de faltantes: pueden imputarse con una regla simple, siempre dentro del pipeline.
- Variables entre ambos umbrales: evaluar cobertura, relacion con el objetivo y riesgo de sesgo antes de decidir.

### Paso 8. Controlar valores extremos y rangos

No eliminar automaticamente outliers clinicos: pueden ser casos reales.

Validar rangos usando el diccionario y el contexto:

- Edad femenina: 12 a 49 anos.
- Edad infantil: usar edad en meses y verificar que corresponda al universo menor de seis anos.
- IMC: revisar valores imposibles, pero conservar valores clinicamente extremos validos.
- Hemoglobina, peso, talla y perimetros: validar unidades, ceros, negativos y limites fisicos antes de imputar.
- Costos, tiempos y conteos: revisar que no sean codigos especiales almacenados como numeros.

Los valores imposibles se convierten en faltantes documentados; los valores extremos validos no se borran sin justificacion.

### Paso 9. Integrar las tablas

Para el modelo de anemia femenina:

1. Filtrar `Peso_talla_hemo` a mujeres con `tip_anemia_m` valido.
2. Unir `Mujer` por `folio+nro`.
3. Unir `Hogar` por `folio+nro`.
4. Unir `Vivienda` por `folio`.
5. Conservar solo una fila por persona objetivo.
6. Verificar que el numero de filas antes y despues de cada union sea el esperado.

Para anemia infantil, reemplazar `Mujer` por `PrimeraInfancia` y usar variables del cuidador, alimentacion, vacunacion, desarrollo y hogar.

Para los demas modelos:

- M3 y M4: integrar `Peso_talla_hemo` con `Mujer` o `Hombre`, respectivamente, usando `folio+nro`.
- M5: usar `Hogar` como tabla principal y agregar `Vivienda` por `folio`; no repetir la vivienda como si fueran personas distintas.
- M6 y M7: usar `PrimeraInfancia` como tabla principal y agregar `Hogar` por `folio+nro` cuando el orden corresponda al nino; validar manualmente una muestra de uniones.
- M8: usar `Mujer` como tabla principal y agregar `Hogar` por `folio+nro` y `Vivienda` por `folio`.
- M9: usar `Hombre` como tabla principal y agregar `Hogar` y `Vivienda` con las mismas claves.
- M10: mantener `HistorialParidad` a nivel de nacimiento o agregarlo a nivel de mujer antes de unirlo a `Mujer`.

Cada integracion debe producir un reporte con filas antes, filas despues, claves no encontradas, claves duplicadas y porcentaje de perdida.

### Paso 10. Seleccionar caracteristicas

Aplicar seleccion despues de separar train/test y dentro de la validacion:

- Eliminar identificadores y fuga de informacion por regla de negocio.
- Quitar variables constantes o duplicadas.
- Revisar correlacion alta entre variables numericas.
- Usar regularizacion L1, importancia por permutation o seleccion univariada dentro del train.
- No seleccionar variables solo porque tienen correlacion con el objetivo si fueron medidas despues del resultado.

PCA puede reservarse para una etapa posterior. No es la primera opcion si se necesita explicar por que una persona fue priorizada.

### Paso 11. Codificar y escalar dentro de un pipeline

- Imputacion, codificacion y escalado deben ajustarse solo con train.
- One-Hot Encoding para categorias nominales.
- StandardScaler para regresion logistica, SVM, KNN o redes neuronales.
- No es obligatorio escalar para arboles de decision, Random Forest o Gradient Boosting, aunque la codificacion y los faltantes siguen siendo necesarios.
- Usar `Pipeline` y `ColumnTransformer` para evitar transformaciones diferentes entre entrenamiento y prueba.

### Paso 12. Separar train, validation y test

Usar como punto de partida 70% train, 15% validation y 15% test, o validacion cruzada estratificada dentro del train.

- Separar primero y transformar despues.
- Mantener la proporcion de anemia en cada particion con `stratify`.
- Si se unen varios registros por persona, dividir por persona, no por fila de historial.
- Si se quiere evaluar generalizacion territorial, hacer una prueba adicional dejando departamentos fuera del entrenamiento.
- Reservar el test hasta el final.

## 6. Modelos recomendados

### Modelo base explicable

Regresion logistica para anemia femenina e infantil, riesgo metabolico, problemas recientes de salud, vacunacion, desarrollo y acceso. Ventajas: probabilidades, coeficientes interpretables y facilidad para explicar factores asociados.

### Modelos de comparacion

- Arbol de decision: facil de explicar y puede servir como referencia.
- Random Forest o Gradient Boosting: capturan relaciones no lineales.
- Multiclase: usarlo solo cuando el objetivo tenga categorias clinicamente o administrativamente definidas, por ejemplo anemia sin anemia/leve/moderada/severa.
- Regresion lineal o modelos de conteo: reservarlos para objetivos numericos como numero de controles, edad o cantidad de hijos; no convertir artificialmente esos objetivos en categorias.
- Clustering: usarlo como analisis exploratorio para perfiles de vulnerabilidad, nunca como sustituto de una etiqueta clinica validada.
- No usar aprendizaje por refuerzo: el dataset es observacional y no contiene estados, acciones, recompensas ni interacciones secuenciales para entrenar un agente.
- Aprendizaje no supervisado puede complementar el estudio para descubrir perfiles, pero no reemplaza la clasificacion supervisada cuando existe `tip_anemia_m` o `tip_anemia`.

## 7. Evaluacion

Para modelos clinicos o de priorizacion, priorizar:

- Sensibilidad: detectar la mayor cantidad posible de personas con anemia.
- Especificidad: evitar demasiadas derivaciones innecesarias.
- Precision, recall y F1.
- AUC-ROC y AUC-PR, especialmente si las clases son desbalanceadas.
- Matriz de confusion.
- Calibracion de probabilidades.
- Sensibilidad por area, region, departamento, edad y quintil de riqueza.

Para vacunacion, desarrollo, acceso y salud sexual agregar cobertura, recall de la clase prioritaria y matrices de confusion por edad y area. Para objetivos multicategoria reportar macro-F1, balanced accuracy y matriz de confusion por clase. Para objetivos numericos reportar MAE, RMSE y R2, sin interpretar R2 como causalidad.

El umbral debe elegirse según la capacidad real del sistema de salud y el costo relativo de un falso negativo. No se debe usar exactitud como unica metrica.

## 8. Productos que deben quedar al finalizar

1. `datos_procesados/` con tablas analiticas separadas por objetivo y poblacion.
2. `diccionario_tecnico.csv` con tipo, universo, transformacion y motivo de exclusion.
3. `reporte_calidad.csv` con faltantes, rangos, duplicados y valores especiales.
4. Notebook o script reproducible de integracion y preprocesamiento.
5. Dataset de train, validation y test sin identificadores directos para cada modelo.
6. Pipeline serializado de transformacion y modelo para M1-M10, o justificacion documentada si algun modelo se descarta.
7. Informe de metricas, calibracion y equidad por subgrupos para cada modelo.
8. Registro de decisiones para que cada eliminacion o imputacion sea auditable.
9. Catalogo de modelos con poblacion, objetivo, version de datos, ponderador, fecha y responsable.
10. Tabla final de prioridades con `folio`, `nro`, modelo, probabilidad y recomendacion de seguimiento, protegida de exposicion innecesaria de datos sensibles.

## 9. Criterio de finalizacion

El preprocesamiento se considera terminado cuando:

- Cada fila del dataset modelado representa una unidad clara.
- La variable objetivo tiene definicion y universo documentados.
- No hay identificadores directos ni fuga de informacion en `X`.
- Todas las uniones pasan validaciones de cardinalidad.
- Los faltantes tienen una regla justificada por variable.
- Las categorias estan codificadas sin imponer orden falso.
- Las transformaciones numericas estan dentro del pipeline.
- Train, validation y test no comparten personas de forma indebida.
- El resultado se puede reproducir desde los CSV originales.
- Las metricas se reportan junto con limitaciones y subgrupos afectados.
