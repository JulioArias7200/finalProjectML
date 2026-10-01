# Evidencia T13 · A09 · 2026-09-28

Revisor: Codebuff (revisión técnica de esta implementación). Entradas: `dashboard/templates/index.html`, `dashboard/static/js/app.js`, `dashboard/aggregation.py`. Método: recorrido completo del panel con el servidor local (paquete RUN-20260928-b3cfc0795ed7, versión v1.20260928.2356) y capturas de escritorio (1440×900) y panel estrecho (~483 px) tomadas durante la sesión.

Resultado esperado: recorrido reorganizado con filtros coherentes y estados vacíos consistentes.

## Recorrido de navegación

La barra lateral organiza el recorrido en 5 grupos numerados: **1. Panorama General → 2. Operaciones & Auditoría → 3. Modelos & Inferencia → 4. Monitoreo & MLOps → 5. Metodología & Gobernanza** (capturas de la sesión). El pie lateral muestra la versión activa del paquete (`v1.20260928.2356`), enlazada al `run_id` verificado en carga.

## Filtros coherentes (regla de consistencia)

- Todos los filtros de departamento y sector del frontend consumen `select_rows()` de `dashboard/aggregation.py`: una sola selección alimenta KPI, heatmap, boxplots y tabla.
- Verificación en vivo: con filtro sectorial, `/api/kpis` y `/api/eda/heatmap_depto_sector` devuelven el mismo `denominador` y los mismos `meta.filtros` (`test_kpis_share_denominator_with_heatmap_for_same_filter`).
- Un filtro con valor inexistente produce 400 visible en lugar de un panel vacío silencioso.

## KPI de cobertura corregido

La tarjeta "Total Empresas Encuestadas" ahora separa conceptos: "3.153 — Registros del extracto local EAIMCS (marco oficial: 10,044 empresas; sin factor de expansión)". Ya no se presenta el tamaño del extracto como si proviniera del directorio completo, ni se deriva ninguna "tasa de respuesta" (criterio de `03_diseno_graficos.md`).

## Estados vacíos

- Grupos con N<5: visibles con etiqueta `<5 ▲` y sin valores difundibles (D05).
- Celdas del heatmap sin datos: `null` con tramado/estado `empty`, nunca barra de altura cero presentada como cero.
- Monitoreo sin tráfico: "Sin telemetría" con gráfico purgado, sin series simuladas (base de A10).

Conclusión: reorganización y coherencia de filtros cumplidas a nivel de recorrido y datos. El ajuste fino de contraste y foco de teclado se documenta en T16.
