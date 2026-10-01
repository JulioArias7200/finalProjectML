# Evidencia T04 · A04 · 2026-09-28

Revisor: Codebuff (revisión técnica de esta implementación). Entradas: `dashboard/aggregation.py`, `dashboard/data_loader.py`, `data/processed/dataset_procesado.csv` (`run_id` de origen **PRE-20260928-d004f6ddd436**). Método: lectura del módulo de agregación, prueba con `unittest` y recuento directo sobre el dataset procesado.

Resultado esperado: todos los KPIs y gráficos coinciden para los mismos filtros; celdas sin observaciones son `null`; N y denominadores acompañan resultados; los subgrupos pequeños siguen una política definida.

Resultado observado:

| Comprobación | Resultado |
|---|---:|
| Fuente única de filtros y agregación | `dashboard/aggregation.py` (única capa; `data_loader` la consume sin recalcular) |
| Filtros válidos aplicados desde el mismo conjunto | `select_rows()` comparte selección para KPI, heatmap, boxplots y tabla |
| Filtro con valor inexistente | `ValueError` inmediato (base para respuesta 400 en la API) |
| Celdas vacías de la matriz depto×sector | `None` con `status="empty"` (JSON `null`, nunca 0) |
| Denominador compartido | `kpis["denominador"] == heatmap["denominador"]` (verificado en test) |
| Unidades en cada resultado | `unidad_ingresos="Bs"`, `unidad_conteo="empresas"`, `unidad_montos="millones de Bs"`, población y periodo etiquetados |

**Política de grupos pequeños (decisión D05).** Umbral `MIN_CELL_N = 5`: celdas o grupos con N < 5 muestran `count=None` y `status="suppressed"` con etiqueta `"<5"`; los estadísticos (`median`, `q25`, `q75`) son `null`. Los grupos existen en el listado (no se ocultan) pero sin valores difundibles. Alineado con la política de difusión del INE (umbral habitual de 5), sin exponer registros inferibles por complemento: la matriz reporta cada celda individualmente y el denominador general permanece visible.

Base empírica de la política sobre el extracto procesado: 117 celdas posibles depto×sector (9×13); 96 con al menos una empresa, 21 vacías y 39 con N<5. Sin supresión, 33 % de las celdas con datos expondrían medianas basadas en menos de 5 empresas.

Comprobación: `./.python/python.exe -m unittest discover -s tests -p "test_data_contract.py"` → `test_filtered_aggregations_share_denominator_and_suppress_small_cells` OK (comprueba denominador compartido, celda `suppressed` y rechazo de filtro inválido). Verificación adicional sobre datos reales: `dashboard.data_loader.DashboardDataLoader.get_filtered_views(depto, sector)` compone KPI + heatmap + grupos con la misma selección.

Conclusión: A04 cumplido en la capa de datos. La propagación de estos contratos a los endpoints `/api/*` y al frontend corresponde a T10–T12 y T13–T16; este módulo ya deja `null` vs `0` distinguibles y el denominador adjunto a cada respuesta.
