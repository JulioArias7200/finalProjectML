# Plan de implementación

## Fase 0. Preparación y decisiones

1. Crear carpetas de salida sin alterar los archivos de fuente: `datos_procesados`, `modelos`, `reportes` y `notebooks` o sus equivalentes.
2. Crear un archivo de configuración con rutas relativas, semilla aleatoria y nombres de variables.
3. Confirmar en `diccionarioDS.md` los códigos exactos de las etiquetas y variables elegidas.
4. Mantener una bitácora de decisiones: variable, fuente, transformación, universo y justificación.

**Salida:** alcance congelado, catálogo de variables y entorno reproducible.

## Fase 1. Perfilado de las fuentes

Para cada fuente usada, generar sin modificarla:

- Número de filas y columnas.
- Nombres, tipos inferidos y tipos esperados.
- Nulos, valores únicos y distribución de categorías.
- Mínimo, máximo, percentiles y valores imposibles de variables numéricas.
- Duplicados de `folio` o `folio+nro`, según corresponda.
- Frecuencia de códigos especiales: no sabe, no responde, no aplica.

No se debe borrar una fila solo por tener un faltante durante esta fase. Primero se debe identificar el universo de cada pregunta.

**Salida:** reporte de perfilado y reglas de limpieza aprobadas.

## Fase 2. Tabla analítica M1

1. Leer `Peso_talla_hemo` y conservar solo registros con `tip_anemia_m` válido.
2. Crear `anemia_mujer` y comprobar sus frecuencias.
3. Validar que la clave persona (`folio+nro`) sea única en el universo objetivo; investigar cualquier duplicado antes de seguir.
4. Seleccionar desde `Mujer` predictores disponibles antes de la medición.
5. Añadir de `Hogar` solo predictores individuales permitidos; verificar cardinalidad uno a uno.
6. Añadir de `Vivienda` por `folio`; verificar que vivienda tenga una fila por folio.
7. Registrar las filas que no hicieron match y no imputar sus claves.
8. Eliminar de `X` identificadores y todas las variables de fuga de información.
9. Crear dos salidas: auditoría con claves y matriz de modelado sin identificadores.

**Control de cierre:** una fila por mujer con etiqueta válida; cada variable incluida tiene descripción, fuente y justificación temporal.

## Fase 3. Tabla analítica M10

1. Leer `HistorialParidad` y confirmar la variable de controles prenatales y sus valores especiales.
2. Definir la clave de evento: clave de mujer más identificador/fecha/número de nacimiento disponible.
3. Conservar eventos válidos; no aplicar deduplicación por mujer.
4. Convertir número de controles a tipo numérico y separar valores desconocidos de cero controles reales.
5. Unir atributos de `Mujer` por `folio+nro`; controlar que la unión no multiplique eventos.
6. Seleccionar únicamente predictores disponibles antes o durante la fase en que se quiere anticipar el número de controles.
7. Examinar distribución: porcentaje de cero, asimetría, máximos y posibles valores imposibles.
8. Crear salida de auditoría y matriz de modelado sin identificadores.

**Control de cierre:** una fila por evento válido, objetivo numérico no negativo y sin variables posteriores al evento.

## Fase 4. Limpieza y transformación

Aplicar por separado para M1 y M10:

1. Unificar textos, espacios, mayúsculas y codificaciones de categorías.
2. Recodificar Sí/No a binario conservando `No sabe` y `No responde` como categorías separadas o nulos documentados.
3. Marcar faltantes estructurales cuando la pregunta no correspondía por salto del cuestionario.
4. Excluir variables con fuga, duplicación semántica o más del umbral acordado de faltantes no recuperables; documentar cada exclusión.
5. Dividir train/validación/test antes de ajustar transformadores.
6. En entrenamiento: imputar numéricas con mediana y categóricas con moda o categoría “desconocido”, según la semántica.
7. Aplicar one-hot encoding a categorías y escalado a numéricas para regresiones. Los árboles no necesitan escalado, pero pueden recibir la misma matriz codificada.
8. Empaquetar estos pasos en un pipeline.

## Fase 5. Partición y validación

- Reservar 15 % para prueba final, sin usarlo al elegir hiperparámetros.
- Reservar 15 % para validación; usar 70 % para entrenamiento inicial.
- En M1 aplicar partición estratificada por `anemia_mujer`.
- Si hay dependencia familiar o varios eventos por madre en M10, aplicar partición agrupada por mujer para impedir que eventos de una misma persona aparezcan tanto en entrenamiento como en prueba.
- Fijar una semilla, por ejemplo `random_state=42`, y registrarla.

## Fase 6. Entrenamiento y selección

### M1

1. Regresión logística regularizada como A.
2. Árbol de decisión con profundidad limitada.
3. Random Forest con número de árboles, profundidad y mínimo de observaciones por hoja ajustados en validación.
4. Gradient Boosting con tasa de aprendizaje, estimadores y profundidad ajustados en validación.
5. Seleccionar por AUC, sensibilidad, calibración e interpretabilidad; no por accuracy aislada.

### M10

1. Regresión lineal como A.
2. Regresión polinomial grado 2 con regularización Ridge; no incrementar el grado sin evidencia de mejora validada.
3. Random Forest Regressor.
4. Gradient Boosting Regressor.
5. Comparar MAE, RMSE y R²; revisar gráficos de residuales y predicciones negativas de los modelos lineales.

## Fase 7. Comparación A/B y prueba final

1. Congelar el mejor modelo B según validación, sin observar aún el test.
2. Evaluar A y B una sola vez sobre el test reservado.
3. Preparar tabla comparativa con métricas, intervalos obtenidos por bootstrap si el tiempo lo permite, complejidad e interpretación.
4. Para M1 incluir rendimiento por área, región y grupo etario cuando la muestra lo permita.
5. Elegir B solo si la mejora es relevante y no empeora de manera inaceptable la equidad o interpretabilidad.

## Fase 8. Documentación y entrega

1. Guardar el pipeline y modelo elegido con versión y fecha.
2. Generar reporte de calidad, métricas, gráficos y tabla de importancia de variables.
3. Redactar limitaciones: encuesta transversal, AUC modesta previa de M1, cobertura de medición, faltantes estructurales y ausencia de validación externa.
4. Entregar una conclusión que use el término “priorización” y no “diagnóstico”.
