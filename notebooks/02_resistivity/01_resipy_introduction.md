---
title: "Processing with ResIPy"
kernelspec:
  name: python3
  display_name: Python 3 (Geophysics)
  language: python
---

# Introduction to ResIPy

```{contents} Table of Contents
:depth: 3
:local:
:backlinks: none
```

---

## Overview

**ResIPy** (also called *resipy*) is a Python wrapper around the robust **R2 / cR2 / R3t / cR3t** inversion codes for 2-D and 3-D electrical resistivity tomography (ERT) and induced polarisation (IP). It provides both a **standalone graphical user interface (GUI)** and a **Python API** designed for use in Jupyter notebooks.

```{admonition} Learning Objectives
:class: note

By the end of this notebook you will be able to:

- Install ResIPy correctly on **Windows**, Linux and macOS
- Create and configure a `Project` object
- Import field data and visualise a **pseudosection**
- Filter noisy or bad measurements
- Fit an **error model** to your data
- Build a **mesh** and run a regularised inversion
- Visualise and interpret the inverted resistivity section
```

> **Citation:** Blanchy G., Saneiyan S., Boyd J., McLachlan P. and Binley A. 2020.
> *ResIPy, an Intuitive Open Source Software for Complex Geoelectrical Inversion/Modeling.*
> Computers & Geosciences, 104423. <https://doi.org/10.1016/j.cageo.2020.104423>

---

## Installation

ResIPy can be installed in three ways depending on your operating system and needs.
**Windows users have the simplest experience** — the inversion binaries are native Windows
executables and no extra software is required.

---

#### Option A — Standalone executable (no Python required, recommended for this course)

This is the quickest way to try ResIPy without installing anything else.

1. Go to the [ResIPy releases page](https://gitlab.com/hkex/resipy/-/releases) on GitLab.
2. Download the latest **`ResIPy_x.x.x_windows.zip`**.
3. Extract the zip to a folder of your choice (e.g. `C:\ResIPy`).
4. Double-click **`ResIPy.exe`** to launch the GUI.

```{admonition} Windows SmartScreen warning
:class: warning
If you see *"Windows protected your PC"*, click **More info** → **Run anyway**.
This appears because the executable is not signed with a commercial certificate — it is
safe to proceed. You may also need to add an exception in your antivirus program.
```

#### Option B — Python API via pip 

You need **Python 3.9 or higher**. If you do not have Python, first install
[Miniconda for Windows](https://docs.conda.io/en/latest/miniconda.html) — a lightweight
Python distribution that also provides the `conda` package manager. During installation,
check **"Add Miniconda to my PATH"** if prompted.

Once Miniconda is installed, open **Anaconda Prompt** (search for it in the Start menu)
and run the following commands **one by one**:

```bat

:: Step 1 — Create a dedicated environment (keeps this course isolated)
conda create -n geophysics-course python=3.10

:: Step 2 — Activate the environment
conda activate geophysics-course

:: Step 3 — Install the core scientific stack via conda
conda install numpy scipy matplotlib pandas jupyter jupyterlab ipykernel ipywidgets

:: Step 4 — Install ResIPy from PyPI
pip install resipy

:: Step 5 — Verify the installation
python -c "from resipy import Project; print('ResIPy OK')"
```

```{admonition} Good news for Windows users
:class: tip
On **Windows**, ResIPy ships with the inversion binaries (`R2.exe`, `cR2.exe`, `R3t.exe`,
`cR3t.exe`) built natively for Windows. **No Wine or extra software is needed.**
You can run full inversions straight away after `pip install resipy`.
```

On **Linux / macOS** you may additionally see:

```
Warning: Wine is not installed!
```

This is expected if Wine is not yet configured. See Section 8 (Troubleshooting) to resolve it.

---

## Complete minimal workflow

# R2 basic tutorial


In this tutorial you will learn how to use the Python API of R* codes (http://www.es.lancs.ac.uk/people/amb/Freeware/R2/R2.htm).
Start by importing the `Project` master class from the API (Application Programming Interface).

+++

### 1 Basics imports

Just import basic packages and the R2 API as a module (note : you will need to change the path for it, here we assume you launched the jupyter from inside the /examples/jupyter-notebook folder).

```{code-cell} python
%matplotlib inline
import warnings
warnings.filterwarnings('ignore')
import os
testdir = '../../assets/complementary_data/dc-2d/'
from resipy import Project
```

+++

### 2 Create an 'Project' object, import data and plot pseudo section

> The `Project` class was referred to as `R2` class in older version of ResIPy.

The first step is to create an object out of the `Project` class, let's call it ```k``` . This is the main object we are going to interact with. Then the second step is to read the data from a survey file. Here we choose a csv file from the Syscal Pro that contains resistivity data only. Note then when importing the survey data, the object automatically search for reciprocal measurements and will compute a reciprocal error with the ones it finds.

```{code-cell} python
k = Project(typ='R2') # create a Project object in a working directory (can also set using k.setwd())
k.createSurvey(testdir + 'syscal.csv', ftype='Syscal') # read the survey file
```

We can plot the pseudosection and display errors based on reciprocal measurements.

```{code-cell} python
k.showPseudo()
k.showError() # plot the reciprocal errors
```

+++

### 3 Data filtering

Below are a few examples of data filtering routines that can be used:
- `k.filterUnpaired()` to remove unpaired measurements (so measurements with no reciprocal) -> those could be dummy measurements in a dipole-dipole configuration
- `k.filterElec([5])` to remove a specific electrode (e.g. here all quadrupoles with electrode 5 are deleted)
- `k.filterRecip(20)` to remove measurements based on their relative reciprocal error (e.g. all quadrupoles with a reciprocal error > 20% are discarded).
More advanced data filtering can be achieved using the `filterData()` method from the `Survey` class. This method allows to filter out specific quadrupoles. An interactive version of it can be access using the `filterManual()` method which produces an interactive pseudo-section in the UI.

```{code-cell} python
k.filterUnpaired()
k.showPseudo() # this actually removed the dummy measurements in this dipole-dipole survey (added for speed optimization)
```

```{code-cell} python
k.filterElec([5]) # remove all quadrupoles associated with electrode 5
k.showPseudo()
```

```{code-cell} python
k.filterRecip(percent=20) # in this case this only removes one quadrupoles with reciprocal error bigger than 20 percent
k.showPseudo()
```

+++

### 4 Fitting an error model

Different errors models are available to be fitted for DC data:
- a simple linear model: `k.fitErrorLin()`
- a power law model: `k.fitErrorPwl()`
- a linear mixed effect model: `k.fitErrorLME()` (on Linux only with an R kernel installed)
Each of those will create a new error column in the `Survey` object that will be used in the inversion if `k.err = True`.


```{code-cell} python
k.fitErrorLin()
```

```{code-cell} python
k.fitErrorPwl()
```

+++

### 5 Mesh

Two types of mesh can be created in 2D:
- a quadrilateral mesh (`k.createMesh('quad')`)
- a triangular mesh (`k.createmesh('trian')`)
For 3D, only tetrahedral mesh can be created using `k.createMesh('tetra')`.

```{code-cell} python
k.createMesh(typ='quad') # generate quadrilateral mesh (default for 2D survey)
k.showMesh()
```

```{code-cell} python
k.createMesh('trian', show_output=False) # this actually call gmsh.exe to create the mesh
k.showMesh()
```

+++

### 7 Inversion

The inversion takes place in the specify working directory of the R2 object specified the first time the `k = R2(<workingDirectory>)` is called. It can be changed after by using `k.setwd(<newWorkingDirectory>)`.
The parameters of the inversion are defined in a dictionnary in `k.param` and ca be changed manually by the user (e.g. `k.param['a_wgt'] = 0.01`. All parameters have a default values and their names follow the R2 manual. The `.in` file is written automatically when the `k.invert()` method is called.

```{code-cell} python
k.param['data_type'] = 1 # using log of resistitivy
k.err = True # if we want to use the error from the error models fitted before
k.invert() # this will do the inversion
```

+++

### 8 Results visualisation and post-processing

Results can be show with `k.showResults()`. Multiple arguments can be passed to the method in order rescale the colorbar bar, view the sensitivity or not, change the attribute or plot contour. The errors from the inversion can also be plotted using either `k.pseudoError()` or `k.showInvError()`.

```{code-cell} python
k.showResults(attr='Resistivity(ohm.m)', sens=False, contour=True, vmin=30, vmax=100)
```

```{code-cell} python
k.showPseudoInvError() # allow to see if some electrodes get higher error
```

```{code-cell} python
k.showInvError() # all errors should be between -3 and 3
```


---

##  Video Tutorials

The ResIPy team maintains an official YouTube channel with step-by-step tutorials.

:::{iframe} https://www.youtube.com/embed/wfJ62rz0EsU?si=K32bWdkjYoZWRdRN
:width: 60%
ResIPy Python API — Getting Started
:::

:::{iframe} https://www.youtube.com/embed/48VN_e8J2kc?si=vH4NVe1OHKQsGf0P
:width: 60%
Introduction to 2-D forward modelling with ResIPy
:::

:::{iframe} https://www.youtube.com/embed/OjZlRZ7QeMk?si=o0VImy3k-X_jDYbM
:width: 60%
Introduction to 2-D inversion with ResIPy
:::

---

## Summary

```{admonition} What you have learned
:class: tip

| Step | Method | Purpose |
|------|--------|---------|
| 1 | `Project(typ='R2')` | Create project |
| 2 | `createSurvey(file, ftype=...)` | Load field data |
| 3 | `showPseudo()` / `showError()` | Inspect data quality |
| 4 | `filterUnpaired()` / `filterRecip()` / `filterElec()` | Remove bad data |
| 5 | `fitErrorLin()` / `fitErrorPwl()` | Fit error model |
| 6 | `createMesh(typ='trian')` | Build finite element mesh |
| 7 | `invert()` | Run regularised inversion |
| 8 | `showResults()` / `showInvError()` | Visualise and validate results |

**Platform summary:**
- **Windows** — native binaries, no Wine needed, full inversion support out of the box
- **Linux / macOS** — install Wine (`sudo apt install wine-stable` or `brew install --cask wine-stable`) for the inversion step

**Next notebook:** [emagpy Introduction](01_emagpy_introduction.md) — process **electromagnetic induction** data with emagpy.
```

---

## Additional Resources

- [ResIPy official documentation](https://hkex.gitlab.io/resipy/)
- [ResIPy GitLab repository & releases](https://gitlab.com/hkex/resipy)
- [ResIPy on PyPI](https://pypi.org/project/resipy/)
- [ResIPy YouTube channel](https://www.youtube.com/channel/UCkg2drwtfaVAo_Tuyeg_z5Q)
- [R2 inversion code — Lancaster University](http://www.es.lancs.ac.uk/people/amb/Freeware/R2/R2.htm)
