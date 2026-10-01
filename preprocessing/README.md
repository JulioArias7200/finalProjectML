# Preprocesamiento EAIMCS

El módulo [`preprocessing.py`](preprocessing.py) carga el extracto local, valida su estructura, agrega materiales por empresa y prepara variables para modelar el ingreso operativo `S00_01_A`. Las reglas de origen y límites de inferencia están en [docs](../docs/implementacion/02_contratos_y_arquitectura.md).

## Entradas y salidas

| Ruta | Contenido |
|---|---|
| `data/raw/MOD_ANUAL_S01-07_12_general_i.csv` | 3.153 empresas, 167 columnas en la línea base: 152 de encuesta y 15 derivados. |
| `data/raw/MOD_ANUAL_S10_materiales_i.csv` | 6.428 filas físicas, de las que una está completamente vacía; 6.427 registros utilizables, 8 columnas y varias filas por empresa. |
| `data/processed/dataset_procesado.csv` | Una fila por empresa con transformaciones `log1p` y agregados de materiales. |
| `preprocessing/bitacora_preprocesamiento.json` | Etapas y decisiones aplicadas. |
| `preprocessing/quality_report.json` | Conteos, conciliación de objetivo, faltantes, sectores y SHA-256 de las entradas. |

Ejecutar desde la raíz con un Python que tenga `requirements.txt` instalado:

```powershell
python preprocessing/preprocessing.py
python -m unittest discover -s tests -p test_data_contract.py
```

En este repositorio puede usarse `./.python/python.exe` si está instalado localmente; esa carpeta está excluida de Git.

## Reglas vigentes

- `ID` debe ser único y no nulo en el módulo general. Materiales puede tener varias filas por ID; se comprueba y reporta cuántas no enlazan con una empresa general. El `left join` valida cardinalidad uno a uno después de agregar.
- Las filas de materiales completamente vacías se cuentan y excluyen antes de validar IDs; una fila parcialmente informada con ID ausente sí detiene el proceso.
- `S00_01_A` es el objetivo. `S05_04` sirve para conciliación. Diferencias absolutas mayores a Bs 1 detienen el proceso; las diferencias menores se registran y no se corrigen automáticamente.
- Importes negativos de materiales pasan a ausente. El código 99999 se cuenta pero **no** se recodifica de forma general: puede ser un importe real sin una regla por campo. Un valor alto no es un ausente.
- `n_insumos=0` significa que no hay filas de materiales enlazadas. `total_valor_co` y `total_valor_uti` permanecen ausentes en ese caso; un cero explícito del origen sigue siendo cero.
- Se excluyen de los predictores las cantidades de capacidad `S12_01_B` y `S12_02_B` mientras no se interpreten con sus unidades `S12_01_C` y `S12_02_C`. No se agregan capacidades heterogéneas.
- Los valores ausentes en predictores permanecen ausentes. La imputación se ajusta solo con el conjunto de entrenamiento, dentro del pipeline del modelo. Las columnas relacionadas algebraicamente con ingresos y las 15 derivadas locales quedan excluidas o bajo auditoría de fuga; véase el [inventario](../docs/implementacion/inventario_columnas.csv).
- `log1p` se aplica a predictores no negativos y objetivo positivo. Una transformación logarítmica ayuda a manejar la asimetría, pero no garantiza homocedasticidad.

El mapeo de actividades puede definir más categorías de las que aparecen en un extracto. La línea base local contiene 13 macrosectores observados. Las salidas registran ese número en vez de declarar presentes todos los sectores teóricos.
