---
title: "Tomografía de Resistividad Eléctrica (ERT)"
kernelspec:
  name: python3
  display_name: "Python 3 (Geophysics)"
  language: python
bibliography:
  - references.bib
authors:
  - name: Benjamin Mary
    email: benjamin.mary@ica.csic.es
    affiliations:
      - ICA-CSIC, Madrid, España
---

```{note} Objetivos de aprendizaje
- Explicar por qué una **configuración de 4 electrodos** separa la inyección de corriente de la medición de voltaje, y por qué esto elimina los errores de resistencia de contacto
- Definir la **resistividad aparente** (ρₐ) incluyendo el papel del factor geométrico K
- Comparar las **configuraciones de electrodos** más comunes (Wenner, Schlumberger, Dipolo-Dipolo) en términos de profundidad de sensibilidad y casos de uso típicos
- Describir el **flujo de trabajo de procesamiento ERT**
- Explicar por qué la inversión produce **un** modelo plausible del subsuelo y no **la** solución única
```

## ¿Qué es la ERT?

Anteriormente vimos que el suelo puede caracterizarse físicamente por su resistividad eléctrica. Aquí extendemos este concepto a la tomografía de resistividad eléctrica. La Tomografía de Resistividad Eléctrica (ERT, por sus siglas en inglés) es un método geofísico de subsuelo somero que permite caracterizar la distribución espacial de la **resistividad eléctrica** (o su inversa, la conductividad eléctrica) del subsuelo. A diferencia de las mediciones en sondeos o testigos de suelo — que son localizadas y destructivas — la ERT es **no invasiva**, proporciona **cobertura espacial 2D y 3D**, y puede repetirse a lo largo del tiempo para el seguimiento de **procesos dinámicos** (ERT en lapso temporal, o 4D).

Capacidades clave de un vistazo:
- Cartografía de contrastes de resistividad del subsuelo en **2D, 3D y a lo largo del tiempo** {cite}`dimech2022`
- Sensible a cambios en el **contenido de agua del suelo, salinidad, contenido en arcilla y temperatura** {cite}`telford1990,binley2005dc`
- Cierra la brecha entre los sensores puntuales dispersos y la teledetección a gran escala {cite}`carriere2022rs`

---

## Resistividad aparente y factor geométrico

En la Tomografía de Resistividad Eléctrica (ERT) y otros levantamientos de resistividad, se utiliza el **método de 4 electrodos** para medir la **resistividad aparente (ρₐ)** del subsuelo. Este método evita el problema de la **resistencia de contacto** y tiene en cuenta la **disposición geométrica** de los electrodos mediante el **factor geométrico (K)**.

El uso de cuatro electrodos separa los roles de **inyección de corriente** y **medición de voltaje**:

1. **Electrodos de corriente (A, B):**
   - Inyectan corriente en el terreno.
   - La resistencia de contacto en estos electrodos no afecta a la medición de voltaje porque éste se mide por separado.

2. **Electrodos de potencial (M, N):**
   - Miden la diferencia de potencial en el subsuelo.

```{figure} ../../assets/images/current-flow-lines-and-equipotential-lines-for-a-half-space
:name: fig-timeline-2
:width: 70%
:align: center
Fuente: Sharma (1997).
```

```{hint} ¿Por qué cuatro electrodos?
Al separar estos roles AB/MN, la medición es **insensible a la resistencia de contacto**, garantizando que ρₐ represente con precisión las condiciones del subsuelo.
Los electrodos de potencial absorben una **corriente despreciable** porque están conectados a un voltímetro de alta impedancia. Como resultado, la caída de tensión en su resistencia de contacto es insignificante, y el voltaje medido (Vₘₙ) refleja únicamente la resistividad del subsuelo.
```

### Resistividad aparente (ρₐ)

La **resistividad aparente (ρₐ)** es el valor de resistividad calculado a partir de las mediciones de campo utilizando cuatro electrodos. Se denomina «aparente» porque representa una **resistividad promedio** del volumen de subsuelo influenciado por la configuración de electrodos. El subsuelo raramente es homogéneo, por lo que ρₐ es un valor efectivo que simplifica la interpretación.

La resistividad aparente se calcula mediante la fórmula:

$$
\rho_a = K \cdot \frac{V_{MN}}{I_{AB}}
$$

- **ρₐ:** Resistividad aparente (Ω·m)
- **K:** Factor geométrico (m), que depende de la disposición de los electrodos
- **Vₘₙ:** Voltaje medido entre los electrodos de potencial M y N (V)
- **IAB:** Corriente inyectada entre los electrodos de corriente A y B (A)

---

## Diseño del levantamiento ERT y estrategia de secuencia

Elegir la secuencia de medición adecuada es fundamental: la configuración de electrodos controla la sensibilidad, la profundidad de investigación y la resolución.

```{figure} https://img.youtube.com/vi/IlqWXWprC1g/hqdefault.jpg
:width: 50%
:align: center
Medición Wenner (cuerpo resistivo) — Crédito [florianwagner4887](https://www.youtube.com/@florianwagner4887). [Ver en YouTube](https://www.youtube.com/watch?v=IlqWXWprC1g)
```
```{figure} https://img.youtube.com/vi/lt1qV-2d5Ps/hqdefault.jpg
:width: 50%
:align: center
Medición Dipolo-Dipolo (cuerpo resistivo) — Crédito [florianwagner4887](https://www.youtube.com/@florianwagner4887). [Ver en YouTube](https://www.youtube.com/watch?v=lt1qV-2d5Ps)
```
```{figure} https://img.youtube.com/vi/h0fnnpU5Pf8/hqdefault.jpg
:width: 50%
:align: center
Medición Schlumberger (cuerpo conductor) — Crédito [florianwagner4887](https://www.youtube.com/@florianwagner4887). [Ver en YouTube](https://www.youtube.com/watch?v=h0fnnpU5Pf8)
```

| Configuración | Patrón de sensibilidad | Caso de uso típico |
|--------------|------------------------|--------------------|
| Wenner | Somero, simétrico | Estructuras estratificadas |
| Schlumberger | Profundidad moderada, enfocado | Perfilado general |
| Dipolo-Dipolo | Profundo, alta resolución lateral | Fracturas, heterogeneidades |
| Polo-Dipolo | Asimétrico, profundo | Levantamientos entre sondeos |

La secuencia óptima, el espaciado de electrodos y los parámetros de inyección se determinan mediante un paso de **modelado directo a priori**: se asume un modelo plausible del subsuelo, se calculan datos sintéticos y se evalúa el rendimiento del array (resolución, intensidad de señal) antes de desplegarlo en campo {cite}`binley2005dc,blanchy2020cageo`.

---

## Flujo de trabajo de procesamiento ERT

Una cadena de procesamiento ERT estándar consta de los siguientes pasos:

1. **Adquisición de datos** – mediciones brutas de resistencia $R = \Delta V / I$
2. **Control de calidad** – filtrado de errores recíprocos, apilamiento, estimación del ruido
3. **Modelado del error** – asignación de incertidumbres a los datos (necesario para la inversión regularizada)
4. **Generación de malla** – malla de elementos finitos o diferencias finitas adaptada a la topografía y las posiciones de los electrodos
5. **Inversión** – minimización iterativa de una función de coste para recuperar el modelo de resistividad que ajusta los datos dentro de sus incertidumbres {cite}`blanchy2020cageo`
6. **Análisis de lapso temporal** – inversión independiente o por cociente/diferencia para resolver cambios en el subsuelo a lo largo del tiempo {cite}`dimech2022`

```{mermaid}
flowchart TD
    A["Adquisición — R = ΔV/I"]
    B["✅ Control de calidad — filtrado · apilamiento"]
    C["📊 Modelado del error — incertidumbres"]
    D["🔲 Malla — topografía · electrodos"]
    E["🔁 Inversión"]
    F["⏱️ Lapso temporal — diferencia · cociente"]

    A --> B --> C --> D --> E --> F
```

El paquete de código abierto **ResIPy** {cite}`blanchy2020cageo` (cuya API de Python es `resipy`) implementa los pasos 2–6 en un entorno único y fácil de usar.

---

## ¿Qué es la inversión en geofísica?

```{admonition}
:class: tip
Queremos saber qué hay **oculto en el subsuelo** sin excavar. Colocamos sensores en la superficie, registramos señales y trabajamos hacia atrás para encontrar qué subsuelo podría haberlas producido. Esto es la **inversión** — y es el motor matemático central de la mayor parte de la imagen geofísica.
```

El proceso opuesto — el **modelado directo** — parte de un subsuelo conocido y calcula cómo sería la señal en superficie. La inversión ejecuta esa lógica a la inversa: partiendo de la señal medida, se encuentra el subsuelo que la explica.

---

### 🧩 El modelo

El subsuelo real es infinitamente complejo. Lo simplificamos en una cuadrícula de celdas — como **píxeles en una imagen** — a cada una de las cuales se le asigna un único valor (p. ej., resistividad, velocidad sísmica). Este subsuelo pixelado es con el que trabaja realmente el ordenador.

El algoritmo de inversión se pregunta entonces: *¿qué combinación de valores de píxel reproduce mejor las mediciones registradas en la superficie?* Lo hace de forma iterativa:

1. **Iniciar** con una suposición inicial del subsuelo (a menudo un semiespacio uniforme)
2. **Calcular** qué señal produciría esa suposición en la superficie (modelo directo)
3. **Comparar** la señal calculada con las mediciones reales — calcular la discrepancia (el *desajuste*)
4. **Ajustar** el modelo del subsuelo para reducir el desajuste
5. **Repetir** hasta que las señales calculada y medida sean suficientemente próximas

```{figure} ../../assets/images/image1-2_Dimechetal.png
:name: fig-timeline-2_Dimechetal
:width: 75%
:align: center
Dinámica temporal de las propiedades clave del suelo tras un incendio forestal (según Dimech et al.). Las zonas sombreadas indican las tres ventanas de intervención: emergencia (rojo), recuperación temprana (naranja) y recuperación tardía (verde).
```

---

### 🔀 No existe una respuesta única

Aquí está la incómoda verdad: muchos subsuelos diferentes pueden producir **exactamente la misma señal en superficie**. No es un error del software ni una limitación del instrumento — es una **certeza matemática**, conocida como el *problema de la no unicidad*.

:::{warning}
El resultado de una inversión es **un** subsuelo posible — no **el** real.

Piénsalo así: si mides un peso total de 1 kg, la caja podría contener un objeto de 1 kg, diez objetos de 100 g, o mil objetos de 1 g. La medición en superficie por sí sola no puede decirte cuál es el caso.
:::

Para que el resultado sea más fiable, los geofísicos utilizan la **regularización** — una forma matemática de añadir conocimiento previo o preferencias para guiar la solución. Las opciones más comunes son:

- **Restricciones de suavidad**: se prefieren modelos en los que las celdas vecinas sean similares (evita saltos bruscos irrealistas)
- **Ponderación en profundidad**: tiene en cuenta que las celdas más profundas están menos restringidas por los datos de superficie
- **Modelos de referencia**: ancla la inversión a un punto de partida conocido (p. ej., a partir de un sondeo)

---

### ✅ ¿Qué hace bueno un resultado de inversión?

Un resultado se considera fiable cuando:

- El **desajuste de datos es bajo** — el modelo directo del resultado reproduce fielmente la señal medida
- El **resultado es estable** — pequeños cambios en las condiciones iniciales no producen imágenes muy diferentes
- El **resultado es coherente** con información independiente (registros de sondeos, testigos de suelo, geología conocida)
- El **análisis de sensibilidad** confirma que los rasgos de interés están realmente resueltos por los datos, y no son artefactos del algoritmo

```{note}
En estudios post-incendio, este último punto merece especial atención. Los cambios inducidos por el fuego en las propiedades del suelo pueden ser sutiles, localizados y enmascarados por la variabilidad natural. Un rasgo visible en una imagen geofísica solo es significativo si puede demostrarse — mediante pruebas de sensibilidad o muestreo de campo — que los datos eran realmente capaces de resolverlo.
```

---

## Interpretación de la ERT

La interpretación de un modelo de resistividad invertido requiere combinar el conocimiento geofísico con información específica del emplazamiento:

- Los **valores absolutos de resistividad** se comparan con rangos litológicos o edáficos conocidos (p. ej., arcillas saturadas: 1–10 Ω·m; arenas secas: más de 1000 Ω·m)
- Los **patrones espaciales** identifican rasgos estructurales (límites de capas, vías de flujo preferencial, zonas de raíces)
- Los **cambios temporales** (lapso temporal) se convierten en cambios de contenido de agua mediante relaciones petrofísicas, con propagación explícita de la incertidumbre {cite}`tso2019wrr`
- La **integración con datos auxiliares** (testigos de suelo, sondas TDR, sensores de flujo de savia) es esencial para una interpretación inequívoca {cite}`mary2021vzj`

---

```{tip} Resumen
Ahora comprendes:
- La resistividad eléctrica y su significado físico
- Los valores típicos de resistividad para materiales terrestres comunes
- Cómo funciona la medición con 4 electrodos y por qué es necesaria
- El factor geométrico de Wenner $K = 2\pi a$
```

---

```{bibliography}
:style: unsrt
```
