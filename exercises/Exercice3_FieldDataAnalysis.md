---
title: Exercice 3 ➡️ Field Data Analysis
authors:
  - name: Benjamin Mary
    email: benjamin.mary@ica.csic.es
    affiliations:
      - ICA-CSIC, Madrid, Spain
kernelspec:
  name: python3
  display_name: Python 3 (Geophysics)
  language: python
  
---


# Plot the data 

- Go to the github and download the example files: Majadas.dat



```{figure} ../assets/images/ERT_dehesas.jpg
:name: fig-ert
:width: 75%
:align: center

ERT survey in a Mediterranean dehesa. Multi-electrode arrays measure apparent resistivity along transects to image soil structure and moisture distribution.
```

```{figure} ../assets/images/EM_antenna_short.jpg
:name: fig-em-antenna
:width: 75%
:align: center

EMI antenna being towed across a burned area. The instrument measures apparent electrical conductivity continuously, enabling rapid spatial mapping.
```



```{code-cell} ipython3
:tags: [hide-input]
import warnings
warnings.filterwarnings('ignore')
import os
import sys
sys.path.append((os.path.relpath('../src'))) # add here the relative path of the API folder

import numpy as np # numpy for electrode generation
from resipy import Project
k = Project(typ='R2') # create R2 object
elec = np.zeros((24,3))
elec[:,0] = np.arange(0, 24*0.5, 0.5) # with 0.5 m spacing and 24 electrodes
k.setElec(elec)
print(k.elec)
k.createMesh(typ='trian', show_output=False, res0=200) # let's create the mesh based on these electrodes position
k.showMesh()
k.addRegion(np.array([[2,-0.3],[2,-2],[3,-2],[3,-0.3],[2,-0.3]]), 50, iplot=True)
k.createSequence([('dpdp', 1, 10, 1, 10)]) # create a dipole-dipole of diple spacing of 1 (=skip 0) with 10 levels
k.forward(noise=0.05, iplot=True) # forward modelling with 5 % noise added to the output

```
