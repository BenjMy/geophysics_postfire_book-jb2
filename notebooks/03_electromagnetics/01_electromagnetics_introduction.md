---
title: "EM mapping"
kernelspec:
  name: python3
  display_name: Python 3 (Geophysics)
  language: python
---

```{admonition} Learning Objectives
:class: note
- Understand the physical basis of magnetic permeability, electrical permitivity and conductivity
```

While conductivity is the generally the main physical property of interest, EM induction methods also depend on the magnetic permeability and electrical permitivity of rocks. Their importance depends upon the frequency of the EM signal used for given a system.

Electromagnetic survey methods are based on two fundamental principles: 
(i) Faraday’s law of electromagnetic induction and the fact that electric currents generate magnetic fields, expressed in Ampère’s law. In its simplest form Faraday’s law states that the electromotive force (EMF) in a closed circuit is proportional to the rate of change of magnetic flux through the circuit, or in even simpler terms: a changing magnetic field will induce an EMF.


{cite}`boaga2017use` 


## EMI Measurement Principle

An EMI instrument consists of a **transmitter coil** and one or more **receiver coils** separated by a fixed distance (coil spacing $s$).

The transmitter generates a **primary magnetic field** $H_p$ that induces eddy currents in the ground. These currents generate a **secondary field** $H_s$ measured at the receiver. The ratio $H_s / H_p$ relates to the bulk apparent electrical conductivity (ECa, mS/m):

$$ECa = \frac{4}{\omega \mu_0 s^2} \cdot \text{Im}\!\left(\frac{H_s}{H_p}\right)$$

where $\omega = 2\pi f$ is the angular frequency and $\mu_0$ is the magnetic permeability of free space.

---

## Coil Orientations

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt

# Sensitivity functions (McNeill 1980)
def sensitivity_HCP(z, s=1.0):
    """Horizontal coplanar (HCP) — vertical dipole."""
    return (4*z**3) / (4*z**2 + s**2)**1.5

def sensitivity_VCP(z, s=1.0):
    """Vertical coplanar (VCP) — horizontal dipole."""
    return (2*z) / (4*z**2 + s**2)**0.5 - (4*z**3) / (4*z**2 + s**2)**1.5

z = np.linspace(0.01, 3, 300)

fig, ax = plt.subplots(figsize=(7, 5))
ax.plot(sensitivity_HCP(z), z, label='HCP (vertical dipole)', color='steelblue', linewidth=2)
ax.plot(sensitivity_VCP(z), z, label='VCP (horizontal dipole)', color='firebrick', linewidth=2, linestyle='--')
ax.set_xlabel("Relative sensitivity")
ax.set_ylabel("Depth / coil spacing ratio (z / s)")
ax.set_ylim(3, 0)
ax.set_title("McNeill (1980) depth sensitivity functions")
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```





```{figure} ../../assets/images/fsoil-04-1239497-g001.png
:name: fig-fsoilEM1
:width: 100%
:align: center
fsoilEM1 from {cite}`mclachlan2021emagpy` 
```
```{figure} ../../assets/images/fsoil-04-1239497-g002.png
:name: fig-fsoilEM2
:width: 100%
:align: center
fsoilEM2 from {cite}`mclachlan2021emagpy` 
```

