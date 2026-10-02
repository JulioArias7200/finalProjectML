# Documentación Técnica y Metodológica (`docs/`)

> **Estado de revisión (2026-09-28):** los cuatro documentos de esta carpeta se conservan como contexto y registro de objetivos originales. Antes de usarlos como especificación vigente, consultar la [auditoría de vigencia](implementacion/00_auditoria_docs.md) y el [plan de implementación y seguimiento](implementacion/README.md). Las correcciones de enlaces, definiciones y cifras heredadas están registradas como tareas pendientes.

Este directorio contiene los fundamentos teóricos, metodológicos, estadísticos y de marco lógico del proyecto **AprendizajeSupervisadoML**, basados en los microdatos oficiales de la **EAIMCS 2017-2018** del Instituto Nacional de Estadística (INE) de Bolivia.

---

## 1. Estructura del Directorio `docs/`

```text
docs/
├── README.md                              -> Esta guía e índice central de documentación
├── 01_analisis_dataset_EAIMCS.md          -> Cobertura, marco muestral, tasas de respuesta y sesgos
├── 02_diccionario_datos_EAIMCS.md         -> Catálogo oficial de variables y reglas contables (datos crudos)
├── 03_preprocesamiento.md                 -> Pipeline de transformación, anti-leakage y agregación relacional
├── 04_diccionario_datos_Preprocesado.md   -> Diccionario detallado de las 184 columnas del dataset final
├── 05_aplicacion_en_modelos.md            -> Benchmark experimental, modelo campeón y selección para dashboard
└── marco_logico_ingresos_operativos.md    -> Matriz de marco lógico, árbol de objetivos e indicadores CCT
```

---

## 2. Índice de Documentos Metodológicos

### 1. [01_analisis_dataset_EAIMCS.md](01_analisis_dataset_EAIMCS.md)
- **Tema:** Análisis contextual y muestral de la encuesta.
- **Contenido Clave:**
  - Identificación del estudio en el catálogo ANDA (`BOL-INE-EAIMCS-2017-2018`).
  - Cobertura geográfica nacional (9 departamentos) y delimitación al estrato de empresas medianas y grandes.
  - Diseño muestral: muestra dirigida sobre un directorio de 10.044 empresas registradas en FUNDEMPRESA y Cuentas Nacionales.
  - Umbrales de estratificación por tamaño (Bs 2.45M – 35M para medianas de producción, > 35M para grandes).
  - Marco de 10.044 empresas y limitaciones de cobertura; las 3.153 filas del extracto local no permiten calcular por sí solas una tasa de respuesta.

### 2. [02_diccionario_datos_EAIMCS.md](02_diccionario_datos_EAIMCS.md)
- **Tema:** Catálogo estructurado de variables y especificación contable (Datos Crudos).
- **Contenido Clave:**
  - Mapeo columna por columna de los módulos general (`MOD_ANUAL_S01-07_12_general_i`) y de materiales (`MOD_ANUAL_S10_materiales_i`).
  - Identificación de `S00_01_A` como objetivo del proyecto y conciliación con `S05_04` (60 diferencias de redondeo de hasta Bs 1).
  - Definición de factores productivos: personal (`S01_05_A`), masa salarial (`S01_03_C`), energía (`S02_09`), activos fijos (`S07_09_E`), inventarios (`S06_06_B`) y almacenamiento (`S12_01_B`, `S12_02_B`).
  - Variables y unidades declaradas; cualquier regla de centinelas debe verificarse por campo antes de aplicarse.
  - El inventario de predictores permitidos y excluidos se controla en el protocolo de modelado del plan de implementación.

### 3. [03_preprocesamiento.md](03_preprocesamiento.md)
- **Tema:** Pipeline de ingeniería de datos y preprocesamiento reproducible.
- **Contenido Clave:**
  - Justificación y principios rectores del pipeline automatizado [`preprocessing/preprocessing.py`](../preprocessing/preprocessing.py).
  - Cadena de transformación y hashes criptográficos SHA-256 de las fuentes crudas.
  - Desglose de las 5 etapas: 1) Validación monetaria y tipos, 2) Agregación relacional de Sección 10 a nivel empresa, 3) Cruce 1:1, banderas y normalización geográfica y sectorial (13 macrosectores CAEB), 4) Políticas anti-fuga (exclusión de 19 variables y capacidad S12) y conciliación de target, 5) Transformación log1p y estrategia de imputación estadística desacoplada (diferida al pipeline de ML).
  - Protocolo de pruebas unitarias de contrato de datos ([`tests/test_data_contract.py`](../tests/test_data_contract.py)).

### 4. [04_diccionario_datos_Preprocesado.md](04_diccionario_datos_Preprocesado.md)
- **Tema:** Diccionario exhaustivo del dataset preprocesado final (`dataset_procesado.csv`).
- **Contenido Clave:**
  - Ficha técnica: 3.153 observaciones × 184 columnas, nivel empresa.
  - Taxonomía funcional de las 184 columnas en 7 módulos.
  - Definición detallada de la variable objetivo (`target` y `target_log`) con estadísticas de distribución.
  - Catálogo de los 9 predictores numéricos fundamentales en escala original y `log1p`, con manejo de ausentes.
  - Distribución de frecuencias para `depto` (9 departamentos) y `sector_macro` (13 categorías observadas).
  - Detalle y justificación econométrica de las 19 variables excluidas por riesgo de fuga de datos (*data leakage*).
  - Catálogo de 147 variables de encuesta conservadas para auditoría contable y dashboards interactivos.
  - Guía de código para científicos de datos y factor de calibración de Duan Smearing.

### 5. [05_aplicacion_en_modelos.md](05_aplicacion_en_modelos.md)
- **Tema:** Benchmark experimental, modelo campeón e integración en el dashboard.
- **Contenido Clave:**
  - Protocolo experimental de validación: 5-Fold Stratified CV, partición 80/20 y conjunto de calibración separado.
  - Benchmark de los 7 modelos evaluados: LinearRegression, Ridge, ElasticNet, TweedieRegressor, HistGradientBoosting, XGBoost y RandomForest.
  - Ratificación del ganador: `RandomForestRegressor` ($R^2_{\text{Bs}} = 0.7396$, $\text{MedAPE} = 34.01\%$, factor de Duan $s = 1.0404$ y cobertura conformal del 88.27%).
  - Importancia de variables de Gini (liderada por masa salarial con 38.03% y remuneraciones con 17.69%).
  - Justificación de los 3 modelos seleccionados para el dashboard (Ridge como línea base lineal interpretable, HGB como boosting ultraligero y Random Forest como modelo campeón en producción).
  - Razones técnicas y arquitectónicas del descarte de MCO, ElasticNet, Tweedie y XGBoost.

### 6. [marco_logico_ingresos_operativos.md](marco_logico_ingresos_operativos.md)
- **Tema:** Formulación del proyecto mediante la Metodología de Marco Lógico (MML).
- **Contenido Clave:**
  - **Árbol de Problemas:** Causa raíz de la falta de herramientas cuantitativas para detectar inconsistencias y subdeclaración en auditorías económicas.
  - **Árbol de Objetivos:** Medios y fines para disponer de un estimador objetivo del ingreso empresarial basado en insumos productivos.
  - **Matriz de Marco Lógico (MML):**
    - *Fin:* Fortalecer la integridad de las estadísticas económicas y la equidad tributaria.
    - *Propósito:* Desarrollar un sistema de Machine Learning con metas históricas $R^2 \ge 0.70$ y MedAPE $\le 25\%$ calculado sobre montos en Bs. El modelo activo registra MedAPE 36,20 %, por lo que esa meta sigue pendiente.
    - *Componentes:* 1) Dataset integrado y depurado, 2) Análisis exploratorio interactivo, 3) Modelos supervisados validados, 4) API REST de inferencia, 5) Dashboard web MLOps.
    - *Actividades:* Cronograma y recursos requeridos.

---

## 3. Relación con la Arquitectura de Software

Los documentos aportan contexto y definiciones para:
- La lógica de limpieza en [`preprocessing/preprocessing.py`](../preprocessing/preprocessing.py).
- La validación del modelo en [`models/train.py`](../models/train.py).
- Las secciones informativas y el endpoint `/api/about` en [`dashboard/app.py`](../dashboard/app.py).

El [plan de implementación](implementacion/README.md) contiene los criterios vigentes de aceptación y seguimiento.
