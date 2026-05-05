---
title: Ejercicio 2 ➡️ Diseño de un sondeo TRE
authors:
  - name: Benjamin Mary
    email: benjamin.mary@ica.csic.es
    affiliations:
      - ICA-CSIC, Madrid, España
---
````{tip} Por qué importa el modelado directo
Antes de ir al campo, el modelado directo permite simular datos TRE sobre un modelo sintético del subsuelo. Es un paso crítico para:
- Elegir el espaciado de electrodos y el tipo de dispositivo apropiados
- Evaluar la sensibilidad del sondeo a la anomalía objetivo
- Anticipar posibles artefactos o límites de resolución
- Optimizar el diseño del sondeo antes de comprometer recursos
````

---

## Parte 1 — Crear un modelo de resistividad por capas

Usando ResIPy, construye un modelo de subsuelo de tres capas que represente la siguiente estratigrafía:

| Capa | Material | Profundidad (m) | Resistividad (Ω·m) |
|---|---|---|---|
| 1 | Ceniza | 0 a −0,5 | 1500 |
| 2 | Suelo | −0,5 a −2,0 | 150 |
| 3 | Roca madre | −2,0 a −5,0 | 1000 |

1. Define la geometría de cada capa como un polígono.
2. Asigna un valor de resistividad a cada región.
3. Ejecuta un modelo directo con **5% de ruido gaussiano**.
4. Invierte los datos sintéticos y compara el resultado con el modelo verdadero.

````{dropdown} Respuesta — Resultado esperado
```{figure} ../assets/images/conceptual_model_layers.png
:width: 100%
:align: center
:alt: Modelo conceptual por capas con ceniza, suelo y roca madre
Modelo conceptual por capas: ceniza (superior), suelo (medio), roca madre (inferior).
```
````

````{dropdown} Solución con la interfaz gráfica de ResIPy
1. Abre ResIPy y crea un nuevo proyecto.
2. Ve a **Modelo > Añadir región** y dibuja manualmente el polígono de cada capa.
3. Asigna los valores de resistividad en el panel de propiedades de la región.
4. Ejecuta **Directo > Simular** con ruido al 5%.
5. Ejecuta la **Inversión** e inspecciona los resultados con **Mostrar resultados**.
````

````{dropdown} Solución con ResIPy — Código Python
```python
import numpy as np

x_min, x_max = -1, 12
z1 = -0.5   # base de la capa de ceniza
z2 = -2.0   # base de la capa de suelo
z3 = -5.0   # fondo del modelo (roca madre)

# Polígonos de capas (cerrados, sentido antihorario)
layer_ash = np.array([
    [x_min, 0],
    [x_max, 0],
    [x_max, z1],
    [x_min, z1],
    [x_min, 0]
])

layer_soil = np.array([
    [x_min, z1],
    [x_max, z1],
    [x_max, z2],
    [x_min, z2],
    [x_min, z1]
])

layer_bedrock = np.array([
    [x_min, z2],
    [x_max, z2],
    [x_max, z3],
    [x_min, z3],
    [x_min, z2]
])

# Asignar valores de resistividad a cada región
k.addRegion(layer_ash,     res0=1500, iplot=True)  # Ceniza — alta resistividad
k.addRegion(layer_soil,    res0=150,  iplot=True)  # Suelo — resistividad moderada
k.addRegion(layer_bedrock, res0=1000, iplot=True)  # Roca madre — resistiva

# Modelado directo con 5% de ruido
k.forward(noise=0.05, iplot=True)

# Inversión
k.invert()

# Visualizar resultados
k.showResults(index=0, electrodes=False, hor_cbar=False)  # Modelo verdadero
k.showResults(index=1, electrodes=False)                  # Modelo invertido
```
````

---

## Parte 2 — Espaciado óptimo de electrodos para una anomalía objetivo

La figura siguiente muestra una anomalía del subsuelo que se desea caracterizar.

````{figure} ../assets/images/design_electrode_geom.png
:width: 100%
:align: center
:alt: Geometría de la anomalía objetivo para el diseño del espaciado de electrodos
Anomalía objetivo utilizada para guiar la selección del espaciado de electrodos.
````

A partir de esta geometría, responde las siguientes preguntas:

1. ¿Qué espaciado de electrodos `a` elegirías para resolver esta anomalía? Justifica tu elección.
2. ¿Cómo se relaciona la **profundidad de investigación** con el espaciado de electrodos para un dispositivo Wenner?
3. ¿Cuál es el compromiso entre usar un espaciado **pequeño** frente a uno **grande**?

````{dropdown} Respuesta
1. El espaciado de electrodos debe ser del orden de la **dimensión lateral de la anomalía o menor** — típicamente `a ≤ ancho del objetivo / 2` para garantizar una resolución horizontal adecuada.
2. Para un dispositivo Wenner, la profundidad de investigación aproximada es **z ≈ 0,5 × a** (regla general). Mayor espaciado → mayor profundidad, pero menor resolución.
3. Compromiso:
   - **Espaciado pequeño:** alta resolución en superficie, penetración limitada en profundidad
   - **Espaciado grande:** mayor profundidad, pero anomalías más suavizadas y menos resueltas
````

---

## Parte 3 — Crear una malla 2D

Usando ResIPy, genera una malla de elementos finitos 2D adecuada para el modelado directo de la geometría definida en la Parte 1.

1. ¿Qué parámetros de malla controlan la resolución cerca de la superficie frente a la profundidad?
2. ¿Cómo debe ajustarse la densidad de malla cerca de las posiciones de los electrodos?
3. Ejecuta la malla y verifica visualmente antes de lanzar el modelo directo.

````{dropdown} Respuesta
- Usa **elementos más finos cerca de la superficie** y de las posiciones de los electrodos para capturar gradientes pronunciados.
- Aumenta el tamaño de los elementos con la profundidad para reducir el tiempo de cálculo sin sacrificar precisión.
- En ResIPy: `k.createMesh(typ='trian', surface=..., cl=0.1, cl_factor=5)` — `cl` controla el tamaño de los elementos en superficie, `cl_factor` controla el engrosamiento en profundidad.
- Inspecciona siempre la malla con `k.showMesh()` antes de ejecutar los modelos directo o inverso.
````
