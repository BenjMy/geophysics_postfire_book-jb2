---
title: "Troubleshooting Guide"
---


# Troubleshooting Guide

```{admonition} Before you start
:class: tip
Check that your conda environment (or Poetry shell) is **activated** before running any commands.
```

---

## Installation Issues

### `poetry: command not found`

```{code-block} bash
export PATH="$HOME/.local/bin:$PATH"
# Make it permanent:
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

### Conda environment not activating

```{code-block} bash
conda init bash   # replace bash with zsh / fish as needed
# Restart your terminal, then:
conda activate geophysics-course
```

---

## Import Errors

### `ModuleNotFoundError: No module named 'resipy'`

````{tab-set}

```{tab-item} Conda
conda env update -f environment.yml
conda activate geophysics-course
```

```{tab-item} Poetry
poetry install
```

```{tab-item} pip
pip install -r requirements.txt
```

````

---

## Jupyter Issues

### Kernel not found

```{code-block} bash
# Register the environment as a Jupyter kernel
python -m ipykernel install --user --name=geophysics-course --display-name "Geophysics (Python 3.10)"
```

Then restart Jupyter Lab and select **Geophysics (Python 3.10)** from the kernel menu.

---

## Performance Issues

### Slow inversion

```{admonition} Tips for faster inversions
:class: note
- Reduce mesh resolution (increase element size)
- Enable parallel processing: `k.param['num_threads'] = 4`
- Monitor RAM with `htop` or Task Manager — inversions are memory-intensive
- Start with 2-D (`typ='R2'`) before attempting 3-D
```

---

## Wine / R2.exe Warning (Linux & macOS)

You may see this on `Project()` creation:

```
Warning: Wine is not installed!
/bin/sh: wine: not found
```

```{admonition} Solution
:class: warning
Install Wine to enable the full inversion engine:
```bash
sudo apt install wine-stable    # Debian / Ubuntu
brew install --cask wine-stable # macOS (Homebrew)
```
Data loading, pseudosection plotting, and mesh creation work without Wine.
```

---

## Getting Further Help

```{list-table}
:header-rows: 1

* - Resource
  - Link
* - GitHub Issues
  - [Open an issue](https://github.com/yourusername/geophysics-python-course/issues)
* - resipy docs
  - [gitlab.com/hkex/resipy](https://gitlab.com/hkex/resipy)
* - emagpy docs
  - [gitlab.com/hkex/emagpy](https://gitlab.com/hkex/emagpy)
```

When opening an issue, please include:

- Your operating system and Python version
- The full error message (copy from the terminal)
- Steps to reproduce the problem
