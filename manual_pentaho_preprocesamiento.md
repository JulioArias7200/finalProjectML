# Manual de preprocesamiento en Pentaho Data Integration

## 1. Proposito

Este documento describe el trabajo de preprocesamiento que se realizara en Pentaho Data Integration para preparar los datasets de la EDSA 2023 para Machine Learning.

Pentaho se utilizara para:

- Leer y validar los CSV.
- Limpiar etiquetas y codigos.
- Separar poblaciones y universos.
- Integrar tablas mediante `folio` y `folio+nro`.
- Crear variables derivadas.
- Agregar tablas de eventos.
- Controlar faltantes, rangos y duplicados.
- Exportar datasets listos para la etapa posterior de modelado.

No se modificaran los CSV originales. Cada transformacion debe guardar su resultado en la carpeta `salida/` y generar un registro de control.

## 2. Orden general de trabajo

Se aplicaran los modelos desde el mas complejo al mas sencillo, considerando dificultad de integracion, cantidad de variables, necesidad de agregacion y riesgo de errores de unidad de observacion.

| Orden | Modelo | Poblacion | Dataset principal | Dificultad |
|---:|---|---|---|---|
| 1 | M10 | Mujeres con nacimientos desde 2018 | `EDSA2023_HistorialParidad.csv` | Muy alta |
| 2 | M1 | Mujeres de 12 a 49 anos | `EDSA2023_Peso_talla_hemo.csv` + `EDSA2023_Mujer.csv` | Alta |
| 3 | M2 | Ninas/os de 6 meses a menores de 6 anos | `EDSA2023_Peso_talla_hemo.csv` + `EDSA2023_PrimeraInfancia.csv` | Alta |
| 4 | M3 | Mujeres con medicion antropometrica valida | `EDSA2023_Peso_talla_hemo.csv` + `EDSA2023_Mujer.csv` | Media-alta |
| 5 | M4 | Hombres con medicion antropometrica valida | `EDSA2023_Peso_talla_hemo.csv` + `EDSA2023_Hombre.csv` | Media-alta |
| 6 | M7 | Ninas/os de primera infancia | `EDSA2023_PrimeraInfancia.csv` | Media |
| 7 | M6 | Ninas/os de primera infancia | `EDSA2023_PrimeraInfancia.csv` | Media |
| 8 | M5 | Personas del hogar | `EDSA2023_Hogar.csv` + `EDSA2023_Vivienda.csv` | Media-baja |
| 9 | M8 | Mujeres entrevistadas | `EDSA2023_Mujer.csv` + `EDSA2023_Hogar.csv` + `EDSA2023_Vivienda.csv` | Baja |
| 10 | M9 | Hombres entrevistados | `EDSA2023_Hombre.csv` + `EDSA2023_Hogar.csv` + `EDSA2023_Vivienda.csv` | Baja |

La dificultad no significa importancia. Todos los modelos deben documentarse y validarse por separado.

## 3. Nombres de datasets de salida

Estos son los nombres que se deben utilizar en `salida/`.

### Salidas de control y catalogos

- `00_catalogo_modelos.csv`
- `00_diccionario_tecnico.csv`
- `00_reporte_calidad_archivos.csv`
- `00_reporte_uniones.csv`
- `00_reporte_faltantes.csv`

### Salidas del modelo M10

- `M10_historial_paridad_largo_limpio.csv`
- `M10_historial_paridad_agregado_mujer.csv`
- `M10_atencion_prenatal_modelo.csv`

### Salidas del modelo M1

- `M1_anemia_mujer_objetivo.csv`
- `M1_anemia_mujer_modelo.csv`

### Salidas del modelo M2

- `M2_anemia_infantil_objetivo.csv`
- `M2_anemia_infantil_modelo.csv`

### Salidas de los modelos M3 y M4

- `M3_riesgo_metabolico_mujer_objetivo.csv`
- `M3_riesgo_metabolico_mujer_modelo.csv`
- `M4_riesgo_metabolico_hombre_objetivo.csv`
- `M4_riesgo_metabolico_hombre_modelo.csv`

### Salidas de los modelos M6 y M7

- `M6_vacunacion_infantil_modelo.csv`
- `M7_desarrollo_infantil_modelo.csv`

### Salidas de los modelos M5, M8 y M9

- `M5_salud_personas_hogar_modelo.csv`
- `M5_salud_hogares_agregado.csv`
- `M8_acceso_sus_mujer_modelo.csv`
- `M9_salud_sexual_hombre_modelo.csv`

### Salidas auxiliares

- `aux_vivienda_features.csv`
- `aux_hogar_persona_limpio.csv`
- `aux_hogar_resumen.csv`
- `aux_mujer_base_limpia.csv`
- `aux_hombre_base_limpia.csv`
- `aux_primera_infancia_base_limpia.csv`

## 4. Preparacion del proyecto en Pentaho

### 4.1 Crear la estructura de carpetas

Crear estas carpetas antes de ejecutar transformaciones:

- `entrada/`: copias de trabajo de los CSV originales.
- `salida/`: datasets preprocesados.
- `control/`: reportes de conteos, faltantes y uniones.
- `pentaho/`: transformaciones `.ktr` y trabajos `.kjb`.
- `documentacion/`: diccionario tecnico y decisiones.

Los archivos originales deben conservarse fuera del flujo de escritura.

### 4.2 Crear parametros de ruta

En el trabajo principal de Pentaho definir parametros para:

- Carpeta de entrada.
- Carpeta de salida.
- Carpeta de control.
- Fecha de ejecucion.
- Version del proceso.

Todas las transformaciones deben utilizar estos parametros. No escribir rutas absolutas diferentes en cada paso.

### 4.3 Transformacion de lectura comun

Para cada CSV utilizar el paso **Text file input**:

1. Seleccionar el archivo CSV.
2. Usar la primera fila como encabezado.
3. Configurar separador coma.
4. Revisar codificacion UTF-8.
5. Definir `folio` y `nro` como texto durante la lectura si aparecen inconsistencias decimales.
6. Definir variables de medicion como numericas.
7. Revisar una muestra de 100 filas.
8. Activar la captura de errores de lectura.
9. Enviar errores a un flujo de rechazo.

No confiar unicamente en la deteccion automatica de tipos. En estas bases algunos numeros son codigos categoricos.

## 5. Reglas comunes de limpieza

### 5.1 Identificadores

Conservar durante todo el ETL:

- `folio`.
- `nro`.
- `upm`.
- `estrato`.

Eliminar estos campos unicamente en la salida final que sera usada como matriz `X` del modelo. Mantenerlos en la tabla de auditoria y en el archivo de prioridades.

### 5.2 Etiquetas y codigos

Usar los pasos **String operations**, **Replace in string** y **Value mapper** para:

- Quitar espacios al inicio y al final.
- Homogeneizar mayusculas y minusculas.
- Separar el codigo antes del punto de la etiqueta.
- Convertir `1. SI` a codigo `1` y etiqueta `SI`.
- Convertir `2. NO` a codigo `2` y etiqueta `NO`.
- Conservar `8. NO SABE` como categoria diferente.
- Conservar `999. SIN ESPECIFICAR` como categoria de no especificacion.

No convertir `8` o `999` en cero. Cero significa ausencia o respuesta negativa solo cuando el diccionario lo indique.

### 5.3 Variables binarias

Usar **Value mapper** para producir variables binarias:

- `SI` -> `1`.
- `NO` -> `0`.
- `NO SABE` -> nulo controlado o categoria separada.
- `NO APLICA` -> categoria separada cuando represente un salto valido.

Registrar la regla en `00_diccionario_tecnico.csv`.

### 5.4 Variables de respuesta multiple

No combinar las respuestas multiples en una sola columna. Cada alternativa debe quedar como indicador independiente.

Ejemplo:

- `ms03_0313_A` -> `usa_esterilizacion_femenina`.
- `ms03_0313_C` -> `usa_pildora`.
- `ms03_0313_D` -> `usa_diu`.
- `ms03_0313_E` -> `usa_inyeccion`.
- `ms03_0313_F` -> `usa_implante`.
- `ms03_0313_H` -> `usa_condon_masculino`.

### 5.5 Faltantes

En Pentaho no se debe aplicar una unica regla global de eliminacion.

Clasificar cada faltante como:

- Faltante estructural por salto.
- No sabe.
- No responde.
- No medido.
- Error de captura.

Usar **Filter rows** para separar cada tipo y crear un reporte de conteo. No imputar objetivos. La imputacion para Machine Learning se realizara despues, dentro del pipeline de entrenamiento, usando estadisticas del conjunto train.

### 5.6 Valores imposibles

Usar **Filter rows** para enviar a rechazo valores como:

- Edad negativa.
- Edad femenina fuera de 12-49 cuando se trate del cuestionario mujer.
- Edad infantil incompatible con el universo de primera infancia.
- Peso, talla, IMC o hemoglobina negativos.
- Meses fuera del rango esperado.
- Categorias que no aparecen en el diccionario.

Los valores clinicamente extremos pero posibles no deben eliminarse automaticamente.

### 5.7 Reporte de calidad

Cada transformacion debe producir:

- Filas leidas.
- Filas validas.
- Filas rechazadas.
- Duplicados detectados.
- Faltantes por campo.
- Categorias desconocidas.
- Fecha y version del proceso.

Usar **Group by**, **Count rows** y **Write to file** para guardar estos reportes.

# 6. Procedimiento modelo por modelo

## M10. Historial reproductivo y atencion prenatal

### Datasets de entrada

- `EDSA2023_HistorialParidad.csv`.
- `EDSA2023_HistorialHijos.csv`.
- `EDSA2023_Mujer.csv`.
- `EDSA2023_PrimeraInfancia.csv`, solo si se relaciona el nacimiento con informacion del nino.

### Unidad de analisis

Primero sera nacimiento/evento. Para un modelo por mujer se generara una segunda salida agregada.

### Flujo Pentaho

1. Leer `EDSA2023_HistorialParidad.csv` con **Text file input**.
2. Validar que `folio` y `nro` no sean nulos.
3. Crear una clave tecnica `clave_mujer = folio + nro` con **Concat fields**.
4. Crear una clave de evento usando `clave_mujer` y `ms04_0403` o el numero de nacimiento.
5. No usar **Unique rows** para eliminar repetidos.
6. Limpiar respuestas de controles prenatales con **Value mapper**.
7. Convertir `ms04_0411` a numerica.
8. Validar que el numero de controles no sea negativo.
9. Recodificar atencion profesional y lugar del parto.
10. Ordenar por `clave_mujer` y fecha/nacimiento con **Sort rows**.
11. Crear indicadores de atencion:
    - `tuvo_control_prenatal`.
    - `controles_prenatales`.
    - `parto_atencion_profesional`.
    - `parto_establecimiento_salud`.
    - `parto_cesarea`.
12. Generar la salida larga con **Text file output**.
13. Para la salida por mujer, usar **Group by** agrupando por `clave_mujer`.
14. Calcular ultimo nacimiento, maximo numero de controles y proporciones de atencion.
15. Unir la salida agregada con `Mujer` mediante **Merge join** o **Stream lookup**.
16. Verificar cardinalidad uno-a-uno despues de la agregacion.
17. Escribir reportes de filas antes y despues.

### Salidas

- `M10_historial_paridad_largo_limpio.csv`.
- `M10_historial_paridad_agregado_mujer.csv`.
- `M10_atencion_prenatal_modelo.csv`.

### Control obligatorio

La salida agregada debe tener como maximo una fila por `folio+nro`. La salida larga puede tener varias filas por mujer.

## M1. Anemia en mujeres

### Datasets de entrada

- `EDSA2023_Peso_talla_hemo.csv`.
- `EDSA2023_Mujer.csv`.
- `EDSA2023_Hogar.csv`.
- `EDSA2023_Vivienda.csv`.

### Objetivo

Crear `anemia_mujer`:

- `0` para `1. SIN ANEMIA`.
- `1` para anemia leve, moderada o severa.

Conservar tambien `tip_anemia_m` como variable descriptiva, no como predictor.

### Flujo Pentaho

1. Leer `Peso_talla_hemo`.
2. Filtrar con **Filter rows** las filas donde `tip_anemia_m` sea valido.
3. Con **Value mapper**, crear `anemia_mujer`.
4. Excluir de las caracteristicas `hs06_0120`, `tip_anemia_m` y cualquier calculo derivado de hemoglobina.
5. Leer `Mujer` y seleccionar solo variables anteriores o disponibles al momento de la priorizacion:
    - Edad.
    - Educacion.
    - Embarazo.
    - Area.
    - Region.
    - Departamento.
    - SUS.
    - Estado conyugal.
    - Actividad y acceso a salud.
6. Leer `Hogar` y conservar seguro, educacion, discapacidad y contexto individual.
7. Leer `Vivienda` y conservar agua, saneamiento, combustible, calidad y riqueza.
8. Antes de unir, usar **Sort rows** por `folio` y `nro` en ambas tablas.
9. Usar **Merge join** por `folio+nro` para personas.
10. Unir `Vivienda` por `folio` despues de comprobar que `folio` es unico.
11. Usar **Select values** para quitar identificadores de la matriz de caracteristicas final, conservandolos en una salida de auditoria.
12. Generar reporte de coincidencias y no coincidencias.
13. Escribir las salidas.

### Salidas

- `M1_anemia_mujer_objetivo.csv`.
- `M1_anemia_mujer_modelo.csv`.

### Control obligatorio

No imputar `anemia_mujer`. La cantidad de filas validas debe coincidir con las mujeres con resultado de hemoglobina valido antes de las uniones.

## M2. Anemia infantil

### Datasets de entrada

- `EDSA2023_Peso_talla_hemo.csv`.
- `EDSA2023_PrimeraInfancia.csv`.
- `EDSA2023_Hogar.csv`.
- `EDSA2023_Vivienda.csv`.

### Objetivo

Crear `anemia_nino` a partir de `tip_anemia`:

- `0` para `1. SIN ANEMIA`.
- `1` para leve, moderada o severa.

### Flujo Pentaho

1. Filtrar el resultado infantil valido en `Peso_talla_hemo`.
2. Crear `anemia_nino` con **Value mapper**.
3. Leer `PrimeraInfancia`.
4. Revisar edad en meses y excluir edades incompatibles con el universo del modelo.
5. Recodificar lactancia, alimentacion, enfermedades, vacunacion y cuidador.
6. No usar `hs06_0127`, `tip_anemia` ni indicadores derivados de hemoglobina.
7. Unir por `folio+nro`.
8. Agregar `Hogar` y `Vivienda` con las claves verificadas.
9. Separar ninos sin resultado de hemoglobina de ninos con resultado valido.
10. Crear reporte de cobertura por area y grupo de edad.
11. Escribir las salidas.

### Salidas

- `M2_anemia_infantil_objetivo.csv`.
- `M2_anemia_infantil_modelo.csv`.

### Control obligatorio

No mezclar ninos de primera infancia con personas adultas. La edad en meses debe quedar en la salida.

## M3. Riesgo metabolico en mujeres

### Datasets de entrada

- `EDSA2023_Peso_talla_hemo.csv`.
- `EDSA2023_Mujer.csv`.
- `EDSA2023_Hogar.csv`.
- `EDSA2023_Vivienda.csv`.

### Objetivo

Crear `sobrepeso_obesidad_mujer` a partir de `categaimc_m`:

- `1` para `2. TOTAL SOBREPESO OBESA`.
- `0` para `3. NORMAL` o `1. TOTAL DELGADA`, si el objetivo es binario.

### Flujo Pentaho

1. Filtrar categorias IMC validas.
2. Crear el objetivo binario.
3. No usar `imc_m`, `categimc_m`, peso ni talla si el objetivo es anticipar el riesgo antes de medir.
4. Unir antecedentes de mujer, hogar y vivienda.
5. Crear grupos de edad, educacion, area, region, actividad y acceso.
6. Validar distribucion del objetivo por area y region.
7. Escribir las salidas.

### Salidas

- `M3_riesgo_metabolico_mujer_objetivo.csv`.
- `M3_riesgo_metabolico_mujer_modelo.csv`.

## M4. Riesgo metabolico en hombres

### Datasets de entrada

- `EDSA2023_Peso_talla_hemo.csv`.
- `EDSA2023_Hombre.csv`.
- `EDSA2023_Hogar.csv`.
- `EDSA2023_Vivienda.csv`.

### Objetivo

Crear `sobrepeso_obesidad_hombre` a partir de `categaimc_h`:

- `1` para `2. TOTAL SOBREPESO OBESO`.
- `0` para normal o delgadez.

### Flujo Pentaho

1. Filtrar categorias IMC validas de hombres.
2. Crear el objetivo binario.
3. Excluir IMC, peso y talla de los predictores si se quiere priorizar antes de la medicion.
4. Unir `Hombre`, `Hogar` y `Vivienda`.
5. Recodificar educacion, actividad laboral, estado conyugal, area y region.
6. Revisar cobertura de la muestra masculina.
7. Escribir las salidas.

### Salidas

- `M4_riesgo_metabolico_hombre_objetivo.csv`.
- `M4_riesgo_metabolico_hombre_modelo.csv`.

## M7. Desarrollo infantil

### Dataset de entrada

- `EDSA2023_PrimeraInfancia.csv`.
- `EDSA2023_Hogar.csv`.
- `EDSA2023_Vivienda.csv`.

### Objetivo

Usar `idit`:

- `0` para hitos alcanzados.
- `1` para hitos no alcanzados.

### Flujo Pentaho

1. Filtrar `idit` valido.
2. Conservar edad en meses.
3. Separar por grupos de edad.
4. Excluir del modelo los mismos hitos que construyen el indice si se desea predecir el indice completo.
5. Crear indicadores de estimulacion, libros, actividades y relacion con el cuidador.
6. Recodificar lactancia y alimentacion.
7. Unir hogar y vivienda.
8. Generar reporte por area, edad y sexo.
9. Escribir la salida.

### Salida

- `M7_desarrollo_infantil_modelo.csv`.

## M6. Vacunacion infantil

### Dataset de entrada

- `EDSA2023_PrimeraInfancia.csv`.
- `EDSA2023_Hogar.csv`.
- `EDSA2023_Vivienda.csv`.

### Objetivo

Crear `vacunacion_incompleta` usando el registro de vacunas, la fuente de informacion y las variables `ps05_0502_*`.

### Flujo Pentaho

1. Separar ninos con tarjeta, con informacion del cuidador y sin registro.
2. No tratar “sin tarjeta” como “no vacunado”.
3. Verificar cada vacuna segun la edad en meses.
4. Crear indicadores por vacuna.
5. Crear `vacunacion_completa` y `vacunacion_incompleta` segun el esquema definido.
6. Unir hogar y vivienda.
7. Crear reporte de cobertura por edad y area.
8. Escribir la salida.

### Salida

- `M6_vacunacion_infantil_modelo.csv`.

## M5. Problema de salud reciente en personas del hogar

### Datasets de entrada

- `EDSA2023_Hogar.csv`.
- `EDSA2023_Vivienda.csv`.

### Objetivo

Crear `problema_salud_reciente` a partir de `hs03_0033`:

- `1` para SI.
- `0` para NO.

### Flujo Pentaho

1. Leer `Hogar` a nivel persona.
2. Recodificar `hs03_0033`.
3. No usar `hs03_0034_*` para anticipar la existencia del problema.
4. Recodificar edad, sexo, educacion, seguro, discapacidad y atencion.
5. Unir `Vivienda` por `folio`.
6. Crear una tabla individual.
7. Crear una tabla agregada por hogar con **Group by**:
    - Numero de residentes.
    - Numero de personas con problema reciente.
    - Numero de personas con seguro.
    - Numero de menores.
8. Escribir ambas salidas.

### Salidas

- `M5_salud_personas_hogar_modelo.csv`.
- `M5_salud_hogares_agregado.csv`.

## M8. Acceso y uso del SUS en mujeres

### Datasets de entrada

- `EDSA2023_Mujer.csv`.
- `EDSA2023_Hogar.csv`.
- `EDSA2023_Vivienda.csv`.

### Objetivos

Crear dos salidas analiticas diferentes:

- Registro en SUS: `ms05_0506`.
- Atencion por SUS desde 2018: `ms05_0507`.

No convertir ambos objetivos en una sola columna.

### Flujo Pentaho

1. Leer `Mujer`.
2. Recodificar SI y NO.
3. Separar no sabe y no especificado.
4. Crear grupos de edad, educacion, embarazo, area, region y seguro.
5. Unir hogar y vivienda.
6. Generar reporte de faltantes y cobertura.
7. Escribir la salida.

### Salida

- `M8_acceso_sus_mujer_modelo.csv`.

## M9. Salud sexual masculina

### Dataset de entrada

- `EDSA2023_Hombre.csv`.
- `EDSA2023_Hogar.csv`.
- `EDSA2023_Vivienda.csv`.

### Objetivo

Definir previamente una sola pregunta objetivo, por ejemplo:

- Uso de condon en la ultima relacion: `vs04_0417`.
- Acceso o conocimiento de un lugar para conseguir condones: `vs04_0432`.

No mezclar objetivos en la misma salida.

### Flujo Pentaho

1. Leer `Hombre`.
2. Seleccionar el bloque de salud sexual y VIH/ITS.
3. Recodificar respuestas binarias.
4. Crear conocimiento acumulado sobre VIH/ITS solo con variables anteriores al objetivo.
5. Unir hogar y vivienda.
6. Excluir identificadores y variables posteriores al evento.
7. Escribir la salida.

### Salida

- `M9_salud_sexual_hombre_modelo.csv`.

## 7. Procesos de Pentaho recomendados

### Transformaciones `.ktr`

Crear una transformacion por tarea:

- `T00_control_archivos.ktr`.
- `T01_limpiar_vivienda.ktr`.
- `T02_limpiar_hogar.ktr`.
- `T03_limpiar_mujer.ktr`.
- `T04_limpiar_hombre.ktr`.
- `T05_limpiar_primera_infancia.ktr`.
- `T06_limpiar_peso_talla_hemo.ktr`.
- `T07_agregar_historial_hijos.ktr`.
- `T08_agregar_historial_paridad.ktr`.
- `T09_transformar_calendario.ktr`.
- `T10_generar_M10.ktr`.
- `T11_generar_M1.ktr`.
- `T12_generar_M2.ktr`.
- `T13_generar_M3_M4.ktr`.
- `T14_generar_M5.ktr`.
- `T15_generar_M6_M7.ktr`.
- `T16_generar_M8_M9.ktr`.
- `T99_validar_salidas.ktr`.

### Trabajo `.kjb`

Crear un trabajo principal que ejecute las transformaciones en este orden:

1. Controlar existencia y lectura de archivos.
2. Limpiar tablas base.
3. Crear auxiliares de vivienda, hogar, mujer, hombre e infancia.
4. Agregar historiales.
5. Construir M10.
6. Construir M1 y M2.
7. Construir M3 y M4.
8. Construir M7 y M6.
9. Construir M5.
10. Construir M8 y M9.
11. Validar todos los archivos de salida.
12. Escribir el resumen de ejecucion.

Si una transformacion falla, el trabajo debe detenerse y conservar el archivo de error. No continuar silenciosamente con una tabla incompleta.

## 8. Pasos Pentaho y su funcion

| Paso Pentaho | Uso en este proyecto |
|---|---|
| **Text file input** | Leer cada CSV. |
| **Select values** | Seleccionar, renombrar y eliminar columnas. |
| **String operations** | Limpiar espacios y texto. |
| **Replace in string** | Corregir etiquetas y caracteres. |
| **Value mapper** | Recodificar SI/NO y categorias. |
| **Filter rows** | Filtrar universos, resultados validos y rechazos. |
| **Calculator** | Crear grupos de edad y variables binarias. |
| **Formula** | Crear indicadores derivados. |
| **Concat fields** | Crear claves tecnicas. |
| **Sort rows** | Preparar entradas para uniones y eventos. |
| **Merge join** | Unir tablas ordenadas por claves. |
| **Stream lookup** | Buscar datos auxiliares cuando la tabla de referencia sea unica y controlada. |
| **Group by** | Agregar historiales y resumir hogares. |
| **Unique rows** | Usar solo en tablas donde la clave deba ser unica; nunca en historiales sin revisar. |
| **Value validator** | Validar rangos, categorias y valores permitidos. |
| **Write to file** | Exportar CSV de salida. |
| **Dummy** | Dividir o conectar flujos sin modificar datos. |
| **Abort** | Detener el trabajo cuando una validacion critica falle. |

## 9. Validacion antes de entregar cada salida

Cada CSV debe revisarse con la siguiente lista:

1. El archivo existe.
2. Tiene encabezado.
3. Tiene filas.
4. La unidad de observacion esta documentada.
5. Las claves no tienen nulos inesperados.
6. Las uniones no multiplicaron filas.
7. Los objetivos tienen solo categorias permitidas.
8. Los predictores no contienen el objetivo ni variables con fuga.
9. Los identificadores fueron excluidos de la matriz de caracteristicas final.
10. Los faltantes tienen una categoria o regla documentada.
11. Las variables binarias contienen solo `0`, `1` o el codigo de faltante documentado.
12. Los valores numericos respetan rangos razonables.
13. El reporte de calidad fue generado.
14. El nombre del archivo coincide con este manual.
15. El proceso puede repetirse desde los CSV originales.

## 10. Resumen final de salidas preprocesadas

- `M10_atencion_prenatal_modelo.csv`
- `M1_anemia_mujer_modelo.csv`
- `M2_anemia_infantil_modelo.csv`
- `M3_riesgo_metabolico_mujer_modelo.csv`
- `M4_riesgo_metabolico_hombre_modelo.csv`
- `M7_desarrollo_infantil_modelo.csv`
- `M6_vacunacion_infantil_modelo.csv`
- `M5_salud_personas_hogar_modelo.csv`
- `M5_salud_hogares_agregado.csv`
- `M8_acceso_sus_mujer_modelo.csv`
- `M9_salud_sexual_hombre_modelo.csv`

La etapa de Pentaho termina cuando estas salidas y los reportes de control existen, tienen unidad de analisis conocida y pasan las validaciones. La imputacion estadistica, el escalado final y la division train/validation/test deben realizarse despues, dentro del pipeline de Machine Learning.
