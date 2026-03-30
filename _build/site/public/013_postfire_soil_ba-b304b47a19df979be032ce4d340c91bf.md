---
title: "Post-fire soil restauration"
kernelspec:
  name: python3
  display_name: Python 3 (Geophysics)
  language: python
---


# Main threads

- Soil erosion
- Fertility( soil organic matter loss
- surface runoff
- affect water flow





# remediation strategies

- mulching
- erosion log/barriers
- bare soil 


(insert here an image 


# Timeline of actuation 

- just after the fire
- 5 years after 
- 10 years after 





# what geophysics can sense?


# ----remove after this 





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
:tags: [hide-input]
import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display

def resistance(rho, L, A):
    """Ohm's Law: resistance of a homogeneous cylinder."""
    return rho * L / A

# Example: a 1 m³ cube of moist loam (rho ≈ 50 Ω·m)
rho_loam = 50   # Ω·m
R = resistance(rho_loam, L=1.0, A=1.0)
print(f"Resistance of 1 m³ loam cube : {R:.1f} Ω")
```

### 🎛️ Interactive Explorer — Ohm's Law

Adjust resistivity, length and cross-section to see how resistance changes:

```{code-cell} ipython3
:tags: [hide-input]
def ohm_widget():
    rho_slider = widgets.FloatLogSlider(
        value=50, base=10, min=0, max=6,
        step=0.05, description='ρ (Ω·m)',
        style={'description_width': '80px'},
        layout=widgets.Layout(width='450px')
    )
    L_slider = widgets.FloatSlider(
        value=1.0, min=0.1, max=10.0, step=0.1,
        description='L (m)',
        style={'description_width': '80px'},
        layout=widgets.Layout(width='450px')
    )
    A_slider = widgets.FloatSlider(
        value=1.0, min=0.01, max=5.0, step=0.01,
        description='A (m²)',
        style={'description_width': '80px'},
        layout=widgets.Layout(width='450px')
    )
    out = widgets.Output()

    def update(change=None):
        R = rho_slider.value * L_slider.value / A_slider.value
        sigma = 1 / rho_slider.value
        with out:
            out.clear_output(wait=True)
            print(f"  Resistance  R = {R:.4f} Ω")
            print(f"  Conductivity σ = {sigma:.6f} S/m")

    rho_slider.observe(update, names='value')
    L_slider.observe(update, names='value')
    A_slider.observe(update, names='value')
    update()

    display(widgets.VBox([
        widgets.HTML("<b>Ohm's Law — R = ρ · L / A</b>"),
        rho_slider, L_slider, A_slider, out
    ]))

ohm_widget()
```

---

## Typical Resistivity Values

```{code-cell} ipython3
:tags: [hide-input]
materials = {
    "Seawater"          : (0.2,   1),
    "Clay"              : (1,    20),
    "Groundwater"       : (10,  100),
    "Moist soil"        : (20,  200),
    "Dry sand / gravel" : (200, 2000),
    "Limestone"         : (500, 10000),
    "Granite"           : (1e4, 1e6),
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

### 🎛️ Interactive Explorer — Material Resistivity

Hover over a material to highlight its range, or select one to see its typical properties:

```{code-cell} ipython3
:tags: [hide-input]
def material_widget():
    mat_names = list(materials.keys())
    dropdown = widgets.Dropdown(
        options=mat_names,
        value='Moist soil',
        description='Material:',
        style={'description_width': '80px'},
        layout=widgets.Layout(width='350px')
    )
    out = widgets.Output()

    def update(change=None):
        mat = dropdown.value
        lo, hi = materials[mat]
        sigma_lo = 1 / hi
        sigma_hi = 1 / lo
        with out:
            out.clear_output(wait=True)
            fig, ax = plt.subplots(figsize=(8, 1.8))
            for i, (m, (l, h)) in enumerate(materials.items()):
                color = 'steelblue' if m == mat else 'lightgrey'
                ax.barh(0, np.log10(h) - np.log10(l),
                        left=np.log10(l), height=0.5,
                        color=color, edgecolor='k', linewidth=0.4, alpha=0.9)
            ax.set_xlabel("log₁₀(ρ / Ω·m)")
            ax.set_yticks([])
            ax.set_xlim(-1, 7)
            ax.set_title(f"{mat}   |   ρ: {lo}–{hi} Ω·m   |   σ: {sigma_lo:.2e}–{sigma_hi:.2e} S/m")
            ax.grid(axis='x', alpha=0.3)
            plt.tight_layout()
            plt.show()

    dropdown.observe(update, names='value')
    update()
    display(widgets.VBox([dropdown, out]))

material_widget()
```

---

## The 4-Electrode (Wenner) Array

In the field we inject current through two **current electrodes** (A, B) and measure voltage across two **potential electrodes** (M, N):

$$\rho_a = K \cdot \frac{V_{MN}}{I_{AB}}$$

where $K$ is the **geometric factor** that depends on electrode geometry.

For the **Wenner** array with spacing $a$:

$$K_{Wenner} = 2 \pi a$$

```{code-cell} ipython3
:tags: [hide-input]
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

### 🎛️ Interactive Explorer — Wenner Array

Adjust electrode spacing, current and true resistivity to explore the measurement:

```{code-cell} ipython3
:tags: [hide-input]
def wenner_widget():
    rho_slider = widgets.FloatLogSlider(
        value=100, base=10, min=0, max=4,
        step=0.05, description='ρ true (Ω·m)',
        style={'description_width': '110px'},
        layout=widgets.Layout(width='450px')
    )
    a_slider = widgets.FloatSlider(
        value=2.0, min=0.5, max=10.0, step=0.5,
        description='Spacing a (m)',
        style={'description_width': '110px'},
        layout=widgets.Layout(width='450px')
    )
    I_slider = widgets.FloatSlider(
        value=0.1, min=0.01, max=1.0, step=0.01,
        description='Current I (A)',
        style={'description_width': '110px'},
        layout=widgets.Layout(width='450px')
    )
    out = widgets.Output()

    def update(change=None):
        rho = rho_slider.value
        a   = a_slider.value
        I   = I_slider.value
        K   = 2 * np.pi * a
        V   = rho * I / K
        rho_a = wenner_apparent_resistivity(V, I, a)
        with out:
            out.clear_output(wait=True)
            print(f"  Geometric factor  K  = {K:.3f} m")
            print(f"  Voltage measured  V  = {V*1000:.4f} mV")
            print(f"  Apparent resist. ρₐ  = {rho_a:.1f} Ω·m")

    rho_slider.observe(update, names='value')
    a_slider.observe(update, names='value')
    I_slider.observe(update, names='value')
    update()

    display(widgets.VBox([
        widgets.HTML("<b>Wenner array — ρₐ = K · V / I &nbsp;&nbsp; K = 2πa</b>"),
        rho_slider, a_slider, I_slider, out
    ]))

wenner_widget()
```

---

## Electrode Geometry Diagram

```{code-cell} ipython3
:tags: [hide-input]
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

### 🎛️ Interactive Explorer — Array Geometry

Move the sliders to see how changing spacing $a$ shifts the electrode positions and updates the geometric factor:

```{code-cell} ipython3
:tags: [hide-input]
def geometry_widget():
    a_slider = widgets.FloatSlider(
        value=2.0, min=0.5, max=5.0, step=0.5,
        description='Spacing a (m)',
        style={'description_width': '110px'},
        layout=widgets.Layout(width='400px')
    )
    out = widgets.Output()

    def update(change=None):
        a = a_slider.value
        K = 2 * np.pi * a
        with out:
            out.clear_output(wait=True)
            fig, ax = plt.subplots(figsize=(9, 2.8))
            ax.axhline(0, color='saddlebrown', linewidth=2)
            ax.fill_between([-1, 4*a + 1], 0, -2, color='wheat', alpha=0.4)

            pos = {'A': 0, 'M': a, 'N': 2*a, 'B': 3*a}
            cols = {'A': 'firebrick', 'M': 'steelblue', 'N': 'steelblue', 'B': 'firebrick'}
            role = {'A': 'Current +', 'M': 'Potential +', 'N': 'Potential −', 'B': 'Current −'}

            for lbl, x in pos.items():
                ax.plot(x, 0, 'v', markersize=14, color=cols[lbl])
                ax.text(x, 0.25, lbl, ha='center', fontsize=12,
                        fontweight='bold', color=cols[lbl])
                ax.text(x, -0.5, role[lbl], ha='center', fontsize=8, color='gray')

            for (x0, x1), txt in [((0, a), 'a'), ((a, 2*a), 'a'), ((2*a, 3*a), 'a')]:
                ax.annotate('', xy=(x1, -0.8), xytext=(x0, -0.8),
                            arrowprops=dict(arrowstyle='<->', color='k'))
                ax.text((x0+x1)/2, -1.05, f'{a} m', ha='center', fontsize=9)

            ax.set_xlim(-0.5, 3*a + 0.5)
            ax.set_ylim(-1.4, 0.8)
            ax.axis('off')
            ax.set_title(f"Wenner array  |  a = {a} m  |  K = 2πa = {K:.2f} m", pad=10)
            plt.tight_layout()
            plt.show()

    a_slider.observe(update, names='value')
    update()
    display(widgets.VBox([a_slider, out]))

geometry_widget()
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
