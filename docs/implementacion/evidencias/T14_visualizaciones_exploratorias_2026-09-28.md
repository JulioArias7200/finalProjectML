# Evidencia T14 · A09 · 2026-09-28

Revisor: Codebuff (revisión técnica de esta implementación). Entradas: `dashboard/static/js/app.js` (renderizadores), `dashboard/aggregation.py`, respuestas de `/api/eda/*` verificadas en vivo. Método: inspección de cada vista exploratoria contra su especificación en `03_diseno_graficos.md`.

Resultado esperado: visualizaciones exploratorias con unidad, N, escala y estados vacíos por especificación.

| Vista | Correcciones aplicadas | Verificación |
|---|---|---|
| Heatmap depto×sector | Selector conteo/mediana/total; celdas `empty`/`suppressed` como `null`; mediana y conteo en escalas separadas (colores distintos por métrica); denominador en `meta` | `test_views_needed_by_frontend_have_expected_shapes` + verificación en vivo |
| Boxplots por departamento y sector | Etiqueta con `N=` por grupo; grupos suprimidos rotulados `<5 ▲` con muestra vacía; escala log rotulada en el eje; tooltip con nombre completo y N | `status === 'suppressed'` en app.js; respuesta con `status`/`count_label` |
| Distribución de ingresos | Alternancia Bs natural vs log1p con ejes rotulados; mediana y promedio con nota de cola Pareto | respuesta `/api/eda/distribution` con `raw_values`/`log_values`/`total_count` |
| Correlaciones | Método rotulado ("Pearson sobre escala log(1+x); asociación no causal"); conteos pareados por par (`pair_counts`); NaN → `null` | `get_correlation_data` en data_loader |
| Atípicos ingreso vs sueldos | Todos los casos señalados + muestreo reproducible (semilla 42) del resto; `total_empresas`, `total_outliers_iqr`, `total_dibujados` y regla en la respuesta | `get_outliers_data` |

**N visible en cada grupo:** los boxplots ahora muestran `Nombre (N=xx)` directamente en el eje, cumpliendo "N por grupo" sin requerir tooltip.

Comprobación: verificación en vivo de las respuestas con el paquete activo (sección Panorama y secciones exploratorias del panel) y suite automatizada 30/30.

Conclusión: A09 en su dimensión exploratoria cumplido; capturas de la sesión disponibles en el hilo de trabajo.
