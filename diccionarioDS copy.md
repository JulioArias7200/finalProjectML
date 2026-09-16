# Diccionario de datasets EDSA 2023

Este documento organiza cada base por seccion. En las tablas, **Columna** es el nombre que aparece en el CSV y **Significado** explica que representa.

## Indice

1. [EDSA2023_Mujer](#edsa2023-mujer) - 14545 casos, 1341 variables
2. [EDSA2023_Vivienda](#edsa2023-vivienda) - 19059 casos, 73 variables
3. [EDSA2023_Hogar](#edsa2023-hogar) - 54008 casos, 235 variables
4. [EDSA2023_HistorialHijos](#edsa2023-historialhijos) - 22360 casos, 26 variables
5. [EDSA2023_Hombre](#edsa2023-hombre) - 5878 casos, 997 variables

---

## EDSA2023_Mujer

**Casos:** 14545  
**Variables:** 1341

**Descripcion:** El Cuestionario Mujer consta de 10 secciones, que son: - Sección I. Antecedentes de la entrevistada - Sección II. Reproducción (parcial) - Sección III. Anticoncepción/Planificación familiar - Sección V. Alimentación y cobertura de salud - Sección VI. Nupcialidad y actividad sexual - Sección VII. Preferencias de fecundidad - Sección VIII. Antecedentes del esposo/compañero y empleo de la entrevistada - Sección IX. VIH/SIDA e Infecciones de transmisión sexual - Sección X. Otros asuntos relacionados con la salud - Sección XI. Violencia a las mujeres

### Columnas y significados

| Columna | Significado |
|---|---|
| `folio` | Folio |
| `nro` | Número de orden de la persona |
| `upm` | Unidad Primaria de Muestreo |
| `estrato` | Estrato |
| `ms01_0101_1a` | Fecha de entrevista - Día |
| `ms01_0101_1b` | Fecha de entrevista - Mes |
| `ms01_0101_1c` | Fecha de entrevista - Año |
| `ms01_0101_a` | Hora de inicio de la entrevista (Hora) |
| `ms01_0101_b` | Hora de inicio de la entrevista (Minutos) |
| `ms01_0101a` | ¿Cuántos años cumplidos tiene usted? |
| `ms01_0101b_1` | ¿Cuál es la fecha de su nacimiento? (DIA) |
| `ms01_0101b_2` | ¿Cuál es la fecha de su nacimiento? (MES) |
| `ms01_0101b_3` | ¿Cuál es la fecha de su nacimiento? (AÑO) |
| `ms01_0102` | ¿Dónde nació? |
| `ms01_0102_01_cod` | (ESPECIFIQUE) ¿En que lugar nació?(DEPARTAMENTO - MUNICIPIO - CIUDAD O COMUNIDAD) |
| `ms01_0102_02_cod` | (ESPECIFIQUE) EN EL EXTERIOR |
| `ms01_0103` | ¿Dónde vive habitualmente?SI LA RESPUESTA ES EN OTRO LUGAR DEL PAIS O EN EL EXTERIOR INDAGUE:¿En qué lugar vive habitualmente? |
| `ms01_0103_01_cod` | (ESPECIFIQUE) ¿Dónde vive habitualmente? (DEPARTAMENTO - MUNICIPIO - CIUDAD O COMUNIDAD) |
| `ms01_0103_02_cod` | (ESPECIFIQUE) EN EL EXTERIOR |
| `ms01_0104` | ¿Dónde vivía hace 5 años?SI LA RESPUESTA ES "EN OTRO LUGAR DEL PAIS" O "EN EL EXTERIOR" INDAGUE:¿En qué lugar vivía? |
| `ms01_0104_01_cod` | (ESPECIFIQUE) ¿En cuál lugar vivía? (DEPARTAMENTO - MUNICIPIO - CIUDAD O COMUNIDAD) |
| `ms01_0104_02_cod` | (ESPECIFIQUE) EN EL EXTERIOR |
| `ms01_0105` | ¿Cuál fue la razón principal por la que se trasladó a otro lugar? |
| `ms01_0105_cod` | (ESPECIFIQUE) OTRA |
| `ms01_0106` | ¿Cuál es el idioma o lengua en el que aprendió a hablar en su niñez ? |
| `ms01_0106_cod` | (ESPECIFIQUE) OTRO NATIVO |
| `ms01_0107_A` | ¿Qué idiomas habla actualmente? (QUECHUA) |
| `ms01_0107_B` | ¿Qué idiomas habla actualmente? (AYMARA) |
| `ms01_0107_C` | ¿Qué idiomas habla actualmente? (CASTELLANO) |
| `ms01_0107_D` | ¿Qué idiomas habla actualmente? (GUARANI) |
| `ms01_0107_X` | ¿Qué idiomas habla actualmente? (OTRO NATIVO) |
| `ms01_0107_Y` | (ESPECIFIQUE) OTRO NATIVO |
| `ms01_0107_X_cod` | ¿Qué idiomas habla actualmente? (EXTRANJERO) |
| `ms01_0107_Y_cod` | (ESPECIFIQUE) EXTRANJERO |
| `ms01_0108` | ¿A que nación o pueblo indígena originario campesino o afro boliviano pertenece? |
| `ms01_0108_npiocs` | (ESPECIFIQUE) LA NACIÓN O PUEBLO ORIGINARIO CAMPESINO O AFROBOLIVIANO |
| `ms01_0111` | ¿Asistió usted alguna vez a la escuela o colegio universidad, Curso de Alfabetización? |
| `ms01_0112_1` | ¿Cuál fue el nivel más alto de instrucción que aprobó? |
| `ms01_0112_2` | ¿Cuál fue el curso más alto de instrucción que aprobó? (CURSO) |
| `ms01_0114` | ¿Actualmente está asistiendo a la escuela, colegio, instituto superior o universidad? |
| `ms01_0115` | ¿Cuál fue la principal razón por la que no asiste a la escuela, instituto superior o universidad? |
| `ms01_0115_cod` | (ESPECIFIQUE) OTRA |
| `ms01_0117` | ¿Alguna vez ha participado usted en un programa de alfabetización o Programa YO SI PUEDO? |
| `ms01_0118` | Ahora me gustaría que: Usted lea en voz alta cada una de las siguientes frases:MUESTRE LA TARJETA A LA ENTREVISTADA. SI LA ENTREVISTADA NO PUEDE LEER TODA LA FRASE INDAGUE:¿Puede leer alguna parte de la frase? |
| `ms01_0118_esp` | (ESPECIFIQUE EL IDIOMA) NO HAY TARJETA EN EL IDIOMA REQUERIDO |
| `ms01_0119` | ¿Cuántos días a la semana lee usted un periódico? (impreso o digital) |
| `ms01_0120` | ¿Cuántos días a la semana escucha usted radio? |
| `ms01_0121` | ¿Cuántos días a la semana mira usted televisión? |
| `ms01_0122` | ¿Cuántos días a la semana entra a internet o a una red social? |
| `ms01_0123_A` | Durante la última semana ¿Realizó usted algunas de las siguientes actividades físicas y/o deportivas por 30 minutos o más:(A) Levantar cosas pesadas? |
| `ms01_0123_B` | Durante la última semana ¿Realizó usted algunas de las siguientes actividades físicas y/o deportivas por 30 minutos o más:(B) Manejar bicicleta? |
| `ms01_0123_C` | Durante la última semana ¿Realizó usted algunas de las siguientes actividades físicas y/o deportivas por 30 minutos o más:(C) Caminar? |
| `ms01_0123_D` | Durante la última semana ¿Realizó usted algunas de las siguientes actividades físicas y/o deportivas por 30 minutos o más:(D) Subir gradas o pendientes? |
| `ms01_0123_E` | Durante la última semana ¿Realizó usted algunas de las siguientes actividades físicas y/o deportivas por 30 minutos o más:(E) Bailar? |
| `ms01_0123_F` | Durante la última semana ¿Realizó usted algunas de las siguientes actividades físicas y/o deportivas por 30 minutos o más:(F) Trotar? |
| `ms01_0123_G` | Durante la última semana ¿Realizó usted algunas de las siguientes actividades físicas y/o deportivas por 30 minutos o más:(G) Correr? |
| `ms01_0123_X` | Durante la última semana ¿Realizó usted algunas de las siguientes actividades físicas y/o deportivas por 30 minutos o más:(X) Alguna otra? (ESPECIFIQUE) |
| `ms01_0123_X_cod` | ALGUNA OTRA? (ESPECIFIQUE) |
| `ms01_0125` | Durante la última semana ¿Cuántos días realizó actividades físicas y/o deportivas por 30 minutos o más? (NÚMERO DE DÍAS A LA SEMANA) |
| `ms01_0126` | ¿Cuántas horas pasa sentada diariamente? (NÚMERO DE HORAS AL DÍA) |
| `ms01_0127` | ¿Usted cree que realizar actividades físicas y/o deportivas es beneficioso para su salud? |
| `ms01_0128` | Durante el último mes ¿Sintió dolor de cabeza y/o zumbido en los oídos y/o sangrado por la nariz? |
| `ms01_0129` | Durante el último mes ¿Sintió disminución de peso aumento de la frecuencia para orinar, aumento de la sed o aumento del apetito? |
| `ms02_0201` | Ahora me gustaría preguntarle acerca de todos los hijos e hijas que usted ha tenido durante su vida.¿Ha tenido algún hijo o hija nacido vivo? |
| `ms02_0202` | De los hijos o hijas que usted tuvo.¿Hay algún hijo o hija que esté viviendo ahora con usted? |
| `ms02_0203_1` | ¿Cuántos hijos (varones) viven con usted? (HIJOS EN CASA)SI DIJO NINGUNO, PRESIONE EL BOTON "NINGUNO" |
| `ms02_0203_2` | ¿Cuántas hijas (mujeres) viven con usted? (HIJAS EN CASA)SI DIJO NINGUNO PRESIONE EL BOTON "NINGUNO" |
| `ms02_0204` | ¿Tiene usted alguna hija o hijo que esté vivo(a), pero que NO esté viviendo con usted? |
| `ms02_0205_1` | ¿Cuántos hijos (varones) están vivos pero NO viven con usted? (HIJOS FUERA)SI DIJO NINGUNO, PRESIONE EL BOTON "NINGUNO" |
| `ms02_0205_2` | ¿Cuántas hijas (mujeres) están vivas pero NO viven con usted? (HIJAS FUERA)SI DIJO NINGUNO PRESIONE EL BOTON "NINGUNO" |
| `ms02_0206` | ¿Alguna vez dio a luz a un niño o a una niña que nació vivo/a pero que falleció después?SI DIJO NO, INDAGUE:¿Tuvo usted alguna/algún (otra/o) niña o niño que lloró o mostró algún signo de vida pero que sólo vivió pocas horas o días? |
| `ms02_0207_1` | ¿Cuántos hijos (varones) han muerto? (HIJOS MUERTOS)SI DIJO NINGUNO, PRESIONE EL BOTON "NINGUNO" |
| `ms02_0207_2` | ¿Cuántas hijas (mujeres) han muerto? (HIJAS MUERTAS) SI DIJO NINGUNO, PRESIONE EL BOTON "NINGUNO" |
| `ms02_0208` | SUME LAS RESPUESTAS DE 203, 205 Y 207 Y ANOTE EL TOTAL. SI NO HA TENIDO HIJOS O HIJAS, ANOTE "00" |
| `ms02_0211` | ¿Cuando tuvo su primera/er hija/o. Usted dejó de estudiar? |
| `ms02_0212` | ¿Cuando tuvo sus siguientes embarazos, Usted dejó de estudiar durante alguno de ellos? |
| `ms02_0214_A` | ¿Cuál es la razón por la que dejó de estudiar?MARQUE TODAS LAS OPCIONES MENCIONADAS TENIA QUE CUIDAR NIÑOS PEQUEÑOS |
| `ms02_0214_B` | ¿Cuál es la razón por la que dejó de estudiar?MARQUE TODAS LAS OPCIONES MENCIONADAS POR TRABAJO |
| `ms02_0214_C` | ¿Cuál es la razón por la que dejó de estudiar?MARQUE TODAS LAS OPCIONES MENCIONADAS EL ESPOSO O SU PAREJA NO QUERIA |
| `ms02_0214_D` | ¿Cuál es la razón por la que dejó de estudiar?MARQUE TODAS LAS OPCIONES MENCIONADAS LOS SUEGROS O PADRES NO QUERIAN |
| `ms02_0214_E` | ¿Cuál es la razón por la que dejó de estudiar?MARQUE TODAS LAS OPCIONES MENCIONADAS FALTA DE DINERO |
| `ms02_0214_X` | ¿Cuál es la razón por la que dejó de estudiar?MARQUE TODAS LAS OPCIONES MENCIONADAS OTRAS RAZONES |
| `ms02_0214_X_cod` | (ESPECIFIQUE) OTRAS RAZONES |
| `ms02_0234` | ¿Está usted embarazada actualmente? |
| `ms02_0235` | ¿Cuántos meses de embarazo tiene?REGISTRE EL NÚMERO DE MESES COMPLETOS |
| `ms02_0237` | Cuando quedó embarazada, ¿Usted quería quedar embarazada en ese momento, quería esperar más tiempo o no quería tener (más) hijas/os o fue forzada? |
| `ms02_0238` | ¿A qué edad quedó embarazada por primera vez? (Edad en años) |
| `ms02_0239` | ¿Ha tenido usted alguna vez un embarazo que terminara en pérdida/fracaso o aborto? |
| `ms02_0240` | ¿Ha tenido usted alguna vez un embarazo que terminara en nacido muerto? |
| `ms02_0242_1` | ¿En qué mes terminó, abortó o nació muerto el último de estos embarazos fallidos? MES |
| `ms02_0242_2` | ¿En qué año terminó, abortó o nació muerto el último de estos embarazos fallidos? AÑO |
| `ms02_0243` | ¿Ese embarazo terminó en pérdida/fracaso/aborto o nacido muerto?SI ES ABORTO SONDEE ¿Espontáneo o inducido? |
| `ms02_0245` | ¿Cuántos meses de embarazo tenía usted cuando ocurrió la pérdida, el aborto o nacido muerto?REGISTRE EL NÚMERO DE MESES COMPLETOS |
| `ms02_0247` | ¿Ha tenido usted algún otro embarazo que haya terminado en pérdida o aborto después de enero de 2018? |
| `ms02_0248` | ¿Ha tenido usted algún otro embarazo que haya terminado en nacido muerto después de enero de 2018? |
| `ms02_0250` | ¿Tuvo usted otros embarazos que terminaran en pérdida, o aborto antes de enero de 2018? |
| `ms02_0251` | ¿Tuvo usted otros embarazos que terminaran en nacido muerto antes de enero del 2018? |
| `ms02_0253_1` | ¿En qué mes ocurrió el último de estos embarazos que terminó antes de enero de 2018? MES |
| `ms02_0253_2` | ¿En qué año ocurrió el último de estos embarazos que terminó antes de enero de 2018? AÑO |
| `ms02_0254` | ¿Cuántos meses duró ése embarazo que terminó antes de enero de 2018?REGISTRE EL NÚMERO DE MESES COMPLETOS |
| `ms02_0255` | ¿Ese embarazo terminó en pérdida/ fracaso/ aborto o nacido muerto?SI ES ABORTO SONDEE ¿Espontáneo o inducido? |
| `ms02_0257_A` | ¿A raíz de su último/actual embarazo, tuvo algún problema de salud: (A) Durante el embarazo? |
| `ms02_0257_B` | ¿A raíz de su último/actual embarazo, tuvo algún problema de salud: (B) Durante el parto o terminación? |
| `ms02_0257_C` | ¿A raíz de su último/actual embarazo, tuvo algún problema de salud: (C) Después del parto o terminación? |
| `ms02_0259_A` | ¿Qué tipo de problema de salud tuvo:(A) Dolor de cabeza fuera de lo normal? |
| `ms02_0259_B` | ¿Qué tipo de problema de salud tuvo:(B) Visión borrosa o como estrellitas? |
| `ms02_0259_C` | ¿Qué tipo de problema de salud tuvo: (C) Presión arterial elevada? |
| `ms02_0259_D` | ¿Qué tipo de problema de salud tuvo:(D) Ataques o convulsiones? |
| `ms02_0259_E` | ¿Qué tipo de problema de salud tuvo:(E) Pérdida de la conciencia? |
| `ms02_0259_F` | ¿Qué tipo de problema de salud tuvo:(F) Fiebre o calentura? |
| `ms02_0259_G` | ¿Qué tipo de problema de salud tuvo:(G) Infección en la matriz? |
| `ms02_0259_H` | ¿Qué tipo de problema de salud tuvo: (H) Flujo vaginal maloliente, con ardor y/o olor? |
| `ms02_0259_I` | ¿Qué tipo de problema de salud tuvo:(I) Dolor o ardor al orinar? |
| `ms02_0259_J` | ¿Qué tipo de problema de salud tuvo:(J) Pérdida de sangre o hemorragia genital antes del parto? |
| `ms02_0259_L` | ¿Qué tipo de problema de salud tuvo:(L) Pérdida de sangre o hemorragia genital después del parto? |
| `ms02_0259_M` | ¿Qué tipo de problema de salud tuvo:(M) La placenta no podía salir? |
| `ms02_0259_N` | ¿Qué tipo de problema de salud tuvo:(N) Desgarros genitales en el parto? |
| `ms02_0259_O` | ¿Qué tipo de problema de salud tuvo:(O) El bebe estaba mal acomodado? |
| `ms02_0259_P` | ¿Qué tipo de problema de salud tuvo:(P) El parto duró mas de 12 horas? |
| `ms02_0259_Q` | ¿Qué tipo de problema de salud tuvo:(Q) Se rompio la bolsa de agua antes de que comiencen los dolores de parto? |
| `ms02_0259_X` | ¿Qué tipo de problema de salud tuvo:(X) Otro no mencionado? (ESPECIFIQUE) |
| `ms02_0259_X_cod` | OTRO (ESPECIFIQUE) |
| `ms02_0260` | ¿Buscó algún tipo de ayuda o atención para ese/ esos problema/s? |
| `ms02_0261_A` | ¿De quiénes buscó atención o ayuda:(A) Del personal de servicio de salud? |
| `ms02_0261_B` | ¿De quiénes buscó atención o ayuda:(B) De partera y/o médico tradicional? |
| `ms02_0261_C` | ¿De quiénes buscó atención o ayuda:(C) De la Farmacia? |
| `ms02_0261_D` | ¿De quiénes buscó atención o ayuda:(D) De la Junta de Vecinos? |
| `ms02_0261_E` | ¿De quiénes buscó atención o ayuda:(E) De su Autoridad local de salud (ALS, COLOSA, COSOMUSA)? |
| `ms02_0261_F` | ¿De quiénes buscó atención o ayuda:(F) De la comunidad organizada? |
| `ms02_0261_G` | ¿De quiénes buscó atención o ayuda:(G) De la Iglesia? |
| `ms02_0261_H` | ¿De quienes busco atención o ayuda:(H) Del Esposo o familiares? |
| `ms02_0261_I` | ¿De quiénes buscó atención o ayuda:(I) De amigos, vecinos? |
| `ms02_0261_J` | ¿De quiénes buscó atención o ayuda:(J) Se atendió usted misma? |
| `ms02_0263_A` | ¿De qué manera recibió ayuda de la comunidad/ Junta de Vecinos/ ALS, para encontrar atención en un servicio de salud?(A) Comunicaron al servicio de salud (Ej. llamaron ambulancia)? |
| `ms02_0263_B` | ¿De qué manera recibió ayuda de la comunidad/ Junta de Vecinos/ ALS, para encontrar atención en un servicio de salud?(B) Gestionaron o coordinaron la atención con el centro de salud? |
| `ms02_0263_C` | ¿De qué manera recibió ayuda de la comunidad/ Junta de Vecinos/ ALS, para encontrar atención en un servicio de salud?(C) Facilitaron transporte? |
| `ms02_0263_D` | ¿De qué manera recibió ayuda de la comunidad/ Junta de Vecinos/ ALS, para encontrar atención en un servicio de salud?(D) Acompañaron hasta el servicio de salud? |
| `ms02_0263_E` | ¿De qué manera recibió ayuda de la comunidad/ Junta de Vecinos/ ALS, para encontrar atención en un servicio de salud?(E) Acompañaron hasta un servicio de medicina tradicional? |
| `ms02_0263_F` | ¿De qué manera recibió ayuda de la comunidad/ Junta de Vecinos/ ALS, para encontrar atención en un servicio de salud?(F) Cuidaron a sus hijas/os? |
| `ms02_0265` | ¿Cuál fue la razón principal por la que usted no buscó ayuda?SI MENCIONA VARIAS, SONDEAR PARA DETERMINAR LA RAZÓN PRINCIPAL |
| `ms02_0265_cod` | (ESPECIFIQUE) OTRA RAZÓN |
| `ms02_0266_A` | ¿Por qué usted no pensó en acudir a un servicio de salud? (EL SERVICIO DE SALUD QUEDA LEJOS) |
| `ms02_0266_B` | ¿Por qué usted no pensó en acudir a un servicio de salud? (NO EXISTE PERSONAL DE SALUD) |
| `ms02_0266_C` | ¿Por qué usted no pensó en acudir a un servicio de salud? (SABEMOS QUE TRATAN MAL) |
| `ms02_0266_D` | ¿Por qué usted no pensó en acudir a un servicio de salud? (NO RESUELVEN LOS PROBLEMAS) |
| `ms02_0266_E` | ¿Por qué usted no pensó en acudir a un servicio de salud? (EL SERVICIO ES CARO) |
| `ms02_0266_F` | ¿Por qué usted no pensó en acudir a un servicio de salud? (NO PENSÓ EN ESA POSIBILIDAD) |
| `ms02_0266_G` | ¿Por qué usted no pensó en acudir a un servicio de salud? (PREOCUPACIÓN DE QUE NO HAYA MEDICAMENTOS PARA LA ATENCIÓN) |
| `ms02_0266_H` | ¿Por qué usted no pensó en acudir a un servicio de salud? (NO CONSENTIMIENTO DEL ESPOSO) |
| `ms02_0266_I` | ¿Por qué usted no pensó en acudir a un servicio de salud? (DE LA MADRE O SUEGRA FAMILIA) |
| `ms02_0266_J` | ¿Por qué usted no pensó en acudir a un servicio de salud? (FALTA DE TRANSPORTE) |
| `ms02_0266_K` | ¿Por qué usted no pensó en acudir a un servicio de salud? (MAL ESTADO DE CAMINOS) |
| `ms02_0266_L` | ¿Por qué usted no pensó en acudir a un servicio de salud? (NO PERMISO EN EL TRABAJO) |
| `ms02_0266_M` | ¿Por qué usted no pensó en acudir a un servicio de salud? (TOQUE MAL INTENCIONADO PERSONAL DE SALUD) |
| `ms02_0266_X` | ¿Por qué usted no pensó en acudir a un servicio de salud? (OTRA RAZÓN) |
| `ms02_0266_X_cod` | (ESPECIFIQUE) OTRA RAZÓN |
| `ms02_0267_A` | ¿Qué hizo o qué tipo de ayuda o tratamiento recibió? (MASAJES) |
| `ms02_0267_B` | ¿Qué hizo o qué tipo de ayuda o tratamiento recibió? (MANTEO) |
| `ms02_0267_C` | ¿Qué hizo o qué tipo de ayuda o tratamiento recibió? (MATES CASEROS) |
| `ms02_0267_D` | ¿Qué hizo o qué tipo de ayuda o tratamiento recibió? (INYECCIONES) |
| `ms02_0267_D_esp` | (ESPECIFIQUE) INYECCIONES |
| `ms02_0267_E` | ¿Qué hizo o qué tipo de ayuda o tratamiento recibió? (TABLETAS O PASTILLAS) |
| `ms02_0267_E_esp` | (ESPECIFIQUE) TABLETAS O PASTILLAS |
| `ms02_0267_F` | ¿Qué hizo o qué tipo de ayuda o tratamiento recibió? (SAHUMERIO) |
| `ms02_0267_G` | ¿Qué hizo o qué tipo de ayuda o tratamiento recibió? (BAÑOS DE HIERBAS) |
| `ms02_0267_X` | ¿Qué hizo o qué tipo de ayuda o tratamiento recibió? (OTRA AYUDA O TRATAMIENTO) |
| `ms02_0267_X_esp` | ¿Qué hizo o qué tipo de ayuda o tratamiento recibió? (NINGUN O NADA) |
| `ms02_0267_Y` | (ESPECIFIQUE) OTRA AYUDA O TRATAMIENTO |
| `ms02_0268` | ¿Tuvo alguna dificultad para llegar hasta el servicio de salud?SI LA RESPUESTA ES "SI", PREGUNTE:¿Cuál fue la principal dificultad que tuvo para llegar hasta el servicio de salud? |
| `ms02_0268_cod` | (ESPECIFIQUE) OTRA DIFICULTAD |
| `ms02_0269` | ¿Cuál fue el principal problema que tuvo en el servicio de salud cuando recibió la atención? |
| `ms02_0269_cod` | (ESPECIFIQUE) OTRO PROBLEMA |
| `ms02_0270` | Si en el hospital le cobraron, le enviaron a otro servicio de salud o no quisieron atenderla:¿Sabía que tenía que ir a un establecimiento de 1er nivel, puesto o centro de salud, en primer lugar? |
| `ms02_0271_A` | ¿Cual es la causa por que no conoce su establecimiento de salud de primer nivel? NO LE INTERESA CONOCER |
| `ms02_0271_B` | ¿Cual es la causa por que no conoce su establecimiento de salud de primer nivel? NADIE LE INFORMÓ |
| `ms02_0271_C` | ¿Cual es la causa por que no conoce su establecimiento de salud de primer nivel? NO SABE |
| `ms02_0272_A` | ¿Cuáles de los siguientes tratamientos le dieron para su problema de salud:(A) Transfusión de sangre? |
| `ms02_0272_B` | ¿Cuáles de los siguientes tratamientos le dieron para su problema de salud:(B) Otro tratamiento médico? |
| `ms02_0272_B_esp` | (ESPECIFIQUE) OTRO TRATAMIENTO MÉDICO |
| `ms02_0272_C` | ¿Cuáles de los siguientes tratamientos le dieron para su problema de salud:(C) Legrado, limpieza, raspaje? |
| `ms02_0272_D` | ¿Cuáles de los siguientes tratamientos le dieron para su problema de salud:(D) Cesárea? |
| `ms02_0272_X` | ¿Cuáles de los siguientes tratamientos le dieron para su problema de salud:(X) Otra cirugía? |
| `ms02_0272_X_cod` | (ESPECIFIQUE) OTRA CIRUGÍA |
| `ms02_0273_1` | ¿Cuándo comenzó su última regla o menstruación? HACE: |
| `ms02_0273_2` | REGISTRE LA RESPUESTA EN LA UNIDAD DE TIEMPO DADA[ms02_0273_01] |
| `ms02_0274` | Entre una menstruación y otra ¿Cree usted que hay ciertos días en los que una mujer puede quedar embarazada más fácilmente si tiene relaciones sexuales? |
| `ms02_0275` | Para usted, ¿cuáles son esos días: |
| `ms02_0275_cod` | (ESPECIFIQUE) OTRO |
| `ms02_0276` | ¿Usted recibió información sobre educación para la sexualidad? |
| `ms02_0277` | ¿Dónde recibió por primera vez, información o educación para la sexualidad? |
| `ms02_0277_cod` | (ESPECIFIQUE) OTRO |
| `ms02_0278` | ¿Considera usted que el cáncer se puede prevenir? |
| `ms02_0279` | ¿Alguna vez en su vida usted ha oído hablar del cáncer de cuello uterino, también llamado cáncer cervical? |
| `ms02_0280` | ¿Alguna vez en su vida usted ha oído hablar del virus del papiloma humano VPH? |
| `ms02_0281` | ¿Conoce usted a qué edad se administra la vacuna contra el VPH? |
| `ms02_0282` | ¿Cuántas mujeres del hogar de sexo femenino entre 10 a 17 años recibieron la vacuna contra el VPH (Virus Papiloma Humano)? |
| `ms02_0283` | ¿Cree usted que el virus del papiloma humano puede causar cáncer de cuello uterino, también llamado cáncer cervical? |
| `ms02_0284` | ¿Se ha realizado el Papanicolaou (PAP) o Inspección Visual con Acido Acético IVAA para detectar Cáncer del Útero en los últimos tres años? |
| `ms02_0285` | ¿Cuántas veces se ha realizado el Papanicolaou (PAP)/ IVAA en los últimos tres años? (NÚMERO DE VECES) |
| `ms02_0286` | ¿Cada cuánto tiempo se ha realizado los exámenes para detectar Cáncer del Útero en los últimos tres años? |
| `ms02_0287` | ¿En la última prueba, cuál fue el resultado?ANOTE LA RESPUESTA DE MANERA TEXTUAL |
| `ms02_0288_A` | Como resultado de la prueba: ¿Fue a otro servicio de salud? |
| `ms02_0288_B` | Como resultado de la prueba:¿Se hizo otros exámenes? |
| `ms02_0288_C` | Como resultado de la prueba:¿Siguió algún tratamiento? |
| `ms02_0288_D` | Como resultado de la prueba:¿Repitió el PAP o IVAA inmediatamente o en los siguientes 30 días? |
| `ms02_0288_E` | Como resultado de la prueba:¿Repitió el PAP o IVAA en un año o más? |
| `ms02_0289` | ¿Por qué razón no se hizo el examen del PAP o IVAA? |
| `ms02_0289_cod` | (ESPECIFIQUE) OTRO |
| `ms02_0290` | ¿Qué hizo cuando el resultado del PAP/IVAA fue negativo? |
| `ms02_0290_cod` | (ESPECIFIQUE) OTRO |
| `ms02_0291` | ¿Conoce usted alguna persona, hermana, familiar, amiga o vecina que haya fallecido por cáncer de cuello uterino? |
| `ms02_0292` | ¿Cuántas mujeres conoce que hayan fallecido por cáncer de cuello uterino? (NÚMERO DE PERSONAS) |
| `ms02_0293` | ¿Ha escuchado sobre el Cáncer de Mama? |
| `ms02_0294` | ¿A partir de qué edad cree usted que debe hacerse un chequeo para descartar el cáncer de mama? |
| `ms02_0295` | ¿Alguna vez se ha practicado el autoexamen de sus pechos/mamas? |
| `ms02_0296` | ¿Alguna vez le han practicado algún examen por problemas de sus pechos/mamas? |
| `ms02_0297_A` | ¿Conoce a alguna persona que ha tenido o tiene cáncer de mama:(A) En su familia? |
| `ms02_0297_B` | ¿Conoce a alguna persona que ha tenido o tiene cáncer de mama:(B) En su comunidad? |
| `ms03_0301_01` | ¿Qué métodos o maneras conoce usted o de cuáles ha oído hablar?¿Conoce o ha oído hablar de:1 Esterilización femenina (ligadura de trompas)Las mujeres pueden someterse a una operación para evitar tener más hijas/os. |
| `ms03_0302_01` | ¿Ud. se ha hecho operar para no tener (más) hijas/os? |
| `ms03_0301_02` | ¿Conoce o ha oído hablar de:2 Esterilización/ operación masculina (vasectomía)Los hombres pueden someterse a una operación para evitar tener más hijas/os. |
| `ms03_0302_02` | ¿Ha tenido una pareja (esposo) que se ha hecho operar para no tener (más) hijas/os? |
| `ms03_0301_03` | ¿Conoce o ha oído hablar de :3 Píldoras/pastillas (métodos orales)?Las mujeres pueden tomar todos los días una pastilla para evitar quedar embarazada. |
| `ms03_0302_03` | ¿Ha usado usted alguna vez píldoras/pastillas (métodos orales)? |
| `ms03_0301_04` | ¿Conoce o ha oído hablar de :4 Dispositivo intrauterino o diu?Las mujeres pueden pedir a un médico o enfermera que le coloque un anillo o una T de cobre en la matriz. |
| `ms03_0302_04` | ¿Ha usado usted alguna vez dispositivo intrauterino o diu? |
| `ms03_0301_05` | ¿Conoce o ha oído hablar de :5 inyección anticonceptiva (para no tener hijos/as)?Las mujeres pueden pedir a un médico o una enfermera que le aplique una inyección mensual o trimestral para evitar quedar embarazada. |
| `ms03_0302_05` | ¿Ha usado usted alguna vez: inyección anticonceptiva (para no tener hijos/as)? |
| `ms03_0301_06` | ¿Conoce o ha oído hablar de :6 Implantes?Las mujeres pueden pedir a un médico o enfermera que le coloque debajo de la piel del brazo cápsulas (tubitos) para evitar que salga embarazada durante uno o varios años. |
| `ms03_0302_06` | ¿Ha usado usted alguna vez implantes? |
| `ms03_0301_07` | ¿Conoce o ha oído hablar de :7 Anticoncepción de emergencia (píldora del día siguiente)?Las mujeres pueden tomar ciertas pastillas hasta 48 horas después de haber tenido relaciones sexuales para evitar quedar embarazadas. |
| `ms03_0302_07` | ¿Ha usado usted alguna vez anticoncepción de emergencia (Pildora del día siguiente)? |
| `ms03_0301_08` | ¿Conoce o ha oído hablar de : 8 Condón (preservativo)?Los hombres pueden usar una fundita de goma puesta en el pene durante las relaciones sexuales para evitar que la mujer salga embarazada. |
| `ms03_0302_08` | ¿Ha usado usted alguna vez condón preservativo? |
| `ms03_0301_09` | ¿Conoce o ha oído hablar de :9 Condón femenino?Las mujeres pueden usar una fundita de goma que tiene dos anillos, uno interno que no contiene espermicidas, que permite la colocación fácil dentro de la vagina, y el otro externo con un diámetro más grande, |
| `ms03_0302_09` | ¿Ha usado alguna vez condón femenino? |
| `ms03_0301_10` | ¿Conoce o ha oído hablar de :10 Tabletas vaginales, óvulos, espuma o jalea (métodos vaginales)?La mujer puede colocarse dentro de la vagina una tableta, crema, espuma, óvulo, jalea antes de tener relaciones sexuales. |
| `ms03_0302_10` | ¿Ha usado usted alguna vez tabletas vaginales óvulos, espuma o jalea (métodos vaginales)? |
| `ms03_0301_11` | ¿Conoce o ha oído hablar de :11 Método de lactancia y amenorrea (mela)?Las mujeres pueden alimentar a su niño sólo con el seno durante los primeros 6 meses mientras no le ha llegado la regla o menstruación para evitar así quedar embarazada. |
| `ms03_0302_11` | ¿Ha usado usted alguna vez método de lactancia y amenorrea (Mela)? |
| `ms03_0301_12` | ¿Conoce o ha oído hablar de :12 Ritmo, ovulación, abstinencia periódica o billings, rosario?Las parejas pueden dejar de tener relaciones sexuales durante aquellos días del mes en los cuales la mujer tiene más posibilidad de quedar embarazada. |
| `ms03_0302_12` | ¿Ha usado usted alguna vez ritmo ovulación, abstinencia periódica o billings, rosario? |
| `ms03_0301_13` | ¿Conoce o ha oído hablar de :13 Retiro (coito interrumpido)?Los hombres pueden ser cuidadosos y retirarse antes de terminar el acto sexual, eyaculando o vaciándose fuera de la vagina de la mujer. |
| `ms03_0302_13` | ¿Ha usado usted alguna vez retiro (COITO INTERRUMPIDO)? |
| `ms03_0301_14` | ¿Conoce o ha oído hablar de :14 Otro método?¿Ha oído usted hablar o conoce alguna otra forma o método usado por las mujeres o los hombres para evitar embarazos? |
| `ms03_0301_14_cod` | (ESPECIFIQUE) OTRO MÉTODO |
| `ms03_0302_14` | ¿Ha usado usted alguna vez [(ESPECIFIQUE) OTRO MÉTODO]? |
| `ms03_0305` | Usted y su pareja ¿Alguna vez han hecho algo o tratado de algún modo de demorar o evitar un embarazo? |
| `ms03_0309` | Ahora me gustaría preguntarle acerca de la primera vez que usted hizo algo o usó algún método para evitar quedar embarazada.¿Cuántas hijas e hijos vivos tenía usted en ese momento? (NÚMERO DE HIJAS/OS) |
| `ms03_0312` | ¿Actualmente está: usted o su marido/ pareja haciendo algo o usando algún método para postergar o evitar quedar embarazada? |
| `ms03_0313_A` | ¿Qué métodos está(n) usando? (ESTERILIZACIÓN FEMENINA) |
| `ms03_0313_B` | ¿Qué métodos está(n) usando? (ESTERILIZACIÓN MASCULINA) |
| `ms03_0313_C` | ¿Qué métodos está(n) usando? (PÍLDORAS/PASTILLAS) |
| `ms03_0313_D` | ¿Qué métodos está(n) usando? (DIU) |
| `ms03_0313_E` | ¿Qué métodos está(n) usando? (INYECCIONES) |
| `ms03_0313_F` | ¿Qué métodos está(n) usando? (IMPLANTE) |
| `ms03_0313_G` | ¿Qué métodos está(n) usando? (ANTICONCEPCIÓN DE EMERGENCIA) |
| `ms03_0313_H` | ¿Qué métodos está(n) usando? (CONDÓN MASCULINO) |
| `ms03_0313_I` | ¿Qué métodos está(n) usando? (CONDÓN FEMENINO) |
| `ms03_0313_J` | ¿Qué métodos está(n) usando? (TABLETA / ÓVULO / ESPUMA / JALEA) |
| `ms03_0313_K` | ¿Qué métodos está(n) usando? (MELA (LACTANCIA Y AMENORREA)) |
| `ms03_0313_L` | ¿Qué métodos está(n) usando? (RITMO) |
| `ms03_0313_M` | ¿Qué métodos está(n) usando? (RETIRO) |
| `ms03_0313_X` | ¿Qué métodos está(n) usando? (OTRO MÉTODO) |
| `ms03_0313_X_cod` | (ESPECIFIQUE) OTRO METODO |
| `ms03_0314` | La última vez que obtuvo [ms03_0313]¿Cuánto pagó en total incluyendo costo del método y consulta? |
| `ms03_0314_01` | ¿Cuánto pagó en total incluyendo costo del método y consulta? (COSTO) |
| `ms03_0315` | ¿Dónde tuvo lugar la esterilización?MARCAR LAS RESPUESTAS MENCIONADASSUBSECTOR PÚBLICOESTABLECIMIENTOS DE SALUD DEL SECTOR PÚBLICO: 1ER NIVEL |
| `ms03_0315_cod` | (ESPECIFIQUE) OTRO LUGAR |
| `ms03_0316_A` | Antes de su operación/ esterilización ¿Le informaron que no podría tener más hijos después de la operación? |
| `ms03_0316_B` | Antes de la operación, ¿Le informaron a su esposo/ compañero que no podría tener más hijos después de la operación? |
| `ms03_0317` | ¿Cuánto pagó usted (su esposo/compañero) en total por la esterilización incluyendo el costo del método y la consulta? |
| `ms03_0317_1` | ¿Cuánto pagó usted (su esposo/compañero) en total por la esterilización incluyendo el costo del método y la consulta? (COSTO) |
| `ms03_0318_1` | ¿En qué MES la(o) operarón/ esterilizarón? |
| `ms03_0318_2` | ¿En qué AÑO la(o) operarón/ esterilizarón? |
| `ms03_0319_1` | ¿En qué MES empezó a usar continuamente [ms03_0313] la última vez? ¿Por cuánto tiempo ha estado usando (MÉTODO) en forma ininterrumpida? |
| `ms03_0319_2` | ¿En qué AÑO empezó a usar continuamente [ms03_0313] la última vez? ¿Por cuánto tiempo ha estado usando (MÉTODO) en forma ininterrumpida? |
| `ms03_0323` | SELECCIONE EL CÓDIGO DEL MÉTODO USADO ACTUALMENTE: |
| `ms03_0324_1` | ¿Dónde obtuvo la primera vez el [ms03_0323] que está usando actualmente? |
| `ms03_0324_cod` | (ESPECIFIQUE) OTRO LUGAR |
| `ms03_0324_2` | ¿Dónde aprendió sobre el MELA o Ritmo? |
| `ms03_0324_2_cod` | (ESPECIFIQUE) OTRO LUGAR |
| `ms03_0326` | SELECCIONE EL CÓDIGO DEL MÉTODO USADO ACTUALMENTE: |
| `ms03_0327_1` | ¿En ese momento, alguien le informó sobre los efectos secundarios o problemas que podría tener por causa del método? |
| `ms03_0328_1` | En ese momento, ¿Le informaron de otros métodos de planificación familiar que podría usar? |
| `ms03_0328_2` | ¿Le informaron de otros métodos de planificación familiar que podría usar? |
| `ms03_0329` | ¿En algún momento un trabajador de salud o de planificación familiar le informó sobre métodos de anticoncepcion que podría usar? |
| `ms03_0330` | SELECCIONE EL MÉTODO USADO ACTUALMENTE: |
| `ms03_0331` | ¿Dónde consiguió el (MÉTODO) la última vez? |
| `ms03_0332` | ¿Sabe de algún lugar donde se pueda obtener un metodo de planificacion familiar/anticoncepción? |
| `ms03_0333_A` | ¿Cuál es ese lugar? (PUESTO DE SALUD) |
| `ms03_0333_B` | ¿Cuál es ese lugar? (CENTRO DE SALUD AMBULATORIO) |
| `ms03_0333_C` | ¿Cuál es ese lugar? (CENTRO DE SALUD CON INTERNACION) |
| `ms03_0333_D` | ¿Cuál es ese lugar? (CENTRO DE SALUD INTEGRAL) |
| `ms03_0333_E` | ¿Cuál es ese lugar? (HOSPITAL DE SEGUNDO NIVEL) |
| `ms03_0333_F` | ¿Cuál es ese lugar? (HOSPITAL DE TERCER NIVEL) |
| `ms03_0333_G` | ¿Cuál es ese lugar? (HOSPITAL ESPECIALIZADO) |
| `ms03_0333_H` | ¿Cuál es ese lugar? (CAJA NACIONAL DE SALUD) |
| `ms03_0333_I` | ¿Cuál es ese lugar? (CAJA DE LA BANCA PRIVADA) |
| `ms03_0333_J` | ¿Cuál es ese lugar? (CAJA PETROLERA) |
| `ms03_0333_K` | ¿Cuál es ese lugar? (CAJA DE LA BANCA ESTATAL) |
| `ms03_0333_L` | ¿Cuál es ese lugar? (CORDES) |
| `ms03_0333_M` | ¿Cuál es ese lugar? (CAJA DE CAMINOS) |
| `ms03_0333_N` | ¿Cuál es ese lugar? (COSSMIL/FFAA) |
| `ms03_0333_O` | ¿Cuál es ese lugar? (SEGURO UNIVERSITARIO) |
| `ms03_0333_P` | ¿Cuál es ese lugar? (ORGANISMOS PRIVADOS (PRIMER NIVEL, SEGUNDO NIVEL, TERCER NIVEL) |
| `ms03_0333_Q` | ¿Cuál es ese lugar? (IGLESIA PRIMER NIVEL, SEGUNDO NIVEL, TERCER NIVEL) |
| `ms03_0333_R` | ¿Cuál es ese lugar? (PROMOTOR DE LA SALUD/RPS/OTRO AGENTE) |
| `ms03_0333_S` | ¿Cuál es ese lugar? (VISITA DOMICILIARIA) |
| `ms03_0333_T` | ¿Cuál es ese lugar? (FARMACIA) |
| `ms03_0333_U` | ¿Cuál es ese lugar? (MEDICINA TRADICIONAL) |
| `ms03_0333_V` | ¿Cuál es ese lugar? (NO ACUDIÓ A NINGUN E.S./NO FUE) |
| `ms03_0333_X` | ¿Cuál es ese lugar? (OTRO LUGAR:) |
| `ms03_0333_Z` | ¿Cuál es ese lugar? (NO SABE) |
| `ms03_0333_X_cod` | (ESPECIFIQUE) OTRO PÚBLICO |
| `ms03_0334_A` | En los últimos doce meses, ¿Usted buscó y encontró información sobre anticoncepción / Planificación familiar:(A) En establecimiento de Salud Privado? |
| `ms03_0334_B` | En los últimos doce meses, ¿Usted buscó y encontró información sobre anticoncepción / Planificación familiar:(B) En establecimiento de Salud Público? |
| `ms03_0334_C` | En los últimos doce meses, ¿Usted buscó y encontró información sobre anticoncepción / Planificación familiar:(C) En Internet? |
| `ms03_0334_D` | En los últimos doce meses, ¿Usted buscó y encontró información sobre anticoncepción / Planificación familiar:(D) En su familia? |
| `ms03_0334_X` | En los últimos doce meses, ¿Usted buscó y encontró información sobre anticoncepción / Planificación familiar:(X) En otro sitio? (ESPECIFIQUE) |
| `ms03_0334_X_cod` | (ESPECIFIQUE) OTRO |
| `ms05_0501` | Durante las últimas dos semanas , ¿usted donde consumió con mayor frecuencia las comidas principales? |
| `ms05_0502_A` | Tipos de alimentos que, usted consumió el día de ayer durante el día o durante la noche, bien por separado o con otros alimentos.1. CEREALES, TUBERCULOS Y DERIVADOS(A) Cereales y derivados:Arroz,fideo,quinua, pan,galletas,otros. |
| `ms05_0502_B` | Tipos de alimentos que, usted consumió el día de ayer durante el día o durante la noche, bien por separado o con otros alimentos.1. CEREALES, TUBERCULOS Y DERIVADOS(B) Leguminosas: Lenteja, poroto, frijol, tarhui y otros |
| `ms05_0502_C` | Tipos de alimentos que, usted consumió el día de ayer durante el día o durante la noche, bien por separado o con otros alimentos.1. CEREALES, TUBERCULOS Y DERIVADOS(C) Tubérculos: Papa,oca, yuca, chuño y otros |
| `ms05_0502_D` | Tipos de alimentos que, usted consumió el día de ayer durante el día o durante la noche, bien por separado o con otros alimentos.2. VERDURAS(D) Color verde obscuro: Acelga, espinaca, apio, brócoli y otros |
| `ms05_0502_E` | Tipos de alimentos que, usted consumió el día de ayer durante el día o durante la noche, bien por separado o con otros alimentos.2. VERDURAS(E) Color amarillo a naranja por dentro: zapallo, zanahoria |
| `ms05_0502_F` | Tipos de alimentos que, usted consumió el día de ayer durante el día o durante la noche, bien por separado o con otros alimentos.2. VERDURAS(F) Cualquier otra verdura |
| `ms05_0502_G` | Tipos de alimentos que, usted consumió el día de ayer durante el día o durante la noche, bien por separado o con otros alimentos.3. FRUTAS(G) Color amarillo a naranja por dentro: papaya, mango, piña, otros |
| `ms05_0502_H` | Tipos de alimentos que, usted consumió el día de ayer durante el día o durante la noche, bien por separado o con otros alimentos.3. FRUTAS(H) Cualquier otra fruta |
| `ms05_0502_I` | Tipos de alimentos que, usted consumió el día de ayer durante el día o durante la noche, bien por separado o con otros alimentos.4. LACTEOS Y DERIVADOS(I) Leche, yogurt, queso y otros |
| `ms05_0502_J` | Tipos de alimentos que, usted consumió el día de ayer durante el día o durante la noche, bien por separado o con otros alimentos.5. CARNES, DERIVADOS Y HUEVOS(J) Res, Hígado, Riñón, Corazón |
| `ms05_0502_K` | Tipos de alimentos que, usted consumió el día de ayer durante el día o durante la noche, bien por separado o con otros alimentos.5. CARNES, DERIVADOS Y HUEVOS(K) Pollo, Pescado, Cerdo, Cordero, Llama, Conejo y vísceras |
| `ms05_0502_L` | Tipos de alimentos que, usted consumió el día de ayer durante el día o durante la noche, bien por separado o con otros alimentos.5. CARNES, DERIVADOS Y HUEVOS(L) Huevo |
| `ms05_0502_M` | Tipos de alimentos que, usted consumió el día de ayer durante el día o durante la noche, bien por separado o con otros alimentos.6. GRASAS Y DERIVADOS(M) Aceite vegetal, oliva, girasol, maíz, soja y otros |
| `ms05_0502_N` | Tipos de alimentos que, usted consumió el día de ayer durante el día o durante la noche, bien por separado o con otros alimentos.6. GRASAS Y DERIVADOS(N) manteca, cebo, margarina |
| `ms05_0502_O` | Tipos de alimentos que, usted consumió el día de ayer durante el día o durante la noche, bien por separado o con otros alimentos.6. GRASAS Y DERIVADOS(O) mantequilla |
| `ms05_0502_P` | Tipos de alimentos que, usted consumió el día de ayer durante el día o durante la noche, bien por separado o con otros alimentos.7. AZUCARES(P) Azucar blanca |
| `ms05_0502_Q` | Tipos de alimentos que, usted consumió el día de ayer durante el día o durante la noche, bien por separado o con otros alimentos.7. AZUCARES(Q) Azúcar morena, miel, chancaca y otros |
| `ms05_0502_R` | Tipos de alimentos que, usted consumió el día de ayer durante el día o durante la noche, bien por separado o con otros alimentos.8. OTROS(R) Agua |
| `ms05_0502_S` | Tipos de alimentos que, usted consumió el día de ayer durante el día o durante la noche, bien por separado o con otros alimentos.8. OTROS(S) Otros líquidos (té, mate,café) |
| `ms05_0503_A` | Ahora me gustaría preguntarle a cerca del consumo en la última semana de los siguientes producto s(A) (COMIDA RÁPIDA) Pollo broaster, Hamburguesa, Salchipapa, Hot dog, papas fritas y otras frituras |
| `ms05_0503_B` | Ahora me gustaría preguntarle a cerca del consumo en la última semana de los siguientes productos(B) (BEBIDAS AZUCARADAS) Bebidas con gas, Néctar, Jugos envasados, Energizantes, Otros |
| `ms05_0503_C` | Ahora me gustaría preguntarle a cerca del consumo en la última semana de los siguientes productos(C) (ALIMENTOS PROCESADOS) Tortas, queques, roscas, galletas dulces/ dulces/ saladas y otros |
| `ms05_0504` | ¿Ha oído hablar del SISTEMA ÚNICO DE SALUD (SUS )? |
| `ms05_0505_A` | ¿A quiénes atiende el SUS? (A TODAS LAS MUJERES) |
| `ms05_0505_B` | ¿A quiénes atiende el SUS? (A MUJERES EMBARAZADAS) |
| `ms05_0505_C` | ¿A quiénes atiende el SUS? (A MUJERES QUE RECIÉN HAN TENIDO HIJOS) |
| `ms05_0505_D` | ¿A quiénes atiende el SUS? (A TODAS/OS LAS/OS NIÑAS Y NIÑOS) |
| `ms05_0505_E` | ¿A quiénes atiende el SUS? (A NIÑAS Y NIÑOS MENORES DE 5 AÑOS) |
| `ms05_0505_F` | ¿A quiénes atiende el SUS? (A TODA LA POBLACIÓN) |
| `ms05_0505_X` | ¿A quiénes atiende el SUS? (OTROS) |
| `ms05_0505_Z` | ¿A quiénes atiende el SUS? (NO SABE A QUIENES) |
| `ms05_0505_X_cod` | (ESPECIFIQUE) OTROS |
| `ms05_0506` | ¿Usted esta registrada al Sistema Único de Salud (SUS) ? |
| `ms05_0507` | ¿Desde el 2018, en algún momento usted ha recibido atención de salud por el Sistema Único de Salud (SUS)? |
| `ms05_0508_A` | ¿Cuál fue la razón principal por la cual no utilizó los servicios del Sistema Único de Salud (SUS)? (TIENE QUE ESPERAR MUCHO) |
| `ms05_0508_B` | ¿Cuál fue la razón principal por la cual no utilizó los servicios del Sistema Único de Salud (SUS)? (NO HAY DONDE ESPERAR/INCÓMODO) |
| `ms05_0508_C` | ¿Cuál fue la razón principal por la cual no utilizó los servicios del Sistema Único de Salud (SUS)? (PERSONAL POCO AMABLE) |
| `ms05_0508_D` | ¿Cuál fue la razón principal por la cual no utilizó los servicios del Sistema Único de Salud (SUS)? (PERSONAL SIN EXPERIENCIA/NO CAPACITADO) |
| `ms05_0508_E` | ¿Cuál fue la razón principal por la cual no utilizó los servicios del Sistema Único de Salud (SUS)? (PERSONAL NUNCA DISPONIBLE) |
| `ms05_0508_F` | ¿Cuál fue la razón principal por la cual no utilizó los servicios del Sistema Único de Salud (SUS)? (EL LUGAR NO ES LIMPIO) |
| `ms05_0508_G` | ¿Cuál fue la razón principal por la cual no utilizó los servicios del Sistema Único de Salud (SUS)? (EL LUGAR QUEDA MUY LEJOS) |
| `ms05_0508_H` | ¿Cuál fue la razón principal por la cual no utilizó los servicios del Sistema Único de Salud (SUS)? (NO ABREN TODOS LOS DÍAS) |
| `ms05_0508_I` | ¿Cuál fue la razón principal por la cual no utilizó los servicios del Sistema Único de Salud (SUS)? (HORARIO DE ATENCIÓN INADECUADO) |
| `ms05_0508_J` | ¿Cuál fue la razón principal por la cual no utilizó los servicios del Sistema Único de Salud (SUS)? (NO TENÍA DINERO) |
| `ms05_0508_K` | ¿Cuál fue la razón principal por la cual no utilizó los servicios del Sistema Único de Salud (SUS)? (NO NECESITABA) |
| `ms05_0508_L` | ¿Cuál fue la razón principal por la cual no utilizó los servicios del Sistema Único de Salud (SUS)? (NO SABE DONDE PRESTAN EL SERVICIO) |
| `ms05_0508_M` | ¿Cuál fue la razón principal por la cual no utilizó los servicios del Sistema Único de Salud (SUS)? (NO SOLUCIONAN PROBLEMA DE SALUD) |
| `ms05_0508_X` | ¿Cuál fue la razón principal por la cual no utilizó los servicios del Sistema Único de Salud (SUS)? (OTRA RAZÓN) |
| `ms05_0508_X_cod` | (ESPECIFIQUE) OTRA RAZÓN |
| `ms05_0509_A` | La atención de salud que recibió fué:(A) ¿Durante el embarazo? |
| `ms05_0509_B` | La atención de salud que recibió fué:(B) ¿En el parto? |
| `ms05_0509_C` | La atención de salud que recibió fué:(C) ¿Después del parto? |
| `ms05_0509_D` | La atención de salud que recibió fué:(D) ¿Cómo persona con discapacidad? |
| `ms05_0509_X` | La atención de salud que recibió fué:(X) ¿Otra causa? (ESPECIFIQUE) |
| `ms05_0509_X_cod` | (ESPECIFIQUE) OTRA CAUSA |
| `ms05_0510_A` | ¿En qué establecimiento de salud recibió esa atención? (PUESTO DE SALUD) |
| `ms05_0510_B` | ¿En qué establecimiento de salud recibió esa atención? (CENTRO DE SALUD AMBULATORIO) |
| `ms05_0510_C` | ¿En qué establecimiento de salud recibió esa atención? (CENTRO DE SALUD CON INTERNACION) |
| `ms05_0510_D` | ¿En qué establecimiento de salud recibió esa atención? (CENTRO DE SALUD INTEGRAL) |
| `ms05_0510_E` | ¿En qué establecimiento de salud recibió esa atención? (HOSPITAL DE SEGUNDO NIVEL) |
| `ms05_0510_F` | ¿En qué establecimiento de salud recibió esa atención? (HOSPITAL DE TERCER NIVEL) |
| `ms05_0510_G` | ¿En qué establecimiento de salud recibió esa atención? (HOSPITAL ESPECIALIZADO) |
| `ms05_0510_H` | ¿En qué establecimiento de salud recibió esa atención? (CAJA NACIONAL DE SALUD) |
| `ms05_0510_I` | ¿En qué establecimiento de salud recibió esa atención? (CAJA DE LA BANCA PRIVADA) |
| `ms05_0510_J` | ¿En qué establecimiento de salud recibió esa atención? (CAJA PETROLERA) |
| `ms05_0510_K` | ¿En qué establecimiento de salud recibió esa atención? (CAJA DE LA BANCA ESTATAL) |
| `ms05_0510_L` | ¿En qué establecimiento de salud recibió esa atención? (CORDES) |
| `ms05_0510_M` | ¿En qué establecimiento de salud recibió esa atención? (CAJA DE CAMINOS) |
| `ms05_0510_N` | ¿En qué establecimiento de salud recibió esa atención? (COSSMIL/FFAA) |
| `ms05_0510_O` | ¿En qué establecimiento de salud recibió esa atención? (SEGURO UNIVERSITARIO) |
| `ms05_0510_P` | ¿En qué establecimiento de salud recibió esa atención? (ORGANISMOS PRIVADOS (PRIMER NIVEL, SEGUNDO NIVEL, TERCER NIVEL)) |
| `ms05_0510_Q` | ¿En qué establecimiento de salud recibió esa atención? (IGLESIA (PRIMER NIVEL, SEGUNDO NIVEL, TERCER NIVEL)) |
| `ms05_0510_R` | ¿En qué establecimiento de salud recibió esa atención? (PROMOTOR DE LA SALUD/RPS/OTRO AGENTE) |
| `ms05_0510_S` | ¿En qué establecimiento de salud recibió esa atención? (VISITA DOMICILIARIA) |
| `ms05_0510_T` | ¿En qué establecimiento de salud recibió esa atención? (FARMACIA) |
| `ms05_0510_U` | ¿En qué establecimiento de salud recibió esa atención? (MEDICINA TRADICIONAL) |
| `ms05_0510_V` | ¿En qué establecimiento de salud recibió esa atención? (NO ACUDIÓ A NINGUN E.S./NO FUE) |
| `ms05_0510_X` | ¿En qué establecimiento de salud recibió esa atención? (OTRO LUGAR:) |
| `ms05_0510_Z` | ¿En qué establecimiento de salud recibió esa atención? (NO SABE) |
| `ms05_0510_X_cod` | (ESPECIFIQUE) OTRO LUGAR |
| `ms05_0511_A` | En la atención que recibió:(A) ¿Le solucionaron su problema de salud? |
| `ms05_0511_B` | En la atención que recibió:(B) ¿Le atendieron en su idioma? |
| `ms05_0511_C` | En la atención que recibió:(C) ¿Los médicos o enfermeras fueron amables con usted? |
| `ms05_0511_D` | En la atención que recibió:(D) ¿Tuvo que pagar por algo? |
| `ms05_0511_E` | En la atención que recibió:(E) ¿Le derivaron a otro establecimiento de salud? |
| `ms05_0512` | Desde enero de 2018, en algun momento alguna de sus hijas e hijos recibio atencion por el Sistema Único de Salud (SUS)? |
| `ms05_0513_A` | ¿Cuál fue la razón principal por la cual no utilizó los servicios del Sistema Único de Salud (SUS) para sus hijas e hijos? (TENÍA QUE ESPERAR MUCHO) |
| `ms05_0513_B` | ¿Cuál fue la razón principal por la cual no utilizó los servicios del Sistema Único de Salud (SUS) para sus hijas e hijos? (NO HABÍA DONDE ESPERAR/INCOMODO) |
| `ms05_0513_C` | ¿Cuál fue la razón principal por la cual no utilizó los servicios del Sistema Único de Salud (SUS) para sus hijas e hijos? (PERSONAL POCO AMABLE) |
| `ms05_0513_D` | ¿Cuál fue la razón principal por la cual no utilizó los servicios del Sistema Único de Salud (SUS) para sus hijas e hijos? (PERSONAL SIN EXPERIENCIA/NO CAPACITADO) |
| `ms05_0513_E` | ¿Cuál fue la razón principal por la cual no utilizó los servicios del Sistema Único de Salud (SUS) para sus hijas e hijos? (PERSONAL NUNCA DISPONIBLE) |
| `ms05_0513_F` | ¿Cuál fue la razón principal por la cual no utilizó los servicios del Sistema Único de Salud (SUS) para sus hijas e hijos? (EL LUGAR NO ESTABA LIMPIO) |
| `ms05_0513_G` | ¿Cuál fue la razón principal por la cual no utilizó los servicios del Sistema Único de Salud (SUS) para sus hijas e hijos? (EL LUGAR QUEDABA MUY LEJOS) |
| `ms05_0513_H` | ¿Cuál fue la razón principal por la cual no utilizó los servicios del Sistema Único de Salud (SUS) para sus hijas e hijos? (NO ABRIAN TODOS LOS DÍAS) |
| `ms05_0513_I` | ¿Cuál fue la razón principal por la cual no utilizó los servicios del Sistema Único de Salud (SUS) para sus hijas e hijos? (HORARIO DE ATENCIÓN INADECUADO) |
| `ms05_0513_J` | ¿Cuál fue la razón principal por la cual no utilizó los servicios del Sistema Único de Salud (SUS) para sus hijas e hijos? (NO TENIA DINERO) |
| `ms05_0513_K` | ¿Cuál fue la razón principal por la cual no utilizó los servicios del Sistema Único de Salud (SUS) para sus hijas e hijos? (NO NECESITE) |
| `ms05_0513_L` | ¿Cuál fue la razón principal por la cual no utilizó los servicios del Sistema Único de Salud (SUS) para sus hijas e hijos? (NO SABÍA DONDE PRESTABAN EL SERVICIO) |
| `ms05_0513_M` | ¿Cuál fue la razón principal por la cual no utilizó los servicios del Sistema Único de Salud (SUS) para sus hijas e hijos? (NO SOLUCIONABAN PROBLEMA DE SALUD) |
| `ms05_0513_X` | ¿Cuál fue la razón principal por la cual no utilizó los servicios del Sistema Único de Salud (SUS) para sus hijas e hijos? (OTRA RAZÓN) |
| `ms05_0513_X_cod` | (ESPECIFIQUE) OTRA RAZÓN |
| `ms05_0514` | ¿Cuántos de sus hijas e hijos recibieron atención por el Sistema Único de Salud (SUS)? |
| `ms05_0515_A` | La atención que recibieron fue:(A)¿Por enfermedad? |
| `ms05_0515_B` | La atención que recibieron fue:(B)¿Por accidente? |
| `ms05_0515_C` | La atención que recibieron fue:(C)¿Para seguimiento de control y desarrollo (incluye vacunas)? |
| `ms05_0515_X` | La atención que recibieron fue:(X) Otro motivo (ESPECIFIQUE) |
| `ms05_0515_X_cod` | (ESPECIFIQUE) OTRO MOTIVO |
| `ms05_0516_A` | ¿En qué establecimiento de salud recibieron esa atención? (PUESTO DE SALUD) |
| `ms05_0516_B` | ¿En qué establecimiento de salud recibieron esa atención? (CENTRO DE SALUD AMBULATORIO) |
| `ms05_0516_C` | ¿En qué establecimiento de salud recibieron esa atención? (CENTRO DE SALUD CON INTERNACION) |
| `ms05_0516_D` | ¿En qué establecimiento de salud recibieron esa atención? (CENTRO DE SALUD INTEGRAL) |
| `ms05_0516_E` | ¿En qué establecimiento de salud recibieron esa atención? (HOSPITAL DE SEGUNDO NIVEL) |
| `ms05_0516_F` | ¿En qué establecimiento de salud recibieron esa atención? (HOSPITAL DE TERCER NIVEL) |
| `ms05_0516_G` | ¿En qué establecimiento de salud recibieron esa atención? (HOSPITAL ESPECIALIZADO) |
| `ms05_0516_H` | ¿En qué establecimiento de salud recibieron esa atención? (CAJA NACIONAL DE SALUD) |
| `ms05_0516_I` | ¿En qué establecimiento de salud recibieron esa atención? (CAJA DE LA BANCA PRIVADA) |
| `ms05_0516_J` | ¿En qué establecimiento de salud recibieron esa atención? (CAJA PETROLERA) |
| `ms05_0516_K` | ¿En qué establecimiento de salud recibieron esa atención? (CAJA DE LA BANCA ESTATAL) |
| `ms05_0516_L` | ¿En qué establecimiento de salud recibieron esa atención? (CORDES) |
| `ms05_0516_M` | ¿En qué establecimiento de salud recibieron esa atención? (CAJA DE CAMINOS) |
| `ms05_0516_N` | ¿En qué establecimiento de salud recibieron esa atención? (COSSMIL/FFAA) |
| `ms05_0516_O` | ¿En qué establecimiento de salud recibieron esa atención? (SEGURO UNIVERSITARIO) |
| `ms05_0516_P` | ¿En qué establecimiento de salud recibieron esa atención? (ORGANISMOS PRIVADOS (PRIMER NIVEL, SEGUNDO NIVEL, TERCER NIVEL)) |
| `ms05_0516_Q` | ¿En qué establecimiento de salud recibieron esa atención? (IGLESIA (PRIMER NIVEL, SEGUNDO NIVEL, TERCER NIVEL)) |
| `ms05_0516_R` | ¿En qué establecimiento de salud recibieron esa atención? (PROMOTOR DE LA SALUD/RPS/OTRO AGENTE) |
| `ms05_0516_S` | ¿En qué establecimiento de salud recibieron esa atención? (VISITA DOMICILIARIA) |
| `ms05_0516_T` | ¿En qué establecimiento de salud recibieron esa atención? (FARMACIA) |
| `ms05_0516_U` | ¿En qué establecimiento de salud recibieron esa atención? (MEDICINA TRADICIONAL) |
| `ms05_0516_V` | ¿En qué establecimiento de salud recibieron esa atención? (NO ACUDIÓ A NINGUN E.S./NO FUE) |
| `ms05_0516_X` | ¿En qué establecimiento de salud recibieron esa atención? (OTRO LUGAR:) |
| `ms05_0516_Z` | ¿En qué establecimiento de salud recibieron esa atención? (NO SABE) |
| `ms05_0516_X_cod` | (ESPECIFIQUE) OTRO LUGAR |
| `ms05_0517_A` | En la atención que recibieron sus hijas e hijos:(A) ¿Solucionaron el problema de salud de sus hijas/os? |
| `ms05_0517_B` | En la atención que recibieron sus hijas e hijos:(B) ¿Le atendieron en su idioma? |
| `ms05_0517_C` | En la atención que recibieron sus hijas e hijos:(C) ¿Los médicos o enfermeras fueron amables con sus hijas/os? |
| `ms05_0517_D` | En la atención que recibieron sus hijas e hijos:(D) ¿Tuvo que pagar por algo? |
| `ms05_0519` | ¿Cómo calificaría la atención que recibió usted o sus hijas/os del Sistema Único de Salud (SUS): buena, regular o mala? |
| `ms05_0520_A` | ¿Cuáles son las razones por las que califica la atención como regular/ mala del Sistema Único de Salud (SUS)? (TENÍA QUE ESPERAR MUCHO) |
| `ms05_0520_B` | ¿Cuáles son las razones por las que califica la atención como regular/ mala del Sistema Único de Salud (SUS)? (NO HABÍA DONDE ESPERAR/INCÓMODO) |
| `ms05_0520_C` | ¿Cuáles son las razones por las que califica la atención como regular/ mala del Sistema Único de Salud (SUS)? (PERSONAL POCO AMABLE) |
| `ms05_0520_D` | ¿Cuáles son las razones por las que califica la atención como regular/ mala del Sistema Único de Salud (SUS)? (PERSONAL SIN EXPERIENCIA/NO CAPACITADO) |
| `ms05_0520_E` | ¿Cuáles son las razones por las que califica la atención como regular/ mala del Sistema Único de Salud (SUS)? (PERSONAL NUNCA DISPONIBLE) |
| `ms05_0520_F` | ¿Cuáles son las razones por las que califica la atención como regular/ mala del Sistema Único de Salud (SUS)? (EL LUGAR NO ERA LIMPIO) |
| `ms05_0520_G` | ¿Cuáles son las razones por las que califica la atención como regular/ mala del Sistema Único de Salud (SUS)? (EL CENTRO DE SALUD ES LEJOS) |
| `ms05_0520_H` | ¿Cuáles son las razones por las que califica la atención como regular/ mala del Sistema Único de Salud (SUS)? (NO SOLUCIONAN PROBLEMA DE SALUD) |
| `ms05_0520_I` | ¿Cuáles son las razones por las que califica la atención como regular/ mala del Sistema Único de Salud (SUS)? (HAY QUE COMPRAR MEDICAMENTOS Y/O EXÁMENES DE LABORATORIOS U OTROS) |
| `ms05_0520_J` | ¿Cuáles son las razones por las que califica la atención como regular/ mala del Sistema Único de Salud (SUS)? (TIENE QUE PAGAR) |
| `ms05_0520_K` | ¿Cuáles son las razones por las que califica la atención como regular/ mala del Sistema Único de Salud (SUS)? (MÉDICO RECOMIENDA CONSULTA PRIVADA) |
| `ms05_0520_X` | ¿Cuáles son las razones por las que califica la atención como regular/ mala del Sistema Único de Salud (SUS)? (OTRA) |
| `ms05_0520_X_cod` | (ESPECIFIQUE) OTRA |
| `ms05_0521` | ¿Usted cuenta con algún otro tipo de seguro de salud que no sea el SUS? |
| `ms05_0522_A` | ¿Qué tipo de seguro de salud tiene usted? (CAJA DE SALUD) |
| `ms05_0522_B` | ¿Qué tipo de seguro de salud tiene usted? (SEGURO PRIVADO) |
| `ms05_0522_X` | ¿Qué tipo de seguro de salud tiene usted? (OTRO:) |
| `ms05_0522_X_cod` | (ESPECIFIQUE) OTRO |
| `ms05_0523_A` | ¿Usted ha recibido el bono Juana Azurduy,(A) Por atención a su persona? |
| `ms05_0523_B` | ¿Usted ha recibido el bono Juana Azurduy,(B) Por atención a sus niñas/niños? |
| `ms06_0601` | ¿Actualmente, esta usted casada o vive en unión con: |
| `ms06_0602` | ¿Ha estado usted casada o unida alguna vez aunque haya sido por poco tiempo? |
| `ms06_0603` | ¿Cuál es su estado civil actual: viuda, separada o divorciada? |
| `ms06_0604` | ¿Su esposo/compañero vive actualmente con usted o vive en alguna otra parte? |
| `ms06_0605` | NÚMERO DE ORDEN DEL ESPOSO/ COMPAÑERO |
| `ms06_0606` | ¿Ha estado usted casada o en unión solo una vez o más de una vez? |
| `ms06_0607_01_1` | ¿En qué mes comenzó a vivir con su esposo o compañero? |
| `ms06_0607_01_2` | ¿En qué año comenzó a vivir con su esposo o compañero? |
| `ms06_0607_02_1` | ¿En qué mes empezó a vivir con su primer esposo o compañero? |
| `ms06_0607_02_2` | ¿En qué año empezó a vivir con su primer esposo o compañero? |
| `ms06_0608` | ¿Cuantos años cumplidos tenia usted cuando empezó a vivir con su esposo/ compañero? (EDAD) |
| `ms06_0610` | ¿Cuántos años tenia usted cuando tuvo su primera relación sexual (si ha tenido)?SI NUNCA HA TENIDO, OPRIMA "00"CUANDO SE CASÓ/UNIÓ, OPRIMA "95" |
| `ms06_0610_a` | ¿Qué edad tenía su pareja? |
| `ms06_0610_b` | ¿Esa relación sexual tenía su consentimiento? |
| `ms06_0612` | La primera vez que tuvo relaciones sexuales, ¿usaron condon? |
| `ms06_0613` | ¿Cuándo fue la última vez que tuvo relaciones sexuales?SI MENOS DE 12 MESES, REGISTRE RESPUESTA EN DIAS, SEMANAS O MESES.SI 12 MESES (1 AÑO) O MÁS, REGISTRE LA RESPUESTA EN AÑOS. |
| `ms06_0613_1` | ¿Cuándo fue la última vez que tuvo relaciones sexuales? (DÍAS) |
| `ms06_0613_2` | ¿Cuándo fue la última vez que tuvo relaciones sexuales? (SEMANAS) |
| `ms06_0613_3` | ¿Cuándo fue la última vez que tuvo relaciones sexuales? (MESES) |
| `ms06_0613_4` | ¿Cuándo fue la última vez que tuvo relaciones sexuales? (AÑOS) |
| `ms06_0614` | En total ¿Con cuántas personas diferentes ha tenido relaciones sexuales durante toda su vida? |
| `ms06_0615_A` | En esta época se habla más abiertamente de las relaciones sexuales entre personas del mismo sexo.¿Usted, ha tenido relaciones sexuales alguna vez con:(A) Mujer? |
| `ms06_0615_B` | En esta época se habla más abiertamente de las relaciones sexuales entre personas del mismo sexo.¿Usted, ha tenido relaciones sexuales alguna vez con:(B) Hombre y Mujer? |
| `ms06_0616` | ¿Sabe de algún lugar donde se puedan conseguir condones ? |
| `ms06_0617_A` | ¿Cuál es ese lugar? (PUESTO DE SALUD) |
| `ms06_0617_B` | ¿Cuál es ese lugar? (CENTRO DE SALUD AMBULATORIO) |
| `ms06_0617_C` | ¿Cuál es ese lugar? (CENTRO DE SALUD CON INTERNACION) |
| `ms06_0617_D` | ¿Cuál es ese lugar? (CENTRO DE SALUD INTEGRAL) |
| `ms06_0617_E` | ¿Cuál es ese lugar? (HOSPITAL DE SEGUNDO NIVEL) |
| `ms06_0617_F` | ¿Cuál es ese lugar? (HOSPITAL DE TERCER NIVEL) |
| `ms06_0617_G` | ¿Cuál es ese lugar? (HOSPITAL ESPECIALIZADO) |
| `ms06_0617_H` | ¿Cuál es ese lugar? (CAJA NACIONAL DE SALUD) |
| `ms06_0617_I` | ¿Cuál es ese lugar? (CAJA DE LA BANCA PRIVADA) |
| `ms06_0617_J` | ¿Cuál es ese lugar? (CAJA PETROLERA) |
| `ms06_0617_K` | ¿Cuál es ese lugar? (CAJA DE LA BANCA ESTATAL) |
| `ms06_0617_L` | ¿Cuál es ese lugar? (CORDES) |
| `ms06_0617_M` | ¿Cuál es ese lugar? (CAJA DE CAMINOS) |
| `ms06_0617_N` | ¿Cuál es ese lugar? (COSSMIL/FFAA) |
| `ms06_0617_O` | ¿Cuál es ese lugar? (SEGURO UNIVERSITARIO) |
| `ms06_0617_P` | ¿Cuál es ese lugar? (ORGANISMOS PRIVADOS (PRIMER NIVEL, SEGUNDO NIVEL, TERCER NIVEL)) |
| `ms06_0617_Q` | ¿Cuál es ese lugar? (IGLESIA (PRIMER NIVEL, SEGUNDO NIVEL, TERCER NIVEL)) |
| `ms06_0617_R` | ¿Cuál es ese lugar? (PROMOTOR DE LA SALUD/RPS/OTRO AGENTE) |
| `ms06_0617_S` | ¿Cuál es ese lugar? (VISITA DOMICILIARIA) |
| `ms06_0617_T` | ¿Cuál es ese lugar? (FARMACIA) |
| `ms06_0617_U` | ¿Cuál es ese lugar? (MEDICINA TRADICIONAL) |
| `ms06_0617_V` | ¿Cuál es ese lugar? (NO ACUDIÓ A NINGUN E.S./NO FUE) |
| `ms06_0617_X` | ¿Cuál es ese lugar? (OTRO LUGAR:) |
| `ms06_0617_Z` | ¿Cuál es ese lugar? (NO SABE) |
| `ms06_0617_X_cod` | (ESPECIFIQUE) OTRO LUGAR |
| `ms06_0618` | Si usted quisiera ¿Podría conseguir condón usted misma? |
| `ms06_0619` | ¿Puede usted decir "no" a su esposo/compañero si no quiere tener relaciones sexuales? |
| `ms07_0702_01` | Ahora tengo algunas preguntas acerca del futuro. ¿Le gustaría tener una/un (otra/o) hija/o o preferiría no tener ningún (más) hija/o(s)? |
| `ms07_0702_02` | Ahora tengo algunas preguntas acerca del futuro. ¿Después del hijo que está esperando, Le gustaría tener otra/o hija o hijo preferiría NO tener más hijas/os? |
| `ms07_0703_01` | ¿Cuanto tiempo le gustaria esperar desde ahora hasta antes del nacimiento de(una/un otra/o) hija/o? |
| `ms07_0703_01_01` | ¿Cuanto tiempo le gustaria esperar desde ahora hasta antes del nacimiento de(una/un otra/o) hija/o? (MESES) |
| `ms07_0703_01_02` | ¿Cuanto tiempo le gustaria esperar desde ahora hasta antes del nacimiento de(una/un otra/o) hija/o? (AÑOS) |
| `ms07_0703_cod` | (ESPECIFIQUE) OTRO |
| `ms07_0703_02` | ¿Cuanto tiempo le gustaria esperar hasta antes del nacimiento de otra/o hija/o? |
| `ms07_0703_02_01` | Después del nacimiento de la hija/o que está esperando, ¿Cuánto tiempo le gustaría esperar hasta antes del nacimiento de otra/o hija/o? (MESES) |
| `ms07_0703_02_02` | Después del nacimiento de la hija/o que está esperando, ¿Cuánto tiempo le gustaría esperar hasta antes del nacimiento de otra/o hija/o? (AÑOS) |
| `ms07_0703_2_cod` | ESPECIFIQUE PARA OTRO |
| `ms07_0707_01_A` | Usted dice que no quiere tener una/un (otra/o) hija/o pronto, pero ud. no está usando ningún método para evitar quedar embarazada,¿Me podría decir por qué no está usando un método?¿Alguna otra razón? (NO EN UNIÓN) |
| `ms07_0707_01_B` | Usted dice que no quiere tener una/un (otra/o) hija/o pronto, pero ud. no está usando ningún método para evitar quedar embarazada,¿Me podría decir por qué no está usando un método?¿Alguna otra razón? (NO TIENE REL. SEXUALES) |
| `ms07_0707_01_C` | Usted dice que no quiere tener una/un (otra/o) hija/o pronto, pero ud. no está usando ningún método para evitar quedar embarazada,¿Me podría decir por qué no está usando un método?¿Alguna otra razón? (SEXO POCO FRECUENTE) |
| `ms07_0707_01_D` | Usted dice que no quiere tener una/un (otra/o) hija/o pronto, pero ud. no está usando ningún método para evitar quedar embarazada,¿Me podría decir por qué no está usando un método?¿Alguna otra razón? (MENOPAUSIA/ HISTERECTOMIZADA) |
| `ms07_0707_01_E` | Usted dice que no quiere tener una/un (otra/o) hija/o pronto, pero ud. no está usando ningún método para evitar quedar embarazada,¿Me podría decir por qué no está usando un método?¿Alguna otra razón? (INFERTILIDAD MUJER) |
| `ms07_0707_01_F` | Usted dice que no quiere tener una/un (otra/o) hija/o pronto, pero ud. no está usando ningún método para evitar quedar embarazada,¿Me podría decir por qué no está usando un método?¿Alguna otra razón? (INFERTILIDAD HOMBRE) |
| `ms07_0707_01_G` | Usted dice que no quiere tener una/un (otra/o) hija/o pronto, pero ud. no está usando ningún método para evitar quedar embarazada,¿Me podría decir por qué no está usando un método?¿Alguna otra razón? (AMENORREA POSTPARTO) |
| `ms07_0707_01_H` | Usted dice que no quiere tener una/un (otra/o) hija/o pronto, pero ud. no está usando ningún método para evitar quedar embarazada,¿Me podría decir por qué no está usando un método?¿Alguna otra razón? (LACTANCIA) |
| `ms07_0707_01_I` | Usted dice que no quiere tener una/un (otra/o) hija/o pronto, pero ud. no está usando ningún método para evitar quedar embarazada,¿Me podría decir por qué no está usando un método?¿Alguna otra razón? (ENTREVISTADA SE OPONE) |
| `ms07_0707_01_J` | Usted dice que no quiere tener una/un (otra/o) hija/o pronto, pero ud. no está usando ningún método para evitar quedar embarazada,¿Me podría decir por qué no está usando un método?¿Alguna otra razón? (MARIDO SE OPONE) |
| `ms07_0707_01_K` | Usted dice que no quiere tener una/un (otra/o) hija/o pronto, pero ud. no está usando ningún método para evitar quedar embarazada,¿Me podría decir por qué no está usando un método?¿Alguna otra razón? (OTROS SE OPONEN) |
| `ms07_0707_01_L` | Usted dice que no quiere tener una/un (otra/o) hija/o pronto, pero ud. no está usando ningún método para evitar quedar embarazada,¿Me podría decir por qué no está usando un método?¿Alguna otra razón? (PROHIBICIÓN RELIGIOSA) |
| `ms07_0707_01_M` | Usted dice que no quiere tener una/un (otra/o) hija/o pronto, pero ud. no está usando ningún método para evitar quedar embarazada,¿Me podría decir por qué no está usando un método?¿Alguna otra razón? (NO CONOCE MÉTODOS) |
| `ms07_0707_01_N` | Usted dice que no quiere tener una/un (otra/o) hija/o pronto, pero ud. no está usando ningún método para evitar quedar embarazada,¿Me podría decir por qué no está usando un método?¿Alguna otra razón? (NO SABE DONDE CONSEGUIRLO) |
| `ms07_0707_01_O` | Usted dice que no quiere tener una/un (otra/o) hija/o pronto, pero ud. no está usando ningún método para evitar quedar embarazada,¿Me podría decir por qué no está usando un método?¿Alguna otra razón? (RAZONES DE SALUD) |
| `ms07_0707_01_P` | Usted dice que no quiere tener una/un (otra/o) hija/o pronto, pero ud. no está usando ningún método para evitar quedar embarazada,¿Me podría decir por qué no está usando un método?¿Alguna otra razón? (MIEDO A EFECTOS SECUNDARIOS) |
| `ms07_0707_01_Q` | Usted dice que no quiere tener una/un (otra/o) hija/o pronto, pero ud. no está usando ningún método para evitar quedar embarazada,¿Me podría decir por qué no está usando un método?¿Alguna otra razón? (USO INCONVENIENTE) |
| `ms07_0707_01_R` | Usted dice que no quiere tener una/un (otra/o) hija/o pronto, pero ud. no está usando ningún método para evitar quedar embarazada,¿Me podría decir por qué no está usando un método?¿Alguna otra razón? (INTERFIERE CON PROCESOS NORMALES DEL CUERPO) |
| `ms07_0707_01_S` | Usted dice que no quiere tener una/un (otra/o) hija/o pronto, pero ud. no está usando ningún método para evitar quedar embarazada,¿Me podría decir por qué no está usando un método?¿Alguna otra razón? (FALTA DE ACCESO/ DEMASIADO LEJOS) |
| `ms07_0707_01_T` | Usted dice que no quiere tener una/un (otra/o) hija/o pronto, pero ud. no está usando ningún método para evitar quedar embarazada,¿Me podría decir por qué no está usando un método?¿Alguna otra razón? (MUY COSTOSO) |
| `ms07_0707_01_X` | Usted dice que no quiere tener una/un (otra/o) hija/o pronto, pero ud. no está usando ningún método para evitar quedar embarazada,¿Me podría decir por qué no está usando un método?¿Alguna otra razón? (OTRA:) |
| `ms07_0707_01_Z` | Usted dice que no quiere tener una/un (otra/o) hija/o pronto, pero ud. no está usando ningún método para evitar quedar embarazada,¿Me podría decir por qué no está usando un método?¿Alguna otra razón? (NO SABE) |
| `ms07_0707_X_cod` | (ESPECIFIQUE) OTRA |
| `ms07_0707_02_A` | Usted me dijo que no quería tener (más) hijas/os, pero usted no está usando ningún método para evitar quedar embarazada.¿Me podria decir por qué no está usando un método?¿Alguna otra razón? (NO EN UNIÓN) |
| `ms07_0707_02_B` | Usted me dijo que no quería tener (más) hijas/os, pero usted no está usando ningún método para evitar quedar embarazada.¿Me podria decir por qué no está usando un método?¿Alguna otra razón? (NO TIENE REL. SEXUALES) |
| `ms07_0707_02_C` | Usted me dijo que no quería tener (más) hijas/os, pero usted no está usando ningún método para evitar quedar embarazada.¿Me podria decir por qué no está usando un método?¿Alguna otra razón? (SEXO POCO FRECUENTE) |
| `ms07_0707_02_D` | Usted me dijo que no quería tener (más) hijas/os, pero usted no está usando ningún método para evitar quedar embarazada.¿Me podria decir por qué no está usando un método?¿Alguna otra razón? (MENOPAUSIA/ HISTERECTOMIZADA) |
| `ms07_0707_02_E` | Usted me dijo que no quería tener (más) hijas/os, pero usted no está usando ningún método para evitar quedar embarazada.¿Me podria decir por qué no está usando un método?¿Alguna otra razón? (INFERTILIDAD MUJER) |
| `ms07_0707_02_F` | Usted me dijo que no quería tener (más) hijas/os, pero usted no está usando ningún método para evitar quedar embarazada.¿Me podria decir por qué no está usando un método?¿Alguna otra razón? (INFERTILIDAD HOMBRE) |
| `ms07_0707_02_G` | Usted me dijo que no quería tener (más) hijas/os, pero usted no está usando ningún método para evitar quedar embarazada.¿Me podria decir por qué no está usando un método?¿Alguna otra razón? (AMENORREA POSTPARTO) |
| `ms07_0707_02_H` | Usted me dijo que no quería tener (más) hijas/os, pero usted no está usando ningún método para evitar quedar embarazada.¿Me podria decir por qué no está usando un método?¿Alguna otra razón? (LACTANCIA) |
| `ms07_0707_02_I` | Usted me dijo que no quería tener (más) hijas/os, pero usted no está usando ningún método para evitar quedar embarazada.¿Me podria decir por qué no está usando un método?¿Alguna otra razón? (ENTREVISTADA SE OPONE) |
| `ms07_0707_02_J` | Usted me dijo que no quería tener (más) hijas/os, pero usted no está usando ningún método para evitar quedar embarazada.¿Me podria decir por qué no está usando un método?¿Alguna otra razón? (MARIDO SE OPONE) |
| `ms07_0707_02_K` | Usted me dijo que no quería tener (más) hijas/os, pero usted no está usando ningún método para evitar quedar embarazada.¿Me podria decir por qué no está usando un método?¿Alguna otra razón? (OTROS SE OPONEN) |
| `ms07_0707_02_L` | Usted me dijo que no quería tener (más) hijas/os, pero usted no está usando ningún método para evitar quedar embarazada.¿Me podria decir por qué no está usando un método?¿Alguna otra razón? (PROHIBICIÓN RELIGIOSA) |
| `ms07_0707_02_M` | Usted me dijo que no quería tener (más) hijas/os, pero usted no está usando ningún método para evitar quedar embarazada.¿Me podria decir por qué no está usando un método?¿Alguna otra razón? (NO CONOCE MÉTODOS) |
| `ms07_0707_02_N` | Usted me dijo que no quería tener (más) hijas/os, pero usted no está usando ningún método para evitar quedar embarazada.¿Me podria decir por qué no está usando un método?¿Alguna otra razón? (NO SABE DONDE CONSEGUIRLO) |
| `ms07_0707_02_O` | Usted me dijo que no quería tener (más) hijas/os, pero usted no está usando ningún método para evitar quedar embarazada.¿Me podria decir por qué no está usando un método?¿Alguna otra razón? (RAZONES DE SALUD) |
| `ms07_0707_02_P` | Usted me dijo que no quería tener (más) hijas/os, pero usted no está usando ningún método para evitar quedar embarazada.¿Me podria decir por qué no está usando un método?¿Alguna otra razón? (MIEDO A EFECTOS SECUNDARIOS) |
| `ms07_0707_02_Q` | Usted me dijo que no quería tener (más) hijas/os, pero usted no está usando ningún método para evitar quedar embarazada.¿Me podria decir por qué no está usando un método?¿Alguna otra razón? (USO INCONVENIENTE) |
| `ms07_0707_02_R` | Usted me dijo que no quería tener (más) hijas/os, pero usted no está usando ningún método para evitar quedar embarazada.¿Me podria decir por qué no está usando un método?¿Alguna otra razón? (INTERFIERE CON PROCESOS NORMALES DEL CUERPO) |
| `ms07_0707_02_S` | Usted me dijo que no quería tener (más) hijas/os, pero usted no está usando ningún método para evitar quedar embarazada.¿Me podria decir por qué no está usando un método?¿Alguna otra razón? (FALTA DE ACCESO/ DEMASIADO LEJOS) |
| `ms07_0707_02_T` | Usted me dijo que no quería tener (más) hijas/os, pero usted no está usando ningún método para evitar quedar embarazada.¿Me podria decir por qué no está usando un método?¿Alguna otra razón? (MUY COSTOSO) |
| `ms07_0707_02_X` | Usted me dijo que no quería tener (más) hijas/os, pero usted no está usando ningún método para evitar quedar embarazada.¿Me podria decir por qué no está usando un método?¿Alguna otra razón? (OTRA:) |
| `ms07_0707_02_Z` | Usted me dijo que no quería tener (más) hijas/os, pero usted no está usando ningún método para evitar quedar embarazada.¿Me podria decir por qué no está usando un método?¿Alguna otra razón? (NO SABE) |
| `ms07_0707_2_X_cod` | (ESPECIFIQUE) OTRA |
| `ms07_0709` | ¿Usted cree que en el futuro usará algún método para evitar quedar embarazada? |
| `ms07_0710` | ¿Qué método le gustaria usar? |
| `ms07_0710_cod` | (ESPECIFIQUE) OTRO METODO |
| `ms07_0711` | ¿Cuál es la razón principal por la que usted no piensa usar ningún método en el futuro? |
| `ms07_0711_cod` | (ESPECIFIQUE) OTRA: |
| `ms07_0713` | ¿Si estuviera casada o en unión, usaría algún método? |
| `ms07_0714_01` | Si usted pudiera volver a la época en que todavía no tenía hijas/os y pudiera elegir exactamente el número de hijas/os que tendría en toda su vida, ¿cuántos serían? |
| `ms07_0714_02` | Si usted pudiera elegir exactamente el número de hijas/os que tendría en toda su vida, ¿cuántos serían? |
| `ms07_0715` | ¿Cuántas/os de estas/os hijas/os le habría gustado que fueran mujeres y cuántos varones, y para cuántos no le importaría el sexo? |
| `ms07_0715_01` | ¿Cuántos de estos hijos le habría gustado que fueran hombres? (NÚMERO DE HOMBRES) |
| `ms07_0715_02` | ¿Cuántos de estos hijos le habría gustado que fueran mujeres? (NÚMERO DE MUJERES) |
| `ms07_0715_03` | ¿Cuántos de estos hijos no le importaría el sexo? (NÚMERO DE CUALQUIER SEXO) |
| `ms07_0715_04` | (ESPECIFIQUE) OTRA RESPUESTA |
| `ms07_0716_A` | Durante los últimos 12 meses:(A) ¿Usted ha escuchado en la RADIO algo sobre anticoncepción/planificación familiar? |
| `ms07_0716_B` | Durante los últimos 12 meses:(B) ¿Usted ha visto en la TELEVISIÓN algo sobre anticoncepción/planificación familiar? |
| `ms07_0716_C` | Durante los últimos 12 meses:(C) ¿Usted ha leído en PERIÓDICOS o REVISTAS algo sobre anticoncepción/planificación familiar? |
| `ms07_0716_D` | Durante los últimos 12 meses:(D) ¿Usted ha visto en INTERNET algo sobre anticoncepción/planificación familiar? |
| `ms07_0716_X` | Durante los últimos 12 meses:(X) OTROS (ESPECIFIQUE) |
| `ms07_0716_cod` | (ESPECIFIQUE) OTROS |
| `ms07_0719` | ¿Su esposo/compañero sabe que usted está usando un método de anticoncepción/ planificación familiar? |
| `ms07_0720` | ¿Usted diría que el uso de anticoncepción/ planificación familiar fue principalmente su decisión, principalmente de su pareja (esposo/compañero) o lo decidieron juntos? |
| `ms07_0720_cod` | (ESPECIFIQUE) OTRA |
| `ms07_0722` | ¿Usted piensa que su pareja (esposo/ compañero) desea el mismo número de hijas/os que usted quiere, o él quiere más o menos que usted? |
| `ms08_0802` | ¿Cuántos años cumplidos tiene su pareja (esposo/compañero)? (EDAD EN AÑOS CUMPLIDOS) |
| `ms08_0803` | ¿Su (última) pareja (esposo/ compañero) alguna vez asistió a la escuela o curso de alfabetización? |
| `ms08_0804_01` | ¿Cuál fue el curso o año de educación más alto que su pareja (esposo/compañero) aprobó y en qué nivel? (NIVEL) |
| `ms08_0804_02` | ¿Cuál fue el curso o año de educación más alto que su pareja (esposo/compañero) aprobó? (CURSO) |
| `ms08_0806` | Durante la semana pasada su pareja (esposo/compañero), ¿trabajó al menos una hora o estuvo ausente debido a permisos, vacaciones u otra razón? |
| `ms08_0807` | Principalmente, ¿su pareja es estudiante, responsable de labores/tareas del hogar, jubilado o benemérito, enfermo o, persona con discapacidad o persona de edad avanzada? |
| `ms08_0807_cod` | (ESPECIFIQUE) OTRO |
| `ms08_0808_cod23` | Codigo COB 2023 |
| `ms08_0809` | Durante la semana pasada, ¿Usted trabajó al menos una hora o estuvo ausente debido a permisos, vacaciones, maternidad u otra razón? |
| `ms08_0810` | Durante la semana pasada, ¿Usted que gestiones hizo para buscar trabajo? |
| `ms08_0811` | ¿Es usted estudiante, ama de casa o responsable del hogar, jubilada o benemérita, enferma o persona con discapacidad, o persona de edad avanzada? |
| `ms08_0811_cod` | (ESPECIFIQUE) OTRO |
| `ms08_0812_cod23` | Codigo COB 2023 |
| `ms08_0813` | TRABAJA(BA) EN ACTIVIDADES AGROPECUARIAS/FORESTALES |
| `ms08_0814` | ¿Usted trabaja(ba) en tierra propia, en tierra de su familia, en tierra arrendada o trabaja(ba) en la tierra de otra persona? |
| `ms08_0815` | ¿Hace (hacia) usted ese trabajo para alguien de su familia, para otra persona o trabaja(ba) por cuenta propia? |
| `ms08_0816` | ¿Usted usualmente trabaja en el hogar o fuera del hogar? |
| `ms08_0817` | ¿Trabaja(ba) usted generalmente todo el año, por épocas o de vez en cuando? |
| `ms08_0818` | ¿A usted le pagan (pagaban) en dinero o en especie por el trabajo que realiza(ba) o no le pagan (pagaban)? |
| `ms08_0819` | ¿Durante los últimos 12 meses, cuántos meses trabajó usted? (NÚMERO DE MESES) |
| `ms08_0822` | Quién decide cómo se utiliza el dinero que usted gana:¿Usted, principalmente su pareja (esposo/compañero), o es una decisión conjunta? |
| `ms08_0822_cod` | (ESPECIFIQUE) OTRA PERSONA |
| `ms08_0823` | ¿Usted diria que el dinero que usted gana es más de lo que gana su pareja (esposo/compañero), menos de lo que él gana, o más o menos lo mismo? |
| `ms08_0824` | ¿Quién decide cómo se utiliza el dinero que su pareja (esposo/compañero) gana: principalmente usted, su pareja (esposo/compañero), o es una decisión conjunta? |
| `ms08_0824_cod` | (ESPECIFIQUE) OTRA PERSONA |
| `ms08_0825_A` | Para cada una de las siguientes actividades, ¿me puede decir quién tiene la última palabra en su casa: Usted, su pareja (esposo/compañero), ambos o alguien más.CUIDADO SALUD |
| `ms08_0825_B` | Para cada una de las siguientes actividades, ¿me puede decir quién tiene la última palabra en su casa: Usted, su pareja (esposo/compañero), ambos o alguien más.COMPRA CARO |
| `ms08_0825_C` | Para cada una de las siguientes actividades, ¿me puede decir quién tiene la última palabra en su casa: Usted, su pareja (esposo/compañero), ambos o alguien más.COMPRA DIARIA |
| `ms08_0825_D` | Para cada una de las siguientes actividades, ¿me puede decir quién tiene la última palabra en su casa: Usted, su pareja (esposo/compañero), ambos o alguien más.VISITAS AMIGAS/ FLIA |
| `ms08_0826_A_1` | El año pasado 2022 ¿Ha sufrido algun tipo de accidente en la ciudad:(A) Accidente de tránsito? |
| `ms08_0826_B_1` | El año pasado 2022 ¿Ha sufrido algun tipo de accidente en la ciudad:(B) Accidente doméstico / dentro del hogar? |
| `ms08_0826_C_1` | El año pasado 2022 ¿Ha sufrido algun tipo de accidente en la ciudad:(C) Accidente deportivo? |
| `ms08_0826_D_1` | El año pasado 2022 ¿Ha sufrido algun tipo de accidente en la ciudad:(D) Accidente en el trabajo? |
| `ms08_0826_E_1` | El año pasado 2022 ¿Ha sufrido algun tipo de accidente en la ciudad:(E) Accidente en desastre natural? |
| `ms08_0826_F_1` | El año pasado 2022 ¿Ha sufrido algun tipo de accidente en la ciudad:(F) Accidente en alguna convulsión social? |
| `ms08_0826_X_1` | El año pasado 2022 ¿Ha sufrido algun tipo de accidente en la ciudad:(X) ¿Accidente en OTRO TIPO DE ACCIDENTE (ESPECIFIQUE)? |
| `ms08_0826_X_1_cod` | (ESPECIFIQUE) (X) OTRO TIPO DE ACCIDENTE |
| `ms08_0826_A_2` | El año pasado 2022 ¿Ha sufrido algun tipo de accidente en el campo:(A) Accidente de tránsito? |
| `ms08_0826_B_2` | El año pasado 2022 ¿Ha sufrido algun tipo de accidente en el campo:(B) Accidente doméstico / dentro del hogar? |
| `ms08_0826_C_2` | El año pasado 2022 ¿Ha sufrido algun tipo de accidente en el campo: (C) Accidente deportivo? |
| `ms08_0826_D_2` | El año pasado 2022 ¿Ha sufrido algun tipo de accidente en el campo:(D) Accidente en el trabajo? |
| `ms08_0826_E_2` | El año pasado 2022 ¿Ha sufrido algun tipo de accidente en el campo:(E) Accidente en desastre natural? |
| `ms08_0826_F_2` | El año pasado 2022 ¿Ha sufrido algun tipo de accidente en el campo:(F) Accidente en alguna convulsión social? |
| `ms08_0826_X_2` | El año pasado 2022 ¿Ha sufrido algun tipo de accidente en el campo:(X) ¿Accidente en OTRO TIPO DE ACCIDENTE (ESPECIFIQUE)? |
| `ms08_0826_X_2_cod` | (ESPECIFIQUE) (X) OTRO TIPO DE ACCIDENTE |
| `ms08_0828_A` | Si tuvo un accidente de trabajo, ¿Quién cubrió los gastos incurridos:SEGURIDAD SOCIAL |
| `ms08_0828_B` | Si tuvo un accidente de trabajo, ¿Quién cubrió los gastos incurridos:EMPRESA CONTRATANTE |
| `ms08_0828_C` | Si tuvo un accidente de trabajo, ¿Quién cubrió los gastos incurridos:USTED MISMA |
| `ms09_0901` | Ahora me gustaría hablarle de algo más. ¿Ha oído usted hablar del VIH / SIDA? |
| `ms09_0902` | ¿Pueden las personas evitar contraer el VIH teniendo una sola pareja sexual fiel que no este infectada? |
| `ms09_0903` | ¿Pueden las personas protegerse del VIH usando condones cada vez que tienen relaciones sexuales? |
| `ms09_0904` | ¿Puede una persona contraer el VIH que causa el SIDA, compartiendo alimentos con una persona que tiene SIDA? |
| `ms09_0905` | ¿Puede una persona contraer el VIH por transfusiones sanguíneas, o por compartir jeringas? |
| `ms09_0906` | ¿Pueden las personas protegerse de contraer el VIH, no teniendo relaciones sexuales? |
| `ms09_0907` | ¿Piensa usted que es posible que una persona que parece saludable, pueda tener el VIH que causa el SIDA? |
| `ms09_0908_A` | En que momento, puede transmitir la madre infectada al hijo, el VIH que provoca el SIDA:(A) ¿Durante el embarazo? |
| `ms09_0908_B` | En que momento, puede transmitir la madre infectada al hijo, el VIH que provoca el SIDA:(B) ¿Durante el parto? |
| `ms09_0908_C` | En que momento, puede transmitir la madre infectada al hijo, el VIH que provoca el SIDA:(C) ¿Durante la cesárea? |
| `ms09_0908_D` | En que momento, puede transmitir la madre infectada al hijo, el VIH que provoca el SIDA:(D) ¿Durante la lactancia? |
| `ms09_0909` | ¿Sabe usted de algún lugar, donde la gente se puede hacer la prueba del VIH, que causa el SIDA? |
| `ms09_0910_A` | ¿Cual es ese lugar? (PUESTO DE SALUD) |
| `ms09_0910_B` | ¿Cual es ese lugar? (CENTRO DE SALUD AMBULATORIO) |
| `ms09_0910_C` | ¿Cual es ese lugar? (CENTRO DE SALUD CON INTERNACION) |
| `ms09_0910_D` | ¿Cual es ese lugar? (CENTRO DE SALUD INTEGRAL) |
| `ms09_0910_E` | ¿Cual es ese lugar? (HOSPITAL DE SEGUNDO NIVEL) |
| `ms09_0910_F` | ¿Cual es ese lugar? (HOSPITAL DE TERCER NIVEL) |
| `ms09_0910_G` | ¿Cual es ese lugar? (HOSPITAL ESPECIALIZADO) |
| `ms09_0910_H` | ¿Cual es ese lugar? (CAJA NACIONAL DE SALUD) |
| `ms09_0910_I` | ¿Cual es ese lugar? (CAJA DE LA BANCA PRIVADA) |
| `ms09_0910_J` | ¿Cual es ese lugar? (CAJA PETROLERA) |
| `ms09_0910_K` | ¿Cual es ese lugar? (CAJA DE LA BANCA ESTATAL) |
| `ms09_0910_L` | ¿Cual es ese lugar? (CORDES) |
| `ms09_0910_M` | ¿Cual es ese lugar? (CAJA DE CAMINOS) |
| `ms09_0910_N` | ¿Cual es ese lugar? (COSSMIL/FFAA) |
| `ms09_0910_O` | ¿Cual es ese lugar? (SEGURO UNIVERSITARIO) |
| `ms09_0910_P` | ¿Cual es ese lugar? (ORGANISMOS PRIVADOS (PRIMER NIVEL, SEGUNDO NIVEL, TERCER NIVEL)) |
| `ms09_0910_Q` | ¿Cual es ese lugar? (IGLESIA (PRIMER NIVEL, SEGUNDO NIVEL, TERCER NIVEL)) |
| `ms09_0910_R` | ¿Cual es ese lugar? (PROMOTOR DE LA SALUD/RPS/OTRO AGENTE) |
| `ms09_0910_S` | ¿Cual es ese lugar? (VISITA DOMICILIARIA) |
| `ms09_0910_T` | ¿Cual es ese lugar? (FARMACIA) |
| `ms09_0910_U` | ¿Cual es ese lugar? (MEDICINA TRADICIONAL) |
| `ms09_0910_V` | ¿Cual es ese lugar? (NO ACUDIÓ A NINGUN E.S./NO FUE) |
| `ms09_0910_X` | ¿Cual es ese lugar? (OTRO LUGAR:) |
| `ms09_0910_Z` | ¿Cual es ese lugar? (NO SABE) |
| `ms09_0910_X_cod` | (ESPECIFIQUE) OTRO LUGAR |
| `ms09_0911` | ¿Compraría usted vegetales/verduras de alguien que estuviese infectado con el VIH que causa el SIDA? |
| `ms09_0912` | ¿Considera usted que niñas y niños que viven con el VIH deben asistir a la escuela con niñas y niños que no tienen el VIH? |
| `ms09_0913_A` | Si algún miembro de su familia contrajera el VIH que causa el SIDA, ¿Usted:(A) Querría mantenerlo en secreto? |
| `ms09_0913_B` | Si algún miembro de su familia contrajera el VIH que causa el SIDA, ¿Usted:(B) Querría apoyarlo? |
| `ms09_0913_C` | Si algún miembro de su familia contrajera el VIH que causa el SIDA, ¿Usted:(C) Estaría dispuesta a cuidarlo en su propia casa? |
| `ms09_0913_D` | Si algún miembro de su familia contrajera el VIH que causa el SIDA, ¿Usted:(D) Lo expulsaría de su casa? |
| `ms09_0914` | ¿Se le debe hablar a los niños/as entre 12-14 años sobre el uso del condón para protegerse del SIDA? |
| `ms09_0915` | Yo no quiero conocer los resultados, pero ¿alguna vez se ha realizado una prueba del VIH? |
| `ms09_0916` | ¿La Última vez que se hizo una prueba de VIH recogió sus resultados? |
| `ms09_0917` | ¿Estaría dispuesto a realizarse una prueba de VIH? |
| `ms09_0918` | Aparte del VIH/SIDA ¿Usted ha oído hablar de otras infecciones que se pueden contagiar mediante las relaciones sexuales? |
| `ms09_0921` | ¿Ha tenido Ud. alguna infección de transmisión sexual durante los últimos 12 meses? |
| `ms09_0922_A` | ¿Sabe usted que las ITS:(A) Se pueden prevenir mediante el uso de condón? |
| `ms09_0922_B` | ¿Sabe usted que las ITS:(B) Aumentan el riesgo de transmisión del VIH? |
| `ms09_0923_A` | Las parejas no siempre están de acuerdo en todo. ¿Usted está de acuerdo con que una mujer se niegue a tener relaciones sexuales con la pareja, esposo/ compañero:(A) Cuando ella sabe que él tiene una infección (ITS) que ella puede adquirir durante las rela |
| `ms09_0923_B` | Las parejas no siempre están de acuerdo en todo ¿Usted está de acuerdo con que una mujer se niegue a tener relaciones sexuales con la pareja, esposo/ compañero:(B) Cuando ella está cansada y no quiere tener relaciones? |
| `ms09_0923_C` | Las parejas no siempre están de acuerdo en todo ¿Usted está de acuerdo con que una mujer se niegue a tener relaciones sexuales con la pareja, esposo/ compañero:(C) Cuándo ella sabe que él tiene relaciones con otra mujer? |
| `ms10_1001` | ¿En los últimos 12 meses, algún médico u otro personal de salud le ha medido la presión arterial? |
| `ms10_1002` | ¿Dónde le midieron a usted la presión arterial la última vez? |
| `ms10_1002_cod` | (ESPECIFIQUE) OTRO LUGAR |
| `ms10_1003` | ¿Alguna vez en su vida un médico le ha diagnosticado hipertensión arterial o "presión alta"? |
| `ms10_1004` | ¿En los últimos 12 meses, usted ha recibido y/o comprado medicamentos para controlar su presión arterial? |
| `ms10_1005` | ¿En los últimos 12 meses, algún médico o personal de salud, le han medido la glucosa (azúcar en la sangre)? |
| `ms10_1006` | ¿Dónde le midieron a usted la glucemia (azúcar en la sangre)? |
| `ms10_1006_cod` | (ESPECIFIQUE) OTRO LUGAR |
| `ms10_1007` | ¿Alguna vez en su vida un médico le ha diagnosticado Diabetes o azucar elevada en la sangre? |
| `ms10_1008` | ¿En los últimos 12 meses, usted ha recibido y/o comprado medicamentos para su Diabetes o azúcar alta en su sangre? |
| `ms10_1009` | ¿Usted ha oido hablar de una enfermedad llamada tuberculosis o TB? |
| `ms10_1010_A` | Usted sabe ¿Cómo se transmite la turberculosis de una persona a otra? (A TRAVÉS DEL AIRE, POR TOS O ESTORNUDOS) |
| `ms10_1010_B` | Usted sabe ¿Cómo se transmite la turberculosis de una persona a otra? (COMPARTIENDO UTENSILIOS) |
| `ms10_1010_C` | Usted sabe ¿Cómo se transmite la turberculosis de una persona a otra? (TOCANDO UNA PERSONA CON TUBERCULOSIS) |
| `ms10_1010_D` | Usted sabe ¿Cómo se transmite la turberculosis de una persona a otra? (COMPARTIENDO ALIMENTOS) |
| `ms10_1010_E` | Usted sabe ¿Cómo se transmite la turberculosis de una persona a otra? (POR CONTACTO SEXUAL) |
| `ms10_1010_F` | Usted sabe ¿Cómo se transmite la turberculosis de una persona a otra? (POR PICADURA DE MOSQUITOS) |
| `ms10_1010_X` | Usted sabe ¿Cómo se transmite la turberculosis de una persona a otra? (OTRA:) |
| `ms10_1010_Z` | Usted sabe ¿Cómo se transmite la turberculosis de una persona a otra? (NO SABE) |
| `ms10_1010_X_cod` | (ESPECIFIQUE) OTRA: |
| `ms10_1011` | ¿En su familia hay alguien con Tuberculosis diagnosticada? |
| `ms10_1012` | ¿Si un miembro de su familia tuviera tuberculosis, usted preferiría mantenerlo en secreto o no? |
| `ms10_1013` | ¿Conoce usted alguna persona que tenga tos por más de 15 días en su familia o en su barrio/comunidad? |
| `ms10_1014` | Usted recibió y/ o compró medicamento para tratamiento de Tuberculosis? |
| `ms10_1015_A` | ¿Donde recibió y/ o compró medicamento para tratamiento de la Tuberculosis? (PUESTO DE SALUD) |
| `ms10_1015_B` | ¿Donde recibió y/ o compró medicamento para tratamiento de la Tuberculosis? (CENTRO DE SALUD AMBULATORIO) |
| `ms10_1015_C` | ¿Donde recibió y/ o compró medicamento para tratamiento de la Tuberculosis? (CENTRO DE SALUD CON INTERNACION) |
| `ms10_1015_D` | ¿Donde recibió y/ o compró medicamento para tratamiento de la Tuberculosis? (CENTRO DE SALUD INTEGRAL) |
| `ms10_1015_E` | ¿Donde recibió y/ o compró medicamento para tratamiento de la Tuberculosis? (HOSPITAL DE SEGUNDO NIVEL) |
| `ms10_1015_F` | ¿Donde recibió y/ o compró medicamento para tratamiento de la Tuberculosis? (HOSPITAL DE TERCER NIVEL) |
| `ms10_1015_G` | ¿Donde recibió y/ o compró medicamento para tratamiento de la Tuberculosis? (HOSPITAL ESPECIALIZADO) |
| `ms10_1015_H` | ¿Donde recibió y/ o compró medicamento para tratamiento de la Tuberculosis? (CAJA NACIONAL DE SALUD) |
| `ms10_1015_I` | ¿Donde recibió y/ o compró medicamento para tratamiento de la Tuberculosis? (CAJA DE LA BANCA PRIVADA) |
| `ms10_1015_J` | ¿Donde recibió y/ o compró medicamento para tratamiento de la Tuberculosis? (CAJA PETROLERA) |
| `ms10_1015_K` | ¿Donde recibió y/ o compró medicamento para tratamiento de la Tuberculosis? (CAJA DE LA BANCA ESTATAL) |
| `ms10_1015_L` | ¿Donde recibió y/ o compró medicamento para tratamiento de la Tuberculosis? (CORDES) |
| `ms10_1015_M` | ¿Donde recibió y/ o compró medicamento para tratamiento de la Tuberculosis? (CAJA DE CAMINOS) |
| `ms10_1015_N` | ¿Donde recibió y/ o compró medicamento para tratamiento de la Tuberculosis? (COSSMIL/FFAA) |
| `ms10_1015_O` | ¿Donde recibió y/ o compró medicamento para tratamiento de la Tuberculosis? (SEGURO UNIVERSITARIO) |
| `ms10_1015_P` | ¿Donde recibió y/ o compró medicamento para tratamiento de la Tuberculosis? (ORGANISMOS PRIVADOS (PRIMER NIVEL, SEGUNDO NIVEL, TERCER NIVEL)) |
| `ms10_1015_Q` | ¿Donde recibió y/ o compró medicamento para tratamiento de la Tuberculosis? (IGLESIA (PRIMER NIVEL, SEGUNDO NIVEL, TERCER NIVEL)) |
| `ms10_1015_R` | ¿Donde recibió y/ o compró medicamento para tratamiento de la Tuberculosis? (PROMOTOR DE LA SALUD/RPS/OTRO AGENTE) |
| `ms10_1015_S` | ¿Donde recibió y/ o compró medicamento para tratamiento de la Tuberculosis? (VISITA DOMICILIARIA) |
| `ms10_1015_T` | ¿Donde recibió y/ o compró medicamento para tratamiento de la Tuberculosis? (FARMACIA) |
| `ms10_1015_U` | ¿Donde recibió y/ o compró medicamento para tratamiento de la Tuberculosis? (MEDICINA TRADICIONAL) |
| `ms10_1015_V` | ¿Donde recibió y/ o compró medicamento para tratamiento de la Tuberculosis? (NO ACUDIÓ A NINGUN E.S./NO FUE) |
| `ms10_1015_X` | ¿Donde recibió y/ o compró medicamento para tratamiento de la Tuberculosis? (OTRO LUGAR:) |
| `ms10_1015_Y` | ¿Donde recibió y/ o compró medicamento para tratamiento de la Tuberculosis? (NO SABE) |
| `ms10_1015_X_cod` | (ESPECIFIQUE) OTRO LUGAR |
| `ms10_1016` | ¿Sabe que es el dengue, zika, chikungunya? |
| `ms10_1017_A` | ¿Conoce como se transmite el Dengue, zika, chikungunya? (PICADURA DE MOSQUITO) |
| `ms10_1017_B` | ¿Conoce como se transmite el Dengue, zika, chikungunya? (COMER ALGO EN MAL ESTADO) |
| `ms10_1017_C` | ¿Conoce como se transmite el Dengue, zika, chikungunya? (CONTACTO CON UN ENFERMO) |
| `ms10_1017_X` | ¿Conoce como se transmite el Dengue, zika, chikungunya? (OTRO:) |
| `ms10_1017_Y` | ¿Conoce como se transmite el Dengue, zika, chikungunya? (NO SABE) |
| `ms10_1017_X_cod` | (ESPECIFIQUE) OTRO |
| `ms10_1018_A` | Que medidas preventivas conoces para prevenir el dengue zika, chikungunya? (ELIMINACION DE CRIADEROS) |
| `ms10_1018_B` | Que medidas preventivas conoces para prevenir el dengue zika, chikungunya? (USO DE REPELENTE) |
| `ms10_1018_C` | Que medidas preventivas conoces para prevenir el dengue zika, chikungunya? (DESECHOS DE AGUAS ESTANCADAS) |
| `ms10_1018_D` | Que medidas preventivas conoces para prevenir el dengue zika, chikungunya? (FUMIGACION DEL HOGAR) |
| `ms10_1018_E` | Que medidas preventivas conoces para prevenir el dengue zika, chikungunya? (USO DE MOSQUITEROS) |
| `ms10_1018_F` | Que medidas preventivas conoces para prevenir el dengue zika, chikungunya? (USO DE MALLA MILIMÉTRICA) |
| `ms10_1018_X` | Que medidas preventivas conoces para prevenir el dengue zika, chikungunya? (OTRO:) |
| `ms10_1018_Y` | Que medidas preventivas conoces para prevenir el dengue zika, chikungunya? (NO SABE) |
| `ms10_1018_X_cod` | (ESPECIFIQUE) OTRO |
| `ms10_1019_A` | ¿Cuáles son los síntomas que puede producir el dengue zika, chikungunya? (FIEBRE) |
| `ms10_1019_B` | ¿Cuáles son los síntomas que puede producir el dengue zika, chikungunya? (DOLOR DE CABEZA) |
| `ms10_1019_C` | ¿Cuáles son los síntomas que puede producir el dengue zika, chikungunya? (DOLOR DE MUSCULAR) |
| `ms10_1019_D` | ¿Cuáles son los síntomas que puede producir el dengue zika, chikungunya? (DOLOR RETROOCULAR) |
| `ms10_1019_E` | ¿Cuáles son los síntomas que puede producir el dengue zika, chikungunya? (SANGRADO DE NARIZ Y ENCÍAS) |
| `ms10_1019_F` | ¿Cuáles son los síntomas que puede producir el dengue zika, chikungunya? (ESCALOFRIOS) |
| `ms10_1019_X` | ¿Cuáles son los síntomas que puede producir el dengue zika, chikungunya? (OTRO:) |
| `ms10_1019_Y` | ¿Cuáles son los síntomas que puede producir el dengue zika, chikungunya? (NO SABE) |
| `ms10_1019_X_cod` | (ESPECIFIQUE) OTRO |
| `ms10_1020_A` | Ahora me gustaría hacerle algunas preguntas sobre el cuidado de su salud. Diferentes factores pueden influir para que la mujer consulte al médico o se haga tratar.Cuando Ud. se enferma y quiere recibir consejo o tratamiento médico, es para Ud. un gran pro |
| `ms10_1020_B` | Ahora me gustaría hacerle algunas preguntas sobre el cuidado de su salud. Diferentes factores pueden influir para que la mujer consulte al médico o se haga tratar.Cuando Ud. se enferma y quiere recibir consejo o tratamiento médico, es para Ud. un gran pro |
| `ms10_1020_C` | Ahora me gustaría hacerle algunas preguntas sobre el cuidado de su salud. Diferentes factores pueden influir para que la mujer consulte al médico o se haga tratar.Cuando Ud. se enferma y quiere recibir consejo o tratamiento médico, es para Ud. un gran pro |
| `ms10_1020_D` | Ahora me gustaría hacerle algunas preguntas sobre el cuidado de su salud. Diferentes factores pueden influir para que la mujer consulte al médico o se haga tratar.Cuando Ud. se enferma y quiere recibir consejo o tratamiento médico, es para Ud. un gran pro |
| `ms10_1020_E` | Ahora me gustaría hacerle algunas preguntas sobre el cuidado de su salud. Diferentes factores pueden influir para que la mujer consulte al médico o se haga tratar.Cuando Ud. se enferma y quiere recibir consejo o tratamiento médico, es para Ud. un gran pro |
| `ms10_1020_F` | Ahora me gustaría hacerle algunas preguntas sobre el cuidado de su salud. Diferentes factores pueden influir para que la mujer consulte al médico o se haga tratar.Cuando Ud. se enferma y quiere recibir consejo o tratamiento médico, es para Ud. un gran pro |
| `ms10_1020_G` | Ahora me gustaría hacerle algunas preguntas sobre el cuidado de su salud. Diferentes factores pueden influir para que la mujer consulte al médico o se haga tratar.Cuando Ud. se enferma y quiere recibir consejo o tratamiento médico, es para Ud. un gran pro |
| `ms10_1020_H` | Ahora me gustaría hacerle algunas preguntas sobre el cuidado de su salud. Diferentes factores pueden influir para que la mujer consulte al médico o se haga tratar.Cuando Ud. se enferma y quiere recibir consejo o tratamiento médico, es para Ud. un gran pro |
| `ms10_1020_I` | Ahora me gustaría hacerle algunas preguntas sobre el cuidado de su salud. Diferentes factores pueden influir para que la mujer consulte al médico o se haga tratar.Cuando Ud. se enferma y quiere recibir consejo o tratamiento médico, es para Ud. un gran pro |
| `ms10_1021_A` | (A) ¿Se ha sentido nerviosa, tensa, irritable, en el trabajo? |
| `ms10_1022_A` | ¿Esa sensación ha interferido con alguna de sus actividades cotidianas? |
| `ms10_1021_B` | (B) ¿Se ha sentido nerviosa, tensa, irritable, en su vida social? |
| `ms10_1022_B` | ¿Esa sensación ha interferido con alguna de sus actividades cotidianas? |
| `ms10_1021_C` | (C) ¿Se ha sentido nerviosa, tensa, irritable en sus estudios? |
| `ms10_1022_C` | ¿Esa sensación ha interferido con alguna de sus actividades cotidianas? |
| `ms10_1021_D` | (D) ¿Se ha sentido nerviosa, tensa, irritable en su familia? |
| `ms10_1022_D` | ¿Esa sensación ha interferido con alguna de sus actividades cotidianas? |
| `ms10_1023` | ¿Se siente triste o llora con mucha frecuencia? |
| `ms10_1024` | ¿Ya no disfruta de actividades de las que antes disfrutaba? |
| `ms10_1025` | ¿Ha pensado alguna vez en hacerse daño, en acabar con su vida o en la muerte? |
| `ms10_1026` | ¿En los últimos 12 meses usted ha tomado bebidas alcohólicas? |
| `ms10_1027_01` | ¿Con qué frecuencia ha tomado bebidas alcohólicas?INDAGUE: SI RESPONDE ALGUNA DE LAS ALTERNATIVAS, PREGUNTE LA CANTIDAD DE VASOS QUE HA TOMADO |
| `ms10_1027_02` | (ESPECIFIQUE) Nº DE VASOS |
| `ms10_1028_A` | ¿Alguna vez el consumo de bebidas alcohólicas ha interferido con sus actividades cotidianas en:(A) Su trabajo? |
| `ms10_1028_B` | ¿Alguna vez el consumo de bebidas alcohólicas ha interferido con sus actividades cotidianas en:(B) Sus estudios? |
| `ms10_1028_C` | ¿Alguna vez el consumo de bebidas alcohólicas ha interferido con sus actividades cotidianas en:(C) Su familia? |
| `ms10_1028_D` | ¿Alguna vez el consumo de bebidas alcohólicas ha interferido con sus actividades cotidianas en:(D) Su salud? |
| `ms10_1028_X` | ¿Alguna vez el consumo de bebidas alcohólicas ha interferido con sus actividades cotidianas en:(X) Otro (ESPECIFIQUE)? |
| `ms10_1028_X_cod` | (ESPECIFIQUE) OTRO |
| `ms10_1029_A` | ¿Alguna vez, bajo el efecto del consumo de bebidas alcohólicas, usted ha provocado o ha cometido acciones que atentan contra otras personas tales como:(A) Agresiones a su pareja? |
| `ms10_1029_B` | ¿Alguna vez, bajo el efecto del consumo de bebidas alcohólicas, usted ha provocado o ha cometido acciones que atentan contra otras personas tales como: (B) Agresiones a sus hijas/os? |
| `ms10_1029_C` | ¿Alguna vez, bajo el efecto del consumo de bebidas alcohólicas, usted ha provocado o ha cometido acciones que atentan contra otras personas tales como:(C) Agresiones a terceros? |
| `ms10_1029_D` | ¿Alguna vez, bajo el efecto del consumo de bebidas alcohólicas, usted ha provocado o ha cometido acciones que atentan contra otras personas tales como:(D) Violaciones? |
| `ms10_1029_E` | ¿Alguna vez, bajo el efecto del consumo de bebidas alcohólicas, usted ha provocado o ha cometido acciones que atentan contra otras personas tales como:(E) Accidentes / hechos de tránsito? |
| `ms10_1029_F` | ¿Alguna vez, bajo el efecto del consumo de bebidas alcohólicas, usted ha provocado o ha cometido acciones que atentan contra otras personas tales como:(F) Intentos de suicidio? |
| `ms10_1030` | ¿En los últimos 12 meses usted ha fumado? |
| `ms10_1031_01` | ¿Con qué frecuencia ha fumado cigarrillos?INDAGUE: SI RESPONDE ALGUNA DE LAS ALTERNATIVAS, PREGUNTE LA CANTIDAD DE CIGARRILLOS QUE HA FUMADO |
| `ms10_1031_02` | (ESPECIFIQUE) NRO. DE CIGARRILLOS. |
| `ms10_1033` | ¿Cuándo estaba embarazada usted fumaba? |
| `ms10_1034` | ¿Sabe que el humo del tabaco dentro de la casa provoca daños a su salud y a la de su familia? |
| `ms10_1035_A` | ¿En qué momento se lava las manos? (ANTES DE COMER) |
| `ms10_1035_B` | ¿En qué momento se lava las manos? (DESPUÉS DE UTILIZAR EL BAÑO) |
| `ms10_1035_C` | ¿En qué momento se lava las manos? (DESPUÉS DE CAMBIAR PAÑALES) |
| `ms10_1035_D` | ¿En qué momento se lava las manos? (ANTES DE PREPARAR LOS ALIMENTOS) |
| `ms10_1035_E` | ¿En qué momento se lava las manos? (ANTES DE DARLE DE COMER O DE LACTAR A SU HIJA/O) |
| `ms10_1035_F` | ¿En qué momento se lava las manos? (OTRA) |
| `ms10_1035_X` | ¿En qué momento se lava las manos? (EN NINGÚN MOMENTO) |
| `ms10_1035_X_cod` | (ESPECIFIQUE) OTRA |
| `ms10_1036` | ¿Conoce o ha escuchado hablar de algún tipo de droga, fuera del alcohol y el tabaco? |
| `ms10_1037_A` | Mencione cuales conoce: (MARIHUANA) |
| `ms10_1037_B` | Mencione cuales conoce: (COCAINA) |
| `ms10_1037_C` | Mencione cuales conoce: (EXTASIS) |
| `ms10_1037_D` | Mencione cuales conoce: (HACHIS) |
| `ms10_1037_E` | Mencione cuales conoce: (ANFETAMINAS) |
| `ms10_1037_F` | Mencione cuales conoce: (INHALANTES(CLEFA)) |
| `ms10_1037_G` | Mencione cuales conoce: (HEROÍNA) |
| `ms10_1037_H` | Mencione cuales conoce: (LSD) |
| `ms10_1037_I` | Mencione cuales conoce: (TRANQUILIZANTES O PSICOESTIMULANTES) |
| `ms10_1037_X` | Mencione cuales conoce: (OTROS) |
| `ms10_1037_X_cod` | (ESPECIFIQUE) OTROS |
| `ms10_1038` | ¿Sabe usted que el cáncer también se da en las/os niñas/os? |
| `ms10_1039` | ¿Sabe de alguna niña o algún niño en su familia o en su comunidad, que haya tenido cáncer? |
| `ms10_1040` | ¿Conoce o ha oido hablar de alguna niña o algún niño que haya fallecido por cáncer? |
| `ms10_1041_A` | Entre las mujeres de su familia. ¿Alguna ha tenido Cáncer de mama:(A) Abuela (s)? |
| `ms10_1041_B` | Entre las mujeres de su familia. ¿Alguna ha tenido Cáncer de mama:(B) Madre? |
| `ms10_1041_C` | Entre las mujeres de su familia. ¿Alguna ha tenido Cáncer de mama:(C) Hermana (s)? |
| `ms10_1041_D` | Entre las mujeres de su familia. ¿Alguna ha tenido Cáncer de mama:(D) Tía (s)? |
| `ms10_1041_E` | Entre las mujeres de su familia. ¿Alguna ha tenido Cáncer de mama:(E) Hija (s)? |
| `ms10_1041_X` | Entre las mujeres de su familia. ¿Alguna ha tenido Cáncer de mama:(X) Otras (ESPECIFIQUE)? |
| `ms10_1041_X_cod` | (ESPECIFIQUE) OTRAS |
| `ms10_1042` | ¿Recibió la vacuna antidiftérica-antitetánica (DT)? |
| `ms10_1042a` | ¿Cúantas dósis de DT ha recibido? |
| `ms10_1044` | ¿Recibió la vacuna contra el Virus Papiloma Humano (VPH)? |
| `ms10_1044a` | ¿Cúantas dósis de VPH ha recibido? |
| `ms11_1101_A` | VERIFICAR LA PRESENCIA DE OTRAS PERSONAS. SE RECOMIENDA PRIVACIDAD. PRIVACIDAD OBTENIDAMENORES DE 10 AÑOS.. |
| `ms11_1101_B` | ESPOSO/COMPAÑERO |
| `ms11_1101_C` | OTROS HOMBRES |
| `ms11_1101_D` | OTRAS MUJERES.. |
| `ms11_1103` | Para usted ¿quién sufre más violencia en las parejas? |
| `ms11_1104_A` | Para usted ¿cuáles son los motivos más comunes para que exista violencia en una relación de pareja?LOS CELOS |
| `ms11_1104_B` | Para usted ¿cuáles son los motivos más comunes para que exista violencia en una relación de pareja?LA INFIDELIDAD |
| `ms11_1104_C` | Para usted ¿cuáles son los motivos más comunes para que exista violencia en una relación de pareja?EL ABUSO DE ALCOHOL |
| `ms11_1104_D` | Para usted ¿cuáles son los motivos más comunes para que exista violencia en una relación de pareja?LA POBREZA |
| `ms11_1104_E` | Para usted ¿cuáles son los motivos más comunes para que exista violencia en una relación de pareja?EXPERIENCIAS DE VIOLENCIA EN LA INFANCIA |
| `ms11_1104_F` | Para usted ¿cuáles son los motivos más comunes para que exista violencia en una relación de pareja?PROBLEMAS CON LOS HIJOS/AS |
| `ms11_1104_G` | Para usted ¿cuáles son los motivos más comunes para que exista violencia en una relación de pareja?MACHISMO/SISTEMA PATRIARCAL |
| `ms11_1104_H` | Para usted ¿cuáles son los motivos más comunes para que exista violencia en una relación de pareja?OTRAS |
| `ms11_1104_X` | Para usted ¿cuáles son los motivos más comunes para que exista violencia en una relación de pareja? (OTRAS) |
| `ms11_1104_X_cod` | (ESPECIFÍQUE) OTRAS |
| `ms11_1105_A` | Por f av or dígame si en los últimos 12 meses se presentaron las siguientes situaciones en la relación con su esposo/ compañero/ nov io ó pareja LO ACUSABA DE SER INFIEL |
| `ms11_1105_B` | Por f av or dígame si en los últimos 12 meses se presentaron las siguientes situaciones en la relación con su esposo/ compañero/ nov io ó pareja iNSULTOS/PALABRAS GROSERA |
| `ms11_1105_C` | Por f av or dígame si en los últimos 12 meses se presentaron las siguientes situaciones en la relación con su esposo/ compañero/ nov io ó pareja ENCERRADO/ PROHIBIR SALIR/ |
| `ms11_1105_D` | Por f av or dígame si en los últimos 12 meses se presentaron las siguientes situaciones en la relación con su esposo/ compañero/ nov io ó pareja HUMILLADO/MENOSPRECIADO |
| `ms11_1105_E` | Por f av or dígame si en los últimos 12 meses se presentaron las siguientes situaciones en la relación con su esposo/ compañero/ nov io ó pareja AMENAZABA CON ABANDONARLA |
| `ms11_1105_F` | Por f av or dígame si en los últimos 12 meses se presentaron las siguientes situaciones en la relación con su esposo/ compañero/ nov io ó pareja AMENAZABA QUITARLE HIJAS/OS |
| `ms11_1105_G` | Por f av or dígame si en los últimos 12 meses se presentaron las siguientes situaciones en la relación con su esposo/ compañero/ nov io ó pareja AMENAZA CON NO CUMPLIR CON LAS RESPONSABILIDADES ECONÓMICAS |
| `ms11_1105_H` | Por f av or dígame si en los últimos 12 meses se presentaron las siguientes situaciones en la relación con su esposo/ compañero/ nov io ó pareja CONTROL RECURSOS ECONO/ QUITA LIBERTAD/ IMPIDE ACT. LABORALES |
| `ms11_1105_I` | Por f av or dígame si en los últimos 12 meses se presentaron las siguientes situaciones en la relación con su esposo/ compañero/ nov io ó pareja PUBLICAR FOTOS/ VIDEOS CONTENIDO SEXUAL EN REDES SOCIALES |
| `ms11_1105_J` | Por f av or dígame si en los últimos 12 meses se presentaron las siguientes situaciones en la relación con su esposo/ compañero/ nov io ó parejaAMENAZABA CON MATARLA |
| `ms11_1105_K` | Por f av or dígame si en los últimos 12 meses se presentaron las siguientes situaciones en la relación con su esposo/ compañero/ nov io ó parejaOTRA |
| `ms11_1105_X` | Por favor dígame si en los últimos 12 meses se presentaron las siguientes situaciones en la relación con su esposo/ compañero/ novio ó pareja. (X) Alguna otra? (especifique) |
| `ms11_1105_X_cod` | (ESPECIFÍQUE) OTRA |
| `ms11_1107_A` | Como resultado de las situaciones mencionadas anteriormente Usted:MIEDO A REACCIÓN Como resultado de las situaciones mencionadas anteriormente Usted:DESGANO, TRISTEZA, LLANTO Como resultado de las situaciones mencionadas anteriormente Usted:DEJÓ DE ESTUDI |
| `ms11_1107_B` | Como resultado de las situaciones mencionadas anteriormente Usted:DESGANO, TRISTEZA, LLANTO |
| `ms11_1107_C` | Como resultado de las situaciones mencionadas anteriormente Usted:DEJÓ DE ESTUDIAR/ TRABAJAR |
| `ms11_1107_D` | Como resultado de las situaciones mencionadas anteriormente Usted: DEJÓ ACT. IMPORTANTES. |
| `ms11_1107_E` | Como resultado de las situaciones mencionadas anteriormente Usted: PENSÓ ABANDONAR SU HOGAR |
| `ms11_1107_F` | Como resultado de las situaciones mencionadas anteriormente Usted:a? LASTIMARSE O QUITARSE LA VIDA |
| `ms11_1107_X` | Como resultado de las situaciones mencionadas anteriormente Usted:OTRA |
| `ms11_1107_X_cod` | (ESPECIFÍQUE) OTRA |
| `ms11_1108_A` | Por f av or dígame si en los últimos 12 meses se presentaron las siguientes situaciones en la relación con su esposo/ compañero/ nov io ó pareja EMPUJADO/ JALONEADO |
| `ms11_1108_B` | Por f av or dígame si en los últimos 12 meses se presentaron las siguientes situaciones en la relación con su esposo/ compañero/ nov io ó pareja EMPUJADO/ JALONEADO |
| `ms11_1108_C` | Por f av or dígame si en los últimos 12 meses se presentaron las siguientes situaciones en la relación con su esposo/ compañero/ nov io ó pareja GOLPEADO CON OBJETO |
| `ms11_1108_D` | Por f av or dígame si en los últimos 12 meses se presentaron las siguientes situaciones en la relación con su esposo/ compañero/ nov io ó pareja TRATADO DE ESTRANGULAR/QUEMAR |
| `ms11_1108_E` | Por f av or dígame si en los últimos 12 meses se presentaron las siguientes situaciones en la relación con su esposo/ compañero/ nov io ó pareja AMENAZA CUCHILLO/ NAVAJA/ PISTOLA |
| `ms11_1108_F` | Por f av or dígame si en los últimos 12 meses se presentaron las siguientes situaciones en la relación con su esposo/ compañero/ nov io ó pareja AGRESIÓN CUCHILLO/ NAVAJA/ PISTOLA |
| `ms11_1108_G` | Por f av or dígame si en los últimos 12 meses se presentaron las siguientes situaciones en la relación con su esposo/ compañero/ nov io ó pareja FUERZA FÍSICA REL. SEXUALES |
| `ms11_1108_H` | Por f av or dígame si en los últimos 12 meses se presentaron las siguientes situaciones en la relación con su esposo/ compañero/ nov io ó pareja EXIGIDO TENER REL. SEXUALES |
| `ms11_1108_I` | Por f av or dígame si en los últimos 12 meses se presentaron las siguientes situaciones en la relación con su esposo/ compañero/ nov io ó pareja FORZADO A ACTIVIDADES SE |
| `ms11_1108_X` | Por f av or dígame si en los últimos 12 meses se presentaron las siguientes situaciones en la relación con su esposo/ compañero/ nov io ó pareja OT R A |
| `ms11_1108_X_cod` | (ESPECIFÍQUE) OTRA |
| `ms11_1110_A` | ¿Estas situaciones se han presentado a solas o en presencia de otras personas?A SOLAS |
| `ms11_1110_B` | ¿Estas situaciones se han presentado a solas o en presencia de otras personas?EN PRESENCIA DE AMIGOS |
| `ms11_1110_C` | ¿Estas situaciones se han presentado a solas o en presencia de otras personas?EN PRESENCIA DE FAMILIARES |
| `ms11_1110_D` | ¿Estas situaciones se han presentado a solas o en presencia de otras personas?OTRAS PERSONAS |
| `ms11_1110_X` | ¿Estas situaciones se han presentado a solas o en presencia de otras personas?OTRAS PERSONAS |
| `ms11_1110_X_cod` | (ESPECIFÍQUE) OTRAS PERSONAS |
| `ms11_1111_A` | Como resultado de las situaciones mencionadas enteriormente Usted:MIEDO A REACCIÓN |
| `ms11_1111_B` | Como resultado de las situaciones mencionadas enteriormente Usted:DESGANO/TRISTEZA/LLANTO |
| `ms11_1111_C` | Como resultado de las situaciones mencionadas enteriormente Usted:MORETONES/ MARCAS/DOLORES HERIDAS/HUESO QUEBRADO |
| `ms11_1111_D` | Como resultado de las situaciones mencionadas enteriormente Usted:PERDIDA TEMP. O DEFINITIVA ORGANO O PARTE DEL CUERPO |
| `ms11_1111_E` | Como resultado de las situaciones mencionadas enteriormente Usted:DEJÓ ESTUDIAR/ TRABAJAR |
| `ms11_1111_F` | Como resultado de las situaciones mencionadas enteriormente Usted:DEJÓ ACT. IMPORTANTES |
| `ms11_1111_G` | Como resultado de las situaciones mencionadas enteriormente Usted:PARTICIPAR ORG. SOC. Ó POL |
| `ms11_1111_H` | Como resultado de las situaciones mencionadas enteriormente Usted:SE EMBARAZÓ |
| `ms11_1111_I` | Como resultado de las situaciones mencionadas enteriormente Usted:PENSÓ ABANDONAR SU HOGAR |
| `ms11_1111_J` | Como resultado de las situaciones mencionadas enteriormente Usted:a? LASTIMARSE O QUITARSE LA VIDA |
| `ms11_1111_X` | Como resultado de las situaciones mencionadas enteriormente Usted:OTRA_ |
| `ms11_1111_X_cod` | (ESPECIFÍQUE) OTRA |
| `ms11_1113` | ¿Cómo resultado de lo que su esposo/compañero/novio o pareja le hizo, usted fue al médico, establecimiento de salud y/o médico forense? |
| `ms11_1114` | Cuando acudió al médico, establecimiento de salud.¿La quisieron atender? |
| `ms11_1115` | El personal del establecimiento de salud, ¿le orientó para denunciar la agresión? |
| `ms11_1116_A` | ¿Qué tipo de orientación le brindo el personal de salud? APOYO Y CONTENCIÓN EMOCIONAL |
| `ms11_1116_B` | ¿Qué tipo de orientación le brindo el personal de salud? ORIENTACIÓN SERVICIOS |
| `ms11_1116_C` | ¿Qué tipo de orientación le brindo el personal de salud? DERIVACIÓN SERVICIOS |
| `ms11_1116_X` | ¿Qué tipo de orientación le brindo el personal de salud? OTRO |
| `ms11_1116_X_cod` | (ESPECIFIQUE) OTRO |
| `ms11_1117` | Despúes de la atención y una vez establecido el diagnóstico ¿le otorgaron un certificado médico? |
| `ms11_1119_A` | Cuando acudio al médico o establecimiento de salud. ¿Usted : recibio: APOYO/CONTENCIÓN EMOCIONAL |
| `ms11_1119_B` | Cuando acudio al médico o establecimiento de salud. ¿Usted : recibio: ANTICONCEPCIÓN EMERGENCIA |
| `ms11_1119_C` | Cuando acudio al médico o establecimiento de salud. ¿Usted : recibio: PREVEN. ITS/VIH/SIDA/Hepatitis |
| `ms11_1119_D` | Cuando acudio al médico o establecimiento de salud. ¿Usted : recibio: ATENCIÓN LESIONES |
| `ms11_1119_E` | Cuando acudio al médico o establecimiento de salud. ¿Usted : TEST EMBARAZO |
| `ms11_1119_F` | Cuando acudio al médico o establecimiento de salud. ¿Usted : recibio: PROCEDIMIENTO ILE |
| `ms11_1119_X` | Cuando acudio al médico o establecimiento de salud. ¿Usted : recibio: alguna otra? |
| `ms11_1119_X_cod` | (ESPECIFIQUE) OTRA |
| `ms11_1121` | ¿Decidió continuar con su embarazo? |
| `ms11_1122_A` | ¿Realizó el procedimiento ILE en el sistema de salud público o privado? SISTEMA DE SALUD PÚBLICO |
| `ms11_1122_B` | ¿Realizó el procedimiento ILE en el sistema de salud público o privado? SISTEMA DE SALUD PRIVADO |
| `ms11_1122_X` | ¿Realizó el procedimiento ILE en el sistema de salud público o privado? ( ESPEC IF ÍQU E) NO RESPONDE |
| `ms11_1122_Z` | ¿Realizó el procedimiento ILE en el sistema de salud público o privado? (NO RESPONDE) |
| `ms11_1122_X_cod` | (ESPECIFIQUE) OTRA |
| `ms11_1123` | Cuando usted solicito el procedimiento ILE (interrupcion legal del embarazo) ¿Le brindaron el servicio? |
| `ms11_1124` | ¿Usted conoce alguna ley sobre el procedimiento ILE? |
| `ms11_1125` | Cuando fue agredida por su esposo/compañero/novio o pareja. ¿Pidió ayuda a personas cercanas a usted? |
| `ms11_1126_A` | ¿A quiénes? MADRE |
| `ms11_1126_B` | ¿A quiénes? PADRE |
| `ms11_1126_C` | ¿A quiénes? MADRASTRA |
| `ms11_1126_D` | ¿A quiénes? PADRASTRO |
| `ms11_1126_E` | ¿A quiénes? HERMANA |
| `ms11_1126_F` | ¿A quiénes? HERMANO |
| `ms11_1126_G` | ¿A quiénes? HIJA |
| `ms11_1126_H` | ¿A quiénes? HIJO. |
| `ms11_1126_I` | ¿A quiénes? PARIENTES POLÍTICOS(SUEGRO/A, CUÑADO/A) |
| `ms11_1126_J` | ¿A quiénes? I REDES SOCIALES EN INTERNET |
| `ms11_1126_K` | ¿A quiénes? VECINOS/AMIGOS |
| `ms11_1126_X` | ¿A quiénes? OTRAS PERSONAS |
| `ms11_1126_X_cod` | (ESPECIFIQUE) OTRAS PERSONAS |
| `ms11_1127` | Cuando la agredieron, ¿Ud. denunció la agresión? |
| `ms11_1127_A` | Cuando la agredieron, ¿Ud. denunció la agresión? SI |
| `ms11_1127_B` | Cuando la agredieron, ¿Ud. denunció la agresión? NO |
| `ms11_1127_C` | ¿Cuánto tiempo transcurrió desde la agresión al momento en que realizó la denuncia? (DESPÚES DE VARIAS SEMANAS) |
| `ms11_1127_X` | ¿Cuánto tiempo transcurrió desde la agresión al momento en que realizó la denuncia? (OTRO) |
| `ms11_1127_X_cod` | (ESPECIFICAR) OTROS |
| `ms11_1128_A` | ¿A qué institución acudió?ESTABLECIMIENTO DE SALUD |
| `ms11_1128_B` | ¿A qué institución acudió?SERVICIO LEGAL INTEGRAL MUNICIPAL (SLIMs) |
| `ms11_1128_C` | ¿A qué institución acudió?MARCAR LAS RESPUESTAS MENCIONADAS IDIF - MEDICO FORENSE |
| `ms11_1128_D` | ¿A qué institución acudió?SEDEGES |
| `ms11_1128_E` | ¿A qué institución acudió?MINISTERIO DE JUSTICIA (SIJ-PLU) |
| `ms11_1128_F` | ¿A qué institución acudió?MINISTERIO DE JUSTICIA |
| `ms11_1128_G` | ¿A qué institución acudió?(SEPDAVI). |
| `ms11_1128_H` | ¿A qué institución acudió?FELCV |
| `ms11_1128_I` | ¿A qué institución acudió? POLICÍA |
| `ms11_1128_J` | ¿A qué institución acudió?AUTORIDADES COMUNITARIAS/ORIGINARIAS |
| `ms11_1128_K` | ¿A qué institución acudió?ONG. |
| `ms11_1128_L` | ¿A qué institución acudió?MINISTERIO PÚBLICO - FISCALIA |
| `ms11_1128_X` | ¿A qué institución acudió? OTRA_ |
| `ms11_1128_X_cod` | (ESPECIFIQUE) OTRA |
| `ms11_1129_A` | ¿Qué tipo de apoyo recibió?MÉDICO |
| `ms11_1129_B` | ¿Qué tipo de apoyo recibió?PSICOLÓGICO . |
| `ms11_1129_C` | ¿Qué tipo de apoyo recibió?LEGAL |
| `ms11_1129_D` | ¿Qué tipo de apoyo recibió?MARCAR LAS RESPUESTAS MENCIONADAS SOCIAL(INFORMACIÓN/ORIENTACIÓN) |
| `ms11_1129_E` | ¿Qué tipo de apoyo recibió?COMUNITARIO |
| `ms11_1129_X` | ¿Qué tipo de apoyo recibió?OTRO |
| `ms11_1129_Y` | ¿Qué tipo de apoyo recibió?NO RECIBIÓ APOYO |
| `ms11_1129_X_cod` | (ESPECIFIQUE) OTRO |
| `ms11_1130_A` | ¿Por qué no hizo la denuncia?NO SABÍA DONDE IR |
| `ms11_1130_B` | ¿Por qué no hizo la denuncia?VERGÜENZA Y HUMILLACIÓN |
| `ms11_1130_C` | ¿Por qué no hizo la denuncia?ES NORMAL |
| `ms11_1130_D` | ¿Por qué no hizo la denuncia?YO TENIA LA CULPA |
| `ms11_1130_E` | ¿Por qué no hizo la denuncia?MIEDO A LA SEPARACIÓN |
| `ms11_1130_F` | ¿Por qué no hizo la denuncia?MIEDO A QUEDARSE SOLA |
| `ms11_1130_G` | ¿Por qué no hizo la denuncia?MIEDO A REPRESALIAS |
| `ms11_1130_H` | ¿Por qué no hizo la denuncia?MIEDO A QUE SU HOGAR NO TENGA SUSTENTO ECONÓMICO |
| `ms11_1130_I` | ¿Por qué no hizo la denuncia?PENSÉ QUE NO VOLVERÍA A OCURRIR NO CREÍA EN LA JUSTICIA |
| `ms11_1130_J` | ¿Por qué no hizo la denuncia?PENSÉ QUE ME COBRARÍAN |
| `ms11_1130_K` | ¿Por qué no hizo la denuncia?RECIBÍ DINERO O PAGO EN ESPECIE |
| `ms11_1130_L` | ¿Por qué no hizo la denuncia?POR NO AFECTAR A LOS HIJOS |
| `ms11_1130_M` | ¿Por qué no hizo la denuncia?MIEDO A QUE ME QUITEN LOS HIJOS |
| `ms11_1130_N` | ¿Por qué no hizo la denuncia?OTRO |
| `ms11_1130_X` | ¿Por qué no hizo la denuncia? (OTRO) |
| `ms11_1130_X_cod` | (ESPECIFIQUE) OTRO |
| `ms11_1131_A` | Según su opinión, los hechos de violencia sexual suceden, habitualmente en:ESPACIOS PÚBLICOS |
| `ms11_1131_B` | Según su opinión, los hechos de violencia sexual suceden, habitualmente en:LUGARES DE ESTUDIO Y/O TRABAJO |
| `ms11_1131_C` | Según su opinión, los hechos de violencia sexual suceden, habitualmente en:LA PROPIA CASA |
| `ms11_1131_D` | Según su opinión, los hechos de violencia sexual suceden, habitualmente en:CASA DE FAMILIARES |
| `ms11_1131_E` | Según su opinión, los hechos de violencia sexual suceden, habitualmente en:EVENTOS PUBLICOS (fiestas y otros) |
| `ms11_1131_X` | Según su opinión, los hechos de violencia sexual suceden, habitualmente en:OTRO |
| `ms11_1131_X_cod` | (ESPECIFIQUE) OTRO |
| `ms11_1132` | Por favor dígame si en los últimos 12 meses, alguna persona que no sea su pareja o sea desconocida ¿La agredió de alguna manera? |
| `ms11_1132_X_cod` | (ESPECIFIQUE) OTRO |
| `ms11_1133_A` | ¿Quién la agredió?PADRE/ MADRE |
| `ms11_1133_B` | ¿Quién la agredió?PADRASTRO/ MADRASTRA |
| `ms11_1133_C` | ¿Quién la agredió?HERMANO/ A |
| `ms11_1133_D` | ¿Quién la agredió?HIJO/ A |
| `ms11_1133_E` | ¿Quién la agredió?PARIENTES POL. (SUEGRO/A, CUÑADO/A) |
| `ms11_1133_F` | ¿Quién la agredió?TIO/ A. |
| `ms11_1133_G` | ¿Quién la agredió?CUÑADO/A |
| `ms11_1133_H` | ¿Quién la agredió?EX ESPOSO/COMPAÑERO/PAREJA |
| `ms11_1133_I` | ¿Quién la agredió?JEFE/ A |
| `ms11_1133_J` | ¿Quién la agredió?PROFESOR/ A |
| `ms11_1133_K` | ¿Quién la agredió?CATEDRÁTICO/ A |
| `ms11_1133_L` | ¿Quién la agredió?COMPAÑERO/A DE TRABAJO |
| `ms11_1133_M` | ¿Quién la agredió?VECINOS/AMIGOS |
| `ms11_1133_N` | ¿Quién la agredió?DIRIGENTE |
| `ms11_1133_O` | ¿Quién la agredió?DESCONOCIDO/ A. |
| `ms11_1133_X` | ¿Quién la agredió?OTRO |
| `ms11_1133_X_cod` | (ESPECIFIQUE) OTRO |
| `ms11_1134_A` | ¿Dónde la agredieron?ESPACIO PUBLICO |
| `ms11_1134_B` | ¿Dónde la agredieron?EN SU TRABAJO |
| `ms11_1134_C` | ¿Dónde la agredieron?EN LA ESCUELA/ COLEGIO |
| `ms11_1134_D` | ¿Dónde la agredieron?EN LA UNIVERSIDAD |
| `ms11_1134_E` | ¿Dónde la agredieron?EVENTOS PUBLICOS (fiestas y otros) |
| `ms11_1134_F` | ¿Dónde la agredieron?EN INSTITUCIÓN POLICIAL / MILITAR |
| `ms11_1134_G` | ¿Dónde la agredieron?ORGANIZACIÓN SOCIAL/PARTIDO POLITICO |
| `ms11_1134_X` | ¿Dónde la agredieron?OTRO LUGAR |
| `ms11_1134_X_cod` | (ESPECIFIQUE) OTRO |
| `ms11_1135` | ¿Durante los últimos 12 meses ha sido forzada a tener relaciones sexuales por alguna persona diferente a su esposo/ compañero/ novio ó pareja? |
| `ms11_1136_A` | ¿Quién la forzó a tener relaciones sexuales?PADRE/ MADRE |
| `ms11_1136_B` | ¿Quién la forzó a tener relaciones sexuales?PADRASTRO/ MADRASTRA |
| `ms11_1136_C` | ¿Quién la forzó a tener relaciones sexuales?HERMANO/ A |
| `ms11_1136_D` | ¿Quién la forzó a tener relaciones sexuales?HIJO/ A |
| `ms11_1136_E` | ¿Quién la forzó a tener relaciones sexuales?PARIENTES POL. (SUEGRO/A, CUÑADO/A) |
| `ms11_1136_F` | ¿Quién la forzó a tener relaciones sexuales?TIO/ A. |
| `ms11_1136_G` | ¿Quién la forzó a tener relaciones sexuales?CUÑADO/A. |
| `ms11_1136_H` | ¿Quién la forzó a tener relaciones sexuales?EX ESPOSO/COMPAÑERO/PAREJA |
| `ms11_1136_I` | ¿Quién la forzó a tener relaciones sexuales?JEFE/ A |
| `ms11_1136_J` | ¿Quién la forzó a tener relaciones sexuales?PROFESOR/ A |
| `ms11_1136_K` | ¿Quién la forzó a tener relaciones sexuales?CATEDRÁTICO/ A |
| `ms11_1136_L` | ¿Quién la forzó a tener relaciones sexuales?COMPAÑERO/A DE TRABAJO |
| `ms11_1136_M` | ¿Quién la forzó a tener relaciones sexuales?VECINOS/AMIGOS |
| `ms11_1136_N` | ¿Quién la forzó a tener relaciones sexuales?DIRIGENTE |
| `ms11_1136_O` | ¿Quién la forzó a tener relaciones sexuales?DESCONOCIDO/ A |
| `ms11_1136_X` | ¿Quién la forzó a tener relaciones sexuales?OTRO_ |
| `ms11_1136_Y` | ¿Quién la forzó a tener relaciones sexuales?NINGUNO/ NO QUIERE HABLAR DEL TEMA |
| `ms11_1136_X_cod` | (ESPECIFIQUE) OTRO |
| `ms11_1137_A` | ¿Donde la forzaron a tener relaciones sexuales?ESPACIO PUBLICO |
| `ms11_1137_B` | ¿Donde la forzaron a tener relaciones sexuales?EN SU TRABAJO |
| `ms11_1137_C` | ¿Donde la forzaron a tener relaciones sexuales?EN LA ESCUELA/ COLEGIO |
| `ms11_1137_D` | ¿Donde la forzaron a tener relaciones sexuales?EN LA UNIVERSIDAD |
| `ms11_1137_E` | ¿Donde la forzaron a tener relaciones sexuales?EVENTOS PUBLICOS |
| `ms11_1137_F` | ¿Donde la forzaron a tener relaciones sexuales?EN INSTITUCIÓN POLICIAL / MILITAR |
| `ms11_1137_G` | ¿Donde la forzaron a tener relaciones sexuales?ORGANIZACIÓN SOCIAL/PARTIDO POLITICO |
| `ms11_1137_X` | ¿Donde la forzaron a tener relaciones sexuales?OTRO LUGAR |
| `ms11_1137_X_cod` | (ESPECIFIQUE) OTRO |
| `ms11_1138` | Cuando la forzaron a tener relaciones sexuales ¿Ud. denunció la agresión? |
| `ms11_1139_A` | ¿A qué institución acudió?ESTABLECIMIENTO DE SALUD |
| `ms11_1139_B` | ¿A qué institución acudió?SERVICIO LEGAL INTEGRAL MUNICIPAL (SLIMs) |
| `ms11_1139_C` | ¿A qué institución acudió?DEFENSORIA DE LA NIÑEZ Y ADOLESCENCIA (DNA) |
| `ms11_1139_D` | ¿A qué institución acudió?IDIF - MEDICO FORENSE |
| `ms11_1139_E` | ¿A qué institución acudió?SEDEGES |
| `ms11_1139_F` | ¿A qué institución acudió?MINISTERIO DE JUSTICIA (SIJ-PLU) |
| `ms11_1139_G` | ¿A qué institución acudió?MINISTERIO DE JUSTICIA (SEPDAPI) |
| `ms11_1139_H` | ¿A qué institución acudió?FELCV |
| `ms11_1139_I` | ¿A qué institución acudió?POLICÍA |
| `ms11_1139_J` | ¿A qué institución acudió?AUTORIDADES COMUNITARIAS/ORIGINARIAS |
| `ms11_1139_K` | ¿A qué institución acudió?ONG |
| `ms11_1139_L` | ¿A qué institución acudió?MINISTERIO PÚBLICO - FISCALIA |
| `ms11_1139_X` | ¿A qué institución acudió?OTRA |
| `ms11_1139_X_cod` | (ESPECIFIQUE) OTRO |
| `ms11_1140_A` | ¿Qué tipo de apoyo recibió?MÉDICO |
| `ms11_1140_B` | ¿Qué tipo de apoyo recibió?PSICOLÓGICO |
| `ms11_1140_C` | ¿Qué tipo de apoyo recibió?LEGALSOCIAL(INFORMACIÓN/ORIENTACIÓN) |
| `ms11_1140_D` | ¿Qué tipo de apoyo recibió?COMUNITARIO |
| `ms11_1140_E` | ¿Qué tipo de apoyo recibió?OTRO |
| `ms11_1140_X` | ¿Qué tipo de apoyo recibió? (OTRO) |
| `ms11_1140_Y` | ¿Qué tipo de apoyo recibió? (NO RECIBIÓ APOYO) |
| `ms11_1140_X_cod` | (ESPECIFIQUE) OTRO |
| `ms11_1141_A` | ¿Qué tipo de apoyo recibió?MÉDICO |
| `ms11_1141_B` | ¿Por qué no hizo la denuncia?VERGÜENZA Y HUMILLACIÓN |
| `ms11_1141_C` | ¿Por qué no hizo la denuncia?ES NORMAL |
| `ms11_1141_D` | ¿Por qué no hizo la denuncia?YO TENIA LA CULPA |
| `ms11_1141_E` | ¿Por qué no hizo la denuncia?MIEDO A LA SEPARACIÓN |
| `ms11_1141_F` | ¿Por qué no hizo la denuncia?MIEDO A QUEDARSE SOLO |
| `ms11_1141_G` | ¿Por qué no hizo la denuncia?MIEDO A REPRESALIAS |
| `ms11_1141_H` | ¿Por qué no hizo la denuncia?MIEDO A QUE SU HOGAR NO TENGA SUSTENTO ECONÓMICO |
| `ms11_1141_I` | ¿Por qué no hizo la denuncia?PENSÉ QUE NO VOLVERÍA A OCURRIR |
| `ms11_1141_J` | ¿Por qué no hizo la denuncia?NO CREÍA EN LA JUSTICIA |
| `ms11_1141_K` | ¿Por qué no hizo la denuncia?PENSÉ QUE ME COBRARÍAN. |
| `ms11_1141_L` | ¿Por qué no hizo la denuncia?RECIBÍ DINERO O PAGO EN ESPECIE |
| `ms11_1141_M` | ¿Por qué no hizo la denuncia?POR NO AFECTAR A LOS HIJOS |
| `ms11_1141_N` | ¿Por qué no hizo la denuncia?MIEDO A QUE ME QUITEN LOS HIJOS |
| `ms11_1141_X` | ¿Por qué no hizo la denuncia?OTRO |
| `ms11_1141_X_cod` | (ESPECIFIQUE) OTRO |
| `ms11_1142` | ¿Observó usted alguna vez agresiones físicas entre sus padres? |
| `ms11_1144_A` | ¿Quién cuida a sus hijas(os) la mayor parte del tiempo?PADRE |
| `ms11_1144_B` | ¿Quién cuida a sus hijas(os) la mayor parte del tiempo?MADRE |
| `ms11_1144_C` | ¿Quién cuida a sus hijas(os) la mayor parte del tiempo?PADRASTRO |
| `ms11_1144_D` | ¿Quién cuida a sus hijas(os) la mayor parte del tiempo?MADRASTRA |
| `ms11_1144_E` | ¿Quién cuida a sus hijas(os) la mayor parte del tiempo?ABUELO |
| `ms11_1144_F` | ¿Quién cuida a sus hijas(os) la mayor parte del tiempo?ABUELA |
| `ms11_1144_G` | ¿Quién cuida a sus hijas(os) la mayor parte del tiempo?HERMANO/A MAY OR |
| `ms11_1144_H` | ¿Quién cuida a sus hijas(os) la mayor parte del tiempo?TRABAJADOR/A DEL HOGAR |
| `ms11_1144_I` | ¿Quién cuida a sus hijas(os) la mayor parte del tiempo?MAESTRO (A) PARVULARIA/ EDUCADORAS |
| `ms11_1144_J` | ¿Quién cuida a sus hijas(os) la mayor parte del tiempo?TUTOR/ A |
| `ms11_1144_X` | ¿Quién cuida a sus hijas(os) la mayor parte del tiempo?OTRO: |
| `ms11_1144_Y` | ¿Quién cuida a sus hijas(os) la mayor parte del tiempo?NADIE |
| `ms11_1144_X_cod` | (ESPECIFIQUE) OTRO |
| `ms11_1145_A` | ¿Alguna persona castiga a sus hijas(os) en el hogar a título de educación, disciplina o corrección?PADRE |
| `ms11_1145_B` | ¿Alguna persona castiga a sus hijas(os) en el hogar a título de educación, disciplina o corrección?MADRE |
| `ms11_1145_C` | ¿Alguna persona castiga a sus hijas(os) en el hogar a título de educación, disciplina o corrección?PADRASTRO |
| `ms11_1145_D` | ¿Alguna persona castiga a sus hijas(os) en el hogar a título de educación, disciplina o corrección?MADRASTRA |
| `ms11_1145_E` | ¿Alguna persona castiga a sus hijas(os) en el hogar a título de educación, disciplina o corrección?ABUELO |
| `ms11_1145_F` | ¿Alguna persona castiga a sus hijas(os) en el hogar a título de educación, disciplina o corrección?ABUELA |
| `ms11_1145_G` | ¿Alguna persona castiga a sus hijas(os) en el hogar a título de educación, disciplina o corrección?H ER MAN A |
| `ms11_1145_H` | ¿Alguna persona castiga a sus hijas(os) en el hogar a título de educación, disciplina o corrección?HERMANO |
| `ms11_1145_I` | ¿Alguna persona castiga a sus hijas(os) en el hogar a título de educación, disciplina o corrección?TIO/ TIA |
| `ms11_1145_J` | ¿Alguna persona castiga a sus hijas(os) en el hogar a título de educación, disciplina o corrección?TUTOR/ TUTORA |
| `ms11_1145_X` | ¿Alguna persona castiga a sus hijas(os) en el hogar a título de educación, disciplina o corrección?OTRO |
| `ms11_1145_Z` | ¿Alguna persona castiga a sus hijas(os) en el hogar a título de educación, disciplina o corrección?NADIE/ NO LOS CASTIGAN |
| `ms11_1145_X_cod` | (ESPECIFIQUE) OTRO |
| `ms11_1147_AA` | A. B. En qué formaJALÓN DE OREJAS/ PALMADAS / SOPAPOS |
| `ms11_1147_AB` | A. B. En qué formaGOLPES CON: CHICOTE, CHINELAS, CINTURÓN, QUIMSA CHARANI |
| `ms11_1147_AC` | A. B. En qué forma GRITOS |
| `ms11_1147_AD` | A. B. En qué forma INSULTOS |
| `ms11_1147_AE` | A. B. En qué forma PRIVÁNDOLOS DE ALIMENTACIÓN |
| `ms11_1147_AF` | A. B. En qué forma DEJÁNDOLOS ENCERRADOS |
| `ms11_1147_AG` | A. B. En qué forma PONIÉNDOLES MÁS TRABAJO |
| `ms11_1147_AH` | A. B. En qué forma DEJÁNDOLOS FUERA DE CASA |
| `ms11_1147_AI` | A. B. En qué forma ECHÁNDOLES AGUA |
| `ms11_1147_AJ` | A. B. En qué forma QUITÁNDOLES LA ROPA QUE LES GUSTA |
| `ms11_1147_AK` | A. B. En qué forma IGNORÁNDOLOS MÁS DE UN DÍA |
| `ms11_1147_AL` | A. B. En qué forma QUITÁNDOLES RECREOS Y MESADAS |
| `ms11_1147_AM` | A. B. En qué forma PROHIBIENDO ALGO QUE LES GUSTA |
| `ms11_1147_AN` | A. B. En qué forma PROHIBIENDO EL USO O DECOMISANDO EL CEL |
| `ms11_1147_AO` | A. B. En qué forma SACUDON /ZARANDEO |
| `ms11_1147_AX` | A. B. En qué forma OTRA |
| `ms11_1147_AX_cod` | (ESPECIFIQUE OTRA) (A) En qué forma castiga Ud. a sus hijos varones? |
| `ms11_1147_BA` | B. En qu A. En q ué forma castig a Ud.JALÓN DE OREJAS/ PALMADAS / SOPAPOS |
| `ms11_1147_BB` | B. En qu A. En q ué forma castig a Ud.GOLPES CON: CHICOTE, CHINELAS, CINTURÓN, QUIMSA CHARANI |
| `ms11_1147_BC` | B. En qu A. En q ué forma castig a Ud.GRITOS |
| `ms11_1147_BD` | B. En qu A. En q ué forma castig a Ud.INSULTOS |
| `ms11_1147_BE` | B. En qu A. En q ué forma castig a Ud.PRIVÁNDOLOS DE ALIMENTACIÓN |
| `ms11_1147_BF` | B. En qu A. En q ué forma castig a Ud.DEJÁNDOLOS ENCERRADOS |
| `ms11_1147_BG` | B. En qu A. En q ué forma castig a Ud.PONIÉNDOLES MÁS TRABAJO |
| `ms11_1147_BH` | B. En qu A. En q ué forma castig a Ud.DEJÁNDOLOS FUERA DE CASA |
| `ms11_1147_BI` | B. En qu A. En q ué forma castig a Ud.ECHÁNDOLES AGUA |
| `ms11_1147_BJ` | B. En qu A. En q ué forma castig a Ud.QUITÁNDOLES LA ROPA QUE LES GUSTA |
| `ms11_1147_BK` | B. En qu A. En qué forma castig a Ud.IGNORÁNDOLOS MÁS DE UN DÍA |
| `ms11_1147_BL` | B. En qu A. En q ué forma castig a Ud.QUITÁNDOLES RECREOS Y MESADAS |
| `ms11_1147_BM` | B. En qu A. En q ué forma castig a Ud.PROHIBIENDO ALGO QUE LES GUSTA |
| `ms11_1147_BN` | B. En qu A. En q ué forma castig a Ud.PROHIBIENDO EL USO O DECOMISANDO EL CEL |
| `ms11_1147_BO` | B. En qu A. En q ué forma castig a Ud.SACUDON /ZARANDEO |
| `ms11_1147_BX` | B. En qu A. En q ué forma castig a Ud.OTRA |
| `ms11_1147_BX_cod` | (ESPECIFIQUE OTRA) (B) En qué forma castiga su esposa/compañera a sus hijos varones? |
| `ms11_1147_CA` | ¿De alg una otra forma? JALÓN DE OREJAS/ PALMADAS / SOPAPOS |
| `ms11_1147_CB` | ¿De alg una otra forma? GOLPES CON: CHICOTE, CHINELAS, CINTURÓN, QUIMSA CHARANI |
| `ms11_1147_CC` | ¿De alg una otra forma? GRITOS |
| `ms11_1147_CD` | ¿De alg una otra forma? INSULTOS |
| `ms11_1147_CE` | ¿De alg una otra forma? PRIVÁNDOLOS DE ALIMENTACIÓN |
| `ms11_1147_CF` | ¿De alg una otra forma? DEJÁNDOLOS ENCERRADOS |
| `ms11_1147_CG` | ¿De alg una otra forma? PONIÉNDOLES MÁS TRABAJO |
| `ms11_1147_CH` | ¿De alg una otra forma? DEJÁNDOLOS FUERA DE CASA |
| `ms11_1147_CI` | ¿De alg una otra forma? ECHÁNDOLES AGUA |
| `ms11_1147_CJ` | ¿De alg una otra forma? QUITÁNDOLES LA ROPA QUE LES GUSTA |
| `ms11_1147_CK` | ¿De alg una otra forma? IGNORÁNDOLOS MÁS DE UN DÍA |
| `ms11_1147_CL` | ¿De alg una otra forma? QUITÁNDOLES RECREOS Y MESADAS |
| `ms11_1147_CM` | ¿De alg una otra forma? PROHIBIENDO ALGO QUE LES GUSTA |
| `ms11_1147_CN` | ¿De alg una otra forma? PROHIBIENDO EL USO O DECOMISANDO EL CEL |
| `ms11_1147_CO` | ¿De alg una otra forma? SACUDON /ZARANDEO |
| `ms11_1147_CX` | ¿De alg una otra forma? OTRA |
| `ms11_1147_CX_cod` | (ESPECIFIQUE OTRA) (C) En qué forma castiga esa persona a sus hijos varones? |
| `ms11_1148_AA` | A. B. En q ué forma JALÓN DE OREJAS/ PALMADAS / SOPAPOS |
| `ms11_1148_AB` | A. B. En q ué forma GOLPES CON: CHICOTE, CHINELAS, CINTURÓN, QUIMSA CHARANI |
| `ms11_1148_AC` | A. B. En q ué forma GRITOS |
| `ms11_1148_AD` | A. B. En q ué forma INSULTOS |
| `ms11_1148_AE` | A. B. En q ué forma PRIVÁNDOLOS DE ALIMENTACIÓN |
| `ms11_1148_AF` | A. B. En q ué forma DEJÁNDOLOS ENCERRADOS |
| `ms11_1148_AG` | A. B. En q ué formaPONIÉNDOLES MÁS TRABAJO |
| `ms11_1148_AH` | A. B. En q ué formaDEJÁNDOLOS FUERA DE CASA |
| `ms11_1148_AI` | A. B. En q ué formaECHÁNDOLES AGUA |
| `ms11_1148_AJ` | A. B. En q ué formaQUITÁNDOLES LA ROPA QUE LES GUSTA |
| `ms11_1148_AK` | A. B. En q ué formaIGNORÁNDOLOS MÁS DE UN DÍA |
| `ms11_1148_AL` | A. B. En q ué formaQUITÁNDOLES RECREOS Y MESADAS |
| `ms11_1148_AM` | A. B. En q ué formaPROHIBIENDO ALGO QUE LES GUSTA |
| `ms11_1148_AN` | A. B. En q ué formaPROHIBIENDO EL USO O DECOMISANDO EL CEL |
| `ms11_1148_AO` | A. B. En q ué formaSACUDON /ZARANDEO |
| `ms11_1148_AX` | A. B. En q ué forma OTRA |
| `ms11_1148_AX_cod` | (ESPECIFIQUE OTRA) (A) En qué forma castiga Ud. a sus hijas mujeres? |
| `ms11_1148_BA` | HIJAS MUJERES - (B) En qué forma castiga Ud. a sus hijas mujeres? (JALÓN DE OREJAS/ PALMADAS / SOPAPOS) |
| `ms11_1148_BB` | HIJAS MUJERES - (B) En qué forma castiga Ud. a sus hijas mujeres? (GOLPES CON: CHICOTE, CHINELAS, CINTURÓN, QUIMSA CHARANI) |
| `ms11_1148_BC` | HIJAS MUJERES - (B) En qué forma castiga Ud. a sus hijas mujeres? (GRITOS) |
| `ms11_1148_BD` | HIJAS MUJERES - (B) En qué forma castiga Ud. a sus hijas mujeres? (INSULTOS) |
| `ms11_1148_BE` | HIJAS MUJERES - (B) En qué forma castiga Ud. a sus hijas mujeres? (PRIVÁNDOLOS DE ALIMENTACIÓN) |
| `ms11_1148_BF` | HIJAS MUJERES - (B) En qué forma castiga Ud. a sus hijas mujeres? (DEJÁNDOLOS ENCERRADOS) |
| `ms11_1148_BG` | HIJAS MUJERES - (B) En qué forma castiga Ud. a sus hijas mujeres? (PONIÉNDOLES MÁS TRABAJO) |
| `ms11_1148_BH` | HIJAS MUJERES - (B) En qué forma castiga Ud. a sus hijas mujeres? (DEJÁNDOLOS FUERA DE CASA) |
| `ms11_1148_BI` | HIJAS MUJERES - (B) En qué forma castiga Ud. a sus hijas mujeres? (ECHÁNDOLES AGUA) |
| `ms11_1148_BJ` | HIJAS MUJERES - (B) En qué forma castiga Ud. a sus hijas mujeres? (QUITÁNDOLES LA ROPA) |
| `ms11_1148_BK` | HIJAS MUJERES - (B) En qué forma castiga Ud. a sus hijas mujeres? (IGNORÁNDOLOS MÁS DE UN DÍA) |
| `ms11_1148_BL` | HIJAS MUJERES - (B) En qué forma castiga Ud. a sus hijas mujeres? (QUITÁNDOLES RECREOS Y MESADAS) |
| `ms11_1148_BM` | HIJAS MUJERES - (B) En qué forma castiga Ud. a sus hijas mujeres? (PROHIBIENDO ALGO QUE LES GUSTA) |
| `ms11_1148_BN` | HIJAS MUJERES - (B) En qué forma castiga Ud. a sus hijas mujeres? (PROHIBIENDO EL USO O DECOMISANDO EL CELULAR) |
| `ms11_1148_BO` | HIJAS MUJERES - (B) En qué forma castiga Ud. a sus hijas mujeres? (SACUDON /ZARANDEO) |
| `ms11_1148_BX` | HIJAS MUJERES - (B) En qué forma castiga Ud. a sus hijas mujeres? (OTRA:) |
| `ms11_1148_BX_cod` | (ESPECIFIQUE OTRA) (B) En qué forma castiga su esposa/compañera a sus hijas mujeres? |
| `ms11_1148_CA` | HIJAS MUJERES - (C) En qué forma castiga esa persona a sus hijas mujeres? (JALÓN DE OREJAS/ PALMADAS / SOPAPOS) |
| `ms11_1148_CB` | HIJAS MUJERES - (C) En qué forma castiga esa persona a sus hijas mujeres? (GOLPES CON: CHICOTE, CHINELAS, CINTURÓN, QUIMSA CHARANI) |
| `ms11_1148_CC` | HIJAS MUJERES - (C) En qué forma castiga esa persona a sus hijas mujeres? (GRITOS) |
| `ms11_1148_CD` | HIJAS MUJERES - (C) En qué forma castiga esa persona a sus hijas mujeres? (INSULTOS) |
| `ms11_1148_CE` | HIJAS MUJERES - (C) En qué forma castiga esa persona a sus hijas mujeres? (PRIVÁNDOLOS DE ALIMENTACIÓN) |
| `ms11_1148_CF` | HIJAS MUJERES - (C) En qué forma castiga esa persona a sus hijas mujeres? (DEJÁNDOLOS ENCERRADOS) |
| `ms11_1148_CG` | HIJAS MUJERES - (C) En qué forma castiga esa persona a sus hijas mujeres? (PONIÉNDOLES MÁS TRABAJO) |
| `ms11_1148_CH` | HIJAS MUJERES - (C) En qué forma castiga esa persona a sus hijas mujeres? (DEJÁNDOLOS FUERA DE CASA) |
| `ms11_1148_CI` | HIJAS MUJERES - (C) En qué forma castiga esa persona a sus hijas mujeres? (ECHÁNDOLES AGUA) |
| `ms11_1148_CJ` | ¿De alg una otra forma?QUITÁNDOLES RECREOS Y MESADAS |
| `ms11_1148_CK` | ¿De alg una otra forma?PROHIBIENDO ALGO QUE LES GUSTA |
| `ms11_1148_CL` | ¿De alg una otra forma?PROHIBIENDO EL USO O DECOMISANDO EL CEL |
| `ms11_1148_CM` | ¿De alg una otra forma?SACUDON /ZARANDEO |
| `ms11_1148_CN` | ¿De alg una otra forma?OTRA |
| `ms11_1148_CO` | HIJAS MUJERES - (C) En qué forma castiga esa persona a sus hijas mujeres? (SACUDON /ZARANDEO) |
| `ms11_1148_CX` | HIJAS MUJERES - (C) En qué forma castiga esa persona a sus hijas mujeres? (OTRA:) |
| `ms11_1148_CX_cod` | (ESPECIFIQUE OTRA) (C) En qué forma castiga esa persona a sus hijas mujeres? |
| `ms11_1149_A` | Generalmente, ¿en qué forma la castigan o castigaban a Ud sus padres o personas con las que creció?JALÓN DE OREJAS/ PALMADAS / SOPAPOS |
| `ms11_1149_B` | Generalmente, ¿en qué forma la castigan o castigaban a Ud sus padres o personas con las que creció?CINTURÓN, QUIMSA CHARANI |
| `ms11_1149_C` | Generalmente, ¿en qué forma la castigan o castigaban a Ud sus padres o personas con las que creció?GRITOS |
| `ms11_1149_D` | Generalmente, ¿en qué forma la castigan o castigaban a Ud sus padres o personas con las que creció?INSULTOS |
| `ms11_1149_E` | Generalmente, ¿en qué forma la castigan o castigaban a Ud sus padres o personas con las que creció?PRIVÁNDOLO DE ALIMENTACIÓN |
| `ms11_1149_F` | Generalmente, ¿en qué forma la castigan o castigaban a Ud sus padres o personas con las que creció?DEJÁNDOLO ENCERRADO |
| `ms11_1149_G` | Generalmente, ¿en qué forma la castigan o castigaban a Ud sus padres o personas con las que creció?PONIÉNDOLE MÁS TRABAJO |
| `ms11_1149_H` | Generalmente, ¿en qué forma la castigan o castigaban a Ud sus padres o personas con las que creció?DEJÁNDOLO FUERA DE CASA |
| `ms11_1149_I` | Generalmente, ¿en qué forma la castigan o castigaban a Ud sus padres o personas con las que creció?ECHÁNDOLE AGUA |
| `ms11_1149_J` | Generalmente, ¿en qué forma la castigan o castigaban a Ud sus padres o personas con las que creció?QUITÁNDOLE LA ROPA. |
| `ms11_1149_K` | Generalmente, ¿en qué forma la castigan o castigaban a Ud sus padres o personas con las que creció?IGNORÁNDOLO MÁS DE UN DÍA |
| `ms11_1149_L` | Generalmente, ¿en qué forma la castigan o castigaban a Ud sus padres o personas con las que creció?QUITÁNDOLE SU RECREO O MESADA |
| `ms11_1149_M` | Generalmente, ¿en qué forma la castigan o castigaban a Ud sus padres o personas con las que creció?PROHIBIENDOLE ALGO QUE LE GUSTA |
| `ms11_1149_N` | Generalmente, ¿en qué forma la castigan o castigaban a Ud sus padres o personas con las que creció?SACUDONES |
| `ms11_1149_X` | Generalmente, ¿en qué forma la castigan o castigaban a Ud sus padres o personas con las que creció?OTRA: |
| `ms11_1149_Y` | Generalmente, ¿en qué forma la castigan o castigaban a Ud sus padres o personas con las que creció?NO LO CASTIGABAN |
| `ms11_1149_X_cod` | (ESPECIFIQUE) OTRA |
| `ms11_1150` | ¿Cree Ud. que para educar a las/os hijas/os es necesario algún castigo?SI ES "SI", PREGUNTE: ¿A menudo o algunas veces?SI ES "NO", MARQUE NUNCA |
| `ms11_1151_A` | En su opinión se justifica que el padre o la madre castigue o lastime de manera física o verbal a sus hijas/osDESOBEDIENTES |
| `ms11_1151_B` | En su opinión se justifica que el padre o la madre castigue o lastime de manera física o verbal a sus hijas/osHACEN RENEGAR |
| `ms11_1151_C` | En su opinión se justifica que el padre o la madre castigue o lastime de manera física o verbal a sus hijas/osLLEGAN TARDE A CASA |
| `ms11_1151_D` | En su opinión se justifica que el padre o la madre castigue o lastime de manera física o verbal a sus hijas/osNO CUMPLEN |
| `ms11_1151_E` | En su opinión se justifica que el padre o la madre castigue o lastime de manera física o verbal a sus hijas/osLLORA |
| `ms11_1151_F` | En su opinión se justifica que el padre o la madre castigue o lastime de manera física o verbal a sus hijas/osEMBARAZAN A UNA NIÑA/ ADOLESCENTE |
| `ms11_1152_A` | ¿Cuál de los siguientes actos considera usted como violencia contra una/un niña/ niño/ adolescente:TOQUETEO |
| `ms11_1152_B` | ¿Cuál de los siguientes actos considera usted como violencia contra una/un niña/ niño/ adolescente:CONVENCER PARA TENER SEXO |
| `ms11_1152_C` | ¿Cuál de los siguientes actos considera usted como violencia contra una/un niña/ niño/ adolescente: ¿Cuál de los siguientes actos considera usted como violencia contra una/un niña/ niño/ adolescente:OTRAS ACTIVIDADES SEXUALES |
| `ms11_1152_D` | ¿Cuál de los siguientes actos considera usted como violencia contra una/un niña/ niño/ adolescente:s? AMENAZAS PARA TENER SEXO |
| `ms11_1152_E` | ¿Cuál de los siguientes actos considera usted como violencia contra una/un niña/ niño/ adolescente:RELACIONES SEXUALES |
| `ms11_1153` | ¿Alguna de sus hijas o alguno de sus hijos ha vivido alguna de estas situaciones? |
| `ms11_1154_A` | Según usted. ¿Quiénes sufren violencia muy frecuentemente, frecuentemente, con poca frecuencia, nunca?Niñas/niños |
| `ms11_1154_B` | Según usted. ¿Quiénes sufren violencia muy frecuentemente, frecuentemente, con poca frecuencia, nunca?Adolescentes |
| `ms11_1154_C` | Según usted. ¿Quiénes sufren violencia muy frecuentemente, frecuentemente, con poca frecuencia, nunca?Jovenes |
| `ms11_1154_D` | Según usted. ¿Quiénes sufren violencia muy frecuentemente, frecuentemente, con poca frecuencia, nunca?Mujeres |
| `ms11_1154_E` | Según usted. ¿Quiénes sufren violencia muy frecuentemente, frecuentemente, con poca frecuencia, nunca?Hombres |
| `ms11_1154_F` | Según usted. ¿Quiénes sufren violencia muy frecuentemente, frecuentemente, con poca frecuencia, nunca?Personas Adultas Mayores |
| `ms11_1154_G` | Según usted. ¿Quiénes sufren violencia muy frecuentemente, frecuentemente, con poca frecuencia, nunca?Población GLBTIQ |
| `ms11_1154_H` | Según usted. ¿Quiénes sufren violencia muy frecuentemente, frecuentemente, con poca frecuencia, nunca?Personas con discapacidad |
| `ms11_1155_A` | Si usted supiera que en su familia hay alguna persona que esta sufriendo violencia ¿Cómo piensa que se debería afrontar este problema?Buscando ayuda, sola |
| `ms11_1155_B` | Si usted supiera que en su familia hay alguna persona que esta sufriendo violencia ¿Cómo piensa que se debería afrontar este problema?Buscando apoyo de su familia |
| `ms11_1155_C` | Si usted supiera que en su familia hay alguna persona que esta sufriendo violencia ¿Cómo piensa que se debería afrontar este problema?Buscando apoyo de los servicios de atención |
| `ms11_1155_D` | Si usted supiera que en su familia hay alguna persona que esta sufriendo violencia ¿Cómo piensa que se debería afrontar este problema?Buscando apoyo del personal de salud |
| `ms11_1155_E` | Si usted supiera que en su familia hay alguna persona que esta sufriendo violencia ¿Cómo piensa que se debería afrontar este problema?Buscando apoyo de las ONGs u organizaciones sociales |
| `ms11_1155_X` | Si usted supiera que en su familia hay alguna persona que esta sufriendo violencia ¿Cómo piensa que se debería afrontar este problema?Otro |
| `ms11_1155_Z` | Si usted supiera que en su familia hay alguna persona que esta sufriendo violencia ¿Cómo piensa que se debería afrontar este problema?No sabe/no responde |
| `ms11_1155_X_cod` | (ESPECIFÍQUE) OTRO |
| `ms11_1157` | ¿Por favor dígame si alguna vez ha sido forzada por alguna persona (pareja o diferente a su pareja) a tener relaciones sexuales antes de cumplir los 18 años? |
| `ms11_1158` | ¿Alguna vez alguien le habló sobre la prevención de la violencia en el sistema de salud? |
| `ms11_1159` | Durante el periodo de cuarentena total (encierro)¿ha sufrido violencia física, psicológica o sexual? |
| `ms11_1160` | ¿Conoce alguna ley que protege los derechos de las personas que sufren violencia? |
| `ms11_1161_A` | ENTREVISTADOR TUVO QUE INTERRUMPIR LA ENTREVISTA DEBIDO A LA PRESENCIA DE OTRA PERSONA QUE TRATABA DE ESCUCHAR, O ENTRÓ EN EL CUARTO, O INTERRUMPIÓ EN ALGUNA OTRA FORMA?ESPOSO/COMPAÑERO/PAREJA |
| `ms11_1161_B` | ENTREVISTADOR TUVO QUE INTERRUMPIR LA ENTREVISTA DEBIDO A LA PRESENCIA DE OTRA PERSONA QUE TRATABA DE ESCUCHAR, O ENTRÓ EN EL CUARTO, O INTERRUMPIÓ EN ALGUNA OTRA FORMA?OTRO HOMBRE ADULTO |
| `ms11_1161_C` | ENTREVISTADOR TUVO QUE INTERRUMPIR LA ENTREVISTA DEBIDO A LA PRESENCIA DE OTRA PERSONA QUE TRATABA DE ESCUCHAR, O ENTRÓ EN EL CUARTO, O INTERRUMPIÓ EN ALGUNA OTRA FORMA?MUJER ADULTA |
| `ms11_1163_a` | HORA DE FINALIZACIÓN |
| `ms11_1163_b` | HORA DE FINALIZACIÓN (Minutos) |
| `ponderadorm` | Ponderador Mujer |
| `area` | Área |
| `region` | Región |
| `departamento` | Departamento |
| `b3_01` | Nacimiento del hijo01 en CMC |
| `b3_02` | Nacimiento del hijo02 en CMC |
| `b3_03` | Nacimiento del hijo03 en CMC |
| `b3_04` | Nacimiento del hijo04 en CMC |
| `b3_05` | Nacimiento del hijo05 en CMC |
| `b3_06` | Nacimiento del hijo06 en CMC |
| `b3_07` | Nacimiento del hijo07 en CMC |
| `b3_08` | Nacimiento del hijo08 en CMC |
| `b3_09` | Nacimiento del hijo09 en CMC |
| `b3_10` | Nacimiento del hijo10 en CMC |
| `b3_11` | Nacimiento del hijo11 en CMC |
| `b3_12` | Nacimiento del hijo12 en CMC |
| `b7_01` | Fallecimiento del hijo01 en CMC |
| `b7_02` | Fallecimiento del hijo02 en CMC |
| `b7_03` | Fallecimiento del hijo03 en CMC |
| `b7_04` | Fallecimiento del hijo04 en CMC |
| `b7_05` | Fallecimiento del hijo05 en CMC |
| `b7_06` | Fallecimiento del hijo06 en CMC |
| `b7_07` | Fallecimiento del hijo07 en CMC |
| `b7_08` | Fallecimiento del hijo08 en CMC |
| `b7_09` | Fallecimiento del hijo09 en CMC |
| `b7_10` | Fallecimiento del hijo10 en CMC |
| `b7_11` | Fallecimiento del hijo11 en CMC |
| `v008` | Fecha de entrevista en CMC |
| `v011` | Fecha de nacimiento en CMC |
| `idiomaninez` | Idioma que aprendio en la niñez |
| `niv_ed` | Nivel educativo detallado |
| `niv_ed_g` | Nivel educativo general |
| `aestudio` | Años de estudio |
| `econyugd_m` | Estado conyugal |
| `embadoles_m` | Embarazo adolescente |
| `cono_algmet` | Conocimiento de metodos anticonceptivos (Cualquier método) |
| `cono_metmod` | Conocimiento de metodos anticonceptivos (Métodos modernos) |
| `cono_mettra` | Conocimiento de metodos anticonceptivos (Métodos tradicionales) |
| `actmaconcep_cme_m` | Actualmente usa método anticonceptivo (Cualquier método) |
| `actmaconcep_mmo_m` | Actualmente usa método anticonceptivo (Métodos modernos) |
| `actmaconcep_mta_m` | Actualmente usa método anticonceptivo (Métodos tradicionales) |
| `actmaconcep_nin_m` | Actualmente usa método anticonceptivo (Ningún método) |
| `actuni_m` | Actualmente unida |
| `sexact_m` | Sexualmente activa |
| `condact_m` | Condición de actividad |
| `cob_m` | Grupo ocupacional |
| `deseo_m` | Deseo/Preferencia de Fecundidad |
| `deseog_m` | Deseo/Preferencia de Fecundidad agrupado |

---

## EDSA2023_Vivienda

**Casos:** 19059  
**Variables:** 73

**Descripcion:** La base de datos EDSA2023_vivienda, contiene información referente a las siguientes secciones del Cuestionario Hogar: Sección V: Características de la Vivienda Que incluyen los temas concernientes a características físicas de la vivienda (Paredes de la vivienda, Techo de la vivienda, Materiales del piso), Servicios básicos de energía eléctrica, principal fuente de abastecimiento de agua que los miembros del hogar utilizan para su consumo, servicio sanitario, tipo de combustible o energía utiliza para cocinar/preparar sus alimentos, condiciones de habitabilidad, convivencia con animales, equipamiento del hogar y hábitos saludables.

### Columnas y significados

| Columna | Significado |
|---|---|
| `folio` | Folio |
| `upm` | Unidad Primaria de Muestreo |
| `estrato` | Estrato |
| `hs04_0060` | ¿La vivienda es? |
| `hs04_0061` | ¿La vivienda que ocupa el hogar es? |
| `hs04_0061_cod` | (ESPECIFIQUE) ¿La vivienda que ocupa el hogar es? |
| `hs04_0062` | ¿Cuál es el material de construcción más utilizado en las paredes de esta vivienda? |
| `hs04_0062_cod` | (ESPECIFIQUE) ¿Cuál es el material de construcción más utilizado en las paredes de esta vivienda? |
| `hs04_0063` | ¿Las paredes interiores de esta vivienda tienen revoque? |
| `hs04_0064` | ¿Cuál es el material más utilizado en los techos de esta vivienda? |
| `hs04_0064_cod` | (ESPECIFIQUE) ¿Cuál es el material más utilizado en los techos de esta vivienda? |
| `hs04_0065` | ¿Cuál es el material más utilizado en los pisos de esta vivienda? |
| `hs04_0065_cod` | (ESPECIFIQUE) ¿Cuál es el material más utilizado en los pisos de esta vivienda? |
| `hs04_0066` | ¿Usa energía eléctrica para alumbrar esta vivienda? |
| `hs04_0067` | ¿Principalmente el agua para beber y cocinar, proviene de... |
| `hs04_0067_cod` | (ESPECIFIQUE) ¿Principalmente el agua para beber y cocinar, proviene de |
| `hs04_0068` | ¿Cuánto tiempo se demora en ir, recoger agua y volver (desde su hogar)? (expresado en MINUTOS) SI ES EN EL SITIO ESCRIBA: 996 |
| `hs04_0069` | ¿Usted hace algún tratamiento al agua para beber? |
| `hs04_0070` | ¿Generalmente en qué consiste ese tratamiento? |
| `hs04_0070_cod` | (ESPECIFIQUE) ¿Generalmente en qué consiste ese tratamiento? |
| `hs04_0071` | ¿Durante las últimas 2 semanas, con qué frecuencia ha estado disponible el agua de esta fuente? |
| `hs04_0072` | ¿Tiene baño, servicio sanitario o letrina? |
| `hs04_0073` | ¿Qué tipo de baño, servicio sanitario o letrina utilizan normalmente los miembros de su hogar? |
| `hs04_0074` | ¿El baño, servicio sanitario o letrina tiene desague... |
| `hs04_0075` | ¿El baño, servicio sanitario o letrina es usado sólo por su hogar o es compartido con otros hogares? |
| `hs04_0076` | Principalmente ¿Qué tipo de combustible o energía utiliza para cocinar/ preparar sus alimentos? |
| `hs04_0076_cod` | (ESPECIFIQUE) Principalmente ¿Qué tipo de combustible o energía utiliza para cocinar/ preparar sus alimentos? |
| `hs04_0077` | ¿Tiene un cuarto sólo para cocinar? |
| `hs04_0078` | ¿Cuántos cuartos o habitaciones ocupa los miembros de su hogar, sin contar baño, cocina, lavandería, garaje, depósito o negocio? NÚMERO DE HABITACIONES |
| `hs04_0079` | De estos cuartos o habitaciones, ¿Cuántos usan exclusivamente para dormir? NÚMERO DE DORMITORIOS |
| `hs04_0080_1_cod` | ¿Conviven con animales en el interior de la vivienda? Si la respuesta es positiva, preguntar ¿Qué animales? SELECCIONE LOS CÓDIGOS DE TODOS LOS ANIMALES MENCIONADOS. SONDEE: ¿Algún otro animal? (CON PERROS) |
| `hs04_0080_2_cod` | ¿Conviven con animales en el interior de la vivienda? Si la respuesta es positiva, preguntar ¿Qué animales? SELECCIONE LOS CÓDIGOS DE TODOS LOS ANIMALES MENCIONADOS. SONDEE: ¿Algún otro animal? (CON GATOS) |
| `hs04_0080_3_cod` | ¿Conviven con animales en el interior de la vivienda? Si la respuesta es positiva, preguntar ¿Qué animales? SELECCIONE LOS CÓDIGOS DE TODOS LOS ANIMALES MENCIONADOS. SONDEE: ¿Algún otro animal? (CON CONEJOS/CUISES) |
| `hs04_0080_4_cod` | ¿Conviven con animales en el interior de la vivienda? Si la respuesta es positiva, preguntar ¿Qué animales? SELECCIONE LOS CÓDIGOS DE TODOS LOS ANIMALES MENCIONADOS. SONDEE: ¿Algún otro animal? (CON GALLINAS) |
| `hs04_0080_5_cod` | ¿Conviven con animales en el interior de la vivienda? Si la respuesta es positiva, preguntar ¿Qué animales? SELECCIONE LOS CÓDIGOS DE TODOS LOS ANIMALES MENCIONADOS. SONDEE: ¿Algún otro animal? (CON OTROS ANIMALES) |
| `hs04_0080_6_cod` | ¿Conviven con animales en el interior de la vivienda? Si la respuesta es positiva, preguntar ¿Qué animales? SELECCIONE LOS CÓDIGOS DE TODOS LOS ANIMALES MENCIONADOS. SONDEE: ¿Algún otro animal? (NO TIENE ANIMALES) |
| `hs04_0080_X_cod` | (ESPECIFIQUE) ¿Conviven con animales en el interior de la vivienda? ¿Qué animales? |
| `hs04_0081_01` | (EQUIPOS) Tiene en su hogar: ¿Radio? |
| `hs04_0081_02` | (EQUIPOS) Tiene en su hogar: ¿Televisor? |
| `hs04_0081_03` | (EQUIPOS) Tiene en su hogar: ¿Equipo de música? |
| `hs04_0081_04` | (EQUIPOS) Tiene en su hogar: ¿Refrigerador? |
| `hs04_0081_05` | (EQUIPOS) Tiene en su hogar: ¿Cocina? |
| `hs04_0081_06` | (EQUIPOS) Tiene en su hogar: ¿Computadora, Laptop o PC? |
| `hs04_0081_07` | (EQUIPOS) Tiene en su hogar: ¿Lavadora de ropa? |
| `hs04_0081_08` | (EQUIPOS) Tiene en su hogar: ¿Calefón o termo tanque? |
| `hs04_0081_09` | (EQUIPOS) Tiene en su hogar: ¿Microondas? |
| `hs04_0081_10` | (SERVICIOS) Tiene en su hogar: ¿Teléfono fijo? |
| `hs04_0081_11` | (SERVICIOS) Tiene en su hogar: ¿Teléfono celular? |
| `hs04_0081_12` | (SERVICIOS) Tiene en su hogar: ¿Internet en el hogar? |
| `hs04_0081_13` | (SERVICIOS) Tiene en su hogar: ¿Televisión por cable? |
| `hs04_0081_14` | (MEDIOS DE TRANSPORTE) Tiene en su hogar: ¿Bicicleta? |
| `hs04_0081_15` | (MEDIOS DE TRANSPORTE) Tiene en su hogar: ¿Motocicleta o cuadratrac? |
| `hs04_0081_16` | (MEDIOS DE TRANSPORTE) Tiene en su hogar: ¿Vehículo automotor? |
| `hs04_0081_17` | (MEDIOS DE TRANSPORTE) Tiene en su hogar: Otro (Especifique) |
| `hs04_0081_X_cod` | (ESPECIFIQUE OTRO) |
| `hs04_0082` | Usted clasifica por el tipo de basura (Plástico, papel, vidrio. etc.) |
| `hs04_0083` | ¿Habitualmente que hace con la basura que genera el hogar? |
| `hs04_0083_cod` | (ESPECIFIQUE) ¿Habitualmente que hace con la basura que genera el hogar? |
| `hs04_0084` | POR OBSERVACIÓN: ¿Me podría mostrar el lugar dónde los miembros de su hogar se lavan más frecuentemente las manos? |
| `hs04_0085_01` | VERIFICAR SI CUENTA CON: A) Agua limpia |
| `hs04_0085_02` | VERIFICAR SI CUENTA CON: B) Jabón (en barra, líquido, polvo) |
| `hs04_0085_03` | VERIFICAR SI CUENTA CON: C) Toalla limpia |
| `hs04_0085_04` | VERIFICAR SI CUENTA CON: D) Ninguno |
| `hs04_0086` | ¿Añade sal extra a la comida ya servida (sopa o segundo)? |
| `hs04_0087` | ANOTE LA HORA DE FIN DE CUESTIONARIO |
| `hs05_0088` | ¿qué tipo de sal y que marca utilizó ayer para cocinar? |
| `hs05_0089` | El resultado de la prueba (de contenido de yodo en la sal) es: |
| `ponderadorhviv` | Ponderador hogar/ vivienda |
| `area` | Área |
| `region` | Región |
| `departamento` | Departamento |
| `qriqueza` | Quintil de riqueza |
| `cviv` | Indice de calidad de la vivienda |

---

## EDSA2023_Hogar

**Casos:** 54008  
**Variables:** 235

**Descripcion:** La base de datos EDSA2023_Hogar de la Encuesta de Demografía y Salud 2023 contiene información referente al Cuestionario Hogar con el propósito de: - Proporcionar información sobre las características generales del hogar y de las personas que habitan en el. - Identificar a mujeres y hombres elegibles para aplicar el Cuestionario Individual. - Identificar a niños/as nacidos/as a partir de enero del 2018 para aplicar las pruebas de hemoglobina, toma de peso y talla. Las secciones del Cuestionario Hogar que considera la base de datos son: Sección I. Composición del hogar Sección II. Educación Sección III. Salud

### Columnas y significados

| Columna | Significado |
|---|---|
| `folio` | Folio |
| `nro` | Número de orden de la persona |
| `upm` | Unidad Primaria de Muestreo |
| `estrato` | Estrato |
| `hs01_0101_1a` | Fecha de entrevista del hogar - Día |
| `hs01_0101_1b` | Fecha de entrevista del hogar - Mes |
| `hs01_0101_1c` | Fecha de entrevista del hogar - Año |
| `hs01_0003` | ¿es hombre o mujer? |
| `hs01_0004a` | ¿Cuántos años cumplidos tiene? |
| `hs01_0004b_1` | ¿Cuál es la fecha de su nacimiento? (DÍA) |
| `hs01_0004b_2` | ¿Cuál es la fecha de su nacimiento? (MES) |
| `hs01_0004b_3` | ¿Cuál es la fecha de su nacimiento? (AÑO) |
| `hs01_0005` | ¿Cuál es la relación o parentesco con el jefe/(la jefa) del hogar? |
| `hs01_0006_A` | NÚMERO DE ORDEN ESPOSO/A O COMPAÑERO/A |
| `hs01_0006_B` | NÚMERO DE ORDEN PADRE/PADRASTRO |
| `hs01_0006_C` | NÚMERO DE ORDEN MADRE/MADRASTRA |
| `hs01_0007` | CÓDIGO CUIDADOR/A PRINCIPAL |
| `hs01_0008` | ¿Cuál es el idioma o lengua en el que aprendió a hablar en su niñez? |
| `hs01_0008_cod` | (ESPECIFIQUE) OTRO NATIVO |
| `hs01_0009_A` | ¿Qué idiomas habla actualmente ? (QUECHUA) |
| `hs01_0009_B` | ¿Qué idiomas habla actualmente ? (AYMARA) |
| `hs01_0009_C` | ¿Qué idiomas habla actualmente ? (CASTELLANO) |
| `hs01_0009_D` | ¿Qué idiomas habla actualmente ? (GUARANÍ) |
| `hs01_0009_X` | ¿Qué idiomas habla actualmente ? (OTRO NATIVO) |
| `hs01_0009_X_cod` | (ESPECIFIQUE) OTRO NATIVO |
| `hs01_0009_Y` | ¿Qué idiomas habla actualmente ? |
| `hs01_0009_Y_cod` | (ESPECIFIQUE) EXTRANJERO |
| `hs01_0010` | ¿A qué nación o pueblo indígena originario campesino o afro boliviano pertenece? |
| `hs01_0010npioc` | ¿A cúal NPIOC? |
| `hs01_0011` | ¿vive habitualmente aquí? |
| `hs01_0012` | ¿Durmió anoche aquí? |
| `hs01_0017` | ¿Está vivo el padre biológico de? |
| `hs01_0018` | NÚMERO DE ORDEN DEL PADRE |
| `hs01_0019` | ¿Está viva la madre biológica de? |
| `hs01_0020` | NÚMERO DE ORDEN DE LA MADRE |
| `hs01_0021` | ¿Tiene Certificado o Acta de nacimiento?, ¿Puedo verlo? |
| `hs02_0022` | ¿Sabe leer y escribir? |
| `hs02_0023` | ¿ ha asistido alguna vez a la escuela, colegio o universidad? SI ES "NO" SONDEE: ¿Ni un solo año? |
| `hs02_0024_1` | ¿Cuál fue el nivel más alto de instrucción que aprobó? |
| `hs02_0024_2` | Ingrese el curso o grado. |
| `hs02_0025` | Actualmente, ¿ se inscribió o matriculó en algún curso o grado de educación escolar, alternativa, superior o postgrado? |
| `hs02_0026_1` | ¿A qué nivel y curso de educación escolar, alternativa, superior o postgrado se inscribió/matriculó este año? |
| `hs02_0026_2` | Ingrese el curso o grado |
| `hs02_0027` | Actualmente, ¿ asiste al nivel y curso al que se inscribió/matriculó este 2023? |
| `hs03_0029_A` | ¿ (Nombre) es beneficiario del SUS o está asegurado en una Caja de Salud o un seguro privado? (SUS) |
| `hs03_0029_B` | ¿ (Nombre) es beneficiario del SUS o está asegurado en una Caja de Salud o un seguro privado? (CAJAS DE SALUD) |
| `hs03_0029_C` | ¿ (Nombre) es beneficiario del SUS o está asegurado en una Caja de Salud o un seguro privado? (SEGURO PRIVADO) |
| `hs03_0029_F` | ¿ (Nombre) es beneficiario del SUS o está asegurado en una Caja de Salud o un seguro privado? (NO SABE) |
| `hs03_0029_X` | ¿ (Nombre) es beneficiario del SUS o está asegurado en una Caja de Salud o un seguro privado? (OTRO) |
| `hs03_0029_G` | ¿ (Nombre) es beneficiario del SUS o esta asegurado en una Caja de Salud o un seguro privado? (NINGUNO) |
| `hs03_0029_X_cod` | ¿ (Nombre) Especificar si es beneficiario de otro seguro |
| `hs03_0030` | ¿El año pasado 2022 (Nombre) ha ido o le han llevado a algún médico tradicional/ curandero/ naturista, partera? |
| `hs03_0031` | ¿El año pasado 2022 (Nombre) ha ido o le han llevado a algún establecimiento o servicio de salud |
| `hs03_0032_A` | Su visita al establecimiento de salud, fue por: ¿Control de salud/chequeo? |
| `hs03_0032_B` | Su visita al establecimiento de salud,fue por:¿Atencion por enfermedad? |
| `hs03_0032_C` | Su visita al establecimiento de salud, fue por: ¿Atención por accidente? |
| `hs03_0032_D` | Su visita al establecimiento de salud, fue por: ¿Atención por algún tipo de violencia? |
| `hs03_0032_E` | Su visita al establecimiento de salud, fue por: ¿Parto (vaginal o cesárea)? |
| `hs03_0032_F` | Su visita al establecimiento de salud, fue por :¿ informacion en salud? |
| `hs03_0033` | ¿(Nombre) Tuvo algún problema de salud en los últimos tres meses? |
| `hs03_0034_A` | El problema de salud que tuvo fue: ¿Diarrea? |
| `hs03_0034_B` | El problema de salud que tuvo fue: ¿Tos con respiración rápida y fiebre elevada? |
| `hs03_0034_C` | El problema de salud que tuvo fue: ¿Tos por más de 15 días? |
| `hs03_0034_D` | El problema de salud que tuvo fue: ¿Accidente/trauma/caída? |
| `hs03_0034_E` | El problema de salud que tuvo fue: ¿Heridas o golpes por agresión? |
| `hs03_0034_F` | El problema de salud que tuvo fue: ¿Problemas en la piel? |
| `hs03_0034_G` | El problema de salud que tuvo fue: ¿Problemas de la vista? |
| `hs03_0034_H` | El problema de salud que tuvo fue: ¿Problemas del oído? |
| `hs03_0034_I` | El problema de salud que tuvo fue: ¿Alguna discapacidad física, mental o sensorial? |
| `hs03_0034_J` | El problema de salud que tuvo fue: ¿Problema odontológico? |
| `hs03_0034_K` | El problema de salud que tuvo fue: ¿Malaria? |
| `hs03_0034_L` | El problema de salud que tuvo fue: ¿Dengue? |
| `hs03_0034_M` | El problema de salud que tuvo fue: ¿Chagas? |
| `hs03_0034_N` | El problema de salud que tuvo fue: ¿Leishmaniasis? |
| `hs03_0034_O` | El problema de salud que tuvo fue: ¿Patología (enfermedad) tradicional del lugar? |
| `hs03_0034_P` | El problema de salud que tuvo fue: ¿Influenza? |
| `hs03_0034_Q` | El problema de salud que tuvo fue: ¿Tuberculosis? |
| `hs03_0034_R` | El problema de salud que tuvo fue: ¿Cancer? |
| `hs03_0034_S` | El problema de salud que tuvo fue: ¿COVID-19? |
| `hs03_0034_T` | El problema de salud que tuvo fue: ¿Ansiedad, depresión? |
| `hs03_0034_X` | El problema de salud que tuvo fue: ¿Otro problema? |
| `hs03_0034_X_cod` | (ESPECIFIQUE) el otro problema de salud que tuvo? |
| `hs03_0035_A` | ¿A dónde fue o llevaron a para atender este(os) problema(s) de salud? ¿PUESTO DE SALUD? marcar las respuestas mencionadas |
| `hs03_0035_B` | ¿A dónde fue o llevaron a para atender este(os) problema(s) de salud? ¿CENTRO DE SALUD AMBULATORIO? marcar todas las respuestas mencionadas |
| `hs03_0035_C` | ¿A dónde fue o llevaron a para atender este(os) problema(s) de salud? ¿CENTRO DE SALUD CON INTERNACION? marcar todas las respuestas mencionadas |
| `hs03_0035_D` | ¿A dónde fue o llevaron a para atender este(os) problema(s) de salud? ¿CENTRO DE SALUD INTEGRAL? marcar las respuestas mencionadas |
| `hs03_0035_E` | ¿A dónde fue o llevaron a para atender este(os) problema(s) de salud? ¿HOSPITAL DE SEGUNDO NIVEL? marcar las respuestas mencionadas |
| `hs03_0035_F` | ¿A dónde fue o llevaron a para atender este(os) problema(s) de salud? ¿HOSPITAL DE TERCER NIVEL? marcar las respuestas mencionadas |
| `hs03_0035_G` | ¿A dónde fue o llevaron a para atender este(os) problema(s) de salud? ¿HOSPITAL ESPECIALIZADO? marcar las respuestas mencionadas |
| `hs03_0035_H` | ¿A dónde fue o llevaron a para atender este(os) problema(s) de salud? ¿CAJA NACIONAL DE SALUD? marcar las respuestas mencionadas |
| `hs03_0035_I` | ¿A dónde fue o llevaron a para atender este(os) problema(s) de salud? ¿CAJA DE LA BANCARIA PRIVADA? marcar las respuestas mencionadas |
| `hs03_0035_J` | ¿A dónde fue o llevaron a para atender este(os) problema(s) de salud? ¿CAJA PETROLERA? marcar las respuestas mencionadas |
| `hs03_0035_K` | ¿A dónde fue o llevaron a para atender este(os) problema(s) de salud? ¿CAJA DE LA BANCA ESTATAL? marcar las respuestas mencionadas |
| `hs03_0035_L` | ¿A dónde fue o llevaron a para atender este(os) problema(s) de salud? ¿CORDES? marcar las respuestas mencionadas |
| `hs03_0035_M` | ¿A dónde fue o llevaron a para atender este(os) problema(s) de salud? ¿CAJA DE CAMINOS? marcar las respuestas mencionadas |
| `hs03_0035_N` | ¿A dónde fue o llevaron a para atender este(os) problema(s) de salud? ¿COSSMIL/FFAA? marcar las respuestas mencionadas |
| `hs03_0035_O` | ¿A dónde fue o llevaron a para atender este(os) problema(s) de salud? ¿SEGURO UNIVERSITARIO? marcar las respuestas mencionadas |
| `hs03_0035_P` | ¿A dónde fue o llevaron a para atender este(os) problema(s) de salud? ¿ORGANISMOS PRIVADOS/PRIMER NIVEL, SEGUNDO NIVEL, TERCER NIVEL? marcar las respuestas mencionadas |
| `hs03_0035_Q` | ¿A dónde fue o llevaron a para atender este(os) problema(s) de salud? ¿ONG/IGLESIA PRIMER NIVEL, SEGUNDO NIVEL, TERCER NIVEL? marcar las respuestas mencionadas |
| `hs03_0035_R` | ¿A dónde fue o llevaron a para atender este(os) problema(s) de salud? ¿PROMOTOR DE LA SALUD/RPS/OTRO AGENTE? marcar las respuestas mencionadas |
| `hs03_0035_S` | ¿A dónde fue o llevaron a para atender este(os) problema(s) de salud? ¿VISITA DOMICILIARIA? marcar las respuestas mencionadas |
| `hs03_0035_T` | ¿A dónde fue o llevaron a para atender este(os) problema(s) de salud? ¿FARMACIA? marcar las respuestas mencionadas |
| `hs03_0035_U` | ¿A dónde fue o llevaron a para atender este(os) problema(s) de salud? ¿MEDICINA TRADICIONAL? marcar las respuestas mencionadas |
| `hs03_0035_V` | ¿A dónde fue o llevaron a para atender este(os) problema(s) de salud? ¿NO ACUDIO A NINGUN E.S. NO FUE? marcar las respuestas mencionadas |
| `hs03_0035_X` | ¿A dónde fue o llevaron a para atender este(os) problema(s) de salud? ¿OTRO LUGAR? marcar las respuestas mencionadas |
| `hs03_0035_Z` | ¿A dónde fue o llevaron a para atender este(os) problema(s) de salud? ¿NO SABE? marcar las respuestas mencionadas |
| `hs03_0035_X_cod` | (ESPECIFIQUE) el otro lugar a dónde fue o llevaron a para atender este(os) problema(s) de salud |
| `hs03_0037_A` | El personal de salud que le atiende a usted y/o su familia normalmente: A) ¿Les atiende en su idioma? |
| `hs03_0037_B` | El personal de salud que le atiende a usted y/o su familia normalmente: B) ¿Respeta sus costumbres? |
| `hs03_0037_C` | El personal de salud que le atiende a usted y/o su familia normalmente: C) ¿Les pide permiso para realizar un procedimiento medico? |
| `hs03_0037_D` | El personal de salud que le atiende a usted y/o su familia normalmente: D) ¿Les explica sobre el procedimiento medico que va a realizar? |
| `hs03_0037_E` | El personal de salud que le atiende a usted y/o su familia normalmente: E) ¿Acepta que ustedes tengan un acompañante cuando estan consultando? |
| `hs03_0037_F` | El personal de salud que le atiende a usted y/o su familia normalmente: F) ¿Respeta la privacidad de ustedes? |
| `hs03_0037_G` | El personal de salud que le atiende a usted y/o su familia normalmente: G) ¿Respeta su orientación sexual? |
| `hs03_0037_H` | El personal de salud que le atiende a usted y/o su familia normalmente: H) ¿Recibe buen trato sin discriminación? |
| `hs03_0037_I` | El personal de salud que le atiende a usted y/o su familia normalmente: I) ¿Les brinda información en temas de salud? |
| `hs03_0039_A` | ¿Por qué no fue o no llevaron a (NOMBRE) a un centro médico o servicio de salud? ¿Hay que esperar mucho? |
| `hs03_0039_B` | ¿Por qué no fue o no llevaron a (NOMBRE) a un centro médico o servicio de salud? ¿No hay donde esperar/incomodo? |
| `hs03_0039_C` | ¿Por qué no fue o no llevaron a (NOMBRE) a un centro médico o servicio de salud? ¿Personal poco amable? |
| `hs03_0039_D` | ¿Por qué no fue o no llevaron a (NOMBRE) a un centro médico o servicio de salud? ¿Personal sin experiencia no capacitado? |
| `hs03_0039_E` | ¿Por qué no fue o no llevaron a (NOMBRE) a un centro médico o servicio de salud? ¿No se encuentra al personal? |
| `hs03_0039_F` | ¿Por qué no fue o no llevaron a (NOMBRE) a un centro médico o servicio de salud? ¿No es limpio? |
| `hs03_0039_G` | ¿Por qué no fue o no llevaron a (NOMBRE) a un centro médico o servicio de salud? ¿queda muy lejos? |
| `hs03_0039_H` | ¿Por qué no fue o no llevaron a (NOMBRE) a un centro médico o servicio de salud? ¿No abre todos los dias? |
| `hs03_0039_I` | ¿Por qué no fue o no llevaron a (NOMBRE) a un centro médico o servicio de salud? ¿Horario de atencion inadecuado? |
| `hs03_0039_J` | ¿Por qué no fue o no llevaron a (NOMBRE) a un centro médico o servicio de salud? ¿No tenia dinero? |
| `hs03_0039_K` | ¿Por qué no fue o no llevaron a (NOMBRE) a un centro médico o servicio de salud? ¿No conoce el centro de salud? |
| `hs03_0039_L` | ¿Por qué no fue o no llevaron a (NOMBRE) a un centro médico o servicio de salud? ¿No atienden en nuestro idioma? |
| `hs03_0039_M` | ¿Por que no fue o no llevaron a (NOMBRE) a un centro medico o servicio de salud? ¿No existe personal? |
| `hs03_0039_X` | ¿Por que no fue o no llevaron a (NOMBRE) a un centro medico o servicio de salud? ¿Alguna otra razon? |
| `hs03_0039_Z` | ¿Por qué no fue o no llevaron a (NOMBRE) a un centro médico o servicio de salud? ¿No sabe? |
| `hs03_0039_X_cod` | ¿Por qué no fue o no llevaron a (NOMBRE) a un centro médico o servicio de salud? ¿Especifique la otra razon? |
| `hs03_0040` | ¿En los últimos tres meses usted recibió o compró medicamentos con receta médica al menos una vez? |
| `hs03_a_0041` | ¿Tiene algún problema de salud, herida o una enfermedad crónica diagnosticada en los últimos doce meses? |
| `hs03_a_0042_A` | El problema de salud que tiene es: A) ¿Diabetes? |
| `hs03_a_0042_B` | El problema de salud que tiene es: B) ¿Obesidad? |
| `hs03_a_0042_C` | El problema de salud que tiene es: C) ¿Hipertensión Arterial (presión alta)? |
| `hs03_a_0042_D` | El problema de salud que tiene es: D) ¿Cáncer? |
| `hs03_a_0042_E` | El problema de salud que tiene es: E) ¿Enfermedad del corazón o vasos sanguíneos? |
| `hs03_a_0042_F` | El problema de salud que tiene es: F) ¿Enfermedad respiratoria crónica? |
| `hs03_a_0042_G` | El problema de salud que tiene es: G) ¿Enfermedad renal? |
| `hs03_a_0042_H` | El problema de salud que tiene es: H) ¿Enfermedad bucodental? |
| `hs03_a_0042_X` | El problema de salud que tiene es: X) ¿Otro? |
| `hs03_a_0042_X_cod` | (ESPECIFIQUE) El problema de salud que tiene : |
| `hs03_a_0043_A` | ¿Dónde fue atendido por este(os) problema(s) de salud? ¿Algún otro lugar? PUESTO DE SALUD |
| `hs03_a_0043_B` | ¿Dónde fue atendido por este(os) problema(s) de salud? ¿Algún otro lugar? CENTRO DE SALUD AMBULATORIO |
| `hs03_a_0043_C` | ¿Dónde fue atendido por este(os) problema(s) de salud? ¿Algún otro lugar? CENTRO DE SALUD CON INTERNACIÓN |
| `hs03_a_0043_D` | ¿Dónde fue atendido por este(os) problema(s) de salud? ¿Algún otro lugar? CENTRO DE SALUD INTEGRAL |
| `hs03_a_0043_E` | ¿Dónde fue atendido por este(os) problema(s) de salud? ¿Algún otro lugar? HOSPITAL DE SEGUNDO NIVEL |
| `hs03_a_0043_F` | ¿Dónde fue atendido por este(os) problema(s) de salud? ¿Algún otro lugar? HOSPITAL DE TERCER NIVEL |
| `hs03_a_0043_G` | ¿Dónde fue atendido por este(os) problema(s) de salud? ¿Algún otro lugar? HOSPITAL ESPECIALIZADO |
| `hs03_a_0043_H` | ¿Dónde fue atendido por este(os) problema(s) de salud? ¿Algún otro lugar? CAJA NACIONA DE SALUD |
| `hs03_a_0043_I` | ¿Dónde fue atendido por este(os) problema(s) de salud? ¿Algún otro lugar? CAJA DE LA BANCA PRIVADA |
| `hs03_a_0043_J` | ¿Dónde fue atendido por este(os) problema(s) de salud? ¿Algún otro lugar? CAJA PETROLERA |
| `hs03_a_0043_K` | ¿Dónde fue atendido por este(os) problema(s) de salud? ¿Algún otro lugar? CAJA DE LA BANCA ESTATAL |
| `hs03_a_0043_L` | ¿Dónde fue atendido por este(os) problema(s) de salud? ¿Algún otro lugar? CORDES |
| `hs03_a_0043_M` | ¿Dónde fue atendido por este(os) problema(s) de salud? ¿Algún otro lugar? CAJA DE CAMINOS |
| `hs03_a_0043_N` | ¿Dónde fue atendido por este(os) problema(s) de salud? ¿Algún otro lugar? COSSMIL/FFAA |
| `hs03_a_0043_O` | ¿Dónde fue atendido por este(os) problema(s) de salud? ¿Algún otro lugar? SEGURO UNIVERSITARIO |
| `hs03_a_0043_P` | ¿Dónde fue atendido por este(os) problema(s) de salud? ¿Algún otro lugar? ORGANISMOS PRIVADOS |
| `hs03_a_0043_Q` | ¿Dónde fue atendido por este(os) problema(s) de salud? ¿Algún otro lugar? ONG/IGLESIA |
| `hs03_a_0043_R` | ¿Dónde fue atendido por este(os) problema(s) de salud? ¿Algún otro lugar? PROMOTOR DE LA SALUD |
| `hs03_a_0043_S` | ¿Dónde fue atendido por este(os) problema(s) de salud? ¿Algún otro lugar? VISITA DOMICILIARIA |
| `hs03_a_0043_T` | ¿Dónde fue atendido por este(os) problema(s) de salud? ¿Algún otro lugar? FARMACIA |
| `hs03_a_0043_U` | ¿Dónde fue atendido por este(os) problema(s) de salud? ¿Algún otro lugar? MEDICINA TRADICIONAL |
| `hs03_a_0043_V` | ¿Dónde fue atendido por este(os) problema(s) de salud? ¿Algún otro lugar? NO ACUDIÓ A NINGÚN E.S. |
| `hs03_a_0043_X` | ¿Dónde fue atendido por este(os) problema(s) de salud? ¿Algún otro lugar? OTRO LUGAR |
| `hs03_a_0043_Z` | ¿Dónde fue atendido por este(os) problema(s) de salud? ¿Algún otro lugar? NO SABE |
| `hs03_a_0043_X_cod` | (ESPECIFIQUE) ¿Dónde fue atendido por este(os) problema(s) de salud? |
| `hs03_a_0045_A` | ¿Por qué no fue o no llevaron a a un centro médico o servicio de salud? A) HAY QUE ESPERAR MUCHO |
| `hs03_a_0045_B` | ¿Por qué no fue o no llevaron a a un centro médico o servicio de salud? B) NO HAY DONDE ESPERAR/INCOMODO |
| `hs03_a_0045_C` | ¿Por qué no fue o no llevaron a a un centro médico o servicio de salud? C) CONSIDERA AL PERSONAL POCO AMABLE |
| `hs03_a_0045_D` | ¿Por qué no fue o no llevaron a a un centro médico o servicio de salud? D) CONSIDERA PERSONAL SIN EXPERIENCIA/NO CAPACITADO |
| `hs03_a_0045_E` | ¿Por qué no fue o no llevaron a a un centro médico o servicio de salud? E) NO SE ENCUENTRA AL PERSONAL |
| `hs03_a_0045_F` | ¿Por qué no fue o no llevaron a a un centro médico o servicio de salud? F) NO ES LIMPIO |
| `hs03_a_0045_G` | ¿Por qué no fue o no llevaron a a un centro médico o servicio de salud? G) QUEDA MUY LEJOS |
| `hs03_a_0045_H` | ¿Por qué no fue o no llevaron a a un centro médico o servicio de salud? H) NO ABREN TODOS LOS DIAS |
| `hs03_a_0045_I` | ¿Por qué no fue o no llevaron a a un centro médico o servicio de salud? I) HORARIO DE ATENCION INADECUADO |
| `hs03_a_0045_J` | ¿Por qué no fue o no llevaron a a un centro médico o servicio de salud? J) NO TENIA DINERO |
| `hs03_a_0045_K` | ¿Por qué no fue o no llevaron a a un centro médico o servicio de salud? K) NO CONOCE EL CENTRO DE SALUD |
| `hs03_a_0045_L` | ¿Por qué no fue o no llevaron a a un centro médico o servicio de salud? L) NO ATIENDEN EN NUESTRO IDIOMA |
| `hs03_a_0045_X` | ¿Por qué no fue o no llevaron a a un centro médico o servicio de salud? X) OTRA RAZON |
| `hs03_a_0045_Z` | ¿Por qué no fue o no llevaron a a un centro médico o servicio de salud? Z) NO SABE |
| `hs03_a_0045_X_cod` | (ESPECIFIQUE OTRA RAZÓN) ¿Por qué no fue o no llevaron a un centro médico o servicio de salud? |
| `hs03_b_0046` | ¿sabe que el Sistema Único de Salud (SUS) permite la atención gratuita a toda la población? |
| `hs03_b_0047` | ¿sabe que para recibir atención del SUS, (que no se trate de una urgencia o emergencia) debe acudir en primera instancia al establecimiento público de primer nivel más cercano a su domicilio? |
| `hs03_b_0048` | ¿sabe que a través del Servicio de Telesalud puede recibir atención médica domiciliaria a través de la teleconsulta mediante el uso de las TIC’s, de manera gratuita? |
| `hs03_c_0049_A` | ¿tiene dificultad permanente: Para ver, incluso cuando usa lentes? |
| `hs03_c_0049_B` | ¿tiene dificultad permanente: para oir, incluso cuando usa audifonos? |
| `hs03_c_0049_C` | ¿tiene dificultad permanente: Para caminar o subir gradas? |
| `hs03_c_0049_D` | ¿tiene dificultad permanente: Para aprender, recordar y concentrarse? |
| `hs03_c_0049_E` | ¿ tiene dificultad permanente: Para cuidarse, bañarse, vestirse y comer por si mismo? |
| `hs03_c_0049_F` | ¿tiene dificultad permanente: Para comunicarse o conversar? |
| `hs05_c_0051_01` | ¿Tiene Carnet de Discapacidad o afiliación al Instituto Boliviano de la Ceguera? |
| `hs03_c_0051_02_1` | Fecha del carnet de discapacidad: DÍA |
| `hs03_c_0051_02_2` | Fecha del carnet de discapacidad: MES |
| `hs03_c_0051_02_3` | Fecha del carnet de discapacidad: AÑO |
| `hs03_c_0051_03_cod` | TIPO DE DISCAPACIDAD - Codificado |
| `hs03_c_0051_04` | GRADO DISCAPACIDAD (En porcentaje) |
| `hs03_c_0052` | ¿Recibió algún tipo de rehabilitación en los últimos tres meses ? |
| `hs03_c_0053` | ¿Esta rehabilitación la recibió en su hogar o en un centro de rehabilitación? |
| `hs03_c_0054` | En que institución realizó su rehabilitación |
| `hs03_c_0054_cod` | (ESPECIFIQUE) En que institución realizó su rehabilitación |
| `hs03_c_0055_A` | ¿Utiliza algún tipo de ayuda técnica para su deficiencia o discapacidad? SILLA DE RUEDAS |
| `hs03_c_0055_B` | ¿Utiliza algún tipo de ayuda técnica para su deficiencia o discapacidad? ANDADORES |
| `hs03_c_0055_C` | ¿Utiliza algún tipo de ayuda técnica para su deficiencia o discapacidad? MULETAS |
| `hs03_c_0055_D` | ¿Utiliza algún tipo de ayuda técnica para su deficiencia o discapacidad? BASTÓN BLANCO |
| `hs03_c_0055_E` | ¿Utiliza algún tipo de ayuda técnica para su deficiencia o discapacidad? LENTES |
| `hs03_c_0055_F` | ¿Utiliza algún tipo de ayuda técnica para su deficiencia o discapacidad? AUDIFONOS |
| `hs03_c_0055_X` | ¿Utiliza algún tipo de ayuda técnica para su deficiencia o discapacidad? OTRO |
| `hs03_c_0055_Z` | ¿Utiliza algún tipo de ayuda técnica para su deficiencia o discapacidad? NO UTILIZA |
| `hs03_c_0055_X_cod` | (ESPECIFIQUE) Utiliza algún tipo de ayuda técnica para su deficiencia o discapacidad |
| `hs03_c_0056_a` | ¿Cuántas veces recibe o recibió el Alimento Complementario Carmelo en un año? |
| `hs03_c_0057` | ¿Consume o consumió el Alimento Complementario Carmelo? |
| `hs03_c_0058` | ¿Conoce la correcta preparación del Alimento Complementario Carmelo? |
| `hs03_c_0059` | ¿Considera que el Alimento Complementario Carmelo contribuye a su salud y nutrición? |
| `factorexph` | factor de expansión |
| `ponderadorhviv` | Ponderador hogar/ vivienda |
| `area` | Área |
| `region` | Región |
| `departamento` | Departamento |
| `ed_cmc` | Edad del encuestado en CMC |
| `idiomaninez` | Idioma que aprendio en la niñez |
| `niv_ed` | Nivel educativo detallado |
| `niv_ed_g` | Nivel educativo general |
| `aestudio` | Años de estudio |
| `tipohogar` | Tipología del hogar |
| `nro_tot` | Numero total de residentes del hogar |
| `afilsegsal` | Afiliación seguro de salud |
| `valid_muj` | Registros elegibles para la boleta mujer |
| `valid_hom` | Registros elegibles para la boleta hombre |
| `valid_nin` | Registros elegibles para la boleta primera infancia |
| `sub` | submuestra |
| `niv_ed_o` | Nivel educativon detallado (anterior) |
| `niv_ed_g_o` | Nivel educativo general (anterior) |

---

## EDSA2023_HistorialHijos

**Casos:** 22360  
**Variables:** 26

**Descripcion:** La base de datos EDSA2023_HistorialHijos de la Encuesta de Demografía y Salud 2023 contiene información referente al Cuestionario de la Mujer, que se encuentra en la Sección II. Reproducción, Historia de Nacimientos (Preguntas 215 a la 225), donde se obtiene información específica sobre el nacimiento de cada uno de los/as hijos/as nacidos/as vivos/as de la mujer (fecha de nacimiento, edad, sexo, supervivencia, etc.). La información contenida en esta base de datos son utilizadas para el cálculo de indicadores, tanto de la fecundidad (nivel de la fecundidad, fecundidad adolescente, espaciamiento de los nacimientos, etc.; también de la mortalidad infantil (neo y pos neonatal), mortalidad infantil, post-infantil y en la niñez. El objetivo de esta información es tener una lista completa de todos los/as hijos/as nacidos/as vivos/as que ha tenido la mujer, en el orden en que han ocurrido esos nacimientos.

### Columnas y significados

| Columna | Significado |
|---|---|
| `folio` | Folio |
| `nro` | Número de orden de la persona |
| `upm` | Unidad Primaria de Muestreo |
| `ms02_0216` | Número de nacimiento |
| `ms01_0101_1a` | Fecha de entrevista - Día |
| `ms01_0101_1b` | Fecha de entrevista - Mes |
| `ms01_0101_1c` | Fecha de entrevista - Año |
| `ms02_0217` | ¿El nacimiento fue parto único o múltiple? (mellizos, trillizos, etc.) |
| `ms02_0218` | ¿Es Mujer u Hombre? |
| `ms02_0219_1` | ¿En qué fecha nació [ms02_0216]? (MES) |
| `ms02_0219_2` | ¿En qué AÑO nació [ms02_0216]? |
| `ms02_0220` | ¿Está viva/o [ms02_0216]? |
| `ms02_0221` | ¿Cuántos años cumplidos tiene? |
| `ms02_0222` | ¿Está [ms02_0216] viviendo con usted? |
| `ms02_0223` | NÚMERO DE ORDEN DEL CUESTIONARIO HOGAR |
| `ms02_0224` | ¿Qué edad tenía [ms02_0216] cuando murió? (FRECUENCIA) |
| `ms02_0224_1` | ¿Qué edad tenía [ms02_0216] cuando murió? (PERIODO) |
| `ms02_0225` | ¿Cuál fue la causa por la que murió [ms02_0216]? |
| `ms02_0225_cod` | (ESPECIFICAR) OTROS |
| `estrato` | Estrato |
| `departamento` | Departamento |
| `area` | Área |
| `ponderadorm` | Ponderador Mujer |
| `b3` | Fecha de nacimiento en CMC |
| `v008` | Fecha de entrevista en CMC |
| `ms02_0223_o` | NÚMERO DE ORDEN DEL CUESTIONARIO HOGAR (anterior) |

---

## EDSA2023_Hombre

**Casos:** 5878  
**Variables:** 997

**Descripcion:** El Cuestionario Hombre consta de 8 secciones, que son: - Sección I. Antecedentes del entrevistado - Sección II. Reproducción - Sección III. Anticoncepción/Planificación familiar - Sección IV. Nupcialidad y actividad sexual - Sección V. Preferencias de fecundidad - Sección VI. Participación en el cuidado de la salud - Sección VII. VIH/SIDA e infecciones de transmisión sexual - Sección VIII. Violencia al hombre

### Columnas y significados

| Columna | Significado |
|---|---|
| `folio` | Folio |
| `nro` | Número de orden de la persona |
| `upm` | Unidad Primaria de Muestreo |
| `estrato` | Estrato |
| `vs01_0101_1a` | Fecha de entrevista - Día |
| `vs01_0101_1b` | Fecha de entrevista - Mes |
| `vs01_0101_1c` | Fecha de entrevista - Año |
| `vs01_0101_a` | Hora de inicio de la entrevista (Hora) |
| `vs01_0101_b` | Hora de inicio de la entrevista (Minutos) |
| `vs01_0101a` | ¿Cuántos años cumplidos tiene usted? |
| `vs01_0101a_1` | ¿Cuál es la fecha de su nacimiento? (dia) |
| `vs01_0101a_2` | ¿Cuál es la fecha de su nacimiento?(mes) |
| `vs01_0101a_3` | ¿Cuál es la fecha de su nacimiento?(año) |
| `vs01_0102` | ¿Dónde nació?SI LA RESPUESTA ES "EN OTRO LUGAR DEL PAIS" O "EN EL EXTERIOR" INDAGUE: ¿En cuál lugar nació? |
| `vs01_0102_02_cod` | (ESPECIFIQUE MUNICIPIO) ¿Dónde nació? EN QUE OTRO LUGAR DEL PAÍS |
| `vs01_0102_04_cod` | (ESPECIFIQUE) ¿Dónde nació? EN EL EXTERIOR |
| `vs01_0103` | ¿Dónde vive habitualmente?SI LA RESPUESTA ES "EN OTRO LUGAR DEL PAIS" O "EN EL EXTERIOR" INDAGUE:¿En cuál lugar vive habitualmente? |
| `vs01_0103_02_cod` | (ESPECIFIQUE MUNICIPIO) ¿Dónde vive habitualmente? EN QUE OTRO LUGAR DEL PAÍS |
| `vs01_0103_04_cod` | (ESPECIFIQUE) ¿Dónde vive habitualmente? EN EL EXTERIOR |
| `vs01_0104` | ¿Dónde vivía hace 5 años?SI LA RESPUESTA ES "EN OTRO LUGAR DEL PAIS" O "EN EL EXTERIOR" INDAGUE:¿En cuál lugar vivía? |
| `vs01_0104_02_cod` | (ESPECIFÍQUE MUNICIPIO) ¿Dónde vivía hace 5 años? EN OTRO LUGAR DEL PAÍS |
| `vs01_0104_04_cod` | (ESPECIFÍQUE) ¿Dónde vivía hace 5 años? EN EL EXTERIOR |
| `vs01_0105` | ¿Cuál fue la razón principal por la que se trasladó a otro lugar? |
| `vs01_0105_cod` | (ESPECIFÍQUE) ¿Cuál fue la razón principal por la que se trasladó a otro lugar? |
| `vs01_0106` | ¿Cuál es el idioma o lengua en el que aprendió a hablar en su niñez? |
| `vs01_0106_cod` | (ESPECIFIQUE OTRO NATIVO) ¿Cuál es el idioma o lengua en el que aprendió a hablar en su niñez ? |
| `vs01_0107_A` | ¿Qué idiomas habla actualmente? (QUECHUA) |
| `vs01_0107_B` | ¿Qué idiomas habla actualmente? (AYMARA) |
| `vs01_0107_C` | ¿Qué idiomas habla actualmente? (CASTELLANO) |
| `vs01_0107_D` | ¿Qué idiomas habla actualmente? (GUARANÍ) |
| `vs01_0107_X` | ¿Qué idiomas habla actualmente? (OTRO NATIVO) |
| `vs01_0107_X_cod` | ESPECIFIQUE OTRO IDIOMA NATIVO ¿Qué idiomas habla actualmente? |
| `vs01_0107_Y` | ¿Qué idiomas habla actualmente? (EXTRANJERO) |
| `vs01_0107_Y_cod` | (ESPECIFIQUE IDIOMA EXTRANJERO) ¿Qué idiomas habla actualmente? |
| `vs01_0108` | ¿A que nación o pueblo indígena originario campesino o afro boliviano pertenece? |
| `vs01_0108_npiocs` | (ESPECIFÍQUE) NACIÓN O PUEBLO INDIGENA ORIGINARIO CAMPESINO O AFROBOLIVIANO |
| `vs01_0111` | ¿Asistió usted alguna vez a la escuela o colegio, universidad, curso de Alfabetización? |
| `vs01_0112_1` | ¿Cuál fue el Nivel más alto de instrucción que aprobó? |
| `vs01_0112_2` | ¿Cuál fue el Curso más alto de instrucción que aprobó? |
| `vs01_0114` | ¿Actualmente está asistiendo a la escuela, colegio, instituto superior o universidad? |
| `vs01_0115` | ¿Cuál fue la principal razón por la que no asiste a la escuela, colegio, instituto superior o universidad? |
| `vs01_0115_cod` | (ESPECIFIQUE OTRA RAZÓN) ¿Cuál fue la principal razón por la que no asiste a la escuela, colegio, instituto superior o universidad? |
| `vs01_0117` | ¿Alguna vez ha participado usted en un programa de alfabetización o programa YO SI PUEDO? |
| `vs01_0118` | Ahora me gustaría que usted lea en voz alta cada una de las siguientes frases:MUESTRE LA TARJETA AL ENTREVISTADO SI EL ENTREVISTADO NO PUEDE LEER TODA LA FRASE INDAGUE:¿Puede leer alguna parte de la frase? |
| `vs01_0118_esp` | (ESPECIFIQUE EL IDIOMA) NO HAY TARJETA EN EL IDIOMA REQUERIDO |
| `vs01_0119` | ¿Cuántos días a la semana lee usted un periódico? (impreso o digital) |
| `vs01_0120` | ¿Cuántos días a la semana escucha usted radio? |
| `vs01_0121` | ¿Cuántos días a la semana mira usted televisión? |
| `vs01_0122` | ¿Cuántos días a la semana entra a internet o a una red social? |
| `vs01_0123_A` | Durante la última semana ¿realizó usted algunas de las siguientes actividades físicas y/o deportivas por 30 minutos o más: A. Levantar cosas pesadas? |
| `vs01_0123_B` | Durante la última semana ¿realizó usted algunas de las siguientes actividades físicas y/o deportivas por 30 minutos o más: B. Manejar bicicleta? |
| `vs01_0123_C` | Durante la última semana ¿realizó usted algunas de las siguientes actividades físicas y/o deportivas por 30 minutos o más: C. Caminar? |
| `vs01_0123_D` | Durante la última semana ¿realizó usted algunas de las siguientes actividades físicas y/o deportivas por 30 minutos o más: D. Subir gradas o pendientes? |
| `vs01_0123_E` | Durante la última semana ¿realizó usted algunas de las siguientes actividades físicas y/o deportivas por 30 minutos o más: E. Bailar? |
| `vs01_0123_F` | Durante la última semana ¿realizó usted algunas de las siguientes actividades físicas y/o deportivas por 30 minutos o más: F. Trotar? |
| `vs01_0123_G` | Durante la última semana ¿realizó usted algunas de las siguientes actividades físicas y/o deportivas por 30 minutos o más: G. Correr? |
| `vs01_0123_X` | Durante la última semana ¿realizó usted algunas de las siguientes actividades físicas y/o deportivas por 30 minutos o más: X. Alguna otra? |
| `vs01_0123_X_cod` | (ESPECIFIQUE) Durante la última semana ¿realizó usted algunas de las siguientes actividades físicas y/o deportivas por 30 minutos o más: Alguna otra? |
| `vs01_0124` | Durante la última semana ¿Cuántos días realizó actividades físicas y/o deportivas por 30 minutos o más? NÚMERO DE DIAS A LA SEMANA |
| `vs01_0125` | ¿Cuántas horas pasa sentado diariamente? NÚMERO DE HORAS AL DIA |
| `vs01_0126` | ¿Usted cree que realizar actividades físicas y/o deportivas es beneficioso para su salud? |
| `vs01_0127` | Durante el ultimo mes ¿sintió dolor de cabeza y/o zumbido en los oídos y/o sangrado por la nariz? |
| `vs01_0128` | Durante el ultimo mes ¿Sintió disminución de peso aumento de la frecuencia para orinar, aumento de la sed o aumento del apetito? |
| `vs01_0129` | Durante las ultimas dos semanas, ¿usted donde consumió con MAYOR FRECUENCIA las comidas principales? |
| `vs01_0130_A` | Ahora quisiera preguntarle acerca de los diferentes tipos de alimentos que usted CONSUMIÓ durante el día de ayer por separado o con otros alimentos.1. CEREALES, TUBERCULOS Y DERIVADOS(A) Cereales y derivados: Arroz, fideo, quinua, pan, galletas, otros. |
| `vs01_0130_B` | Ahora quisiera preguntarle acerca de los diferentes tipos de alimentos que usted CONSUMIÓ durante el día de ayer por separado o con otros alimentos.1. CEREALES, TUBERCULOS Y DERIVADOS(B) Leguminosas: Lenteja, poroto, frijol, tarhui y otros |
| `vs01_0130_C` | Ahora quisiera preguntarle acerca de los diferentes tipos de alimentos que usted CONSUMIÓ durante el día de ayer por separado o con otros alimentos.1. CEREALES, TUBERCULOS Y DERIVADOS(C) Tubérculos: Papa, oca, yuca, chuño y otros |
| `vs01_0130_D` | Ahora quisiera preguntarle acerca de los diferentes tipos de alimentos que usted CONSUMIÓ durante el día de ayer por separado o con otros alimentos.2. VERDURAS(D) Color verde obscuro: Acelga, espinaca, apio, brócoli y otros |
| `vs01_0130_E` | Ahora quisiera preguntarle acerca de los diferentes tipos de alimentos que usted CONSUMIÓ durante el día de ayer por separado o con otros alimentos.2. VERDURAS(E) Color amarillo a naranja por dentro: zapallo, zanahoria |
| `vs01_0130_F` | Ahora quisiera preguntarle acerca de los diferentes tipos de alimentos que usted CONSUMIÓ durante el día de ayer por separado o con otros alimentos.2. VERDURAS(F) Cualquier otra verdura |
| `vs01_0130_G` | Ahora quisiera preguntarle acerca de los diferentes tipos de alimentos que usted CONSUMIÓ durante el día de ayer por separado o con otros alimentos.3. FRUTAS(G) Color amarillo a naranja por dentro: papaya, mango, piña, otros |
| `vs01_0130_H` | Ahora quisiera preguntarle acerca de los diferentes tipos de alimentos que usted CONSUMIÓ durante el día de ayer por separado o con otros alimentos.3. FRUTAS(H) Cualquier otra fruta |
| `vs01_0130_I` | Ahora quisiera preguntarle acerca de los diferentes tipos de alimentos que usted CONSUMIÓ durante el día de ayer por separado o con otros alimentos.4. LACTEOS Y DERIVADOS(I) Leche, yogurt, queso y otros |
| `vs01_0130_J` | Ahora quisiera preguntarle acerca de los diferentes tipos de alimentos que usted CONSUMIÓ durante el día de ayer por separado o con otros alimentos.5. CARNES, DERIVADOS Y HUEVOS(J) Res, Hígado, Riñón, Corazón |
| `vs01_0130_K` | Ahora quisiera preguntarle acerca de los diferentes tipos de alimentos que usted CONSUMIÓ durante el día de ayer por separado o con otros alimentos.5. CARNES, DERIVADOS Y HUEVOS(K) Pollo, Pescado, Mariscos, Cerdo, Cordero, Llama, Conejo y vísceras |
| `vs01_0130_L` | Ahora quisiera preguntarle acerca de los diferentes tipos de alimentos que usted CONSUMIÓ durante el día de ayer por separado o con otros alimentos.5. CARNES, DERIVADOS Y HUEVOS(L) Huevo |
| `vs01_0130_M` | Ahora quisiera preguntarle acerca de los diferentes tipos de alimentos que usted CONSUMIÓ durante el día de ayer por separado o con otros alimentos.6. GRASAS Y DERIVADOS(M) Aceite vegetal, oliva, girasol, maíz, soja y otros |
| `vs01_0130_N` | Ahora quisiera preguntarle acerca de los diferentes tipos de alimentos que usted CONSUMIÓ durante el día de ayer por separado o con otros alimentos.6. GRASAS Y DERIVADOS(N) Manteca, cebo, margarina |
| `vs01_0130_O` | Ahora quisiera preguntarle acerca de los diferentes tipos de alimentos que usted CONSUMIÓ durante el día de ayer por separado o con otros alimentos.6. GRASAS Y DERIVADOS(O) Mantequilla |
| `vs01_0130_P` | Ahora quisiera preguntarle acerca de los diferentes tipos de alimentos que usted CONSUMIÓ durante el día de ayer por separado o con otros alimentos.7. AZUCARES(P) Azúcar blanca |
| `vs01_0130_Q` | Ahora quisiera preguntarle acerca de los diferentes tipos de alimentos que usted CONSUMIÓ durante el día de ayer por separado o con otros alimentos.7. AZUCARES(Q) Azúcar morena, miel, chancaca y otros |
| `vs01_0130_R` | Ahora quisiera preguntarle acerca de los diferentes tipos de alimentos que usted CONSUMIÓ durante el día de ayer por separado o con otros alimentos.8. OTROS(R) ¿Agua? |
| `vs01_0130_S` | Ahora quisiera preguntarle acerca de los diferentes tipos de alimentos que usted CONSUMIÓ durante el día de ayer por separado o con otros alimentos.8. OTROS(S) Otros líquidos(te, mate, café) |
| `vs01_0131_A` | Ahora me gustaría preguntarle acerca del consumo en la última semana de los siguientes productosA. (COMIDA RAPIDA)Pollo broaster, Hamburguesa, Salchipapa, Hot dog, papas fritas y otras frituras |
| `vs01_0131_B` | Ahora me gustaría preguntarle acerca del consumo en la última semana de los siguientes productosB. (BEBIDAS AZUCARADAS)Bebidas con gas, Néctar, Jugos envasados, Energizantes, Otros |
| `vs01_0131_C` | Ahora me gustaría preguntarle acerca del consumo en la última semana de los siguientes productosC. (ALIMENTOS PROCESADOS)Tortas, queques, roscas, galletas dulces/dulces/saladas y otros |
| `vs01_0132_A` | A. ¿Se ha sentido nervioso, tenso, irritable en el trabajo? |
| `vs01_0133_A` | Me podría decir si... ¿Esa sensación ha interferido con alguna de sus actividades cotidianas? |
| `vs01_0132_B` | B. ¿Se ha sentido nervioso, tenso, irritable en su vida social? |
| `vs01_0133_B` | Me podría decir si...¿Esa sensación ha interferido con alguna de sus actividades cotidianas? |
| `vs01_0132_C` | C. ¿Se ha sentido nervioso, tenso, irritable en sus estudios? |
| `vs01_0133_C` | Me podría decir si...¿Esa sensación ha interferido con alguna de sus actividades cotidianas? |
| `vs01_0132_D` | D. ¿Se ha sentido nervioso, tenso, irritable en su familia? |
| `vs01_0133_D` | Me podría decir si...¿Esa sensación ha interferido con alguna de sus actividades cotidianas? |
| `vs01_0134` | ¿Se siente triste o llora con mucha frecuencia? |
| `vs01_0135` | ¿Ya no disfruta de actividades de las que antes disfrutaba? |
| `vs01_0136` | ¿Ha pensado alguna vez en hacerse daño, en acabar con su vida o en la muerte? |
| `vs01_0137` | ¿En los últimos 12 meses usted ha tomado bebidas alcohólicas? |
| `vs01_0138` | ¿Con qué frecuencia ha tomado bebidas alcohólicas? PREGUNTE LA CANTIDAD DE VASOS QUE HA TOMADO |
| `vs01_0138_01` | (Nº DE VASOS) ¿Con qué frecuencia ha tomado bebidas alcohólicas? |
| `vs01_0139_A` | ¿Alguna vez el consumo de bebidas alcohólicas ha interferido con sus actividades cotidianas:A. En su trabajo? |
| `vs01_0139_B` | ¿Alguna vez el consumo de bebidas alcohólicas ha interferido con sus actividades cotidianas:B. En sus estudios? |
| `vs01_0139_C` | ¿Alguna vez el consumo de bebidas alcohólicas ha interferido con sus actividades cotidianas:C. En su familia? |
| `vs01_0139_D` | ¿Alguna vez el consumo de bebidas alcohólicas ha interferido con sus actividades cotidianas:D. En su salud? |
| `vs01_0139_X` | ¿Alguna vez el consumo de bebidas alcohólicas ha interferido con sus actividades cotidianas:X. Otra actividad? (Especifique) |
| `vs01_0139_X_cod` | (ESPECIFIQUE) ¿Alguna vez el consumo de bebidas alcohólicas ha interferido con sus actividades cotidianas? |
| `vs01_0140_A` | ¿Alguna vez, bajo el efecto del consumo de bebidas alcohólicas, usted ha provocado o ha cometido acciones que atentan contra otras personas tales como:A. Agresiones a su pareja? |
| `vs01_0140_B` | ¿Alguna vez, bajo el efecto del consumo de bebidas alcohólicas, usted ha provocado o ha cometido acciones que atentan contra otras personas tales como:B. Agresiones a sus hijas/os? |
| `vs01_0140_C` | ¿Alguna vez, bajo el efecto del consumo de bebidas alcohólicas, usted ha provocado o ha cometido acciones que atentan contra otras personas tales como:C. Agresiones a terceros? |
| `vs01_0140_D` | ¿Alguna vez, bajo el efecto del consumo de bebidas alcohólicas, usted ha provocado o ha cometido acciones que atentan contra otras personas tales como:D. Violaciones? |
| `vs01_0140_E` | ¿Alguna vez, bajo el efecto del consumo de bebidas alcohólicas, usted ha provocado o ha cometido acciones que atentan contra otras personas tales como:E. Accidentes/Hechos de transito? |
| `vs01_0140_F` | ¿Alguna vez, bajo el efecto del consumo de bebidas alcohólicas, usted ha provocado o ha cometido acciones que atentan contra otras personas tales como:F. Intentos de suicidio? |
| `vs01_0140_X` | ¿Alguna vez, bajo el efecto del consumo de bebidas alcohólicas, usted ha provocado o ha cometido acciones que atentan contra otras personas tales como:Otra?(Especifique) |
| `vs01_0140_X_cod` | (ESPECIFIQUE OTRA) ¿Alguna vez, bajo el efecto del consumo de bebidas alcohólicas, usted ha provocado o ha cometido acciones que atentan contra otras personas tales como: otra? |
| `vs01_0141` | ¿En los últimos 12 meses, usted ha fumado? |
| `vs01_0142_01` | ¿Con qué frecuencia ha fumado consumido cigarrillos? INDAGUE: SI RESPONDE ALGUNA DE LAS ALTERNATIVAS, PREGUNTE LA CANTIDAD DE CIGARRILLOS QUE HA FUMADO |
| `vs01_0142_02` | (N° DE CIGARRILLOS) ¿Con qué frecuencia ha fumado consumido cigarrillos? |
| `vs01_0143` | ¿Usted fumaba en la casa, en presencia de su esposa/compañera cuando ella estaba embarazada? |
| `vs01_0144` | ¿Sabe que el humo del tabaco que fuma dentro de la casa provoca daños a su salud y a la de su familia? |
| `vs01_0145` | ¿Conoce o ha escuchado hablar de algún tipo de droga, fuera del alcohol y el tabaco? |
| `vs01_0146_A` | Mencione cuales conoce (MARIHUANA) |
| `vs01_0146_B` | Mencione cuales conoce (COCAÍNA) |
| `vs01_0146_C` | Mencione cuales conoce (ÉXTASIS) |
| `vs01_0146_D` | Mencione cuales conoce (HACHÍS) |
| `vs01_0146_E` | Mencione cuales conoce (ANFETAMINAS) |
| `vs01_0146_F` | Mencione cuales conoce (INHALANTES/CLEFA) |
| `vs01_0146_G` | Mencione cuales conoce (HEROÍNA) |
| `vs01_0146_H` | Mencione cuales conoce (LSD) |
| `vs01_0146_I` | Mencione cuales conoce (TRANQUILIZANTES/PSICOESTIMULANTES) |
| `vs01_0146_X` | Mencione cuales conoce (OTROS) |
| `vs01_0146_X_cod` | (ESPECIFIQUE OTROS) Mencione cuales conoce |
| `vs01_0147_A` | ¿En qué momento se lava las manos (ANTES DE COMER) |
| `vs01_0147_B` | ¿En qué momento se lava las manos (DESPUÉS DE UTILIZAR EL BAÑO) |
| `vs01_0147_C` | ¿En qué momento se lava las manos (DESPUÉS DE CAMBIAR PAÑALES) |
| `vs01_0147_D` | ¿En qué momento se lava las manos (ANTES DE PREPARAR LOS ALIMENTOS) |
| `vs01_0147_E` | ¿En qué momento se lava las manos (ANTES DE DARLE DE COMER A SU HIJO) |
| `vs01_0147_X` | ¿En qué momento se lava las manos (OTRA) |
| `vs01_0147_Z` | ¿En qué momento se lava las manos (EN NINGÚN MOMENTO) |
| `vs01_0147_X_cod` | (ESPECIFIQUE OTRA) ¿En qué momento se lava las manos? |
| `vs01_0148` | Durante la semana pasada, ¿trabajó al menos una hora? ó ¿Estuvo ausente debido a permisos, vacaciones u otra razón? |
| `vs01_0149` | Durante la semana pasada, ¿Usted que gestiones hizo para buscar trabajo? |
| `vs01_0150` | "¿Es usted estudiante, responsable de labores/tareas del hogar, jubilado o benemérito, enfermo o persona con discapacidad o persona de edad avanzada?" |
| `vs01_0150_cod` | (ESPECIFIQUE OTRA) |
| `vs01_0151_cod23` | vs01_0151_cod23 |
| `vs01_0152` | TRABAJA(BA) EN ACTIVIDADES AGROPECUARIAS/FORESTALES |
| `vs01_0153` | ¿Usted trabaja(ba) en tierra propia, en tierra de su familia, en tierra arrendada o trabaja(ba) en la tierra de otra persona? |
| `vs01_0154` | ¿Hace (hacía) usted ese trabajo para alguien de su familia, para otra persona o trabaja(ba) por cuenta propia? |
| `vs01_0154_01` | ¿Usted usualmente trabaja en el hogar o fuera del hogar? |
| `vs01_0155` | ¿Trabaja(ba) usted generalmente durante todo el año, por épocas o de vez en cuando? |
| `vs01_0156` | ¿A usted le pagan (pagaban) en dinero o en especie por el trabajo que realiza(ba) o no le pagan (pagaban)? |
| `vs01_0157` | ¿Durante los últimos 12 meses, cuántos meses trabajó usted? (NÚMERO DE MESES) |
| `vs01_0158` | ¿Cuánto de los gastos de su hogar se pagan (pagaban) con lo que usted gana(ba)? |
| `vs01_0158_cod` | (ESPECIFIQUE OTRO ) ¿Cuánto de los gastos de su hogar se pagan (pagaban) con lo que usted gana(ba)? |
| `vs02_0201` | Ahora me gustaría preguntarle acerca de todos sus hijos e hijas si es que ha tenido. Estamos interesados solamente en hijos e hijas que usted ha engendrado, es decir, sus hijos propios.¿Ha tenido usted algún hijo o hija propio? |
| `vs02_0202` | De los hijos o hijas que usted tuvo, ¿Hay algún hijo o hija que esté viviendo ahora con usted? |
| `vs02_0203_1` | ¿Cuántos hijos (varones) viven con usted?HIJOS EN CASA (SI ES NINGUNO PRESIONE EL BOTON "NINGUNO") |
| `vs02_0203_2` | ¿Cuántos hijas (mujeres) viven con usted?HIJAS EN CASA (SI ES NINGUNO PRESIONE EL BOTON "NINGUNO") |
| `vs02_0204` | ¿Tiene usted alguna hija o hijo que esté viva(o), pero que no esté viviendo con usted? |
| `vs02_0205_1` | ¿Cuántos hijos (varones) están vivos pero NO viven con usted?HIJOS FUERA (SI ES NINGUNO PRESIONE EL BOTON "NINGUNO") |
| `vs02_0205_2` | ¿Cuántas hijas (mujeres) están vivas pero NO viven con usted?HIJAS FUERA (SI ES NINGUNO PRESIONE EL BOTON "NINGUNO") |
| `vs02_0206` | ¿Alguna vez tuvo una niña o un niño que nació viva/o pero que falleció después?SI DIJO NO, INDAGUE:¿Tuvo usted alguna/algún (otra/o) niña o niño que lloró o mostró algún signo de vida pero que sólo vivió pocas horas o días? |
| `vs02_0207_1` | ¿Cuántos hijos (varones) han muerto?HIJOS MUERTOS (SI ES NINGUNO PRESIONE EL BOTON "NINGUNO") |
| `vs02_0207_2` | ¿Cuántas hijas (mujeres) han muerto?HIJAS MUERTOS (SI ES NINGUNO PRESIONE EL BOTON "NINGUNO") |
| `vs02_0208` | SUME LAS RESPUESTAS DE 203, 205 Y 207 Y ANOTE EL TOTAL. SI NO HA TENIDO HIJOS O HIJAS, ANOTE "00" |
| `vs02_0209_01` | Quisiera asegurarme que tengo la información correcta: Usted ha tenido [vs02_0208] hijo/s nacidos vivos durante toda su vida, ¿Es correcto? |
| `vs02_0211` | ¿Cuando tuvo su primera/er hija/o. Usted dejó de estudiar? |
| `vs02_0212` | ¿Cuándo tuvo sus siguientes hijas/os, Usted dejó de estudiar? |
| `vs02_0214_A` | ¿Cuál es la razón por la que dejó de estudiar? (TENIA QUE CUIDAR NIÑOS PEQUEÑOS) |
| `vs02_0214_B` | ¿Cuál es la razón por la que dejó de estudiar? (POR TRABAJO) |
| `vs02_0214_C` | ¿Cuál es la razón por la que dejó de estudiar? (EL ESPOSO O SU PAREJA NO QUERÍA) |
| `vs02_0214_D` | ¿Cuál es la razón por la que dejó de estudiar? (LOS SUEGROS O PADRES NO QUERIAN) |
| `vs02_0214_E` | ¿Cuál es la razón por la que dejó de estudiar? (FALTA DE DINERO) |
| `vs02_0214_X` | ¿Cuál es la razón por la que dejó de estudiar? (OTRAS RAZONES) |
| `vs02_0214_X_cod` | (ESPECIFÍQUE OTRAS RAZONES) ¿Cuál es la razón por la que dejó de estudiar? |
| `vs02_0215` | Las/os hijas/os que Usted ha tenido, ¿Todas/os han sido con la misma mujer? |
| `vs02_0216` | ¿Cuántos años tenía usted cuando nació su primer/a hijo/a? (EDAD EN AÑOS) |
| `vs03_0301_01` | ¿Qué métodos o maneras conoce usted o de cuáles ha oído hablar?¿Conoce o ha oído hablar de:1 Esterilización femenina (ligadura de trompas)Las mujeres pueden someterse a una operación para evitar tener más hijas/os. |
| `vs03_0302_01` | ¿Ha tenido usted una pareja que se ha hecho operar para no tener (más) hijas/os? |
| `vs03_0301_02` | ¿Conoce o ha oído hablar de:2 Esterilización/ operación masculina (vasectomía)Los hombres pueden someterse a una operación para evitar tener más hijas/os. |
| `vs03_0302_02` | ¿Ud. se ha hecho operar para no tener (más) hijas/os? |
| `vs03_0301_03` | ¿Conoce o ha oído hablar de :3 Píldoras/pastillas (métodos orales)?Las mujeres pueden tomar todos los días una pastilla para evitar quedar embarazada. |
| `vs03_0302_03` | ¿Ha usado usted alguna vez (PÍLDORAS/PASTILLAS) con alguna de sus parejas? |
| `vs03_0301_04` | ¿Conoce o ha oído hablar de :4 Dispositivo intrauterino o diu?Las mujeres pueden pedir a un médico o enfermera que le coloque un anillo o una T de cobre en la matriz. |
| `vs03_0302_04` | ¿Ha tenido usted una pareja que ha usado alguna vez (DISPOSITIVO INTRAUTERINO O DIU) con usted? |
| `vs03_0301_05` | ¿Conoce o ha oído hablar de :5 inyección anticonceptiva (para no tener hijos/as)?Las mujeres pueden pedir a un médico o una enfermera que le aplique una inyección mensual o trimestral para evitar quedar embarazada. |
| `vs03_0302_05` | ¿Ha usado usted alguna vez (INYECCIÓN ANTICONCEPTIVA) con alguna de sus parejas? |
| `vs03_0301_06` | ¿Conoce o ha oído hablar de :6 Implantes?Las mujeres pueden pedir a un médico o enfermera que le coloque debajo de la piel del brazo cápsulas (tubitos) para evitar que salga embarazada durante uno o varios años. |
| `vs03_0302_06` | ¿Ha usado usted alguna vez (IMPLANTES) con alguna de sus parejas? |
| `vs03_0301_07` | ¿Conoce o ha oído hablar de :7 Anticoncepción de emergencia (píldora del día siguiente)?Las mujeres pueden tomar ciertas pastillas hasta 48 horas después de haber tenido relaciones sexuales para evitar quedar embarazadas. |
| `vs03_0302_07` | ¿Ha usado usted alguna vez (ANTICONCEPCIÓN DE EMERGENCIA (PÍLDORA DEL DÍA SIGUIENTE)) con alguna de sus parejas? |
| `vs03_0301_08` | ¿Conoce o ha oído hablar de : 8 Condón (preservativo)?Los hombres pueden usar una fundita de goma puesta en el pene durante las relaciones sexuales para evitar que la mujer salga embarazada. |
| `vs03_0302_08` | ¿Ha usado usted alguna vez (CONDÓN) con alguna de sus parejas? |
| `vs03_0301_09` | ¿Conoce o ha oído hablar de :9 Condón femenino?Las mujeres pueden usar una fundita de goma que tiene dos anillos, uno interno que no contiene espermicidas, que permite la colocación fácil dentro de la vagina, y el otro externo con un diámetro más grande, |
| `vs03_0302_09` | ¿Ha usado usted alguna vez (CONDÓN FEMENINO) con alguna de sus parejas? |
| `vs03_0301_10` | ¿Conoce o ha oído hablar de :10 Tabletas vaginales, óvulos, espuma o jalea (métodos vaginales)?La mujer puede colocarse dentro de la vagina una tableta, crema, espuma, óvulo, jalea antes de tener relaciones sexuales. |
| `vs03_0302_10` | ¿Ha usado usted alguna vez (TABLETAS VAGINALES, ÓVULOS, ESPUMA O JALEA) con alguna de sus parejas? |
| `vs03_0301_11` | ¿Conoce o ha oído hablar de :11 Método de lactancia y amenorrea (mela)?Las mujeres pueden alimentar a su niño sólo con el seno durante los primeros 6 meses mientras no le ha llegado la regla o menstruación para evitar así quedar embarazada. |
| `vs03_0302_11` | ¿Ha usado usted alguna vez (MÉTODO DE LACTANCIA Y AMENORREA) con alguna de sus parejas? |
| `vs03_0301_12` | ¿Conoce o ha oído hablar de :12 Ritmo, ovulación, abstinencia periódica o billings, rosario?Las parejas pueden dejar de tener relaciones sexuales durante aquellos días del mes en los cuales la mujer tiene más posibilidad de quedar embarazada. |
| `vs03_0302_12` | ¿Ha usado usted alguna vez el (MÉTODO DE RITMO, OVULACIÓN, ABSTINENCIA PERIÓDICA O BILLINGS, ROSARIO) con alguna de sus parejas? |
| `vs03_0301_13` | ¿Conoce o ha oído hablar de :13 Retiro (coito interrumpido)?Los hombres pueden ser cuidadosos y retirarse antes de terminar el acto sexual, eyaculando o vaciándose fuera de la vagina de la mujer. |
| `vs03_0302_13` | ¿Ha usado usted alguna vez el (MÉTODO RETIRO (COITO INTERRUMPIDO)) con alguna de sus parejas? |
| `vs03_0301_14` | ¿Conoce o ha oído hablar de :14 Otro método?¿Ha oído usted hablar o conoce alguna otra forma o método usado por las mujeres o los hombres para evitar embarazos? |
| `vs03_0301_14_cod` | (ESPECIFIQUE) OTRO MÉTODO |
| `vs03_0302_14` | ¿Ha usado usted alguna vez el [vs03_0301_14_302_01] con alguna de sus parejas? |
| `vs03_0304` | Ahora me gustaría preguntarle sobre la posibilidad/ riesgo/ probabilidad de embarazo que tiene la mujer.¿Considera usted que entre una menstruación y otra hay días en que la mujer tiene más posibilidad/ riesgo/ probabilidad de quedar embarazada? |
| `vs03_0305` | Para usted ¿Cuáles son esos días: justo antes de que comience la menstruación, durante la menstruación, inmediatamente después de terminada la menstruación, en la mitad del ciclo menstrual, o en cualquier momento? |
| `vs03_0305_cod` | (ESPECIFÍQUE OTRA) ¿justo antes de que comience la menstruación, justo después que termine la menstruación ó a la mitad entre una menstruación y otra? |
| `vs03_0306` | ¿Usted tiene conocimiento que durante los primeros meses después de tener un hijo, una mujer que está dando el pecho/dando de lactar, no puede quedar embarazada? |
| `vs04_0401` | ¿Actualmente, está usted casado o vive en unión con su pareja? |
| `vs04_0402` | ¿Ha estado usted casado o unido alguna vez aunque haya sido sólo por un tiempo? |
| `vs04_0403` | Aparte de la esposa o pareja que vive en la casa ¿Actualmente, tiene usted alguna otra pareja sexual regular u ocasional, o no tiene otra pareja sexual? |
| `vs04_0404` | ¿Actualmente, tiene usted pareja sexual regular, ocasional, o no tiene pareja sexual? |
| `vs04_0405` | ¿Cuál es su estado civil actual: viudo, separado, divorciado o soltero? |
| `vs04_0406` | ¿Su esposa/compañera vive actualmente con usted o vive en alguna otra parte? |
| `vs04_0407` | NÚMERO DE ORDEN DE LA ESPOSA/COMPAÑERA |
| `vs04_0408` | ¿Ha estado usted casado o en unión libre con una mujer sólo una vez o más de una vez? |
| `vs04_0409` | En total, ¿Con cuántas mujeres ha estado usted casado o en unión libre en toda su vida? (NÚMERO DE MUJERES) |
| `vs04_0410_01` | ¿En qué MES comenzó a vivir con su esposa/ compañera?(SI NO SABE EL MES COLOQUE 98): |
| `vs04_0410_02` | ¿En qué AÑO comenzó a vivir con su esposa/ compañera?(SI NO SABE EL AÑO COLOQUE 9998): |
| `vs04_0410_03` | ¿En qué MES comenzó a vivir con su PRIMERA esposa/ compañera?(SI NO SABE EL MES COLOQUE 98): |
| `vs04_0410_04` | ¿En qué AÑO comenzó a vivir con su PRIMERA esposa/ compañera? |
| `vs04_0411` | ¿Cuántos años cumplidos tenía usted cuando empezó a vivir con su esposa o pareja? (EDAD) |
| `vs04_0412` | Ahora necesito hacerle algunas preguntas sobre su actividad sexual, con el fin de tener una mejor comprensión de algunos temas de la vida familiar¿Cuántos años tenía usted cuando tuvo su primera relación sexual (si ha tenido)?(EDAD EN AÑOS)SI NUNCA HA TEN |
| `vs04_0414_A` | ¿Dónde recibió por primera vez información o educación para la sexualidad? (EN SU CASA) |
| `vs04_0414_B` | ¿Dónde recibió por primera vez información o educación para la sexualidad? (EN LA ESCUELA) |
| `vs04_0414_C` | ¿Dónde recibió por primera vez información o educación para la sexualidad? (INTERNET) |
| `vs04_0414_D` | ¿Dónde recibió por primera vez información o educación para la sexualidad? (AMIGOS) |
| `vs04_0414_X` | ¿Dónde recibió por primera vez información o educación para la sexualidad? (MARQUE TODAS LAS OPCIONES MENCIONADAS) |
| `vs04_0414_X_cod` | (ESPECIFÍQUE OTRO) ¿Dónde recibió por primera vez información o educación para la sexualidad? |
| `vs04_0415` | La primera vez que tuvo relaciones sexuales, ¿Uso condón? |
| `vs04_0416` | ¿Cuándo fue la última vez que tuvo relaciones sexuales?REGISTRE LA RESPUESTA EN LA UNIDAD DE TIEMPO DADA POR EL ENTREVISTADO, PERO SI LA RESPUESTA EQUIVALE A 12 MESES O MÁS, ANOTE EN AÑOS |
| `vs04_0416_01` | (ESPECIFÍQUE EL TIEMPO) ¿Cuándo fue la última vez que tuvo relaciones sexuales? |
| `vs04_0417` | La última vez que tuvo relaciones sexuales, ¿Uso condón? |
| `vs04_0418` | ¿Cuál fue la razón principal por la cual usted usó condón esa última vez? |
| `vs04_0418_cod` | (ESPECIFÍQUE OTRA) ¿Cuál fue la razón principal por la cual usted usó condón esa última vez? |
| `vs04_0420_01` | ¿La última vez que tuvo relaciones sexuales con una mujer, usted o ella usaron algo además de condón para evitar un embarazo? |
| `vs04_0420_02` | ¿La última vez que tuvo relaciones sexuales con una mujer, usted o ella usaron algo para evitar un embarazo? |
| `vs04_0421` | ¿Qué método usaron para evitar un embarazo? |
| `vs04_0421_cod` | (ESPECIFÍQUE OTRO MÉTODO) ¿Qué método usaron para evitar un embarazo? |
| `vs04_0423` | ¿Cuál fue la razón principal por la que no usaron ningún método para evitar un embarazo? |
| `vs04_0423_cod` | (ESPECIFÍQUE OTRO) ¿Cuál fue la razón principal por la que no usaron ningún método para evitar un embarazo? |
| `vs04_0424` | ¿Con quién tuvo su última relación sexual? |
| `vs04_0424_cod` | (ESPECIFÍQUE OTRO) ¿Con quién tuvo su última relación sexual? |
| `vs04_0425_01` | ¿Durante cuánto tiempo mantuvo (ha tenido) relaciones sexuales con esta persona?REGISTRE LA RESPUESTA EN LA UNIDAD DE TIEMPO DADA POR EL ENTREVISTADO |
| `vs04_0425_02` | (ESPECIFÍQUE EL TIEMPO) ¿Durante cuánto tiempo mantuvo (ha tenido) relaciones sexuales con esta persona? |
| `vs04_0426` | Durante los últimos 12 meses ¿Ha tenido relaciones sexuales con otra persona diferente? |
| `vs04_0427` | En total ¿Con cuántas personas diferentes ha tenido usted relaciones sexuales durante los últimos 12 meses? (NÚMERO DE PERSONAS) |
| `vs04_0428_A` | En esta época se habla más abiertamente de las relaciones entre personas del mismo sexo. ¿Usted, ha tenido sexo alguna vez con otro:(A) Hombres? |
| `vs04_0428_B` | En esta época se habla más abiertamente de las relaciones entre personas del mismo sexo. ¿Usted, ha tenido sexo alguna vez con:(B) Hombre y Mujer? |
| `vs04_0429` | ¿Ha pagado usted alguna vez para tener relaciones sexuales? |
| `vs04_0430_01` | ¿Cuánto tiempo hace desde la última vez que pagó por tener relaciones sexuales? |
| `vs04_0430_02` | (ESPECIFIQUE EL TIEMPO) ¿Cuánto tiempo hace desde la última vez que pagó por tener relaciones sexuales? |
| `vs04_0431` | La última vez que tuvo relaciones sexuales pagadas, ¿usarón condón? |
| `vs04_0432` | ¿Sabe de algún lugar dónde se puede conseguir condones? |
| `vs04_0433_A` | ¿Cuál es ese lugar?(PUESTO DE SALUD) |
| `vs04_0433_B` | ¿Cuál es ese lugar?(CENTRO DE SALUD AMBULATORIO) |
| `vs04_0433_C` | ¿Cuál es ese lugar?(CENTRO DE SALUD CON INTERNACION) |
| `vs04_0433_D` | ¿Cuál es ese lugar?(CENTRO DE SALUD INTEGRAL) |
| `vs04_0433_E` | ¿Cuál es ese lugar?(HOSPITAL DE SEGUNDO NIVEL) |
| `vs04_0433_F` | ¿Cuál es ese lugar?(HOSPITAL DE TERCER NIVEL) |
| `vs04_0433_G` | ¿Cuál es ese lugar?(HOSPITAL ESPECIALIZADO) |
| `vs04_0433_H` | ¿Cuál es ese lugar?(CAJA NACIONAL DE SALUD) |
| `vs04_0433_I` | ¿Cuál es ese lugar?(CAJA DE LA BANCA PRIVADA) |
| `vs04_0433_J` | ¿Cuál es ese lugar?(CAJA PETROLERA) |
| `vs04_0433_K` | ¿Cuál es ese lugar?(CAJA DE LA BANCA ESTATAL) |
| `vs04_0433_L` | ¿Cuál es ese lugar?(CORDES) |
| `vs04_0433_M` | ¿Cuál es ese lugar?(CAJA DE CAMINOS) |
| `vs04_0433_N` | ¿Cuál es ese lugar?(COSSMIL/FFAA) |
| `vs04_0433_O` | ¿Cuál es ese lugar?(SEGURO UNIVERSITARIO) |
| `vs04_0433_P` | ¿Cuál es ese lugar?(ORGANISMOS PRIVADOS (PRIMER NIVEL, SEGUNDO NIVEL, TERCER NIVEL)) |
| `vs04_0433_Q` | ¿Cuál es ese lugar?(IGLESIA (PRIMER NIVEL, SEGUNDO NIVEL, TERCER NIVEL)) |
| `vs04_0433_R` | ¿Cuál es ese lugar?(PROMOTOR DE LA SALUD/RPS/OTRO AGENTE) |
| `vs04_0433_S` | ¿Cuál es ese lugar?(VISITA DOMICILIARIA) |
| `vs04_0433_T` | ¿Cuál es ese lugar?(FARMACIA) |
| `vs04_0433_U` | ¿Cuál es ese lugar?(MEDICINA TRADICIONAL) |
| `vs04_0433_V` | ¿Cuál es ese lugar?(NO ACUDIÓ A NINGUN E.S./NO FUE) |
| `vs04_0433_X` | ¿Cuál es ese lugar?(OTRO LUGAR:) |
| `vs04_0433_Y` | ¿Cuál es ese lugar?(NO SABE) |
| `vs04_0433_X_cod` | (ESPECIFIQUE OTRO LUGAR) |
| `vs04_0434` | Si usted quisiera ¿podría conseguir un condón? |
| `vs04_0436` | ¿Cuántos años tenía usted cuando usó un condón por primera vez?(EDAD AL PRIMER USO) (SI NO RECUERDA COLOQUE "98") |
| `vs04_0437_A` | ¿Por qué usó condón esa primera vez?(PARA EVITAR UN EMBARAZO) |
| `vs04_0437_B` | ¿Por qué usó condón esa primera vez?(PARA EVITAR CONTAGIO DE VIH/SIDA) |
| `vs04_0437_C` | ¿Por qué usó condón esa primera vez?(PARA EVITAR CONTAGIARSE DE ITS) |
| `vs04_0437_D` | ¿Por qué usó condón esa primera vez?(PARA EVITAR INFECTAR A LA PAREJA) |
| `vs04_0437_E` | ¿Por qué usó condón esa primera vez?(PARA EXPERIMENTAR/ENSAYAR CONDÓN) |
| `vs04_0437_X` | ¿Por qué usó condón esa primera vez?(OTRO:) |
| `vs04_0437_X_cod` | (ESPECIFÍQUE OTRO) ¿Por qué usó condón esa primera vez? |
| `vs04_0438_A` | ¿Ha tenido problemas con el uso del condón?(DIFICULTAD PARA DESHACERSE DE ÉL) |
| `vs04_0438_B` | ¿Ha tenido problemas con el uso del condón?(DIFICULTAD PARA PONÉRSELO/ QUITÁRSELO) |
| `vs04_0438_C` | ¿Ha tenido problemas con el uso del condón?(DISMINUYE EL PLACER) |
| `vs04_0438_D` | ¿Ha tenido problemas con el uso del condón?(COMPAÑERA/ESPOSA CUESTIONA/ NO GUSTA) |
| `vs04_0438_E` | ¿Ha tenido problemas con el uso del condón?(COMPAÑERA/ESPOSA QUEDÓ EMBARAZADA) |
| `vs04_0438_F` | ¿Ha tenido problemas con el uso del condón?(INCONVENIENTE PARA USAR) |
| `vs04_0438_G` | ¿Ha tenido problemas con el uso del condón?(SE ROMPIÓ) |
| `vs04_0438_X` | ¿Ha tenido problemas con el uso del condón?(OTRO:) |
| `vs04_0438_Z` | ¿Ha tenido problemas con el uso del condón?(NINGÚN PROBLEMA) |
| `vs04_0438_X_cod` | (ESPECIFÍQUE OTRO PROBLEMA) ¿Ha tenido problemas con el uso del condón? |
| `vs04_0439_A` | Dígame con cuáles de las siguientes afirmaciones usted está de acuerdo o en desacuerdo(A) El condón disminuye el placer sexual del hombre |
| `vs04_0439_B` | Dígame con cuáles de las siguientes afirmaciones usted está de acuerdo o en desacuerdo(B) El condón es muy complicado de usar |
| `vs04_0439_C` | Dígame con cuáles de las siguientes afirmaciones usted está de acuerdo o en desacuerdo(C) El condón puede usarse varias veces |
| `vs04_0439_D` | Dígame con cuáles de las siguientes afirmaciones usted está de acuerdo o en desacuerdo(D) El condón protege contra las infecciones de transmisión sexual |
| `vs04_0439_E` | Dígame con cuáles de las siguientes afirmaciones usted está de acuerdo o en desacuerdo(E) Comprar condones es vergonzoso |
| `vs04_0439_F` | Dígame con cuáles de las siguientes afirmaciones usted está de acuerdo o en desacuerdo(F) Una mujer tiene derecho a pedirle a un hombre que use condón |
| `vs05_0502` | ¿Está su esposa/pareja/compañera actualmente embarazada? |
| `vs05_0503_01` | Ahora tengo algunas preguntas sobre el futuro.¿Le gustaría tener una/un (otra/o) hija/o o preferiría no tener ningún (más) hija/o(s)? |
| `vs05_0503_02` | Ahora tengo algunas preguntas sobre el futuro.¿Después del bebé que su esposa/ compañera(pareja principal) está esperando ahora, le gustaría tener otra/o hija/o o preferiría no tener más hija/o (s)? |
| `vs05_0504` | ¿Cuánto tiempo le gustaría esperar desde ahora hasta el nacimiento de una/un (otra/o) hija/o? |
| `vs05_0504_01` | NÚMERO MESES |
| `vs05_0504_02` | NÚMERO AÑOS |
| `vs05_0504_cod` | (ESPECIFIQUE) OTRA |
| `vs05_0505_01` | Si usted pudiera volver a la época en que todavía no tenía hijas/os y pudiera elegir exactamente el número de hijas/os que tendría en toda su vida, ¿Cuántos serían? |
| `vs05_0505_02` | Si usted pudiera elegir exactamente el número de hijas/os que tendría en toda su vida, ¿Cuántos serían? |
| `vs05_0505_03` | ¿Cuántos serían? (NÚMERO DE HIJAS/OS) |
| `vs05_0505_1_cod` | (ESPECIFIQUE) INGRESE OTRA RESPUESTA |
| `vs05_0505_05` | ¿Cuántos serían? (NÚMERO DE HIJAS/OS) |
| `vs05_0505_2_cod` | (ESPECIFIQUE) INGRESE OTRA RESPUESTA |
| `vs05_0506` | ¿Cuántas/os de estas/os hijas/os le habría gustado que fueran mujeres y cuántos varones y para cuántos no le importaria el sexo? |
| `vs05_0506_01` | ¿Cuántas/os de estas/os hijas/os le habría gustado que fueran hombres? NÚMERO DE HOMBRES: |
| `vs05_0506_02` | ¿Cuántas/os de estas/os hijas/os le habría gustado que fueran mujeres? NÚMERO DE MUJERES: |
| `vs05_0506_03` | ¿Cuántas/os de estas/os hijas/os no le importaría el sexo? NÚMERO CUALQUIER SEXO: |
| `vs05_0506_04` | (ESPECIFIQUE) OTRA |
| `vs05_0507` | ¿Usted está de acuerdo o en desacuerdo con que las parejas usen métodos anticonceptivos para evitar embarazos? |
| `vs05_0508_A` | Durante los últimos 12 meses, usted ha: (A) ¿Escuchado en la radio algo sobre anticoncepción/ planificación familiar? |
| `vs05_0508_B` | Durante los últimos 12 meses, usted ha:(B) ¿Visto en la televisión algo sobre anticoncepción/ planificación familiar? |
| `vs05_0508_C` | Durante los últimos 12 meses, usted ha:(C) ¿Leído en periódicos o revistas algo sobre anticoncepción/ planificación familiar? |
| `vs05_0508_D` | Durante los últimos 12 meses, usted ha:(D) ¿Visto en Internet algo sobre anticoncepción/ planificación familiar? |
| `vs05_0508_X` | Durante los últimos 12 meses, usted ha: X. Otro (ESPECIFIQUE). |
| `vs05_0508_X_cod` | (ESPECIFIQUE) OTRA |
| `vs05_0509_A` | En los últimos doce meses, ¿Usted busco y encontró información sobre anticoncepción/ Planificación familiar:(A) En establecimiento de Salud Privado ? |
| `vs05_0509_B` | En los últimos doce meses, ¿Usted buscó y encontró información sobre anticoncepción / Planificación familiar:(B) En establecimiento de Salud Público? |
| `vs05_0509_C` | En los últimos doce meses, ¿Usted buscó y encontró información sobre anticoncepción / Planificación familiar:(C) En un grupo de amigos? |
| `vs05_0509_D` | En los últimos doce meses, ¿Usted buscó y encontró información sobre anticoncepción / Planificación familiar:(D) En Internet? |
| `vs05_0509_E` | En los últimos doce meses, ¿Usted buscó y encontró información sobre anticoncepción / Planificación familiar:(E) En su Familia? |
| `vs05_0509_X` | En los últimos doce meses, ¿Usted buscó y encontró información sobre anticoncepción / Planificación familiar:(X) En otra parte (ESPECIFIQUE)? |
| `vs05_0509_X_cod` | (ESPECIFIQUE) En otra parte. |
| `vs06_0602` | NÃšMERO DEL ÃšLTIMO HIJO/A |
| `vs06_0602_02` | ¿cual es el nombre y el sexo de su ultima hija/o? (Sexo) |
| `vs06_0603_01` | ¿en qué mes y año nació (nombre de la niña o niño)? (Mes) |
| `vs06_0603_02` | ¿en qué mes y año nació (nombre de la niña o niño)? (Año) |
| `vs06_0604` | ¿esta vivo (a) [nombre]? |
| `vs06_0605_01` | ¿qué edad tenia [nombre] cuando ella/ el murió? |
| `vs06_0605_02` | ¿qué edad tenia [nombre] cuando ella/ el murió? |
| `vs06_0606` | NÃšMERO DE LA MADRE DEL ÃšLTIMO HIJO/A |
| `vs06_0609` | ¿cuál es su relación con [nombre de la madre de la/el niño]? |
| `vs06_0609_cod` | ¿cuál es su relación con [nombre de la madre de la/el niña/o]? otro (especifique) codificado |
| `vs06_0610` | ¿en algún momento mientras (nombre de la madre de la/el niño) estaba embarazada de [nombre de la/el niña/o], hablo usted con algún profesional de salud sobre la salud de la madre en su embarazo? |
| `vs06_0612` | ¿vive (nombre de la/el niña/niño) con usted? |
| `vs06_0613_A` | ¿en su hogar, quién generalmente decide qué hacer si (nombre de la/el niña/niño se enferma? ¿el padre? |
| `vs06_0613_B` | ¿en su hogar, quién generalmente decide qué hacer si (nombre de la/el niña/niño se enferma? ¿la madre de la/el niña/o? |
| `vs06_0613_C` | ¿en su hogar, quién generalmente decide qué hacer si (nombre de la/el niña/niño se enferma? ¿pariente femenino? |
| `vs06_0613_D` | ¿en su hogar, quién generalmente decide qué hacer si (nombre de la/el niña/niño se enferma? ¿pariente masculino? |
| `vs06_0613_X` | ¿en su hogar, quién generalmente decide qué hacer si (nombre de la/el niña/niño se enferma? ¿otro? (especifique) |
| `vs06_0613_Y` | ¿en su hogar, quién generalmente decide qué hacer si (nombre de la/el niña/niño se enferma? ¿niño/a nunca se enferma? |
| `vs06_0613_X_cod` | ¿en su hogar, quién generalmente decide qué hacer si (nombre de la/el niña/niño se enferma? ¿otro? (especifique) codificado |
| `vs06_0614_A` | Algunas veces una mujer embarazada puede presentar signos de peligro del embarazo que podría provocar un aborto, pérdida o muerte de la madre o la/el niña/o. ¿me puede decir cuáles son algunos de estos problemas? ¿sangrado vaginal? |
| `vs06_0614_B` | Algunas veces una mujer embarazada puede presentar signos de peligro del embarazo que podria provocar un aborto, perdida o muerte de la madre o la/el niña/o ¿me puede decir cuáles son algunos de estos problemas? ¿fiebre alta? |
| `vs06_0614_C` | Algunas veces una mujer embarazada puede presentar signos de peligro del embarazo que podría provocar un aborto, pérdida o muerte de la madre o la/el niña/o. ¿me puede decir cuáles son algunos de estos problemas? ¿dolor abdominal? |
| `vs06_0614_D` | Algunas veces una mujer embarazada puede presentar signos de peligro del embarazo que podría provocar un aborto, pérdida o muerte de la madre o la/el niña/o. ¿me puede decir cuáles son algunos de estos problemas? ¿hinchazón de manos y los pies? |
| `vs06_0614_E` | Algunas veces una mujer embarazada puede presentar signos de peligro del embarazo que pódria provocar un aborto, pérdida o muerte de la madre o ¿trabajo de parto difícil por más de 2 horas? |
| `vs06_0614_F` | Algunas veces una mujer embarazada puede presentar signos de peligro del embarazo que podría provocar un aborto, pérdida o muerte de la madre o la/el niña/o.¿me puede decir cuáles son algunos de estos problemas? ¿convulsiones? |
| `vs06_0614_G` | Algunas veces una mujer embarazada puede presentar signos de peligro del embarazo que podria provocar un aborto, perdida o muerte de la madre o la/el niña/o.¿Me puede decir cuales son algunos de estos problemas? ¿Dolor en el vientre bajo? |
| `vs06_0614_X` | Algunas veces una mujer embarazada puede presentar signos de peligro del embarazo que podría provocar un aborto, pérdida o muerte de la madre o la/el niña/o.¿me puede decir cuáles son algunos de estos problemas? ¿otro? (especifique) |
| `vs06_0614_Z` | Algunas veces una mujer embarazada puede dar signos de peligro del embarazo podría provocar un aborto, pérdida o muerte de la madre o la/el niña/o.¿me puede decir cuáles son algunos de estos problemas? ¿no conoce ningún problema? |
| `vs06_0614_X_cod` | Algunas veces una mujer embarazada puede presentar signos de peligro del embarazo que podría provocar un aborto, pérdida o muerte de la madre o la/el niña/o. ¿otro? (especifique) codificado |
| `vs06_0615` | Cuando una/un niña/o tiene diarrea ¿se le debe dar menos cantidad, la misma cantidad o más liquido que de costumbre? |
| `vs06_0616` | ¿ha oído usted hablar de un producto especial llamado sales de rehidratación oral o suero de la vida que se pueden usar para el tratamiento de la diarrea? |
| `vs06_0617` | ¿usted ha utilizado alguna vez con su niña o niño sales de rehidratación oral o suero de la vida? |
| `vs06_0618` | En el establecimiento de salud al que lleva a su niña/o ¿recibe información/ educación sobre alimentación y nutrición que su niña o niño debe recibir? |
| `vs06_0619` | ¿en los últimos tres años, en algún momento le pusieron a usted una vacuna antitetánica? |
| `vs06_0620` | ¿cuántas dosis de vacuna antitetánica recibió en total? |
| `vs06_0621` | ¿Conoce la vacuna ciontra la influenza estacional (H1N1)? |
| `vs06_0622` | ¿usted sabe que el hombre puede desarrollar cáncer de próstata? |
| `vs06_0623` | ¿usted sabe que el cáncer de próstata puede diagnosticarse tempranamente mediante un exámen clinico y de sangre? |
| `vs06_0624` | ¿se ha realizado un examen clínico y/o de sangre para detectar cáncer de próstata? |
| `vs06_0625_01` | ¿Hace cuanto tiempo le realizaron la ultima vez la prueba de Tacto Rectaly/o sangre? Registre en meses si es menor a 1 año (meses) |
| `vs06_0625_02` | ¿Hace cuanto tiempo le realizaron la ultima vez la prueba de Tacto Rectaly/o sangre? Registre en meses si es menor a 1 año (Año) |
| `vs06_0626_A` | ¿Conoce a alguien de la familia que: A Ha tenido cancer de Prostata |
| `vs06_0626_B` | ¿Conoce a alguien de la familia que: B Ha fallecido por cancer de prostata |
| `vs06_0627` | ¿En los ultimos 12 meses, algun medico u otro personal de salud le ha medido la Presion Arterial? |
| `vs06_0628` | ¿Donde le midieron a usted la Presion Arterial la ultima vez? |
| `vs06_0628_cod` | ¿Donde le midieron a usted la Presion Arterial la ultima vez? ESPECIFIQUE OTRO |
| `vs06_0629` | ¿Alguna vez en su vida un medico le ha diagnosticado hipertension arterial o "presion alta"? (ESPECIFIQUE) OTRO LUGAR |
| `vs06_0630` | los últimos 12 meses, usted ha recibido y/o comprado medicamentos para controlar su presión arterial? |
| `vs06_0631` | ¿En los últimos 12 meses, algún médico o personal de salud, le han medido la glucosa (azúcar en la sangre)? |
| `vs06_0632` | ¿Donde le midieron a usted la glucosa (azucar en la sangre)? |
| `vs06_0632_cod` | ¿Donde le midieron a usted la glucosa (azucar en la sangre)? ESPECIFIQUE OTRO |
| `vs06_0633` | ¿Alguna vez en su vida un medico le ha diagnosticado Diabetes o azucar ellevada en sangre? |
| `vs06_0634` | ¿En los ultimos 12 meses, usted ha recibidoy/o comprado medicamentos para controlar su Diabetes o azucar alta en la sangre? |
| `vs06_0635` | ¿usted ha oido hablar de una enfermedad llamada tuberculosis o tb? |
| `vs06_0636_A` | ¿cómo se transmite la tuberculosis de una persona a otra? ¿a través del aire, por tos o estornudos? |
| `vs06_0636_B` | ¿cómo se transmite la tuberculosis de una persona a otra? ¿compartiendo utensilios? |
| `vs06_0636_C` | ¿cómo se transmite la tuberculosis de una persona a otra? ¿ tocando una persona con tuberculosis? |
| `vs06_0636_D` | ¿cómo se transmite la tuberculosis de una persona a otra? ¿compartiendo alimentos? |
| `vs06_0636_E` | ¿cómo se transmite la tuberculosis de una persona a otra? ¿por contacto sexual? |
| `vs06_0636_F` | ¿como se trasmite la tuberculosis de una persona a otra? ¿por picadura de mosquitos? |
| `vs06_0636_X` | ¿cómo se transmite la tuberculosis de una persona a otra? ¿otra? (especifique) |
| `vs06_0636_Z` | ¿cómo se transmite la tuberculosis de una persona a otra? ¿no sabe? |
| `vs06_0636_X_cod` | ¿cómo se transmite la tuberculosis de una persona a otra? ¿otra? (especifique) codificado |
| `vs06_0637` | ¿en su familia hay alguien con tuberculosis diagnosticada? |
| `vs06_0638` | ¿si un miembro de su familia tuviera tuberculosis, usted preferiria mantenerlo en secreto o no? |
| `vs06_0638a` | ¿Usted recibio/compro medicamentos para tratamiento de tuberculosis? |
| `vs06_0639_A` | ¿Donde recibio y/o compro medicamentos para tratamiento de Tuberculosis? Subsector Publico (PUESTO DE SALUD) |
| `vs06_0639_B` | ¿Donde recibio y/o compro medicamentos para tratamiento de Tuberculosis? (CENTRO DE SALUD AMBULATORIO) |
| `vs06_0639_C` | ¿Donde recibio y/o compro medicamentos para tratamiento de Tuberculosis? (CENTRO DE SALUD AMBULATORIO) |
| `vs06_0639_D` | ¿Donde recibio y/o compro medicamentos para tratamiento de Tuberculosis? (CENTRO DE SALUD INTEGRAL) |
| `vs06_0639_E` | ¿Donde recibio y/o compro medicamentos para tratamiento de Tuberculosis? (HOSPITAL DE SEGUNDO NIVEL) |
| `vs06_0639_F` | ¿Donde recibio y/o compro medicamentos para tratamiento de Tuberculosis? (HOSPITAL DE TERCER NIVEL) |
| `vs06_0639_G` | ¿Donde recibio y/o compro medicamentos para tratamiento de Tuberculosis? (HOSPITAL ESPECIALIZADO) |
| `vs06_0639_H` | ¿Donde recibio y/o compro medicamentos para tratamiento de Tuberculosis? Seguridad social a corto plazo (CAJA NACIONAL DE SALUD) |
| `vs06_0639_I` | ¿Donde recibio y/o compro medicamentos para tratamiento de Tuberculosis? (CAJA DE LA BANCA PRIVADA) |
| `vs06_0639_J` | ¿Donde recibio y/o compro medicamentos para tratamiento de Tuberculosis? (CAJA PETROLERA) |
| `vs06_0639_K` | ¿Donde recibio y/o compro medicamentos para tratamiento de Tuberculosis? (CAJA DE LA BANCA ESTATAL) |
| `vs06_0639_L` | ¿Donde recibio y/o compro medicamentos para tratamiento de Tuberculosis? (CORDES) |
| `vs06_0639_M` | ¿Donde recibio y/o compro medicamentos para tratamiento de Tuberculosis? (CAJA DE CAMINOS) |
| `vs06_0639_N` | ¿Donde recibio y/o compro medicamentos para tratamiento de Tuberculosis? (COSSMIL/FFAA) |
| `vs06_0639_O` | ¿Donde recibio y/o compro medicamentos para tratamiento de Tuberculosis? (SEGURO UNIVERSITARIO) |
| `vs06_0639_P` | ¿Donde recibio y/o compro medicamentos para tratamiento de Tuberculosis? Subsector privado (ORGANISMOS PRIVADOS primer nivel, segundo nivel, tercer nivel) |
| `vs06_0639_Q` | ¿Donde recibio y/o compro medicamentos para tratamiento de Tuberculosis? (ONG/IGLESIA primer nivel, segundo nivel, tercer nivel) |
| `vs06_0639_R` | ¿Donde recibio y/o compro medicamentos para tratamiento de Tuberculosis? Otros (PROMOTOR DE LA SALUD/RPS/OTRO AGENTE) |
| `vs06_0639_S` | ¿Donde recibio y/o compro medicamentos para tratamiento de Tuberculosis? (VISITA DOMICILIARIA) |
| `vs06_0639_T` | ¿Donde recibio y/o compro medicamentos para tratamiento de Tuberculosis? (FARMACIA) |
| `vs06_0639_U` | ¿Donde recibio y/o compro medicamentos para tratamiento de Tuberculosis? (MEDICINA TRADICIONAL) |
| `vs06_0639_V` | ¿Donde recibio y/o compro medicamentos para tratamiento de Tuberculosis? (NO ACUDIO A NINGUN E.S./NO FUE) |
| `vs06_0639_X` | ¿Donde recibio y/o compro medicamentos para tratamiento de Tuberculosis? (OTRO LUGAR) |
| `vs06_0639_Z` | ¿Donde recibio y/o compro medicamentos para tratamiento de Tuberculosis? (NO SAbe) |
| `vs06_0639_X_cod` | ¿Donde recibio y/o compro medicamentos para tratamiento de Tuberculosis? (ESPECIFIQUE OTRO LUGAR) |
| `vs06_0640` | ¿Sabe que es el dengue, zika, chikungunya? |
| `vs06_0641_A` | ¿Conoce cómo se transmite el Dengue, zika, chikungunya? ¿Por picadura de mosquito? |
| `vs06_0641_B` | ¿Conoce cómo se transmite el Dengue, zika, chikungunya? ¿Por comida en mal estado? |
| `vs06_0641_C` | ¿Conoce cómo se transmite el Dengue, zika, chikungunya? ¿Por contacto con un enfermo? |
| `vs06_0641_X` | ¿Conoce cómo se transmite el Dengue, zika, chikungunya? ¿Otra razón? |
| `vs06_0641_Y` | ¿Conoce cómo se transmite el Dengue, zika, chikungunya? ¿No sabe? |
| `vs06_0641_X_cod` | ¿Conoce cómo se transmite el Dengue, zika, chikungunya? ¿Especifique si es otra razón? |
| `vs06_0642_A` | ¿Qué medidas preventivas conoce para prevenir el dengue,zika, chikungunya? Eliminacion de criaderos |
| `vs06_0642_B` | ¿Qué medidas preventivas conoce para prevenir el dengue,zika, chikungunya? (Uso de repelente) |
| `vs06_0642_C` | ¿Qué medidas preventivas conoce para prevenir el dengue,zika, chikungunya? (Desechos de aguas estancadas) |
| `vs06_0642_D` | ¿Qué medidas preventivas conoce para prevenir el dengue,zika, chikungunya? (Fumigacion del Hogar) |
| `vs06_0642_E` | ¿Qué medidas preventivas conoce para prevenir el dengue,zika, chikungunya? (Uso de mosquiteros) |
| `vs06_0642_F` | ¿Qué medidas preventivas conoce para prevenir el dengue,zika, chikungunya? (Uso de malla milimetrica) |
| `vs06_0642_X` | ¿Qué medidas preventivas conoce para prevenir el dengue,zika, chikungunya? (Otra medida preventiva) |
| `vs06_0642_Y` | ¿Qué medidas preventivas conoce para prevenir el dengue,zika, chikungunya? (No sabe) |
| `vs06_0642_X_cod` | ¿Qué medidas preventivas conoce para prevenir el dengue,zika, chikungunya? (Especifique la otra medida preventiva) |
| `vs06_0643_A` | ¿Cuáles son los sintomas que puede producir el dengue zika, chikungunya? (fiebre) |
| `vs06_0643_B` | ¿Cuáles son los sintomas que puede producir el dengue zika, chikungunya? (Dolor de cabeza) |
| `vs06_0643_C` | ¿Cuáles son los sintomas que puede producir el dengue zika, chikungunya? (Dolor muscular) |
| `vs06_0643_D` | ¿Cuáles son los sintomas que puede producir el dengue zika, chikungunya? (Dolor retroocular) |
| `vs06_0643_E` | ¿Cuáles son los sintomas que puede producir el dengue zika, chikungunya? (Sangrado de Nariz y encias) |
| `vs06_0643_F` | ¿Cuáles son los sintomas que puede producir el dengue zika, chikungunya? (Escalofrios) |
| `vs06_0643_X` | ¿Cuáles son los sintomas que puede producir el dengue zika, chikungunya? (Otro sintoma) |
| `vs06_0643_Y` | ¿Cuáles son los sintomas que puede producir el dengue zika, chikungunya? (No sabe) |
| `vs06_0643_X_cod` | ¿Cuáles son los sintomas que puede producir el dengue zika, chikungunya? (Especifique el otro sintoma) |
| `vs06_0644_A` | ¿Entre las mujeres de su familia, ¿ha tenido cáncer de mama su: esposa o pareja? |
| `vs06_0644_B` | ¿Entre las mujeres de su familia, ¿ha tenido cáncer de mama su: abuela (s)? |
| `vs06_0644_C` | ¿Entre las mujeres de su familia, ¿ha tenido cáncer de mama su: madre ? |
| `vs06_0644_D` | ¿Entre las mujeres de su familia, ¿ha tenido cáncer de mama su: hermana (s)? |
| `vs06_0644_E` | ¿Entre las mujeres de su familia, ¿ha tenido cáncer de mama su: tía (s)? |
| `vs06_0644_F` | ¿Entre las mujeres de su familia, ¿ha tenido cáncer de mama su: hija (s)? |
| `vs06_0644_X` | ¿Entre las mujeres de su familia, ¿ha tenido cáncer de mama su: otra persona de su familia? |
| `vs06_0644_X_esp` | ¿Entre las mujeres de su familia, ¿ha tenido cáncer de mama su: especifique si es otra persona de su familia? |
| `vs06_0645_A_1` | Por favor me dice si el año pasado 2022 sufrió algún tipo de accidente en la ciudad o pueblo/campo:¿Sufrió el año pasado algun tipo de Accidente de tránsito en la ciudad?</br> |
| `vs06_0645_B_1` | ¿Sufrió el año pasado algún tipo de Accidente de transito en el pueblo/campo? |
| `vs06_0645_C_1` | ¿Sufrió el año pasado algún Accidente doméstico en la cuidad? |
| `vs06_0645_D_1` | ¿Sufrió el año pasado algún tipo de Accidente doméstico en el pueblo/campo? |
| `vs06_0645_E_1` | ¿Sufrió el año pasado algun tipo de Accidente Deportivo en la ciudad? |
| `vs06_0645_F_1` | ¿Sufrió el año pasado algún tipo de Accidente Deportivo en el pueblo/campo? |
| `vs06_0645_X_1` | ¿Sufrió el año pasado algún tipo de Accidente en el Trabajo en la ciudad? |
| `vs06_0645_X_1_cod` | ¿Sufrió el año pasado algún tipo de Accidente de Trabajo en el pueblo/campo? |
| `vs06_0645_A_2` | ¿Sufrió el año pasado algún tipo de Accidente en Desastre natural en la ciudad? |
| `vs06_0645_B_2` | ¿Sufrió el año pasado algún tipo de Accidente en Desastre natural en el pueblo/campo? |
| `vs06_0645_C_2` | ¿Sufrió el año pasado algún tipo de accidente en alguna Convulsión social en la ciudad? |
| `vs06_0645_D_2` | "¿Sufrió el año pasado algún tipo de accidente en alguna Convulsion Social en el pueblo/campo?" |
| `vs06_0645_E_2` | "¿Sufrió el año pasado algún tipo de accidente deportivo en el campo/campo?" |
| `vs06_0645_F_2` | Por favor me dice si el año pasado 2022 sufrio algun tipo de accidente en la ciudad o en el campo? ¿otro tipo de accidente en el campo? |
| `vs06_0645_X_2` | ¿Sufrió Otro tipo de accidente en el pueblo/campo? |
| `vs06_0645_X_2_cod` | Por favor me dice si el año pasado 2022 sufrio algun tipo de accidente en la ciudad o en el campo? ¿Especificar el otro tipo de accidente ya sea en la ciudad o en el campo? |
| `vs06_0647_A` | Si tuvo un accidente de trabajo. ¿quién cubrió los gastos incurridos? ¿seguridad social? |
| `vs06_0647_B` | Si tuvo un accidente de trabajo. ¿quién cubrió los gastos incurridos? ¿empresa contratante? |
| `vs06_0647_C` | Si tuvo un accidente de trabajo. ¿quién cubrió los gastos incurridos? ¿usted mismo? |
| `vs06_0648_A` | ¿Usted es beneficiario del SUS o esta asegurado en una Caja de Salud o un seguro Privado? marcar las respuestas mencionadas (SUS) |
| `vs06_0648_B` | ¿Usted es beneficiario del SUS o esta asegurado en una Caja de Salud o un seguro Privado? (CAJAS DE SALUD) |
| `vs06_0648_C` | ¿Usted es beneficiario del SUS o esta asegurado en una Caja de Salud o un seguro Privado? (SEGURO PRIVADO) |
| `vs06_0648_X` | ¿Usted es beneficiario del SUS o esta asegurado en una Caja de Salud o un seguro Privado? (OTRO SEGURO) |
| `vs06_0648_X_cod` | ¿Usted es beneficiario del SUS o esta asegurado en una Caja de Salud o un seguro Privado? (ESPECIFIQUE SI ES OTRO) |
| `vs06_0649` | ¿Recibio la vacuna Antidifterica-Antitetanica (DT)? |
| `vs06_0650` | ¿Cuantas dosis de DT ha recibido? |
| `vs07_0701` | Ahora me gustaría hablarle de algo más. ¿Ha oído usted hablar del VIH/ SIDA? |
| `vs07_0702_A` | ¿Qué puede hacer una persona para evitar que le transmitan el VIH, que produce el SIDA? (NO TENER RELACIONES SEXUALES) |
| `vs07_0702_B` | ¿Qué puede hacer una persona para evitar que le transmitan el VIH, que produce el SIDA? (USAR CONDONES) |
| `vs07_0702_C` | ¿Qué puede hacer una persona para evitar que le transmitan el VIH, que produce el SIDA? (TENER SEXO CON UNA SOLA PAREJA/SERLE FIEL A SU PAREJA) |
| `vs07_0702_D` | ¿Qué puede hacer una persona para evitar que le transmitan el VIH, que produce el SIDA? (DISMINUIR EL NÚMERO DE PAREJAS SEXUALES) |
| `vs07_0702_E` | ¿Qué puede hacer una persona para evitar que le transmitan el VIH, que produce el SIDA? (NO TENER SEXO CON PROSTITUTAS) |
| `vs07_0702_F` | ¿Qué puede hacer una persona para evitar que le transmitan el VIH, que produce el SIDA? (NO TENER SEXO CON PERSONAS QUE TIENEN MÁS DE UNA PAREJA) |
| `vs07_0702_G` | ¿Qué puede hacer una persona para evitar que le transmitan el VIH, que produce el SIDA? (NO TENER SEXO CON HOMOSEXUALES) |
| `vs07_0702_H` | ¿Qué puede hacer una persona para evitar que le transmitan el VIH, que produce el SIDA? (NO TENER SEXO CON PERSONAS QUE SE INYECTAN DROGAS) |
| `vs07_0702_I` | ¿Qué puede hacer una persona para evitar que le transmitan el VIH, que produce el SIDA? (EVITANDO TRANSFUSIONES DE SANGRE) |
| `vs07_0702_J` | ¿Qué puede hacer una persona para evitar que le transmitan el VIH, que produce el SIDA? (EVITANDO INYECCIONES/TATUAJES) |
| `vs07_0702_K` | ¿Qué puede hacer una persona para evitar que le transmitan el VIH, que produce el SIDA? (NO BESARSE) |
| `vs07_0702_L` | ¿Qué puede hacer una persona para evitar que le transmitan el VIH, que produce el SIDA? (NO ABRAZAR PERSONAS CON SIDA) |
| `vs07_0702_M` | ¿Qué puede hacer una persona para evitar que le transmitan el VIH, que produce el SIDA? (NO COMPARTIENDO NAVAJAS/ CUCHILLAS DE AFEITAR/ RASURAR) |
| `vs07_0702_N` | ¿Qué puede hacer una persona para evitar que le transmitan el VIH, que produce el SIDA? (TENER BUENA DIETA) |
| `vs07_0702_O` | ¿Qué puede hacer una persona para evitar que le transmitan el VIH, que produce el SIDA? (NO COMPARTIENDO ALIMENTOS CON UNA PERSONA QUE TIENE EL VIRUS VIH O EL SIDA) |
| `vs07_0702_X` | ¿Qué puede hacer una persona para evitar que le transmitan el VIH, que produce el SIDA? (OTRO) |
| `vs07_0702_Z` | ¿Qué puede hacer una persona para evitar que le transmitan el VIH, que produce el SIDA? (NO SABE) |
| `vs07_0702_X_cod` | (ESPECIFÍQUE OTRO) ¿Qué puede hacer una persona para evitar que le transmitan el VIH, que produce el SIDA? |
| `vs07_0703` | ¿Pueden las personas evitar contraer el VIH teniendo una sola pareja sexual fiel que no este infectada? |
| `vs07_0704` | ¿Pueden las personas protegerse del VIH usando condones cada vez que tienen relaciones sexuales? |
| `vs07_0705` | ¿Puede una persona contraer el VIH que causa el SIDA compartiendo alimentos con una persona que tiene VIH/SIDA? |
| `vs07_0706` | ¿Pueden las personas protegerse de contraer el VIH no teniendo relaciones sexuales? |
| `vs07_0707` | ¿Puede una persona contraer el VIH por transfusiones sanguíneas, o por compartir jeringas? |
| `vs07_0708` | "¿Piensa usted que es posible que una persona que parece saludable, pueda tener el VIH que causa el SIDA?" |
| `vs07_0709_A` | En qué momento puede transmitir la madre infectada al hijo, el VIH, que provoca el SIDA:A. ¿Durante el embarazo? |
| `vs07_0709_B` | En qué momento puede transmitir la madre infectada al hijo, el VIH, que provoca el SIDA:B. ¿Durante el parto? |
| `vs07_0709_C` | En qué momento puede transmitir la madre infectada al hijo, el VIH, que provoca el SIDA:C. ¿Durante la cesárea? |
| `vs07_0709_D` | En qué momento puede transmitir la madre infectada al hijo, el VIH, que provoca el SIDA:D. ¿Mientras está lactando o amamantando? |
| `vs07_0711` | ¿Alguna vez, ha hablado usted con su esposa/compañera sobre las formas de evitar transmitirse el VIH? |
| `vs07_0712_A` | ¿Está usted de acuerdo o en desacuerdo con que se de información sobre VIH/SIDA en:A. La radio? |
| `vs07_0712_B` | ¿Está usted de acuerdo o en desacuerdo con que se de información sobre VIH/SIDA en:B. La televisión? |
| `vs07_0712_C` | ¿Está usted de acuerdo o en desacuerdo con que se de información sobre VIH/SIDA en:C. El periódico? |
| `vs07_0712_D` | ¿Está usted de acuerdo o en desacuerdo con que se de información sobre VIH/SIDA en:D. Internet? |
| `vs07_0713` | ¿Compraría usted vegetales/verduras de alguien que estuviese infectado con VIH que causa el SIDA? |
| `vs07_0714` | ¿Considera usted que niñas y niños que viven con VIH deben asistir a la escuela con niñas y niños que no tienen VIH? |
| `vs07_0715_A` | Si algún miembro de su familia contrajera el VIH que causa el SIDA, ¿Usted:A. ¿Querría mantenerlo en secreto? |
| `vs07_0715_B` | Si algún miembro de su familia contrajera el VIH que causa el SIDA, ¿Usted:B. ¿Querría apoyarlo? |
| `vs07_0715_C` | Si algún miembro de su familia contrajera el VIH que causa el SIDA, ¿Usted:C. ¿Estaría dispuesta a cuidarlo en su propia casa? |
| `vs07_0715_D` | Si algún miembro de su familia contrajera el VIH que causa el SIDA, ¿Usted:D. ¿Lo expulsaría de su casa? |
| `vs07_0716` | ¿Se le debe hablar a los niños/as entre 12-14 años sobre el uso del condón para protegerse del SIDA? |
| `vs07_0717` | Yo no quiero conocer los resultados, pero ¿alguna vez se ha realizado la prueba del VIH? |
| `vs07_0718` | ¿La Última vez que se hizo una prueba de VIH recogió sus resultados? |
| `vs07_0719` | ¿Estaría dispuesto a realizarse una prueba de VIH? |
| `vs07_0720` | "¿Sabe usted de algún lugar, donde la gente se puede hacer la prueba del VIH, que causa el SIDA?" |
| `vs07_0721_A` | ¿Cuál es ese lugar? (PUESTO DE SALUD) |
| `vs07_0721_B` | ¿Cuál es ese lugar? (CENTRO DE SALUD AMBULATORIO) |
| `vs07_0721_C` | ¿Cuál es ese lugar? (CENTRO DE SALUD CON INTERNACION) |
| `vs07_0721_D` | ¿Cuál es ese lugar? (CENTRO DE SALUD INTEGRAL) |
| `vs07_0721_E` | ¿Cuál es ese lugar? (HOSPITAL DE SEGUNDO NIVEL) |
| `vs07_0721_F` | ¿Cuál es ese lugar? (HOSPITAL DE TERCER NIVEL) |
| `vs07_0721_G` | ¿Cuál es ese lugar? (HOSPITAL ESPECIALIZADO) |
| `vs07_0721_H` | ¿Cuál es ese lugar? (CAJA NACIONAL DE SALUD) |
| `vs07_0721_I` | ¿Cuál es ese lugar? (CAJA DE LA BANCA PRIVADA) |
| `vs07_0721_J` | ¿Cuál es ese lugar? (CAJA PETROLERA) |
| `vs07_0721_K` | ¿Cuál es ese lugar? (CAJA DE LA BANCA ESTATAL) |
| `vs07_0721_L` | ¿Cuál es ese lugar? (CORDES) |
| `vs07_0721_M` | ¿Cuál es ese lugar? (CAJA DE CAMINOS) |
| `vs07_0721_N` | ¿Cuál es ese lugar? (COSSMIL/FFAA) |
| `vs07_0721_O` | ¿Cuál es ese lugar? (SEGURO UNIVERSITARIO) |
| `vs07_0721_P` | ¿Cuál es ese lugar? (ORGANISMOS PRIVADOS (PRIMER NIVEL, SEGUNDO NIVEL, TERCER NIVEL) |
| `vs07_0721_Q` | ¿Cuál es ese lugar? (IGLESIA PRIMER NIVEL, SEGUNDO NIVEL, TERCER NIVEL) |
| `vs07_0721_R` | ¿Cuál es ese lugar? (PROMOTOR DE LA SALUD/RPS/OTRO AGENTE) |
| `vs07_0721_S` | ¿Cuál es ese lugar? (VISITA DOMICILIARIA) |
| `vs07_0721_T` | ¿Cuál es ese lugar? (FARMACIA) |
| `vs07_0721_U` | ¿Cuál es ese lugar? (MEDICINA TRADICIONAL) |
| `vs07_0721_V` | ¿Cuál es ese lugar? (NO ACUDIÓ A NINGUN E.S./NO FUE) |
| `vs07_0721_X` | ¿Cuál es ese lugar? (OTRO LUGAR:) |
| `vs07_0721_Y` | ¿Cuál es ese lugar? (NO SABE) |
| `vs07_0721_X_cod` | (ESPECIFIQUE) OTRO LUGAR |
| `vs07_0722` | Aparte del VIH/SIDA ¿Usted ha oído hablar de otras infecciones que se pueden contagiar mediante las relaciones sexuales? |
| `vs07_0724` | Ha tenido usted alguna infección de transmisión sexual durante los últimos 12 meses? |
| `vs07_0725_01` | Hizo usted algo de lo siguiente para evitar contagiar una infección de transmisión sexual a su pareja:A. ¿Dejó de tener relaciones sexuales? |
| `vs07_0725_02` | Hizo usted algo de lo siguiente para evitar contagiar una infección de transmisión sexual a su pareja:B. ¿Usó condones al tener relaciones sexuales? |
| `vs07_0725_03` | Hizo usted algo de lo siguiente para evitar contagiar una infección de transmisión sexual a su pareja:C. ¿Tomó medicamentos? |
| `vs07_0726` | Si usted tuviera una infección de transmisión sexual/enfermedad venérea. ¿Sabe que tendría un mayor riesgo de infectarse con el virus VIH que causa el SIDA? |
| `vs08_0801_A` | Verifique la presencia de otras personas. Se recomienda privacidad. Presencia de otros: menores de 10 años |
| `vs08_0801_B` | Verifique la presencia de otras personas.Se recomienda privacidad. Presencia de otros: esposa/compañera |
| `vs08_0801_C` | Verifique la presencia de otras personas. Se recomienda privacidad. Presencia de otros: otros hombres |
| `vs08_0801_D` | Algunas preguntas son muy personales,sin embargo, sus respuestas son muy importantes para ayudar a entender la condición de los hombres en bolivia.Le aseguro que sus respuestas son completamente confidenciales |
| `vs08_0803_A` | Ahora me gustaría conversar con usted acerca de la relación con su última esposa/ compañera ¿Para usted quien sufre mas violencia en las parejas? La mujer |
| `vs08_0803_B` | Ahora me gustaría conversar con usted acerca de la relación con su última esposa/ compañera si las siguientes situaciones se presentaron los últimos 12 meses ¿lo celaba con alguna amiga? |
| `vs08_0803_C` | Ahora me gustaría conversar con usted acerca de la relación con su última esposa/ compañera ¿Para usted quien sufre mas violencia en las parejas? Ambos por igual |
| `vs08_0803_Z` | ¿Quién sufre más violencia en las parejas? (NO SABE/NO RESPONDE) |
| `vs08_0804_A` | Para usted ¿Cuales son los motivos mas comunes para que exista violencia en una relacion de pareja? Los celos |
| `vs08_0804_B` | Para usted ¿Cuales son los motivos mas comunes para que exista violencia en una relacion de pareja? La infidelidad . |
| `vs08_0804_C` | Para usted ¿Cuales son los motivos mas comunes para que exista violencia en una relacion de pareja? Otro |
| `vs08_0804_D` | Para usted ¿Cuales son los motivos mas comunes para que exista violencia en una relacion de pareja? El abuso del alcohol |
| `vs08_0804_E` | Para usted ¿Cuales son los motivos mas comunes para que exista violencia en una relacion de pareja? Experiencia de la infancia |
| `vs08_0804_F` | Para usted ¿Cuales son los motivos mas comunes para que exista violencia en una relacion de pareja? Problemas con los hijos |
| `vs08_0804_G` | Para usted ¿Cuales son los motivos mas comunes para que exista violencia en una relacion de pareja? incumplimiento de resp. domesticas |
| `vs08_0804_H` | Para usted ¿Cuales son los motivos mas comunes para que exista violencia en una relacion de pareja? machismo/sistema patrical |
| `vs08_0804_X` | Para usted ¿Cuáles son los motivos más comunes para que exista violencia en una relación de pareja? (OTRAS) |
| `vs08_0804_X_cod` | (ESPECIFÍQUE OTRAS) ¿Cuáles son los motivos más comunes para que exista violencia en una relación de pareja? |
| `vs08_0805_A` | Ahora me gustaría conversar con usted acerca de la relación con su última esposa/ compañera si las siguientes situaciones se presentaron los últimos 12 meses ¿le acusaba de serle infiel? |
| `vs08_0805_B` | Por favor digame si en los ultimos 12 meses se presentaron las siguientes situaciones en la relacíon con su esposa(compañera/novia o pareja) insultos palabras groseras |
| `vs08_0805_C` | Ahora me gustaría conversar con usted acerca de la relación con su última esposa/ compañera si las siguientes situaciones se presentaron los últimos 12 meses ¿trataba de limitarle contactos con su familia? |
| `vs08_0805_D` | Ahora me gustaría conversar con usted acerca de la relación con su última esposa/ compañera si las siguientes situaciones se presentaron los últimos 12 meses ¿lo humillaba o insultaba? |
| `vs08_0805_E` | Ahora me gustaría conversar con usted acerca de la relación con su última esposa/ compañera si las siguientes situaciones se presentaron los últimos 12 meses ¿lo amenazaba con abandonarlo? |
| `vs08_0805_F` | Ahora me gustaría conversar con usted acerca de la relación con su última esposa/ compañera si las siguientes situaciones se presentaron los últimos 12 meses ¿lo amenazaba con quitarle a sus hijas/os? |
| `vs08_0805_G` | Ahora me gustaría conversar con usted acerca de la relación con su última esposa/ compañera si las siguientes situaciones se presentaron los últimos 12 meses ¿al enojarse rompía objetos, como forma de amenaza? |
| `vs08_0805_H` | Se consulta al hombre si en los últimos 12 meses ha sufrido algunas situaciones de violencia psicológica y con que frecuencia departe de su pareja como ser: Rompia objetos como amenza |
| `vs08_0805_I` | Se consulta al hombre si en los últimos 12 meses ha sufrido algunas situaciones de violencia psicológica y con que frecuencia departe de su pareja como ser: amenaza con no cumplir con las responsabilidades economicas |
| `vs08_0805_J` | Se consulta al hombre si en los últimos 12 meses ha sufrido algunas situaciones de violencia psicológica y con que frecuencia departe de su pareja como ser: control recursos ecno/quita libertad/impide act. laborales |
| `vs08_0805_K` | Por favor digame si en los ultimos 12 meses se presentaron las siguientes situaciones en la relacíon con su esposa(compañera/novia o pareja). Control recursos economico /quita libertad/ Impide act. Laborales. |
| `vs08_0805_X` | Por favor dígame si en los últimos 12 meses se presentaron las siguientes situaciones en la relación con su esposa/ compañera/ novia ó pareja(X) ¿Alguna otra? (especifique) |
| `vs08_0805_X_cod` | (ESPECIFÍQUE) OTRA |
| `vs08_0807_A` | Como resultado de éstas situaciones con su esposa/compañera: ¿sintió miedo constante a la reacción de su esposa/compañera? |
| `vs08_0807_B` | Como resultado de éstas situaciones con su esposa/compañera: ¿tuvo desgano, tristeza o llanto frecuentes? |
| `vs08_0807_C` | Como resultado de éstas situaciones con su esposa/ compañera: ¿dejó de trabajar? |
| `vs08_0807_D` | Como resultado de éstas situaciones con su esposa/ compañera: ¿dejó de realizar otras actividades importantes para usted? |
| `vs08_0807_E` | Como resultado de éstas situaciones con su esposa/compañera: ¿ha pensado en abandonar su hogar? |
| `vs08_0807_F` | Como resultado de éstas situaciones con su esposa/ compañera: ¿ha pensado alguna vez en lastimarse a si mismo? |
| `vs08_0807_X` | Como resultado de las situaciones mencionadas anteriormente Usted:X. ¿Alguna otra? (especifique) |
| `vs08_0807_X_cod` | (ESPECIFÍQUE OTRO) Como resultado de las situaciones mencionadas |
| `vs08_0808_A` | Digame si en los últimos 12 meses, se presentaron las siguientes situaciones en la relación con su esposa/ compañera, muy a menudo, algunas veces, una vez o nunca. ¿lo ha empujado o jaloneado? |
| `vs08_0808_B` | Digame si en los últimos 12 meses, se presentaron las siguientes situaciones en la relación con su esposa/ compañera, muy a menudo, algunas veces, una vez o nunca. ¿lo ha golpeado con la mano o con el pie? |
| `vs08_0808_C` | Digame si en los últimos 12 meses, se presentaron las siguientes situaciones en la relación con su esposa/ compañera, muy a menudo, algunas veces, una vez o nunca. ¿lo ha golpeado con objeto? |
| `vs08_0808_D` | Digame si en los últimos 12 meses, se presentaron las siguientes situaciones en la relación con su esposa/ compañera, muy a menudo, algunas veces, una vez o nunca. ¿lo ha tratado de estrangular o quemar? |
| `vs08_0808_E` | Digame, si en los últimos 12 meses se presentó alguna situación en la relación con su esposa/ compañera como: AMENAZA CON CUCHILLO/NAVAJA/ PISTOLA |
| `vs08_0808_F` | Digame, si en los últimos 12 meses se presentó alguna situación en la relación con su esposa/ compañera como: AGRESIÓN CON CUCHILLO/NAVAJA/ PISTOLA |
| `vs08_0808_G` | Los últimos 12 meses, se presentaron las siguientes situaciones en la relación con su esposa/ compañera, muy a menudo, algunas veces, una vez o nunca. ¿lo ha forzado a tener relaciones sexuales que usted no quería? |
| `vs08_0808_H` | Digame, si en los últimos 12 meses se presentó alguna situación en la relación con su esposa/ compañera como: HA EXIGIDO TENER RELACIONES SEXUALES AUNUQE USTED NO QUERIA |
| `vs08_0808_I` | Digame, si en los últimos 12 meses se presentó alguna situación en la relación con su esposa/ compañera como: HA FORZADO A TENER ALGUN TIPO DE ACTIVIDAD SEUXAL QUE USTED NO QUERIA |
| `vs08_0808_X` | Por favor dígame si en los últimos 12 meses se presentaron las siguientes situaciones en la relación con su esposa/ compañera/ novia ó pareja(X) ¿Alguna otra? (especifique) |
| `vs08_0808_X_cod` | (ESPECIFÍQUE) OTRA |
| `vs08_0810_A` | ¿estas situaciones se han presentado a solas o en presencia de otras personas? ¿a solas? |
| `vs08_0810_B` | ¿estas situaciones se han presentado a solas o en presencia de otras personas? ¿en presencia de amigos? |
| `vs08_0810_C` | ¿estas situaciones se han presentado a solas o en presencia de otras personas? ¿en presencia de familiares? |
| `vs08_0810_D` | ¿estas situaciones se han presentado a solas o en presencia de otras personas? ¿en presencia de los hijos? |
| `vs08_0810_X` | ¿estas situaciones se han presentado a solas o en presencia de otras personas? ¿otras personas? (especificar) |
| `vs08_0810_X_cod` | (ESPECIFÍQUE) OTRAS PERSONAS |
| `vs08_0811_A` | Como resultado de estas agresiones fisicas de su esposa/compañera: ¿sintió miedo constante a la reacción de su esposa/compañera? |
| `vs08_0811_B` | Como resultado de estas agresiones fisicas de su esposa/compañera: ¿tuvo desgano, tristeza o llanto frecuentes? |
| `vs08_0811_C` | Como resultado de estas agresiones fisicas de su esposa/compañera: ¿tuvo moretones, marcas y dolores en el cuerpo, heridas o algún hueso quebrado? |
| `vs08_0811_D` | Como resultado de estas agresiones fisicas de su esposa/compañera: ¿tuvo pérdida temporal o definitiva de algún órgano, función o parte del cuerpo? |
| `vs08_0811_E` | Como resultado de estas agresiones fisicas de su esposa/compañera: ¿dejó de trabajar? |
| `vs08_0811_F` | Como resultado de estas agresiones fisicas de su esposa/compañera: ¿dejó de realizar otras actividades importantes para usted? |
| `vs08_0811_G` | Como resultado de estas agresiones fisicas de su esposa/compañera: ¿dejó de participar en organizaciones sociales o politicas donde participaba? |
| `vs08_0811_H` | Como resultado de las agresiones físicas de su esposa/compañera: PENSO EN ABANDONAR SU HOGAR |
| `vs08_0811_I` | Como resultado de estas agresiones fisicas de su esposa/compañera: ¿ha pensado alguna vez en lastimarse a si mismo? |
| `vs08_0811_X` | Como resultado de las situaciones mencionadas anteriormente Usted:(X) ¿Alguna otra? (especifique) |
| `vs08_0811_X_cod` | (ESPECIFÍQUE) OTRA |
| `vs08_0813` | ¿Cómo resultado de lo que su esposa/compañera/novia o pareja le hizo, usted fue al médico, establecimiento de salud y/o médico forense? |
| `vs08_0814` | El personal del establecimiento de salud, ¿le orientó para denunciar la agresión? |
| `vs08_0815_A` | Que tipo de orientación le brinco el personal de salud? APOYO Y CONTENCION EMOCIONAL |
| `vs08_0815_B` | Que tipo de orientación le brinco el personal de salud? ORIENTACION SERVICIOS |
| `vs08_0815_C` | Que tipo de orientación le brinco el personal de salud? DERIVACION DE SERVICIOS |
| `vs08_0815_X` | ¿Qué tipo de orientación le brindo el personal de salud? (OTRO) |
| `vs08_0815_X_cod` | (ESPECIFÍQUE OTRO) ¿Qué tipo de orientación le brindo el personal de salud? |
| `vs08_0816` | Después de la atención y una vez establecido el diagnóstico ¿le otorgaron un certificado médico? |
| `vs08_0817` | Cuando fue agredido por su esposa/compañera/novia o pareja. ¿Pidió ayuda a personas cercanas a usted? |
| `vs08_0818_A` | ¿a quiénes? ¿madre? |
| `vs08_0818_B` | ¿a quiénes? ¿padre? |
| `vs08_0818_C` | ¿a quiénes? ¿madrastra? |
| `vs08_0818_D` | ¿a quiénes? ¿padrastro? |
| `vs08_0818_E` | ¿a quiénes? ¿hermana? |
| `vs08_0818_F` | ¿a quiénes? ¿hermano? |
| `vs08_0818_G` | ¿a quiénes? ¿hija? |
| `vs08_0818_H` | ¿a quiénes? ¿hijo? |
| `vs08_0818_I` | ¿a quiénes? ¿parientes políticos (suegro/a, cuñado/a? |
| `vs08_0818_J` | ¿a quiénes? ¿redes sociales en internet? |
| `vs08_0818_K` | ¿a quiénes? ¿vecinos/amigos? |
| `vs08_0818_X` | ¿a quiénes? ¿otras personas? (especifique) |
| `vs08_0818_X_cod` | (ESPECIFÍQUE) OTRAS PERSONAS |
| `vs08_0819` | Cuando lo agredieron, ¿Ud. denunció la agresión? |
| `vs08_0820_A` | Cuando lo agredieron, ¿ud. Denunció la agresión? ¿centro de salud? |
| `vs08_0820_B` | Cuando lo agredieron, ¿ud. Denunció la agresión? ¿slims? |
| `vs08_0820_C` | Cuando lo agredieron, ¿ud. Denunció la agresión? ¿defensoria de la niñez y adolescencia? |
| `vs08_0820_D` | ¿A que institución acudió? : IDIF - MEDICO FORENCE |
| `vs08_0820_E` | Cuando lo agredieron, ¿ud. Denunció la agresión? ¿sedeges? |
| `vs08_0820_F` | ¿A que institución acudió? : MINISTERIO DE JUSTICIA(SIJ-PLU) |
| `vs08_0820_G` | ¿A que institución acudió? : MINISTERIO DE JUSTICIA(SEPDAPI) |
| `vs08_0820_H` | Cuando lo agredieron, ¿ud. Denunció la agresión? ¿felcv/brigada? |
| `vs08_0820_I` | Cuando lo agredieron, ¿ud. Denunció la agresión? ¿policía? |
| `vs08_0820_J` | Cuando lo agredieron, ¿ud. Denunció la agresión? ¿autoridades comunitarias/ originarias? |
| `vs08_0820_K` | Cuando lo agredieron, ¿ud. Denunció la agresión? ¿ong? |
| `vs08_0820_L` | Cuando lo agredieron, ¿ud. Denunció la agresión? ¿fiscalia? |
| `vs08_0820_X` | ¿A qué institución acudió? (OTRA) |
| `vs08_0820_X_cod` | (ESPECIFÍQUE OTRA) ¿A qué institución acudió? |
| `vs08_0821_A` | ¿qué tipo de apoyo recibió? ¿médico? |
| `vs08_0821_B` | ¿qué tipo de apoyo recibió? ¿psicológico? |
| `vs08_0821_C` | ¿qué tipo de apoyo recibió? ¿legal? |
| `vs08_0821_D` | ¿qué tipo de apoyo recibió? ¿social (información/orientación)? |
| `vs08_0821_E` | ¿qué tipo de apoyo recibió? ¿comunitario? |
| `vs08_0821_X` | ¿qué tipo de apoyo recibió? ¿otro? (especifique) |
| `vs08_0821_Y` | ¿qué tipo de apoyo recibió? ¿no recibió apoyo? |
| `vs08_0821_X_cod` | (ESPECIFIQUE OTRO) ¿Qué tipo de apoyo recibió? |
| `vs08_0822_A` | ¿por qué no denunció a la persona que la agredió? ¿no sabia donde ir? |
| `vs08_0822_B` | ¿por qué no denunció a la persona que la agredió? ¿verguenza y humillación? |
| `vs08_0822_C` | ¿por qué no denunció a la persona que la agredió? ¿es normal? |
| `vs08_0822_D` | ¿por qué no denunció a la persona que la agredió? ¿yo tenia la culpa? |
| `vs08_0822_E` | ¿por qué no denunció a la persona que la agredió? ¿miedo a la separación? |
| `vs08_0822_F` | ¿por qué no denunció a la persona que la agredió? ¿miedo a quedarse solo? |
| `vs08_0822_G` | ¿por qué no denunció a la persona que la agredió? ¿miedo a represalias? |
| `vs08_0822_H` | ¿por qué no denunció a la persona que la agredió? ¿miedo a que su hogar no tenga sustento económico? |
| `vs08_0822_I` | ¿por qué no denunció a la persona que la agredió? ¿pensé que no volveria a ocurrir? |
| `vs08_0822_J` | ¿por qué no denunció a la persona que la agredió? ¿no creia en la justicia? |
| `vs08_0822_K` | ¿por qué no denunció a la persona que la agredió? ¿pensé que me cobrarían? |
| `vs08_0822_L` | ¿por qué no denunció a la persona que la agredió? ¿recibi dinero o pago en especie? |
| `vs08_0822_M` | ¿por qué no denunció a la persona que la agredió? ¿por no afectar a los hijos? |
| `vs08_0822_N` | ¿por qué no denunció a la persona que la agredió? ¿miedo a que me quiten los hijos? |
| `vs08_0822_X` | ¿por qué no denunció a la persona que la agredió? ¿otra? (especifique) |
| `vs08_0822_X_cod` | (ESPECIFIQUE OTRO) ¿Por qué no hizo la denuncia? |
| `vs08_0823_A` | Segun su opinion , los hechos de violencia sexual suceden habitualmente en: LUGARES DE ESTUDIO Y TRABAJO |
| `vs08_0823_B` | Segun su opinion , los hechos de violencia sexual suceden habitualmente en: LUGARES DE ESTUDIO Y TRABAJO |
| `vs08_0823_C` | Segun su opinion , los hechos de violencia sexual suceden habitualmente en: LA PROPIA CASA |
| `vs08_0823_D` | Segun su opinion , los hechos de violencia sexual suceden habitualmente en: CASA DE FAMILIARES |
| `vs08_0823_E` | Segun su opinion , los hechos de violencia sexual suceden habitualmente en: EVENTOS PUBLICOS) |
| `vs08_0823_X` | Según su opinión, los hechos de violencia sexual suceden habitualmente en: (OTRO) |
| `vs08_0823_X_cod` | (ESPECIFIQUE OTRO) Según su opinión, los hechos de violencia sexual suceden habitualmente en: |
| `vs08_0824` | Por favor dígame si en los últimos 12 meses, alguna persona que no sea su pareja o sea desconocida ¿Lo agredió de alguna manera? |
| `vs08_0824_cod` | (ESPECIFIQUE) OTRO |
| `vs08_0825_A` | ¿quién lo agredió? ¿padre/madre? |
| `vs08_0825_B` | ¿quién lo agredió? ¿padrastro/madrastra? |
| `vs08_0825_C` | ¿quién lo agredió? ¿hermano/a? |
| `vs08_0825_D` | Si lo agredió alguna persona diferente a su esposa/compañera, quien fue: HIJO/A. |
| `vs08_0825_E` | ¿quién lo agredió? ¿suegro/a? |
| `vs08_0825_F` | ¿quién lo agredió? ¿tio/a? |
| `vs08_0825_G` | ¿quién lo agredió? ¿cuñado/a? |
| `vs08_0825_H` | ¿quién lo agredió? ¿ex esposa/ compañera/pareja? |
| `vs08_0825_I` | ¿quién lo agredió? ¿patrón /jefe? |
| `vs08_0825_J` | ¿quién lo agredió? ¿profesor/a? |
| `vs08_0825_K` | ¿quién lo agredió? ¿catedrático/a? |
| `vs08_0825_L` | Si lo agredió alguna persona diferente a su esposa/compañera, quien fue: COMPAÑERO DE TRABAJO |
| `vs08_0825_M` | ¿quién lo agredió? ¿amigo/a? |
| `vs08_0825_N` | ¿quién lo agredió? ¿dirigente? |
| `vs08_0825_O` | ¿quién lo agredió? ¿desconocido/a? |
| `vs08_0825_X` | ¿quién lo agredió? ¿otro? (especifique) |
| `vs08_0825_X_cod` | (ESPECIFIQUE) OTRO |
| `vs08_0826_A` | ¿dónde lo agredieron? ¿en la calle? |
| `vs08_0826_B` | ¿dónde lo agredieron? ¿en su trabajo? |
| `vs08_0826_C` | ¿dónde lo agredieron? ¿en la escuela/ colegio? |
| `vs08_0826_D` | ¿dónde lo agredieron? ¿en la universidad? |
| `vs08_0826_E` | ¿dónde lo agredieron? ¿en una fiesta? |
| `vs08_0826_F` | ¿dónde lo agredieron? ¿en institución policial/ militar? |
| `vs08_0826_G` | ¿dónde lo agredieron? ¿organización social/partido politico? |
| `vs08_0826_X` | ¿Dónde lo agredieron? (OTRO LUGAR |
| `vs08_0826_X_cod` | (ESPECIFIQUE) OTRO LUGAR |
| `vs08_0827` | ¿Durante los últimos 12 meses ha sido forzado a tener relaciones sexuales por alguna persona diferente a su esposa/ compañera/ novia ó pareja? |
| `vs08_0828_A` | ¿quién lo forzó a tener relaciones sexuales? ¿padre/madre? |
| `vs08_0828_B` | ¿quién lo forzó a tener relaciones sexuales? ¿padrastro/ madrastra? |
| `vs08_0828_C` | ¿quién lo forzó a tener relaciones sexuales? ¿hermano/a? |
| `vs08_0828_D` | La persona diferente a la esposa/compañera del hombre que lo forzó a tener relaciones sexuales fue: Hijo/A. |
| `vs08_0828_E` | ¿quién lo forzó a tener relaciones sexuales? ¿suegro/a? |
| `vs08_0828_F` | ¿quién lo forzó a tener relaciones sexuales? ¿tio/a? |
| `vs08_0828_G` | ¿quién lo forzó a tener relaciones sexuales? ¿cuñado/a? |
| `vs08_0828_H` | ¿quién lo forzó a tener relaciones sexuales? ¿ex esposa/ compañera/pareja? |
| `vs08_0828_I` | ¿quién lo forzó a tener relaciones sexuales? ¿patrón /jefe? |
| `vs08_0828_J` | ¿quién lo forzó a tener relaciones sexuales? ¿profesor/a? |
| `vs08_0828_K` | ¿quién lo forzó a tener relaciones sexuales? ¿catedrático/a? |
| `vs08_0828_L` | ¿quién lo forzó a tener relaciones sexuales? ¿compañero de trabajo |
| `vs08_0828_M` | ¿quién lo forzó a tener relaciones sexuales? ¿amigo/ a? |
| `vs08_0828_N` | ¿quién lo forzó a tener relaciones sexuales? ¿dirigente? |
| `vs08_0828_O` | ¿quién lo forzó a tener relaciones sexuales? ¿desconocido/ a? |
| `vs08_0828_X` | ¿quién lo forzó a tener relaciones sexuales? ¿otro? (especifique) |
| `vs08_0828_Y` | ¿quién lo forzó a tener relaciones sexuales? ¿ninguno/no quiere hablar del tema? |
| `vs08_0828_X_cod` | (ESPECIFIQUE) OTRO |
| `vs08_0829_A` | ¿donde lo forzaron a tener relaciones sexuales? ¿en la calle? |
| `vs08_0829_B` | ¿donde lo forzaron a tener relaciones sexuales? ¿en su trabajo? |
| `vs08_0829_C` | ¿donde lo forzaron a tener relaciones sexuales? ¿en la escuela/ colegio? |
| `vs08_0829_D` | ¿donde lo forzaron a tener relaciones sexuales? ¿en la universidad? |
| `vs08_0829_E` | ¿donde lo forzaron a tener relaciones sexuales? ¿en una fiesta? |
| `vs08_0829_F` | ¿donde lo forzaron a tener relaciones sexuales? ¿en institución policial/ militar? |
| `vs08_0829_G` | ¿donde lo forzaron a tener relaciones sexuales? ¿organizacion social /partido politicor? |
| `vs08_0829_X` | ¿donde lo forzaron a tener relaciones sexuales? ¿otro lugar? (especifique) |
| `vs08_0829_X_cod` | (ESPECIFIQUE) OTRO LUGAR |
| `vs08_0830` | Cuando lo forzaron a tener relaciones sexuales¿Ud. denunció la agresión? |
| `vs08_0831_A` | Cuando lo obligaron o forzaron sexualmente. ¿ud. Denunció la agresión? ¿centro de salud? |
| `vs08_0831_B` | Cuando lo obligaron o forzaron sexualmente. ¿ud. Denunció la agresión? ¿slims? |
| `vs08_0831_C` | Cuando lo obligaron o forzaron sexualmente. ¿ ¿ud. Denunció la agresión? ¿defensoria de la niñez y adolescencia? |
| `vs08_0831_D` | Cuando lo obligaron o forzaron sexualmente. ¿ud. Denunció la agresión? Idf medico forence |
| `vs08_0831_E` | Cuando lo obligaron o forzaron sexualmente. ¿ud. Denunció la agresión? ¿sedeges? |
| `vs08_0831_F` | Cuando lo obligaron o forzaron sexualmente. ¿ud. Denunció la agresión? Ministerio de justicia (sij plu |
| `vs08_0831_G` | Cuando lo obligaron o forzaron sexualmente. ¿ud. Denunció la agresión? MInisterio de justicia (SEPDAPI) |
| `vs08_0831_H` | Cuando lo obligaron o forzaron sexualmente. ¿ud. Denunció la agresión? ¿felcv/brigada? |
| `vs08_0831_I` | Cuando lo obligaron o forzaron sexualmente. ¿ud. Denunció la agresión? ¿policia? |
| `vs08_0831_J` | Cuando lo obligaron o forzaron sexualmente. ¿ ¿ud. Denunció la agresión? ¿autoridades comunitarias/ originarias? |
| `vs08_0831_K` | Cuando lo obligaron o forzaron sexualmente. ¿ud. Denunció la agresión? ¿ong? |
| `vs08_0831_L` | Cuando lo obligaron o forzaron sexualmente. ¿ud. Denunció la agresión? ¿fiscalia? |
| `vs08_0831_X` | Cuando lo obligaron o forzaron sexualmente. ¿ud. Denunció la agresión? ¿otra? (especifique) |
| `vs08_0831_X_cod` | (ESPECIFÍQUE) OTRO |
| `vs08_0832_A` | ¿qué tipo de apoyo recibió: médico, psicológico, legal u otro? ¿médico? |
| `vs08_0832_B` | ¿qué tipo de apoyo recibió: médico, psicológico, legal u otro? ¿psicológico? |
| `vs08_0832_C` | ¿qué tipo de apoyo recibió: médico, psicológico, legal u otro? ¿legal? |
| `vs08_0832_D` | ¿qué tipo de apoyo recibió: médico, psicológico, legal u otro? ¿social (información/orientación)? |
| `vs08_0832_E` | ¿qué tipo de apoyo recibió: médico, psicológico, legal u otro? ¿comunitario? |
| `vs08_0832_X` | ¿qué tipo de apoyo recibió: médico, psicológico, legal u otro? ¿otro? (especifique) |
| `vs08_0832_Y` | ¿qué tipo de apoyo recibió: médico, psicológico, legal u otro? ¿no recibio apoyo? |
| `vs08_0832_X_cod` | ¿qué tipo de apoyo recibió: médico, psicológico, legal u otro? ¿otro? (especifique) codificado |
| `vs08_0833_A` | ¿por qué no denunció? ¿no sabía donde ir? |
| `vs08_0833_B` | ¿por qué no denunció? ¿vergüenza y humillación? |
| `vs08_0833_C` | ¿por qué no denunció? ¿es normal? |
| `vs08_0833_D` | ¿por qué no denunció? ¿yo tenia la culpa? |
| `vs08_0833_E` | ¿por qué no denunció? ¿miedo a la separación? |
| `vs08_0833_F` | ¿por qué no denunció? ¿miedo a quedarse solo? |
| `vs08_0833_G` | ¿por qué no denunció? ¿miedo a represalias? |
| `vs08_0833_H` | ¿por qué no denunció? ¿miedo a que su hogar no tenga sustento económico? |
| `vs08_0833_I` | ¿por qué no denunció? ¿pensé que no volvería a ocurrir? |
| `vs08_0833_J` | ¿por qué no denunció? ¿no creía en la justicia? |
| `vs08_0833_K` | ¿por qué no denunció? ¿pensé que me cobrarían? |
| `vs08_0833_L` | ¿por qué no denunció? ¿recibí dinero o pago en especie? |
| `vs08_0833_M` | ¿por qué no denunció? ¿por no afectar a los hijos? |
| `vs08_0833_N` | ¿por qué no denunció? ¿miedo a que me quiten los hijos? |
| `vs08_0833_X` | ¿por qué no denunció? ¿otra? (especifique) |
| `vs08_0833_X_cod` | ¿por qué no denunció? ¿otra? (especifique) codificado |
| `vs08_0834` | ¿observó usted alguna vez agresiones fisicas entre sus padres? |
| `vs08_0836_A` | ¿quién cuida a sus hijas(os) la mayor parte del tiempo? ¿padre? |
| `vs08_0836_B` | ¿quién cuida a sus hijas(os) la mayor parte del tiempo? ¿madre? |
| `vs08_0836_C` | ¿quién cuida a sus hijas(os) la mayor parte del tiempo? ¿padrastro? |
| `vs08_0836_D` | ¿quién cuida a sus hijas(os) la mayor parte del tiempo? ¿madrastra? |
| `vs08_0836_E` | ¿quién cuida a sus hijas(os) la mayor parte del tiempo? ¿abuelo? |
| `vs08_0836_F` | ¿quién cuida a sus hijas(os) la mayor parte del tiempo? ¿abuela? |
| `vs08_0836_G` | ¿quién cuida a sus hijas(os) la mayor parte del tiempo? ¿hermano/a mayor? |
| `vs08_0836_H` | ¿quién cuida a sus hijas(os) la mayor parte del tiempo? ¿trabajador/a del hogar? |
| `vs08_0836_I` | ¿quién cuida a sus hijas(os) la mayor parte del tiempo? ¿maestro(a) parvularia/ educadoras? |
| `vs08_0836_J` | ¿quién cuida a sus hijas(os) la mayor parte del tiempo? ¿tutor/ a? |
| `vs08_0836_X` | ¿quién cuida a sus hijas(os) la mayor parte del tiempo? ¿otro? (especifique) |
| `vs08_0836_Y` | ¿quién cuida a sus hijas(os) la mayor parte del tiempo? ¿nadie? |
| `vs08_0836_X_cod` | (ESPECIFIQUE OTRO) ¿Quién cuida a sus hijas(os) la mayor parte del tiempo? |
| `vs08_0837_A` | ¿alguna persona agrede a sus hijas(os) en el hogar a titulo de educación, disciplina o corrección? ¿padre? |
| `vs08_0837_B` | ¿alguna persona agrede a sus hijas(os) en el hogar a titulo de educación, disciplina o corrección? ¿madre? |
| `vs08_0837_C` | ¿alguna persona agrede a sus hijas(os) en el hogar a titulo de educación, disciplina o corrección? ¿padrastro? |
| `vs08_0837_D` | ¿alguna persona agrede a sus hijas(os) en el hogar a titulo de educación, disciplina o corrección? ¿madrastra? |
| `vs08_0837_E` | ¿alguna persona agrede a sus hijas(os) en el hogar a titulo de educación, disciplina o corrección? ¿abuelo? |
| `vs08_0837_F` | ¿alguna persona agrede a sus hijas(os) en el hogar a titulo de educación, disciplina o corrección? ¿abuela? |
| `vs08_0837_G` | ¿alguna persona agrede a sus hijas(os) en el hogar a titulo de educación, disciplina o corrección? ¿hermana? |
| `vs08_0837_H` | ¿alguna persona agrede a sus hijas(os) en el hogar a titulo de educación, disciplina o corrección? ¿hermano? |
| `vs08_0837_I` | ¿alguna persona agrede a sus hijas(os) en el hogar a titulo de educación, disciplina o corrección? ¿tio/ tia? |
| `vs08_0837_J` | ¿alguna persona agrede a sus hijas(os) en el hogar a titulo de educación, disciplina o corrección?¿tutor/ tutora? |
| `vs08_0837_X` | ¿alguna persona agrede a sus hijas(os) en el hogar a titulo de educación, disciplina o corrección? ¿otro? (especifique) |
| `vs08_0837_Z` | ¿alguna persona agrede a sus hijas(os) en el hogar a titulo de educación, disciplina o corrección? ¿nadie/ no los castigan? |
| `vs08_0837_X_cod` | (ESPECIFIQUE OTRO) ¿Alguna persona castiga a sus hijas(os) en el hogar a título de educación, disciplina o corrección? |
| `vs08_0839_AA` | Hijos varones: en qué forma castiga ud. A sus hijos varones? ¿jalón de orejas/ palmadas/ sopapos? |
| `vs08_0839_AB` | ¿en qué forma castiga ud. A sus hijos varones? ¿golpes con: chicote, chinelas, cinturón, quimsa charani? |
| `vs08_0839_AC` | ¿en qué forma castiga ud. A sus hijos varones? ¿gritos? |
| `vs08_0839_AD` | ¿en qué forma castiga ud. A sus hijos varones? ¿insultos? |
| `vs08_0839_AE` | ¿en qué forma castiga ud. A sus hijos varones? ¿privándolos de alimentación? |
| `vs08_0839_AF` | ¿en qué forma castiga ud. A sus hijos varones? ¿dejándolos encerrados? |
| `vs08_0839_AG` | ¿en qué forma castiga ud. A sus hijos varones? ¿poniéndoles más trabajo? |
| `vs08_0839_AH` | ¿en qué forma castiga ud. A sus hijos varones? ¿dejándolos fuera de casa? |
| `vs08_0839_AI` | ¿en qué forma castiga ud. A sus hijos varones? ¿echándoles agua? |
| `vs08_0839_AJ` | ¿en qué forma castiga ud. A sus hijos varones? ¿quitándoles la ropa? |
| `vs08_0839_AK` | ¿en qué forma castiga ud. A sus hijos varones? ¿ignorándolos más de un dia? |
| `vs08_0839_AL` | ¿en qué forma castiga ud. A sus hijos varones? ¿quitandoles recreos y mesadas? |
| `vs08_0839_AM` | ¿en qué forma castiga ud. A sus hijos varones? ¿prohibiendo algo que le gusta? |
| `vs08_0839_AN` | ¿en qué forma castiga ud. A sus hijos varones? ¿prohibiendo el uso o decomisando algo que les gusta? |
| `vs08_0839_AO` | ¿en qué forma castiga ud. A sus hijos varones? ¿sacudón /zamarrear? |
| `vs08_0839_AX` | ¿en qué forma castiga ud. A sus hijos varones? ¿otra? (especifique) |
| `vs08_0839_AX_cod` | (ESPECIFIQUE OTRA) (A) En qué forma castiga Ud. a sus hijos varones? |
| `vs08_0839_BA` | Hijos varones:¿en qué forma castiga su esposa/compañera a sus hijos varones? ¿jalón de orejas/ palmadas/ sopapos? |
| `vs08_0839_BB` | ¿en qué forma castiga su esposa/compañera a sus hijos varones? ¿golpes con: chicote, chinelas, cinturón, quimsa charani? |
| `vs08_0839_BC` | ¿en qué forma castiga su esposa/compañera a sus hijos varones? ¿gritos? |
| `vs08_0839_BD` | ¿en qué forma castiga su esposa/compañera a sus hijos varones? ¿insultos? |
| `vs08_0839_BE` | ¿en qué forma castiga su esposa/compañera a sus hijos varones? ¿privándolos de alimentación? |
| `vs08_0839_BF` | ¿en qué forma castiga su esposa/compañera a sus hijos varones? ¿dejándolos encerrados? |
| `vs08_0839_BG` | ¿en qué forma castiga su esposa/compañera a sus hijos varones? ¿poniéndoles más trabajo? |
| `vs08_0839_BH` | ¿en qué forma castiga su esposa/compañera a sus hijos varones? ¿dejándolos fuera de casa? |
| `vs08_0839_BI` | ¿en qué forma castiga su esposa/compañera a sus hijos varones? ¿echándoles agua? |
| `vs08_0839_BJ` | ¿en qué forma castiga su esposa/compañera a sus hijos varones? ¿quitándoles la ropa? |
| `vs08_0839_BK` | ¿en qué forma castiga su esposa/compañera a sus hijos varones? ¿ignorándoles más de un dia? |
| `vs08_0839_BL` | ¿en qué forma castiga su esposa/compañera a sus hijos varones? ¿quitándoles recreos y mesadas? |
| `vs08_0839_BM` | ¿en qué forma castiga su esposa/compañera a sus hijos varones? ¿prohibiendo algo que le gusta? |
| `vs08_0839_BN` | ¿en qué forma castiga ud. A sus hijos varones? ¿prohibiendo el uso o decomisando algo que les gusta? |
| `vs08_0839_BO` | ¿en qué forma castiga su esposa/compañera a sus hijos varones? ¿sacudón /zamarrear? |
| `vs08_0839_BX` | ¿en qué forma castiga su esposa/compañera a sus hijos varones? ¿otra? (especifique) |
| `vs08_0839_BX_cod` | ¿en qué forma castiga su esposa/compañera a sus hijos varones? ¿otra? (especifique) codificado |
| `vs08_0839_CA` | Hijos varones:¿en qué forma castiga esa persona a sus hijos varones? ¿jalón de orejas/ palmadas/ sopapos? |
| `vs08_0839_CB` | ¿en qué forma castiga esa persona a sus hijos varones? ¿golpes con: chicote, chinelas, cinturón, quimsa charani? |
| `vs08_0839_CC` | ¿en qué forma castiga esa persona a sus hijos varones? ¿gritos? |
| `vs08_0839_CD` | ¿en qué forma castiga esa persona a sus hijos varones? ¿insultos? |
| `vs08_0839_CE` | ¿en qué forma castiga esa persona a sus hijos varones? ¿privándolos de alimentación? |
| `vs08_0839_CF` | ¿en qué forma castiga esa persona a sus hijos varones? ¿dejándolos encerrados? |
| `vs08_0839_CG` | ¿en qué forma castiga esa persona a sus hijos varones? ¿poniéndoles más trabajo? |
| `vs08_0839_CH` | ¿en qué forma castiga esa persona a sus hijos varones? ¿dejándolos fuera de casa? |
| `vs08_0839_CI` | ¿en qué forma castiga esa persona a sus hijos varones? ¿echándoles agua? |
| `vs08_0839_CJ` | ¿en qué forma castiga esa persona a sus hijos varones? ¿quitándoles la ropa? |
| `vs08_0839_CK` | ¿en qué forma castiga esa persona a sus hijos varones? ¿ignorándoles más de un dia? |
| `vs08_0839_CL` | ¿en qué forma castiga esa persona a sus hijos varones? ¿quitándoles recreos y mesadas? |
| `vs08_0839_CM` | ¿en qué forma castiga esa persona a sus hijos varones? ¿prohibiendo algo que le gusta? |
| `vs08_0839_CN` | ¿en qué forma castiga ud. A sus hijos varones? ¿prohibiendo el uso o decomisando algo que les gusta? |
| `vs08_0839_CO` | ¿en qué forma castiga esa persona a sus hijos varones? ¿sacudón /zamarrear? |
| `vs08_0839_CX` | ¿en qué forma castiga esa persona a sus hijos varones? ¿otra? (especifique) |
| `vs08_0839_CX_cod` | (ESPECIFIQUE OTRA) (C) En qué forma castiga esa persona a sus hijos varones? |
| `vs08_0840_AA` | Hijas mujeres:en qué forma castiga ud. A sus hijas mujeres: jalón de orejas/ palmadas/ sopapos? |
| `vs08_0840_AB` | ¿en qué forma castiga ud. A sus hijas mujeres? ¿golpes con: chicote, chinelas, cinturón, quimsa charani? |
| `vs08_0840_AC` | ¿en qué forma castiga ud. A sus hijas mujeres? ¿gritos? |
| `vs08_0840_AD` | ¿en qué forma castiga ud. A sus hijas mujeres? ¿insultos? |
| `vs08_0840_AE` | ¿en qué forma castiga ud. A sus hijas mujeres? ¿privándolos de alimentación? |
| `vs08_0840_AF` | ¿en qué forma castiga ud. A sus hijas mujeres? ¿dejándolos encerrados? |
| `vs08_0840_AG` | ¿en qué forma castiga ud. A sus hijas mujeres? ¿poniéndoles más trabajo? |
| `vs08_0840_AH` | ¿en qué forma castiga ud. A sus hijas mujeres? ¿dejándolos fuera de casa? |
| `vs08_0840_AI` | ¿en qué forma castiga ud. A sus hijas mujeres? ¿echándoles agua? |
| `vs08_0840_AJ` | ¿en qué forma castiga ud. A sus hijas mujeres? ¿quitándoles la ropa? |
| `vs08_0840_AK` | ¿en qué forma castiga ud. A sus hijas mujeres? ¿ignorándolos más de un dia? |
| `vs08_0840_AL` | ¿en qué forma castiga ud. A sus hijas mujeres? ¿quitandoles recreos y mesadas? |
| `vs08_0840_AM` | ¿en qué forma castiga ud. A sus hijas mujeres? ¿prohibiendo algo que le gusta? |
| `vs08_0840_AN` | ¿en qué forma castiga ud. A sus hijos varones? ¿prohibiendo el uso o decomisando algo que les gusta? |
| `vs08_0840_AO` | ¿en qué forma castiga ud. A sus hijas mujeres? ¿sacudón /zamarrear? |
| `vs08_0840_AX` | ¿en qué forma castiga ud. A sus hijas mujeres? ¿otra? (especifique) |
| `vs08_0840_AX_cod` | ¿en qué forma castiga ud. A sus hijas mujeres? ¿otra? (especifique) codificado |
| `vs08_0840_BA` | Hijas mujeres:¿en qué forma castiga su esposa/compañera a sus hijas mujeres? ¿jalón de orejas/ palmadas/ sopapos? |
| `vs08_0840_BB` | ¿en qué forma castiga su esposa/compañera a sus hijas mujeres? ¿golpes con: chicote, chinelas, cinturón, quimsa charani? |
| `vs08_0840_BC` | ¿en qué forma castiga su esposa/compañera a sus hijas mujeres? ¿gritos? |
| `vs08_0840_BD` | ¿en qué forma castiga su esposa/compañera a sus hijas mujeres? ¿insultos? |
| `vs08_0840_BE` | ¿en qué forma castiga su esposa/compañera a sus hijas mujeres? ¿privándolos de alimentación? |
| `vs08_0840_BF` | ¿en qué forma castiga su esposa/compañera a sus hijas mujeres? ¿dejándolos encerrados? |
| `vs08_0840_BG` | ¿en qué forma castiga su esposa/compañera a sus hijas mujeres? ¿poniéndoles más trabajo? |
| `vs08_0840_BH` | ¿en qué forma castiga su esposa/compañera a sus hijas mujeres? ¿dejándolos fuera de casa? |
| `vs08_0840_BI` | ¿en qué forma castiga su esposa/compañera a sus hijas mujeres? ¿echándoles agua? |
| `vs08_0840_BJ` | ¿en qué forma castiga su esposa/compañera a sus hijas mujeres? ¿quitándoles la ropa? |
| `vs08_0840_BK` | ¿en qué forma castiga su esposa/compañera a sus hijas mujeres? ¿ignorándoles más de un dia? |
| `vs08_0840_BL` | ¿en qué forma castiga su esposa/compañera a sus hijas mujeres? ¿quitándoles recreos y mesadas? |
| `vs08_0840_BM` | ¿en qué forma castiga su esposa/compañera a sus hijas mujeres? ¿prohibiendo algo que le gusta? |
| `vs08_0840_BN` | ¿en qué forma castiga ud. A sus hijos varones? ¿prohibiendo el uso o decomisando algo que les gusta? |
| `vs08_0840_BO` | ¿en qué forma castiga su esposa/compañera a sus hijas mujeres? ¿sacudón /zamarrear? |
| `vs08_0840_BX` | ¿en qué forma castiga su esposa/compañera a sus hijas mujeres? ¿otra? (especifique) |
| `vs08_0840_BX_cod` | ¿en qué forma castiga su esposa/compañera a sus hijas mujeres? ¿otra? (especifique) codificado |
| `vs08_0840_CA` | Hijas mujeres:¿en qué forma castiga esa persona a sus hijas mujeres? ¿jalón de orejas/ palmadas/ sopapos? |
| `vs08_0840_CB` | ¿en qué forma castiga esa persona a sus hijas mujeres? ¿golpes con: chicote, chinelas, cinturón, quimsa charani? |
| `vs08_0840_CC` | ¿en qué forma castiga esa persona a sus hijas mujeres? ¿gritos? |
| `vs08_0840_CD` | ¿en qué forma castiga esa persona a sus hijas mujeres? ¿insultos? |
| `vs08_0840_CE` | ¿en qué forma castiga esa persona a sus hijas mujeres? ¿privándolos de alimentación? |
| `vs08_0840_CF` | ¿en qué forma castiga esa persona a sus hijas mujeres? ¿dejándolos encerrados? |
| `vs08_0840_CG` | ¿en qué forma castiga esa persona a sus hijas mujeres? ¿poniéndoles más trabajo? |
| `vs08_0840_CH` | ¿en qué forma castiga esa persona a sus hijas mujeres? ¿dejándolos fuera de casa? |
| `vs08_0840_CI` | ¿en qué forma castiga esa persona a sus hijas mujeres? ¿echándoles agua? |
| `vs08_0840_CJ` | ¿en qué forma castiga esa persona a sus hijas mujeres? ¿quitándoles la ropa? |
| `vs08_0840_CK` | ¿en qué forma castiga esa persona a sus hijas mujeres? ¿ignorándoles más de un dia? |
| `vs08_0840_CL` | ¿en qué forma castiga esa persona a sus hijas mujeres? ¿quitándoles recreos y mesadas? |
| `vs08_0840_CM` | ¿en qué forma castiga esa persona a sus hijas mujeres? ¿prohibiendo algo que le gusta? |
| `vs08_0840_CN` | ¿en qué forma castiga ud. A sus hijos varones? ¿prohibiendo el uso o decomisando algo que les gusta? |
| `vs08_0840_CO` | ¿en qué forma castiga esa persona a sus hijas mujeres? ¿sacudón /zamarrear? |
| `vs08_0840_CX` | ¿en qué forma castiga esa persona a sus hijas mujeres? ¿otra? (especifique) |
| `vs08_0840_CX_cod` | (ESPECIFIQUE OTRA) (C) En qué forma castiga esa persona a sus hijas mujeres? |
| `vs08_0841_A` | Generalmente, ¿en qué forma lo castigan o castigaban a ud. Sus padres o personas con las que creció? ¿jalón de orejas/ palmadas/ sopapos? |
| `vs08_0841_B` | Generalmente, ¿en qué forma lo castigan o castigaban a ud. Sus padres o personas con las que creció? ¿golpes con: chicote, chinelas, cinturón, quimsa charani? |
| `vs08_0841_C` | Generalmente, ¿en qué forma lo castigan o castigaban a ud. Sus padres o personas con las que creció? ¿gritos? |
| `vs08_0841_D` | Generalmente, ¿en qué forma lo castigan o castigaban a ud. Sus padres o personas con las que creció? ¿insultos? |
| `vs08_0841_E` | Generalmente, ¿en qué forma lo castigan o castigaban a ud. Sus padres o personas con las que creció? ¿privándolo de alimentación? |
| `vs08_0841_F` | Generalmente, ¿en qué forma lo castigan o castigaban a ud. Sus padres o personas con las que creció? ¿dejándolo encerrado? |
| `vs08_0841_G` | Generalmente, ¿en qué forma lo castigan o castigaban a ud. Sus padres o personas con las que creció? ¿poniéndole más trabajo? |
| `vs08_0841_H` | Generalmente, ¿en qué forma lo castigan o castigaban a ud. Sus padres o personas con las que creció? ¿dejándolo fuera de casa? |
| `vs08_0841_I` | Generalmente, ¿en qué forma lo castigan o castigaban a ud. Sus padres o personas con las que creció?¿echándole agua? |
| `vs08_0841_J` | Generalmente, ¿en qué forma lo castigan o castigaban a ud. Sus padres o personas con las que creció? ¿quitándole la ropa? |
| `vs08_0841_K` | Generalmente, ¿en qué forma lo castigan o castigaban a ud. Sus padres o personas con las que creció? ¿ignorándolo más de un dia? |
| `vs08_0841_L` | Generalmente, ¿en qué forma lo castigan o castigaban a ud. Sus padres o personas con las que creció? ¿quitándole recreo y mesada? |
| `vs08_0841_M` | Generalmente, ¿en qué forma lo castigan o castigaban a ud. Sus padres o personas con las que creció? ¿prohibiendole algo que le gusta? |
| `vs08_0841_N` | ¿en qué forma castiga ud. A sus hijos varones? ¿prohibiendo el uso o decomisando algo que les gusta? |
| `vs08_0841_X` | Generalmente, ¿en qué forma lo castigan o castigaban a ud. Sus padres o personas con las que creció? ¿sacudones? |
| `vs08_0841_Y` | Generalmente, ¿en qué forma lo castigan o castigaban a ud. Sus padres o personas con las que creció? ¿otra? (especifique) |
| `vs08_0841_X_cod` | (ESPECIFIQUE OTRA) ¿en qué forma la castigan o castigaban a Ud. sus padres o personas con las que creció? |
| `vs08_0842_01` | ¿cree ud. Que para educar a las/os hijas/os es necesario algún castigo? A MENUDO |
| `vs08_0842_02` | ¿cree ud. Que para educar a las/os hijas/os es necesario algún castigo? ALGUNAS VECES |
| `vs08_0843_A` | En su opinión se justifica que el padre o la madre castigue (agreda) a sus hijas/os: ¿cuando son desobedientes? |
| `vs08_0843_B` | En su opinión se justifica que el padre o la madre castigue (agreda) a sus hijas/os: ¿cuando hacen renegar? |
| `vs08_0843_C` | En su opinión se justifica que el padre o la madre castigue (agreda) a sus hijas/os: ¿cuando llegan tarde a la casa? |
| `vs08_0843_D` | En su opinión se justifica que el padre o la madre castigue (agreda) a sus hijas/os: ¿cuando no cumplen con las tareas familiares? |
| `vs08_0843_E` | En su opinión se justifica que el padre o la madre castigue (agreda) a sus hijas/os: ¿cuando lloran mucho? |
| `vs08_0843_F` | En su opinión se justifica que el padre o la madre castigue (agreda) a sus hijas/os: ¿cuando embarazan a una niña/adolescente? |
| `vs08_0844` | Verifique 208 (si tiene uno o mas hijas/os): ¿usted tiene hijas/os menores a 18 años? |
| `vs08_0845_A` | ¿cuál de los siguientes actos considera usted como violencia contra una/un niña/ niño adolescente? ¿toqueteo sin consentimiento? |
| `vs08_0845_B` | ¿cuál de los siguientes actos considera usted como violencia contra una/un niña/ niño adolescente? ¿convencerle o persuadirle de tener relaciones sexuales? |
| `vs08_0845_C` | ¿cuál de los siguientes actos considera usted como violencia contra una/un niña/ niño adolescente? ¿realizar otras actividades sexuales? |
| `vs08_0845_D` | ¿cuál de los siguientes actos considera usted como violencia contra una/un niña/ niño adolescente? ¿presionarle a traves de amenazas a tener relaciones sexuales? |
| `vs08_0845_E` | ¿cuál de los siguientes actos considera usted como violencia contra una/un niña/ niño adolescente? ¿tener relaciones sexuales sin consentimiento? |
| `vs08_0846` | ¿Alguna de sus hijas o alguno de sus hijos ha vivido alguna de estas situaciones? |
| `vs08_0847_A` | Segun usted quien sufre mas violencia Niñas/niños |
| `vs08_0847_B` | Segun usted quien sufre mas violencia: Adolescentes |
| `vs08_0847_C` | Segun usted quien sufre mas violencia: Jovenes |
| `vs08_0847_D` | Segun usted quien sufre mas violencia: Mujeres |
| `vs08_0847_E` | Segun usted quien sufre mas violencia: Hombres |
| `vs08_0847_F` | Segun usted quien sufre mas violencia: Personas adultas mayores |
| `vs08_0847_G` | Segun usted quien sufre mas violencia: Poblaciones GLBTIQ |
| `vs08_0847_H` | Segun usted quien sufre mas violencia: Poblaciones Personas con discapacidad |
| `vs08_0848_A` | Si usted supiera que en su familia hay alguna persona que esta sufriendo violencia¿Cómo piensa que se debería afrontar este problema? (AYUDA SOLA) |
| `vs08_0848_B` | VERIFICAR 101A de 18 a 29 años o mayoro oigual a 39 años |
| `vs08_0848_C` | Si usted supiera que en su familia hay alguna persona que esta sufriendo violencia¿Cómo piensa que se debería afrontar este problema? (APOYO SERVICIOS) |
| `vs08_0848_D` | Si usted supiera que en su familia hay alguna persona que esta sufriendo violencia¿Cómo piensa que se debería afrontar este problema? (APOYO PERSONAL SALUD) |
| `vs08_0848_E` | Si usted supiera que en su familia hay alguna persona que esta sufriendo violencia¿Cómo piensa que se debería afrontar este problema? (APOYO ONGs/ORG.SOC) |
| `vs08_0848_X` | Si usted supiera que en su familia hay alguna persona que esta sufriendo violencia¿Cómo piensa que se debería afrontar este problema? (OTRO) |
| `vs08_0848_Z` | Si usted supiera que en su familia hay alguna persona que esta sufriendo violencia¿Cómo piensa que se debería afrontar este problema? (NO SABE/NO RESPONDE) |
| `vs08_0848_X_cod` | (ESPECIFÍQUE OTRO) ¿Cómo piensa que se debería afrontar este problema? |
| `vs08_0848b` | ¿Por favor dígame si alguna vez ha sido forzado por alguna persona (pareja o diferente a su pareja) a tener relaciones sexuales antes de cumplir los 18 años? |
| `vs08_0849` | ¿Alguna vez alguien le habló sobre la prevención de la violencia en el sistema de salud? |
| `vs08_0850` | Durante el periodo de cuarentena total (encierro)¿ha sufrido violencia física, psicológica o sexual? |
| `vs08_0851` | ¿Conoce alguna ley que protege los derechos de las personas que sufren violencia? |
| `vs08_0852_A` | ¿entrevistador tuvo que interrumpir la entrevista debido a la presencia de otra persona que trataba de escuchar, o entro en el cuarto, o interrumpio en alguna otra forma? |
| `vs08_0852_B` | ¿entrevistador tuvo que interrumpir la entrevista debido a la presencia de otra persona que trataba de escuchar, o entro en el cuarto, o interrumpio en alguna otra forma? |
| `vs08_0852_C` | ¿entrevistador tuvo que interrumpir la entrevista debido a la presencia de otra persona que trataba de escuchar, o entro en el cuarto, o interrumpio en alguna otra forma? |
| `vs08_0854_a` | Hora de finalización de la entrevista a: [nombre] |
| `vs08_0854_b` | Minutos de finalización de la entrevista a: [nombre] |
| `ponderadorh` | Ponderador para hombres |
| `area` | Área |
| `region` | Región |
| `departamento` | Departamento |
| `idiomaninez` | Idioma que aprendio en la niñez |
| `niv_ed` | Nivel educativo detallado |
| `niv_ed_g` | Nivel educativo general |
| `aestudio` | Años de estudio |
| `cono_algmet` | Conocimiento de metodos anticonceptivos (Cualquier método) |
| `cono_metmod` | Conocimiento de metodos anticonceptivos (Métodos modernos) |
| `cono_mettra` | Conocimiento de metodos anticonceptivos (Métodos tradicionales) |
| `actuni_h` | Actualmente unido |
| `sexact_h` | Sexualmente activo |
| `condact_h` | Condición de actividad |
| `econyugd_h` | Estado civil o conyugal |
| `cob_h` | Grupo ocupacional |
| `deseo_h` | Deseo/Preferencia de Fecundidad |
| `deseog_h` | Deseo/Preferencia de Fecundidad agrupado |

---
