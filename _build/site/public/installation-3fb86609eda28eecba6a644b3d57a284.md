---
title: "Installation Guide"
---


# Installation Guide

## System Requirements

```{list-table}
:header-rows: 1
:widths: 30 70

* - Requirement
  - Minimum / Recommended
* - **Python**
  - 3.9+ (3.10 recommended)
* - **RAM**
  - 4 GB minimum · 8 GB recommended
* - **Disk space**
  - 2 GB free
* - **OS**
  - Linux, macOS, Windows 10/11
```

---

## Method 1 · Conda (Recommended)

Conda handles both Python and native library dependencies cleanly.

**Step 1 — Install Miniconda** (if needed):

Download from [docs.conda.io](https://docs.conda.io/en/latest/miniconda.html) and follow the installer.

**Step 2 — Create the environment:**

```bash
conda env create -f environment.yml
conda activate geophysics-course
```

**Step 3 — Launch Jupyter Lab:**

```bash
jupyter lab
```

---

## Method 2 · Poetry

Poetry provides reproducible dependency management.

**Step 1 — Install Poetry:**

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

**Step 2 — Install and activate:**

```bash
git clone https://github.com/yourusername/geophysics-python-course.git
cd geophysics-python-course
poetry install
poetry shell
```

**Step 3 — Launch Jupyter Lab:**

```bash
jupyter lab
```

---

## Method 3 · pip + venv

```bash
python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

---

## Verifying the Installation

```{code-cell} ipython3
:tags: [remove-output]
import resipy
import emagpy
import numpy as np
import matplotlib.pyplot as plt

print(f"NumPy     : {np.__version__}")
print(f"Matplotlib: {plt.matplotlib.__version__}")
print("✅ All packages imported successfully!")
```

---

```{admonition} Linux / Wine note
:class: warning
On Linux, the **R2.exe** inversion binary inside resipy requires **Wine** to run.
Install it with:
```bash
sudo apt install wine-stable   # Debian / Ubuntu
sudo dnf install wine          # Fedora
```
You will see a warning on `Project()` creation if Wine is missing, but data loading and visualisation will still work.
```

---

## Troubleshooting

```{seealso}
See [Troubleshooting Guide](troubleshooting.md) for solutions to the most common installation issues.
```
