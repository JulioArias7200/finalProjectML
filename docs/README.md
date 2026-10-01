# Documentación Técnica y Metodológica (`docs/`)

> **Estado de revisión (2026-09-28):** los cuatro documentos de esta carpeta se conservan como contexto y registro de objetivos originales. Antes de usarlos como especificación vigente, consultar la [auditoría de vigencia](implementacion/00_auditoria_docs.md) y el [plan de implementación y seguimiento](implementacion/README.md). Las correcciones de enlaces, definiciones y cifras heredadas están registradas como tareas pendientes.

Este directorio contiene los fundamentos teóricos, metodológicos, estadísticos y de marco lógico del proyecto **AprendizajeSupervisadoML**, basados en los microdatos oficiales de la **EAIMCS 2017-2018** del Instituto Nacional de Estadística (INE) de Bolivia.

---

## 1. Estructura del Directorio `docs/`

```text
docs/
├── README.md                              -> Esta guía e índice central de documentación
├── 01_analisis_dataset_EAIMCS.md          -> Cobertura, marco muestral, tasas de respuesta y sesgos
├── 02_diccionario_datos_EAIMCS.md         -> Catálogo oficial de variables y reglas contables
└── marco_logico_ingresos_operativos.md    -> Matriz de marco lógico, árbol de objetivos e indicadores CCT
```

---

## 2. Índice de Documentos Metodológicos

### 1. [01_analisis_dataset_EAIMCS.md](01_analisis_dataset_EAIMCS.md)
- **Tema:** Análisis contextual y muestral de la encuesta.
- **Contenido Clave:**
  - Identificación del estudio en el catálogo ANDA (`BOL-INE-EAIMCS-2017-2018`).
  - Cobertura geográfica nacional (9 departamentos) y delimitación al estrato de empresas medianas y grandes.
  - Diseño muestral: muestra dirigida sobre un directorio de 10,044 empresas registradas en FUNDEMPRESA y Cuentas Nacionales.
  - Umbrales de estratificación por tamaño (Bs 2.45M – 35M para medianas de producción, > 35M para grandes).
  - Marco de 10.044 empresas y limitaciones de cobertura; las 3.153 filas del extracto local no permiten calcular por sí solas una tasa de respuesta.

### 2. [02_diccionario_datos_EAIMCS.md](02_diccionario_datos_EAIMCS.md)
- **Tema:** Catálogo estructurado de variables y especificación contable.
- **Contenido Clave:**
  - Mapeo columna por columna de los módulos general (`MOD_ANUAL_S01-07_12_general_i`) y de materiales (`MOD_ANUAL_S10_materiales_i`).
  - Identificación de `S00_01_A` como objetivo del proyecto y conciliación con `S05_04` (60 diferencias de redondeo de hasta Bs 1).
  - Definición de factores productivos: personal (`S01_05_A`), masa salarial (`S01_03_C`), energía (`S02_09`), activos fijos (`S07_09_E`), inventarios (`S06_06_B`) y almacenamiento (`S12_01_B`, `S12_02_B`).
  - Variables y unidades declaradas; cualquier regla de centinelas debe verificarse por campo antes de aplicarse.
  - El inventario de predictores permitidos y excluidos se controla en el protocolo de modelado del plan de implementación.

### 3. [marco_logico_ingresos_operativos.md](marco_logico_ingresos_operativos.md)
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
