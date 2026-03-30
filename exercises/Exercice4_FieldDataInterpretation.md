---
title: Exercice 4 ➡️ Field Data Interpretation
authors:
  - name: Benjamin Mary
    email: benjamin.mary@ica.csic.es
    affiliations:
      - ICA-CSIC, Madrid, Spain
  - name: Hector Nieto
    email: hector.nieto@ica.csic.es
    affiliations:
      - ICA-CSIC, Madrid, Spain
  - name: Miguel Herrezuelo
    affiliations:
      - ICA-CSIC, Madrid, Spain
  - name: Alfonso Torres
    affiliations:
      - Civil and Environmental Engineering Department, Utah State University (USA) 
  - name: Adrián Olalla
    affiliations:
      - ICA-CSIC, Madrid, Spain
      - COMPLUTIG SL, Alcalá de Henares (ES)
---




# Exploring Soil Management Legacies in Agronomy through EM and ERT


```{admonition} No relation with post-fire!
:class: caution
This example is not directly linked to post-fire soil management but rather to agronomy. But the results obtained are also interesting to understand dynamics of the measured electrical conductivity under varying soil conditions.
```

---

## Field Site description

### La Poveda Experimental Site

- **Location:** Near Madrid, Spain
- **Description:** Barley field (fallow during the survey) with four distinct treatments (00,01,11,10): 
  - fertilization 
  - irrigation
  - both
  - neither

```{figure} ../assets/images/plotpoveda_hidden.png
:width: 100%
:align: center
:alt: Poveda experimental site

*La Poveda experimental site with four subplots.*
```

```{admonition} Objective
:class: objective
Retreive the correct treatment according to the ERT and EM survey results i.e.

For instance (this is wrong only for the purpose of our understanding): 

- 01: irrigated/fertilized
- 11: irrigated 
- ...


```

---

## Methods

- **EM Survey:** Apparent EC measured with a 6L mini-explorer (gf-instrument) conducted in high mode sensitivity (HCP - 0.20 is the coil distance).
- **ERT Survey:** 4 roll-along with 0.5m electrodes inter-spacing.

---

## Geophysical results

### September 2025: EM survey apparent EC

```{figure} ../assets/images/empoveda.png
:width: 100%
:align: center
:alt: Poveda experimental site EM survey

Poveda experimental site EM survey
```

```{figure} ../assets/images/ertpoveda.png
:width: 100%
:align: center
:alt: Poveda experimental site ERT survey

Poveda experimental site ERT survey
```

- **Findings:** Despite minimal topography and a shallow water table (<1 m), post-rainfall conditions were not uniform. EM and ERT measurements showed treatment-dependent EC differences near the surface and at 1 m depth.

---

- **Findings:** Long-term soil management practices (e.g., irrigation, fertilization) create persistent differences in soil structure and moisture retention. Even after a saturating rainfall event, soil moisture and electrical conductivity (EC) vary among treatments.


## Perspectives

- **Geophysical Observations:** Findings highlight the importance of exercising caution when performing initial measurements in an agronomic system, as prior management and environmental history can strongly influence soil properties.
- **Legacy Effects:** Potential legacy effects can be indicated by the difference between predicted and actual values.
- **Model Integration:** Further advances in land surface models and closer integration of model simulations (e.g., water balance mode, SaltMod/SahysMod for long-term salinisation trends) and observations are needed to better characterize moisture memory.
- **Ecological Memory:** Extend the concept to the carbon fluxes and ecological memory (Canarini et al., 2021; Heinrich et al., 2025).

---

## Solution


```{admonition} Solution
:class: dropdown

```{figure} ../assets/images/plotpoveda_solution.png
:width: 100%
:align: center
:alt: Poveda experimental site

*La Poveda experimental site with four subplots.*
```

## Acknowledgements

This research was supported by the TWISTT project under the PRIMA Programme, funded by the European Union, and by the research project PCI2025-163228, financed by MICIU/AEI/10.13039/501100011033 and co-financed by the European Union. Benjamin Mary benefits from the grant "RyC2023-045040-I", funded by MICIU/AEI (grant no. 10.13039/501100011033) and the FSE. Field experiments in La Poveda were supported by EO4WUE project (TED2021-129814B-I00) funded by MCIN/AEI (DOI:10.13039/501100011033) and the European Union NextGenerationEU/PRTR. El Socorro experiments were supported by DATI project (PCI2021-121932) funded by MCIN/AEI (DOI:10.13039/501100011033) and the PRIMA EU program.

---

## References
