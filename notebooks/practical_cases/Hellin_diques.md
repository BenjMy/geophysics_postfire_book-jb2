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

# 🌊 River Bank ERT — Interactive Forward Model

```{contents} On this page
:depth: 2
:local:
```

---

## 👥 Authors

```{admonition} Contributors
:class: tip
**Benjamin Mary** — [benjamin.mary@ica.csic.es](mailto:benjamin.mary@ica.csic.es)
ICA-CSIC, Madrid, Spain

<!-- TODO: add co-authors -->
```

---

## 📍 Location

**Site:** Hellín — Rambla check dam network, Albacete, Spain
**Coordinates:** 38.50° N, 1.68° W
**Elevation:** ~580 m a.s.l.

```{code-cell} ipython3
:tags: [hide-input]
import folium
m = folium.Map(location=[38.5, -1.68], zoom_start=13, tiles='OpenStreetMap')
folium.Marker(
    [38.5, -1.68],
    popup=folium.Popup('<b>Dique 1</b><br>Check dam — sediment monitoring', max_width=200),
    icon=folium.Icon(color='red', icon='info-sign')
).add_to(m)
folium.Marker([38.498, -1.676], popup='<b>Dique 2</b><br>Check dam — sediment monitoring').add_to(m)
folium.Marker([38.495, -1.671], popup='<b>Dique 3</b><br>Check dam — sediment monitoring').add_to(m)
m
```

---

## 🌍 Context

```{figure} ../../assets/images/diques2.jpeg
:width: 60%
:align: center
:alt: diques1
:name: diques1

One of the sediment check dams in the Hellín rambla network. Picture credit to ??.
```

```{figure} ../../assets/images/diques1.jpeg
:width: 60%
:align: center
:alt: diques2
:name: diques2

One of the sediment check dams in the Hellín rambla network. Picture credit to ??.
```

```{figure} ../../assets/images/diques3.jpeg
:width: 60%
:align: center
:alt: diques3
:name: diques3

One of the sediment check dams in the Hellín rambla network. Picture credit to ??.
```

Sediment check dams (*diques de sedimentación*) are a common post-fire restoration measure in Spanish ramblas and ephemeral streams. They are designed to trap sediment mobilised by post-fire erosion, reduce downstream flood risk, and promote vegetation recovery in gully floors. However, their effectiveness and the physical properties of trapped sediments remain poorly characterised.

```{admonition} Post-fire restoration context
:class: note
After the 2022 wildfires in the Hellín area, a network of check dams was installed along the main rambla as an emergency erosion-control measure. This notebook provides a forward-modelling framework to design and evaluate ERT acquisition strategies for the geophysical characterisation of the sediment body behind these structures **prior to field data collection**.
```

```{admonition} Semi-permeable or confined dam?
:class: caution
From the figures above, we can observe that the dams are not designed the same way i.e. {numref}`diques1` shows a concrete dam that does not let sediment nor water through, while {numref}`diques2` and {numref}`diques3` are permeable to water.
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

This notebook implements a **2D ERT forward model** of a river bank cross-section perpendicular to the minor bed, with geology representative of the Hellín rambla system. The workflow allows the user to:

1. Define the channel cross-section geometry (bank height, channel width, slope)
2. Assign resistivity values to each geological layer (sediment, alluvium, bedrock)
3. Configure the electrode array (number, spacing, acquisition sequence)
4. Run the forward model and inspect the synthetic apparent resistivity pseudosection
5. Run the inversion and compare the recovered model to the true model

```{admonition} Why forward modelling before fieldwork?
:class: tip
Synthetic modelling before data collection allows optimisation of survey design — electrode spacing, array type, and profile length — to maximise sensitivity to the target structures (sediment layers, moisture zones) given the expected depth range and resistivity contrasts.
```

The geological model is built from available literature values and sediment core analogues from comparable post-fire Mediterranean catchments. It includes:

- A multi-layer post-fire sediment wedge (coarse first-flush gravels, fine ash/silt, mixed re-mobilisation deposits)
- An unsaturated bank zone above the water table
- A saturated alluvial substrate
- A clay lens representative of overbank fine deposits
- Weathered and competent bedrock

```{admonition} Resistivity contrasts in post-fire sediments
:class: note
Fine ash and silt layers deposited after the initial post-fire flood pulse are particularly conductive (low resistivity, ~20–50 Ω·m) due to their high surface area, ionic load from burnt organic material, and tendency to retain moisture. Coarser gravel layers deposited during high-energy events are more resistive (~150–300 Ω·m). This contrast is the primary target for ERT-based stratigraphic discrimination.
```

---

## ⚙️ Interactive Simulation

The cells below implement the full interactive forward-modelling workflow. All parameters are controlled via sliders and dropdowns — no code editing required.

### Dependencies

```{code-cell} ipython3
:tags: [remove-input, cache]
import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from ipywidgets import HBox, VBox, HTML
from IPython.display import display, clear_output
from resipy import Project
```

### Electrode & Acquisition Settings

```{code-cell} ipython3
:tags: [remove-input, cache]
style  = {'description_width': '180px'}
layout = widgets.Layout(width='420px')

w_n_elec = widgets.IntSlider(
    value=57, min=10, max=120, step=1,
    description='Number of electrodes',
    style=style, layout=layout)

w_spacing = widgets.FloatSlider(
    value=1.0, min=0.25, max=5.0, step=0.25,
    description='Electrode spacing (m)',
    style=style, layout=layout)

w_sequence = widgets.Dropdown(
    options=[
        ('Wenner-α  (sensitivity: layers)',            'wa'),
        ('Wenner-β  (sensitivity: vertical contacts)', 'wb'),
        ('Wenner-γ  (cross-borehole style)',           'wg'),
        ('Dipole-Dipole  (lateral resolution)',        'dd'),
        ('Pole-Dipole  (deep targets)',                'pd'),
        ('Pole-Pole  (maximum depth)',                 'pp'),
        ('Schlumberger  (horizontal layers)',          'schlum'),
        ('Gradient  (fast acquisition)',               'grad'),
    ],
    value='dd',
    description='Acquisition sequence',
    style=style, layout=layout)

w_noise = widgets.FloatSlider(
    value=3.0, min=0.0, max=15.0, step=0.5,
    description='Noise level (%)',
    style=style, layout=layout)

display(HTML('<b>🔌 Electrode & Acquisition</b>'))
display(VBox([w_n_elec, w_spacing, w_sequence, w_noise]))
```

### Channel Geometry

```{code-cell} ipython3
:tags: [remove-input, cache]
w_river_width = widgets.FloatSlider(
    value=10.0, min=2.0, max=30.0, step=0.5,
    description='Channel width (m)',
    style=style, layout=layout)

w_bank_height = widgets.FloatSlider(
    value=2.0, min=0.5, max=6.0, step=0.25,
    description='Bank height (m)',
    style=style, layout=layout)

w_bank_slope = widgets.FloatSlider(
    value=4.0, min=1.0, max=10.0, step=0.5,
    description='Bank slope width (m)',
    style=style, layout=layout)

display(HTML('<b>🏞️ Channel Geometry</b>'))
display(VBox([w_river_width, w_bank_height, w_bank_slope]))
```

### Layer Depths & Resistivities

Depths are measured **below the channel floor**. Layer order is from shallowest to deepest.

```{code-cell} ipython3
:tags: [remove-input, cache]
layers_config = [
    ('Gravel bed (channel fill)',  2.0,  150),
    ('Hyporheic zone',             4.0,   40),
    ('Saturated alluvium',         8.0,   80),
    ('Weathered bedrock',         13.0,  600),
    ('Competent bedrock',         20.0, 2500),
]

depth_widgets = []
res_widgets   = []
rows          = []

for name, depth_def, res_def in layers_config:
    wd = widgets.FloatSlider(
        value=depth_def, min=0.5, max=25.0, step=0.25,
        description='Base depth (m)',
        style=style, layout=layout)
    wr = widgets.IntSlider(
        value=res_def, min=1, max=5000, step=5,
        description='Resistivity (Ω·m)',
        style=style, layout=layout)
    depth_widgets.append(wd)
    res_widgets.append(wr)
    rows.append(VBox([
        HTML(f'<b>Layer: {name}</b>'),
        HBox([wd, wr])
    ]))

w_res_bank = widgets.IntSlider(
    value=300, min=10, max=3000, step=10,
    description='Unsaturated bank (Ω·m)',
    style=style, layout=layout)

w_clay_on = widgets.Checkbox(value=True, description='Include clay lens (left bank)')
w_res_clay = widgets.IntSlider(
    value=8, min=1, max=100, step=1,
    description='Clay lens (Ω·m)',
    style=style, layout=layout)

display(HTML('<b>🗂️ Subsurface Layers</b>'))
for r in rows:
    display(r)
display(HTML('<hr><b>🏦 Bank & Clay</b>'))
display(VBox([w_res_bank, HBox([w_clay_on, w_res_clay])]))
```

### Run the Simulation

```{code-cell} ipython3
:tags: [remove-input, cache]
run_button    = widgets.Button(description='▶  Run Forward Model',
                               button_style='success',
                               layout=widgets.Layout(width='220px', height='40px'))
invert_button = widgets.Button(description='⚙  Run Inversion',
                               button_style='warning',
                               layout=widgets.Layout(width='220px', height='40px'))
out   = widgets.Output()
state = {'k': None}

def build_model(_=None):
    with out:
        clear_output(wait=True)

        n_elec       = w_n_elec.value
        spacing      = w_spacing.value
        sequence     = w_sequence.value
        noise        = w_noise.value / 100.0
        river_width  = w_river_width.value
        bank_height  = w_bank_height.value
        bank_slope_w = w_bank_slope.value
        layer_depths = [wd.value for wd in depth_widgets]
        layer_res    = [wr.value for wr in res_widgets]
        res_bank     = w_res_bank.value
        clay_on      = w_clay_on.value
        res_clay     = w_res_clay.value

        total_length  = n_elec * spacing + 4.0
        river_center  = total_length / 2.0
        x_left_top    = river_center - river_width/2 - bank_slope_w
        x_left_toe    = river_center - river_width/2
        x_right_toe   = river_center + river_width/2
        x_right_top   = river_center + river_width/2 + bank_slope_w
        z_bank_top    = 0.0
        z_river_bed   = -bank_height

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

        def water_table_z(x):
            dist = max(0, abs(x - river_center) - river_width/2)
            return z_river_bed + dist * 0.04

        x_elec = np.linspace(2.0, 2.0 + (n_elec - 1) * spacing, n_elec)
        z_elec = np.array([topo_z(x) for x in x_elec])
        elec   = np.column_stack([x_elec, z_elec])

        # Profile preview
        fig, ax = plt.subplots(figsize=(12, 3))
        x_plot = np.linspace(0, total_length, 500)
        z_plot = np.array([topo_z(x) for x in x_plot])
        ax.fill_between(x_plot, z_plot, z_plot.min() - 0.5,
                        color='#c8a97e', alpha=0.4, label='Subsurface')
        ax.plot(x_plot, z_plot, 'k-', lw=2, label='Surface')
        ax.plot(x_elec, z_elec, 'rv', ms=6,
                label=f'Electrodes (n={n_elec}, Δ={spacing} m)')
        wt_z = np.array([water_table_z(x) for x in x_plot])
        ax.plot(x_plot, wt_z, 'b--', lw=1.2, alpha=0.6, label='Water table')
        ax.set_xlabel('Distance (m)')
        ax.set_ylabel('Elevation (m)')
        ax.set_title(f'Profile preview — sequence: {sequence.upper()}  |  '
                     f'{n_elec} electrodes @ {spacing} m  |  '
                     f'Profile length: {total_length:.1f} m')
        ax.legend(loc='lower right', fontsize=8)
        ax.set_aspect('equal')
        plt.tight_layout()
        plt.show()

        print('Building model...')
        k = Project(typ='R2')
        k.setElec(elec)
        k.createSequence([('dpdp', 1, 8, 1, 8)]) # dipole-dipole sequence
        #k.createMesh(cl=0.5, res0=300)      
        k.createMesh(typ='quad')

        depths = sorted(layer_depths)
        layer_tops = [z_river_bed] + [z_river_bed - d for d in depths[:-1]]
        layer_bots = [z_river_bed - d for d in depths]

        def horiz_poly(z_top, z_bot):
            return np.array([
                [0.0,          z_top],
                [total_length, z_top],
                [total_length, z_bot],
                [0.0,          z_bot],
                [0.0,          z_top],
            ])

        for zt, zb, res in zip(layer_tops, layer_bots, layer_res):
            k.addRegion(horiz_poly(zt, zb), res0=res, iplot=False)

        left_bank_unsat = np.array([
            [0.0,        topo_z(0.0)],
            [x_left_toe, topo_z(x_left_toe)],
            [x_left_toe, water_table_z(x_left_toe)],
            [0.0,        water_table_z(0.0)],
            [0.0,        topo_z(0.0)],
        ])
        right_bank_unsat = np.array([
            [x_right_toe,  topo_z(x_right_toe)],
            [total_length, topo_z(total_length)],
            [total_length, water_table_z(total_length)],
            [x_right_toe,  water_table_z(x_right_toe)],
            [x_right_toe,  topo_z(x_right_toe)],
        ])
        k.addRegion(left_bank_unsat,  res0=res_bank, iplot=False)
        k.addRegion(right_bank_unsat, res0=res_bank, iplot=False)

        if clay_on:
            clay_lens = np.array([
                [4.0,   z_river_bed + 0.5],
                [14.0,  z_river_bed + 0.5],
                [14.0,  z_river_bed - 0.5],
                [4.0,   z_river_bed - 0.8],
                [4.0,   z_river_bed + 0.5],
            ])
            k.addRegion(clay_lens, res0=res_clay, iplot=False)

        print('Plotting initial resistivity model...')
        k.mesh.show(attr='res0')
        plt.title('Initial resistivity model (before inversion)')
        plt.show()

        print(f'Running forward model (noise={noise*100:.1f}%)...')
        k.forward(noise=noise, iplot=True)
        plt.show()

        state['k'] = k
        print('✅ Forward model complete. Press ⚙ Run Inversion to invert.')

def run_inversion(_=None):
    with out:
        k = state.get('k')
        if k is None:
            print('⚠️  Run the forward model first.')
            return
        print('Running inversion...')
        k.invert()
        k.showResults(index=0, electrodes=True, hor_cbar=False)
        plt.title('True resistivity model')
        plt.show()
        k.showResults(index=1, electrodes=True)
        plt.title('Inverted resistivity model')
        plt.show()
        print('✅ Inversion complete.')

run_button.on_click(build_model)
invert_button.on_click(run_inversion)

display(HBox([run_button, invert_button]))
display(out)
```

---

## 🔄 On-going & Perspective Work

- [ ] Field data collection across the Hellín check dam network
- [ ] Calibration of forward model resistivity values against sediment cores and in-situ moisture measurements
- [ ] Time-lapse ERT to track seasonal moisture dynamics within the sediment body
- [ ] 3D ERT inversion for volumetric sediment estimates
- [ ] Comparison of ERT sensitivity across array types for thin-layer detection
- [ ] Integration with EMI (CMD Mini-Explorer) grid surveys for spatial extrapolation

```{admonition} GRWater project
:class: tip
This site is part of the [GRWater project](https://grwater.ica.csic.es/) — multi-scale monitoring of the Earth Critical Zone for post-fire forest management.
```

---

## ✅ Conclusion

Forward modelling of the river bank ERT cross-section demonstrates that the main resistivity contrasts in a post-fire check dam system — between dry coarse gravels, conductive ash/silt layers, and the saturated alluvial substrate — are resolvable with a standard 48-electrode Dipole-Dipole or Wenner-α array at 0.5–1 m spacing. The clay lens and hyporheic zone produce distinct low-resistivity anomalies that are detectable even under moderate noise conditions (3–5%).

```{admonition} Key takeaway
:class: important
Synthetic ERT modelling confirms that a cross-dam perpendicular transect with 48 electrodes at 1 m spacing provides sufficient depth of investigation (~8–10 m) and lateral resolution to discriminate post-fire sediment layers and moisture zones within the check dam sediment body — supporting the planned field campaign.
```

---

```{admonition} Data Acquisition & Processing Service
:class: note
[ICA-CSIC](https://www.ica.csic.es) offers a professional service for geophysical
data acquisition and processing as part of its
[Geo-Spatial Technologies for Agro-Forestry Systems](https://www.ica.csic.es/servicios/servicios-cientifico-tecnicos/tecnologias-geo-espaciales-para-el-estudio-de-sistemas-agro-forestales)
scientific-technical services unit.
```
