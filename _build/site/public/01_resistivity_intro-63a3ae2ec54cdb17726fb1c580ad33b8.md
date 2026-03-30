---
title: "Introduction to Electrical Resistivity Tomography (ERT)"
kernelspec:
  name: python3
  display_name: "Python 3 (Geophysics)"
  language: python
bibliography:
  - references.bib
---

# Introduction to Electrical Resistivity Tomography (ERT)

## What is ERT and why does it matter?

Electrical Resistivity Tomography (ERT) is a near-surface geophysical method that
images the spatial distribution of the **electrical resistivity** (or its inverse,
electrical conductivity) of the subsurface.  Unlike borehole or soil-core
measurements—which are local and destructive—ERT is **non-invasive**, provides
**2D and 3D spatial coverage**, and can be repeated over time to track **dynamic
processes** (time-lapse, or 4D, ERT).

Key capabilities at a glance:

- Maps subsurface resistivity contrasts in **2D, 3D and through time**
  {cite}`dimech2022`
- Sensitive to changes in **soil water content, salinity, clay content and
  temperature** {cite}`telford1990,binley2005dc`
- Bridges the gap between sparse point sensors and large-scale remote sensing
  {cite}`carriere2022rs`

---

## ERT is sensitive to subsurface electrical properties

The measured quantity is the **apparent resistivity** $\rho_a$ (Ω·m), derived
from Ohm's law:

$$
\rho_a = K \frac{\Delta V}{I}
$$

where $K$ is the geometric factor of the electrode array, $\Delta V$ is the
measured potential difference and $I$ is the injected current.

Soil resistivity is controlled by the **Archie's law** petrophysical chain:

$$
\rho = a \, \phi^{-m} \, S_w^{-n} \, \rho_w
$$

where $\phi$ is porosity, $S_w$ is the degree of water saturation, $\rho_w$ is
the pore-water resistivity, and $a$, $m$, $n$ are empirical Archie parameters.
Because the petrophysical relationship is site-specific, interpreting resistivity
images in terms of soil moisture always carries uncertainty
{cite}`tso2019wrr`.

---

## Application domains

ERT has been applied across a wide range of scientific and engineering contexts.

### Civil engineering and geotechnical studies

Subsurface structure, void detection, dam monitoring, and embankment stability
are classic civil engineering targets for ERT {cite}`dimech2022`.

### Ecohydrology and forest ecology

ERT provides spatially distributed information on root water uptake (RWU) and
soil-water dynamics that point sensors cannot match.  Time-lapse ERT has been
used to image RWU dynamics in vineyards {cite}`mary2020soil,mary2019srep`,
orchard trees {cite}`vanella2018jhydrol`, and mixed forest stands
{cite}`loiseau2023scitotenv,carriere2022rs`.  Machine-learning approaches
combining ERT with proximal sensing data can now assess grapevine water status
non-invasively {cite}`mary2023bg`.

### Hydrological studies and petrophysical relationships

ERT couples naturally with hydrological modelling through petrophysical
relationships between resistivity and soil moisture
{cite}`tso2019wrr,mary2021vzj`.  Long-term monitoring systems have advanced
understanding of processes ranging from hillslope drainage to groundwater–surface
water exchange {cite}`slater2021wires`.  Geophysics can also be framed as a
**hypothesis-testing tool** to constrain critical-zone hydrogeological models
{cite}`dumont2024wires`.

### Post-wildfire environments

Combined ERT and stable-water-isotope analyses revealed that rainfall infiltrates
into weathered bedrock more deeply in fire-affected catchments than previously
thought, complicating simple runoff models {cite}`atwood2023natcomm`.

---

## ERT survey design and prospection strategy

Choosing the right measurement sequence is fundamental: the electrode
configuration controls sensitivity, depth of investigation and resolution.

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

The open-source package **ResIPy** {cite}`blanchy2020cageo` (the Python API of
which is `resipy`) implements steps 2–6 in a single, user-friendly environment.

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

:::{note}
Petrophysical relationships are site-specific and non-unique.  Always report
the uncertainty bounds on any moisture estimate derived from ERT data
{cite}`tso2019wrr`.
:::

---

## References

```{bibliography}
:style: unsrt
```
