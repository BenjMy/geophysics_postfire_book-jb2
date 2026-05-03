---
title: Hellín — Soil Moisture at Catchment Scale
authors:
  - name: Benjamin Mary
    email: benjamin.mary@ica.csic.es
    affiliations:
      - ICA-CSIC, Madrid, Spain
---

# 💧 Hellín — Soil Moisture at Catchment Scale

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

**Site:** Hellín, Albacete, Spain
**Coordinates:** 38.52° N, 1.70° W
**Elevation:** ~600 m a.s.l.

```{code-cell} ipython3
:tags: [hide-input]
import folium
m = folium.Map(location=[38.52, -1.7], zoom_start=12, tiles='OpenStreetMap')
folium.Marker(
    [38.52, -1.7],
    popup=folium.Popup('<b>Hellin</b><br>Soil moisture catchment study', max_width=200),
    icon=folium.Icon(color='red', icon='info-sign')
).add_to(m)
m
```

---

## 🌍 Context

```{figure} ../../assets/images/hellin_context.jpg
:width: 60%
:align: center
:alt: Overview of the Hellín study catchment

Overview of the Hellín study area showing land use and post-fire vegetation recovery.
<!-- TODO: replace with actual image path -->
```

The Hellín area was affected by a major wildfire in recent years, leaving large tracts of formerly forested hillslopes bare and susceptible to erosion and runoff. The site complements the Agramón catchment by providing a paired comparison between a recovering burned area and an adjacent unburned control zone.

```{admonition} Paired catchment design
:class: note
The Hellín and Agramón sites together form a paired catchment experiment, enabling direct comparison of geophysical signatures between burned and reference conditions.
```

---

## ❓ Scientific Question

> **How does a wildfire event alter the subsurface hydraulic architecture of a catchment, and can time-lapse geophysics track the trajectory of recovery?**

Key sub-questions:

- Does fire-induced hydrophobicity persist below the surface and for how long?
- How do lateral subsurface flow pathways change after fire?
- Can ERT time-lapse imaging resolve the wetting front dynamics during storm events?

---

## 🛠️ Data Collected

```{list-table} Instruments and survey configuration
:header-rows: 1
:widths: 20 25 25 30

* - Instrument
  - Method
  - Configuration
  - Notes
* - CMD Mini-Explorer
  - Electromagnetic Induction (EMI)
  - 3 coil spacings: 0.32 / 0.71 / 1.18 m
  - Vertical dipole; grid survey 5 × 5 m
* - ERT system (ABEM)
  - Electrical Resistivity Tomography
  - Dipole-Dipole, 64 electrodes, 1 m spacing
  - Time-lapse: pre/post rainfall events
* - Soil moisture sensors (5TM)
  - Capacitance
  - 10 / 30 / 60 cm depth
  - 3 nests across burned / unburned zones
* - Portable rainfall simulator
  - Infiltration experiment
  - 0.5 m² plots
  - 6 plots × 3 burn severity classes
```

```{admonition} Data availability
:class: warning
Raw data are stored in the ICA-CSIC data repository. Contact the authors for access.
<!-- TODO: add DOI or data repository link -->
```

---

## 🔄 On-going & Perspective Work

- [ ] Time-lapse ERT monitoring during post-fire recovery (3-year programme)
- [ ] Stochastic inversion for uncertainty quantification
- [ ] Linkage with RUSLE-based erosion modelling
- [ ] Vegetation recovery mapping with multispectral UAV imagery

```{admonition} GRWater project
:class: tip
This site is part of the [GRWater project](https://grwater.ica.csic.es/) — multi-scale monitoring of the Earth Critical Zone for post-fire forest management.
```

---

## ✅ Conclusion

Time-lapse ERT surveys at Hellín reveal a clear contrast in subsurface moisture dynamics between burned and unburned hillslopes. The burned zone shows higher resistivity values near the surface, consistent with fire-induced hydrophobicity, while deeper horizons display greater moisture retention than the unburned control — suggesting altered preferential flow pathways.

```{admonition} Key takeaway
:class: important
Time-lapse ERT is a powerful tool for tracking the hydrological legacy of wildfire in Mediterranean catchments, revealing subsurface processes invisible to surface-based methods.
```

---

```{admonition} Data Acquisition & Processing Service
:class: note
[ICA-CSIC](https://www.ica.csic.es) offers a professional service for geophysical
data acquisition and processing as part of its
[Geo-Spatial Technologies for Agro-Forestry Systems](https://www.ica.csic.es/servicios/servicios-cientifico-tecnicos/tecnologias-geo-espaciales-para-el-estudio-de-sistemas-agro-forestales)
scientific-technical services unit.
```
