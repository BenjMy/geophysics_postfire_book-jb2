---
title: "Emagpy processing"
kernelspec:
  name: python3
  display_name: Python 3 (Geophysics)
  language: python
---


# Introduction to emagpy

## Overview

**emagpy** is a Python API for processing and inverting **Electromagnetic Induction (EMI)** data, often collected with ground-conductivity meters such as the Dualem or CMD instruments.

```{admonition} Learning Objectives
:class: note
- Understand the EMI measurement principle
- Import and inspect an EMI dataset with emagpy
- Visualise raw ECa maps and profiles
- Run a 1-D lateral inversion to estimate subsurface conductivity
```



---

## Creating a Problem

```{code-cell} ipython3
from emagpy import Problem

k = Problem()
print("emagpy Problem created successfully!")
```

---

## Importing Data

```{code-cell} ipython3
# Load a CSV data file
# k.importData('data/sample_em/survey.csv')

# Expected CSV format:
print("Expected CSV columns:")
header = "x, y, ECa_HCP_0.32m, ECa_HCP_0.71m, ECa_HCP_1.18m, ECa_VCP_0.32m"
print(" ", header)
print("  0.0, 0.0, 35.2, 48.1, 62.4, 28.9")
print("  0.5, 0.0, 36.8, 49.3, 63.1, 29.5")
print("  ...")
```

---

## Synthetic ECa Map

```{code-cell} ipython3
np.random.seed(7)

# Simulate a survey grid (50 × 20 m)
x = np.linspace(0, 50, 60)
y = np.linspace(0, 20, 25)
X, Y = np.meshgrid(x, y)

# Synthetic ECa: background + conductive anomaly
ECa = 25 + 20 * np.exp(-((X - 25)**2 / 60 + (Y - 10)**2 / 15))
ECa += np.random.normal(0, 1.5, ECa.shape)  # add noise

fig, ax = plt.subplots(figsize=(11, 4))
im = ax.pcolormesh(X, Y, ECa, cmap='viridis', shading='auto')
cb = fig.colorbar(im, ax=ax, pad=0.02)
cb.set_label("ECa (mS/m)")
ax.set_xlabel("Easting (m)")
ax.set_ylabel("Northing (m)")
ax.set_title("Synthetic ECa map — HCP 1.18 m coil")
ax.set_aspect('equal')
plt.tight_layout()
plt.show()
```

---

## 1-D Lateral Inversion

emagpy inverts each measurement position independently using a layered-earth model.

```{code-cell} ipython3
# After importing real data:
#
# k.setInit(conds0=[30, 30, 30],    # initial conductivity (mS/m) per layer
#           depths0=[0.5, 1.5])     # layer depths (m)
# k.invertGN()                      # Gauss-Newton inversion
# k.showResults()                   # plot conductivity maps per layer

# Conceptual layered model illustration
layer_depths  = [0,    0.5,  1.5,  4.0]
layer_conds   = [20,   55,   30,   15]   # mS/m
layer_labels  = ["Topsoil", "Clay lens", "Sandy subsoil", "Bedrock"]
colors        = ['#c4a35a', '#8b4513', '#d2b48c', '#808080']

fig, ax = plt.subplots(figsize=(5, 6))
for i in range(len(layer_conds)):
    top    = -layer_depths[i]
    bottom = -layer_depths[i+1] if i+1 < len(layer_depths) else -5.5
    rect = plt.Rectangle((0, bottom), layer_conds[i], top - bottom,
                          color=colors[i], alpha=0.85, edgecolor='k', linewidth=0.8)
    ax.add_patch(rect)
    ax.text(layer_conds[i] / 2, (top + bottom) / 2,
            f"{layer_labels[i]}\n{layer_conds[i]} mS/m",
            ha='center', va='center', fontsize=9)

ax.set_xlim(0, 70)
ax.set_ylim(-5.5, 0.2)
ax.set_xlabel("Electrical conductivity (mS/m)")
ax.set_ylabel("Depth (m)")
ax.set_title("Example 1-D inverted model")
ax.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.show()
```

---

```{admonition} Summary
:class: tip
You have learned:
- The physics of electromagnetic induction measurement
- How coil orientation affects depth sensitivity (McNeill 1980)
- How to create an emagpy `Problem` and load survey data
- What the inverted conductivity model looks like
```
