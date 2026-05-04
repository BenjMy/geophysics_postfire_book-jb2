---
title: "Electrical Resistivity Tomography (ERT)"
kernelspec:
  name: python3
  display_name: "Python 3 (Geophysics)"
  language: python
bibliography:
  - references.bib
authors:
  - name: Benjamin Mary
    email: benjamin.mary@ica.csic.es
    affiliations:
      - ICA-CSIC, Madrid, Spain
---

```{note} Learning Objectives
- Explain why a **4-electrode configuration** separates current injection from voltage measurement, and why this eliminates contact resistance errors
- Define **apparent resistivity** (ρₐ) including the role of the geometric factor K
- Compare common **electrode arrays** (Wenner, Schlumberger, Dipole-Dipole) in terms of sensitivity depth and typical use cases
- Describe the **ERT processing workflow** 
- Explain why inversion yields **a** plausible subsurface model rather than **the** unique solution
```


## What is ERT?

Previously, we saw that soil can be physically characterised by its electrical resistivity. Here, we extend this concept to electrical resistivity tomography. Electrical Resistivity Tomography (ERT) is a near-surface geophysical method that images the spatial distribution of the **electrical resistivity** (or its inverse, electrical conductivity) of the subsurface. Unlike borehole or soil-core measurements — which are localised and destructive — ERT is **non-invasive**, provides **2D and 3D spatial coverage**, and can be repeated over time to track **dynamic processes** (time-lapse, or 4D, ERT).

Key capabilities at a glance:
- Maps subsurface resistivity contrasts in **2D, 3D and through time** {cite}`dimech2022`
- Sensitive to changes in **soil water content, salinity, clay content and temperature** {cite}`telford1990,binley2005dc`
- Bridges the gap between sparse point sensors and large-scale remote sensing {cite}`carriere2022rs`


---



## Apparent resistivity and geometric Factor

In Electrical Resistivity Tomography (ERT) and other resistivity surveys, the **4-electrode method** is used to measure the **apparent resistivity (ρₐ)** of the subsurface. This method avoids the issue of **contact resistance** and accounts for the **geometric arrangement** of electrodes through the **geometric factor (K)**.


Using four electrodes separates the roles of **current injection** and **voltage measurement**:

1. **Current Electrodes (A, B):**
   - Inject current into the ground.
   - Contact resistance at these electrodes does not affect the voltage measurement because voltage is measured separately.

2. **Potential Electrodes (M, N):**
   - Measure the voltage drop in the subsurface.


```{figure} ../../assets/images/current-flow-lines-and-equipotential-lines-for-a-half-space
:name: fig-timeline-2
:width: 70%
:align: center
Source: Sharma, (1997).  
```


```{hint} Why four electrodes?
By separating these roles AB/MN, the measurement is **insensitive to contact resistance**, ensuring that ρₐ accurately represents the subsurface conditions.
Potential electrodes draw **negligible current** because they are connected to a high-impedance voltmeter. As a result, the voltage drop across their contact resistance is insignificant, and the measured voltage (Vₘₙ) reflects only the subsurface resistivity.

```

### Apparent resistivity (ρₐ)

**Apparent resistivity (ρₐ)** is the resistivity value calculated from field measurements using four electrodes. It is called "apparent" because it represents an **average resistivity** of the subsurface volume influenced by the electrode configuration. The subsurface is rarely homogeneous, so ρₐ is an effective value that simplifies interpretation.

The apparent resistivity is calculated using the formula:

$$
\rho_a = K \cdot \frac{V_{MN}}{I_{AB}}
$$

- **ρₐ:** Apparent resistivity (Ω·m)
- **K:** Geometric factor (m), which depends on the electrode arrangement
- **Vₘₙ:** Voltage measured between potential electrodes M and N (V)
- **IAB:** Current injected between current electrodes A and B (A)



---

## ERT survey design and sequence strategy

Choosing the right measurement sequence is fundamental: the electrode
configuration controls sensitivity, depth of investigation and resolution.

```{figure} https://img.youtube.com/vi/IlqWXWprC1g/hqdefault.jpg
:width: 50%
:align: center
Wenner Measurement (resistive body) — Credit [florianwagner4887](https://www.youtube.com/@florianwagner4887). [Watch on YouTube](https://www.youtube.com/watch?v=IlqWXWprC1g)
```
```{figure} https://img.youtube.com/vi/lt1qV-2d5Ps/hqdefault.jpg
:width: 50%
:align: center
Dipole-Dipole Measurement (resistive body) — Credit [florianwagner4887](https://www.youtube.com/@florianwagner4887). [Watch on YouTube](https://www.youtube.com/watch?v=lt1qV-2d5Ps)
```
```{figure} https://img.youtube.com/vi/h0fnnpU5Pf8/hqdefault.jpg
:width: 50%
:align: center
Schlumberger Measurement (conductive body) — Credit [florianwagner4887](https://www.youtube.com/@florianwagner4887). [Watch on YouTube](https://www.youtube.com/watch?v=h0fnnpU5Pf8)
```



| Array        | Sensitivity pattern         | Typical use case            |
|--------------|-----------------------------|-----------------------------|
| Wenner       | Shallow, symmetric          | Layered structures          |
| Schlumberger | Moderate depth, focused     | General-purpose profiling   |
| Dipole-Dipole| Deep, high lateral resolution | Fractures, heterogeneities |
| Pole-Dipole  | Asymmetric, deep            | Cross-borehole surveys      |

The optimal sequence, electrode spacing, and injection parameters are determined
through an **a-priori forward modelling** step: a plausible subsurface model is
assumed, synthetic data are computed, and array performance (resolution, signal
strength) is evaluated before deploying in the field
{cite}`binley2005dc,blanchy2020cageo`.

---

## ERT processing workflow

A standard ERT processing chain consists of the following steps:



1. **Data acquisition** – raw resistance measurements $R = \Delta V / I$
2. **Quality control** – reciprocal-error filtering, stacking, noise estimation
3. **Error modelling** – assign data uncertainties (needed for regularised inversion)
4. **Mesh generation** – finite-element or finite-difference mesh adapted to
   topography and electrode positions
5. **Inversion** – iterative minimisation of a cost function to recover the
   resistivity model that fits the data within its uncertainties
   {cite}`blanchy2020cageo`
6. **Time-lapse analysis** – independent or ratio/difference inversion to resolve
   subsurface changes over time {cite}`dimech2022`
   
```{mermaid}

flowchart TD
    A["Acquisition — R = ΔV/I"]
    B["✅ Quality Control — filtering · stacking"]
    C["📊 Error Modelling — data uncertainties"]
    D["🔲 Mesh — topography · electrodes"]
    E["🔁 Inversion"]
    F["⏱️ Time-lapse — difference · ratio"]

    A --> B --> C --> D --> E --> F
```


The open-source package **ResIPy** {cite}`blanchy2020cageo` (the Python API of
which is `resipy`) implements steps 2–6 in a single, user-friendly environment.

---

## What is inversion in geophysics?



```{admonition} 
:class: tip
We want to know what is **hidden underground** without digging. We place sensors
on the surface, record signals, and work backwards to find which underground
could have produced them. This is **inversion** — and it is the core mathematical
engine behind most geophysical imaging.
```

The opposite process — **forward modelling** — starts from a known underground and computes what the surface signal would look like. Inversion runs that logic in reverse: start from the measured signal, find the underground that explains it.

---

### 🧩 The model

The real underground is infinitely complex. We simplify it into a grid of cells —
like **pixels in an image** — each assigned a single value (e.g. resistivity, seismic velocity). This pixelated underground is what the computer actually works with.

The inversion algorithm then asks: *which combination of pixel values best reproduces the measurements I recorded at the surface?* It does this iteratively:

1. **Start** with an initial guess for the underground (often a uniform half-space)
2. **Compute** what signal that guess would produce at the surface (forward model)
3. **Compare** the computed signal to the real measurements — calculate the mismatch (the *misfit*)
4. **Adjust** the underground model to reduce the mismatch
5. **Repeat** until the computed and measured signals are close enough

```{figure} ../../assets/images/image1-2_Dimechetal.png
:name: fig-timeline-2_Dimechetal
:width: 75%
:align: center
Temporal dynamics of key soil properties following wildfire (after Dimech et al.). Shaded zones indicate the three intervention windows: emergency (red), early recovery (orange), and late recovery (green).
```

---

### 🔀 No unique answer

Here is the uncomfortable truth: many different undergrounds can produce **exactly
the same surface signal**. This is not a software bug or a limitation of the
instrument — it is a **mathematical certainty**, known as the *non-uniqueness problem*.



:::{warning}
The result of an inversion is **a** possible underground — not **the** real one.

Think of it this way: if you measure a total weight of 1 kg, the box could contain
one 1 kg object, or ten 100 g objects, or a thousand 1 g objects. The surface
measurement alone cannot tell you which.
:::

To make the result more trustworthy, geophysicists use **regularisation** — a mathematical way of adding prior knowledge or preferences to guide the solution. Common choices include:

- **Smoothness constraints**: prefer models where neighbouring cells are similar (avoids unrealistic sharp jumps)
- **Depth weighting**: account for the fact that deeper cells are less well constrained by surface data
- **Reference models**: anchor the inversion to a known starting point (e.g. from a borehole)


---

### ✅ What makes a good inversion result?

A result is considered reliable when:

- The **data misfit is low** — the forward model of the result closely reproduces the measured signal
- The **result is stable** — small changes in starting conditions do not produce wildly different images
- The **result is consistent** with independent information (borehole logs, soil cores, known geology)
- **Sensitivity analysis** confirms that the features of interest are actually resolved by the data, not artefacts of the algorithm

```{note}
In post-fire studies, this last point deserves special attention. Fire-induced changes in soil properties can be subtle, localised, and overprinted by natural variability. A feature visible in a geophysical image is only meaningful if it can be shown — through sensitivity tests or ground-truth sampling — that the data were actually capable of resolving it.
```



---

## ERT interpretation

Interpreting an inverted resistivity model requires combining geophysical
knowledge with site-specific information:

- **Absolute resistivity values** are compared to known lithological or soil
  ranges (e.g., saturated clays: 1–10 Ω·m; dry sands: 1000+ Ω·m)
- **Spatial patterns** identify structural features (layer boundaries,
  preferential flow paths, root zones)
- **Temporal changes** (time-lapse) are converted to changes in water content
  via petrophysical relationships, with explicit uncertainty propagation
  {cite}`tso2019wrr`
- **Integration with ancillary data** (soil cores, TDR probes, sap-flow sensors)
  is essential for unambiguous interpretation {cite}`mary2021vzj`

---

```{tip} Summary
You now understand:
- Electrical resistivity and its physical meaning
- Typical resistivity values for common earth materials
- How the 4-electrode measurement works and why it is necessary
- The Wenner geometric factor $K = 2\pi a$
```

---

```{bibliography}
:style: unsrt
```
