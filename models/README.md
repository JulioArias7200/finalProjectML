# Módulo de Modelado y MLOps (`models/`)

Este directorio contiene el pipeline de entrenamiento, evaluación comparativa, calibración estadística y monitoreo continuo de deriva de datos (*Data Drift*) para el proyecto **AprendizajeSupervisadoML**.

---

## 1. Estructura del Directorio `models/`

```text
models/
├── README.md                       -> Esta guía técnica de arquitectura y modelos
├── protocolo_entrenamiento.md      -> Protocolo G2 predefinido (partición, metas D06, conformal D02)
├── train.py                        -> Entrenamiento, CV, calibración conformal y exportación MLOps
├── drift.py                        -> Detector de Data Drift (KS y Wasserstein)
├── bitacora_modelos.json           -> Bitácora comparativa con run_id de la ejecución activa
└── reference_stats.json            -> Distribuciones empíricas base (percentiles y proporciones de ceros)
```

---

## 2. Flujo de Trabajo del Módulo

```text
data/processed/dataset_procesado.csv
                 │
                 ▼
┌────────────────────────────────────────────────────────┐
│ models/train.py                                        │
│ 1. Carga de predictores numéricos (log1p) y categoricos │
│ 2. Partición estratificada Train (80%) / Test (20%)    │
│ 3. Preprocesamiento: ColumnTransformer                 │
│    - StandardScaler -> 11 variables log1p              │
│    - OneHotEncoder  -> depto y sector_macro            │
│ 4. Evaluación 5-Fold Cross Validation (CV R²)          │
│ 5. Cálculo del Smearing Factor de Duan en escala Bs    │
│ 6. Selección de modelo campeón (Random Forest)        │
└───────────────┬────────────────────────────────────────┘
                │
                ├───────────────────────────────────────────────────────┐
                ▼                                                       ▼
  dashboard/artifacts/                                         models/reference_stats.json
  ├── best_model.joblib          (Pipeline serializado)        (Estadísticas empíricas de
  ├── registry.json              (Gobernanza MLOps)             entrenamiento para drift)
  ├── feature_importance.json    (Importancia de variables)             │
  └── test_predictions.csv       (Residuos y diagnósticos)              ▼
                                                               ┌───────────────────────────┐
                                                               │ models/drift.py           │
                                                               │ KS-test + Wasserstein     │
                                                               │ con ajuste de Bonferroni  │
                                                               └───────────────────────────┘
```

---

## 3. Metodología de Modelado y Calibración

### A. Variable Objetivo y Transformación
- **Target original:** `S00_01_A` (Ingreso Operativo Anual en Bolivianos, idéntico a `S05_04`).
- **Espacio de optimización:** Se modela $y_{\log} = \ln(1 + y)$.
- **Problema de re-transformación:** El operador exponencial simple $\exp(\hat{y}_{\log})$ subestima sistemáticamente la media esperada debido a la desigualdad de Jensen:
  $$\mathbb{E}[\exp(\varepsilon)] \ge \exp(\mathbb{E}[\varepsilon]) = 1$$
- **Solución implementada:** Se aplica el **Estimador de Smearing no paramétrico de Duan**:
  $$s = \frac{1}{n} \sum_{i=1}^n \exp(y_i - \hat{y}_i)$$
  $$\hat{y}_{\text{Bs}} = \max\left(0, \exp(\hat{y}_{\log}) \cdot s - 1\right)$$
  *(Factor de Duan para Random Forest: $s \approx 1.0401$)*.

### B. Predictores Utilizados
1. **9 Variables Numéricas:** `log_S01_05_A` (personal), `log_S01_03_C` (sueldos básicos), `log_S01_14` (otras remuneraciones), `log_S02_09` (energía y agua), `log_S07_09_E` (activos fijos), `log_S06_06_B` (inventarios finales), `log_n_insumos` (variedad de insumos), `log_total_valor_co` (compras de insumos), `log_total_valor_uti` (consumo productivo de insumos). Las cantidades de capacidad `S12_*_B` quedaron **excluidas** por decisión D07: sus unidades `S12_*_C` son heterogéneas y no admiten suma ni normalización defendible en este extracto.
2. **2 Variables Categóricas:** `depto` (9 departamentos observados) y `sector_macro` (13 macrosectores observados; no se declaran los 14 teóricos).
3. **Faltantes:** la imputación por mediana vive dentro del `Pipeline` y se ajusta solo con datos de entrenamiento; los faltantes de materiales preservados por T03 nunca se rellenan con cero antes del modelo.

---

## 4. Benchmark de Modelos Evaluados (iteración v1.20260928.2256, run_id RUN-20260928-b3cfc0795ed7)

Protocolo predefinido en [protocolo_entrenamiento.md](protocolo_entrenamiento.md): prueba final reservada (631 empresas), calibración separada (631), CV sobre el bloque de ajuste (1.891). Evaluación sobre el conjunto de prueba y validación cruzada de 5 particiones estratificadas:

| Algoritmo | CV $R^2$ (Log) | Test $R^2$ (Log) | Test $R^2$ (Escala Bs) | MedAPE | Smearing | Cobertura conformal | Estado |
|---|---|---|---|---|---|---|---|
| **Ridge Regression** | 0.5662 ± 0.054 | 0.5953 | 0.5750 | 67.41% | — | 84.47% | Base Lineal |
| **Random Forest Regressor** 🏆 | **0.7609 ± 0.027** | **0.7824** | **0.7396** | **35.10%** | 1.0404 | **88.27%** | **En Producción** |
| **HistGradientBoosting** | 0.7630 ± 0.030 | 0.7744 | 0.6286 | 39.37% | — | 90.65% | Alternativa Ensamble |

### Justificación del Modelo Seleccionado:
**Random Forest Regressor** fue seleccionado como el modelo campeón debido a:
- Mayor poder explicativo tanto en escala logarítmica ($R^2 = 0.7824$) como en escala monetaria real ($R^2 = 0.7396$).
- Menor sesgo de re-transformación (factor de Duan más cercano a 1.0).
- Mayor robustez ante relaciones no lineales entre factores productivos (capital y trabajo).
- Intervalo predictivo **conformal calibrado** (D02): q̂(log)=0,9025 sobre un conjunto de calibración separado; cobertura empírica 88,27% dentro de la tolerancia predefinida [85%, 95%], por lo que puede etiquetarse como intervalo calibrado al 90% nominal. La cobertura por quintiles varía de 83,5% (Q1) a 93,7% (Q2) y se publica por segmento; el método ±1,645×RMSE queda como referencia nominal no calibrada.
- Meta D06: MedAPE 35,10% ≤ umbral de aprobación 40% y R²(Bs) 0,7396 ≥ 0,70 → **umbral de aprobación cumplido**; la meta histórica ≤25% **no se alcanza** y se muestra siempre etiquetada como brecha.

---

## 5. Sistema de Detección de Data Drift (`models/drift.py`)

El módulo de monitoreo MLOps supervisa la estabilidad temporal de las distribuciones de entrada para alertar si los datos de nuevas empresas difieren significativamente de la base de entrenamiento de la EAIMCS:

1. **Pruebas Estadísticas Aplicadas:**
   - **Prueba de Kolmogorov-Smirnov de 2 Muestras (`ks_2samp`):** Evalúa si la muestra de inferencia proviene de la misma función de distribución acumulada (CDF) continua.
   - **Distancia de Wasserstein (`wasserstein_distance`):** Mide el costo de transporte óptimo (*Earth Mover's Distance*) entre distribuciones.
2. **Corrección por Multiplicidad de Pruebas (Bonferroni):**
   - Al evaluarse simultáneamente 5 variables productivas clave, se ajusta el umbral de significancia:
     $$\alpha_{\text{Bonferroni}} = \frac{\alpha_{\text{base}}}{k} = \frac{0.05}{5} = 0.01$$
3. **Variables Monitoreadas:**
   - Personal Ocupado (`S01_05_A`)
   - Sueldos y Salarios (`S01_03_C`)
   - Energía y Combustibles (`S02_09`)
   - Activos Fijos (`S07_09_E`)
   - Insumos Utilizados (`total_valor_uti`)

---

## 6. Ejecución y Comandos

### Entrenar los Modelos y Generar Artefactos:
```bash
python models/train.py
```

### Ejecutar Verificación del Detector de Drift:
```bash
python models/drift.py
```

---

## 7. Gobernanza y Trazabilidad MLOps

Cada ejecución de `models/train.py`:
1. Genera `run_id` (RUN-fecha-hash) derivado del modelo serializado y del `run_id` de preprocesamiento; el paquete completo comparte ese identificador.
2. Actualiza `dashboard/artifacts/registry.json` con versión activa, cohortes (ajuste/calibración/prueba), conformal y metas D06, archivando la versión anterior.
3. Escribe `dashboard/artifacts/manifest.json` con los SHA-256 de `best_model.joblib`, `test_predictions.csv`, `cv_results.json`, `feature_importance.json`, `registry.json` y `bitacora_modelos.json`; el servidor debe rechazar mezclas entre ejecuciones verificando `run_id` y hashes (A07).
4. Guarda `test_predictions.csv` con intervalo conformal (`lower_bs`/`upper_bs`), referencia nominal rotulada, sector, departamento y quintil por fila.
5. Exporta la importancia de variables y `models/bitacora_modelos.json` con el mismo `run_id`.

Pruebas: `python -m unittest discover -s tests -p "test_model_evaluation.py"` (8 casos A05–A07).
