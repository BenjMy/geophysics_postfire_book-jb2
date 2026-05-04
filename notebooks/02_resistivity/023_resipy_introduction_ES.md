---
title: "Procesamiento con ResIPy"
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

# Introducción a ResIPy

## Descripción general

**ResIPy** (también denominado *resipy*) es un envoltorio de Python en torno a los robustos códigos de inversión **R2 / cR2 / R3t / cR3t** para tomografía de resistividad eléctrica (ERT) e inducción polarizada (IP) en 2D y 3D. Proporciona tanto una **interfaz gráfica de usuario (GUI) independiente** como una **API de Python** diseñada para su uso en cuadernos Jupyter.

```{note} Objetivos de aprendizaje

Al finalizar este cuaderno serás capaz de:

- Instalar ResIPy correctamente en **Windows**, Linux y macOS
- Crear y configurar un objeto `Project`
- Importar datos de campo y visualizar una **pseudosección**
- Filtrar mediciones ruidosas o defectuosas
- Ajustar un **modelo de error** a tus datos
- Construir una **malla** y ejecutar una inversión regularizada
- Visualizar e interpretar la sección de resistividad invertida
```

> **Cita:** Blanchy G., Saneiyan S., Boyd J., McLachlan P. and Binley A. 2020.
> *ResIPy, an Intuitive Open Source Software for Complex Geoelectrical Inversion/Modeling.*
> Computers & Geosciences, 104423. <https://doi.org/10.1016/j.cageo.2020.104423>

---

## Instalación

ResIPy puede instalarse de tres maneras según tu sistema operativo y necesidades.
**Los usuarios de Windows tienen la experiencia más sencilla** — los binarios de inversión son ejecutables nativos de Windows y no se requiere software adicional.

---

#### Opción A — Ejecutable independiente (sin Python, recomendado para este curso)

Es la forma más rápida de probar ResIPy sin instalar nada más.

1. Ve a la [página de versiones de ResIPy](https://gitlab.com/hkex/resipy/-/releases) en GitLab.
2. Descarga el último **`ResIPy_x.x.x_windows.zip`**.
3. Extrae el zip en una carpeta de tu elección (p. ej. `C:\ResIPy`).
4. Haz doble clic en **`ResIPy.exe`** para iniciar la GUI.

```{warning} Advertencia de Windows SmartScreen
Si ves *"Windows protegió tu PC"*, haz clic en **Más información** → **Ejecutar de todas formas**.
Esto aparece porque el ejecutable no está firmado con un certificado comercial — es
seguro continuar. Es posible que también debas añadir una excepción en tu programa antivirus.
```

#### Opción B — API de Python mediante pip

Necesitas **Python 3.9 o superior**. Si no tienes Python, instala primero
[Miniconda para Windows](https://docs.conda.io/en/latest/miniconda.html) — una distribución
ligera de Python que también proporciona el gestor de paquetes `conda`. Durante la instalación,
marca **"Añadir Miniconda a mi PATH"** si se te solicita.

Una vez instalado Miniconda, abre **Anaconda Prompt** (búscalo en el menú Inicio)
y ejecuta los siguientes comandos **uno por uno**:

```bat

:: Paso 1 — Crear un entorno dedicado (mantiene este curso aislado)
conda create -n geophysics-course python=3.10

:: Paso 2 — Activar el entorno
conda activate geophysics-course

:: Paso 3 — Instalar el núcleo científico mediante conda
conda install numpy scipy matplotlib pandas jupyter jupyterlab ipykernel ipywidgets

:: Paso 4 — Instalar ResIPy desde PyPI
pip install resipy

:: Paso 5 — Verificar la instalación
python -c "from resipy import Project; print('ResIPy OK')"
```

```{tip} Buenas noticias para los usuarios de Windows
En **Windows**, ResIPy incluye los binarios de inversión (`R2.exe`, `cR2.exe`, `R3t.exe`,
`cR3t.exe`) compilados de forma nativa para Windows. **No se necesita Wine ni software adicional.**
Puedes ejecutar inversiones completas inmediatamente tras `pip install resipy`.
```

En **Linux / macOS** es posible que veas adicionalmente:

```
Warning: Wine is not installed!
```

Esto es esperado si Wine aún no está configurado. Consulta la Sección 8 (Resolución de problemas) para solucionarlo.

---

## Flujo de trabajo mínimo completo

# Tutorial básico de R2


En este tutorial aprenderás a usar la API de Python de los códigos R* (http://www.es.lancs.ac.uk/people/amb/Freeware/R2/R2.htm).
Comienza importando la clase maestra `Project` desde la API (Interfaz de Programación de Aplicaciones).

+++

### 1 Importaciones básicas

Importa los paquetes básicos y la API de R2 como módulo (nota: deberás cambiar la ruta, aquí asumimos que lanzaste Jupyter desde dentro de la carpeta /examples/jupyter-notebook).

```{code-cell} python
%matplotlib inline
import warnings
warnings.filterwarnings('ignore')
import os
testdir = '../../assets/complementary_data/dc-2d/'
from resipy import Project
```

+++

### 2 Crear un objeto 'Project', importar datos y representar la pseudosección

> La clase `Project` se denominaba clase `R2` en versiones anteriores de ResIPy.

El primer paso es crear un objeto a partir de la clase `Project`, llamémoslo ```k```. Este es el objeto principal con el que vamos a interactuar. El segundo paso es leer los datos de un archivo de campaña. Aquí elegimos un archivo CSV del Syscal Pro que contiene únicamente datos de resistividad. Ten en cuenta que al importar los datos de campaña, el objeto busca automáticamente mediciones recíprocas y calculará un error recíproco con las que encuentre.

```{code-cell} python
k = Project(typ='R2') # crear un objeto Project en un directorio de trabajo (también se puede establecer con k.setwd())
k.createSurvey(testdir + 'syscal.csv', ftype='Syscal') # leer el archivo de campaña
```

Podemos representar la pseudosección y mostrar los errores basados en mediciones recíprocas.

```{code-cell} python
k.showPseudo()
k.showError() # representar los errores recíprocos
```

+++

### 3 Filtrado de datos

A continuación se muestran algunos ejemplos de rutinas de filtrado de datos que pueden utilizarse:
- `k.filterUnpaired()` para eliminar mediciones sin pareja (es decir, mediciones sin recíproca) -> podrían ser mediciones ficticias en una configuración dipolo-dipolo
- `k.filterElec([5])` para eliminar un electrodo específico (p. ej., aquí se eliminan todos los cuadrupolos con el electrodo 5)
- `k.filterRecip(20)` para eliminar mediciones en función de su error recíproco relativo (p. ej., todos los cuadrupolos con un error recíproco > 20% se descartan).
Un filtrado de datos más avanzado puede lograrse usando el método `filterData()` de la clase `Survey`. Este método permite filtrar cuadrupolos específicos. Se puede acceder a una versión interactiva mediante el método `filterManual()`, que genera una pseudosección interactiva en la interfaz.

```{code-cell} python
k.filterUnpaired()
k.showPseudo() # esto elimina las mediciones ficticias en esta campaña dipolo-dipolo (añadidas para optimizar la velocidad)
```

```{code-cell} python
k.filterElec([5]) # eliminar todos los cuadrupolos asociados al electrodo 5
k.showPseudo()
```

```{code-cell} python
k.filterRecip(percent=20) # en este caso solo se elimina un cuadrupolo con error recíproco mayor del 20 por ciento
k.showPseudo()
```

+++

### 4 Ajuste de un modelo de error

Hay diferentes modelos de error disponibles para ajustar datos de corriente continua (DC):
- un modelo lineal simple: `k.fitErrorLin()`
- un modelo de ley de potencias: `k.fitErrorPwl()`
- un modelo lineal de efectos mixtos: `k.fitErrorLME()` (solo en Linux con un kernel de R instalado)
Cada uno de ellos creará una nueva columna de error en el objeto `Survey` que se usará en la inversión si `k.err = True`.


```{code-cell} python
k.fitErrorLin()
```

```{code-cell} python
k.fitErrorPwl()
```

+++

### 5 Malla

En 2D se pueden crear dos tipos de malla:
- una malla cuadrilateral (`k.createMesh('quad')`)
- una malla triangular (`k.createmesh('trian')`)
En 3D, solo se puede crear una malla tetraédrica mediante `k.createMesh('tetra')`.

```{code-cell} python
k.createMesh(typ='quad') # generar malla cuadrilateral (predeterminada para campaña 2D)
k.showMesh()
```

```{code-cell} python
k.createMesh('trian', show_output=False) # esto llama a gmsh.exe para crear la malla
k.showMesh()
```

+++

### 7 Inversión

La inversión se lleva a cabo en el directorio de trabajo especificado del objeto R2, indicado la primera vez que se llama a `k = R2(<workingDirectory>)`. Se puede cambiar posteriormente usando `k.setwd(<newWorkingDirectory>)`.
Los parámetros de la inversión se definen en un diccionario en `k.param` y pueden ser modificados manualmente por el usuario (p. ej. `k.param['a_wgt'] = 0.01`). Todos los parámetros tienen valores predeterminados y sus nombres siguen el manual de R2. El archivo `.in` se escribe automáticamente cuando se llama al método `k.invert()`.

```{code-cell} python
k.param['data_type'] = 1 # usar el logaritmo de la resistividad
k.err = True # si queremos usar el error de los modelos de error ajustados anteriormente
k.invert() # esto realizará la inversión
```

+++

### 8 Visualización de resultados y postprocesado

Los resultados pueden mostrarse con `k.showResults()`. Se pueden pasar múltiples argumentos al método para reescalar la barra de colores, mostrar o no la sensibilidad, cambiar el atributo o representar contornos. Los errores de la inversión también pueden representarse usando `k.pseudoError()` o `k.showInvError()`.

```{code-cell} python
k.showResults(attr='Resistivity(ohm.m)', sens=False, contour=True, vmin=30, vmax=100)
```

```{code-cell} python
k.showPseudoInvError() # permite ver si algunos electrodos presentan un error mayor
```

```{code-cell} python
k.showInvError() # todos los errores deberían estar entre -3 y 3
```


---

## Videotutoriales

El equipo de ResIPy mantiene un canal oficial de YouTube con tutoriales paso a paso.

:::{iframe} https://www.youtube.com/embed/wfJ62rz0EsU?si=K32bWdkjYoZWRdRN
:width: 60%
API de Python de ResIPy — Primeros pasos
:::

:::{iframe} https://www.youtube.com/embed/48VN_e8J2kc?si=vH4NVe1OHKQsGf0P
:width: 60%
Introducción al modelado directo 2D con ResIPy
:::

:::{iframe} https://www.youtube.com/embed/OjZlRZ7QeMk?si=o0VImy3k-X_jDYbM
:width: 60%
Introducción a la inversión 2D con ResIPy
:::

---

## Resumen

```{tip} Lo que has aprendido

| Paso | Método | Propósito |
|------|--------|-----------|
| 1 | `Project(typ='R2')` | Crear proyecto |
| 2 | `createSurvey(file, ftype=...)` | Cargar datos de campo |
| 3 | `showPseudo()` / `showError()` | Inspeccionar la calidad de los datos |
| 4 | `filterUnpaired()` / `filterRecip()` / `filterElec()` | Eliminar datos defectuosos |
| 5 | `fitErrorLin()` / `fitErrorPwl()` | Ajustar modelo de error |
| 6 | `createMesh(typ='trian')` | Construir malla de elementos finitos |
| 7 | `invert()` | Ejecutar inversión regularizada |
| 8 | `showResults()` / `showInvError()` | Visualizar y validar resultados |

**Resumen por plataforma:**
- **Windows** — binarios nativos, no se necesita Wine, soporte completo de inversión desde el principio
- **Linux / macOS** — instala Wine (`sudo apt install wine-stable` o `brew install --cask wine-stable`) para el paso de inversión

**Siguiente cuaderno:** [Introducción a emagpy](01_emagpy_introduction.md) — procesa datos de **inducción electromagnética** con emagpy.
```

---

## Recursos adicionales

- [Documentación oficial de ResIPy](https://hkex.gitlab.io/resipy/)
- [Repositorio GitLab y versiones de ResIPy](https://gitlab.com/hkex/resipy)
- [ResIPy en PyPI](https://pypi.org/project/resipy/)
- [Canal de YouTube de ResIPy](https://www.youtube.com/channel/UCkg2drwtfaVAo_Tuyeg_z5Q)
- [Código de inversión R2 — Universidad de Lancaster](http://www.es.lancs.ac.uk/people/amb/Freeware/R2/R2.htm)
