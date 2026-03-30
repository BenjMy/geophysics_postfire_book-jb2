---
title: "Electrical Resistivity"
kernelspec:
  name: python3
  display_name: Python 3 (Geophysics)
  language: python
---


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
print(f"\033[96mResistance of 1 m3 loam cube : {R:.1f} Ω\033[0m")
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


https://em.geosci.xyz/content/physical_properties/electrical_conductivity/electrical_conductivity_values.html


---

## The 4-Electrode concept

In the field we inject current through two **current electrodes** (A, B) and measure voltage across two **potential electrodes** (M, N):

$$\rho_a = K \cdot \frac{V_{MN}}{I_{AB}}$$

where $K$ is the **geometric factor** that depends on electrode geometry.

For the **Wenner** array with spacing $a$:

$$K_{Wenner} = 2 \pi a$$

Explain here why 4 electrodes (to avoid electrical resistance)


### Electrode geometry and sequence 

Adjust electrode spacing, current and true resistivity to explore the measurement:

---



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
