# Evidencia T03 · A03 · 2026-09-28

Revisor: Codebuff (revisión técnica de esta implementación). Entradas: `data/raw/MOD_ANUAL_S01-07_12_general_i.csv` (SHA-256 `e711b839…927f7`), `data/raw/MOD_ANUAL_S10_materiales_i.csv` (SHA-256 `b41ad4ed…41b4a`), `preprocessing/preprocessing.py`, `preprocessing/quality_report.json`. Ejecución: `run_id` **PRE-20260928-d004f6ddd436**, comando `.python/python.exe preprocessing/preprocessing.py` desde la raíz (Python 3.13.14, pandas 3.0.5, sin entorno virtual obligatorio; el runtime local `.python/` está excluido de Git).

Resultado esperado: claves, cardinalidad, faltantes, ceros, centinelas, unidades y exclusiones comprobados; no se suman capacidades de unidades distintas; sin unidades incompatibles ni fugas en el dataset modelable.

Resultado observado (comandos reproducibles en la sección Comprobación):

| Comprobación | Resultado |
|---|---:|
| Empresas generales / IDs únicos / columnas | 3.153 / 3.153 / 167 |
| Filas de materiales utilizables (1 fila totalmente vacía excluida y contada) | 6.427 de 6.428 físicas |
| Empresas con materiales / filas huérfanas | 1.614 / 0 |
| Objetivo `S00_01_A` conciliado con `S05_04` | 3.093 exactos; 60 por redondeo ≤ Bs 1; exclusión por discrepancia: 0 |
| Empresas retenidas con objetivo > 0 | 3.153 (100 %) |
| Faltantes en predictores de estructura (S01/S02/S06/S07) | 0 |
| `total_valor_co` / `total_valor_uti` ausentes tras el join (empresas sin declaración) | 1.540 / 1.539 |
| Código 99999 detectado en campos monetarios del extracto | 0 (conteo documentado; no se recodifica globalmente) |
| Macrosectores observados | 13 (no se declaran los 14 teóricos) |
| `S12_01_C` | 1.744 respuestas "ELIJA LA OPCION", 216 nulas; unidades reales heterogéneas (KILOGRAMO, ARROBA, …) |

Decisiones aplicadas (reglas vigentes en `preprocessing/README.md`):

1. **Sentinelas:** el valor exacto 99999 se cuenta por campo pero no se recodifica globalmente; puede ser un importe real. Un importe alto nunca se trata como ausente. Los importes negativos pasan a ausente (sin acotar a cero). En este extracto no apareció ningún 99999 en campos monetarios del modelo.
2. **Faltantes ≠ cero:** `n_insumos=0` significa ausencia de filas enlazadas; los importes de materiales sin declaración permanecen `null` (1.540/1.539 empresas). Un cero explícito del origen sigue siendo cero. La imputación de predictores se hará solo dentro del pipeline de entrenamiento.
3. **Unidades (decisión D07):** las cantidades de capacidad `S12_01_B` y `S12_02_B` quedan **excluidas de los predictores** mientras no se interpreten con su unidad `S12_*_C`. Evidencia de imposibilidad de normalización en este extracto: 1.744 registros con la opción sin seleccionar "ELIJA LA OPCION" y 216 nulos en `S12_01_C`; el resto mezcla KILOGRAMO, ARROBA y otras unidades. No se suman capacidades heterogéneas; los valores originales se conservan para auditoría.
4. **Conciliación del objetivo:** `S00_01_A` es el objetivo (decisión D01); `S05_04` solo controla conciliación y está excluido de predictores junto con `S05_01`–`S05_03` y las 15 derivadas locales. Una diferencia mayor a Bs 1 en ejecuciones futuras detiene el proceso como incidencia.

Comprobación: `./.python/python.exe -m unittest discover -s tests -p "test_data_contract.py"` → 6/6 OK, incluye `test_extract_structure_and_target_reconciliation`, `test_materials_keep_unknown_separate_from_zero`, `test_missing_material_record_is_not_fabricated_monetary_zero` y `test_capacity_requires_unit_and_is_not_model_predictor`. Los valores de la tabla provienen de `preprocessing/quality_report.json` y de una lectura directa del dataset procesado.

Conclusión: A03 cumplido para el extracto actual con la política de unidades documentada. La revisión de la matriz de faltantes por campo completo (167 columnas) queda como mejora continua; las columnas fuera del espacio de predictores no afectan al contrato de modelado.
