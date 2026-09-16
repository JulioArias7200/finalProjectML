# Estado y bitácora del proyecto

## Estado actual

**Fase actual:** planificación y documentación.

La documentación de la raíz ya identifica las fuentes EDSA 2023, sus unidades de observación, las reglas de unión, riesgos de fuga de información y un conjunto amplio de modelos posibles. Sin embargo, aún no se observan en el proyecto transformaciones Pentaho, scripts de entrenamiento, tablas analíticas procesadas ni modelos serializados.

El cuaderno `covertir.ipynb` es un intento de conversión de SAV a CSV; no forma parte del flujo de ML y no debe considerarse el pipeline de preprocesamiento. Los CSV ya existen y son las fuentes de entrada previstas.

## Decisiones tomadas

| Fecha | Decisión | Motivo |
|---|---|---|
| 2026-09-15 | Limitar el alcance a M1 y M10. | Permite cubrir clasificación, regresión, bagging, boosting y comparación A/B sin dispersar el trabajo. |
| 2026-09-15 | M1 será el modelo prioritario. | Está alineado con el objetivo sanitario y tiene etiqueta documentada. |
| 2026-09-15 | M10 se usará como problema de regresión. | Permite aplicar lineal y polinomial sobre una variable numérica real, sin usar métodos inadecuados para anemia binaria. |
| 2026-09-15 | Las fuentes se preservan sin cambios. | Garantiza trazabilidad y reproducibilidad. |
| 2026-09-15 | A/B se interpreta como evaluación offline. | No hay intervención prospectiva ni autorización para experimentar con personas. |

## Avance por componente

| Componente | Estado | Próxima acción |
|---|---|---|
| Inventario de bases | Completado según documentación existente | Confirmar tipos/códigos al implementar. |
| Selección de dos modelos | Completado | Congelar variables candidatas. |
| Documentación de alcance | Completado | Mantener actualizada la bitácora. |
| Perfilado de fuentes | Pendiente | Generar estadísticas, faltantes y validación de claves. |
| Tabla M1 | Pendiente | Construir etiqueta, validar joins y excluir fuga. |
| Tabla M10 | Pendiente | Validar controles prenatales y conservar nivel evento. |
| Pipeline de preprocesamiento | Pendiente | Implementar pipeline reproducible. |
| Entrenamiento baseline | Pendiente | Entrenar logística y lineal. |
| Bagging/boosting | Pendiente | Ajustar solo con validación. |
| A/B offline | Pendiente | Evaluar A y B sobre test congelado. |
| Informe final | Pendiente | Integrar resultados, limitaciones y conclusiones. |

## Riesgos abiertos

1. **Rendimiento limitado de M1.** La documentación existente registra un AUC inicial de aproximadamente 0,57. Se debe reportar con honestidad y no convertirlo en una herramienta clínica.
2. **Faltantes estructurales.** Las tasas de faltantes son altas en módulos de encuesta por saltos de cuestionario; la eliminación indiscriminada puede sesgar la muestra.
3. **Cardinalidad de uniones.** La unión de tablas de eventos con tablas de personas puede duplicar filas si no se controla la unidad final.
4. **Temporalidad.** Algunas variables describen consecuencias del resultado o del parto; deben ser excluidas como predictores.
5. **Interpretación de A/B.** La comparación es computacional, no un ensayo experimental sobre personas.

## Próximo hito

Completar el perfilado de las cinco fuentes usadas, revisar los códigos de `tip_anemia_m` y `ms04_0411`, y producir los reportes de claves, faltantes y rangos. Solo después de aprobar esos controles se debe crear la primera tabla analítica.
