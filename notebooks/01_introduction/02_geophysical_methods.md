---
title: "Geophysical methods overview"
exports:
  - format: pdf
    template: plain_latex
    output: exports/02_geophysical_methods.pdf
---


# What is Geophysics?

**Geo** (Earth) + **physics** = the physics of the Earth. Geophysics applies physical
principles — mechanics, electromagnetism, thermodynamics — to study the subsurface
**without being destructive**. 


```{figure} ../../assets/images/ImageForArticle_1202_44837100215127314495.png
:name: ImageForArticle_1202_44837100215127314495.png
:width: 60%
:align: center
Image Credit: Lukiyanova Natalia / frenta / Shutterstock.com
```






Geophysics is classically split into two families:

- **Global / deep-Earth geophysics** — seismology, geomagnetism, geodesy. Targets
  the mantle, core, and plate-scale processes. Think earthquake monitoring or mapping
  the Earth's magnetic field {cite}`telford1990applied`.

- **Applied / environmental geophysics** — the branch we use here. Born from mineral
  and hydrocarbon exploration in the early 20th century {cite}`reynolds2011introduction`,
  it was progressively adapted to shallower targets: aquifers, contaminated soils,
  archaeological sites, and — more recently — ecosystem monitoring. Depths of interest
  range from centimetres to a few hundred metres.



::::{admonition} Key Concept: The "Anomaly"
:class: tip
The physical contrast measured in geophysical surveys is often referred to as an anomaly. Anomalies can vary in shape, size, and physical properties. For example, the water table may appear as an anomaly in electrical resistivity surveys, distinguishing it from surrounding soils.
::::


```{figure} ../../assets/images/Geological cross-section with water anomaly.png
:name: Geological cross-section with water anomaly.png
:width: 60%
:align: center
Conceptual subsurface cross-section showing a layered ground profile with a localized anomaly in the shallow subsurface. A distinct zone contrasts with surrounding material properties, representing a water-saturated region (e.g., a water table signature) that differs from the background soil and underlying bedrock in physical response (such as electrical resistivity).. 
```



Applied geophysics operates by detecting  **physical contrast** between materials. Geophysical surveys are designed to measure spatial variations in intrinsic physical properties from the surface. Every rock, soil layer, or fluid possesses characteristic properties, including:
- Electrical resistivity
- Dielectric permittivity
- Seismic velocity
- ...

A range of geophysical methods exists for measuring the physical properties of the soil. Each method responds to one or multiple specific properties, offering unique insights into subsurface characteristics.The [table below](#geophysical-methods-table) summarises the main geophysical methods used organised by the physical property they measure.






The measured **physical contrasts** are sensitive to the properties we care about: 
- Water content
- Texture
- Organic matter
- Soil structure
- ...


## Adressing limitation of punctual sensors

Geophysical methods allow us to image subsurface properties **non-invasively**, across **large areas**, and at [**repeated time steps**](#timelapseGeophy) — addressing exactly the limitations of traditional soil sampling. 

::::{admonition} Why non-invasive?
:class: tip
Traditional soil sampling is destructive, slow, and spatially sparse. A single geophysical
profile can produce thousands of subsurface data points in under an hour,
preserving soil structure.
::::


## Geophysics to image the critical zone

[**The figure below**](#fig-10_1002_wat2.1732_Fig1) illustrates the four themes where geophysics has been used as a hypothesis-testing tool in critical zone ({term}`CZ`) for imaging {cite}`dumont2024geophysics`:
- (A) **subsurface structure** and controls on hydrologic properties and processes; 
- (B) **storage and partitioning** of water in the CZ, parsed here as (B1) dimensionality of infiltration and controls on aquifer recharge, and (B2) seasonal- and event-based controls on groundwater–surface water exchange; 
- (V) **tree water uptake** and its role in subsurface variability;
- (D) **biogeochemical reactions** related to water fluxes in the CZ.



```{figure} ../../assets/images/10_1002_wat2.1732_Fig1
:name: fig-10_1002_wat2.1732_Fig1
:width: 100%
:align: center
Illustration of four themes where geophysics has been used as a hypothesis-testing tool in critical zone (CZ) hydrogeologic studies
(after {cite}`dumont2024geophysics`).  
```

---

The table below summarises the main geophysical methods used in soil and post-fire studies, organised by the physical property they measure.
:::{table} Main geophysical methods
:name: geophysical-methods-table

| Method | Physical property | Typical depth | Scale | Platform |
|---|---|---|---|---|
| {term}`ERT` | Electrical resistivity | 0.5–20 m | Plot to hillslope | Ground |
| {term}`EMI` | Electrical resistivity | 0.5–6 m | Field to catchment | Ground / UAV / Airborne |
| {term}`GPR` | Dielectric permittivity | 0.1–5 m | Plot to field | Ground / UAV |
| {term}`Seismic refraction` | P-wave velocity | 1–30 m | Plot to hillslope | Ground |
| {term}`MASW` | S-wave velocity | 1–20 m | Plot to hillslope | Ground |
:::

---


## Electrical Methods

### Electrical Resistivity Tomography (ERT)


```{admonition} Analogy
:class: hint
Tomography refers to the spatial reconstruction of a physical property within a medium from indirect measurements. The term is also widely used in medicine — most famously in CT (Computed Tomography) scans.
```

ERT is the **workhorse method** for shallow subsurface imaging in soil studies. Four electrodes are inserted into the ground: two inject electrical current, two measure the resulting voltage. By repeating this measurement across dozens of electrode combinations along a line or grid, a 2D or 3D image of subsurface **resistivity** is reconstructed through [inversion](resistivity-introduction#true-space-vs-model-space) (see [fig](fig-timeline-2_Dimechetal)).
```{figure} ../../assets/images/ERT_dehesas.jpg
:name: fig-ert
:width: 75%
:align: center
ERT survey in a Mediterranean dehesa. Multi-electrode arrays measure apparent resistivity along transects to image soil structure and moisture distribution.
```

**What ERT is sensitive to:**
- Soil water content (strongly — wet soils are conductive, dry soils resistive)
- Clay content and texture

See [the dedicated section](er-concept#how-to-translate-er-to-another-proxy-of-interest)

**Practical characteristics:**
- Depth of investigation: typically **0.5–20 m** depending on electrode spacing
- Spatial resolution: **centimetres to metres** depending on array geometry
- Survey time: **1/2–1 hour** per 2D transect with a modern multichannel system
- Limitation: requires good electrode–soil contact; dry or stony soils increase contact resistance

(More detailed on [ERT physical principles fundation](resistivity-introduction).)

---

ERT has been applied across a wide range of scientific and engineering contexts.
#### Civil engineering and geotechnical studies

Subsurface structure, void detection, dam monitoring, and embankment stability
are classic civil engineering targets for ERT {cite}`dimech2022`.

#### Ecohydrology and forest ecology

ERT provides spatially distributed information on root water uptake (RWU) and
soil-water dynamics that point sensors cannot match.  Time-lapse ERT has been
used to image RWU dynamics in vineyards {cite}`mary2020soil,mary2019srep`,
orchard trees {cite}`vanella2018jhydrol`, and mixed forest stands
{cite}`loiseau2023scitotenv,carriere2022rs`.  Machine-learning approaches
combining ERT with proximal sensing data can now assess grapevine water status
non-invasively {cite}`mary2023bg`.

```{figure} ../../assets/images/SG_ERT_plant
:name: fig-SG_ERT_plant
:width: 50%
:align: center
Geophysics conquering new territories: The rise of “agrogeophysics”.
(after {cite}`garre2021geophysics`). 
```


#### Hydrological studies and petrophysical relationships

ERT couples naturally with hydrological modelling through petrophysical
relationships between resistivity and soil moisture
{cite}`tso2019wrr,mary2021vzj`.  Long-term monitoring systems have advanced
understanding of processes ranging from hillslope drainage to groundwater–surface
water exchange {cite}`slater2021wires`.  Geophysics can also be framed as a
**hypothesis-testing tool** to constrain critical-zone hydrogeological models
{cite}`dumont2024wires`.

#### Post-wildfire environments

Combined ERT and stable-water-isotope analyses revealed that rainfall infiltrates
into weathered bedrock more deeply in fire-affected catchments than previously
thought, complicating simple runoff models {cite}`atwood2023natcomm`.


---

## Electromagnetic wave methods

### Electromagnetic Induction (EMI)

More detailed on [EM](electromagnetics-introduction)


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


**Practical characteristics:**
- Depth of investigation: **0.5–6 m** depending on coil geometry and frequency
- Spatial coverage: **several hectares per day** at walking speed
- No electrodes needed — ideal for stony or crusted post-fire surfaces
- Limitation: lower vertical resolution than ERT; sensitive to metal objects and infrastructure


```{figure} ../../assets/images/SG_EM_plant
:name: fig-SG_EM_plant
:width: 50%
:align: center
Geophysics conquering new territories: The rise of “agrogeophysics”.
(after {cite}`garre2021geophysics`). 
```

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

MASW analyses the **dispersive properties of surface waves** (Rayleigh waves) to derive a shear-wave velocity (Vs) profile. Vs is sensitive to **soil stiffness and bulk density**, which change with compaction.

**Practical characteristics:**
- Uses the same geophone spread as refraction — often acquired simultaneously
- Depth of investigation: **1–20 m**
- Particularly useful for detecting shallow compaction layers

---

## Multi-method strategy



```{figure} ../../assets/images/1-s2.0-S0048969723041268-ga1_lrg
:name: loiseau2023geophysical
:width: 100%
:align: center
Field implementation of geophysical techniques mostly discussed in the review article  {cite}`loiseau2023geophysical`). 
```


No single geophysical method answers all questions. Often we combine:

- **ERT** for high-resolution 2D profiles of water content and soil structure at plot scale
- **EMI** (ground and UAV) for rapid spatial mapping of conductivity patterns across burned and control catchments
- **GPR** for shallow interface detection and water content profiling
- ...

The [figure below](#loiseau2023geophysical) shows field the combination of geophysical techniques in the context of ecology (some methods are not explicity describe here, the reader is invited to refer to 	{cite}`loiseau2023geophysical` for more details : 
- A) ground penetrating radar (GPR), used to detect coarse roots; 
- B) self-potential (SP), used to monitor water flow; 
- C) gravimetry, used to monitor water stores; 
- D) electromagnetic induction (EMI), used to characterize the spatial heterogeneity of subsurface properties; 
- E) electrical resistivity tomography (ERT), used to characterize the spatial heterogeneity of subsurface properties and possibly monitor water dynamics. 

Seismic methods are not represented, but the implementation of seismic tomography is similar to that of ERT by replacing the electrodes with geophones and the transmitter is a shot, and it is also used to map spatial heterogeneity of subsurface properties.
(after {cite}`loiseau2023geophysical`). 



---

(timelapseGeophy)=
## Time-lapse strategy

Time-lapse geophysics is a monitoring strategy based on repeating the same geophysical measurements over time to detect changes in subsurface properties. By comparing datasets acquired at different moments, it highlights the temporal evolution of anomalies, allowing processes such as water movement, recharge, or soil moisture dynamics to be tracked through their changing physical signatures.


```{figure} ../../assets/images/image1-5_Dimechetal.png
:name: fig-timeline-2
:width: 100%
:align: center
Applied geophysics works by measuring a **physical contrast** between materials and investigate how it evolves with **time**. Figure from {cite}`dimech2023review`. 
```



---
```{admonition} Summary
:class: tip
In this introduction you have learned:
- **What geophysics is**: a non-invasive way to investigate the subsurface using physical principles.  
- **How geophysical methods work**: by detecting **contrasts in physical properties** (e.g., resistivity, permittivity, seismic velocity).  
- **What an anomaly represents**: a spatial variation in these properties, often linked to key features such as water content or subsurface structure.  
- **Why geophysics is powerful**: it provides spatially continuous information, overcoming the limitations of point-scale measurements.  
- **How multiple methods complement each other**: combining techniques improves interpretation of complex subsurface systems.  
- **What a time-lapse strategy adds**: the ability to monitor **temporal changes**, revealing dynamic processes such as water movement and recharge.  
```

