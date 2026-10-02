# Cuadernos de Exploración, Conversión y Benchmark (`notebooks/`)

Este directorio contiene cuadernos interactivos Jupyter Notebook utilizados para la extracción inicial de microdatos, pruebas de concepto y la evaluación experimental rigurosa de algoritmos de Machine Learning del proyecto **AprendizajeSupervisadoML** (EAIMCS - INE Bolivia).

---

## 1. Estructura del Directorio `notebooks/`

```text
notebooks/
├── README.md                            -> Guía y documentación de los cuadernos de trabajo
├── convertir.ipynb                      -> Conversión automatizada de microdatos SPSS (.sav) a CSV (.csv)
├── 01_preprocesamiento_y_muestreo.ipynb -> Pipeline interactivo de ingestión, limpieza, ingeniería y muestreo
└── comparacion_modelos.ipynb           -> Benchmark experimental, 5-Fold CV y evaluación de 7 modelos de regresión
```

---

## 2. Descripción de Cuadernos

### 1. `convertir.ipynb`
* **Propósito:** Automatizar la extracción y exportación de microdatos oficiales del INE en formato IBM SPSS Statistics (`.sav`) hacia formato texto delimitado por comas (`.csv`, codificación UTF-8), garantizando su lectura eficiente y liviana dentro de los pipelines de Python.
* **Librerías utilizadas:** `pandas`, `pyreadstat`, `os`.
* **Archivos procesados:**
  * `MOD_ANUAL_S01-07_12_general_i.sav` $\rightarrow$ `MOD_ANUAL_S01-07_12_general_i.csv`
  * `MOD_ANUAL_S10_materiales_i.sav` $\rightarrow$ `MOD_ANUAL_S10_materiales_i.csv`
* **Estado:** Los archivos ya se encuentran generados en `data/raw/`, por lo que su reejecución es opcional.

---

### 2. `01_preprocesamiento_y_muestreo.ipynb`
* **Propósito:** Demostrar de forma didáctica, visual y reproducible el flujo completo de ingeniería de datos desde los microdatos crudos hasta los conjuntos de modelado:
  1. *Ingestión y auditoría de integridad* ($N = 3,153$ empresas y $6,428$ registros de insumos).
  2. *Limpieza de centinelas e inconsistencias* (tratamiento de negativos y validación del código `99999`).
  3. *Agregación relacional N-a-1* (cálculo de variedad `n_insumos`, compras `total_valor_co` y consumo `total_valor_uti`).
  4. *Fusión 1-a-1 y normalización categórica* (departamentos y mapeo CAEB a macrosectores con gráficos de barras).
  5. *Conciliación del target y prevención de fuga de datos* (conciliación `S00_01_A` vs `S05_04` con `Decimal` y exclusión de 19 variables *leakage*).
  6. *Estabilización de varianza* (transformación `log1p` con histogramas comparativos).
  7. *Muestreo estratificado en 3 cohortes* (Entrenamiento 60%, Calibración Conformal 20%, Prueba Ciega 20% mediante deciles del target).
  8. *Aserciones de contrato y exportación* hacia `data/processed/dataset_procesado.csv`.
* **Librerías utilizadas:** `pandas`, `numpy`, `matplotlib`, `seaborn`, `decimal`, `sklearn`.

---

### 3. `comparacion_modelos.ipynb`
* **Propósito:** Benchmark experimental y reproducible que compara el desempeño de **7 algoritmos de regresión supervisada** sobre el dataset oficial procesado ($N = 3,153$ empresas) bajo validación cruzada estratificada de 5 pliegues (*5-Fold Stratified CV* por quintiles de ingreso):
  1. `LinearRegression` (Línea base OLS sin regularización)
  2. `Ridge` (Regularización $L_2$)
  3. `ElasticNet` (Regularización combinada $L_1 + L_2$)
  4. `RandomForestRegressor` (**Modelo Campeón Serializado**)
  5. `HistGradientBoostingRegressor` (Boosting con discretización por histogramas)
  6. `XGBRegressor` (XGBoost optimizado)
  7. `TweedieRegressor` (GLM Compound Poisson-Gamma con enlace logarítmico)
* **Métricas calculadas:** $R^2$, $RMSE$, $MAE$ y $MedAPE (\%)$ tanto en escala logarítmica como monetaria (Bs) con corrección de sesgo de Duan Smearing y cálculo de cobertura empírica al 90%.
* **Salidas:** Generación de gráficos comparativos con barras de error ($\pm 1\sigma$) y exportación auditable hacia `models/bitacora_modelos.json`.

---

## 3. Instrucciones de Ejecución

1. **Activar el entorno virtual del proyecto:**
   ```bash
   # En Windows:
   .\venv\Scripts\activate
   # En Linux / macOS:
   source venv/bin/activate
   ```

2. **Iniciar Jupyter Notebook o JupyterLab:**
   ```bash
   jupyter notebook
   # o bien:
   jupyter lab
   ```

3. **Ejecutar los cuadernos:**
   * Para explorar los modelos y replicar el benchmark: abrir y ejecutar `notebooks/comparacion_modelos.ipynb`.
   * El cuaderno carga automáticamente `data/processed/dataset_procesado.csv` y utiliza las semillas y constantes oficiales del proyecto (`RANDOM_STATE_SEED = 42`).
