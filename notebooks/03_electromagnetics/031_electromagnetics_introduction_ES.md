---
title: "Cartografía EM"
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
- Comprender las bases físicas de la permeabilidad magnética, la permitividad eléctrica y la conductividad eléctrica
- Aprender cómo los instrumentos de inducción electromagnética (EMI) miden la conductividad eléctrica aparente (ECa)
- Entender cómo la orientación y la separación de las bobinas controlan la profundidad de investigación
- Conocer cómo los instrumentos multibobina multifrecuencia muestrean múltiples profundidades simultáneamente
```

---

## Fundamento físico

Los métodos de prospección electromagnética (EM) se basan en la **ley de Faraday** de la inducción:
un campo magnético variable induce una fuerza electromotriz (FEM) en cualquier conductor
cercano. Un campo magnético variable en el tiempo genera corrientes de Foucault en el
subsuelo, y esas corrientes revelan las propiedades del subsuelo.

Aunque la conductividad eléctrica $\sigma$ (S/m) es la propiedad de
interés principal, los métodos EM también dependen de:

- La permeabilidad magnética $\mu$ — con qué facilidad se magnetiza un material
  (importante en suelos y rocas magnéticamente susceptibles)
- La permitividad eléctrica $\varepsilon$ — cuánta energía eléctrica almacena
  un material (predomina a altas frecuencias, p. ej. GPR)

A bajas frecuencias (< 100 kHz), la conductividad domina. A altas frecuencias,
la permitividad toma el relevo ({cite}`boaga2017use`).

---

## Principio de medición

### De la antena al subsuelo

Una bobina transmisora — un bucle de cable que transporta corriente alterna — actúa como
antena. La corriente oscilante genera un **campo magnético primario** $H_p$ variable en
el tiempo que se irradia hacia el subsuelo.

Cuando $H_p$ penetra en un cuerpo conductivo, induce **corrientes de Foucault** — pequeños
bucles de corriente eléctrica que circulan dentro del conductor. Estas generan un
**campo secundario** $H_s$. Una bobina receptora detecta la superposición de $H_p$
y $H_s$. Como $H_p$ es conocido, $H_s$ puede aislarse — y contiene
información sobre la conductividad del subsuelo.


```{figure} ../../assets/images/fsoil-04-1239497-g001
:name: fig-fsoilEM1
:width: 100%
:align: center
Ejemplo de mapas de ECa obtenidos con múltiples configuraciones de bobinas adquiridas
simultáneamente con un instrumento EMI multibobina. De {cite}`mclachlan2021emagpy`.
```


### Conductividad eléctrica aparente

Bajo la hipótesis del **número de inducción bajo (LIN)** — válida cuando la
separación entre bobinas $s \ll$ profundidad de penetración — la conductividad
eléctrica aparente ECa (mS/m) es:

$$ECa = \frac{4}{\omega \mu_0 s^2} \cdot \text{Im}\!\left(\frac{H_s}{H_p}\right)$$

donde $\omega = 2\pi f$ es la frecuencia angular y $\mu_0$ la
permeabilidad magnética del vacío.

:::{note}
La aproximación de número de inducción bajo deja de ser válida en suelos
muy conductivos (ECa > ~100 mS/m). En esos casos debe usarse la inversión con solución completa.
:::

---

## Instrumentos multibobina y multifrecuencia

Un par transmisor-receptor a una sola frecuencia y una sola separación proporciona un
único valor de ECa — una media ponderada en profundidad de la conductividad sobre un
volumen amplio. Para obtener un **perfil de conductividad en profundidad**, los instrumentos
modernos de dominio de frecuencia (FDEM) combinan múltiples configuraciones simultáneamente:

- **Múltiples separaciones entre bobinas** $s_1, s_2, \dots$ — mayor separación → mayor
  profundidad de investigación
- **Múltiples frecuencias** $f_1, f_2, \dots$ — menor frecuencia → mayor
  profundidad de penetración → mayor penetración

Cada combinación proporciona un valor de ECa a una profundidad efectiva diferente, generando
un conjunto de mediciones independientes por localización que pueden invertirse conjuntamente
para obtener un perfil de conductividad en profundidad.


```{figure} ../../assets/images/fsoil-04-1239497-g002
:name: fig-fsoilEM2
:width: 100%
:align: center
Principio de medición EMI — campo primario $H_p$, corrientes de Foucault inducidas y
campo secundario $H_s$. De {cite}`mclachlan2021emagpy`.
```



<!--
```{figure} ../../assets/images/placeholder_multicoil_depth.png
:name: fig-multicoil-depth
:width: 75%
:align: center
Curvas de sensibilidad acumulada para múltiples separaciones de bobinas en modo HCP —
el aumento de la separación amplía la profundidad de investigación. *[figura por añadir]*
```
-->

---

## Orientaciones de las bobinas

Se utilizan dos configuraciones estándar, cada una con un perfil de **sensibilidad en
profundidad** diferente (McNeill, 1980):

- **HCP — Coplanar Horizontal** (bobinas planas, dipolo magnético vertical):
  sensibilidad más profunda, máximo por debajo de la superficie — alcanza ~ $0.75\,s$
- **VCP — Coplanar Vertical** (bobinas en posición vertical, dipolo magnético horizontal):
  respuesta más superficial, mayor sensibilidad cerca de la superficie — alcanza ~ $0.5\,s$

<!--
```{figure} ../../assets/images/placeholder_coil_geometry.png
:name: fig-coil-geometry
:width: 70%
:align: center
Configuraciones de bobinas HCP y VCP con sus respectivas orientaciones de dipolo magnético.
*[figura por añadir]*
```
-->

```{code-cell} ipython3
:tags: [hide-input]
import numpy as np
import matplotlib.pyplot as plt

def sensitivity_HCP(z, s=1.0):
    return (4*z**3) / (4*z**2 + s**2)**1.5

def sensitivity_VCP(z, s=1.0):
    return (2*z) / (4*z**2 + s**2)**0.5 - (4*z**3) / (4*z**2 + s**2)**1.5

z = np.linspace(0.01, 3, 300)

fig, ax = plt.subplots(figsize=(7, 5))
ax.plot(sensitivity_HCP(z), z, label='HCP (dipolo vertical)', color='steelblue', linewidth=2)
ax.plot(sensitivity_VCP(z), z, label='VCP (dipolo horizontal)', color='firebrick', linewidth=2, linestyle='--')
ax.set_xlabel("Sensibilidad relativa")
ax.set_ylabel("Relación profundidad / separación de bobinas (z / s)")
ax.set_ylim(3, 0)
ax.set_title("Funciones de sensibilidad en profundidad de McNeill (1980)")
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```
