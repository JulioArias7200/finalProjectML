# Módulo del Dashboard Web (`dashboard/`)

Este directorio contiene el servidor web, la API REST, la interfaz SPA interactiva (*Single Page Application*), los estilos visuales y los artefactos serializados de Machine Learning para el proyecto **AprendizajeSupervisadoML**.

---

## 1. Estructura del Directorio `dashboard/`

```text
dashboard/
├── README.md                 -> Esta guía de arquitectura y uso del dashboard
├── requirements.txt          -> Dependencias específicas del entorno web
├── app.py                    -> Servidor web Flask y catálogo de rutas API REST
├── data_loader.py            -> Cargador Singleton de datos preprocesados y agregaciones
├── run_server.py             -> Script de inicialización directa en el puerto 5055
├── artifacts/                -> Artefactos de ML consumidos por el dashboard (desde models/)
│   ├── manifest.json         -> Raíz de integridad: run_id + SHA-256 de cada artefacto (A07)
│   ├── best_model.joblib     -> Pipeline de regresión entrenado (Random Forest Regressor)
│   ├── registry.json         -> Trazabilidad MLOps, cohortes, conformal y metas D06
│   ├── cv_results.json       -> Resultados por pliegue de la validación cruzada
│   ├── feature_importance.json -> Importancia relativa de predictores para Plotly.js
│   └── test_predictions.csv  -> Predicciones de prueba con intervalo conformal y subgrupos
├── static/                   -> Recursos estáticos del frontend
│   ├── css/
│   │   └── styles.css        -> Sistema de diseño corporativo, soporte dark/light y tipografía Inter
│   └── js/
│       └── app.js            -> Lógica cliente, navegación SPA, llamadas asíncronas y gráficos Plotly.js
└── templates/                -> Plantillas del motor Jinja2
    └── index.html            -> Cascarón HTML5 interactivo con las 8 secciones analíticas
```

---

## 2. Las 8 Secciones del Dashboard Interactivo

El dashboard está concebido para perfiles tanto ejecutivos como técnicos y de auditoría:

1. **Resumen Ejecutivo & KPIs:** Métricas macroeconómicas consolidadas de las 3,153 empresas encuestadas (ingresos medios/medianos, dispersión por departamentos, volumen muestral).
2. **Diccionario de Datos Interactivo:** Buscador en tiempo real de variables oficiales con desglose por secciones, tipos de datos y reglas de consistencia contable del INE.
3. **Análisis Exploratorio (EDA):** Gráficos dinámicos con Plotly.js:
   - Distribución de ingresos (escala natural asimétrica vs. normalizada $\log(1+x)$).
   - Boxplots por los 9 departamentos de Bolivia.
   - Boxplots por los 13 macrosectores económicos observados en el extracto.
   - Mapa de calor de correlaciones lineales de Spearman/Pearson.
   - Gráfico de dispersión de inconsistencias y detección de centinelas 99999.
4. **Pipeline de Preprocesamiento:** Trazabilidad paso a paso del flujo de ingeniería de datos y políticas de prevención de fuga de información (*anti-leakage*).
5. **Diagnóstico de Modelos:** Comparativa de desempeño (Ridge vs. Random Forest vs. HistGradientBoosting), diagrama de dispersión de *Valores Reales vs. Predichos*, distribución de residuos y ranking de importancia de variables.
6. **Simulador Predictivo Interactivo:** Formulario de inferencia operativa en tiempo real con estimación en Bolivianos (Bs), cálculo de intervalos de predicción al 90% y clasificación de tamaño empresarial (Mediana vs. Gran empresa según umbrales de producción/servicios).
7. **MLOps, Versiones y Data Drift:** Auditoría de versiones registradas en `registry.json` y medición de deriva con la telemetría real de `/api/predict` (ventana y N visibles); sin tráfico suficiente, modo simulado rotulado o "SIN TELEMETRÍA".
8. **Marco Lógico y Metodología:** Justificación técnica, matriz de marco lógico, árbol de objetivos y limitaciones metodológicas de la EAIMCS.

---

## 3. Catálogo de Endpoints de la API REST

### Contrato transversal (docs/implementacion/02_contratos_y_arquitectura.md)

- Toda respuesta analítica incluye `meta: {run_id, dataset_id, periodo, poblacion, n, filtros, unidad, escala, generated_at, limitaciones}`.
- Filtro o entrada inválida → **400** con `error` y `detalle` comprensibles. Paquete de artefactos ausente o inconsistente (hash/run_id) → **503** `paquete_no_disponible`: el servidor nunca mezcla ejecuciones.
- Celdas o grupos sin observaciones se serializan como JSON `null`; `0` significa cero observado. Las celdas con N<5 llegan suprimidas según la decisión D05.
- El detalle individual de empresas permanece cerrado (**403**) según la decisión D04 mientras no exista control de acceso verificado; la entrega pública es agregada por defecto.

| Método | Endpoint | Descripción |
|---|---|---|
| `GET` | `/` | Renderiza la interfaz gráfica SPA Jinja2. |
| `GET` | `/api/kpis` | KPIs con denominador compartido; acepta `?depto=` y `?sector=` validados. |
| `GET` | `/api/dictionary` | Diccionario interactivo filtrable por texto (`?q=`) y sección (`?section=`). |
| `GET` | `/api/eda/distribution` | Histogramas de distribución natural y logarítmica para Plotly. |
| `GET` | `/api/eda/boxplot_deptos` | Cuartiles por departamento con supresión D05 de N<5. |
| `GET` | `/api/eda/boxplot_sectors` | Cuartiles por macrosector con supresión D05 de N<5. |
| `GET` | `/api/eda/correlations` | Matriz de correlación en escala log1p con conteos por par. |
| `GET` | `/api/eda/outliers` | Dispersión descriptiva ingreso vs sueldos/personal. |
| `GET` | `/api/eda/heatmap_depto_sector` | Matriz depto×sector con celdas `null`/`suppressed` y denominador. |
| `GET` | `/api/pipeline` | Fases del pipeline de preprocesamiento vigentes (reglas T03). |
| `GET` | `/api/bitacora_preprocesamiento` | Bitácora auditable del preprocesamiento con `run_id`. |
| `GET` | `/api/bitacora_modelos` | Bitácora comparativa de modelos de la ejecución activa. |
| `GET` | `/api/models` | Métricas globales y por subgrupo, conformal, metas D06, importancia y diagnósticos. |
| `GET` | `/api/cross_validation` | Resultados por pliegue de la validación cruzada con `run_id`. |
| `POST` | `/api/predict` | Inferencia validada en Bs con intervalo **conformal calibrado** (D02) y limitación de uso. |
| `GET` | `/api/empresas_riesgo` | Listado agregado ordenado por score de riesgo con paginación validada y política D04. |
| `GET` | `/api/empresas_riesgo/<id>` | Ficha individual — **403** mientras D04 no se resuelva con control de acceso. |
| `GET` | `/api/bunching_alerta` | Señal agregada y descriptiva de densidad sectorial, rotulada sin carácter acusatorio. |
| `GET` | `/api/mlops` | Versiones, cohortes y deriva; usa telemetría real si hay ≥30 registros (`__modo__: real`), con fallback simulado rotulado. |
| `GET` | `/api/mlops/monitoring` | Telemetría real de `/api/predict`; sin tráfico muestra "SIN TELEMETRÍA". |
| `POST` | `/api/mlops/drift` | Prueba de deriva por variable; respuesta rotulada `__modo__`. |
| `GET` | `/api/about` | Metadatos de la encuesta EAIMCS, marco lógico y limitaciones de muestreo. |

---

## 4. Instrucciones de Ejecución

### Opción A: Desde la raíz del proyecto (Recomendado)
```bash
python dashboard/app.py
```
O bien mediante el script lanzador con configuración de puerto:
```bash
python dashboard/run_server.py
```

### Opción B: Desde dentro de la carpeta `dashboard/`
```bash
cd dashboard
python app.py
```

Una vez iniciado, abre tu navegador en:
👉 **`http://127.0.0.1:5055`**

> Nota: este repositorio incluye un runtime embebido en `.python/` (Python 3.13 con dependencias ya instaladas). Con él, los comandos anteriores se ejecutan como `.python/python.exe dashboard/app.py` desde la raíz; no se requiere entorno virtual.

### Pruebas y verificación (T18)

```bash
# Suite automatizada (32 pruebas, sin servidor):
.python/python.exe -m unittest discover -s tests

# Verificación integral del paquete activo (sin servidor):
.python/python.exe tests/integracion/verificacion_integral.py

# Integración A10 con tráfico controlado (requieren el servidor activo en 127.0.0.1:5055):
.python/python.exe tests/integracion/prueba_a10_sin_drift.py
.python/python.exe tests/integracion/prueba_a10_drift_detectado.py
```

Para regenerar el paquete completo desde la fuente: `preprocessing/preprocessing.py` y luego `models/train.py` (el servidor valida `run_id` y hashes al arrancar; nunca sirve ejecuciones mezcladas).

---

## 5. Dependencias y Requisitos

Las dependencias pueden instalarse desde la raíz (`pip install -r requirements.txt`) o específicamente para el dashboard:
```bash
pip install -r dashboard/requirements.txt
```

---

## 6. Documentación Relacionada

- [models/README.md](../models/README.md): Entrenamiento, calibración y generación de los artefactos en `artifacts/`.
- [preprocessing/README.md](../preprocessing/README.md): Pipeline de transformación que alimenta el archivo de datos consumido por `data_loader.py`.
- [docs/02_diccionario_datos_EAIMCS.md](../docs/02_diccionario_datos_EAIMCS.md): Definición detallada de cada variable expuesta en `/api/dictionary`.
- [Plan de implementación](../docs/implementacion/README.md): contrato de API, matriz de aceptación y estado de puertas.
