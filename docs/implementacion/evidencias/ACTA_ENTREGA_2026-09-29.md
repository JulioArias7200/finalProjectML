# Acta de entrega · Proyecto EAIMCS · 2026-09-29

## 1. Producto entregado

Dashboard integrado, reproducible y estadísticamente interpretable para el extracto local EAIMCS 2017: exploración con denominadores y supresión de celdas pequeñas, diagnóstico honesto de modelos, predicción con intervalo conformal calibrado y monitoreo real con ventana y N. Publicación agregada por defecto; detalle individual cerrado según D04.

## 2. Procedencia

| Elemento | Valor |
|---|---|
| Fuente | EAIMCS 2017 (INE), extracto local de 3.153 empresas (sin factor de expansión; no extrapolable a Bolivia) |
| `run_id` de preprocesamiento | PRE-20260928-d004f6ddd436 |
| Paquete de modelo | v1.20260929.0054 · `run_id` RUN-20260929-b3cfc0795ed7 |
| Integridad | `dashboard/artifacts/manifest.json`: 6/6 hashes SHA-256 verificados; el servidor rechaza mezclas entre ejecuciones (503) |
| Objetivo | `S00_01_A` (ingresos operativos anualizados, Bs, escala log1p), conciliado con `S05_04` por redondeo (D01) |
| Predictor excluido | Capacidades por unidades heterogéneas (D07) |

## 3. Métricas del paquete activo (recalculadas y verificadas)

| Métrica | Valor | Umbral | Estado |
|---|---|---|---|
| R² log (prueba, n=631) | 0.7824 | — | — |
| R² escala Bs | 0.7396 | — | — |
| MedAPE | 35.10 % | ≤ 40 % (D06) | ✅ Cumple |
| Cobertura conformal 90 % (D02) | 88.27 % | [85, 95] | ✅ Calibrado |
| Cobertura referencia nominal ±1,645×RMSE | 90.33 % | — | Solo rotulada como referencia |

**Meta aspiracional del marco lógico (MedAPE ≤ 25 %): NO alcanzada** (35.10 %). La brecha está registrada y el producto declara "prototipo validado bajo criterios operativos (D06)", no modelo para uso operativo de alto impacto.

## 4. Puertas y trazabilidad

| Puerta | Tareas | Estado | Cierre |
|---|---|---|---|
| G0 Documentación | T01–T02 | ✅ Aprobada | 2026-09-28 (Codex) |
| G1 Datos | T03–T05 | ✅ Aprobada | 2026-09-28 (Codebuff) |
| G2 Modelo | T06–T09 | ✅ Aprobada | 2026-09-28 (Codebuff) |
| G3 Servicio | T10–T12 | ✅ Aprobada | 2026-09-28 (Codebuff) |
| G4 Interfaz | T13–T16 | ✅ Aprobada | 2026-09-28 (Codebuff) |
| G5 Operación | T17–T19 | ✅ Aprobada | 2026-09-29 (Codebuff) |

Avance: **19/19 tareas completadas**. Pruebas: 32/32 automatizadas OK + verificación integral TODO OK + integración A10 en ambos sentidos (sin drift 5/5 estable; con drift 5/5 detectado).

## 5. Decisiones cerradas

D01 (objetivo y conciliación), D02 (intervalo conformal calibrado, cobertura 88.27 % ∈ [85, 95]), D03 (versionado /api/v1), D04 (detalle individual cerrado con 403), D05 (supresión de celdas N<5), D06 (meta MedAPE operativa 40 %; aspiracional 25 % no alcanzada), D07 (capacidades excluidas por unidades heterogéneas).

## 6. Criterios no alcanzados y limitaciones

1. **Meta aspiracional MedAPE ≤ 25 % no alcanzada** (35.10 %). Limitación de lectura: el modelo sirve para lectura descriptiva y exploratoria con incertidumbre calibrada, no para determinaciones individuales de fiscalización.
2. **Extracto sin factor de expansión**: todas las cifras corresponden a las 3.153 empresas del extracto; ninguna cifra es proyectable al universo nacional.
3. **Señales de riesgo descriptivas**: bunching y scores son exploratorios, no acusatorios; evaluación de falsos positivos pendiente por diseño (plan de pruebas).
4. **Drift real requiere ≥30 registros** en ventana; por debajo, "SIN TELEMETRÍA" o fallback simulado rotulado.
5. **Detalle individual cerrado (D04)** hasta existir control de acceso verificado.

## 7. Decisión de exposición de datos

- Toda vista pública es **agregada** con N y denominadores visibles; celdas N<5 suprimidas (D05).
- Ficha individual `/api/empresas_riesgo/<id>` devuelve **403** (D04) mientras no exista control de acceso verificado.
- Telemetría guarda insumos crudos sin identificadores empresariales.

## 8. Reproducibilidad

```bash
.python/python.exe preprocessing/preprocessing.py   # -> run_id PRE
.python/python.exe models/train.py                  # -> paquete con run_id RUN y manifest
.python/python.exe -m unittest discover -s tests    # 32/32 OK
.python/python.exe tests/integracion/verificacion_integral.py  # TODO OK
.python/python.exe dashboard/app.py                 # servidor en 127.0.0.1:5055
```

**Revisor y responsable de cierre:** Codebuff (revisión técnica, 2026-09-29). Evidencias por tarea en `docs/implementacion/evidencias/`; control de estados en `docs/implementacion/seguimiento.csv`.
