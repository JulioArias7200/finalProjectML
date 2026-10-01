# Fuentes y línea base de la auditoría

Fecha: 2026-09-28. Los valores locales son observaciones del repositorio en esta fecha, no estadísticas oficiales extrapoladas. Recalcularlos al cambiar entradas o artefactos.

## Fuentes primarias

- [Catálogo INE de EAIMCS](https://anda.ine.gob.bo/index.php/catalog/252): diseño, marco y periodo de referencia de la encuesta.
- [Diccionario de datos de la sección F1](https://anda.ine.gob.bo/index.php/catalog/252/data-dictionary/F1): variables de encuesta, incluido `S00_01_A`.
- [Materiales metodológicos de EAIMCS](https://anda.ine.gob.bo/index.php/catalog/252/related-materials): reglas, clasificación y documentación complementaria; verificar descarga y versión antes de operacionalizar sentinelas y unidades.
- [Política de difusión del INE](https://anda.ine.gob.bo/index.php/politicas-difusion): confidencialidad y difusión; no inferir permisos para publicar registros individuales solo por disponibilidad del archivo.

## Observaciones locales por verificar automáticamente en G0–G2

| Hecho observado | Origen local | Lectura correcta |
|---|---|---|
| 3.153 filas generales, 167 columnas; 6.428 filas de materiales, 8 columnas | CSV crudos del repositorio | Tamaño del extracto disponible, no universo ni tasa de respuesta. |
| 152 campos de encuesta + 15 indicadores derivados | Cabecera CSV y diccionario | Separar fuente oficial de ingeniería local de variables. |
| 3.093 coincidencias exactas `S00_01_A`/`S05_04`; 60 con diferencia absoluta ≤Bs 1 | CSV general | Equivalencia práctica por redondeo, pendiente de regla formal de objetivo. |
| 13 macrosectores observados | Datos procesados | No rotular 14 sectores observados. |
| Modelo activo R² Bs ≈0,753 y MedAPE ≈36,20 % | `dashboard/artifacts/registry.json` | Estado de un paquete concreto; no satisface meta histórica MedAPE≤25 %. |
| Bitácora `models/bitacora_modelos.json` y registro `dashboard/artifacts/registry.json` corresponden a ejecuciones diferentes | JSON locales | No mezclar resultados en una comparación sin cohorte y versión explícitas. |

La documentación original aporta contexto, pero las afirmaciones sobre tasa de no respuesta, usos legales específicos, variables centinela y representatividad económica deben contrastarse contra los documentos oficiales pertinentes antes de integrarlas al producto.
