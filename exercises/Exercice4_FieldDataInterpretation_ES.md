---
title: Ejercicio 4 ➡️ Interpretación de datos de campo
authors:
  - name: Benjamin Mary
    email: benjamin.mary@ica.csic.es
    affiliations:
      - ICA-CSIC, Madrid, España
  - name: Hector Nieto
    email: hector.nieto@ica.csic.es
    affiliations:
      - ICA-CSIC, Madrid, España
  - name: Miguel Herrezuelo
    affiliations:
      - ICA-CSIC, Madrid, España
  - name: Alfonso Torres
    affiliations:
      - Departamento de Ingeniería Civil y Ambiental, Utah State University (EE. UU.)
  - name: Adrián Olalla
    affiliations:
      - ICA-CSIC, Madrid, España
      - COMPLUTIG SL, Alcalá de Henares (ES)
---

# Exploración de legados de gestión del suelo en agronomía mediante EM y TRE

```{caution} Sin relación con incendios forestales
Este ejemplo no está directamente relacionado con la gestión post-incendio del suelo, sino con la agronomía. Sin embargo, los resultados obtenidos también son interesantes para comprender la dinámica de la conductividad eléctrica medida bajo condiciones variables del suelo.
```

---

## Descripción del sitio de campo

### Sitio experimental de La Poveda

- **Ubicación:** Cerca de Madrid, España
- **Descripción:** Campo de cebada (en barbecho durante el sondeo) con cuatro tratamientos distintos (00, 01, 11, 10):
  - fertilización
  - riego
  - ambos
  - ninguno

```{figure} ../assets/images/plotpoveda_hidden.png
:width: 100%
:align: center
:alt: Sitio experimental de La Poveda

*Sitio experimental de La Poveda con cuatro subparcelas.*
```

```{admonition} Objetivo
:class: objective
Identificar el tratamiento correcto a partir de los resultados del sondeo TRE y EM, es decir:

Por ejemplo (esto es incorrecto, solo a efectos didácticos):

- 01: regado/fertilizado
- 11: regado
- ...
```

---

## Métodos

- **Sondeo EM:** CE aparente medida con un mini-explorador 6L (gf-instrument) en modo de alta sensibilidad (HCP - 0,20 es la distancia entre bobinas).
- **Sondeo TRE:** 4 desplazamientos continuos con espaciado entre electrodos de 0,5 m.

---

## Resultados geofísicos

### Septiembre 2025: CE aparente del sondeo EM

```{figure} ../assets/images/empoveda.png
:width: 100%
:align: center
:alt: Sondeo EM del sitio experimental de La Poveda

Sondeo EM del sitio experimental de La Poveda
```

```{figure} ../assets/images/ertpoveda.png
:width: 100%
:align: center
:alt: Sondeo TRE del sitio experimental de La Poveda

Sondeo TRE del sitio experimental de La Poveda
```

- **Hallazgos:** A pesar de la topografía mínima y un nivel freático somero (<1 m), las condiciones post-lluvia no fueron uniformes. Las medidas de EM y TRE mostraron diferencias de CE dependientes del tratamiento cerca de la superficie y a 1 m de profundidad.

---

- **Hallazgos:** Las prácticas de gestión del suelo a largo plazo (p. ej., riego, fertilización) crean diferencias persistentes en la estructura del suelo y la retención de humedad. Incluso después de un evento de lluvia saturante, la humedad del suelo y la conductividad eléctrica (CE) varían entre tratamientos.

## Perspectivas

- **Observaciones geofísicas:** Los resultados destacan la importancia de ejercer cautela al realizar mediciones iniciales en un sistema agronómico, ya que la gestión previa y el historial ambiental pueden influir fuertemente en las propiedades del suelo.
- **Efectos de legado:** Los posibles efectos de legado pueden indicarse por la diferencia entre los valores predichos y los reales.
- **Integración de modelos:** Se necesitan avances adicionales en modelos de superficie terrestre y una integración más estrecha de simulaciones (p. ej., modo de balance hídrico, SaltMod/SahysMod para tendencias de salinización a largo plazo) y observaciones para caracterizar mejor la memoria de humedad.
- **Memoria ecológica:** Extender el concepto a los flujos de carbono y la memoria ecológica (Canarini et al., 2021; Heinrich et al., 2025).

---

## Solución

```{admonition} Solución
:class: dropdown

```{figure} ../assets/images/plotpoveda_solution.png
:width: 100%
:align: center
:alt: Sitio experimental de La Poveda

*Sitio experimental de La Poveda con cuatro subparcelas.*
```

## Agradecimientos

Esta investigación fue financiada por el proyecto TWISTT en el marco del Programa PRIMA, con fondos de la Unión Europea, y por el proyecto de investigación PCI2025-163228, financiado por MICIU/AEI/10.13039/501100011033 y cofinanciado por la Unión Europea. Benjamin Mary se beneficia de la ayuda "RyC2023-045040-I", financiada por MICIU/AEI (ref. 10.13039/501100011033) y el FSE. Los experimentos de campo en La Poveda contaron con el apoyo del proyecto EO4WUE (TED2021-129814B-I00), financiado por MCIN/AEI (DOI:10.13039/501100011033) y el programa NextGenerationEU/PRTR de la Unión Europea. Los experimentos de El Socorro recibieron el apoyo del proyecto DATI (PCI2021-121932), financiado por MCIN/AEI (DOI:10.13039/501100011033) y el programa PRIMA de la UE.

---

## Referencias
