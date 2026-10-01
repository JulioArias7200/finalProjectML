# Evidencia T07 · A05 · 2026-09-28

Revisor: Codebuff (revisión técnica de esta implementación). Ejecución: `./.python/python.exe models/train.py` → versión **v1.20260928.2256**, `run_id` **RUN-20260928-b3cfc0795ed7** (preprocesamiento PRE-20260928-d004f6ddd436). Entorno: Python 3.13.14, scikit-learn 1.9.0, semilla 42.

Resultado esperado: evaluación honesta global y por subgrupo, con escalas correctas y prueba final consultada una sola vez.

## Resultado global (conjunto de prueba, 631 empresas)

| Modelo | CV R² (log) | Test R² (log) | Test R² (Bs) | MedAPE | Cobertura conformal |
|---|---|---|---|---|---|
| Ridge | 0,5662 ± 0,054 | 0,5953 | 0,5750 | 67,41 % | 84,47 % |
| **RandomForest** 🏆 | **0,7609 ± 0,027** | **0,7824** | **0,7396** | **35,10 %** | **88,27 %** |
| HistGradientBoosting | 0,7630 ± 0,030 | 0,7744 | 0,6286 | 39,37 % | 90,65 % |

Factor de Duan del campeón: 1,0404. Cambios frente a la iteración previa: la CV ahora corre solo sobre el bloque de ajuste y la imputación por mediana se añadió dentro del pipeline; por eso las cifras difieren levemente de las históricas (p. ej. MedAPE 36,20 % → 35,10 %) y **no deben mezclarse** en una misma comparación sin cohorte (contrato 02).

## Resultado por subgrupo (prueba)

- **13 sectores observados**: cada uno con N, mediana del objetivo y, si N ≥ 10, R²(Bs), MedAPE y error mediano. Los segmentos con N < 10 (p. ej. Actividades Inmobiliarias, N=8) se publican **sin conclusión de desempeño** (`nota: N<10`).
- **9 departamentos** y **5 quintiles de ingreso** con la misma política.
- Estabilidad del MedAPE ante objetivos bajos: el objetivo mínimo del extracto es Bs 1.285.236 y la mediana del denominador por quintil se registra en `registry.json`; sin indicios de inestabilidad por objetivos cercanos a cero.

## Veredicto D06

MedAPE 35,10 % ≤ 40 % y R²(Bs) 0,7396 ≥ 0,70 → **umbral de aprobación cumplido**. La meta histórica ≤ 25 % **no se alcanza**; brecha ≈ 10 puntos documentada y rotulada en `registry.json` (`metas`) y `models/README.md`.

Comprobación: `test_test_metrics_are_recomputable_from_test_predictions` (R² y MedAPE se recalculan desde `test_predictions.csv` y coinciden con el registro) y `test_champion_meets_d06_threshold_and_meta_is_labeled`. Suite completa: 8/8 OK.

Conclusión: evaluación global y por subgrupo completada y reproducible; A05 cumplido.
