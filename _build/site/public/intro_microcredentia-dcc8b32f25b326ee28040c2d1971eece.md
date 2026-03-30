# Inteligencia Artificial y Tecnologías Geoespaciales Aplicadas a la Restauración de Ecosistemas Forestales Afectados por Incendios y Sequías Extremas
## Aquisition and integration of geophysical data


Agenda - Bloque 2 7h

05/05/2026	Martes	16:00 - 18:30	Integración de datos geofísicos: teoría
06/05/2026	Miércoles	16:00 - 18:30	Caso práctico: humedad del suelo a escala de cuenca
07/05/2026	Jueves	16:00 - 18:00	Caso práctico: diques de sedimentación
08/05/2026	Viernes	Trabajo alumnos bloque 1: Trabajo 3: manejo de datos geofísicos con softwares abierto (10h)

Add GRWATER web



Add contact emails



micro_UCLM_flyer.jpeg (located in assets/images/)




---->>> remove what's next



```{admonition} Welcome!
:class: tip
This course teaches geophysical data analysis using two powerful Python packages — **resipy** for electrical resistivity imaging, and **emagpy** for electromagnetic induction data processing.
```

::::{grid} 1 1 2 3
:class-container: text-center
:gutter: 3

:::{grid-item-card}
:link: docs/getting_started
:link-type: doc
:class-header: bg-light

🚀 **Getting Started**
^^^
New to the course? Begin here for setup instructions and an overview of what you'll learn.
:::

:::{grid-item-card}
:link: notebooks/01_introduction/01_python_basics
:link-type: doc
:class-header: bg-light

🐍 **Python Basics**
^^^
Brush up on Python fundamentals with geophysics-focused examples and exercises.
:::

:::{grid-item-card}
:link: exercises/README
:link-type: doc
:class-header: bg-light

🧪 **Exercises**
^^^
Practice problems and solutions for each bloc of the course.
:::

::::

---

## 📖 Course Overview

This course covers the full pipeline of geophysical data analysis in Python:

```{list-table}
:header-rows: 1
:widths: 10 25 65

* - Day
  - Topic
  - Content
* - 1
  - **Python Fundamentals**
  - Variables, data types, control structures, functions, NumPy & Matplotlib
* - 2
  - **resipy · Resistivity**
  - Project setup, data import, pseudosection visualisation, ERT inversion
* - 3
  - **emagpy · Electromagnetics**
  - EMI data processing, forward modelling, lateral & depth inversion
* - 4
  - **Integrated Case Study**
  - Archaeological survey and groundwater investigation workflows
```

---

## 🎯 Learning Outcomes

By the end of this course you will be able to:

- Process and analyse geophysical data using Python
- Perform 2-D and 3-D resistivity inversions with **resipy**
- Process electromagnetic induction data with **emagpy**
- Create publication-quality visualisations
- Apply techniques to real-world geophysical scenarios


## 📂 Repository Structure

```
geophysics-python-course/
├── docs/               ← Documentation & guides
├── exercises/          ← Practice problems
├── notebooks/
│   ├── 01_introduction/   ← Python & geophysics basics
│   ├── 02_resipy/         ← Resistivity notebooks
│   └── 03_emagpy/         ← Electromagnetics notebooks
├── data/               ← Sample datasets
└── src/                ← Reusable utility functions
```

---

```{admonition} How to use this book
:class: note
Work through the chapters in order. Each notebook builds on the previous one.
Always **attempt exercises yourself** before looking at the solutions!
```

---

*Licensed under the [MIT License](https://opensource.org/licenses/MIT). Contributions welcome — see [CONTRIBUTING.md](https://github.com/BenjMy/geophysics-python-course/blob/main/CONTRIBUTING.md).*
