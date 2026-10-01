# Evidencia T11 · D04/A08 · 2026-09-28

Revisor: Codebuff (revisión técnica de esta implementación). Entradas: `dashboard/app.py` (constante `ACCESO_INDIVIDUAL_HABILITADO`, endpoints `/api/empresas_riesgo*`), `docs/implementacion/02_contratos_y_arquitectura.md`, `docs/implementacion/06_decisiones_y_riesgos.md`.

Resultado esperado: política de acceso aplicada y señales agregadas presentadas sin lenguaje acusatorio.

## Política de acceso (D04) aplicada

1. La entrega pública queda **agregada por defecto**: `ACCESO_INDIVIDUAL_HABILITADO = False`.
2. `GET /api/empresas_riesgo/<id>` responde **403** con cuerpo que referencia explícitamente la decisión D04 (`decision: "D04"`) mientras no exista control de acceso verificado. Comprobado por `test_individual_access_gated_by_d04`.
3. El listado `/api/empresas_riesgo` incluye el bloque `acceso_individual` rotulando la política; la paginación se valida (400 ante `limit` no entero o fuera de 1–200) y su respuesta lleva `meta`.
4. El listado sigue entregando los campos agregados de contexto por empresa (sector, posición relativa) pero sin habilitar el detalle ampliado mientras D04 esté cerrada; el mecanismo queda listo para habilitarse solo con el control de acceso de la decisión.

## Señales descriptivas, no acusaciones

- `/api/bunching_alerta` añade `caracter_descriptivo`: señal agregada sectorial; "no constituye evidencia de incumplimiento ni acusación contra empresa alguna". Verificado por `test_bunching_is_labeled_descriptive`.
- `/api/predict` responde con `limitacion_uso`: "no constituye evaluación tributaria ni declaración individual".
- El score de riesgo se presenta como ordenamiento descriptivo de discrepancia frente a la estructura productiva, con el score derivado del modelo activo (`run_id` en `meta`), no como veredicto.

Comprobación: suite `tests/test_api_contract.py` 12/12 OK.

Conclusión: política de acceso y rotulación de señales aplicadas; componente D04 de A08 cumplido.
