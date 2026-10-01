# Evidencia T02 · A02 · 2026-09-28

Revisor: Codex (revisión técnica de esta implementación). Entradas: `data/raw/MOD_ANUAL_S01-07_12_general_i.csv`, `data/raw/MOD_ANUAL_S10_materiales_i.csv`, [diccionario F1 del INE](https://anda.ine.gob.bo/index.php/catalog/252/data-dictionary/F1) y [ficha EAIMCS](https://anda.ine.gob.bo/index.php/catalog/252). Método: lectura de cabeceras con PowerShell e `Import-Csv`; comparación decimal invariante de `S00_01_A` y `S05_04`, sin publicar identificadores.

| Comprobación | Resultado |
|---|---:|
| Registros generales / IDs únicos | 3.153 / 3.153 |
| Columnas generales | 167 |
| Variables de encuesta / derivadas locales | 152 / 15 |
| Filas físicas de materiales / filas utilizables / empresas distintas con materiales | 6.428 / 6.427 / 1.614 |
| Objetivos exactamente iguales | 3.093 |
| Objetivos con diferencia | 60 |
| Diferencia absoluta máxima | Bs 1 |

El [inventario](../inventario_columnas.csv) enumera las 167 columnas, origen y función preliminar. Las 15 derivadas son `VPA`, `PC`, `ISPOINF`, `VIPP`, `VBP`, `EAC`, `OGO`, `VUMPEEI`, `CI`, `VA`, `SSB`, `OPP`, `PS`, `R`, `D`.

Decisión D01: `S00_01_A` será el objetivo de regresión; `S05_04` es control de conciliación y queda excluido de predictores, junto con los componentes `S05_*` y los 15 derivados hasta completar auditoría de fuga. La tolerancia de Bs 1 refleja la diferencia máxima observada y no autoriza reemplazo automático en datos futuros. El periodo se rotula como EAIMCS 2017 con cierres por actividad descritos en la ficha oficial; no se afirma que cada empresa cierre el 31 de diciembre.

Conclusión: A02 cumplido para el extracto actual. La elegibilidad de predictores restantes requiere G2.
