# Analisis de los datasets EDSA 2023

## Alcance

El analisis se basa en los diccionarios del proyecto y en los archivos CSV derivados de los SAV. Las bases corresponden a distintos niveles del cuestionario de la EDSA 2023: vivienda, hogar, personas, mujeres, eventos reproductivos y mediciones antropometricas.

## Inventario y unidad de observacion

| Base | Filas | Variables | Unidad principal |
|---|---:|---:|---|
| `EDSA2023_Vivienda.csv` | 19,059 | 73 | Vivienda, identificada por `folio` |
| `EDSA2023_Hogar.csv` | 54,008 | 235 | Persona dentro del hogar, identificada por `folio+nro` |
| `EDSA2023_Mujer.csv` | 14,545 | 1,341 | Mujer entrevistada, `folio+nro` |
| `EDSA2023_Hombre.csv` | 5,878 | 997 | Hombre entrevistado, `folio+nro` |
| `EDSA2023_PrimeraInfancia.csv` | 5,529 | 490 | Nino/a de primera infancia, `folio+nro` |
| `EDSA2023_Peso_talla_hemo.csv` | 46,581 | 44 | Persona elegible para antropometria/hemoglobina |
| `EDSA2023_MujerCalendario.csv` | 14,545 | 77 | Mujer y calendario mensual de anticoncepcion |
| `EDSA2023_HistorialParidad.csv` | 5,273 | 154 | Embarazo/nacimiento reportado desde enero de 2018 |
| `EDSA2023_HistorialHijos.csv` | 22,360 | 26 | Hijo/a registrado en el historial reproductivo |

Los identificadores comunes son `folio`, `nro`, `upm` y `estrato`. `Vivienda` no contiene `nro`, por lo que se relaciona con las demas tablas mediante `folio`. Las tablas de historial son tablas uno-a-muchos: presentan claves `folio+nro` repetidas porque una mujer puede tener varios hijos o eventos. No deben deduplicarse sin una regla basada en las variables del evento.

## Calidad y estructura

- Las tablas de encuesta individual tienen claves `folio+nro` unicas en los CSV revisados.
- `HistorialHijos` tiene 8,528 claves `folio+nro` distintas para 22,360 filas; `HistorialParidad` tiene 4,140 claves para 5,273 filas. Esto es consistente con registros repetidos por persona, no evidencia suficiente de duplicacion accidental.
- `Vivienda` tiene una fila por cada uno de sus 19,059 `folios`.
- El porcentaje promedio de celdas faltantes es alto en varios modulos: mujer 72.49%, hombre 67.05%, hogar 69.29%, primera infancia 58.45%, antropometria 55.64% e historial de paridad 58.31%.
- Los faltantes son en buena parte estructurales por saltos del cuestionario. Por ejemplo, en antropometria solo corresponde calcular IMC o anemia para subpoblaciones medidas; no se debe interpretar el faltante como ausencia de enfermedad.
- En `Hogar`, las variables de elegibilidad (`valid_muj`, `valid_hom`, `valid_nin`) confirman que muchos registros no pertenecen a la subpoblacion de mujeres, hombres o ninos elegibles.

## Resultados descriptivos

Los porcentajes siguientes usan el ponderador del modulo cuando existe y se calculan sobre respuestas validas para la variable indicada.

### Hogares

- Area: 71.00% urbana y 29.00% rural.
- Region: 37.44% Altiplano, 28.15% Valles y 34.41% Llanos.
- Tipo de hogar: 50.00% nuclear completo, 16.12% monoparental, 11.41% extendido, 10.22% unipersonal y 8.78% pareja nuclear.
- Afiliacion a salud: 66.53% SUS, 16.54% cajas de salud, 2.07% seguros privados y 14.69% sin afiliacion.

### Mujeres entrevistadas

- La base contiene 14,545 mujeres de 12 a 49 anos; edad media 28.84 y mediana 28.
- La distribucion ponderada por grupos es: 12-14 anos 9.41%, 15-19 15.10%, 20-24 14.51%, 25-29 14.58%, 30-34 13.40%, 35-39 11.79%, 40-44 11.66% y 45-49 9.55%.
- El embarazo actual (`ms02_0234`) registra 391 casos afirmativos, 14,123 negativos y 31 respuestas de duda/no sabe.
- En anticoncepcion actual, las variables `ms03_0313_*` son de respuesta multiple y solo se llenan para los metodos seleccionados. Por eso el porcentaje correcto para cada metodo se calcula sobre todas las mujeres, no sobre las filas no faltantes. Con `ponderadorm`: implante 6.79%, esterilizacion femenina 7.22%, DIU 3.42%, inyeccion 5.83%, condon masculino 6.80% y pildora 2.73%.

### Antropometria y hemoglobina

Entre las observaciones con categoria valida, no sobre toda la tabla:

| Indicador | Categoria | Porcentaje |
|---|---|---:|
| IMC mujeres | Sobrepeso/obesidad | 50.02% |
| IMC mujeres | Normal | 36.28% |
| IMC mujeres | Delgadez | 13.70% |
| IMC hombres | Sobrepeso/obesidad | 42.85% |
| IMC hombres | Normal | 40.89% |
| IMC hombres | Delgadez | 16.26% |
| Hemoglobina mujeres | Alguna anemia | 54.85% |
| Hemoglobina ninas/os | Alguna anemia | 63.24% |

La anemia se obtuvo agrupando las categorias leve, moderada y severa. En la distribucion observada, la anemia moderada y severa representan 27.64% de las mujeres con resultado y 38.88% de los ninos/as con resultado. Estos resultados requieren revisar el universo exacto de elegibilidad y los ponderadores especificos (`ponderador_mhm`, `ponderador_nhm`) antes de producir estimaciones oficiales.

## Recomendaciones para el modelado

1. Definir primero la unidad de analisis: hogar, mujer, persona medida o evento reproductivo.
2. Unir `Vivienda` con `Hogar` por `folio`; unir modulos individuales por `folio+nro`.
3. Mantener `HistorialHijos` y `HistorialParidad` en formato largo y conservar todas sus filas.
4. Convertir respuestas etiquetadas como `1. SI`, `2. NO`, etc. a codigos numericos separados de sus etiquetas.
5. Tratar los faltantes por salto como `NA estructural`, diferenciandolos de `no sabe`, `no responde` y resultados de medicion no realizados.
6. Aplicar el ponderador correspondiente al modulo y declarar el denominador en cada indicador. Para inferencia formal tambien deben incorporarse estrato y UPM.
7. Antes de entrenar un modelo, excluir identificadores directos (`folio`, `nro`, `upm`) y revisar fuga de informacion entre variables derivadas y sus componentes.

## Preguntas analiticas sugeridas

- Asociacion entre area, region, educacion y uso actual de anticonceptivos.
- Diferencias de anemia por area, region, edad y embarazo, usando el ponderador de hemoglobina.
- Relacion entre tipo de hogar, afiliacion a salud y acceso a controles prenatales.
- Evolucion del uso de metodos anticonceptivos en `MujerCalendario`, agregando los meses por ano y metodo.
- Comparacion entre mujeres y hombres en IMC, estratificada por area y edad.

## Analisis orientado al arbol de problemas

### Problema central

El dataset permite estudiar la **identificacion tardia de perfiles con anemia y riesgo metabolico**, pero no permite medir directamente el tiempo de espera ni probar causalidad. La EDSA 2023 es una encuesta transversal: sirve para estimar prevalencias, localizar grupos prioritarios y construir un prototipo de clasificacion, no para afirmar que una variable causa una enfermedad.

### Evidencia encontrada

Los resultados siguientes se calcularon sobre observaciones con resultado valido:

| Resultado | Universo | Resultado observado |
|---|---:|---:|
| Anemia en mujeres | 5,375 mujeres con `tip_anemia_m` | 54.87% |
| Anemia en mujeres urbanas | 3,856 | 53.29% |
| Anemia en mujeres rurales | 1,519 | 58.85% |
| Anemia en mujeres del Altiplano | 2,058 | 53.06% |
| Anemia en mujeres de Valles | 1,606 | 59.34% |
| Anemia en mujeres de Llanos | 1,711 | 52.83% |
| Anemia en ninas/os | 1,461 con `tip_anemia` | 63.24% |
| Anemia en ninas/os rurales | 585 | 66.15% |
| Sobrepeso/obesidad en mujeres | 20,270 con categoria IMC | 50.02% |
| Sobrepeso/obesidad en hombres | 19,936 con categoria IMC | 42.85% |

Tambien existen variables para estudiar enfermedades cronicas y acceso. En mujeres, la prevalencia ponderada declarada de hipertension fue 9.37% y la de diabetes 3.07%. El 70.35% declaro estar registrada en el SUS y 45.73% declaro haber recibido atencion por SUS desde 2018. Estos porcentajes describen declaracion y acceso reportado; no sustituyen un diagnostico clinico.

### Relacion con las causas

| Causa del arbol | Variables disponibles | Lectura analitica |
|---|---|---|
| Atencion y registro manual | `folio`, `nro`, resultados de medicion, variables de elegibilidad | La informacion esta distribuida entre modulos; se requiere una tabla analitica integrada y reglas de calidad. |
| Mezcla de variables y codificaciones | Variables etiquetadas como `1. SI`, `2. NO`, `8. NO SABE`, categorias de IMC y anemia | Se deben separar codigo y etiqueta antes de modelar. |
| Datos faltantes por saltos | `ponderador_mhm`, `ponderador_nhm`, resultados de medicion | El faltante puede significar persona no elegible, rechazo o medicion no realizada; no debe recodificarse automaticamente como cero. |
| Diferencias sociales y territoriales | `area`, `region`, `departamento`, `qriqueza`, `cviv`, educacion, seguro | Permiten estratificar riesgo y detectar brechas rurales, regionales y socioeconomicas. |
| Falta de modelo predictivo | `tip_anemia_m`, `tip_anemia`, categorias de IMC y predictores de mujer/hogar | Permiten desarrollar una prueba retrospectiva de priorizacion, con validacion y calibracion. |

### Prueba de modelo inicial

Se unieron mujeres, hogar y antropometria por `folio+nro`. Se excluyeron identificadores directos, el resultado objetivo y el ponderador como predictores. Con 17 predictores sociodemograficos, territoriales, de acceso y salud, una regresion logistica balanceada obtuvo:

- 5,375 observaciones con hemoglobina valida.
- 54.87% de casos positivos, definidos como anemia leve, moderada o severa.
- AUC media de validacion cruzada de **0.57** con desviacion estandar **0.018**.

Este resultado es una linea base, no un modelo listo para uso clinico. Su capacidad discriminativa es modesta. Antes de usarlo para alertas se necesitan mejores variables, tratamiento formal del diseno muestral, validacion externa, calibracion por area y region, analisis de equidad y revision de personal sanitario.

## Soluciones propuestas y como comprobarlas

1. **Diccionario y datos integrados:** crear una tabla analitica por persona con metadatos de modulo, tipo de variable, universo valido, codigo, etiqueta y ponderador. Comprobarla con validaciones de claves y rangos.
2. **Deteccion automatizada de riesgo:** construir modelos separados para anemia en mujeres, anemia infantil y riesgo metabolico. Reportar sensibilidad, especificidad, AUC, calibracion y falsos negativos; no usar exactitud como unico criterio.
3. **Priorizacion territorial:** generar tableros por area, region y departamento. La primera prioridad de seguimiento debe incluir ninas/os y mujeres rurales, sin convertir el territorio en diagnostico individual.
4. **Alertas explicables:** usar modelos interpretables o explicaciones de variables para que el personal conozca por que una persona fue priorizada. Una alerta debe recomendar confirmacion clinica, no etiquetar enfermedad.
5. **Seguimiento de costos y carga:** la EDSA no contiene costos hospitalarios ni tiempo de atencion. Para comprobar la reduccion de costos se necesita enlazar el riesgo con registros administrativos y medir consultas, derivaciones, hospitalizaciones y tiempo hasta confirmacion.
6. **Monitoreo de calidad:** registrar fecha de medicion, resultado, rechazo, no presencia y causa de dato faltante. Asi se puede distinguir aumento real del riesgo de una mejora o deterioro en la cobertura de medicion.

## Limitaciones importantes

- No hay una variable directa que mida ``deteccion tardia`` ni costos del sistema.
- Las asociaciones son descriptivas y no prueban causalidad.
- El modelo inicial usa datos de encuesta y tiene AUC modesta; no debe desplegarse como instrumento de decision clinica.
- Los resultados poblacionales deben calcularse con el ponderador del modulo correspondiente e idealmente con estrato y UPM para inferencia de encuesta.
