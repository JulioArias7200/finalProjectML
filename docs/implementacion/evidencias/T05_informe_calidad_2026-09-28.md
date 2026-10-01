# Evidencia T05 · A03/A04 · 2026-09-28

Revisor: Codebuff (revisión técnica de esta implementación). Entradas: `tests/test_data_contract.py` (6 casos), `preprocessing/quality_report.json`, `preprocessing/bitacora_preprocesamiento.json`, `preprocessing/README.md`. Método: ejecución del plan de pruebas de nivel Datos definido en `05_plan_pruebas.md`.

## Ejecución

```
./.python/python.exe preprocessing/preprocessing.py          # regenera dataset + bitácora + informe (run_id PRE-20260928-d004f6ddd436)
./.python/python.exe -m unittest discover -s tests -p "test_data_contract.py" -v
```

```
Ran 6 tests in 0.930s
OK
```

Entorno: Python 3.13.14 (runtime embebido `.python/`, no requiere activar entorno virtual), pandas 3.0.5, numpy 2.5.1, scikit-learn 1.9.0. Datos de entrada congelados por SHA-256: `e711b839…927f7` (general) y `b41ad4ed…41b4a` (materiales); semilla 42 en usos aleatorios posteriores.

## Cobertura de casos mínimos del plan de pruebas (nivel Datos)

| Caso mínimo del plan | Comprobación ejecutada | Resultado |
|---|---|---|
| unicidad de empresa | `ID` único y no nulo en el módulo general | OK |
| cardinalidad de materiales | 6.427 utilizables de 6.428 físicas; 1.614 empresas; 0 huérfanas | OK |
| 152+15 campos | inventario T02 (A02) + estructura 3153×167 verificada | OK |
| tipos/unidades | `S12_*_B` excluidas de predictores mientras exista `S12_*_C` heterogénea | OK |
| faltantes vs cero | `valor_co=99999` se conserva, `-4`→ausente, cero explícito sigue siendo 0; empresa sin filas de materiales queda con importes `null` | OK |
| redondeo entre objetivos | 60 diferencias ≤ Bs 1, máximo Bs 1; discrepancia mayor detiene el proceso | OK |
| grupos sin datos | heatmap con `empty`/`suppressed` → JSON `null`; denominador compartido KPI/gráficos | OK |
| mapeo CAEB | 13 macrosectores observados (no 14 teóricos) | OK |

## Informe de calidad (fuente: `preprocessing/quality_report.json`)

- `general_rows` 3.153 / `general_unique_ids` 3.153; `materials_rows` 6.427 (1 fila vacía excluida y contada); `orphan_material_rows` 0.
- Conciliación: 3.093 pares exactos, 60 por redondeo ≤ Bs 1, `target_excluded_rows` 0.
- 13 macrosectores observados; código 99999 en campos monetarios: 0; `monetary_missing_after_join`: `total_valor_co` 1.540, `total_valor_uti` 1.539 (desconocido preservado, no cero).
- Capacidad: `S12_01_C` con 1.744 "ELIJA LA OPCION" y 216 nulos → decisión D07: sin normalización defendible, `S12_*_B` fuera de predictores y sin sumas entre unidades.
- Trazabilidad: bitácora e informe comparten el `run_id` de la misma ejecución, con SHA-256 de ambas entradas.

## Incidencias y mejoras registradas

1. **(Corregida en esta ejecución)** La primera pasada de T03 tenía `valores_afectados` de la etapa 1 miscalculado (contaba el total de filas de materiales en lugar de las celdas negativas/centinela afectadas: 1 real frente a 6.427). Corregido en `preprocessing.py`; la bitácora refleja ahora el valor real.
2. **(Mejora continua)** Revisar la matriz de faltantes de las 167 columnas fuera del espacio de predictores; no bloquea A03.
3. **(Cierre D05)** Umbral de supresión fijado en 5 con base empírica de 39 celdas N<5 y 21 vacías; ver evidencia T04.

Conclusión: los contratos de datos están probados y el informe de calidad es reproducible. Criterios A03 y A04 cumplidos; puerta G1 lista para revisión (T03–T05 `en_revision`), pendiente de que la revisión apruebe el cierre de la puerta G1.
