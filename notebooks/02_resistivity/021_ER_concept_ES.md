---
title: "Resistividad Eléctrica"
kernelspec:
  name: python3
  display_name: Python 3 (Geophysics)
  language: python
authors:
  - name: Benjamin Mary
    email: benjamin.mary@ica.csic.es
    affiliations:
      - ICA-CSIC, Madrid, España
---
    
```{note} Objetivos de aprendizaje
- Comprender la base física de la resistividad eléctrica
- Aplicar la Ley de Ohm en un contexto geofísico
- Conocer los rangos de resistividad eléctrica para materiales terrestres comunes
- Explorar cómo las propiedades del suelo controlan la resistividad
```

---

## Propiedades físicas del suelo

La **resistividad** eléctrica $\rho$ (Ω·m) describe con qué intensidad se opone un material al paso de la corriente eléctrica. Su inversa es la **conductividad** $\sigma$ (S/m):

$$\sigma = \frac{1}{\rho}$$

### Ley de Ohm

Para un cilindro homogéneo de sección transversal $A$ (m²) y longitud $L$ (m):

$$R = \rho \frac{L}{A}$$

donde $R$ es la resistencia (Ω). Reordenando:

$$\rho = R \frac{A}{L}$$

Ajusta la resistividad, la longitud y la sección transversal para ver cómo cambia la resistencia:

```{code-cell} ipython3
:tags: [remove-input, cache]
import ipywidgets as widgets
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.colors as mcolors
import numpy as np

def resistance_widget():
    style  = {'description_width': '80px'}
    layout = widgets.Layout(width='450px')

    rho_slider = widgets.FloatLogSlider(
        value=50, base=10, min=0, max=6, step=0.05,
        description='ρ (Ω·m)', style=style, layout=layout)
    L_slider = widgets.FloatSlider(
        value=1.0, min=0.1, max=10.0, step=0.1,
        description='L (m)', style=style, layout=layout)
    A_slider = widgets.FloatSlider(
        value=1.0, min=0.01, max=5.0, step=0.01,
        description='A (m²)', style=style, layout=layout)

    out = widgets.Output()

    def update(change=None):
        rho = rho_slider.value
        L   = L_slider.value
        A   = A_slider.value
        R   = rho * L / A
        sigma = 1.0 / rho
        side  = np.sqrt(A)

        with out:
            out.clear_output(wait=True)

            fig, axes = plt.subplots(1, 2, figsize=(10, 4))

            ax = axes[0]
            ax.set_xlim(0, 10)
            ax.set_ylim(0, 6)
            ax.set_aspect('equal')
            ax.axis('off')

            norm     = mcolors.LogNorm(vmin=1, vmax=1e6)
            cmap     = plt.cm.RdYlBu_r
            face_col = cmap(norm(rho))

            w = min(max(side * 0.8, 0.5), 3.5)
            h = min(max(side * 0.8, 0.5), 3.5)
            d = min(max(L   * 0.6, 0.5), 5.0)

            ox, oy = 1.5, 1.0

            front = mpatches.FancyBboxPatch(
                (ox, oy), w, h,
                boxstyle='square,pad=0',
                facecolor=face_col, edgecolor='k', linewidth=1.5, zorder=2)
            ax.add_patch(front)

            top_x = [ox, ox+w, ox+w+d*0.4, ox+d*0.4, ox]
            top_y = [oy+h, oy+h, oy+h+d*0.3, oy+h+d*0.3, oy+h]
            ax.fill(top_x, top_y, color=mcolors.to_rgba(face_col, 0.7),
                    edgecolor='k', linewidth=1.5, zorder=2)

            right_x = [ox+w, ox+w+d*0.4, ox+w+d*0.4, ox+w, ox+w]
            right_y = [oy, oy+d*0.3, oy+h+d*0.3, oy+h, oy]
            ax.fill(right_x, right_y, color=mcolors.to_rgba(face_col, 0.5),
                    edgecolor='k', linewidth=1.5, zorder=2)

            ax.annotate('', xy=(ox+d*0.4+0.1, oy-0.4),
                        xytext=(ox+0.0, oy-0.4),
                        arrowprops=dict(arrowstyle='<->', color='k', lw=1.5))
            ax.text(ox + d*0.2, oy-0.7, f'L = {L:.1f} m',
                    ha='center', fontsize=10, fontstyle='italic')

            sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
            sm.set_array([])
            cbar = fig.colorbar(sm, ax=ax, orientation='vertical',
                                fraction=0.03, pad=0.02,
                                label='ρ (Ω·m)')
            cbar.ax.tick_params(labelsize=8)

            ax.set_title('Geometría del elemento resistivo', fontsize=11, pad=8)

            ax2 = axes[1]
            ax2.axis('off')

            lines = [
                ('Ecuación',          r'$R = \rho \cdot \dfrac{L}{A}$',  14, 'black'),
                ('',                  '',                                   8, 'black'),
                ('ρ (resistividad)',  f'{rho:.2e} Ω·m',                   12, '#c0392b'),
                ('L (longitud)',      f'{L:.2f} m',                        12, '#2980b9'),
                ('A (sección trans.)',f'{A:.4f} m²',                       12, '#27ae60'),
                ('',                  '',                                    8, 'black'),
                ('R (resistencia)',   f'{R:.4f} Ω',                        14, 'black'),
                ('σ (conductividad)', f'{sigma:.2e} S/m',                  12, '#7f8c8d'),
            ]

            y = 0.92
            for label, value, fs, col in lines:
                if label == '':
                    y -= 0.04
                    continue
                ax2.text(0.05, y, f'{label}:', fontsize=fs,
                         transform=ax2.transAxes, color='#555')
                ax2.text(0.55, y, value, fontsize=fs, fontweight='bold',
                         transform=ax2.transAxes, color=col)
                y -= 0.13

            ax2.text(0.05, 0.04,
                     '⚠ R = ρ·L/A es la ecuación de la resistencia,\n'
                     '   no la Ley de Ohm (V = R·I)',
                     fontsize=8, color='#888',
                     transform=ax2.transAxes, style='italic')

            plt.tight_layout()
            plt.show()

    rho_slider.observe(update, names='value')
    L_slider.observe(update, names='value')
    A_slider.observe(update, names='value')
    update()

    display(widgets.VBox([
        widgets.HTML(
            "<b>Ecuación de la resistencia — R = ρ · L / A</b>"
            "<br><small style='color:grey'>La Ley de Ohm es V = R·I — "
            "este widget muestra cómo la geometría y el material controlan R</small>"),
        rho_slider, L_slider, A_slider, out
    ]))

resistance_widget()
```

---

## Valores típicos de resistividad

Consulta la [tabla de referencia de EMGeoSci](https://em.geosci.xyz/content/physical_properties/electrical_conductivity/electrical_conductivity_values.html) para una visión completa de los rangos de resistividad de los materiales terrestres más comunes.

```{figure} ../../assets/images/resistivity_table1.png
:name: fig-timeline-2
:width: 100%
:align: center
Visión general de los rangos de resistividad para materiales terrestres comunes (tabla de referencia EMGeoSci).
```
