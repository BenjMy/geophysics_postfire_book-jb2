---
title: "Post-fire & Geophysics: a good match?"
kernelspec:
  name: python3
  display_name: Python 3 (Geophysics)
  language: python
---


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
