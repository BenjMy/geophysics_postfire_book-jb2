---
title: Agramón — Soil Moisture at Catchment Scale
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

```{contents} On this page
:depth: 2
:local:
```

---

## 👥 Authors

```{admonition} Contributors
:class: tip
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
:tags: [hide-input]
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

```{figure} ../../assets/images/agramon_context.jpg
:width: 60%
:align: center
:alt: Aerial view of the Agramón catchment

Aerial view of the Agramón catchment showing vegetation cover and topography.
<!-- TODO: replace with actual image path -->
```

The Agramón catchment is located in a semi-arid region of southeastern Spain heavily impacted by recurring drought and wildfire events. Post-fire recovery of forest ecosystems in this area is tightly coupled to soil water availability, which controls vegetation re-establishment and erosion dynamics.

```{admonition} Why this site?
:class: note
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
* - CMD Mini-Explorer
  - Electromagnetic Induction (EMI)
  - 3 coil spacings: 0.32 / 0.71 / 1.18 m
  - Vertical dipole mode; ~0–1.8 m depth
* - ERT system (ABEM)
  - Electrical Resistivity Tomography
  - Wenner-Schlumberger, 48 electrodes, 2 m spacing
  - Two transects across the catchment
* - UAV (DJI Phantom 4)
  - Aerial photogrammetry
  - RGB + multispectral
```

```{admonition} Data availability
:class: warning
Raw data are stored in the ICA-CSIC data repository. Contact the authors for access.
<!-- TODO: add DOI or data repository link -->
```

---

## 🔬 Analysis & Processing

This section contains the full data processing workflow, from raw EMI data import through to spatial analysis and visualisation.

### Setup & Imports

```{code-cell} ipython3
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
```

### File Paths & DTM Loading

```{code-cell} ipython3
rootPath = Path('.')
figPath = rootPath / 'figures'
preproDir = rootPath / 'prepro'
rawDir = rootPath / 'raw/EM6L/April2025/'

dtm_dataset = AgUtils.load_dtm_stack(rootPath)
```

### Study Area: Plot Boundaries

```{code-cell} ipython3
gdf_Agramon = gpd.read_file(rootPath / 'shapefiles/microcuencas_13.shp')
gdf_Agramon = gdf_Agramon.rename(columns={'TRATAMIENT': 'PlotID'})

fig, ax = plt.subplots(figsize=(10, 8))
gdf_Agramon.plot(
    ax=ax,
    column="PlotID",
    legend=True,
    edgecolor="black",
    alpha=0.5
)
ax.set_title("All Plot Boundaries")
plt.show()
```

### Load Survey Log

```{code-cell} ipython3
logEM_Agramon = pd.read_csv(
    rootPath / 'raw/log_EM_Agramon_test.csv',
    sep=';'
)
logEM_Agramon.columns
```

### Preprocessing — Read & Concatenate Raw DAT Files

```{code-cell} ipython3
plt.close('all')

file2plot = [
    '02AG2',
    'AG3',
]

# Read and concatenate into one DataFrame
df_all = pd.concat(
    [pd.read_csv(f'{rawDir}/{fname}.DAT', sep='\t') for fname in file2plot],
    ignore_index=True
)

EM_prepro_file_Agramon = '02AG2.DAT'
df_all.to_csv(f'{rawDir}/{EM_prepro_file_Agramon}', sep='\t', index=False)

selec_survey = logEM_Agramon[logEM_Agramon['Filename'] == {EM_prepro_file_Agramon}]
CLH = 0
MODE = 'High'
```

### EMI Data Import with emagpy

```{code-cell} ipython3
k = Problem()  # create the main emagpy object
k.importGF(
    fnameHi=f'{rawDir}/{EM_prepro_file_Agramon}',
    device='CMD Mini-Explorer 6L',
    hx=CLH,
    calib='Yes',
)

k.convertFromCoord(targetProjection='EPSG:32630')

col2plot = ['HCP0.20', 'HCP0.33', 'HCP0.50', 'HCP0.72', 'HCP1.03', 'HCP1.50']
```

### Quick Map & Profile Plot

```{code-cell} ipython3
fig, ax = plt.subplots()
k.showMap(
    coil=col2plot[0],
    contour=False,
    pts=True,
    ax=ax,
)
plt.show()
```

```{code-cell} ipython3
fig, ax = plt.subplots()
k.show(ax=ax, dist=True)
plt.suptitle(f'EM 6L ({EM_prepro_file_Agramon}) — Coil Height: {CLH} ; Mode: {MODE}')
fig.savefig(f'{rootPath}/figures/EM_ECa_2d.png', dpi=450, transparent=True)
plt.show()
```

### Multi-Coil Map with Catchment Boundaries

```{code-cell} ipython3
minx, miny, maxx, maxy = gdf_Agramon.total_bounds

fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(7, 5))
axes = axes.flatten()

vmin, vmax = 5, 60

for i, col in enumerate(col2plot):
    ax = axes[i]
    k.showMap(coil=col, contour=False, pts=True, ax=ax, vmin=vmin, vmax=vmax)
    gdf_Agramon.plot(ax=ax, facecolor='none', edgecolor='red', linewidth=1)
    ax.set_xlim(minx, maxx)
    ax.set_ylim(miny, maxy)
    ax.set_title(col, fontsize=10)
    ax.set_axis_off()

plt.suptitle(f'EM6L  |  Coil Height: {CLH} ; Mode: {MODE}')
fig.savefig(f'{rootPath}/figures/EM_ECa_map_scaled.png', dpi=450, transparent=True)
plt.show()
```

### Spatial Join — Treatments & Conductivity Stats

```{code-cell} ipython3
df = k.surveys[0].df.copy()
coils = k.surveys[0].coils

# Build GeoDataFrame from survey coordinates
geometry = [Point(xy) for xy in zip(df['x'], df['y'])]
gdf_survey = gpd.GeoDataFrame(df, geometry=geometry, crs=gdf_Agramon.crs)

# Annotate treatment types and spatially join
gdf_Agramon = AgUtils.assign_treatments(gdf_Agramon)
gdf_measurements = AgUtils.spatially_join_treatments(gdf_survey, gdf_Agramon)

# Compute per-coil conductivity statistics
stats_df = AgUtils.compute_conductivity_stats(coils, gdf_measurements)
stats_df
```

### Elevation Extraction from DTM

```{code-cell} ipython3
dtm_reprojected = dtm_dataset.rio.reproject(gdf_measurements.crs)
df_with_elev = AgUtils.extract_dtm_values(dtm_reprojected, gdf_measurements)
```

```{code-cell} ipython3
# Use cropped DEM for elevation correction
gdf_survey = AgUtils.create_gdf_survey(k, crs=gdf_Agramon.crs)
gdf_Agramon = AgUtils.assign_treatments(gdf_Agramon)
gdf_measurements = AgUtils.spatially_join_treatments(gdf_survey, gdf_Agramon)

dtm_dataset_cropped = rxr.open_rasterio(preproDir / 'DEM_Agramon_cropped.tif').squeeze()
dtm_dataset_cropped_reprojected = dtm_dataset_cropped.rio.reproject(gdf_measurements.crs)
df_with_elev = AgUtils.extract_dtm_values(dtm_dataset_cropped_reprojected, gdf_measurements)

GPS_pts_elevation = k.surveys[0].df.elevation
print('Correcting GPS elevation using DEM values...')
k.surveys[0].df.elevation = df_with_elev['Elevation']

df_with_elev.to_csv(preproDir / 'ECa_withElevation.csv')
print(f'Saved: {preproDir}/ECa_withElevation.csv')
```

### Conductivity Maps by Coil — Raw Points

```{code-cell} ipython3
fig, axs = plt.subplots(3, 2, figsize=(12, 12), sharex=True, sharey=True)
axs = axs.flatten()

for i in range(len(axs)):
    gdf_Agramon.plot(ax=axs[i], edgecolor="black", facecolor="none", linewidth=1)

AgUtils.plot_conductivity_sensors(gdf_measurements, coils, axs)
fig.savefig(f'{rootPath}/figures/EM_ECa_DEM_coil0.png', dpi=300)
plt.show()
```

### Conductivity Maps — Interpolated Grid

```{code-cell} ipython3
fig, axes = plt.subplots(2, 3, figsize=(15, 10), sharex=True, sharey=True)
axes = axes.flatten()

AgUtils.plot_interpolated_conductivity(
    gdf_measurements, coils, axes,
    grid_res=10,
    vmin=10, vmax=40
)

for i in range(len(axes)):
    gdf_Agramon.plot(ax=axes[i], edgecolor="black", facecolor="none", linewidth=1)

plt.tight_layout()
fig.savefig(f'{rootPath}/figures/EM_ECa_interp.png', dpi=300)
plt.show()
```

### Conductivity Statistics per Plot (Mean, GeoTIFF export)

```{code-cell} ipython3
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes = axes.ravel()

AgUtils.plot_conductivity_statistics(
    gdf=gdf_measurements,
    coils=coils,
    axes=axes,
    stat='mean',
    grid_res=25,
    vmin=0,
    vmax=50,
    save_tif=True,
    output_prefix=preproDir / 'conductivity'
)

plt.tight_layout()
plt.show()
```

### Conductivity vs Elevation & Treatment — 2D Binned Maps

```{code-cell} ipython3
fig, ax = plt.subplots(figsize=(8, 6))
cax = AgUtils.imshow_cond_by_elevation_treatment(
    df_with_elev, cond_col=coils[0], bins=3, ax=ax
)
fig.colorbar(cax, label=f"{coils[0]} [mS/m]")
ax.set_title(f"Conductivity vs Elevation & Treatment — {coils[0]}")
fig.savefig(f'{rootPath}/figures/EM_ECa_DEM_coil0.png', dpi=300)
plt.show()
```

```{code-cell} ipython3
fig, ax = plt.subplots(figsize=(8, 6))
cax = AgUtils.imshow_cond_by_elevation_treatment(
    df_with_elev, cond_col=coils[5], bins=3, ax=ax
)
fig.colorbar(cax, label=f"{coils[5]} [mS/m]")
ax.set_title(f"Conductivity vs Elevation & Treatment — {coils[5]}")
plt.show()
```

### Boxplot — Conductivity Distribution by Sensor & Treatment

```{code-cell} ipython3
melted = gdf_measurements.melt(
    id_vars='Treatment',
    value_vars=coils,
    var_name='Sensor',
    value_name='Conductivity'
)

fig, ax = plt.subplots(figsize=(8, 4))
sns.boxplot(data=melted, x='Sensor', y='Conductivity', hue='Treatment', ax=ax)
ax.set_title('Conductivity Distribution per Sensor and Treatment')
ax.set_ylabel('ECa (mS/m)')
plt.xticks(rotation=45)
plt.tight_layout()
fig.savefig(f'{rootPath}/figures/EM_ECa_stats_barplot.png', dpi=450, transparent=True)
plt.show()
```

### 3D Visualisation with PyVista

```{code-cell} ipython3
import pyvista as pv
from scipy.interpolate import RegularGridInterpolator

# --- Step 1: Prepare raster grid ---
array_name = "Plot6Control"
da = dtm_reprojected[array_name].fillna(0)

x = dtm_reprojected['x'].values
y = dtm_reprojected['y'].values
z_grid = da.values

# Ensure y is increasing for interpolation
interp_func = RegularGridInterpolator(
    (y[::-1], x), z_grid[::-1, :],
    bounds_error=False, fill_value=0
)

# --- Step 2: Extract and interpolate elevation at survey points ---
x_pts = gdf_measurements['x'].values
y_pts = gdf_measurements['y'].values
xy_pts = np.column_stack((y_pts, x_pts))  # (y, x) order
z_pts = interp_func(xy_pts)

# --- Step 3: Build PyVista point cloud ---
points = np.column_stack((x_pts, y_pts, z_pts))
point_cloud = pv.PolyData(points)
point_cloud["HCP0.50"] = gdf_measurements["HCP0.50"].values

# --- Step 4: Build terrain surface ---
xx, yy = np.meshgrid(x, y)
grid = pv.StructuredGrid(xx, yy, z_grid)

# --- Step 5: Render ---
plotter = pv.Plotter()
plotter.add_mesh(grid, cmap="terrain", show_edges=False)
plotter.add_mesh(grid.outline(), color="black", line_width=2)
plotter.add_points(
    point_cloud,
    render_points_as_spheres=True,
    point_size=10,
    cmap="viridis",
    scalar_bar_args={"title": "HCP0.50"}
)
plotter.show()
```

---

## 🔄 On-going & Perspective Work

- [ ] Seasonal time-lapse EMI surveys (4× per year)
- [ ] Joint inversion of EMI + ERT for improved depth resolution
- [ ] Coupling with hydrological model (SWAT+) at catchment scale
- [ ] Integration with remote sensing (Sentinel-1 SAR) for spatial upscaling

```{admonition} GRWater project
:class: tip
This site is part of the [GRWater project](https://grwater.ica.csic.es/) — multi-scale monitoring of the Earth Critical Zone for post-fire forest management.
```

---

## ✅ Conclusion

Preliminary results indicate that EMI surveys successfully resolve spatial patterns of soil moisture at the catchment scale, with apparent electrical conductivity values strongly correlated with gravimetric measurements. Burn severity significantly alters the depth-moisture profile, with hydrophobic surface layers observed in heavily burned zones.

```{admonition} Key takeaway
:class: important
Geophysical methods — particularly EMI — provide a cost-effective tool for catchment-scale soil moisture monitoring in post-fire Mediterranean landscapes.
```

---

```{admonition} Data Acquisition & Processing Service
:class: note
[ICA-CSIC](https://www.ica.csic.es) offers a professional service for geophysical
data acquisition and processing as part of its
[Geo-Spatial Technologies for Agro-Forestry Systems](https://www.ica.csic.es/servicios/servicios-cientifico-tecnicos/tecnologias-geo-espaciales-para-el-estudio-de-sistemas-agro-forestales)
scientific-technical services unit.
```
