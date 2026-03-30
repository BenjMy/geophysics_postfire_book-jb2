---
title: Exercice 1 ➡️ Understand resistivity
authors:
  - name: Benjamin Mary
    email: benjamin.mary@ica.csic.es
    affiliations:
      - ICA-CSIC, Madrid, Spain
---
## Exercise 1 — Electrical Resistivity

> **Context:** Electrical resistivity is a fundamental property in applied geophysics. Understanding how it varies with material type and moisture content is essential for interpreting subsurface surveys such as ERT (Electrical Resistivity Tomography).

---

### 🟢 Q1 (Easy) — Basic concept of resistivity

**Define electrical resistivity** and explain what it tells us about a material's behavior toward electric current. Using the table below as a guide, classify the following materials as **good conductors** (low resistivity) or **poor conductors** (high resistivity):

| Material | Resistivity class |
|---|---|
| Dry granite | ? |
| Saline water | ? |
| Clay | ? |
| Dry sand | ? |
```{dropdown} Answer
Electrical resistivity quantifies how strongly a material opposes the flow of electric current.

- **Low resistivity → good conductor** (e.g., clay, saline water)
- **High resistivity → poor conductor** (e.g., dry sand, dry granite)
```

---

### 🟡 Q2 (Medium) — Effect of moisture content

A soil sample is progressively wetted with saline water. **Describe and explain** how its resistivity evolves as moisture content increases. Your answer should address:

1. What happens physically inside the pore space?
2. What role do ions play?
3. Under what condition could a soil **remain resistive** despite being saturated?
```{dropdown} Answer
As moisture content increases, resistivity generally **decreases** because:

1. Water fills pore spaces, reducing air gaps that block current flow
2. Dissolved ions in pore water create charge carriers that conduct electricity
3. Connectivity between grains improves conduction pathways

**Exception:** Very clean (ion-poor) sands may remain relatively resistive even when saturated, because resistivity depends on both fluid content *and* fluid conductivity.
```

---

### 🟠 Q3 (Hard) — Multi-cause reasoning

The two soil profiles below show the **same low resistivity value** (ρ ≈ 5 Ω·m) at shallow depth, but have **very different origins**.

> Profile A is located in a coastal area with known seawater infiltration.  
> Profile B is located inland over a glacial deposit.

1. Propose **one geological interpretation** for each profile that explains the low resistivity.
2. What additional data (geochemical, lithological, or geophysical) would help **distinguish** between the two causes?
3. What fundamental limitation of resistivity surveys does this illustrate?
```{dropdown} Answer
1. **Profile A:** Saline groundwater intrusion — seawater lowers resistivity through high ionic concentration.  
   **Profile B:** Clay-rich or organic-rich saturated sediment — clay has high surface conductivity.

2. Distinguishing data:
   - Water conductivity / salinity measurements (EC probe)
   - Borehole or core sampling for lithology
   - IP (Induced Polarization) to detect clay minerals
   - Seismic survey for stratigraphic context

3. This illustrates the **non-uniqueness problem**: identical resistivity values can result from very different geological causes, making ground-truth data essential for reliable interpretation.
```

---

### 📊 Q4 (MCQ) — Material identification

Which of the following materials typically has the **highest electrical resistivity**?

- A. Saturated clay
- B. Saline water
- C. Dry granite
- D. Wet sand
```{dropdown} Answer
✅ **C. Dry granite**

Dry granite contains virtually no free ions or connected fluid pathways, making it an excellent electrical insulator. Resistivity can exceed **10⁶ Ω·m**, far higher than wet or clay-bearing materials.
```

---

### 📊 Q5 (MCQ) — Moisture and resistivity trend

In a soil profile, resistivity values **decrease with depth** from 500 Ω·m at the surface to 20 Ω·m at 3 m depth. What is the **most likely explanation**?

- A. The soil becomes coarser with depth
- B. Moisture content and/or pore water salinity increase with depth
- C. The soil becomes drier approaching the water table
- D. Grain size decreases, reducing porosity
```{dropdown} Answer
✅ **B. Moisture content and/or pore water salinity increase with depth**

Approaching the water table, pore spaces become increasingly saturated with electrolytic water, dramatically lowering resistivity. This is one of the most common patterns observed in ERT profiles.
```