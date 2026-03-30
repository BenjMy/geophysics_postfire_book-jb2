---
title: "Course Exercises"
---


# Course Exercises

```{admonition} Golden rule
:class: important
Always **attempt the exercise yourself** before looking at the solution. Struggling with a problem is where learning happens!
```

---

## Structure

Each week's exercise folder contains:

- **Main exercise notebook** — problems with guidance and hints
- **`solutions/` sub-folder** — reference implementations to review after your attempt

```
exercises/
├── week1_python_fundamentals/
│   ├── exercise.ipynb
│   └── solutions/
│       └── solution.ipynb
├── week2_resipy/
│   ├── exercise.ipynb
│   └── solutions/
│       └── solution.ipynb
├── week3_emagpy/
│   ├── exercise.ipynb
│   └── solutions/
│       └── solution.ipynb
└── week4_case_study/
    ├── exercise.ipynb
    └── solutions/
        └── solution.ipynb
```

---

## Weekly Topics

::::{grid} 1 1 2 2
:gutter: 3

:::{grid-item-card} 📘 Week 1 · Python Fundamentals
:class-header: bg-light
Practice variables, lists, loops, and functions using geophysics-themed examples.

**Key skills:** NumPy arrays · Matplotlib plotting · Pandas DataFrames
:::

:::{grid-item-card} 📗 Week 2 · resipy Basics
:class-header: bg-light
Load a real resistivity dataset, visualise the pseudosection, and run your first inversion.

**Key skills:** `Project()` · `createSurvey()` · `invert()` · pseudosection plot
:::

:::{grid-item-card} 📙 Week 3 · emagpy Introduction
:class-header: bg-light
Import EMI data, apply calibration, and perform a 1-D lateral inversion.

**Key skills:** `Problem()` · `importData()` · `invertGN()` · profile maps
:::

:::{grid-item-card} 📕 Week 4 · Integrated Case Study
:class-header: bg-light
Combine resistivity and EM data to map subsurface features in a realistic scenario.

**Key skills:** Multi-method integration · interpretation · report figures
:::

::::

---

## Guidelines

```{list-table}
:header-rows: 1
:widths: 10 90

* - #
  - Guideline
* - 1
  - Attempt exercises **before** viewing solutions
* - 2
  - Experiment — change parameters and observe what happens
* - 3
  - Compare your approach with the provided solution; both can be correct!
* - 4
  - Ask questions in the course discussion if you are stuck for more than 20 minutes
```

---

```{tip}
Use the **Jupyter Lab** split-screen view (`Ctrl + Shift + D`) to keep the exercise and solution side by side when reviewing.
```
