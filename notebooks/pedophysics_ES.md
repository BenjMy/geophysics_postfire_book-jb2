---
title: "Modelo petro/pedofísico"
kernelspec:
  name: python3
  display_name: Python 3 (Geophysics)
  language: python
---


```{admonition} Principio clave
:class: tip
Las mediciones geofísicas son **indirectas**. No miden directamente el contenido de agua del suelo ni el contenido de arcilla — miden una señal física (resistividad, velocidad de onda, tiempo de tránsito radar) que se correlaciona con esas propiedades. La interpretación de datos geofísicos siempre requiere cierto conocimiento de las condiciones locales del suelo.
```

Por ejemplo, la resistividad medida en campo integra en una única cantidad global:
- Los efectos de la geometría de los poros
- La saturación de fluidos
- La química del agua intersticial


La **petrofísica** es el estudio de las propiedades físicas y químicas de rocas y suelos y de los fluidos que contienen. Proporciona el vínculo cuantitativo — conocido como **función de transferencia petrofísica** — entre una cantidad geofísica medible y una propiedad física objetivo de interés. Dado que estas relaciones son empíricas y dependientes de la litología, deben calibrarse para cada emplazamiento y conllevan una incertidumbre inherente.


La extracción de variables de estado hidrológico a partir de datos de resistividad requiere, por tanto, un **modelo petrofísico** explícito. Para medios porosos limpios y libres de arcilla, la **ley de Archie** {cite}`archie2003electrical` proporciona el marco empírico estándar:

$$
\rho = a \, \phi^{-m} \, S_w^{-n} \, \rho_w
$$

donde $\phi$ es la porosidad (–), $S_w$ es el grado de saturación de agua (–), $\rho_w$ es la resistividad del agua intersticial (Ω·m), y $a$, $m$, $n$ son parámetros empíricos de Archie que controlan la tortuosidad, la cementación y el exponente de saturación, respectivamente. Dado que estos parámetros dependen de la litología y deben calibrarse a partir de muestras de testigos o mediciones en sondeos, la inversión de imágenes de resistividad en campos de humedad del suelo siempre conlleva una **incertidumbre de modelo** {cite}`tso2019wrr`.


```{admonition} Las relaciones son empíricas y dependientes de la litología
:class: caution
Las relaciones petrofísicas deben calibrarse para cada emplazamiento.
```

La [figura siguiente](#fig-pedophysicsChou) ilustra un ejemplo de datos ERT convertidos a potencial mátrico del suelo y contenido volumétrico de agua mediante relaciones petrofísicas. Para más detalles, consulta el artículo completo {cite}`chou2024improving`.


```{figure} ../assets/images/pedophysicsChou.png
:name: fig-pedophysicsChou
:width: 100%
:align: center
Ejemplo de datos ERT convertidos a potencial mátrico del suelo y contenido volumétrico de agua mediante relaciones petrofísicas (figura de {cite}`chou2024improving`).
```



El código siguiente ilustra cómo la **Ley de Archie** relaciona la saturación de agua ($S_w$) con la resistividad de la formación ($\rho$) para una porosidad ($\phi$) y un factor de tortuosidad ($a$) dados, mostrando que a medida que $S_w$ disminuye — lo que indica que más hidrocarburos desplazan a la salmuera — la resistividad aumenta de forma no lineal siguiendo una relación en ley de potencias gobernada por el exponente de saturación $n$.

```{code-cell} ipython3
:tags: [hide-input]
import numpy as np
import plotly.graph_objects as go
import ipywidgets as widgets
from IPython.display import display
import matplotlib.pyplot as plt
from ipywidgets import interact

def archie_resistivity(phi, Sw, rho_w=0.1, a=1.0, m=1.5, n=2.0):
    return a * phi**(-m) * Sw**(-n) * rho_w

Sw_arr = np.linspace(0.05, 1.0, 300)

def plot_archie(phi=0.20, a=1.0):
    rho = archie_resistivity(phi, Sw_arr, a=a)
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.plot(rho, Sw_arr, color='#2980b9', linewidth=2.5)
    ax.set_xscale('log')
    ax.set_xlim(0.01, 1000)
    ax.set_ylim(0, 1.05)
    ax.set_xlabel('Resistividad ρ (Ω·m)')
    ax.set_ylabel('Saturación de agua $S_w$')
    ax.set_title("Ley de Archie — ρ = a · φ$^{-m}$ · $S_w^{-n}$ · ρ$_w$")
    ax.grid(True, which='both', linestyle='--', alpha=0.4)
    plt.tight_layout()
    plt.show()

interact(
    plot_archie,
    phi=widgets.SelectionSlider(
        options=[(str(v), v) for v in np.round(np.arange(0.05, 0.61, 0.01), 2)],
        value=0.20,
        description='φ (porosidad)',
        style={'description_width': '120px'},
        layout=widgets.Layout(width='500px')
    ),
    a=widgets.SelectionSlider(
        options=[(str(v), v) for v in np.round(np.arange(0.5, 2.05, 0.25), 2)],
        value=1.0,
        description='a (tortuosidad)',
        style={'description_width': '120px'},
        layout=widgets.Layout(width='500px')
    ),
)
```
