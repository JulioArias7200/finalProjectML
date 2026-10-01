# Decisiones y riesgos

Las decisiones técnicas se cierran por tarea, con fecha, responsable, evidencia y justificación. No cambiar un umbral después de mirar resultados de prueba sin documentar una nueva ejecución.

| ID | Decisión pendiente | Opciones / regla propuesta | Se resuelve en |
|---|---|---|---|
| D01 | Objetivo monetario | **Decidido 2026-09-28:** usar `S00_01_A` como objetivo, coherente con el pipeline actual y la carátula de ingresos. `S05_04` queda para conciliación, nunca predictor. En el extracto actual 60/3.153 pares difieren por redondeo, máximo Bs 1; nuevos pares con diferencia mayor se reportan como incidencia, no se corrigen silenciosamente. Véase `evidencias/T02_inventario_objetivo_2026-09-28.md`. | T02 |
| D02 | Intervalo y criterio de cobertura | **Cerrado 2026-09-28 en T08:** intervalo por *split conformal* en escala log1p con conjunto de calibración separado (631 empresas), cobertura nominal 90% y tolerancia global predefinida [85%, 95%] antes de mirar la prueba. Resultado: q̂(log)=0,9025, cobertura empírica 88,27% → etiqueta "intervalo calibrado" procede. Cobertura por quintiles 83,5%–93,7% publicada por segmento; el método ±1,645×RMSE queda prohibido como "90%" y solo como referencia nominal. Ver `evidencias/T08_...2026-09-28.md` y `models/protocolo_entrenamiento.md`. | T08 (cerrada) |
| D03 | Versionado API | **Cerrado 2026-09-28 en T12:** se mantienen las rutas existentes con `meta` completo en todas las respuestas analíticas; no se introduce `/api/v1` en esta iteración para no romper consumidores. Si se requiere coexistencia futura, `/api/v1/*` se añadirá como alias sin cambio de semántica. Contrato documentado en `dashboard/README.md`. | T12 (cerrada) |
| D04 | Exposición de datos individuales | Revisar condiciones de uso de los microdatos y acceso autorizado. Por defecto, entrega pública agregada; detalle empresarial condicionado a permiso y control verificable. | T11 |
| D05 | Tamaño mínimo de celda | **Cerrado 2026-09-28 en T04:** umbral `MIN_CELL_N = 5` en `dashboard/aggregation.py`. Grupos y celdas con N<5 muestran `null` con `status="suppressed"` y etiqueta `"<5"`; los grupos siguen listados sin valores difundibles. Base empírica: 39 celdas depto×sector con N<5 y 21 vacías en el extracto (ver `evidencias/T04_agregacion_supresion_2026-09-28.md`). Alineado con la práctica de difusión del INE; se reevaluará si la política oficial fija otro umbral. | T04 (cerrada) |
| D06 | Umbral de meta MedAPE | **Cerrado 2026-09-28 en T06:** la meta histórica ≤25% se conserva como referencia aspiracional que **no** se alcanza; el umbral de aprobación de la iteración G2 se fijó **antes** de entrenar en MedAPE ≤40% y R²(Bs) ≥0,70 (`models/protocolo_entrenamiento.md`). Resultado: MedAPE 35,10%, R²(Bs) 0,7396 → umbral cumplido y brecha frente a 25% documentada. El dashboard debe mostrar ambas cifras etiquetadas. | T06 (cerrada) |
| D07 | Variables de capacidad | **Cerrado 2026-09-28 en T03:** `S12_01_B` y `S12_02_B` quedan excluidas de los predictores; no existe transformación defendible porque `S12_01_C` registra 1.744 respuestas "ELIJA LA OPCION" y 216 nulos, y las unidades declaradas son heterogéneas (KILOGRAMO, ARROBA, …). No se suman cantidades entre unidades; los valores originales se conservan para auditoría (ver `evidencias/T03_limpieza_unidades_sentinelas_2026-09-28.md`). | T03 (cerrada) |

| Riesgo | Efecto posible | Mitigación y evidencia |
|---|---|---|
| Fuga de información por columnas derivadas o componentes del objetivo | Métricas optimistas | Inventario temporal/algebraico y pruebas de exclusión antes del entrenamiento. |
| Muestra dirigida y periodos de cierre distintos | Conclusiones poblacionales o temporales indebidas | Etiquetas de población y periodo; sin expansión ni tasa de respuesta inferida del extracto. |
| Colas extremas y grupos pequeños | Gráficos engañosos e intervalos débiles | Escala clara, N, cuantiles, sensibilidad y supresión según D05. |
| Dos bitácoras/ejecuciones en la interfaz | Modelo y métricas incompatibles | Paquete atómico con `run_id` y hashes; rechazo de mezcla. |
| Privacidad y uso de señales individuales | Divulgación o interpretación dañina | Resolver D04, agregar por defecto, lenguaje descriptivo y acceso controlado. |
| Drift simulado confundido con real | Confianza falsa en monitoreo | Telemetría real versionada, demostración separada y N/ventana visibles. |

En la implementación, añadir una entrada fechada por cada decisión tomada y registrar el resultado de cualquier cambio de alcance o umbral en la evidencia de la tarea correspondiente.
