---
title: "Geophysical Methods for Post-fire Monitoring"
kernelspec:
  name: python3
  display_name: Python 3 (Geophysics)
  language: python
---

## Why Geophysics?

Geophysical methods allow us to image subsurface properties **non-invasively**, across **large areas**, and at **repeated time steps** — addressing exactly the limitations of traditional soil sampling described in the previous section. Rather than measuring soil directly, geophysics measures **physical contrasts** (electrical, mechanical, electromagnetic) that are sensitive to the properties we care about: water content, texture, organic matter, and structure.
```{admonition} Key principle
:class: tip
Geophysical measurements are **indirect**. They do not measure soil water content or clay content directly — they measure a physical signal (resistivity, wave velocity, radar travel time) that correlates with those properties. Interpreting geophysical data always requires some knowledge of the local geology and soil conditions.
```

---

## Overview of Methods

The table below summarises the main geophysical methods used in soil and post-fire studies, organised by the physical property they measure.

| Method | Physical property | Typical depth | Scale | Platform |
|---|---|---|---|---|
| ERT | Electrical resistivity | 0.5–20 m | Plot to hillslope | Ground |
| EMI | Electrical conductivity | 0.5–6 m | Field to catchment | Ground / UAV / Airborne |
| GPR | Dielectric permittivity | 0.1–5 m | Plot to field | Ground / UAV |
| Seismic refraction | P-wave velocity | 1–30 m | Plot to hillslope | Ground |
| MASW | S-wave velocity | 1–20 m | Plot to hillslope | Ground |
---

## Electrical Methods

### Electrical Resistivity Tomography (ERT)

ERT is the **workhorse method** for shallow subsurface imaging in soil studies. Four electrodes are inserted into the ground: two inject electrical current, two measure the resulting voltage. By repeating this measurement across dozens of electrode combinations along a line or grid, a 2D or 3D image of subsurface **resistivity** is reconstructed through inversion.
```{figure} ../../assets/images/ERT_dehesas.jpg
:name: fig-ert
:width: 75%
:align: center
ERT survey in a Mediterranean dehesa. Multi-electrode arrays measure apparent resistivity along transects to image soil structure and moisture distribution.
```

**What ERT is sensitive to:**
- Soil water content (strongly — wet soils are conductive, dry soils resistive)
- Clay content and texture

**Practical characteristics:**
- Depth of investigation: typically **0.5–20 m** depending on electrode spacing
- Spatial resolution: **centimetres to metres** depending on array geometry
- Survey time: **1/2–1 hour** per 2D transect with a modern multichannel system
- Limitation: requires good electrode–soil contact; dry or stony soils increase contact resistance

---

### Electromagnetic Induction (EMI)

EMI instruments generate a primary electromagnetic field that induces eddy currents in the subsurface. The secondary field produced by those currents is measured at the surface and related to the apparent **electrical conductivity** of the soil. Unlike ERT, EMI requires **no ground contact** — the instrument is simply carried or towed across the surface.
```{figure} ../../assets/images/EM_antenna_short.jpg
:name: fig-em-antenna
:width: 75%
:align: center
EMI antenna being towed across a burned area. The instrument measures apparent electrical conductivity continuously, enabling rapid spatial mapping at walking speed.
```

**What EMI is sensitive to:**
- Bulk electrical conductivity (same drivers as ERT: water, clay, salinity)
- Spatial patterns of soil variability at field to catchment scale
- Ash-induced salinity changes immediately after fire

**Practical characteristics:**
- Depth of investigation: **0.5–6 m** depending on coil geometry and frequency
- Spatial coverage: **several hectares per day** at walking speed
- No electrodes needed — ideal for stony or crusted post-fire surfaces
- Limitation: lower vertical resolution than ERT; sensitive to metal objects and infrastructure

---

## Electromagnetic Wave Methods

### Ground-Penetrating Radar (GPR)

GPR emits short pulses of high-frequency electromagnetic energy into the ground and records the time for reflections to return from subsurface interfaces. Travel time and signal amplitude depend on the **dielectric permittivity** of the material, which is strongly controlled by water content.

**What GPR is sensitive to:**
- Soil water content (via changes in dielectric permittivity)
- Sharp interfaces: surface crust, stone layers, bedrock top
- Pipe-like features and buried objects
- Soil horizon boundaries when contrast is sufficient

**Practical characteristics:**
- Depth of investigation: **0.1–5 m** (shallower in wet or clay-rich soils)
- Very high horizontal resolution — centimetre-scale with high-frequency antennas
- Fast data acquisition — continuous profiling at walking speed
- Limitation: strong signal attenuation in conductive (clay-rich, saline) soils; limited depth penetration post-fire if soils are wet

---

## Seismic Methods

### Seismic Refraction

A seismic source (hammer blow or small explosive) generates elastic waves that travel through the ground and are refracted at velocity contrasts between layers. First-arrival travel times recorded at a line of geophones are inverted to produce a **P-wave velocity** model.

**What seismic refraction reveals:**
- Depth to bedrock or a hard compacted layer
- Degree of **weathering** — weathered rock has much lower velocity than fresh rock
- Large-scale soil compaction changes post-fire (e.g., from heavy machinery or surface sealing)

**Practical characteristics:**
- Depth of investigation: **1–30 m** depending on source energy and geophone spread
- Good for detecting the soil–bedrock interface
- Limitation: requires a velocity increase with depth; cannot resolve low-velocity layers beneath faster ones

---

### MASW (Multichannel Analysis of Surface Waves)

MASW analyses the **dispersive properties of surface waves** (Rayleigh waves) to derive a shear-wave velocity (Vs) profile. Vs is sensitive to **soil stiffness and bulk density**, which change with compaction, organic matter loss, and structural degradation after fire.

**Practical characteristics:**
- Uses the same geophone spread as refraction — often acquired simultaneously
- Depth of investigation: **1–20 m**
- Particularly useful for detecting shallow compaction layers

---

## What can geophysics sense? — summary

The table below maps key post-fire soil properties to the methods potentially sensitive to them. 
```{admonition} A word of caution
:class: caution
Applying geophysical methods to post-fire soils is an **emerging field**. The sensitivities listed below are based on general geophysical principles and early case studies — they are **working hypotheses, not established facts**. Fire-induced changes in soil properties are complex, often co-occurring, and may produce competing or ambiguous geophysical signals. Empirical validation in burned soils remains limited.
```

| Soil property | ERT | EMI | GPR | Seismic | Hypothesised change after fire |
|---|---|---|---|---|---|
| Water content | 🟡 Likely high | 🟡 Likely high | 🟡 Likely high | ❓ Unclear | Probably reduced due to hydrophobicity — but variable |
| Clay content & texture | 🟡 Possibly moderate | 🟡 Possibly moderate | ⚪ Unlikely | ⚪ Unlikely | Likely unchanged short-term — but ash mixing uncertain |
| Bulk density / compaction | 🟠 Indirect, uncertain | 🟠 Indirect, uncertain | ⚪ Unlikely | 🟡 Possibly | May increase — evidence limited in post-fire contexts |
| Ion concentration (salinity) | 🟡 Likely sensitive | 🟡 Likely sensitive | ⚪ Unlikely | ⚪ Unlikely | May increase with ash leaching — timing poorly constrained |
| Char / ash layer | 🟠 Weakly, uncertain | 🟠 Weakly, uncertain | 🟠 Possibly — untested | ⚪ Unlikely | Present immediately post-fire — signature unclear |
| Organic matter loss | 🟠 Possibly indirect | 🟠 Possibly indirect | ⚪ Unlikely | ⚪ Unlikely | Strongly reduced — geophysical detectability unknown |
| Bedrock depth | 🟡 Moderate | ⚪ Unlikely | 🟡 Moderate | 🟡 Likely | Unchanged — but weathering front may shift over years |
| Hydrophobic layer | 🟠 Speculative | 🟠 Speculative | 🟠 Speculative | ⚪ Unlikely | Expected — no clear geophysical signature documented yet |

**Legend:**
🟡 Plausible sensitivity based on physical principles or analogous studies  
🟠 Possible but poorly constrained — requires field validation  
⚪ Unlikely or not demonstrated  
❓ Theoretically possible but direction and magnitude unknown
```{admonition} Open research questions
:class: seealso
- Can ERT or EMI reliably distinguish between a **dry hydrophobic layer** and a **dry pre-fire soil**?
- Does the **ash layer** produce a detectable geophysical contrast, or is it too thin and heterogeneous?
- How quickly do fire-induced geophysical signals **converge back** to pre-fire baselines?
- Are geophysical responses to fire **site-specific** (climate, soil type, fire severity) or generalisable?

These are among the core questions this project aims to address.
```

---

## Multi-Method Strategy

No single geophysical method answers all questions. In the GRwater project, we combine:

- **ERT** for high-resolution 2D profiles of water content and soil structure at plot scale
- **EMI** (ground and UAV) for rapid spatial mapping of conductivity patterns across burned and control catchments
- **GPR** for shallow interface detection and water content profiling
- **UAV LiDAR / SfM** for topographic change detection and erosion quantification
```{figure} ../../assets/images/concept_fig.png
:name: fig-concept
:width: 80%
:align: center
Conceptual figure illustrating how complementary geophysical methods detect changes in subsurface moisture pathways, soil structure, and surface topography following wildfire and restoration treatments.
```
```{admonition} Temporal monitoring
:class: seealso
By repeating surveys at 1, 3 and 8 years post-fire, we track the full temporal trajectory of soil recovery and assess the effectiveness of different restoration interventions — without disturbing the monitoring plots between campaigns.
```