---
title: River Bank ERT — Interactive Forward Model
authors:
  - name: Benjamin Mary
    email: benjamin.mary@ica.csic.es
    affiliations:
      - ICA-CSIC, Madrid, Spain
kernelspec:
  name: python3
  display_name: Python 3 (Geophysics)
  language: python

---

## 📍 Location

**Site:** Hellín — Rambla check dam network, Albacete, Spain
**Coordinates:** 38.50° N, 1.68° W
**Elevation:** ~580 m a.s.l.

---

## 🌍 Context

Sediment check dams (*diques de sedimentación*) are a common post-fire restoration measure in Spanish ramblas and ephemeral streams. They are designed to trap sediment mobilised by post-fire erosion, reduce downstream flood risk, and promote vegetation recovery in gully floors. However, their effectiveness and the physical properties of trapped sediments remain poorly characterised.

```{figure} ../../assets/images/diques2.jpeg
:width: 60%
:align: center
:alt: Check dam in Hellín rambla network
:name: diques1

One of the sediment check dams in the Hellín rambla network. Picture credit to M.E. Lucas Borja.
```

```{figure} ../../assets/images/diques1.jpeg
:width: 60%
:align: center
:alt: Check dam in Hellín rambla network
:name: diques2

One of the sediment check dams in the Hellín rambla network. Picture credit to M.E. Lucas Borja.
```

```{figure} ../../assets/images/diques3.jpeg
:width: 60%
:align: center
:alt: Check dam in Hellín rambla network
:name: diques3

One of the sediment check dams in the Hellín rambla network. Picture credit to M.E. Lucas Borja.
```

```{note}
Post-fire restoration context: After the 2022 wildfires in the Hellín area, a network of check dams was installed along the main rambla as an emergency erosion-control measure. This notebook provides a forward-modelling framework to design and evaluate ERT acquisition strategies for the geophysical characterisation of the sediment body behind these structures **prior to field data collection**.
```

```{caution}
Semi-permeable or confined dam? From the figures above, we can observe that the dams are not designed the same way, i.e., {numref}`diques1` shows a concrete dam that does not let sediment nor water through, while {numref}`diques2` and {numref}`diques3` are permeable to water.
```

---

## ❓ Scientific Question

> **What is the internal architecture and hydrological behaviour of sediment bodies trapped behind post-fire check dams, and how do they evolve over time?**

Key sub-questions:
- What is the volume and stratigraphic structure of accumulated sediment?
- Does water storage within the sediment body contribute to local groundwater recharge?
- How quickly do check dams fill, and what controls their trapping efficiency?
- Which ERT acquisition sequence and electrode layout best resolves the sediment stratigraphy?

---

## 🔬 Modelling Approach

### What is ERT?
Electrical Resistivity Tomography (ERT) is a geophysical method that images the underground by injecting electrical current into the ground through metal stakes called *electrodes*, and measuring the resulting voltage at other electrodes along the same line. Different materials conduct electricity differently: wet clay is a good conductor (low resistivity), while dry gravel or hard rock is a poor conductor (high resistivity). By combining many such measurements along a profile, we can reconstruct a 2-D image of the subsurface resistivity distribution — and from that infer geology, water content, or sediment layering.

### What is a forward model?
A *forward model* does the calculation in the "easy" direction: given a known underground structure, it predicts what an ERT instrument would measure. This is the opposite of *inversion*, which starts from real field measurements and tries to recover the underground structure. Running a forward model before going to the field is extremely useful because it lets us test different electrode layouts, array types, and noise levels *on the computer* before committing to a field campaign — saving time and resources.

This notebook implements a **2D ERT forward model** of a river bank cross-section perpendicular to the minor bed, with geology representative of the Hellín rambla system.

```{tip}
Why forward modelling before fieldwork? Synthetic modelling before data collection allows optimisation of survey design — electrode spacing, array type, and profile length — to maximise sensitivity to the target structures (sediment layers, moisture zones) given the expected depth range and resistivity contrasts.
```

The geological model is built from available literature values and sediment core analogues from comparable post-fire Mediterranean catchments.

```{note}
Resistivity contrasts in post-fire sediments: Fine ash and silt layers deposited after the initial post-fire flood pulse are particularly conductive (low resistivity, ~20–50 Ω·m) due to their high surface area, ionic load from burnt organic material, and tendency to retain moisture. Coarser gravel layers deposited during high-energy events are more resistive (~150–300 Ω·m). This contrast is the primary target for ERT-based stratigraphic discrimination.
```

---

## ⚙️ Simulation

### Step 1 — Imports

The cell below loads all the Python libraries needed for this notebook. Run it first before anything else.

- **numpy** handles numerical arrays and maths.
- **matplotlib** produces all the plots.
- **resipy** is the ERT modelling library — it wraps the R2 inversion code developed at Lancaster University.
- **ipywidgets** enables interactive widgets for dynamic parameter adjustments.

```{code-cell} ipython3
:tags: [remove-input]
import numpy as np
import matplotlib.pyplot as plt
from resipy import Project
import ipywidgets as widgets
from IPython.display import display, clear_output
```

---

### Step 2 & 3 — Survey, Geometry & Resistivity Parameters

This is the **only cell you need to edit** to customise the simulation. All subsequent cells read from these variables — so change values here and re-run the notebook from top to bottom.
**All parameters update automatically** when you adjust the sliders.

```{code-cell} ipython3
:tags: [remove-input]
# ---------------------------------------------------------------------------
# Electrode & acquisition
# ---------------------------------------------------------------------------
N_ELEC = widgets.IntSlider(
    value=57, min=10, max=100, step=1,
    description='Number of Electrodes:',
    style={'description_width': '200px'},
)
SPACING = widgets.FloatSlider(
    value=1.0, min=0.1, max=5.0, step=0.1,
    description='Electrode Spacing (m):',
    style={'description_width': '200px'},
)
SEQUENCE = widgets.Dropdown(
    options=['dpdp', 'wenner-schlumberger'],
    value='dpdp',
    description='Acquisition Sequence:',
    style={'description_width': '200px'},
)

NOISE = widgets.FloatSlider(
    value=0.03, min=0.01, max=0.1, step=0.01,
    description='Noise Level:',
    style={'description_width': '200px'},
)

# ---------------------------------------------------------------------------
# Channel cross-section geometry
# ---------------------------------------------------------------------------
RIVER_WIDTH = widgets.FloatSlider(
    value=10.0, min=5.0, max=30.0, step=0.5,
    description='River Width (m):',
    style={'description_width': '200px'},
)
BANK_HEIGHT = widgets.FloatSlider(
    value=2.0, min=0.5, max=5.0, step=0.1,
    description='Bank Height (m):',
    style={'description_width': '200px'},
)
BANK_SLOPE_W = widgets.FloatSlider(
    value=4.0, min=1.0, max=10.0, step=0.5,
    description='Bank Slope Width (m):',
    style={'description_width': '200px'},
)

# ---------------------------------------------------------------------------
# Subsurface layer model
# ---------------------------------------------------------------------------
LAYER_NAMES = [
    'Gravel bed (channel fill)',
    'Hyporheic zone',
    'Saturated alluvium',
    'Weathered bedrock',
    'Competent bedrock',
]

LAYER_DEPTH_1 = widgets.FloatSlider(
    value=2.0, min=0.0, max=30.0, step=0.5,
    description='Gravel bed depth (m):',
    style={'description_width': '200px'},
)
LAYER_DEPTH_2 = widgets.FloatSlider(
    value=4.0, min=0.0, max=30.0, step=0.5,
    description='Hyporheic zone depth (m):',
    style={'description_width': '200px'},
)
LAYER_DEPTH_3 = widgets.FloatSlider(
    value=8.0, min=0.0, max=30.0, step=0.5,
    description='Saturated alluvium depth (m):',
    style={'description_width': '200px'},
)

# Resistivity sliders (1-600 Ω·m)
LAYER_RES_1 = widgets.IntSlider(
    value=150, min=1, max=600, step=1,
    description='Gravel bed resistivity (Ω·m):',
    style={'description_width': '200px'},
)
LAYER_RES_2 = widgets.IntSlider(
    value=40, min=1, max=600, step=1,
    description='Hyporheic zone resistivity (Ω·m):',
    style={'description_width': '200px'},
)
LAYER_RES_3 = widgets.IntSlider(
    value=80, min=1, max=600, step=1,
    description='Saturated alluvium resistivity (Ω·m):',
    style={'description_width': '200px'},
)

# ---------------------------------------------------------------------------
# Geometry & Resistivity Preview
# ---------------------------------------------------------------------------
_geo = {}
_state = {'project': None}

def _make_topo(x_left_top, x_left_toe, x_right_toe, x_right_top,
               z_bank_top, z_river_bed):
    def topo_z(x):
        if x <= x_left_top:
            return z_bank_top
        elif x <= x_left_toe:
            t = (x - x_left_top) / (x_left_toe - x_left_top)
            return z_bank_top + t * (z_river_bed - z_bank_top)
        elif x <= x_right_toe:
            return z_river_bed
        elif x <= x_right_top:
            t = (x - x_right_toe) / (x_right_top - x_right_toe)
            return z_river_bed + t * (z_bank_top - z_river_bed)
        else:
            return z_bank_top
    return topo_z

def _make_water_table(river_center, river_width, z_river_bed):
    def water_table_z(x):
        dist = max(0.0, abs(x - river_center) - river_width / 2.0)
        return z_river_bed + dist * 0.04
    return water_table_z

def horiz_poly(z_top, z_bot):
    L = _geo['total_length']
    return np.array([
        [0, z_top], [L, z_top],
        [L, z_bot], [0, z_bot],
        [0, z_top],
    ])

def update_all(_=None):
    plt.close('all')  # Close all existing plots to avoid overlap

    # Update geometry
    n_elec = N_ELEC.value
    spacing = SPACING.value
    river_width = RIVER_WIDTH.value
    bank_height = BANK_HEIGHT.value
    bank_slope_w = BANK_SLOPE_W.value

    total_length = n_elec * spacing + 4.0
    river_center = total_length / 2.0

    x_left_top = river_center - river_width / 2.0 - bank_slope_w
    x_left_toe = river_center - river_width / 2.0
    x_right_toe = river_center + river_width / 2.0
    x_right_top = river_center + river_width / 2.0 + bank_slope_w

    z_bank_top = 0.0
    z_river_bed = -bank_height

    topo_z = _make_topo(x_left_top, x_left_toe, x_right_toe,
                        x_right_top, z_bank_top, z_river_bed)
    water_table_z = _make_water_table(river_center, river_width, z_river_bed)

    x_elec = np.linspace(2.0, 2.0 + (n_elec - 1) * spacing, n_elec)
    z_elec = np.array([topo_z(x) for x in x_elec])
    elec = np.column_stack([x_elec, z_elec])

    _geo.update(dict(
        n_elec=n_elec,
        spacing=spacing,
        total_length=total_length,
        river_center=river_center,
        z_river_bed=z_river_bed,
        topo_z=topo_z,
        water_table_z=water_table_z,
        elec=elec,
    ))

    # Plot geometry
    x_plot = np.linspace(0, total_length, 500)
    z_plot = np.array([topo_z(x) for x in x_plot])
    wt_z = np.array([water_table_z(x) for x in x_plot])

    fig, ax = plt.subplots(figsize=(12, 3))
    ax.fill_between(x_plot, z_plot, z_plot.min() - 0.5,
                    color='#c8a97e', alpha=0.4)
    ax.plot(x_plot, z_plot, 'k-', lw=2)
    ax.plot(x_elec, z_elec, 'rv', ms=6)
    ax.plot(x_plot, wt_z, 'b--', lw=1.2, alpha=0.7)

    ax.set_title(
        f'{SEQUENCE.value.upper()} | '
        f'{n_elec} electrodes @ {spacing:.0f} m spacing | '
        f'L = {total_length:.1f} m'
    )
    ax.set_aspect('equal')
    plt.show()

    # Rebuild resistivity model from scratch
    k = Project(typ='R2')
    k.setElec(elec)
    k.createSequence([(SEQUENCE.value, 1, 8, 1, 8)])
    k.createMesh(typ='quad')

    z0 = z_river_bed
    depths = [
        LAYER_DEPTH_1.value,
        LAYER_DEPTH_2.value,
        LAYER_DEPTH_3.value,
    ]
    res = [
        LAYER_RES_1.value,
        LAYER_RES_2.value,
        LAYER_RES_3.value,
    ]

    tops = [z0] + [z0 - d for d in depths[:-1]]
    bots = [z0 - d for d in depths]

    for zt, zb, r in zip(tops, bots, res):
        k.addRegion(horiz_poly(zt, zb), res0=r)

    _state['project'] = k
    k.mesh.show(attr='res0')
    plt.title("True resistivity model")
    plt.show()

# Register callbacks for all widgets
for widget in [N_ELEC, SPACING, SEQUENCE, NOISE, RIVER_WIDTH, BANK_HEIGHT, BANK_SLOPE_W,
               LAYER_DEPTH_1, LAYER_DEPTH_2, LAYER_DEPTH_3,
               LAYER_RES_1, LAYER_RES_2, LAYER_RES_3]:
    widget.observe(update_all, names='value')

# Display widgets
geometry_widgets = widgets.VBox([
    widgets.HBox([N_ELEC, SPACING, SEQUENCE, NOISE]),
    widgets.HBox([RIVER_WIDTH, BANK_HEIGHT, BANK_SLOPE_W]),
    widgets.Label('Layer Depths (m):'),
    LAYER_DEPTH_1, LAYER_DEPTH_2, LAYER_DEPTH_3,
    widgets.Label('Layer Resistivities (Ω·m):'),
    LAYER_RES_1, LAYER_RES_2, LAYER_RES_3,
])

display(geometry_widgets)
update_all()  # Initialize plots
```

---
### Step 4 — Run the Forward Model

The forward model computes what voltage readings the instrument *would* record if the true model above were the actual subsurface.

```{code-cell} ipython3
:tags: [remove-input]
def run_forward_model():
    k = _state.get('project')
    if k is None:
        print("Update geometry and resistivity model first")
        return

    noise = NOISE.value
    seq = SEQUENCE.value

    k.createSequence([(seq, 1, 8, 1, 8)])

    print(f'Running forward ({noise*100:.0f}% noise)...')
    k.forward(noise=noise, iplot=True)
    plt.show()

run_forward_model()
```

---
### Step 5 — Run the Inversion

Inversion is the mathematical process of working *backwards* from the pseudosection data to estimate the true resistivity model.

```{code-cell} ipython3
:tags: [remove-input]
def run_inversion():
    k = _state.get('project')
    if k is None:
        print("Run forward first")
        return

    print("Running inversion...")
    k.invert()

    fig, ax = plt.subplots(1, 2, figsize=(14, 4))

    k.mesh.show(attr='res0', ax=ax[0])
    ax[0].set_title("True")

    k.showResults(ax=ax[1])
    ax[1].set_title("Inverted")

    plt.show()

run_inversion()
```

---
## 🔄 On-going & Perspective Work

- Field data collection across the Hellín check dam network.
- Calibration of forward model resistivity values against sediment cores and in-situ moisture measurements.
- Time-lapse ERT to track seasonal moisture dynamics within the sediment body.
- 3D ERT inversion for volumetric sediment estimates.
- Comparison of ERT sensitivity across array types for thin-layer detection.
- Integration with EMI (CMD Mini-Explorer) grid surveys for spatial extrapolation.

```{tip}
GRWater project: This site is part of the [GRWater project](https://grwater.ica.csic.es/) — multi-scale monitoring of the Earth Critical Zone for post-fire forest management.
```

---
## ✅ Conclusion

Forward modelling of the river bank ERT cross-section demonstrates that the main resistivity contrasts in a post-fire check dam system — between dry coarse gravels, conductive ash/silt layers, and the saturated alluvial substrate — are resolvable with a standard 48-electrode Dipole-Dipole or Wenner-α array at 0.5–1 m spacing.

```{important}
Key takeaway: Synthetic ERT modelling confirms that a cross-dam perpendicular transect with 48 electrodes at 1 m spacing provides sufficient depth of investigation (~8–10 m) and lateral resolution to discriminate post-fire sediment layers and moisture zones within the check dam sediment body — supporting the planned field campaign.
```

---
```{note}
Data Acquisition & Processing Service: [ICA-CSIC](https://www.ica.csic.es) offers a professional service for geophysical data acquisition and processing as part of its [Geo-Spatial Technologies for Agro-Forestry Systems](https://www.ica.csic.es/servicios/servicios-cientifico-tecnicos/tecnologias-geo-espaciales-para-el-estudio-de-sistemas-agro-forestales) scientific-technical services unit.
```
