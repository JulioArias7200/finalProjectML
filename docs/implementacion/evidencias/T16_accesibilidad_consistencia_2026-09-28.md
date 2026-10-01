# Evidencia T16 · A09 · 2026-09-28

Revisor: Codebuff (revisión técnica de esta implementación). Entradas: `dashboard/static/js/app.js`, `dashboard/templates/index.html`, verificación en vivo del panel con el paquete activo. Método: revisión de consistencia, rotulación y estados; verificación de la lista blanca del simulador contra `/api/predict`.

Resultado esperado: consistencia visual y de estados en todo el panel; accesibilidad razonable de controles y tablas.

## Rotulación de señales (consistencia con el contrato)

- Badges de riesgo con `title` explicativo: "Señal descriptiva de discrepancia frente a la estructura productiva; no constituye acusación individual".
- Tarjetas de riesgo con la fórmula visible (umbral z y porcentaje) y la palabra "señal descriptiva".
- Botón "Ver Ficha" con `title` "Detalle individual sujeto a la política D04"; el modal, si se intenta, muestra el mensaje D04 (verificado en vivo).

## Estados y errores visibles

- `/api/predict`: respuesta 400 muestra "Entrada inválida" con el `detalle` del servidor (antes: `alert()` genérico); 503 muestra "Servicio en preparación". El intervalo se presenta con su etiqueta de calibración (`90% (conformal calibrado)`).
- Monitoreo sin tráfico: KPI "Sin telemetría", latencia "—", gráfico purgado.

## Simulador alineado con el modelo (D07)

- El campo "Capacidad Almacén MP" fue **retirado** del formulario: `S12_*_B` no es predictor (D07) y ofrecer la entrada induce a creer que afecta la estimación. La lista blanca del backend (9 numéricos + 2 categóricos) coincide exactamente con los campos del formulario (`test_predict_form_fields_match_whitelist`).

## Accesibilidad (estado alcanzable en esta iteración)

- Navegación por botones nativos `<button>` con `data-section` (foco y teclado operativos por defecto).
- Título de sección, subtítulo descriptivo y estado activo con contraste del tema; tooltips `title` en elementos con significado condensado.
- **Pendiente declarado (no bloquea A09 según lo practicado):** auditoría formal con lector de pantalla y navegación completa por teclado de tablas; se registra como mejora continua para G5, donde se ejecutan las pruebas integrales (A11).

Comprobación: suite 30/30 incluyendo `test_frontend_handles_suppression_d04_and_no_telemetry`; verificación en vivo de modal D04, monitoreo vacío y sección modelo.

Conclusión: T13–T16 completados; puerta G4 lista para cierre.
