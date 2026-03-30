---
title: Hellín — Sediment Check Dams
authors:
  - name: Benjamin Mary
    email: benjamin.mary@ica.csic.es
    affiliations:
      - ICA-CSIC, Madrid, Spain
---

# 🪨 Hellín — Sediment Check Dams

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

```{raw} html
<div id="map-diques" style="height:350px; width:100%; border-radius:8px; margin: 1em 0;"></div>
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script>
  document.addEventListener("DOMContentLoaded", function () {
    var map = L.map('map-diques').setView([38.50, -1.68], 13);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    // Multiple check dam locations
    var dams = [
      { lat: 38.502, lon: -1.682, name: "Dique 1" },
      { lat: 38.498, lon: -1.676, name: "Dique 2" },
      { lat: 38.495, lon: -1.671, name: "Dique 3" },
    ];
    dams.forEach(function(d) {
      L.marker([d.lat, d.lon])
        .addTo(map)
        .bindPopup('<b>' + d.name + '</b><br>Check dam — sediment monitoring');
    });
  });
</script>
```

---

## 🌍 Context

```{figure} ../../assets/images/hellin_diques_context.jpg
:width: 60%
:align: center
:alt: Check dam in the Hellín rambla

One of the sediment check dams in the Hellín rambla network, showing sediment accumulation behind the structure.
<!-- TODO: replace with actual image path -->
```

Sediment check dams (*diques de sedimentación*) are a common post-fire restoration measure in Spanish ramblas and ephemeral streams. They are designed to trap sediment mobilised by post-fire erosion, reduce downstream flood risk, and promote vegetation recovery in gully floors. However, their effectiveness and the physical properties of trapped sediments remain poorly characterised.

```{admonition} Post-fire restoration context
:class: note
After the 2022 wildfires in the Hellín area, a network of check dams was installed along the main rambla as an emergency erosion-control measure. This study provides the first geophysical characterisation of the sediment body behind these structures.
```

---

## ❓ Scientific Question

> **What is the internal architecture and hydrological behaviour of sediment bodies trapped behind post-fire check dams, and how do they evolve over time?**

Key sub-questions:

- What is the volume and stratigraphic structure of accumulated sediment?
- Does water storage within the sediment body contribute to local groundwater recharge?
- How quickly do check dams fill, and what controls their trapping efficiency?

---

## 🛠️ Data Collected

```{list-table} Instruments and survey configuration
:header-rows: 1
:widths: 20 25 25 30

* - Instrument
  - Method
  - Configuration
  - Notes
* - ERT system (ABEM)
  - Electrical Resistivity Tomography
  - Wenner, 48 electrodes, 0.5 m spacing
  - Longitudinal + cross-dam transects
* - GPR (MALA ProEx)
  - Ground-Penetrating Radar
  - 250 MHz antenna
  - Longitudinal profiles along sediment surface
* - CMD Mini-Explorer
  - Electromagnetic Induction (EMI)
  - 0.32 / 0.71 / 1.18 m coil spacings
  - Grid survey over sediment body
* - Topographic survey (GNSS)
  - RTK GPS
  - Leica GS18
  - DEM of sediment surface pre/post events
* - Sediment core sampling
  - Manual coring
  - 1 m cores at 5 locations
  - Grain size, bulk density, organic matter
```

```{admonition} Data availability
:class: warning
Raw data are stored in the ICA-CSIC data repository. Contact the authors for access.
<!-- TODO: add DOI or data repository link -->
```

---

## 🔄 On-going & Perspective Work

- [ ] Annual repeat surveys to track sediment filling rates
- [ ] Moisture monitoring within sediment body (buried sensors)
- [ ] 3D ERT inversion for volumetric estimates
- [ ] Comparison across dam types (concrete vs. gabion vs. log)
- [ ] Assessment of dam failure risk under extreme rainfall scenarios

```{admonition} GRWater project
:class: tip
This site is part of the [GRWater project](https://grwater.ica.csic.es/) — multi-scale monitoring of the Earth Critical Zone for post-fire forest management.
```

---

## ✅ Conclusion

ERT and GPR surveys reveal a heterogeneous internal structure within the sediment bodies, with alternating coarse and fine layers reflecting episodic deposition during individual storm events. High-resistivity zones near the surface of some dams indicate dry, coarse-grained material, while low-resistivity zones at depth suggest persistent moisture retention — indicating a potential groundwater recharge function not previously attributed to these structures.

```{admonition} Key takeaway
:class: important
Geophysical imaging of post-fire check dam sediments reveals a dual function: sediment trapping **and** subsurface water storage — with implications for restoration design and long-term catchment recovery.
```

---

```{admonition} Data Acquisition & Processing Service
:class: note
[ICA-CSIC](https://www.ica.csic.es) offers a professional service for geophysical
data acquisition and processing as part of its
[Geo-Spatial Technologies for Agro-Forestry Systems](https://www.ica.csic.es/servicios/servicios-cientifico-tecnicos/tecnologias-geo-espaciales-para-el-estudio-de-sistemas-agro-forestales)
scientific-technical services unit.
```
