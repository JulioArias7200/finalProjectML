# Evidencia T01 · A01 · 2026-09-28

Revisor: Codex (revisión técnica de esta implementación). Entradas: los cuatro documentos originales en `docs/` y las fichas oficiales enlazadas en `07_fuentes_y_linea_base.md`. Método: inspección de contenido, corrección editorial y búsqueda de enlaces absolutos en los cuatro documentos originales.

Resultado esperado: conservar el contexto original con enlaces navegables, distinguir metas históricas de logros y evitar afirmaciones de cobertura, escala MedAPE o usos legales sin sustento.

Resultado observado: `docs/README.md` enlaza con rutas relativas, separa 10.044 del marco y 3.153 del extracto, y declara que MedAPE 36,20 % no cumple la meta 25 %. `01_analisis_dataset_EAIMCS.md` acota la afirmación de representatividad, elimina la regla de tratar importes altos como ausentes y remite a la política oficial para citar y verificar permisos. `02_diccionario_datos_EAIMCS.md` distingue 152+15 variables y unidades. `marco_logico_ingresos_operativos.md` mantiene las metas históricas y añade el estado observado.

Comprobación: búsqueda `rg -n 'file:///' docs/README.md docs/01_analisis_dataset_EAIMCS.md docs/02_diccionario_datos_EAIMCS.md docs/marco_logico_ingresos_operativos.md` sin coincidencias. Los enlaces relativos de `docs/` se comprobaron con `Test-Path`; los enlaces externos se contrastaron con el catálogo y la política de difusión del INE.

Conclusión: A01 cumplido para esta revisión. La política de acceso individual queda deliberadamente en D04/G3.
