---
title: Exercice 5 ➡️ Document your post-fire event in Spain
authors:
  - name: Benjamin Mary
    email: benjamin.mary@ica.csic.es
    affiliations:
      - ICA-CSIC, Madrid, Spain
kernelspec:
  name: python3
  display_name: "Python 3 (Geophysics)"
  language: python
---

# 🔥 Post-Fire Geophysics — Field Strategy

Design a geophysical prospection campaign for a burned site of your choice.
No wrong answers — your reasoning matters more than the result.

::::{admonition} Instructions
:class: tip
You have **~10 minutes**. Work through each part and click **"Review my answers"** at the end.
::::

---

## 🌍 Part 1 — Your Field Site

Use one of these to identify a burned area:
- 🛰️ EO imagery / dNBR maps from the previous session
- 📄 A paper from your literature review  
- 🌐 [EFFIS](https://effis.jrc.ec.europa.eu/) · [NASA FIRMS](https://firms.nasa.gov/)
```{code-cell} ipython3
:tags: [hide-input]
import ipywidgets as w
from IPython.display import display

w_site = w.Text(
    description="📍 Site:",
    placeholder="Name, country, approx. coordinates",
    style={"description_width": "80px"},
    layout=w.Layout(width="100%")
)
w_source = w.Textarea(
    description="🛰️ Source:",
    placeholder="e.g. dNBR from Sentinel-2 / EFFIS / paper reference",
    style={"description_width": "80px"},
    layout=w.Layout(width="100%", height="65px")
)
w_why = w.Textarea(
    description="💡 Why?",
    placeholder="Why is this site interesting for post-fire soil/water research? (1–2 sentences)",
    style={"description_width": "80px"},
    layout=w.Layout(width="100%", height="65px")
)
display(w_site, w_source, w_why)
```

---

## 🧪 Part 2 — Post-Fire Processes
```{code-cell} ipython3
:tags: [hide-input]
w_processes = w.SelectMultiple(
    description="Processes:",
    options=[
        "Soil hydrophobicity (water repellency)",
        "Loss of soil structure / compaction",
        "Changes in infiltration / preferential flow",
        "Erosion and sediment redistribution",
        "Vegetation recovery affecting soil moisture",
        "Ash layer → conductive surface crust",
        "Other (explain below)",
    ],
    rows=7,
    style={"description_width": "80px"},
    layout=w.Layout(width="100%")
)
w_phys = w.Textarea(
    description="⚡ Effect:",
    placeholder="How does each selected process affect soil resistivity or conductivity?",
    style={"description_width": "80px"},
    layout=w.Layout(width="100%", height="75px")
)
display(
    w.HTML("<b>Select 1–3 processes you expect at your site:</b>"),
    w_processes,
    w.HTML("<b>How would each affect soil resistivity/conductivity?</b>"),
    w_phys
)
```

---

## 📡 Part 3 — Geophysical Methods
```{code-cell} ipython3
:tags: [hide-input]
METHODS = ["— select —", "ERT", "EMI / FDEM", "GPR", "Seismic refraction", "TDR monitoring", "Other"]

def method_row(n):
    m = w.Dropdown(options=METHODS, layout=w.Layout(width="160px"))
    t = w.Text(placeholder="What are you targeting?", layout=w.Layout(width="270px"))
    l = w.Text(placeholder="Main limitation at this site", layout=w.Layout(width="270px"))
    header = w.HTML(f"<b>Method {n}</b>")
    return w.VBox([header, w.HBox([m, t, l])]), m, t, l

box1, w_m1, w_t1, w_l1 = method_row(1)
box2, w_m2, w_t2, w_l2 = method_row(2)

display(
    w.HTML("<b style='font-size:.9rem'>For each method: what are you targeting and what is the main limitation?</b>"),
    box1, box2
)
```

---

## 🗺️ Part 4 — Where & When
```{code-cell} ipython3
:tags: [hide-input]
w_transects = w.Textarea(
    description="📍 Where:",
    placeholder="Where would you place transects? Along slope? Crossing burn severity gradient? Near stream?",
    style={"description_width": "60px"},
    layout=w.Layout(width="100%", height="65px")
)
w_when = w.RadioButtons(
    description="⏱ When:",
    options=[
        "Immediately after fire (dry)",
        "Before first significant rainfall",
        "After first rains (wet season onset)",
        "Repeated: dry + wet season (monitoring)",
        "Other",
    ],
    style={"description_width": "60px"},
    layout=w.Layout(width="100%")
)
w_when_why = w.Textarea(
    description="💬 Why:",
    placeholder="Justify your timing in 1–2 sentences",
    style={"description_width": "60px"},
    layout=w.Layout(width="100%", height="55px")
)
display(w_transects, w_when, w_when_why)
```

---

## ✍️ Part 5 — Link to Restoration
```{code-cell} ipython3
:tags: [hide-input]
w_resto = w.Textarea(
    description="🌱 Action:",
    placeholder="How could your results inform a restoration decision? (where to plant, erosion risk, check dam placement…)",
    style={"description_width": "60px"},
    layout=w.Layout(width="100%", height="75px")
)
display(w_resto)
```

---

## 📋 Review Your Answers
```{code-cell} ipython3
:tags: [hide-input]
from datetime import datetime

btn = w.Button(
    description="📋 Review my answers",
    button_style="warning",
    layout=w.Layout(width="220px", height="38px")
)
out = w.Output()

def on_click(_):
    with out:
        out.clear_output()
        answers = {
            "Site":                  w_site.value,
            "Source":                w_source.value,
            "Why interesting":       w_why.value,
            "Processes":             ", ".join(w_processes.value),
            "Effect on resistivity": w_phys.value,
            "Method 1":              f"{w_m1.value} | target: {w_t1.value} | limitation: {w_l1.value}",
            "Method 2":              f"{w_m2.value} | target: {w_t2.value} | limitation: {w_l2.value}",
            "Transect placement":    w_transects.value,
            "Timing":                w_when.value,
            "Timing rationale":      w_when_why.value,
            "Restoration link":      w_resto.value,
        }
        print(f"{'─'*58}")
        print(f"  ANSWERS  —  {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        print(f"{'─'*58}")
        for k, v in answers.items():
            print(f"\n▸ {k}\n   {v or '— no answer —'}")
        print(f"\n{'─'*58}")

btn.on_click(on_click)
display(btn, out)
```
```{admonition} Data Acquisition & Processing Service
:class: note
[ICA-CSIC](https://www.ica.csic.es) offers a professional service for geophysical
data acquisition and processing as part of its
[Geo-Spatial Technologies for Agro-Forestry Systems](https://www.ica.csic.es/servicios/servicios-cientifico-tecnicos/tecnologias-geo-espaciales-para-el-estudio-de-sistemas-agro-forestales)
scientific-technical services unit.
```
