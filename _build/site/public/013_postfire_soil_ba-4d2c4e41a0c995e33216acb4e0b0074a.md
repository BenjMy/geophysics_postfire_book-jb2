---
title: "Post-fire soil restoration"
kernelspec:
  name: python3
  display_name: Python 3 (Geophysics)
  language: python
---

# Post-fire Soil Restoration

Wildfires have profound and lasting effects on soil physical, chemical, and biological properties. Understanding these effects is critical for designing effective restoration strategies and monitoring ecosystem recovery over time. Geophysical methods — particularly electrical resistivity tomography (ERT) and electromagnetic induction (EMI) — provide non-invasive tools to track soil changes across large spatial extents and at multiple temporal scales {cite}`lucas-borja_changes_2021`.

## Main Threats to Post-fire Soils

After a wildfire, soils are exposed and highly vulnerable. The main processes threatening soil integrity are:

- **Soil erosion** — loss of the protective plant cover leads to accelerated erosion by rain splash and overland flow.
- **Organic matter loss** — combustion destroys soil organic matter, degrading aggregate stability and nutrient availability {cite}`lucas-borja_fostering_2024`.
- **Surface runoff** — hydrophobic compounds deposited by fire can create water-repellent layers that drastically increase runoff.
- **Altered water flow** — changes in soil porosity, structure and the creation of hydrophobic layers modify subsurface water pathways and recharge rates {cite}`kopp_perspectives_2023`.

```{admonition} Why does this matter?
:class: important
These processes are interconnected: higher runoff promotes erosion, which removes the organic-rich topsoil layer that is slowest to recover. Early intervention is therefore critical to break this feedback cycle.
```

## Remediation Strategies

Three broad intervention approaches are commonly applied after wildfires, depending on slope, severity, and restoration goals {cite}`lucas-borja_changes_2021`:

| Strategy | Mechanism | Typical application |
|---|---|---|
| **Mulching** | Protects soil surface from raindrop impact; retains moisture | Gentle to moderate slopes, early post-fire |
| **Erosion logs / barriers** | Slows overland flow; traps sediment | Steep slopes, gullies |
| **Bare soil** (control) | No intervention; natural recovery reference | Monitoring and comparison plots |

```{admonition} Choosing the right strategy
:class: tip
The choice of strategy depends on the time elapsed since the fire (see [Timeline of Actuation](#timeline-of-actuation)), slope gradient, rainfall regime, and the target ecosystem. Combining mulching with erosion barriers has shown synergistic effects in Mediterranean environments {cite}`lucas-borja_changes_2021`.
```

### Field Illustrations

The following images show typical post-fire field conditions and intervention techniques.

```{figure} ../../assets/images/errosion_barriers.jpg
:name: fig-erosion-barriers
:width: 70%
:align: center

Erosion log barriers installed on a burned slope to trap sediment and slow overland flow.
```

```{figure} ../../assets/images/field_Albacete.jpg
:name: fig-field-albacete
:width: 70%
:align: center

Field site in Albacete showing post-fire soil conditions with sparse vegetation recovery.
```

```{figure} ../../assets/images/agramon-1.png
:name: fig-agramon
:width: 70%
:align: center

Aerial view of the Agramon study site, showing the spatial extent of fire damage and recovery patches.
```

## The Critical Zone Framework

Post-fire soil restoration is best understood within the **Critical Zone** (CZ) framework, which considers the thin layer of Earth from the top of the vegetation canopy down to fresh bedrock as a single, integrated system {cite}`kopp_perspectives_2023`.

```{figure} ./assets/images/ECZ.jpg
:name: fig-critical-zone
:width: 80%
:align: center

Figure from {cite}`kopp_perspectives_2023`: the critical zone at nested scales from landscape to microscopic. The GRwater project investigates water fluxes from landscape to local scale in relation to biodiversity and ecosystem restoration.
```

```{admonition} Critical Zone and fire
:class: note
Wildfires represent one of the most intense and rapid disturbances to the Critical Zone. They alter the physical structure, biological community, and chemical composition of soils simultaneously, making post-fire landscapes ideal natural experiments for studying CZ dynamics {cite}`kopp_perspectives_2023`.
```

## Geophysical Monitoring

Geophysical methods allow us to image subsurface properties non-invasively over large areas and repeated time steps. Two methods are particularly relevant for post-fire monitoring:

- **Electrical Resistivity Tomography (ERT)** — resolves 2-D or 3-D resistivity distributions sensitive to soil water content, texture and structure (see {numref}`fig-ert`).
- **Electromagnetic Induction (EMI)** — rapidly maps apparent electrical conductivity over large areas (see {numref}`fig-em-antenna`).

```{figure} ../../assets/images/ERT_dehesas.jpg
:name: fig-ert
:width: 75%
:align: center

ERT survey in a Mediterranean dehesa. Multi-electrode arrays measure apparent resistivity along transects to image soil structure and moisture distribution.
```

```{figure} ../../assets/images/EM_antenna_short.jpg
:name: fig-em-antenna
:width: 75%
:align: center

EMI antenna being towed across a burned area. The instrument measures apparent electrical conductivity continuously, enabling rapid spatial mapping.
```

```{figure} ../../assets/images/concept_fig.png
:name: fig-concept
:width: 80%
:align: center

Conceptual figure illustrating how ERT and EMI can detect changes in subsurface moisture pathways and soil structure following wildfire and restoration treatments.
```

### What Can Geophysics Sense?

Geophysical methods respond to physical and chemical soil properties that change following wildfire and during recovery. The table below summarises the main targets:

| Soil property | ERT sensitive? | EMI sensitive? | Change after fire |
|---|---|---|---|
| Water content | ✅ High | ✅ High | Reduced (hydrophobicity) |
| Clay content & texture | ✅ Moderate | ✅ Moderate | Unchanged short-term |
| Organic matter | ✅ Moderate | ✅ Moderate | Strongly reduced |
| Bulk density / compaction | ✅ Indirect | ✅ Indirect | Often increased |
| Ion concentration (salinity) | ✅ High | ✅ High | May increase post-ash |
| Char / ash layer | ✅ Low | ✅ Low | Present immediately post-fire |

```{admonition} Key insight
:class: seealso
By repeating geophysical surveys at 1, 3 and 8 years post-fire, we can track the temporal trajectory of soil recovery and assess the effectiveness of different restoration interventions — without disturbing the plots we are monitoring.
```

(timeline-of-actuation)=
## Timeline of Actuation

Restoration tools should be deployed according to the phase of post-fire regeneration. The three critical windows are:

```{list-table} Recommended interventions by post-fire phase
:header-rows: 1
:name: table-timeline

* - Phase
  - Timing
  - Priority actions
  - Geophysical monitoring
* - **Emergency**
  - Immediately after fire
  - Erosion barriers, mulching on steep slopes, seed application
  - Baseline ERT and EMI surveys (reference state)
* - **Early recovery**
  - ~3 years post-fire
  - Maintain barriers, selective planting, monitor water repellency
  - Repeat surveys; detect moisture redistribution
* - **Late recovery**
  - ~8 years post-fire
  - Remove barriers if vegetation established; assess long-term C sequestration
  - Full 3-D ERT inversion to assess deep soil recovery
```

```{admonition} Long-term perspective
:class: warning
Full ecosystem recovery after severe wildfire can take decades. The 8-year window captures the transition from active restoration to natural succession, but geophysical monitoring should ideally continue beyond this horizon to capture deep soil and hydrological recovery {cite}`lucas-borja_fostering_2024`.
```

The figures below illustrate the typical trajectory of soil property recovery after wildfire and the recommended timing of interventions:

```{figure} ../../assets/images/image1-2_Dimechetal.png
:name: fig-timeline-1
:width: 75%
:align: center

Temporal dynamics of key soil properties following wildfire (after Dimech et al.). Shaded zones indicate the three intervention windows: emergency (red), early recovery (orange), and late recovery (green).
```

```{figure} ../../assets/images/image1-5_Dimechetal.png
:name: fig-timeline-2
:width: 75%
:align: center

Comparative effectiveness of restoration strategies across post-fire recovery phases (after Dimech et al.).
```

## Project Context: fBBVA

This research is supported by the fBBVA programme. The project logo and further details are shown below.

```{figure} ../../assets/images/fbbva.png
:name: fig-fbbva
:width: 30%
:align: left

Fundación BBVA project logo.
```

The study site at Agramon (Albacete, SE Spain) was severely burned in 2022 and represents a typical Mediterranean pine forest on calcareous soils. The video below gives an aerial overview of the site.


:::{figure} ../../assets/images/agramon_compressed.mp4
An embedded video with a caption!
:::


:::{iframe} https://www.youtube.com/watch?v=wfJ62rz0EsU
:width: 100%
ResIPy Python API - Getting Started 
:::


:::{iframe} https://www.youtube.com/watch?v=48VN_e8J2kc
:width: 100%
Introduction to 2D forward modeling with ResIPy (beginner to professional) 
:::

:::{iframe} https://www.youtube.com/watch?v=OjZlRZ7QeMk
:width: 100%
Introduction to 2D inversion with ResIPy 
:::







---

```{admonition} Summary
:class: tip
In this introduction you have learned:
- The **main threats** to soil after wildfire (erosion, organic matter loss, runoff, altered water flow).
- The three main **remediation strategies** and when to apply them.
- How the **Critical Zone framework** provides a holistic view of post-fire soil dynamics.
- What **geophysical methods** can and cannot detect in post-fire soils.
- The **three-phase timeline** (1, 3, 8 years) that guides monitoring and intervention decisions.

Next notebook: [Soil Physical Properties and Ohm's Law](012_geophysics_basics_ohmslaw.md).
```

## References

The key references used throughout this notebook are:

- {cite}`kopp_perspectives_2023` — critical zone perspectives for managing changing forests.
- {cite}`lucas-borja_changes_2021` — changes in ecosystem properties after post-fire management strategies in wildfire-affected Mediterranean forests.
- {cite}`lucas-borja_fostering_2024` — fostering biodiversity research in post-fire biology.

```{bibliography}
:filter: docname in docnames
```
