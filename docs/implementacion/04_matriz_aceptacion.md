# Matriz de aceptación y trazabilidad

Cada criterio tiene una comprobación observable. **Estado inicial de todos: pendiente**. El revisor registra el resultado en la evidencia de la tarea y solo después cambia `seguimiento.csv`. Una puerta se aprueba cuando todas sus tareas cumplen los criterios relacionados.

| ID | Objetivo y tareas | Criterio de aceptación | Evidencia requerida |
|---|---|---|---|
| A01 | Documentación fiable · T01 | Los cuatro documentos heredados conservan utilidad; enlaces relativos funcionan; metas históricas se distinguen de resultados; afirmaciones externas tienen fuente. | Informe de enlaces y revisión editorial. |
| A02 | Fuente y objetivo · T02 | Inventario 152+15 documentado; 3.153/6.428 y periodo respaldados; `S00_01_A` y `S05_04` conciliados con regla de redondeo y decisión formal. | Tabla de variables, reporte de diferencias y decisión D01. |
| A03 | Calidad de datos · T03–T05 | Claves, cardinalidad, faltantes, ceros, centinelas, unidades, exclusiones y 13 sectores observados comprobados; no se suman capacidades de unidades distintas. | Informe de calidad y pruebas de contratos. |
| A04 | Agregación · T04 | Todos los KPIs y gráficos coinciden para los mismos filtros; celdas sin observaciones son `null`; N y denominadores acompañan resultados; subgrupos pequeños siguen la política definida. | Casos de agregación reproducibles. |
| A05 | Evaluación modelo · T06–T08 | Transformaciones ajustadas solo en entrenamiento; CV, prueba final y escalas etiquetadas; métricas globales y por subgrupo calculadas; meta MedAPE ≤25 % aprobada o declarada no alcanzada con brecha. | Protocolo, resultados y pruebas estadísticas. |
| A06 | Incertidumbre · T08 | Intervalo nominal reporta cobertura y amplitud empíricas en prueba y segmentos; si no satisface umbral predefinido, no se anuncia como intervalo calibrado. | Curva/reporte de cobertura y decisión D02. |
| A07 | Artefactos únicos · T09–T10 | Modelo, registro, CV, predicciones e importancias comparten `run_id`, hashes y cohorte; servidor rechaza mezcla o ausencia. | Manifiesto y prueba de carga inválida. |
| A08 | API y acceso · T10–T12 | Respuestas incluyen metadatos mínimos; entradas inválidas dan 400; fallo de paquete da 503; acceso individual cumple D04; ninguna señal se presenta como acusación. | Pruebas API, revisión de acceso y ejemplo anonimizado. |
| A09 | Gráficos · T13–T16 | Todas las vistas cumplen [especificación](03_diseno_graficos.md): unidad, N, escala, periodo, etiquetas completas, estados vacíos y alternativas accesibles. Comparación de métricas usa escalas separadas. | Capturas escritorio/móvil y revisión visual. |
| A10 | Monitoreo · T17 | Tráfico, latencia y drift provienen de registros reales con ventana y N; simulación solo en modo rotulado; sin tráfico se muestra “sin telemetría”. | Prueba con tráfico controlado y arranque vacío. |
| A11 | Integración y entrega · T18–T19 | Recorrido completo funciona; documentación de ejecución y límites corresponde a producto; pruebas automatizadas y revisión manual pasan; G0–G5 aprobadas. | Registro de pruebas, informe final y salida de `-RequireComplete`. |

## Decisión de aceptación final

1. Ejecutar las pruebas de [05_plan_pruebas.md](05_plan_pruebas.md) con el paquete elegido.
2. Revisar cada evidencia contra la fila A01–A11. Un archivo existente sin resultado verificable no cuenta.
3. Actualizar estados, revisor y fecha. Ejecutar `./scripts/verificar_plan.ps1 -RequireComplete`.
4. Publicar un acta con `run_id`, dataset, N, métricas, criterios no alcanzados, limitaciones y decisión de exposición de datos. Si A05 o A06 no cumplen su umbral, la entrega puede describir un prototipo limitado, pero no un modelo validado para uso operativo.
