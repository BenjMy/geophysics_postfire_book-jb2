---
title: "Procesamiento con EMagPy"
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

# Introducción a EMagPy

---

## Descripción general

**EMagPy** es un paquete de Python para el procesamiento e inversión de datos EMI. Proporciona
tanto una **interfaz gráfica de usuario (GUI) independiente** como una **API de Python** diseñada
para su uso en cuadernos Jupyter. La clase principal es `Problem`.

```{note} Objetivos de aprendizaje

Al finalizar este cuaderno serás capaz de:

- Instalar EMagPy e importar la clase `Problem`
- Cargar datos de campo e inspeccionar el formato CSV
- Visualizar perfiles y mapas de ECa
- Definir un modelo de partida y ejecutar una inversión 1D
- Visualizar perfiles de conductividad invertida en profundidad y secciones horizontales
```

> **Cita:** McLachlan P., Blanchy G. and Binley A. 2021.
> *EMagPy: Open-source, platform-independent processing and inversion of electromagnetic induction data.*
> Computers & Geosciences, 146, 104561. <https://doi.org/10.1016/j.cageo.2020.104561>

---

## Instalación

EMagPy puede instalarse de tres maneras según tus necesidades.

#### Opción A — Ejecutable independiente (sin Python, recomendado para este curso)

1. Ve a la [página de versiones de EMagPy](https://gitlab.com/hkex/emagpy/-/releases) en GitLab.
2. Descarga el último **`EMagPy_x.x.x_windows.zip`**.
3. Extrae el zip y haz doble clic en **`EMagPy.exe`** para iniciar la GUI.

```{warning} Advertencia de Windows SmartScreen
Si ves *"Windows protegió tu PC"*, haz clic en **Más información** → **Ejecutar de todas formas**.
El ejecutable no está firmado comercialmente pero es seguro de usar.
```

#### Opción B — pip (recomendado para scripts y Jupyter)

```bash
pip install emagpy
```

---

## Flujo de trabajo mínimo completo

+++

### 1 Importaciones

```{code-cell} python
import os
import numpy as np
import pandas as pd
from emagpy import Problem  # clase principal
testdir = '../../assets/complementary_data/cover-crop/'
```

+++

### 2 Cargar datos e inspeccionar el formato

EMagPy importa datos de un archivo `.csv` donde **las cabeceras de columna son las
configuraciones de bobinas** (p. ej. `VCP0.71`, `HCP1.48`). Cada fila corresponde a una
localización de medición.

```{code-cell} python
k = Problem()                              # crear el objeto principal
k.createSurvey(testdir + 'coverCrop.csv') # importar los datos
```

```{code-cell} python
df = pd.read_csv(testdir + 'coverCrop.csv')
df.head()  # inspeccionar el formato de las cabeceras
```

+++

### 3 Visualización de datos

`Problem.show()` representa la ECa como un gráfico de líneas por configuración de bobina.
Si hay coordenadas espaciales (`x`, `y`) disponibles, `Problem.showMap()` produce un
mapa de conductividad eléctrica aparente (ECa) en planta.

```{code-cell} python
k.show(vmax=50)
```

```{code-cell} python
k.showMap(coil='VCP0.71', contour=True, pts=True)
```

+++

### 4 Modelo de partida

Antes de la inversión, define un modelo en capas de partida: la **profundidad inferior de cada
capa** y un valor inicial de conductividad eléctrica para cada capa
(incluido el semisespacio inferior).

```{code-cell} python
k.setInit(
    depths0=[0.5, 1],           # base de cada capa (m) — la última capa es infinita
    conds0=[20, 20, 20],        # conductividad de partida (mS/m) por capa
    fixedConds=[False, False, False]
)
```

+++

### 5 Modelos directos y solvers

Hay varios modelos directos disponibles, con diferentes compromisos entre precisión y velocidad:

| Modelo | Descripción |
|---|---|
| `CS` | Sensibilidad acumulada (McNeill 1980) — predeterminado, más rápido |
| `CSgn` | CS con solver de Gauss-Newton — usa `invertGN()` automáticamente |
| `FSlin` | Solución completa (Maxwell) con aproximación de número de inducción bajo (LIN) |
| `FSeq` | Solución completa sin LIN — ECa aparente mediante optimización (Andrade et al. 2016) |
| `Q` | Solución completa minimizando directamente la cuadratura — preferida para ECa > 100 mS/m |

Hay disponibles dos familias de solvers:

- **Basados en gradiente** (`L-BFGS-B`, `TNC`, `CG`, `Nelder-Mead`) mediante `scipy.optimize.minimize()`
- **Basados en MCMC** (`ROPE`, `SCEUA`, `DREAM`) mediante `spotpy` — adecuados cuando las profundidades de las capas son parámetros libres

+++

### 6 Inversión

```{code-cell} python
k.invert()       # predeterminado: modelo directo CS, solver L-BFGS-B
k.showResults()  # sección de conductividad invertida en profundidad
k.showMisfit()   # desajuste de datos por bobina
k.showOne2one()  # ECa observada frente a predicha
```

+++

### 7 Secciones horizontales

Si hay coordenadas espaciales disponibles, `showSlice()` produce mapas en planta
de la conductividad a un índice de capa determinado.

```{code-cell} python
k.showSlice(islice=0, contour=True, vmin=12, vmax=50)  # capa superior
k.showSlice(islice=2, contour=True, vmin=12, vmax=50)  # capa inferior
```

Consulta la cadena de documentación del método para todas las opciones disponibles:

```{code-cell} python
:tags: [hide-output]
help(k.showSlice)
```

---

## Resumen

```{tip} Lo que has aprendido

| Paso | Método | Propósito |
|------|--------|-----------|
| 1 | `Problem()` | Crear el objeto principal |
| 2 | `createSurvey(file)` | Cargar datos de campo |
| 3 | `show()` / `showMap()` | Visualizar datos de ECa |
| 4 | `setInit(depths0, conds0)` | Definir modelo de partida |
| 5 | `invert()` | Ejecutar inversión 1D |
| 6 | `showResults()` / `showMisfit()` / `showOne2one()` | Evaluar la calidad de la inversión |
| 7 | `showSlice()` | Mapas de conductividad en planta |

**Siguiente cuaderno:** [Procesamiento ERT con ResIPy](nb_resipy.md) — procesa datos de **tomografía de resistividad eléctrica** con ResIPy.
```

---

## Recursos adicionales

- [Documentación oficial de EMagPy](https://hkex.gitlab.io/emagpy/)
- [Repositorio GitLab de EMagPy](https://gitlab.com/hkex/emagpy)
- [EMagPy en PyPI](https://pypi.org/project/emagpy/)
