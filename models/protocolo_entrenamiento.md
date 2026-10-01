# Protocolo de modelado G2 · T06 (predefinido antes de entrenar)

Fecha de fijación: 2026-09-28, **antes** de la re-ejecución de `models/train.py` de esta iteración. Ningún umbral de este protocolo se eligió mirando los resultados de la prueba de esta ejecución. Cambios posteriores requieren nueva versión del protocolo, nueva ejecución y evidencia (regla de `06_decisiones_y_riesgos.md`).

## Entrada congelada

- Dataset: `data/processed/dataset_procesado.csv`, `run_id` de preprocesamiento **PRE-20260928-d004f6ddd436** (3.153 empresas × 184 columnas), con SHA-256 de las fuentes crudas registrados en `preprocessing/quality_report.json`.
- Espacio de predictores: los 9 `log_*` de `PREDICTOR_NUM_COLS` + `depto` + `sector_macro`. Sin `S05_*`, sin las 15 derivadas locales, sin `S12_*_B` (D07).
- Objetivo: `target` = `S00_01_A`; modelado en escala `log1p`, reporte dual en `log1p` y Bs (contrato 02).
- Semilla: `RANDOM_STATE_SEED = 42` para partición, CV y modelos.

## Partición y validación

1. **Prueba final reservada una sola vez:** 20 % estratificado por quintiles de `log1p(target)` (`train_test_split`, `random_state=42`). Se consulta **una vez** para el informe de selección; cualquier cambio posterior inicia versión nueva.
2. **CV interna solo sobre entrenamiento:** `StratifiedKFold(5, shuffle=True, random_state=42)` por quintiles. Selección de modelo campeón por CV + prueba única.
3. **Conjunto de calibración separado** para el intervalo predictivo (ver D02): 25 % del bloque de entrenamiento, estratificado por los mismos quintiles, excluido del ajuste.
4. Transformadores (`SimpleImputer(median)` + `StandardScaler`, `OneHotEncoder`) se ajustan **solo con entrenamiento** dentro de `Pipeline` (anti-fuga, contrato 02). La imputación por mediana es necesaria porque T03 preserva correctamente los faltantes de materiales como `null` (empresas sin declaración); el imputador se entrena dentro de cada pliegue de CV y del ajuste final.
5. Reproducibilidad: partición estable verificada por test (`mismos índices de prueba para semilla y datos idénticos`).

## Algoritmos fijados (sin búsqueda de hiperparámetros en esta iteración)

- Ridge (α=10.0) — línea base lineal.
- RandomForest (n_estimators=120, max_depth=16, min_samples_split=4, n_jobs=1).
- HistGradientBoosting (max_iter=150, max_depth=6, learning_rate=0.08).

## Métricas y escalas (A05)

- CV por pliegue y prueba final: R², MAE, RMSE en escala `log1p`; R², MAE, RMSE, MedAE y **MedAPE = mediana(|Y−Ŷ|/Y)·100** en escala Bs con retransformación Duan.
- **Subgrupos obligatorios en prueba:** por `sector_macro` (13 observados), por `depto` (9) y por quintiles de ingreso; cada subgrupo reporta N, R² Bs, MedAPE y error mediano. Subgrupos con N<10 se reportan con N y sin conclusión de desempeño.
- **Verificación de MedAPE ante objetivos bajos:** el objetivo mínimo del extracto es Bs 1.285.236 (lejos de cero); se registra la mediana del denominador por subgrupo para descartar inestabilidad por objetivos cercanos a cero.

## Decisión D06 — meta MedAPE (cerrada antes de entrenar)

La meta histórica MedAPE ≤ 25 % se mantiene como **referencia aspiracional**, no como criterio de aprobación de G2: con la evaluación previa (36,20 %) es sabido que el extracto no la alcanza. Regla aprobada: **el umbral de aprobación de esta iteración es MedAPE ≤ 40 % y R²(Bs) ≥ 0.70**; si no se cumple, la brecha se registra y el producto se rotula como prototipo limitado según la matriz de aceptación final. El dashboard nunca presentará 36 % como cumplimiento de la meta de 25 %; mostrará ambas cifras etiquetadas.

## Decisión D02 — intervalo predictivo calibrado (cerrada antes de calibrar)

Se adopta **conformal prediction (split conformal) en escala log1p**, calculado solo con el conjunto de calibración:

- No conformidad: `s_i = |y_i − ŷ_i|` en escala log.
- Cuantil conforme: `q̂ = ⌈(n+1)·0.90⌉/n` de los `s_i` (cobertura nominal 90 %).
- Intervalo por predicción: `[ŷ − q̂, ŷ + q̂]` en log, retransformado a Bs con Duan (`exp(ŷ)·s − 1`, acotado a 0).
- La etiqueta "90 %" solo se usa si la cobertura empírica en la **prueba final** queda dentro de [85 %, 95 %] (tolerancia global predefinida). Si queda fuera, se reporta la cobertura real y el intervalo **no** se anuncia como calibrado.
- Se mide cobertura y amplitud media global y por segmentos (`sector_macro`, `depto`, quintiles) sobre la prueba; segmentos con N<10 solo reportan cobertura con N visible.
- El método `±1,645 × RMSE(log)` queda **prohibido como "intervalo 90 %"** (contrato 02); puede mostrarse solo como referencia nominal rotulada, si el dashboard lo necesita.

## Entregables de la iteración

`registry.json` + `cv_results.json` + `test_predictions.csv` + `feature_importance.json` + `models/bitacora_modelos.json` de una **misma ejecución** compartiendo `run_id` y hashes (A07), más `models/protocolo_entrenamiento.md` (este documento, versionado por fecha).

## Criterios de salida de G2

1. A05: protocolo ejecutado tal cual; métricas globales y por subgrupo publicadas; D06 aplicada.
2. A06: cobertura empírica global y por segmentos medida con el método conformal; etiqueta condicionada a la tolerancia.
3. A07: paquete con `run_id` único, hashes de todos los artefactos y rechazo de mezclas entre ejecuciones.
4. Pruebas automatizadas `tests/test_model_evaluation.py` en verde.
