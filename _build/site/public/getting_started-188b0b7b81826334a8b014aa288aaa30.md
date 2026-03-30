---
title: "Getting Started"
---


# Getting Started

```{admonition} Prerequisites
:class: important
- Python 3.9 or higher installed
- Basic familiarity with the command line
- Jupyter Notebook or JupyterLab
```

## First Steps

**1. Launch Jupyter Lab:**

```bash
jupyter lab
```

**2. Navigate to notebooks:**

Open `notebooks/01_introduction/01_python_basics.ipynb`

**3. Run your first cell:**

Press `Shift + Enter` to run cells.

---

## Course Structure

::::{grid} 1 1 2 2
:gutter: 3

:::{grid-item-card} Week 1 · Python Basics
:class-header: bg-light
- Introduction to Python
- NumPy and Matplotlib
- Data handling with Pandas
:::

:::{grid-item-card} Week 2 · resipy
:class-header: bg-light
- Electrical resistivity theory
- Data import and visualisation
- ERT inversion basics
:::

:::{grid-item-card} Week 3 · emagpy
:class-header: bg-light
- Electromagnetic methods overview
- EMI data processing
- Forward modelling
:::

:::{grid-item-card} Week 4 · Case Studies
:class-header: bg-light
- Archaeological survey
- Groundwater investigation
- Full workflow integration
:::

::::

---

## Verifying Your Installation

Open a Python terminal and run:

```python
import resipy
import emagpy
import numpy as np
import matplotlib.pyplot as plt

print("All packages imported successfully!")
```

If you see the success message, you are ready to go!

---

## Tips for Success

```{tip}
- Complete exercises in order — each builds on the last
- Experiment with code examples, break things, fix them!
- Attempt exercises **before** looking at solutions
- Ask questions in the course discussions
```

---

## Next Steps

```{seealso}
- [Installation Guide](installation.md) — Detailed installation instructions for all platforms
- [Troubleshooting Guide](troubleshooting.md) — Common issues and fixes
- [Python Basics](../notebooks/01_introduction/01_python_basics.md) — Start the first notebook
```
