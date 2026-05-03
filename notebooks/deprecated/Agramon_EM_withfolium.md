---
title: Agramón — EM
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


# 💧 Agramón — Soil Moisture at Catchment Scale

<!--
+++{"no-pdf": true}
```{contents} On this page
:depth: 2
:local:
` ` `
+++
```

::::{only} html
:::{iframe} https://www.youtube.com/embed/IlqWXWprC1g?si=KJfat9-sMGUsI2Fh
:width: 50%
Wenner Measurement (resistive body) - Credit [florianwagner4887](https://www.youtube.com/@florianwagner4887)
:::
:::{iframe} https://www.youtube.com/embed/lt1qV-2d5Ps?si=C1Vz5CDo1zCovlKQ
:width: 50%
Dipole-Dipole Measurement (resistive body) - Credit [florianwagner4887](https://www.youtube.com/@florianwagner4887)
:::
:::{iframe} https://www.youtube.com/embed/h0fnnpU5Pf8?si=DkoYLza1tkrqI6UO
:width: 50%
Schlumberger Measurement (conductive body) - Credit [florianwagner4887](https://www.youtube.com/@florianwagner4887)
:::
::::
-->

---

## 👥 Authors

```{tip} Contributors
**Benjamin Mary** — [benjamin.mary@ica.csic.es](mailto:benjamin.mary@ica.csic.es)
ICA-CSIC, Madrid, Spain

**Hector Nieto**
ICA-CSIC, Madrid, Spain
<!-- TODO: add co-authors -->
```

---

## 📍 Location

**Site:** Agramón, Albacete, Spain
**Coordinates:** 38.43° N, 1.55° W
**Elevation:** ~550 m a.s.l.

```{code-cell} ipython3
:tags: [remove-input, cache]
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

## 🌍 Context




+++{"no-pdf": true}
```{figure} ../../assets/images/agramon_compressed.mp4
:width: 60%
:align: center
:alt: Aerial view of the Agramón catchment
Aerial view of the Agramón catchment showing vegetation cover and topography.
```
+++




The Agramón catchment is located in a semi-arid region of southeastern Spain heavily impacted by recurring drought and wildfire events. Post-fire recovery of forest ecosystems in this area is tightly coupled to soil water availability, which controls vegetation re-establishment and erosion dynamics.

```{note} Why this site?
Agramón offers a representative example of a Mediterranean catchment under combined fire and drought stress. Its relatively small size makes it tractable for multi-scale geophysical monitoring.
```

---

## ❓ Scientific Question

> **How does soil moisture vary spatially and temporally across a fire-affected catchment, and what geophysical proxies best capture this variability?**

Key sub-questions:

- Can electromagnetic induction (EMI) surveys track seasonal moisture dynamics?
- How does burn severity affect the vertical distribution of soil water?
- What is the relationship between apparent electrical conductivity and volumetric water content at this site?

---

## 🛠️ Data Collected

```{list-table} Instruments and survey configuration
:header-rows: 1
:widths: 20 25 25 30

* - Instrument
  - Method
  - Configuration
  - Notes
* - CMD Mini-Explorer 6L
  - Electromagnetic Induction (EMI)
  - 6 coil spacings
  - Vertical dipole mode; 
* - UAV (DJI Phantom 4)
  - Aerial photogrammetry
  - RGB + multispectral + thermal
  - For co-registration and ET mapping
```

```{warning} Data availability
Raw data are stored in the ICA-CSIC data repository. Contact the authors for access.
<!-- TODO: add DOI or data repository link -->
```

---

## 🔬 Analysis & Processing

### Setup & Imports

```{code-cell} ipython3
:tags: [remove-input, cache]
import os
import sys
from pathlib import Path
current_dir = Path().resolve()
assets_path = current_dir.parents[1] / "assets"
sys.path.append(str(assets_path))

print(Path().resolve())
print(assets_path)
print(assets_path.exists())

import Agramon_utils as AgUtils

import numpy as np
import pandas as pd
from emagpy import Problem
from matplotlib import pyplot as plt
import Agramon_utils as AgUtils
from shapely.geometry import Point
import geopandas as gpd
import seaborn as sns
import rioxarray as rxr
import plotly.express as px
import plotly.graph_objects as go

preproDir = assets_path / 'complementary_data'
rawDir    = assets_path / 'complementary_data/raw/EM6L/April2025/'

dtm_dataset = AgUtils.load_dtm_stack(assets_path / 'complementary_data')
```

### Study area

```{code-cell} ipython3
:tags: [remove-input, cache]
gdf_Agramon = gpd.read_file(assets_path / 'complementary_data/shapefiles/microcuencas_13.shp')
gdf_Agramon = gdf_Agramon.rename(columns={'TRATAMIENT': 'PlotID'})

gdf_wgs = gdf_Agramon.to_crs(epsg=4326)
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
    title='Plot Boundaries — Agramón Catchment',
)
fig.update_layout(margin={"r": 0, "t": 40, "l": 0, "b": 0}, height=500)
fig.show()
```


```{code-cell} ipython3
:tags: [remove-input, cache]
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

print(df_all.head())
```

### Data import

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

### ECa profile 2D

Apparent electrical conductivity (ECa) recorded along the survey transect. Use the dropdown to switch between coil spacings (shallow → deep).

```{code-cell} ipython3
:tags: [remove-input, cache]
df_survey['dist_m'] = (
    np.sqrt(df_survey['x'].diff().fillna(0)**2 +
            df_survey['y'].diff().fillna(0)**2)
    .cumsum()
)

fig = go.Figure()
for col in col2plot:
    fig.add_trace(go.Scatter(
        x=df_survey['dist_m'],
        y=df_survey[col],
        mode='lines',
        name=col,
        visible=(col == col2plot[0]),
        hovertemplate='Distance: %{x:.1f} m<br>ECa: %{y:.1f} mS/m<extra></extra>',
    ))

buttons = [
    dict(
        label=col,
        method='update',
        args=[{'visible': [c == col for c in col2plot]},
              {'title': f'ECa Profile — {col}  (Height: {CLH} m, Mode: {MODE})'}]
    )
    for col in col2plot
]
fig.update_layout(
    updatemenus=[dict(type='dropdown', x=0.01, y=1.14,
                      showactive=True, buttons=buttons)],
    title=f'ECa Profile — {col2plot[0]}  (Height: {CLH} m, Mode: {MODE})',
    xaxis_title='Distance along transect (m)',
    yaxis_title='ECa (mS/m)',
    height=420,
)
fig.show()
```

### Spatial distribution of ECa — multi-coil map

Interactive scatter map of all six coil spacings (faceted). Hover for coordinates and ECa value; use the colour scale to identify high-conductivity zones.

```{code-cell} ipython3
:tags: [hide-input]
df_long = df_survey[['x', 'y'] + col2plot].melt(
    id_vars=['x', 'y'],
    value_vars=col2plot,
    var_name='Coil',
    value_name='ECa_mSm'
)

fig = px.scatter(
    df_long,
    x='x', y='y',
    color='ECa_mSm',
    facet_col='Coil',
    facet_col_wrap=3,
    color_continuous_scale='Viridis',
    range_color=[5, 60],
    labels={'ECa_mSm': 'ECa (mS/m)', 'x': 'Easting (m)', 'y': 'Northing (m)'},
    title=f'ECa Spatial Distribution — All Coils  |  Height: {CLH} m, Mode: {MODE}',
    height=600,
    hover_data={'ECa_mSm': ':.1f', 'x': ':.1f', 'y': ':.1f'},
)
fig.update_traces(marker=dict(size=4))
fig.update_layout(coloraxis_colorbar=dict(title='ECa (mS/m)'))
fig.show()
```

### Compute statistics per treatments

```{code-cell} ipython3
:tags: [hide-input, cache]
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

print('Applying DEM-based elevation correction...')
k.surveys[0].df.elevation = df_with_elev['Elevation']
#df_with_elev.to_csv(preproDir / 'ECa_withElevation.csv')
#print(f'Saved → {preproDir}/ECa_withElevation.csv')
```

---

## 📊 Statistical Interpretation

### Conductivity Distribution by Sensor & Treatment

Boxplots comparing ECa across coil spacings (depth proxies) grouped by burn treatment. Hover for quartile values; click legend entries to isolate treatments.

```{code-cell} ipython3
:tags: [hide-input]
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
    labels={'ECa_mSm': 'ECa (mS/m)', 'Sensor': 'Coil (depth proxy)'},
    title='ECa Distribution per Coil and Treatment',
    color_discrete_sequence=px.colors.qualitative.Set2,
    height=480,
)
fig.update_layout(boxmode='group', legend_title='Treatment')
fig.show()
```

### Conductivity vs Elevation & Treatment

Scatter plots with OLS trendlines comparing how ECa varies with terrain elevation across treatments. The **shallowest coil** (HCP0.20, ~0–0.3 m) captures near-surface moisture; the **deepest coil** (HCP1.50, ~0–1.8 m) integrates the full profile.

```{code-cell} ipython3
:tags: [hide-input]
for coil_col, depth_label in [
    (coils[0], f'Shallow (~0–0.3 m)  —  {coils[0]}'),
    (coils[5], f'Deep (~0–1.8 m)  —  {coils[5]}'),
]:
    fig = px.scatter(
        df_with_elev.dropna(subset=[coil_col, 'Elevation', 'Treatment']),
        x='Elevation',
        y=coil_col,
        color='Treatment',
        facet_col='Treatment',
        trendline='ols',
        labels={coil_col: 'ECa (mS/m)', 'Elevation': 'Elevation (m a.s.l.)'},
        title=depth_label,
        color_discrete_sequence=px.colors.qualitative.Set2,
        height=400,
        hover_data={coil_col: ':.1f', 'Elevation': ':.1f'},
    )
    fig.update_traces(marker=dict(size=4, opacity=0.6))
    fig.update_layout(showlegend=False)
    fig.show()
```


---

## 🔄 On-going & Perspective Work

- [ ] Seasonal time-lapse EMI surveys
- [ ] Joint inversion of EMI + ERT for improved depth resolution
- [ ] Coupling with hydrological model (pyCATHY) at catchment scale
- [ ] Integration with remote sensing for spatial upscaling

```{tip} GRWater project
This site is part of the [GRWater project](https://grwater.ica.csic.es/) — multi-scale monitoring of the Earth Critical Zone for post-fire forest management.
```

---

## ✅ Conclusion

Preliminary results indicate that EMI surveys successfully resolve spatial patterns of soil moisture at the catchment scale, with apparent electrical conductivity values strongly correlated with gravimetric measurements. Burn severity significantly alters the depth-moisture profile, with hydrophobic surface layers observed in heavily burned zones.

```{important} Key takeaway
Geophysical methods — particularly EMI — provide a cost-effective tool for catchment-scale soil moisture monitoring in post-fire Mediterranean landscapes.
```

---

```{note} Data Acquisition & Processing Service
[ICA-CSIC](https://www.ica.csic.es) offers a professional service for geophysical
data acquisition and processing as part of its
[Geo-Spatial Technologies for Agro-Forestry Systems](https://www.ica.csic.es/servicios/servicios-cientifico-tecnicos/tecnologias-geo-espaciales-para-el-estudio-de-sistemas-agro-forestales)
scientific-technical services unit.
```
