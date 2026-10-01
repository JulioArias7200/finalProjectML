# Especificación de visualizaciones

Cada gráfico debe mostrar título que diga qué se mide, unidad, periodo, población, N, versión de datos/modelo cuando corresponda, definición de filtro y nota de limitación. El estado “sin datos” no usa una barra de altura cero. Tooltips muestran valor completo y base de cálculo. Una tabla accesible resume los valores clave.

| Vista actual / propuesta | Problema a resolver | Diseño y criterio visual |
|---|---|---|
| KPI de cobertura y calidad | Mezcla marco oficial con tamaño del extracto | Mostrar `3.153 registros locales` y `10.044 marco oficial` como conceptos separados, sin llamar su cociente tasa de respuesta. Indicadores de faltantes y exclusiones con denominador. |
| Distribución de ingresos | Cola extrema comprime la mayoría | Histograma en `log1p(Bs)` o bandas de cuantiles, con opción Bs y ejes inequívocos; mediana y P90/P99; informar ceros y valores extremos. |
| Boxplots por departamento y sector | Grupos desiguales y etiquetas densas | Orden por mediana, N por grupo, escala log indicada; ocultar o señalar grupos bajo umbral predefinido; permitir desplazamiento y etiquetas completas. |
| Mapa departamento × sector | Sectores omitidos, celdas vacías como cero y N pequeños | Incluir los 13 sectores observados; selector `conteo`, `mediana` y `total`; `null`/tramado para celdas sin datos; umbral mínimo para métricas monetarias; tooltip N, unidad y valor. El color de mediana no comparte escala con conteo. |
| Correlaciones | Asociación puede parecer causalidad y depender de escala | Usar variables con unidad/transformación rotuladas, método de correlación y N pareado; advertir multicolinealidad y prohibir lectura causal. |
| Atípicos ingreso vs sueldos | Muestra de 500 puede ocultar casos señalados | Mostrar todos los casos señalados y muestreo reproducible del resto; informar `N total`, `N señalados`, `N dibujados` y regla. Mantener conteos de gráfico y tarjeta compatibles. |
| Comparación de modelos | R², RMSE(log) y MedAPE/100 aparecen en el mismo eje | Tres paneles o tabla: calidad adimensional, error monetario/log y porcentaje. Marcar modelo activo, prueba final, N y bandas de incertidumbre CV cuando sean válidas. Nunca graficar MedAPE/100 como si fuese R². |
| CV y prueba | Cuatro gráficos redundantes y comparaciones no homogéneas | Resumen de distribución por fold para una métrica elegida; junto a resultado único de prueba con escala y cohorte explícitas. Comparar mismo conjunto y métrica. |
| Predicción vs observado / residuos | Diagnóstico puede ocultar sesgos por tramo | Dispersión con diagonal, residuos vs predicción, cuantiles de error y panel por sector/rango; escala y N visibles; no dar intervalo de cobertura no validada. |
| Tabla de señales y bunching | “Riesgo” puede interpretarse como juicio individual | Título descriptivo, fórmula y sensibilidad visibles; resultados agregados por defecto, tamaños mínimos y acceso individual sujeto a `D04`. |
| Monitoreo de tráfico y drift | Datos simulados presentados como operación | Solo series reales con ventana, N, fuente y momento de actualización; simulación en modo demostración separado y rotulado. Si no hay observaciones, mostrar “sin telemetría”. |

La validación visual se hace en escritorio y móvil con capturas fechadas, más auditoría de lectores de pantalla/teclado para filtros, tabla y estados de carga. Ver [pruebas](05_plan_pruebas.md).
