---
title: "ERT"
kernelspec:
  name: python3
  display_name: Python 3 (Geophysics)
  language: python
---


# Introduction to electrical resistivity tomography

## Overview

**resipy** (also called *ResIPy*) is a Python wrapper around the robust R2 / cR2 / R3t inversion codes for 2-D and 3-D electrical resistivity tomography (ERT).

```{admonition} Learning Objectives
:class: note
- Understand the ERT data-acquisition workflow
- Create and configure a resipy `Project`
- Import field data and visualise a pseudosection
- Run a basic regularised inversion
- Interpret an inverted resistivity section
```

---

## Installation Check

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt
from resipy import Project

print("resipy imported successfully!")
```

```{admonition} Wine warning on Linux/macOS
:class: warning
You may see `Warning: Wine is not installed!` — this is expected if Wine is absent.
Data loading and visualisation work without Wine; only the inversion binary (R2.exe) needs it.
Install with `sudo apt install wine-stable` on Debian/Ubuntu to enable full inversion.
```

---

## Creating a Project

```{code-cell} ipython3
# Create a 2-D resistivity project
k = Project(typ='R2')
print("Project created!")
```

The `typ` argument selects the inversion engine:

| `typ`  | Engine | Use case |
|--------|--------|----------|
| `'R2'` | R2.exe | 2-D resistivity |
| `'cR2'`| cR2.exe| 2-D complex resistivity (IP) |
| `'R3t'`| R3t.exe| 3-D resistivity |
| `'cR3t'`|cR3t.exe|3-D complex resistivity |

---

## Importing Survey Data

```{code-cell} ipython3
# Load a survey data file (ABMN format)
# k.createSurvey('data/sample_resistivity/survey.dat')

# For this demo, we inspect the expected data format
print("Expected column format (.dat file):")
print("  A    B    M    N    Resistance(Ω)")
print("  0    9    3    6    12.45")
print("  0   12    4    8     9.21")
print("  ...")
```

```{admonition} Data formats
:class: note
resipy supports many common ERT data formats including:
**Syscal** (IRIS), **Res2Dinv**, **ABEM LS**, **Campus Tigre**, **Protocol** and more.
Pass `ftype='Syscal'` (or other) to `createSurvey()` for automatic parsing.
```

---

## Pseudosection Visualisation

A **pseudosection** plots apparent resistivity against electrode mid-point and pseudo-depth.
It is a qualitative picture of the data — not a true depth section.

```{code-cell} ipython3
# After loading data:
# k.showPseudoSection()

# Simulated pseudosection for illustration
np.random.seed(42)
n_levels = 8
n_points = 40

fig, ax = plt.subplots(figsize=(11, 5))

x_mid  = np.linspace(0, 47, n_points)
depths = np.arange(1, n_levels + 1) * 1.5

cmap = plt.cm.RdYlBu_r
norm = plt.Normalize(vmin=10, vmax=500)

for depth in depths:
    rho_a = np.exp(np.random.normal(loc=4.5, scale=0.4, size=n_points))
    sc = ax.scatter(x_mid, -np.full_like(x_mid, depth),
                    c=rho_a, cmap=cmap, norm=norm, s=60, marker='v')

cb = fig.colorbar(sc, ax=ax, pad=0.02)
cb.set_label("Apparent Resistivity (Ω·m)")
ax.set_xlabel("Mid-point position (m)")
ax.set_ylabel("Pseudo-depth (m)")
ax.set_title("Synthetic Pseudosection — Wenner Array")
ax.grid(True, alpha=0.2)
plt.tight_layout()
plt.show()
```

---

## Running an Inversion

```{code-cell} ipython3
# After creating the survey and mesh:
#
# k.createMesh(typ='trian')        # triangular mesh
# k.param['a_wgt'] = 0.01         # regularisation weight
# k.invert()                       # run R2
# k.showResults()                  # display inverted section
#
# The inversion minimises:
#   Φ = ‖Wd(d_obs − d_pred)‖² + λ‖Wm m‖²
# where λ is the regularisation parameter (trade-off).

print("Inversion parameters overview:")
params = {
    "a_wgt"    : "Absolute data weight (noise floor)",
    "b_wgt"    : "Relative data weight",
    "alpha_s"  : "Smoothness regularisation weight",
    "max_iter" : "Maximum inversion iterations",
}
for k_p, desc in params.items():
    print(f"  {k_p:12s}  →  {desc}")
```

---

## Synthetic Inverted Section

```{code-cell} ipython3
from matplotlib.colors import LogNorm

# Synthetic 2-D resistivity model for illustration
nx, nz = 80, 30
x = np.linspace(0, 47, nx)
z = np.linspace(0, -15, nz)
X, Z = np.meshgrid(x, z)

# Background + conductive anomaly + resistive layer
rho = np.full((nz, nx), 150.0)
rho[Z > -8] = 80      # shallow moist layer
rho[(Z > -12) & (Z < -8) & (X > 15) & (X < 30)] = 12   # conductive body
rho[Z < -13] = 800    # resistive bedrock

fig, ax = plt.subplots(figsize=(11, 4))
im = ax.pcolormesh(X, Z, rho, cmap='RdYlBu_r', norm=LogNorm(vmin=10, vmax=1000), shading='auto')
cb = fig.colorbar(im, ax=ax, pad=0.02)
cb.set_label("Resistivity (Ω·m)")
ax.set_xlabel("Distance (m)")
ax.set_ylabel("Depth (m)")
ax.set_title("Synthetic Inverted Resistivity Section")
plt.tight_layout()
plt.show()
```

---

## Interpretation Guide

```{list-table}
:header-rows: 1
:widths: 25 25 50

* - Feature
  - Resistivity
  - Possible interpretation
* - Shallow low-ρ zone
  - < 30 Ω·m
  - Moist / clay-rich topsoil
* - Deep conductive body
  - 5–20 Ω·m
  - Saline groundwater, leachate plume
* - Resistive layer
  - > 500 Ω·m
  - Dry sand, gravel, bedrock
* - Lateral contrast
  - —
  - Lithological boundary or fault
```

---

```{admonition} Summary
:class: tip
You have learned:
- How to create a **resipy** `Project` and load ERT data
- What a pseudosection shows (and its limitations)
- How regularised inversion works conceptually
- Basic interpretation of an inverted resistivity section

Next: [emagpy Introduction](01_emagpy_introduction.md) — process **electromagnetic** data with emagpy.
```
