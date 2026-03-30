---
title: Exercise 2 ➡️ ERT Survey Design
authors:
  - name: Benjamin Mary
    email: benjamin.mary@ica.csic.es
    affiliations:
      - ICA-CSIC, Madrid, Spain
---
````{admonition} Why forward modelling matters
:class: tip
Before going to the field, forward modelling allows you to simulate ERT data on a synthetic subsurface model. This is a critical step to:
- Choose appropriate electrode spacing and array type
- Assess the sensitivity of the survey to the target anomaly
- Anticipate potential artefacts or resolution limits
- Optimize the survey design before committing resources
````

---

## Part 1 — Create a layered resistivity model

Using ResIPy, build a three-layer subsurface model representing the following stratigraphy:

| Layer | Material | Depth (m) | Resistivity (Ω·m) |
|---|---|---|---|
| 1 | Ash | 0 to −0.5 | 1500 |
| 2 | Soil | −0.5 to −2.0 | 150 |
| 3 | Bedrock | −2.0 to −5.0 | 1000 |

1. Define the geometry of each layer as a polygon.
2. Assign a resistivity value to each region.
3. Run a forward model with **5% Gaussian noise**.
4. Invert the synthetic data and compare the result to the true model.
````{dropdown} Answer — Expected output
```{figure} ../assets/images/conceptual_model_layers.png
:width: 100%
:align: center
:alt: Conceptual layered model with ash, soil and bedrock
Conceptual layered model: ash (top), soil (middle), bedrock (bottom).
```
````
````{dropdown} Solution with ResIPy GUI
1. Open ResIPy and create a new project.
2. Go to **Model > Add Region** and draw each layer polygon manually.
3. Assign resistivity values in the region properties panel.
4. Run **Forward > Simulate** with noise set to 5%.
5. Run **Inversion** and inspect results with **Show Results**.
````
````{dropdown} Solution with ResIPy — Python code
```python
import numpy as np

x_min, x_max = -1, 12
z1 = -0.5   # base of ash layer
z2 = -2.0   # base of soil layer
z3 = -5.0   # bottom of model (bedrock)

# Layer polygons (closed, counter-clockwise)
layer_ash = np.array([
    [x_min, 0],
    [x_max, 0],
    [x_max, z1],
    [x_min, z1],
    [x_min, 0]
])

layer_soil = np.array([
    [x_min, z1],
    [x_max, z1],
    [x_max, z2],
    [x_min, z2],
    [x_min, z1]
])

layer_bedrock = np.array([
    [x_min, z2],
    [x_max, z2],
    [x_max, z3],
    [x_min, z3],
    [x_min, z2]
])

# Assign resistivity values to each region
k.addRegion(layer_ash,     res0=1500, iplot=True)  # Ash — high resistivity
k.addRegion(layer_soil,    res0=150,  iplot=True)  # Soil — moderate resistivity
k.addRegion(layer_bedrock, res0=1000, iplot=True)  # Bedrock — resistive

# Forward modelling with 5% noise
k.forward(noise=0.05, iplot=True)

# Inversion
k.invert()

# Visualise results
k.showResults(index=0, electrodes=False, hor_cbar=False)  # True model
k.showResults(index=1, electrodes=False)                  # Inverted model
```
````

---

## Part 2 — Optimal electrode spacing for a target anomaly

The figure below shows a subsurface anomaly you want to image.
````{figure} ../assets/images/design_electrode_geom.png
:width: 100%
:align: center
:alt: Target anomaly geometry for electrode spacing design
Target anomaly used to guide electrode spacing selection.
````

Based on this geometry, answer the following questions:

1. What electrode spacing `a` would you choose to resolve this anomaly? Justify your choice.
2. How does the **depth of investigation** relate to electrode spacing for a Wenner array?
3. What is the trade-off between using a **small** vs **large** electrode spacing?
````{dropdown} Answer
1. Electrode spacing should be on the order of the anomaly's **lateral dimension or smaller** — typically `a ≤ target width / 2` to ensure adequate horizontal resolution.
2. For a Wenner array, the approximate depth of investigation is **z ≈ 0.5 × a** (rule of thumb). Larger spacing → greater depth, but lower resolution.
3. Trade-off:
   - **Small spacing:** high resolution near surface, limited depth penetration
   - **Large spacing:** greater depth, but smoothed, less resolved anomalies
````

---

## Part 3 — Create a 2D mesh

Using ResIPy, generate a 2D finite-element mesh suitable for forward modelling of the geometry defined in Part 1.

1. What mesh parameters control resolution near the surface vs at depth?
2. How should mesh density be adjusted near electrode positions?
3. Run the mesh and verify it visually before launching the forward model.
````{dropdown} Answer
- Use **finer elements near the surface** and electrode positions to capture sharp gradients.
- Increase element size with depth to reduce computation time without sacrificing accuracy.
- In ResIPy: `k.createMesh(typ='trian', surface=..., cl=0.1, cl_factor=5)` — `cl` controls surface element size, `cl_factor` controls coarsening at depth.
- Always inspect the mesh with `k.showMesh()` before running forward or inverse models.
````