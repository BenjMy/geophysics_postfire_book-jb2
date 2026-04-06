---
title: Agramón — ERT
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


# 💧 Agramón — Depth of the sedimentation layer

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

**Hector Nieto**
ICA-CSIC, Madrid, Spain
<!-- TODO: add co-authors -->
```

---

## 📍 Location

**Site:** Agramón, Albacete, Spain
**Coordinates:** 38.43° N, 1.55° W
**Elevation:** ~550 m a.s.l.

```{code-cell} ipython3
:tags: [hide-input]
import folium
m = folium.Map(location=[38.43, -1.55], zoom_start=12, tiles='OpenStreetMap')
folium.Marker(
    [38.43, -1.55],
    popup=folium.Popup('<b>Agramon</b><br>Soil moisture catchment study', max_width=200),
    icon=folium.Icon(color='red', icon='info-sign')
).add_to(m)
m
```

---

## 🌍 Context


The Agramón catchment is located in a semi-arid region of southeastern Spain heavily impacted by recurring drought and wildfire events. Post-fire recovery of forest ecosystems in this area is tightly coupled to soil water availability, which controls vegetation re-establishment and erosion dynamics.

```{admonition} Why this site?
:class: note
Agramón offers a representative example of a Mediterranean catchment under combined fire and drought stress. Its relatively small size makes it tractable for multi-scale geophysical monitoring.
```


```{figure} ../../assets/images/ERT_Agramon_October2025_1.jpg
:width: 60%
:align: center
:alt: ERT_Agramon_October2025_1

ERT_Agramon_October2025_1
```

```{figure} ../../assets/images/ERT_Agramon_October2025_2.jpg
:width: 60%
:align: center
:alt: ERT_Agramon_October2025_2

ERT_Agramon_October2025_2
```





---

## ❓ Scientific Question

> **How does soil moisture vary spatially and temporally across a fire-affected catchment, and what geophysical proxies best capture this variability?**

Key sub-questions:

- Can ERT surveys can infer different sedimentation depths according to the post-fire treatments?
- How does restoration treatments affect the sedimentation rate?

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
  - Vertical dipole mode; ~0–1.8 m depth
* - ERT system (Syscal Pro)
  - Electrical Resistivity Tomography
  - Custum sequence, 72 electrodes, 1 m spacing
  - Three transects across the catchment
* - Sedimentation traps
  - Traps
  - At various location at the outlet of each subcatchements
  - 
* - UAV (DJI Phantom 4)
  - Aerial photogrammetry
  - RGB + multispectral
  - For co-registration and NDVI mapping
```

```{admonition} Data availability
:class: warning
Raw data are stored in the ICA-CSIC data repository. Contact the authors for access.
<!-- TODO: add DOI or data repository link -->
```

---

## 🔬 Analysis & Processing



## 🔄 On-going & Perspective Work

- [ ] Seasonal time-lapse ERT surveys
- [ ] Joint inversion of EMI + ERT for improved depth resolution
- [ ] Coupling with hydrological model (pyCATHY) at catchment scale
- [ ] Integration with remote sensing for spatial upscaling

```{admonition} GRWater project
:class: tip
This site is part of the [GRWater project](https://grwater.ica.csic.es/) — multi-scale monitoring of the Earth Critical Zone for post-fire forest management.
```

---

## ✅ Conclusion

Preliminary results indicate that 
```{admonition} Key takeaway
:class: important
??
```

---

```{admonition} Data Acquisition & Processing Service
:class: note
[ICA-CSIC](https://www.ica.csic.es) offers a professional service for geophysical
data acquisition and processing as part of its
[Geo-Spatial Technologies for Agro-Forestry Systems](https://www.ica.csic.es/servicios/servicios-cientifico-tecnicos/tecnologias-geo-espaciales-para-el-estudio-de-sistemas-agro-forestales)
scientific-technical services unit.
```
