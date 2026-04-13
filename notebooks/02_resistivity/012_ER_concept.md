---
title: "Electrical Resistivity"
kernelspec:
  name: python3
  display_name: Python 3 (Geophysics)
  language: python
---
    
```{admonition} Learning Objectives
:class: note
- Understand the physical basis of electrical resistivity 
- Apply Ohm's Law in a geophysical context
- Electrical Resistivity ranges for common earth materials.
- Explore how soil properties control resistivity
```

---

## Soil physical properties

The electrical **resistivity** $\rho$ (Ω·m) describes how strongly a material opposes the flow of electric current. Its inverse is **conductivity** $\sigma$ (S/m):

$$\sigma = \frac{1}{\rho}$$

### Ohm's Law

For a homogeneous cylinder of cross-section $A$ (m²) and length $L$ (m):

$$R = \rho \frac{L}{A}$$

where $R$ is resistance (Ω). Rearranging:

$$\rho = R \frac{A}{L}$$
```{code-cell} ipython3
:tags: [remove-input]
import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display

def resistance(rho, L, A):
    """Ohm's Law: resistance of a homogeneous cylinder."""
    return rho * L / A

# Example: a 1 m³ cube of moist loam (rho ≈ 50 Ω·m)
rho_loam = 50   # Ω·m
R = resistance(rho_loam, L=1.0, A=1.0)
print(f"\033[96mResistance of 1 m3 loam cube : {R:.1f} Ω\033[0m")
```


Adjust resistivity, length and cross-section to see how resistance changes:
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
        side  = np.sqrt(A)          # side length of square cross-section

        with out:
            out.clear_output(wait=True)

            fig, axes = plt.subplots(1, 2, figsize=(10, 4))

            # ── Left: 3D-style sketch of the resistive element ──────────────
            ax = axes[0]
            ax.set_xlim(0, 10)
            ax.set_ylim(0, 6)
            ax.set_aspect('equal')
            ax.axis('off')

            # Normalise rho to a colour (low=blue/conductive, high=red/resistive)
            norm     = mcolors.LogNorm(vmin=1, vmax=1e6)
            cmap     = plt.cm.RdYlBu_r
            face_col = cmap(norm(rho))

            # Draw cuboid (isometric-style): front face + top face + right face
            w = min(max(side * 0.8, 0.5), 3.5)   # visual width (capped)
            h = min(max(side * 0.8, 0.5), 3.5)   # visual height (capped)
            d = min(max(L   * 0.6, 0.5), 5.0)    # visual depth = L

            ox, oy = 1.5, 1.0   # origin

            # Front face
            front = mpatches.FancyBboxPatch(
                (ox, oy), w, h,
                boxstyle='square,pad=0',
                facecolor=face_col, edgecolor='k', linewidth=1.5, zorder=2)
            ax.add_patch(front)

            # Top face (parallelogram)
            top_x = [ox, ox+w, ox+w+d*0.4, ox+d*0.4, ox]
            top_y = [oy+h, oy+h, oy+h+d*0.3, oy+h+d*0.3, oy+h]
            ax.fill(top_x, top_y, color=mcolors.to_rgba(face_col, 0.7),
                    edgecolor='k', linewidth=1.5, zorder=2)

            # Right face (parallelogram)
            right_x = [ox+w, ox+w+d*0.4, ox+w+d*0.4, ox+w, ox+w]
            right_y = [oy, oy+d*0.3, oy+h+d*0.3, oy+h, oy]
            ax.fill(right_x, right_y, color=mcolors.to_rgba(face_col, 0.5),
                    edgecolor='k', linewidth=1.5, zorder=2)

            # Dimension arrows & labels
            # L arrow (along depth direction)
            ax.annotate('', xy=(ox+d*0.4+0.1, oy-0.4),
                        xytext=(ox+0.0, oy-0.4),
                        arrowprops=dict(arrowstyle='<->', color='k', lw=1.5))
            ax.text(ox + d*0.2, oy-0.7, f'L = {L:.1f} m',
                    ha='center', fontsize=10, fontstyle='italic')

            # Colourbar for ρ
            sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
            sm.set_array([])
            cbar = fig.colorbar(sm, ax=ax, orientation='vertical',
                                fraction=0.03, pad=0.02,
                                label='ρ (Ω·m)')
            cbar.ax.tick_params(labelsize=8)

            ax.set_title('Resistive element geometry', fontsize=11, pad=8)

            # ── Right: result summary ────────────────────────────────────────
            ax2 = axes[1]
            ax2.axis('off')

            lines = [
                ('Equation',        r'$R = \rho \cdot \dfrac{L}{A}$',  14, 'black'),
                ('',                '',                                   8, 'black'),
                ('ρ (resistivity)', f'{rho:.2e} Ω·m',                   12, '#c0392b'),
                ('L (length)',      f'{L:.2f} m',                        12, '#2980b9'),
                ('A (cross-sect.)', f'{A:.4f} m²',                       12, '#27ae60'),
                ('',                '',                                    8, 'black'),
                ('R (resistance)',  f'{R:.4f} Ω',                        14, 'black'),
                ('σ (conductivity)',f'{sigma:.2e} S/m',                  12, '#7f8c8d'),
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

            # Note clarifying terminology
            ax2.text(0.05, 0.04,
                     '⚠ R = ρ·L/A is the resistance equation,\n'
                     '   not Ohm\'s law (V = R·I)',
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
            "<b>Resistance equation — R = ρ · L / A</b>"
            "<br><small style='color:grey'>Ohm's law is V = R·I — "
            "this widget shows how geometry and material control R</small>"),
        rho_slider, L_slider, A_slider, out
    ]))

resistance_widget()
```

---

## Typical resistivity values

See the [EMGeoSci reference table](https://em.geosci.xyz/content/physical_properties/electrical_conductivity/electrical_conductivity_values.html) for a comprehensive overview of resistivity ranges for common earth materials.

```{figure} ../../assets/images/resistivity_table1.png
:name: fig-timeline-2
:width: 100%
:align: center
Overview of resistivity ranges for common earth materials (EMGeoSci reference table). 
```


