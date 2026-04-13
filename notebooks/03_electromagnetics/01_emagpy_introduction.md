---
title: "Processing with EMagPy"
kernelspec:
  name: python3
  display_name: Python 3 (Geophysics)
  language: python
---

# Introduction to EMagPy

```{contents} Table of Contents
:depth: 3
:local:
:backlinks: none
```

---

## Overview

**EMagPy** is a Python package for processing and inverting {term}`EMI` data. It provides
both a **standalone graphical user interface (GUI)** and a **Python API** designed
for use in Jupyter notebooks. The main class is `Problem`.

```{admonition} Learning Objectives
:class: note

By the end of this notebook you will be able to:

- Install EMagPy and import the `Problem` class
- Load field data and inspect the CSV format
- Visualise ECa profiles and maps
- Define a starting model and run a 1D inversion
- Visualise inverted conductivity depth profiles and slices
```

> **Citation:** McLachlan P., Blanchy G. and Binley A. 2021.
> *EMagPy: Open-source, platform-independent processing and inversion of electromagnetic induction data.*
> Computers & Geosciences, 146, 104561. <https://doi.org/10.1016/j.cageo.2020.104561>

---

## Installation

EMagPy can be installed in three ways depending on your needs.

#### Option A — Standalone executable (no Python required, recommended for this course)

1. Go to the [EMagPy releases page](https://gitlab.com/hkex/emagpy/-/releases) on GitLab.
2. Download the latest **`EMagPy_x.x.x_windows.zip`**.
3. Extract the zip and double-click **`EMagPy.exe`** to launch the GUI.

```{admonition} Windows SmartScreen warning
:class: warning
If you see *"Windows protected your PC"*, click **More info** → **Run anyway**.
The executable is not commercially signed but is safe to use.
```

#### Option B — pip (recommended for scripting and Jupyter)

```bash
pip install emagpy
```

---

## Complete minimal workflow

+++

### 1 Imports

```{code-cell} python
import os
import numpy as np
import pandas as pd
from emagpy import Problem  # main class
testdir = '../../assets/complementary_data/cover-crop/'
```

+++

### 2 Load data and inspect format

EMagPy imports data from a `.csv` file where **column headers are the coil
configurations** (e.g. `VCP0.71`, `HCP1.48`). Each row is one measurement
location.

```{code-cell} python
k = Problem()                              # create the main object
k.createSurvey(testdir + 'coverCrop.csv') # import the data
```

```{code-cell} python
df = pd.read_csv(testdir + 'coverCrop.csv')
df.head()  # inspect the header format
```

+++

### 3 Data visualisation

`Problem.show()` plots ECa as a line graph per coil configuration.
If spatial coordinates (`x`, `y`) are present, `Problem.showMap()` produces a
plan-view {term}`apparent electrical conductivity` map.

```{code-cell} python
k.show(vmax=50)
```

```{code-cell} python
k.showMap(coil='VCP0.71', contour=True, pts=True)
```

+++

### 4 Starting model

Before inversion, define a layered starting model: the **bottom depth of each
layer** and an initial {term}`electrical conductivity` value for each layer
(including the half-space below).

```{code-cell} python
k.setInit(
    depths0=[0.5, 1],           # bottom of each layer (m) — last layer is infinite
    conds0=[20, 20, 20],        # starting conductivity (mS/m) per layer
    fixedConds=[False, False, False]
)
```

+++

### 5 Forward models and solvers

Several forward models are available, trading accuracy for speed:

| Model | Description |
|---|---|
| `CS` | Cumulative Sensitivity (McNeill 1980) — default, fastest |
| `CSgn` | CS with Gauss-Newton solver — uses `invertGN()` automatically |
| `FSlin` | Full Solution (Maxwell) with {term}`low induction number (LIN)` approximation |
| `FSeq` | Full Solution without LIN — apparent ECa via optimisation (Andrade et al. 2016) |
| `Q` | Full Solution minimising quadrature directly — preferred for ECa > 100 mS/m |

Two families of solvers are available:

- **Gradient-based** (`L-BFGS-B`, `TNC`, `CG`, `Nelder-Mead`) via `scipy.optimize.minimize()`
- **MCMC-based** (`ROPE`, `SCEUA`, `DREAM`) via `spotpy` — suited when layer depths are free parameters

+++

### 6 Inversion

```{code-cell} python
k.invert()       # default: CS forward model, L-BFGS-B solver
k.showResults()  # inverted conductivity depth section
k.showMisfit()   # data misfit per coil
k.showOne2one()  # observed vs predicted ECa
```

+++

### 7 Depth slices

If spatial coordinates are available, `showSlice()` produces plan-view maps
of conductivity at a given layer index.

```{code-cell} python
k.showSlice(islice=0, contour=True, vmin=12, vmax=50)  # top layer
k.showSlice(islice=2, contour=True, vmin=12, vmax=50)  # bottom layer
```

Access the method docstring for all available options:

```{code-cell} python
:tags: [hide-output]
help(k.showSlice)
```

---

## Summary

```{admonition} What you have learned
:class: tip

| Step | Method | Purpose |
|------|--------|---------|
| 1 | `Problem()` | Create the main object |
| 2 | `createSurvey(file)` | Load field data |
| 3 | `show()` / `showMap()` | Visualise ECa data |
| 4 | `setInit(depths0, conds0)` | Define starting model |
| 5 | `invert()` | Run 1D inversion |
| 6 | `showResults()` / `showMisfit()` / `showOne2one()` | Assess inversion quality |
| 7 | `showSlice()` | Plan-view conductivity maps |

**Next notebook:** [ERT Processing with ResIPy](nb_resipy.md) — process **electrical resistivity tomography** data with ResIPy.
```

---

## Additional Resources

- [EMagPy official documentation](https://hkex.gitlab.io/emagpy/)
- [EMagPy GitLab repository](https://gitlab.com/hkex/emagpy)
- [EMagPy on PyPI](https://pypi.org/project/emagpy/)
