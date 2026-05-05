---
title: Ejercicio 5 ➡️ Documenta tu evento post-incendio en España
authors:
  - name: Benjamin Mary
    email: benjamin.mary@ica.csic.es
    affiliations:
      - ICA-CSIC, Madrid, España
kernelspec:
  name: python3
  display_name: "Python 3 (Geofísica)"
  language: python
---

# 🔥 Geofísica Post-Incendio — Estrategia de campo

Diseña una campaña de prospección geofísica para un sitio quemado de tu elección.
No hay respuestas incorrectas — lo que importa es tu razonamiento.

::::{tip} Instrucciones
Tienes **~10 minutos**. Trabaja cada parte y haz clic en **"Revisar mis respuestas"** al final.
::::

---

## 🌍 Parte 1 — Tu sitio de campo

Usa uno de estos recursos para identificar una zona quemada:
- 🛰️ Imágenes EO / mapas dNBR de la sesión anterior
- 📄 Un artículo de tu revisión bibliográfica
- 🌐 [EFFIS](https://effis.jrc.ec.europa.eu/) · [NASA FIRMS](https://firms.nasa.gov/)

```{code-cell} ipython3
:tags: [hide-input]
import ipywidgets as w
from IPython.display import display

w_site = w.Text(
    description="📍 Sitio:",
    placeholder="Nombre, país, coordenadas aproximadas",
    style={"description_width": "80px"},
    layout=w.Layout(width="100%")
)
w_source = w.Textarea(
    description="🛰️ Fuente:",
    placeholder="p. ej. dNBR de Sentinel-2 / EFFIS / referencia bibliográfica",
    style={"description_width": "80px"},
    layout=w.Layout(width="100%", height="65px")
)
w_why = w.Textarea(
    description="💡 ¿Por qué?",
    placeholder="¿Por qué es interesante este sitio para la investigación post-incendio de suelo/agua? (1-2 frases)",
    style={"description_width": "80px"},
    layout=w.Layout(width="100%", height="65px")
)
display(w_site, w_source, w_why)
```

---

## 🧪 Parte 2 — Procesos post-incendio

```{code-cell} ipython3
:tags: [hide-input]
w_processes = w.SelectMultiple(
    description="Procesos:",
    options=[
        "Hidrofobicidad del suelo (repelencia al agua)",
        "Pérdida de estructura del suelo / compactación",
        "Cambios en la infiltración / flujo preferencial",
        "Erosión y redistribución de sedimentos",
        "Recuperación de la vegetación que afecta la humedad del suelo",
        "Capa de ceniza → costra superficial conductora",
        "Otro (explicar abajo)",
    ],
    rows=7,
    style={"description_width": "80px"},
    layout=w.Layout(width="100%")
)
w_phys = w.Textarea(
    description="⚡ Efecto:",
    placeholder="¿Cómo afecta cada proceso seleccionado a la resistividad o conductividad del suelo?",
    style={"description_width": "80px"},
    layout=w.Layout(width="100%", height="75px")
)
display(
    w.HTML("<b>Selecciona 1-3 procesos que esperas en tu sitio:</b>"),
    w_processes,
    w.HTML("<b>¿Cómo afectaría cada uno a la resistividad/conductividad del suelo?</b>"),
    w_phys
)
```

---

## 📡 Parte 3 — Métodos geofísicos

```{code-cell} ipython3
:tags: [hide-input]
METHODS = ["— seleccionar —", "TRE", "EMI / FDEM", "GPR", "Refracción sísmica", "Monitoreo TDR", "Otro"]

def method_row(n):
    m = w.Dropdown(options=METHODS, layout=w.Layout(width="160px"))
    t = w.Text(placeholder="¿Qué estás caracterizando?", layout=w.Layout(width="270px"))
    l = w.Text(placeholder="Principal limitación en este sitio", layout=w.Layout(width="270px"))
    header = w.HTML(f"<b>Método {n}</b>")
    return w.VBox([header, w.HBox([m, t, l])]), m, t, l

box1, w_m1, w_t1, w_l1 = method_row(1)
box2, w_m2, w_t2, w_l2 = method_row(2)

display(
    w.HTML("<b style='font-size:.9rem'>Para cada método: ¿qué estás caracterizando y cuál es la principal limitación?</b>"),
    box1, box2
)
```

---

## 🗺️ Parte 4 — Dónde y cuándo

```{code-cell} ipython3
:tags: [hide-input]
w_transects = w.Textarea(
    description="📍 Dónde:",
    placeholder="¿Dónde colocarías los perfiles? ¿A lo largo de la pendiente? ¿Cruzando el gradiente de severidad del incendio? ¿Cerca del arroyo?",
    style={"description_width": "60px"},
    layout=w.Layout(width="100%", height="65px")
)
w_when = w.RadioButtons(
    description="⏱ Cuándo:",
    options=[
        "Inmediatamente después del incendio (seco)",
        "Antes de la primera lluvia significativa",
        "Después de las primeras lluvias (inicio de la estación húmeda)",
        "Repetido: estación seca + húmeda (monitoreo)",
        "Otro",
    ],
    style={"description_width": "60px"},
    layout=w.Layout(width="100%")
)
w_when_why = w.Textarea(
    description="💬 Por qué:",
    placeholder="Justifica tu elección temporal en 1-2 frases",
    style={"description_width": "60px"},
    layout=w.Layout(width="100%", height="55px")
)
display(w_transects, w_when, w_when_why)
```

---

## ✍️ Parte 5 — Vínculo con la restauración

```{code-cell} ipython3
:tags: [hide-input]
w_resto = w.Textarea(
    description="🌱 Acción:",
    placeholder="¿Cómo podrían tus resultados informar una decisión de restauración? (dónde plantar, riesgo de erosión, ubicación de diques de retención…)",
    style={"description_width": "60px"},
    layout=w.Layout(width="100%", height="75px")
)
display(w_resto)
```

---

## 📋 Revisar tus respuestas

```{code-cell} ipython3
:tags: [hide-input]
from datetime import datetime

btn = w.Button(
    description="📋 Revisar mis respuestas",
    button_style="warning",
    layout=w.Layout(width="240px", height="38px")
)
out = w.Output()

def on_click(_):
    with out:
        out.clear_output()
        answers = {
            "Sitio":                       w_site.value,
            "Fuente":                      w_source.value,
            "Por qué es interesante":      w_why.value,
            "Procesos":                    ", ".join(w_processes.value),
            "Efecto en la resistividad":   w_phys.value,
            "Método 1":                    f"{w_m1.value} | objetivo: {w_t1.value} | limitación: {w_l1.value}",
            "Método 2":                    f"{w_m2.value} | objetivo: {w_t2.value} | limitación: {w_l2.value}",
            "Ubicación de perfiles":       w_transects.value,
            "Temporización":               w_when.value,
            "Justificación temporal":      w_when_why.value,
            "Vínculo con restauración":    w_resto.value,
        }
        print(f"{'─'*58}")
        print(f"  RESPUESTAS  —  {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        print(f"{'─'*58}")
        for k, v in answers.items():
            print(f"\n▸ {k}\n   {v or '— sin respuesta —'}")
        print(f"\n{'─'*58}")

btn.on_click(on_click)
display(btn, out)
```

```{note} Servicio de Adquisición y Procesado de Datos
El [ICA-CSIC](https://www.ica.csic.es) ofrece un servicio profesional de adquisición y procesado de datos geofísicos en el marco de su unidad de servicios científico-técnicos de [Tecnologías Geo-Espaciales para el Estudio de Sistemas Agro-Forestales](https://www.ica.csic.es/servicios/servicios-cientifico-tecnicos/tecnologias-geo-espaciales-para-el-estudio-de-sistemas-agro-forestales).
```
