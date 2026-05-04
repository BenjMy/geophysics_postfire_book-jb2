---
title: "Panorámica de los métodos geofísicos"
authors:
  - name: Benjamin Mary
    email: benjamin.mary@ica.csic.es
    affiliations:
      - ICA-CSIC, Madrid, España
---

# ¿Qué es la geofísica?

**Geo** (Tierra) + **física** = la física de la Tierra. La geofísica aplica principios físicos — mecánica, electromagnetismo, termodinámica — para estudiar el subsuelo **sin ser destructiva**.

```{figure} ../../assets/images/ImageForArticle
:name: ImageForArticle_1202_44837100215127314495
:width: 60%
:align: center
Crédito de imagen: Lukiyanova Natalia / frenta / Shutterstock.com
```

La geofísica se divide clásicamente en dos grandes familias:

- **Geofísica global / de la Tierra profunda** — sismología, geomagnetismo, geodesia. Se ocupa del manto, el núcleo y los procesos a escala de placas. Piénsese en la monitorización de terremotos o en la cartografía del campo magnético terrestre {cite}`telford1990applied`.

- **Geofísica aplicada / ambiental** — la rama que aquí utilizamos. Nacida de la exploración mineral e hidrocarburífera a principios del siglo XX {cite}`reynolds2011introduction`, fue adaptada progresivamente a objetivos más someros: acuíferos, suelos contaminados, yacimientos arqueológicos y, más recientemente, el seguimiento de ecosistemas. Las profundidades de interés van desde centímetros hasta unos pocos centenares de metros.

## Concepto clave

La geofísica aplicada opera detectando **contrastes físicos** entre materiales, midiendo variaciones espaciales en propiedades físicas intrínsecas desde la superficie. Cada roca, capa de suelo o fluido posee propiedades características, entre ellas:

- Resistividad eléctrica
- Permitividad dieléctrica
- Velocidad sísmica
- ...

Estos contrastes sirven a **dos propósitos fundamentalmente distintos pero complementarios**:

### 1. Imagen de la estructura

Algunos rasgos del subsuelo cambian muy lentamente o no cambian en absoluto en escalas de tiempo humanas — la profundidad hasta la roca madre, el espesor de los horizontes del suelo, la geometría de las capas geológicas o la arquitectura de la zona de raíces. La geofísica puede **cartografiar este esqueleto estático** de la Zona Crítica de forma no invasiva, proporcionando un contexto espacial que ningún muestreo puntual puede replicar. Un sondeo o un testigo de suelo te dice qué hay en un lugar; un levantamiento geofísico te dice cómo varía a lo largo del paisaje.

```{admonition} La "Anomalía"
:class: tip
El contraste físico medido en los levantamientos geofísicos se denomina habitualmente **anomalía** — cualquier localización donde una propiedad medida se desvía del valor de fondo esperado. Las anomalías pueden variar en forma, tamaño e intensidad, y pueden ser estructurales (una capa rocosa enterrada) o dinámicas (un frente de humectación tras la lluvia). Distinguir entre ambas es uno de los principales retos interpretativos de la geofísica aplicada.
```

```{figure} ../../assets/images/geological-cross-section-water-anomaly.png
:name: geological-cross-section-water-anomaly
:width: 60%
:align: center
Sección transversal conceptual del subsuelo que muestra un perfil de terreno estratificado con una anomalía localizada en el subsuelo somero. Una zona diferenciada contrasta con las propiedades del material circundante, representando una región saturada de agua (p. ej., una firma del nivel freático) que difiere del suelo de fondo y de la roca madre subyacente en la respuesta física (como la resistividad eléctrica).
```

### 2. Seguimiento de flujos

Otros procesos subsuperficiales son rápidos, transitorios y espacialmente localizados — un frente de infiltración de lluvia que desciende por el suelo, agua que drena preferentemente a través de una grieta, raíces que extraen humedad de una profundidad concreta durante una tarde calurosa. Estos **flujos dejan una huella física** que la geofísica puede detectar, especialmente cuando las mediciones se repiten a lo largo del tiempo. Aquí es donde las estrategias de lapso temporal resultan esenciales: el cambio entre dos levantamientos revela el flujo que lo causó.

Un amplio abanico de métodos geofísicos existe, cada uno respondiendo a una o más propiedades físicas específicas y ofreciendo perspectivas únicas sobre la estructura o la dinámica del subsuelo. La [tabla siguiente](#geophysical-methods-table) resume los principales métodos organizados según la propiedad física que miden. Los contrastes medidos son en última instancia sensibles a las propiedades del suelo que nos interesan:

- Contenido en agua
- Textura
- Materia orgánica
- Estructura del suelo
- ...

## Superando las limitaciones de los sensores puntuales

Los métodos geofísicos nos permiten caracterizar las propiedades del subsuelo **de forma no invasiva**, sobre **grandes áreas**, y en [**pasos de tiempo repetidos**](#timelapseGeophy) — respondiendo exactamente a las limitaciones del muestreo de suelo tradicional.

::::{tip} ¿Por qué no invasivo?
El muestreo de suelo tradicional es destructivo, lento y espacialmente disperso. Un único perfil geofísico puede producir miles de datos del subsuelo en menos de una hora, preservando la estructura del suelo.
::::

## Geofísica para caracterizar la zona crítica

La [**figura siguiente**](#fig-10_1002_wat2.1732_Fig1) ilustra los cuatro temas en los que la geofísica se ha utilizado como herramienta de verificación de hipótesis en la Zona Crítica (ZC) {cite}`dumont2024geophysics`:
- (A) **estructura del subsuelo** y controles sobre las propiedades y procesos hidrológicos;
- (B) **almacenamiento y partición** del agua en la ZC, desglosada en (B1) dimensionalidad de la infiltración y controles sobre la recarga del acuífero, y (B2) controles estacionales y de eventos sobre el intercambio aguas subterráneas–aguas superficiales;
- (V) **absorción de agua por los árboles** y su papel en la variabilidad subsuperficial;
- (D) **reacciones biogeoquímicas** relacionadas con los flujos de agua en la ZC.

```{figure} ../../assets/images/10_1002_wat2.1732_Fig1
:name: fig-10_1002_wat2.1732_Fig1
:width: 100%
:align: center
Ilustración de cuatro temas en los que la geofísica se ha utilizado como herramienta de verificación de hipótesis en estudios hidrogeológicos de la zona crítica (según {cite}`dumont2024geophysics`).
```

## Principales métodos geofísicos

La tabla siguiente resume los principales métodos geofísicos utilizados en estudios de suelo y post-incendio, organizados según la propiedad física que miden.

:::{table} Principales métodos geofísicos
:name: geophysical-methods-table

| Método | Propiedad física | Profundidad típica | Escala | Plataforma |
|---|---|---|---|---|
| ERT | Resistividad eléctrica | 0,5–20 m | Parcela a ladera | Terrestre |
| EMI | Resistividad eléctrica | 0,5–6 m | Campo a cuenca | Terrestre / UAV / Aéreo |
| GPR | Permitividad dieléctrica | 0,1–5 m | Parcela a campo | Terrestre / UAV |
| Refracción sísmica | Velocidad de onda P | 1–30 m | Parcela a ladera | Terrestre |
| MASW | Velocidad de onda S | 1–20 m | Parcela a ladera | Terrestre |
:::

---

### Tomografía de Resistividad Eléctrica (ERT)

```{hint} Analogía
La tomografía hace referencia a la reconstrucción espacial de una propiedad física dentro de un medio a partir de mediciones indirectas. El término también se utiliza ampliamente en medicina — el ejemplo más conocido es el TAC (Tomografía Axial Computarizada).
```

La ERT es el **método de referencia** para la caracterización del subsuelo somero en estudios de suelo. Se insertan cuatro electrodos en el terreno: dos inyectan corriente eléctrica, dos miden la diferencia de potencial resultante. Repitiendo esta medición a lo largo de decenas de combinaciones de electrodos en una línea o cuadrícula, se reconstruye una imagen 2D o 3D de la **resistividad** del subsuelo mediante [inversión](resistivity-introduction#true-space-vs-model-space).

```{figure} ../../assets/images/ERT_dehesas.jpg
:name: fig-ert
:width: 85%
:align: center
Levantamiento ERT en una dehesa mediterránea. Las matrices multielectrodo miden la resistividad aparente a lo largo de transectos para caracterizar la estructura del suelo y la distribución de la humedad.
```

**A qué es sensible la ERT:**
- Contenido de agua en el suelo (muy sensible — los suelos húmedos son conductores, los secos son resistivos)
- Contenido en arcilla y textura

**Características prácticas:**
- Profundidad de investigación: típicamente **0,5–20 m** según el espaciado de electrodos
- Resolución espacial: **centímetros a metros** según la geometría del array
- Tiempo de levantamiento: **½–1 hora** por transecto 2D con un sistema multicanal moderno
- Limitación: requiere buen contacto electrodo–suelo; los suelos secos o pedregosos aumentan la resistencia de contacto

(Más detalles en [concepto de RE](er-concept#how-to-translate-er-to-another-proxy-of-interest) y [fundamentos físicos de ERT](resistivity-introduction))

La ERT se ha aplicado en una amplia gama de contextos científicos e ingenieriles.

#### Ingeniería civil y estudios geotécnicos

La estructura del subsuelo, la detección de cavidades, el seguimiento de presas y la estabilidad de terraplenes son objetivos clásicos de la ERT en ingeniería civil {cite}`dimech2022`.

#### Ecohidrología y ecología forestal

La ERT proporciona información espacialmente distribuida sobre la absorción de agua por las raíces (AWR) y la dinámica agua–suelo que los sensores puntuales no pueden igualar. La ERT en lapso temporal se ha utilizado para caracterizar la dinámica de AWR en viñedos {cite}`mary2020soil,mary2019srep`, árboles frutales {cite}`vanella2018jhydrol` y rodales forestales mixtos {cite}`loiseau2023scitotenv,carriere2022rs`. Los enfoques de aprendizaje automático que combinan ERT con datos de teledetección proximal permiten ahora evaluar el estado hídrico de la vid de forma no invasiva {cite}`mary2023bg`.

```{figure} ../../assets/images/SG_ERT_plant
:name: fig-SG_ERT_plant
:width: 50%
:align: center
La geofísica conquista nuevos territorios: el auge de la «agrogeofísica» (según {cite}`garre2021geophysics`).
```

#### Estudios hidrológicos y relaciones petrofísicas

La ERT se acopla de forma natural con el modelado hidrológico a través de relaciones petrofísicas entre resistividad y humedad del suelo {cite}`tso2019wrr,mary2021vzj`. Los sistemas de monitorización a largo plazo han avanzado en la comprensión de procesos que van desde el drenaje de laderas hasta el intercambio aguas subterráneas–aguas superficiales {cite}`slater2021wires`. La geofísica también puede formularse como una **herramienta de verificación de hipótesis** para restringir modelos hidrogeológicos de la zona crítica {cite}`dumont2024wires`.

#### Entornos post-incendio

El análisis combinado de ERT e isótopos estables del agua reveló que la lluvia se infiltra en la roca meteorizada a mayor profundidad en cuencas afectadas por incendios de lo que se pensaba anteriormente, complicando los modelos simples de escorrentía {cite}`atwood2023natcomm`.

---

### Inducción Electromagnética (EMI)

Más detalles en [EM](electromagnetics-introduction)

Los instrumentos EMI generan un campo electromagnético primario que induce corrientes de Foucault en el subsuelo. El campo secundario producido por esas corrientes se mide en la superficie y se relaciona con la **conductividad eléctrica aparente** del suelo. A diferencia de la ERT, la EMI **no requiere contacto con el suelo** — el instrumento simplemente se transporta o arrastra por la superficie.

```{figure} ../../assets/images/EM_antenna_short.jpg
:name: fig-em-antenna
:width: 75%
:align: center
Antena EMI siendo arrastrada por una zona quemada. El instrumento mide la conductividad eléctrica aparente de forma continua, permitiendo una cartografía espacial rápida a velocidad de marcha.
```

**A qué es sensible la EMI:**
- Conductividad eléctrica aparente (mismos factores que la ERT: agua, arcilla, salinidad)
- Patrones espaciales de variabilidad del suelo a escala de campo y cuenca

**Características prácticas:**
- Profundidad de investigación: **0,5–6 m** según la geometría de la bobina y la frecuencia
- Cobertura espacial: **varias hectáreas por día** a velocidad de marcha
- Sin electrodos — ideal para superficies pedregosas o con costras post-incendio
- Limitación: menor resolución vertical que la ERT; sensible a objetos metálicos e infraestructuras

```{figure} ../../assets/images/SG_EM_plant
:name: fig-SG_EM_plant
:width: 50%
:align: center
La geofísica conquista nuevos territorios: el auge de la «agrogeofísica» (según {cite}`garre2021geophysics`).
```

### Georradar (GPR)

El GPR emite pulsos cortos de energía electromagnética de alta frecuencia hacia el suelo y registra el tiempo que tardan en regresar las reflexiones procedentes de interfaces del subsuelo. El tiempo de llegada y la amplitud de la señal dependen de la **permitividad dieléctrica** del material, que está fuertemente controlada por el contenido de agua.

**A qué es sensible el GPR:**
- Contenido de agua en el suelo (a través de cambios en la permitividad dieléctrica)
- Interfaces nítidas: costra superficial, capas de piedras, techo de la roca madre
- Elementos tubulares y objetos enterrados
- Límites entre horizontes del suelo cuando el contraste es suficiente

**Características prácticas:**
- Profundidad de investigación: **0,1–5 m** (menor en suelos húmedos o ricos en arcilla)
- Muy alta resolución horizontal — centimétrica con antenas de alta frecuencia
- Adquisición de datos rápida — perfilado continuo a velocidad de marcha
- Limitación: fuerte atenuación de la señal en suelos conductores (ricos en arcilla, salinos); penetración limitada post-incendio si los suelos están húmedos

---

### Refracción Sísmica

Los métodos sísmicos no están representados en la figura, pero la implementación de la tomografía sísmica es similar a la de la ERT, sustituyendo los electrodos por geófonos y siendo la fuente un disparo; también se utiliza para cartografiar la heterogeneidad espacial de las propiedades del subsuelo.

Una fuente sísmica (golpe de martillo o pequeño explosivo) genera ondas elásticas que viajan por el terreno y se refractan en los contrastes de velocidad entre capas. Los tiempos de primera llegada registrados en una línea de geófonos se invierten para producir un modelo de **velocidad de onda P**.

**Lo que revela la refracción sísmica:**
- Profundidad hasta la roca madre o una capa compactada dura
- Grado de **meteorización** — la roca meteorizada tiene una velocidad mucho menor que la roca fresca
- Cambios de compactación del suelo a gran escala post-incendio (p. ej., por maquinaria pesada o sellado superficial)

**Características prácticas:**
- Profundidad de investigación: **1–30 m** según la energía de la fuente y el tendido de geófonos
- Adecuada para detectar la interfaz suelo–roca madre
- Limitación: requiere un aumento de velocidad con la profundidad; no puede resolver capas de baja velocidad bajo otras más rápidas

---

### MASW (Análisis Multicanal de Ondas Superficiales)

La MASW analiza las **propiedades dispersivas de las ondas superficiales** (ondas Rayleigh) para obtener un perfil de velocidad de onda de cizalla (Vs). La Vs es sensible a la **rigidez del suelo y la densidad aparente**, que varían con la compactación.

**Características prácticas:**
- Utiliza el mismo tendido de geófonos que la refracción — a menudo se adquieren simultáneamente
- Profundidad de investigación: **1–20 m**
- Especialmente útil para detectar capas compactadas someras

---

## Estrategia multimétodo

Ningún método geofísico responde a todas las preguntas. A menudo combinamos:

- **ERT** para perfiles 2D de alta resolución del contenido de agua y la estructura del suelo a escala de parcela
- **EMI** (terrestre y UAV) para cartografía espacial rápida de los patrones de conductividad en cuencas quemadas y de control
- **GPR** para la detección de interfaces someras y el perfil de contenido de agua
- ...

La [figura siguiente](#loiseau2023geophysical) muestra la combinación de técnicas geofísicas en el contexto de la ecología (algunos métodos no se describen explícitamente aquí; el lector puede consultar {cite}`loiseau2023geophysical` para más detalles):
- A) georradar (GPR), utilizado para detectar raíces gruesas;
- B) potencial espontáneo (SP), utilizado para monitorizar el flujo de agua;
- C) gravimetría, utilizada para monitorizar las reservas de agua;
- D) inducción electromagnética (EMI), utilizada para caracterizar la heterogeneidad espacial de las propiedades del subsuelo;
- E) tomografía de resistividad eléctrica (ERT), utilizada para caracterizar la heterogeneidad espacial de las propiedades del subsuelo y posiblemente monitorizar la dinámica del agua.

Los métodos sísmicos no están representados, pero la implementación de la tomografía sísmica es similar a la de la ERT sustituyendo los electrodos por geófonos (según {cite}`loiseau2023geophysical`).

```{figure} ../../assets/images/1-s2.0-S0048969723041268-ga1_lrg
:name: loiseau2023geophysical
:width: 100%
:align: center
Implementación en campo de las técnicas geofísicas discutidas principalmente en el artículo de revisión {cite}`loiseau2023geophysical`.
```

---

(timelapseGeophy)=
## Estrategia de lapso temporal

La geofísica en lapso temporal es una estrategia de monitorización basada en la repetición de las mismas mediciones geofísicas a lo largo del tiempo para detectar cambios en las propiedades del subsuelo. Comparando conjuntos de datos adquiridos en distintos momentos, pone de relieve la evolución temporal de las anomalías, permitiendo el seguimiento de procesos como el movimiento del agua, la recarga o la dinámica de la humedad del suelo a través de sus cambiantes firmas físicas.

```{figure} ../../assets/images/image1-5_Dimechetal.png
:name: fig-timeline-2
:width: 100%
:align: center
La geofísica aplicada mide un **contraste físico** entre materiales e investiga cómo evoluciona con el **tiempo**. Figura de {cite}`dimech2023review`.
```

### Un enfoque en crecimiento impulsado por la tecnología

Históricamente, la geofísica en lapso temporal ha estado limitada por el coste y la carga logística de desplegar instrumentos de forma repetida en el campo. Esto está cambiando rápidamente: los sensores son cada vez **más pequeños, más baratos y más autónomos**, lo que permite dejar in situ durante meses o años matrices de electrodos permanentes y registradores de datos que se activan de forma remota. Lo que antes requería un equipo de campo y una jornada completa de trabajo puede ahora programarse como una adquisición automatizada nocturna. Como resultado, las estrategias de lapso temporal están pasando de instantáneas ocasionales a una **monitorización del subsuelo casi continua**, generando conjuntos de datos que se asemejan cada vez más a la resolución temporal de los registros meteorológicos o hidrológicos.

```{admonition} ¿Por qué es importante?
:class: tip
Los instrumentos más baratos y la adquisición automatizada hacen que la geofísica en lapso temporal ya no esté restringida a grandes proyectos de investigación. Es cada vez más accesible para consultorías medioambientales, programas de restauración y observatorios ecológicos a largo plazo — ampliando el rango de emplazamientos y preguntas que pueden abordarse.
```

### La vegetación: un objetivo especialmente dinámico

Esta resolución temporal es especialmente importante cuando el sistema estudiado incluye **vegetación viva**. Las plantas no son componentes pasivos de la Zona Crítica — redistribuyen activamente el agua a través de:

- 🌿 **Transpiración**: las raíces extraen agua del suelo diariamente, creando ciclos diurnos de agotamiento de humedad que se propagan hacia abajo en el perfil
- 🍂 **Fenología estacional**: el contraste entre un dosel en pleno follaje en verano y uno en reposo invernal impulsa cambios drásticos en la demanda de evapotranspiración y, por tanto, en los patrones de humedad del suelo
- 🌧️ **Interceptación y redistribución**: la estructura del dosel controla cómo llega la lluvia a la superficie del suelo, produciendo heterogeneidad espacial que evoluciona a medida que la vegetación se recupera tras la perturbación
- 🌱 **Crecimiento radicular**: a medida que la vegetación se restablece tras el incendio, las redes radiculares en expansión acceden progresivamente a reservas de agua más profundas, alterando la profundidad y el patrón de las anomalías de humedad

Estos procesos se desarrollan en **escalas de tiempo que van de horas a años**, y un único levantamiento geofísico — por detallado que sea — capta solo un momento congelado en el tiempo. La adquisición en lapso temporal no es, por tanto, solo un refinamiento técnico, sino una **necesidad conceptual** cuando la dinámica de la vegetación es parte de la pregunta que se está investigando.

```{note}
En el seguimiento de la recuperación post-incendio, esto es especialmente relevante: el retorno de la vegetación es uno de los principales objetivos de la restauración, pero también es uno de los principales motores del cambio subsuperficial. La geofísica en lapso temporal ofrece una forma de seguir ambos simultáneamente — vinculando lo que es visible sobre el suelo con lo que ocurre en el suelo y la zona de raíces por debajo.
```

---

```{tip} Resumen
En esta introducción has aprendido:
- **Qué es la geofísica**: una forma no invasiva de investigar el subsuelo utilizando principios físicos.
- **Cómo funcionan los métodos geofísicos**: detectando **contrastes en propiedades físicas** (p. ej., resistividad, permitividad, velocidad sísmica).
- **Qué representa una anomalía**: una variación espacial en estas propiedades, a menudo vinculada a rasgos clave como el contenido de agua o la estructura del subsuelo.
- **Por qué es poderosa la geofísica**: proporciona información espacialmente continua, superando las limitaciones de las mediciones a escala puntual.
- **Cómo se complementan múltiples métodos**: la combinación de técnicas mejora la interpretación de sistemas subsuperficiales complejos.
- **Qué aporta una estrategia de lapso temporal**: la capacidad de monitorizar **cambios temporales**, revelando procesos dinámicos como el movimiento del agua y la recarga.
```
