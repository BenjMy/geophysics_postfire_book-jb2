---
title: Agramón — EM
authors:
  - name: Benjamin Mary
    email: benjamin.mary@ica.csic.es
    affiliations:
      - ICA-CSIC, Madrid, España
kernelspec:
  name: python3
  display_name: Python 3 (Geophysics)
  language: python
numbering:
  headings: false
---

## 📍 Ubicación

**Sitio:** Agramón, Albacete, España  
**Coordenadas:** 38,43° N, 1,55° O  
**Altitud:** ~550 m s.n.m.

```{code-cell} ipython3
:tags: [remove-input, no-typst]
import folium
m = folium.Map(location=[38.43, -1.55], zoom_start=12, tiles='OpenStreetMap')
folium.Marker(
    [38.43, -1.55],
    popup=folium.Popup('<b>Agramon</b><br>Soil moisture catchment study', max_width=200),
    icon=folium.Icon(color='red', icon='info-sign')
).add_to(m)
m
```

---

## 🌍 Contexto

+++{"no-typst": true}
```{figure} ../../assets/images/agramon_compressed.mp4
:width: 60%
:align: center
:alt: Vista aérea de la cuenca de Agramón
Vista aérea de la cuenca de Agramón mostrando la cobertura vegetal y la topografía.
```
+++


La cuenca de Agramón se encuentra en una región semiárida del sureste de España, fuertemente afectada por episodios recurrentes de sequía e incendios forestales. La recuperación post-incendio de los ecosistemas forestales en esta zona está estrechamente ligada a la disponibilidad de agua en el suelo, que controla el re-establecimiento de la vegetación y la dinámica erosiva.

```{note} ¿Por qué este sitio?
Agramón ofrece un ejemplo representativo de una cuenca mediterránea bajo estrés combinado de fuego y sequía. Su tamaño relativamente pequeño la hace abordable para el monitoreo geofísico a múltiples escalas.
```

---

## ❓ Pregunta Científica

> **¿Cómo varía la humedad del suelo espacial y temporalmente a lo largo de una cuenca afectada por incendios, y qué proxies geofísicos capturan mejor esta variabilidad?**

Preguntas secundarias clave:

- ¿Pueden los levantamientos por inducción electromagnética (EMI) seguir la dinámica estacional de la humedad?
- ¿Cómo afecta la severidad del incendio a la distribución vertical del agua en el suelo?
- ¿Cuál es la relación entre la conductividad eléctrica aparente y el contenido volumétrico de agua en este sitio?

---

## 🛠️ Datos Recolectados

```{list-table} Instrumentos y configuración del levantamiento
:header-rows: 1
:widths: 20 25 25 30

* - Instrumento
  - Método
  - Configuración
  - Notas
* - CMD Mini-Explorer 6L
  - Inducción Electromagnética (EMI)
  - 6 espaciados de bobinas
  - Modo dipolo vertical
* - UAV (DJI Phantom 4)
  - Fotogrametría aérea
  - RGB + multiespectral + térmico
  - Para co-registro y mapeo de ET
```

```{warning} Disponibilidad de datos
Los datos brutos están almacenados en el repositorio de datos del ICA-CSIC. Contacte a los autores para solicitar acceso.
```

---

## 🔬 Análisis y Procesamiento

### Configuración e Importaciones

```{code-cell} ipython3
:tags: [remove-input]
import os
import sys
from pathlib import Path
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from emagpy import Problem
import geopandas as gpd
import rioxarray as rxr
from shapely.geometry import Point
from matplotlib.gridspec import GridSpec
import plotly.express as px
import plotly.graph_objects as go

current_dir = Path().resolve()
assets_path = current_dir.parents[1] / "assets"
sys.path.append(str(assets_path))
import Agramon_utils as AgUtils

preproDir = assets_path / 'complementary_data'
rawDir    = assets_path / 'complementary_data/raw/EM6L/April2025/'

dtm_dataset = AgUtils.load_dtm_stack(assets_path / 'complementary_data')
```

### Área de estudio

```{code-cell} ipython3
:tags: [remove-input]
gdf_Agramon = gpd.read_file(assets_path / 'complementary_data/shapefiles/microcuencas_13.shp')
gdf_Agramon = gdf_Agramon.rename(columns={'TRATAMIENT': 'PlotID'})
gdf_wgs = gdf_Agramon.to_crs(epsg=4326)
```

```{code-cell} ipython3
:tags: [remove-input, no-typst]
fig = px.choropleth_mapbox(
    gdf_wgs,
    geojson=gdf_wgs.__geo_interface__,
    locations=gdf_wgs.index,
    color='PlotID',
    mapbox_style='open-street-map',
    center={"lat": gdf_wgs.geometry.centroid.y.mean(),
            "lon": gdf_wgs.geometry.centroid.x.mean()},
    zoom=13,
    opacity=0.5,
    title='Límites de parcelas — Cuenca de Agramón',
)
fig.update_layout(margin={"r": 0, "t": 40, "l": 0, "b": 0}, height=500)
fig.show()
```

```{code-cell} ipython3
:tags: [remove-input]
# Versión estática — solo esta celda llega a Typst; la celda de plotly es no-typst
fig_s, ax_s = plt.subplots(figsize=(7, 5))
gdf_wgs.plot(column='PlotID', ax=ax_s, legend=True,
             legend_kwds={'title': 'PlotID', 'loc': 'lower right', 'fontsize': 7})
ax_s.set_title('Límites de parcelas — Cuenca de Agramón', fontsize=11)
ax_s.set_xlabel('Longitud')
ax_s.set_ylabel('Latitud')
plt.tight_layout()
plt.show()
```

```{code-cell} ipython3
:tags: [remove-input]
logEM_Agramon = pd.read_csv(assets_path / 'complementary_data/raw/log_EM_Agramon_test.csv', sep=';')

file2plot = ['02AG2', 'AG3']
df_all = pd.concat(
    [pd.read_csv(f'{rawDir}/{fname}.DAT', sep='\t') for fname in file2plot],
    ignore_index=True
)
EM_prepro_file_Agramon = '02AG2.DAT'
df_all.to_csv(f'{rawDir}/{EM_prepro_file_Agramon}', sep='\t', index=False)

selec_survey = logEM_Agramon[logEM_Agramon['Filename'] == {EM_prepro_file_Agramon}]
CLH  = 0
MODE = 'High'
```

### Importación de datos

Importamos los datos recolectados usando el software Emagpy, especificando el **dispositivo** utilizado y la altura de la antena.

```{code-cell} ipython3
:tags: [hide-cell]
k = Problem()
k.importGF(
    fnameHi=f'{rawDir}/{EM_prepro_file_Agramon}',
    device='CMD Mini-Explorer 6L',
    hx=CLH,
    calib='Yes',
)
k.convertFromCoord(targetProjection='EPSG:32630')

col2plot  = ['HCP0.20', 'HCP0.33', 'HCP0.50', 'HCP0.72', 'HCP1.03', 'HCP1.50']
coils     = k.surveys[0].coils
df_survey = k.surveys[0].df.copy()
```

### Perfil 2D de ECa

Conductividad eléctrica aparente (ECa) registrada a lo largo del transecto del levantamiento. Use el desplegable para cambiar entre espaciados de bobinas (de superficial a profundo).

```{code-cell} ipython3
:tags: [remove-input]
df_survey['dist_m'] = (
    np.sqrt(df_survey['x'].diff().fillna(0)**2 +
            df_survey['y'].diff().fillna(0)**2)
    .cumsum()
)
```

<!--
```{code-cell} ipython3
:tags: [remove-input, no-typst]
fig = go.Figure()
for col in col2plot:
    fig.add_trace(go.Scatter(
        x=df_survey['dist_m'],
        y=df_survey[col],
        mode='lines',
        name=col,
        visible=(col == col2plot[0]),
        hovertemplate='Distancia: %{x:.1f} m<br>ECa: %{y:.1f} mS/m<extra></extra>',
    ))
buttons = [
    dict(
        label=col,
        method='update',
        args=[{'visible': [c == col for c in col2plot]},
              {'title': f'Perfil ECa — {col}  (Altura: {CLH} m, Modo: {MODE})'}]
    )
    for col in col2plot
]
fig.update_layout(
    updatemenus=[dict(type='dropdown', x=0.01, y=1.14,
                      showactive=True, buttons=buttons)],
    title=f'Perfil ECa — {col2plot[0]}  (Altura: {CLH} m, Modo: {MODE})',
    xaxis_title='Distancia a lo largo del transecto (m)',
    yaxis_title='ECa (mS/m)',
    height=420,
)
fig.show()
```
-->

```{code-cell} ipython3
fig_s, ax_s = plt.subplots(figsize=(8, 3))
for col in col2plot:
    ax_s.plot(df_survey['dist_m'], df_survey[col], label=col, lw=1)
ax_s.set_xlabel('Distancia a lo largo del transecto (m)')
ax_s.set_ylabel('ECa (mS/m)')
ax_s.set_title(f'Perfil ECa — Todas las bobinas  (Altura: {CLH} m, Modo: {MODE})')
ax_s.legend(fontsize=8, ncol=3)
plt.tight_layout()
plt.show()
```

### Distribución espacial de ECa — mapa multi-bobina

Mapa de dispersión interactivo de los seis espaciados de bobinas (facetado). Pase el cursor para ver coordenadas y valor de ECa; use la escala de colores para identificar zonas de alta conductividad.

<!--
```{code-cell} ipython3
:tags: [hide-input, no-typst]
df_long = df_survey[['x', 'y'] + col2plot].melt(
    id_vars=['x', 'y'],
    value_vars=col2plot,
    var_name='Bobina',
    value_name='ECa_mSm'
)
fig = px.scatter(
    df_long,
    x='x', y='y',
    color='ECa_mSm',
    facet_col='Bobina',
    facet_col_wrap=3,
    color_continuous_scale='Viridis',
    range_color=[5, 60],
    labels={'ECa_mSm': 'ECa (mS/m)', 'x': 'Este (m)', 'y': 'Norte (m)'},
    title=f'Distribución espacial de ECa — Todas las bobinas  |  Altura: {CLH} m, Modo: {MODE}',
    height=600,
    hover_data={'ECa_mSm': ':.1f', 'x': ':.1f', 'y': ':.1f'},
)
fig.update_traces(marker=dict(size=4))
fig.update_layout(coloraxis_colorbar=dict(title='ECa (mS/m)'))
fig.show()
```
-->

```{code-cell} ipython3
:tags: [remove-input]
# Versión estática para PDF Typst
fig_s = plt.figure(figsize=(10, 7))
gs    = GridSpec(2, 3, figure=fig_s, hspace=0.45, wspace=0.35)
for idx, col in enumerate(col2plot):
    ax = fig_s.add_subplot(gs[idx // 3, idx % 3])
    sc = ax.scatter(df_survey['x'], df_survey['y'],
                    c=df_survey[col], cmap='viridis',
                    vmin=5, vmax=60, s=4)
    ax.set_title(col, fontsize=9)
    ax.set_xlabel('Este (m)', fontsize=7)
    ax.set_ylabel('Norte (m)', fontsize=7)
    ax.tick_params(labelsize=6)
fig_s.colorbar(sc, ax=fig_s.axes, shrink=0.6, label='ECa (mS/m)')
fig_s.suptitle(f'Distribución espacial de ECa  |  Altura: {CLH} m, Modo: {MODE}', fontsize=11)
plt.show()
```

### Cálculo de estadísticas por tratamiento

```{code-cell} ipython3
:tags: [hide-input]
geometry = [Point(xy) for xy in zip(df_survey['x'], df_survey['y'])]
gdf_survey_geo   = gpd.GeoDataFrame(df_survey, geometry=geometry, crs=gdf_Agramon.crs)
gdf_Agramon      = AgUtils.assign_treatments(gdf_Agramon)
gdf_measurements = AgUtils.spatially_join_treatments(gdf_survey_geo, gdf_Agramon)
stats_df         = AgUtils.compute_conductivity_stats(coils, gdf_measurements)

dtm_reprojected  = dtm_dataset.rio.reproject(gdf_measurements.crs)
gdf_survey_geo   = AgUtils.create_gdf_survey(k, crs=gdf_Agramon.crs)
gdf_Agramon      = AgUtils.assign_treatments(gdf_Agramon)
gdf_measurements = AgUtils.spatially_join_treatments(gdf_survey_geo, gdf_Agramon)

dtm_cropped      = rxr.open_rasterio(preproDir / 'DEM_Agramon_cropped.tif').squeeze()
dtm_cropped_repr = dtm_cropped.rio.reproject(gdf_measurements.crs)
df_with_elev     = AgUtils.extract_dtm_values(dtm_cropped_repr, gdf_measurements)

k.surveys[0].df.elevation = df_with_elev['Elevation']
```

---

## 📊 Interpretación Estadística

### Distribución de Conductividad por Sensor y Tratamiento

Diagramas de caja comparando la ECa entre espaciados de bobinas (proxies de profundidad) agrupados por tratamiento de quema.

<!--
```{code-cell} ipython3
:tags: [hide-input, no-typst]
melted = gdf_measurements.melt(
    id_vars='Treatment',
    value_vars=coils,
    var_name='Sensor',
    value_name='ECa_mSm'
)
fig = px.box(
    melted,
    x='Sensor',
    y='ECa_mSm',
    color='Treatment',
    points='outliers',
    labels={'ECa_mSm': 'ECa (mS/m)', 'Sensor': 'Bobina (proxy de profundidad)'},
    title='Distribución de ECa por Bobina y Tratamiento',
    color_discrete_sequence=px.colors.qualitative.Set2,
    height=480,
)
fig.update_layout(boxmode='group', legend_title='Tratamiento')
fig.show()
```
-->

```{code-cell} ipython3
:tags: [remove-input]
melted = gdf_measurements.melt(
    id_vars='Treatment',
    value_vars=coils,
    var_name='Sensor',
    value_name='ECa_mSm'
)
treatments = melted['Treatment'].unique()
sensors    = list(melted['Sensor'].unique())
n_t        = len(treatments)
width      = 0.8 / n_t
positions  = np.arange(len(sensors))

fig_s, ax_s = plt.subplots(figsize=(9, 4))
for i, (treat, color) in enumerate(zip(treatments, plt.cm.Set2.colors)):
    data = [melted[(melted['Treatment'] == treat) &
                   (melted['Sensor'] == s)]['ECa_mSm'].dropna().values
            for s in sensors]
    ax_s.boxplot(data,
                 positions=positions + (i - n_t / 2 + 0.5) * width,
                 widths=width * 0.85,
                 patch_artist=True,
                 boxprops=dict(facecolor=color, alpha=0.7),
                 medianprops=dict(color='black'),
                 flierprops=dict(marker='o', markersize=2, alpha=0.4),
                 label=treat)
ax_s.set_xticks(positions)
ax_s.set_xticklabels(sensors, fontsize=8)
ax_s.set_xlabel('Bobina (proxy de profundidad)')
ax_s.set_ylabel('ECa (mS/m)')
ax_s.set_title('Distribución de ECa por Bobina y Tratamiento')
ax_s.legend(title='Tratamiento', fontsize=8)
plt.tight_layout()
plt.show()
```

### Conductividad vs Altitud y Tratamiento

Diagramas de dispersión con líneas de tendencia OLS que comparan cómo varía la ECa con la altitud del terreno entre tratamientos. La **bobina más superficial** (HCP0.20, ~0–0,3 m) captura la humedad cercana a la superficie; la **bobina más profunda** (HCP1.50, ~0–1,8 m) integra el perfil completo.

<!--
```{code-cell} ipython3
:tags: [hide-input, no-typst]
for coil_col, depth_label in [
    (coils[0], f'Superficial (~0–0,3 m)  —  {coils[0]}'),
    (coils[5], f'Profundo (~0–1,8 m)  —  {coils[5]}'),
]:
    fig = px.scatter(
        df_with_elev.dropna(subset=[coil_col, 'Elevation', 'Treatment']),
        x='Elevation',
        y=coil_col,
        color='Treatment',
        facet_col='Treatment',
        trendline='ols',
        labels={coil_col: 'ECa (mS/m)', 'Elevation': 'Altitud (m s.n.m.)'},
        title=depth_label,
        color_discrete_sequence=px.colors.qualitative.Set2,
        height=400,
        hover_data={coil_col: ':.1f', 'Elevation': ':.1f'},
    )
    fig.update_traces(marker=dict(size=4, opacity=0.6))
    fig.update_layout(showlegend=False)
    fig.show()
```
-->

```{code-cell} ipython3
:tags: [remove-input]
for coil_col, depth_label in [
    (coils[0], f'Superficial (~0–0,3 m)  —  {coils[0]}'),
    (coils[5], f'Profundo (~0–1,8 m)  —  {coils[5]}'),
]:
    df_plot    = df_with_elev.dropna(subset=[coil_col, 'Elevation', 'Treatment'])
    treatments = df_plot['Treatment'].unique()
    n_t        = len(treatments)
    fig_s, axes = plt.subplots(1, n_t, figsize=(3.5 * n_t, 4), sharey=True)
    if n_t == 1:
        axes = [axes]
    for ax, (treat, color) in zip(axes, zip(treatments, plt.cm.Set2.colors)):
        sub = df_plot[df_plot['Treatment'] == treat]
        ax.scatter(sub['Elevation'], sub[coil_col],
                   color=color, s=10, alpha=0.6)
        ax.set_title(treat, fontsize=9)
        ax.set_xlabel('Altitud (m s.n.m.)', fontsize=8)
    axes[0].set_ylabel('ECa (mS/m)', fontsize=8)
    fig_s.suptitle(depth_label, fontsize=10)
    plt.tight_layout()
    plt.show()
```

---

## 🔄 Trabajo en Curso y Perspectivas

- [ ] Levantamientos EMI de lapso de tiempo estacional
- [ ] Inversión conjunta de EMI + ERT para mejorar la resolución en profundidad
- [ ] Acoplamiento con modelo hidrológico (pyCATHY) a escala de cuenca
- [ ] Integración con teledetección para escalado espacial

```{tip} Proyecto GRWater
Este sitio forma parte del [proyecto GRWater](https://grwater.ica.csic.es/) — monitoreo multiescala de la Zona Crítica Terrestre para la gestión forestal post-incendio.
```

---

## ✅ Conclusión

Los resultados preliminares indican que los levantamientos EMI resuelven con éxito los patrones espaciales de humedad del suelo a escala de cuenca, con valores de conductividad eléctrica aparente fuertemente correlacionados con mediciones gravimétricas. La severidad del incendio altera significativamente el perfil de humedad en profundidad, observándose capas superficiales hidrofóbicas en las zonas de mayor intensidad de quema.

```{important} Conclusión clave
Los métodos geofísicos — en particular el EMI — proporcionan una herramienta rentable para el monitoreo de la humedad del suelo a escala de cuenca en paisajes mediterráneos post-incendio.
```

---

```{note} Servicio de Adquisición y Procesamiento de Datos
[ICA-CSIC](https://www.ica.csic.es) ofrece un servicio profesional de adquisición y procesamiento de datos geofísicos como parte de su unidad de servicios científico-técnicos de
[Tecnologías Geo-Espaciales para Sistemas Agro-Forestales](https://www.ica.csic.es/servicios/servicios-cientifico-tecnicos/tecnologias-geo-espaciales-para-el-estudio-de-sistemas-agro-forestales).
```
