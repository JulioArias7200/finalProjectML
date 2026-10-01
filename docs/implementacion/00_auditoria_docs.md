# Auditoría de `docs/`

Revisión del 2026-09-28. **Conservar los cuatro archivos**, porque registran propósito, fuente y definiciones de variables. No usarlos como evidencia de resultados actuales hasta corregir los puntos indicados. La revisión de relevancia no elimina ni reescribe el material histórico.

| Documento | Valor que conserva | Corrección necesaria | Decisión |
|---|---|---|---|
| [`docs/README.md`](../README.md) | Índice, objetivo y navegación conceptual | Sustituir enlaces `file:///` de otra computadora por relativos; separar meta de resultado observado; corregir que MedAPE se mide en porcentaje sobre Bs, no en escala log; revisar cobertura y sectores. | Conservar y actualizar en G0. |
| [`01_analisis_dataset_EAIMCS.md`](../01_analisis_dataset_EAIMCS.md) | Contexto de encuesta, universo y limitaciones del diseño | Citar con precisión la fuente para periodo y cobertura; no convertir ausencia de respuesta o códigos grandes en valores perdidos sin regla oficial; distinguir marco de 10.044 de extracto local de 3.153. | Conservar como contexto, validar afirmaciones en G0–G1. |
| [`02_diccionario_datos_EAIMCS.md`](../02_diccionario_datos_EAIMCS.md) | Traducción de campos y unidades | Distinguir 152 variables de encuesta de 167 columnas locales: 15 derivadas; no fijar enero–diciembre para todos los cierres; documentar que `S12_*_B` requiere la unidad `S12_*_C`; precisar relación `S00_01_A`/`S05_04`. | Conservar como diccionario, corregir en G0–G1. |
| [`marco_logico_ingresos_operativos.md`](../marco_logico_ingresos_operativos.md) | Objetivos y criterios iniciales | Marcar presupuestos/fechas como históricos; sustituir “0 casos” por conteo local comprobado; separar umbrales aspiracionales de desempeño alcanzado; armonizar definición de objetivo. | Conservar como acta histórica; añadir estado real en G0. |

## Hallazgos transversales que bloquean la declaración de cumplimiento

- Los datos locales generales tienen 3.153 filas y 167 columnas; materiales 6.428 filas y 8 columnas. Los 152 campos de encuesta y 15 derivados del CSV local requieren procedencia explícita. El marco oficial de 10.044 empresas no es el denominador de una tasa de respuesta estimable con este extracto por sí solo.
- `S00_01_A` y `S05_04` coinciden exactamente en 3.093 de 3.153 filas; 60 difieren solo por precisión/redondeo: diferencia absoluta máxima Bs 1. Debe definirse y probarse una tolerancia. La elección del objetivo debe quedar explícita.
- El modelo activo informa R² en Bs ≈ 0,753 y MedAPE ≈ 36,20 % sobre prueba. Una meta histórica de MedAPE ≤ 25 % no está cumplida. No reducirla a una etiqueta de logro.
- El catálogo oficial y la política de difusión indican uso estadístico y protección de información individual. Cualquier afirmación legal específica sobre usos prohibidos debe tener respaldo textual verificable. La vista de empresas individuales requiere revisión de acceso y divulgación en G3.

La tarea `T01` se ejecutó con correcciones y enlaces relativos en los cuatro documentos. `T02` se apoya en el [inventario completo](inventario_columnas.csv) y la decisión D01. Quedan pendientes las comprobaciones de datos, predictores, acceso y desempeño de G1–G5. Los hallazgos proceden de [fuentes y línea base](07_fuentes_y_linea_base.md).
