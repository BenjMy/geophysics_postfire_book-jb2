---
title: "Petro/pedophysical model"
kernelspec:
  name: python3
  display_name: Python 3 (Geophysics)
  language: python
---


```{admonition} Key principle
:class: tip
Geophysical measurements are **indirect**. They do not measure soil water content or clay content directly — they measure a physical signal (resistivity, wave velocity, radar travel time) that correlates with those properties. Interpreting geophysical data always requires some knowledge of the local soil conditions.
```

For instance, field-measured resistivity integrates into a single bulk quantity: 
- The effects of pore geometry
- Fluid saturation, 
- Pore-water chemistry.


**Petrophysics** is the study of the physical and chemical properties of rocks and soils and their contained fluids. It provides the quantitative link — known as a **petrophysical transfer function** — between a measurable geophysical quantity and a target physical property of interest. Because these relationships are empirical and lithology-dependent, they must be calibrated for each site and carry inherent uncertainty.


Extracting hydrological state variables from resistivity data therefore requires an explicit **petrophysical model**. For clean, clay-free porous media, **Archie's law** {cite}`archie2003electrical` provides the standard empirical framework:

$$
\rho = a \, \phi^{-m} \, S_w^{-n} \, \rho_w
$$

where $\phi$ is porosity (–), $S_w$ is the degree of water saturation (–), $\rho_w$ is the pore-water resistivity (Ω·m), and $a$, $m$, $n$ are empirical Archie parameters controlling tortuosity, cementation, and saturation exponent, respectively. Because these parameters are lithology-dependent and must be calibrated from core or borehole measurements, the inversion of resistivity images into soil-moisture fields always carries **model uncertainty** {cite}`tso2019wrr`.


```{admonition} Relationships are empirical and lithology-dependent
:class: caution
Petrophysical relationships must be calibrated for each site.
```

The [figure below](#fig-pedophysicsChou) illustrate an example of ERT data converted to soil matric potential and soil water content using petrophysical relationships. For more details, please read the full article {cite}`chou2024improving`. 


```{figure} ../assets/images/pedophysicsChou.png
:name: fig-pedophysicsChou
:width: 100%
:align: center
Example of ERT data converted to soil matric potential and soil water content using petrophysical relationships (figure from {cite}`chou2024improving`). 
```



The code below illustrates how **Archie's Law** relates water saturation ($S_w$) to bulk formation resistivity ($\rho$) for a given porosity ($\phi$) and tortuosity factor ($a$), showing that as $S_w$ decreases — indicating more hydrocarbons displacing brine — resistivity increases nonlinearly following a power-law relationship governed by the saturation exponent $n$.

```{code-cell} ipython3
:tags: [hide-input]
import numpy as np
import plotly.graph_objects as go
import ipywidgets as widgets
from IPython.display import display
import matplotlib.pyplot as plt
from ipywidgets import interact

def archie_resistivity(phi, Sw, rho_w=0.1, a=1.0, m=1.5, n=2.0):
    return a * phi**(-m) * Sw**(-n) * rho_w

Sw_arr = np.linspace(0.05, 1.0, 300)

def plot_archie(phi=0.20, a=1.0):
    rho = archie_resistivity(phi, Sw_arr, a=a)
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.plot(rho, Sw_arr, color='#2980b9', linewidth=2.5)
    ax.set_xscale('log')
    ax.set_xlim(0.01, 1000)
    ax.set_ylim(0, 1.05)
    ax.set_xlabel('Resistivity ρ (Ω·m)')
    ax.set_ylabel('Water Saturation $S_w$')
    ax.set_title("Archie's Law — ρ = a · φ$^{-m}$ · $S_w^{-n}$ · ρ$_w$")
    ax.grid(True, which='both', linestyle='--', alpha=0.4)
    plt.tight_layout()
    plt.show()

interact(
    plot_archie,
    phi=widgets.SelectionSlider(
        options=[(str(v), v) for v in np.round(np.arange(0.05, 0.61, 0.01), 2)],
        value=0.20,
        description='φ (porosity)',
        style={'description_width': '120px'},
        layout=widgets.Layout(width='500px')
    ),
    a=widgets.SelectionSlider(
        options=[(str(v), v) for v in np.round(np.arange(0.5, 2.05, 0.25), 2)],
        value=1.0,
        description='a (tortuosity)',
        style={'description_width': '120px'},
        layout=widgets.Layout(width='500px')
    ),
)
```




 
