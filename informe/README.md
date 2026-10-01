# Informe Académico del Proyecto (`informe/`)

Este directorio contiene el informe formal del proyecto desarrollado para la materia **Machine Learning (DAT-255)** de la **Carrera de Informática** en la **Universidad Mayor de San Andrés (UMSA)**.

---

## 1. Estructura de Archivos

```text
informe/
├── informeAPA7.tex            -> Documento maestro principal en LaTeX
├── main.tex                   -> Punto de entrada estándar alternativo
├── referencias.bib            -> Base de datos bibliográfica BibTeX
├── imagenes/                  -> Directorio de recursos gráficos
│   ├── logo_umsa.png          -> Escudo oficial de la UMSA (alta resolución)
│   ├── arbol_problemas.png    -> Diagrama oficial del Árbol de Problemas
│   └── arbol_objetivos.png    -> Diagrama oficial del Árbol de Objetivos
└── secciones/                 -> Estructura modular del documento
    ├── 01_introduccion.tex    -> 1. Introducción
    ├── 02_antecedentes.tex    -> 2. Antecedentes (EAIMCS, normativa, estado del arte)
    ├── 03_problematica.tex    -> 3. Problemática (incluye 3.a Árbol de Problemas con diagrama)
    ├── 04_objetivos.tex       -> 4. Objetivos (incluye 4.a Árbol de Objetivos con diagrama)
    ├── 05_justificacion.tex   -> 5. Justificación (técnica, socioeconómica, metodológica)
    ├── 06_metodologia.tex     -> 6. Metodología, Desarrollo y Validación (benchmark calibrado)
    ├── 07_herramientas.tex    -> 7. Herramientas y Técnicas (Python, Flask, Plotly, Data Drift)
    ├── 08_conclusiones.tex    -> 8. Conclusiones y recomendaciones
    └── anexos.tex             -> Anexos A, B y C (ficha técnica, marco lógico, diccionario)
```

---

## 2. Instrucciones de Compilación

### Compilación en Overleaf
1. Subir la carpeta completa `informe/` a un nuevo proyecto en **Overleaf**.
2. Asegurarse de que el compilador esté configurado en **pdfLaTeX**.
3. Definir `informeAPA7.tex` o `main.tex` como archivo principal (*Main document*).
4. Presionar **Recompile**.

### Compilación Local (Línea de Comandos)
```bash
cd informe
pdflatex informeAPA7.tex
bibtex informeAPA7
pdflatex informeAPA7.tex
pdflatex informeAPA7.tex
```

---

## 3. Características Especiales
- **Carátula Oficial:** Formateada según los requerimientos exactos de la Carrera de Informática de la UMSA (DAT-255).
- **Fallback de Logo Universitario:** Si el archivo `imagenes/logo_umsa.png` no está presente, el documento renderiza automáticamente un sello vectorial TikZ representativo, garantizando una compilación limpia sin errores de archivos faltantes.
- **Diagramas TikZ Nativos:** Los árboles de problemas y de objetivos están dibujados vectorialmente con `tikz`, garantizando máxima resolución y nitidez tipográfica en el PDF generado.
