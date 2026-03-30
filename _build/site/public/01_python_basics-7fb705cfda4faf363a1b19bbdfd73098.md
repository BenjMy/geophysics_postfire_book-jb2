---
title: "Introduction to Python Basics"
kernelspec:
  name: python3
  display_name: Python 3 (Geophysics)
  language: python
---


# Introduction to Python Basics

Welcome to the Geophysics Python Course!

```{admonition} Learning Objectives
:class: note
- Understand Python syntax and the interactive notebook environment
- Work with variables and the most common data types
- Use basic control structures (loops, conditionals)
- Write and call your first functions
```

---

## Hello, Geophysics!

```{code-cell} ipython3
# Your first Python code
print("Hello, Geophysics!")
```

---

## Variables and Data Types

Python variables need no explicit type declaration — the interpreter infers the type from the value assigned.

```{code-cell} ipython3
# Numeric types
resistivity = 100.5   # float — Ohm·m
num_electrodes = 48   # int

# String
survey_type = "Wenner array"

# List  
measurements = [12.5, 15.3, 18.7, 21.2]  # apparent resistivity values

print(f"Survey type       : {survey_type}")
print(f"Electrodes        : {num_electrodes}")
print(f"Resistivity (Ω·m) : {resistivity}")
print(f"Measurements      : {measurements}")
```

```{code-cell} ipython3
# Check the type of a variable
print(type(resistivity))
print(type(num_electrodes))
print(type(survey_type))
print(type(measurements))
```

---

## Control Structures

### Conditionals

```{code-cell} ipython3
rho = 250  # Ohm·m

if rho < 10:
    print("Very conductive — possible clay or saline water")
elif rho < 100:
    print("Moderately conductive — moist soil")
elif rho < 1000:
    print("Resistive — dry soil or gravel")
else:
    print("Highly resistive — bedrock or dry sand")
```

### Loops

```{code-cell} ipython3
electrode_positions = [0, 1, 2, 3, 4]  # metres

for i, pos in enumerate(electrode_positions):
    print(f"Electrode {i+1:2d}  →  x = {pos} m")
```

---

## Functions

Functions let you package reusable logic with a clear interface.

```{code-cell} ipython3
def apparent_resistivity(V, I, K):
    """
    Calculate apparent resistivity.

    Parameters
    ----------
    V : float
        Measured voltage (V)
    I : float
        Applied current (A)
    K : float
        Geometric factor for the array (m)

    Returns
    -------
    float
        Apparent resistivity (Ω·m)
    """
    return K * (V / I)

# Wenner array with a = 1 m → K = 2πa
import math
a = 1.0          # electrode spacing (m)
K_wenner = 2 * math.pi * a

rho_a = apparent_resistivity(V=0.05, I=0.001, K=K_wenner)
print(f"Apparent resistivity: {rho_a:.1f} Ω·m")
```

---

## NumPy Basics

[NumPy](https://numpy.org) is the backbone of numerical computing in Python.

```{code-cell} ipython3
import numpy as np

# Create an array of electrode positions
x = np.linspace(0, 47, 48)   # 48 electrodes, 1 m spacing
print(f"Electrode positions: {x[:6]} ... {x[-3:]}")
print(f"Array shape: {x.shape}")

# Vectorised arithmetic — no loops needed
rho_values = np.random.lognormal(mean=4.5, sigma=0.5, size=48)
print(f"\nMean apparent resistivity : {rho_values.mean():.1f} Ω·m")
print(f"Std  apparent resistivity : {rho_values.std():.1f} Ω·m")
```

---

## Matplotlib Quick Plot

```{code-cell} ipython3
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(9, 3))
ax.plot(x, rho_values, 'o-', color='steelblue', markersize=4, linewidth=1)
ax.set_xlabel("Electrode position (m)")
ax.set_ylabel("Apparent resistivity (Ω·m)")
ax.set_title("Synthetic resistivity profile — Wenner array")
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

---

```{admonition} Summary
:class: tip
You have covered:
- Variables, data types, and lists
- `if / elif / else` conditionals and `for` loops
- Defining functions with docstrings
- NumPy arrays and vectorised operations
- Basic Matplotlib plotting

Move on to [Geophysics Basics](012_geophysics_basics.md) for an introduction to geophysical theory.
```
