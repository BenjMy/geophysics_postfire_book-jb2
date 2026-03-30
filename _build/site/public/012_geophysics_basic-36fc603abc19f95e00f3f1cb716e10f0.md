---
title: "Introduction to Geophysics"
kernelspec:
  name: python3
  display_name: Python 3 (Geophysics)
  language: python
---


# Introduction to Geophysics

```{admonition} Learning Objectives
:class: note
- Understand the physical basis of electrical resistivity methods
- Apply Ohm's Law in a geophysical context
- Explore how soil properties control resistivity
- Introduce the concept of a 4-electrode measurement
```

---

## Soil Physical Properties

The electrical **resistivity** $\rho$ (Ω·m) describes how strongly a material opposes the flow of electric current. Its inverse is **conductivity** $\sigma$ (S/m):

$$\sigma = \frac{1}{\rho}$$

### Ohm's Law

For a homogeneous cylinder of cross-section $A$ (m²) and length $L$ (m):

$$R = \rho \frac{L}{A}$$

where $R$ is resistance (Ω). Rearranging:

$$\rho = R \frac{A}{L}$$

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt

def resistance(rho, L, A):
    """Ohm's Law: resistance of a homogeneous cylinder."""
    return rho * L / A

# Example: a 1 m³ cube of moist loam (rho ≈ 50 Ω·m)
rho_loam = 50   # Ω·m
R = resistance(rho_loam, L=1.0, A=1.0)
print(f"Resistance of 1 m³ loam cube : {R:.1f} Ω")
```

---

## Typical Resistivity Values

```{code-cell} ipython3
materials = {
    "Seawater"        : (0.2,   1),
    "Clay"            : (1,    20),
    "Groundwater"     : (10,  100),
    "Moist soil"      : (20,  200),
    "Dry sand / gravel": (200, 2000),
    "Limestone"       : (500, 10000),
    "Granite"         : (1e4, 1e6),
}

fig, ax = plt.subplots(figsize=(9, 4))
for i, (mat, (lo, hi)) in enumerate(materials.items()):
    ax.barh(i, np.log10(hi) - np.log10(lo),
            left=np.log10(lo), height=0.6,
            color=plt.cm.RdYlBu_r(i / len(materials)), edgecolor='k', linewidth=0.5)
    ax.text(np.log10(lo) - 0.05, i, mat, ha='right', va='center', fontsize=9)

ax.set_xlabel("log₁₀(Resistivity / Ω·m)")
ax.set_title("Typical resistivity ranges for earth materials")
ax.set_yticks([])
ax.set_xlim(-1, 7)
ax.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.show()
```

---

## The 4-Electrode (Wenner) Array

In the field we inject current through two **current electrodes** (A, B) and measure voltage across two **potential electrodes** (M, N):

$$\rho_a = K \cdot \frac{V_{MN}}{I_{AB}}$$

where $K$ is the **geometric factor** that depends on electrode geometry.

For the **Wenner** array with spacing $a$:

$$K_{Wenner} = 2 \pi a$$

```{code-cell} ipython3
def wenner_apparent_resistivity(V_mn, I_ab, a):
    """
    Compute apparent resistivity for a Wenner array.

    Parameters
    ----------
    V_mn : array-like  Measured voltage (V)
    I_ab : float       Injected current (A)
    a    : float       Electrode spacing (m)

    Returns
    -------
    np.ndarray  Apparent resistivity (Ω·m)
    """
    K = 2 * np.pi * a
    return K * np.asarray(V_mn) / I_ab

# Simulate a simple measurement
a = 2.0     # m — electrode spacing
I = 0.1     # A — injected current

# Synthetic voltages for a uniform half-space (rho = 100 Ω·m)
rho_true = 100  # Ω·m
K = 2 * np.pi * a
V_synthetic = rho_true * I / K

rho_a = wenner_apparent_resistivity(V_synthetic, I, a)
print(f"Geometric factor K = {K:.3f} m")
print(f"Voltage measured   = {V_synthetic*1000:.3f} mV")
print(f"Apparent resist.   = {rho_a:.1f} Ω·m  (should equal {rho_true} Ω·m for uniform half-space)")
```

---

## Electrode Geometry Diagram

```{code-cell} ipython3
fig, ax = plt.subplots(figsize=(9, 3))

# Ground surface
ax.axhline(0, color='saddlebrown', linewidth=2, label='Ground surface')
ax.fill_between([-1, 10], 0, -2, color='wheat', alpha=0.4)

positions = {'A': 0, 'M': 2, 'N': 4, 'B': 6}
colours   = {'A': 'firebrick', 'M': 'steelblue', 'N': 'steelblue', 'B': 'firebrick'}
roles     = {'A': 'Current +', 'M': 'Potential +', 'N': 'Potential −', 'B': 'Current −'}

for label, x in positions.items():
    ax.plot(x, 0, 'v', markersize=14, color=colours[label])
    ax.text(x, 0.25, label, ha='center', fontsize=12, fontweight='bold', color=colours[label])
    ax.text(x, -0.55, roles[label], ha='center', fontsize=8, color='gray')

# Spacing annotations
for (x0, x1), txt in [((0, 2), 'a'), ((2, 4), 'a'), ((4, 6), 'a')]:
    ax.annotate('', xy=(x1, -0.85), xytext=(x0, -0.85),
                arrowprops=dict(arrowstyle='<->', color='k'))
    ax.text((x0 + x1) / 2, -1.1, txt, ha='center', fontsize=10)

ax.set_xlim(-1, 7)
ax.set_ylim(-1.5, 1.0)
ax.set_aspect('equal')
ax.axis('off')
ax.set_title("Wenner array — equal electrode spacing $a$", pad=12)
plt.tight_layout()
plt.show()
```

---

```{admonition} Summary
:class: tip
You now understand:
- Electrical resistivity and its physical meaning
- Typical resistivity values for common earth materials
- How the 4-electrode measurement works
- The Wenner geometric factor $K = 2\pi a$

Next: [resipy Introduction](../02_resipy/01_resipy_introduction.md) — use **resipy** to process real survey data.
```
