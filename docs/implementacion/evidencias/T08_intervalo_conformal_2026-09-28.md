# Evidencia T08 · A06 · 2026-09-28

Revisor: Codebuff (revisión técnica de esta implementación). Ejecución: misma iteración **RUN-20260928-b3cfc0795ed7**. Entradas: `models/train.py` (sección conformal), `models/protocolo_entrenamiento.md` (D02), `dashboard/artifacts/registry.json`, `dashboard/artifacts/test_predictions.csv`.

Resultado esperado: intervalo predictivo calibrado con procedimiento reproducible sobre datos separados de entrenamiento; cobertura y amplitud empíricas globales y por segmentos; etiqueta "90 %" solo si satisface el umbral predefinido.

## Método (fijado antes de calibrar, D02)

*Split conformal* en escala `log1p`: no conformidad `s_i = |y_i − ŷ_i|`; cuantil conforme `q̂ = s_(⌈(n+1)·0,90⌉)` sobre el **conjunto de calibración separado** (631 empresas, excluido del ajuste y de la CV); intervalo `[ŷ − q̂, ŷ + q̂]` retransformado a Bs con Duan. Tolerancia global predefinida: cobertura empírica en prueba dentro de [85 %, 95 %]. El método ±1,645×RMSE queda prohibido como "intervalo 90 %" (contrato 02) y se conserva solo como referencia nominal rotulada.

## Resultado observado

| Magnitud | Valor |
|---|---:|
| q̂ conforme (escala log) | 0,9025 |
| Cobertura empírica global en prueba | **88,27 %** (527/631 dentro del intervalo) |
| ¿Dentro de tolerancia [85 %, 95 %]? | Sí → `etiqueta_calibrado: true` |
| Amplitud media global | Bs 91,2 millones |
| Cobertura por quintiles (N≈126–127 c/u) | Q1 83,46 % · Q2 93,65 % · Q3 91,27 % · Q4 87,30 % · Q5 85,71 % |
| Amplitud media por quintiles | Bs 16,5 M (Q1) → Bs 320,6 M (Q5) |
| Cobertura por sector y departamento | Publicada en `registry.json → metrics.segmentos_cobertura` con N visible |

Lectura honesta: la cobertura global cumple la tolerancia predefinida, pero **Q1 queda 1,5 puntos por debajo del límite inferior global** (83,46 % < 85 %): se publica tal cual, sin renombrar la calibración; la calibración es válida globalmente y su desempeño por segmento se muestra con N. La amplitud crece con el tamaño de empresa (intervalos absolutos más anchos en Q5), coherente con la heterocedasticidad residual.

Comprobación: `test_conformal_interval_meets_predefined_tolerance` verifica cobertura en tolerancia, coherencia con el registro y recálculo de la cobertura de la referencia nominal desde el CSV. La cobertura se recalcula desde `test_predictions.csv` (88,27 %) y coincide con el registro.

Conclusión: A06 cumplido. Decisión D02 cerrada y registrada; el consumidor del dashboard recibirá cobertura, amplitud y N por segmento.
