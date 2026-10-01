# Evidencia T16 · revisión de ventanas MLOps · 2026-09-29

Revisor: Codex. Problema observado: la plantilla mostraba valores de ejemplo (`845`, `13.8 ms`, `v1.20260927`, `RandomForestRegressor`, `1.0401`) mientras algunas métricas se cargaban por API. Si una petición fallaba o tardaba, esos valores podían interpretarse como información vigente.

Corrección aplicada:

- `dashboard/templates/index.html` inicia las métricas dinámicas en `Cargando...` o `—`, sin cifras heredadas.
- `dashboard/app.py:/api/mlops` expone `model_type`, `smearing_factor`, `rmse_log` y `conformal` del paquete activo.
- `dashboard/static/js/app.js` actualiza tipo de modelo, smearing y fecha desde esa respuesta.
- Se añadió `test_mlops_window_metadata_matches_active_package` al contrato de API.

Verificación en el servidor actualizado (puerto de prueba 5056): `run_id=RUN-20260929-b3cfc0795ed7`, versión `v1.20260929.0054`, modelo `RandomForest`, smearing `1.0403537`, cobertura conformal `88.27%`. Suite completa: 33/33 pruebas OK. Las cadenas de ejemplo anteriores ya no aparecen en plantilla ni JavaScript.

Nota operativa: el puerto 5055 tenía procesos Flask antiguos escuchando simultáneamente; para validar la versión actual se utilizó el puerto 5056. Reiniciar los procesos anteriores y levantar una sola instancia en 5055 antes de presentar el dashboard.
