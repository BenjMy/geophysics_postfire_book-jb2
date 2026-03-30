#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  5 15:03:34 2025
"""


import os
import numpy as np
import sys
import pandas as pd
try:
    from emagpy import Problem # import the main Problem class from emagpy
except:
    print('Install emagpy if needed')
from matplotlib import pyplot as plt
from pathlib import Path
import rioxarray as rxr
import geopandas as gpd
import numpy as np
from shapely.geometry import Point
from shapely.geometry import Polygon, MultiPolygon
from datetime import datetime, timedelta
import random
import xarray as xr
from scipy.interpolate import griddata
import numpy as np
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from shapely.geometry import LineString
from scipy.stats import binned_statistic_2d
from rasterio.transform import from_bounds
import pandas as pd
import pyvista as pv
from typing import List

try:
    import pygimli as pg
    import pygimli.meshtools as mt
except:
    print('Install pygimli if needed')

#%%
plot_names = [
    # "Plot1PostFirefascine",
    "Plot2PostFirefascine", "Plot3PostFirefascine",
    "Plot4Mulching", "Plot5Mulching", "Plot6Control",
    "Plot7Mulching", "Plot8Mulching", "Plot9Control",
    # "Plot10Control"
]


def get_Agramon_EPGS():
    return 'EPSG:25830'

def load_plot_shapefiles(root_path):
    """
    Reads multiple shapefiles and merges them into a single GeoDataFrame.

    Parameters:
    - plot_names: list of shapefile names (without the `.shp` extension)
    - root_path: Path object or string pointing to the folder containing the shapefiles

    Returns:
    - A merged GeoDataFrame with an added 'PlotID' column
    """
    gdfs = []
    for name in plot_names:
        path = os.path.join(root_path, f"{name}.shp")
        gdf = gpd.read_file(path)
        gdf["PlotID"] = name
        gdfs.append(gdf)

    return gpd.GeoDataFrame(pd.concat(gdfs, ignore_index=True), crs=gdfs[0].crs)


def generate_random_points(gdf, n_points):
    minx, miny, maxx, maxy = gdf.total_bounds
    points = []
    while len(points) < n_points:
        random_point = Point(np.random.uniform(minx, maxx),
                             np.random.uniform(miny, maxy))
        if gdf.contains(random_point).any():
            points.append(random_point)
    return points

def generate_measurement_geodataframe(gdf_Agramon, n_points):
    geometry = generate_random_points(gdf_Agramon, n_points)

    # Simulated data
    now = datetime.now()
    data = {
        "Latitude": [pt.y for pt in geometry],
        "Longitude": [pt.x for pt in geometry],
        "Altitude": np.random.uniform(300, 500, n_points),  # example range in meters
        "Date": [(now + timedelta(days=i)).date() for i in range(n_points)],
        "Time": [(now + timedelta(minutes=15*i)).time().strftime('%H:%M:%S') for i in range(n_points)],
        "DOP": np.random.uniform(0.8, 2.5, n_points),
        "Satelites": np.random.randint(4, 12, n_points),
    }

    # Add conductivity and in-phase values for 6 sensors
    for i in range(1, 7):
        data[f"Cond.{i} [mS/m]"] = np.random.uniform(10, 50, n_points)
        data[f"Inph.{i} [ppt]"] = np.random.uniform(-5, 5, n_points)

    data["Note"] = random.choices(["", "rocky", "wet area", "slope"], k=n_points)

    # Create GeoDataFrame
    gdf = gpd.GeoDataFrame(data, geometry=geometry, crs=gdf_Agramon.crs)
    return gdf

def plot_conductivity_sensors(gdf, coils, axes):
    """
    Plots conductivity values (Cond.1 to Cond.6) on the given axes.

    Parameters:
    - gdf: GeoDataFrame with columns Cond.1 to Cond.6
    - axes: list or array of matplotlib Axes objects (length 6)
    """
    for i in range(0, len(coils)):
        gdf.plot(ax=axes[i], column=f"{coils[i]}",
                 cmap="viridis", legend=True, markersize=1)
        axes[i].set_title(f"{coils[i]} [mS/m]")
        # axes[i-1].axis('off')

# def extract_treatment(plot_id: str) -> str:
#     plot_id_lower = plot_id.lower()
#     if "fascine" in plot_id_lower:
#         return "PostFirefascine"
#     elif "mulching" in plot_id_lower:
#         return "Mulching"
#     elif "control" in plot_id_lower:
#         return "Control"
#     else:
#         return "Unknown"

def extract_treatment(plot_id: str) -> str:
    plot_id_lower = plot_id.lower()
    if "fascines" in plot_id_lower:
        return "fascine"
    elif "mulching" in plot_id_lower:
        return "Mulching"
    elif "control" in plot_id_lower:
        return "Control"
    else:
        return "Unknown"
    
    
def create_gdf_survey(k,crs=None):
    df = k.surveys[0].df.copy()
    coils = k.surveys[0].coils
    geometry = [Point(xy) for xy in zip(df['x'], df['y'])]
    gdf_survey = gpd.GeoDataFrame(df, geometry=geometry, crs=crs)  # WGS84
    return gdf_survey


def assign_treatments(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    gdf = gdf.copy()
    gdf["Treatment"] = gdf["PlotID"].apply(extract_treatment)
    return gdf

def assign_treatments_Lietor(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    gdf = gdf.copy()
    # Save geometry column
    geom = gdf.geometry.copy()

    # Modify columns as you want
    gdf['ZONA'] = gdf['ZONA'].str.upper()
    gdf['TIPO'] = gdf['TIPO'].str.lower()

    # Re-assign geometry column back and explicitly set geometry
    gdf['geometry'] = geom
    gdf = gdf.set_geometry('geometry')
    return gdf


def spatially_join_treatments(gdf_measurements: gpd.GeoDataFrame,
                               gdf_plots: gpd.GeoDataFrame,
                               col2add: List[str] = ["geometry", "PlotID", "Treatment"]) -> gpd.GeoDataFrame:
    joined = gpd.sjoin(
        gdf_measurements,
        gdf_plots[col2add],
        how="left",
        predicate="within"
    )
    return joined

def compute_conductivity_stats(cols,gdf: gpd.GeoDataFrame) -> pd.DataFrame:
    # cond_cols = [f"Cond.{i} [mS/m]" for i in range(1, 7)]
    # cond_cols = [f"Cond.{i} [mS/m]" for i in range(1, 7)]
    stats = gdf.groupby("Treatment")[cols].agg(['mean', 'std', 'min', 'max'])
    stats.columns = ['_'.join(col) for col in stats.columns]  # flatten MultiIndex
    return stats.reset_index()


def load_dtm_stack(root_path):
    """
    Load multiple DTM rasters into an xarray.Dataset.

    Parameters:
    - root_path (Path): root directory where DTM subfolders are located.
    - plot_names (list): list of plot names, used to label each DTM layer.

    Returns:
    - xarray.Dataset: stacked DTM data with plot names as variable keys.
    """
    dtm_layers = {}

    for i, name in enumerate(plot_names, start=1):
        dtm_path = root_path / f"DTMplots/dtmplot{i}" / "w001001.adf"
        dtm = rxr.open_rasterio(dtm_path, masked=True).squeeze()
        dtm.name = name  # give the DataArray a meaningful name
        dtm_layers[name] = dtm

    # Combine all into a dataset
    ds = xr.Dataset(dtm_layers)

    return ds


def extract_dtm_values(ds_dtm, gdf_measurements):
    """
    For each point in gdf_measurements, extract DTM values from ds_dtm
    for the corresponding plot.

    Assumes:
    - gdf_measurements has a column 'PlotID' matching ds_dtm variable names.
    - Both datasets are in the same CRS and units.
    """
    # Ensure CRS match
    assert gdf_measurements.crs == ds_dtm.rio.crs, "CRS mismatch! Reproject first."

    # Prepare a list to store extracted results
    extracted_rows = []

    for idx, row in gdf_measurements.iterrows():
        x, y = row.geometry.x, row.geometry.y
        # Extract DTM value using .sel with method='nearest'
        elev = ds_dtm.sel(x=x, y=y, method='nearest').values

        # Append extracted data with original row info plus elevation
        data = row.to_dict()
        data['Elevation'] = elev
        extracted_rows.append(data)

    # Build DataFrame with all extracted points + elevation
    df = pd.DataFrame(extracted_rows)

    return df

def extract_dtm_values_perplot(ds_dtm, gdf_measurements):
    """
    For each point in gdf_measurements, extract DTM values from ds_dtm
    for the corresponding plot.

    Assumes:
    - gdf_measurements has a column 'PlotID' matching ds_dtm variable names.
    - Both datasets are in the same CRS and units.
    """
    # Ensure CRS match
    assert gdf_measurements.crs == ds_dtm.rio.crs, "CRS mismatch! Reproject first."

    # Prepare a list to store extracted results
    extracted_rows = []

    # Loop over plots (variables in ds_dtm)
    for plot_name in ds_dtm.data_vars:
        # Select points corresponding to this plot
        pts = gdf_measurements[gdf_measurements["PlotID"] == plot_name]

        if pts.empty:
            continue

        # Extract elevation values for each point:
        dtm = ds_dtm[plot_name]

        for idx, row in pts.iterrows():
            x, y = row.geometry.x, row.geometry.y
            # Extract DTM value using .sel with method='nearest'
            elev = dtm.sel(x=x, y=y, method='nearest').values.item()

            # Append extracted data with original row info plus elevation
            data = row.to_dict()
            data['Elevation'] = elev
            extracted_rows.append(data)

    # Build DataFrame with all extracted points + elevation
    df = pd.DataFrame(extracted_rows)

    return df



def imshow_cond_by_elevation_treatment(df, cond_col="Cond.1 [mS/m]",
                                       elevation_col="Elevation",
                                       treatment_col="Treatment",
                                       bins=10,
                                       ax=None):
    # Ensure elevation is numeric
    df[elevation_col] = pd.to_numeric(df[elevation_col], errors='coerce')
    df = df.dropna(subset=[elevation_col, cond_col, treatment_col])

    # Create elevation bins
    df["ElevationBin"] = pd.cut(df[elevation_col], bins=bins)

    # Pivot table: rows = elevation bins, columns = treatments, values = mean conductivity
    pivot = df.pivot_table(index="ElevationBin", columns=treatment_col, values=cond_col, aggfunc='mean')

    # Replace NaN with some value (e.g., 0 or np.nan)
    data = pivot.fillna(np.nan).values

    # Plot with imshow
    cax = ax.imshow(data, aspect='auto', interpolation='nearest', cmap='viridis')

    # Axis labels and ticks
    ax.set_xticks(np.arange(len(pivot.columns)))
    ax.set_xticklabels(pivot.columns, rotation=45, ha='right')

    ax.set_yticks(np.arange(len(pivot.index)))
    ax.set_yticklabels([str(bin) for bin in pivot.index])

    ax.set_xlabel("Treatment")
    ax.set_ylabel(f"{elevation_col} bins")
    ax.set_title(f"Mean {cond_col} by Elevation and Treatment")

    plt.tight_layout()
    return cax


def plot_interpolated_conductivity(gdf, coils,
                                   axes,
                                   method='cubic',
                                   grid_res=20,
                                   vmin=0, vmax=50,
                                   ):
    """
    Interpolates and plots conductivity values (Cond.1 to Cond.6) using imshow.

    Parameters:
    - gdf: GeoDataFrame with columns Cond.1 to Cond.6
    - axes: list or array of matplotlib Axes objects (length 6)
    - method: interpolation method ('linear', 'nearest', 'cubic')
    - grid_res: resolution of the interpolation grid
    """
    x = gdf.geometry.x.values
    y = gdf.geometry.y.values

    # Define grid
    xi = np.linspace(x.min(), x.max(), grid_res)
    yi = np.linspace(y.min(), y.max(), grid_res)
    xi, yi = np.meshgrid(xi, yi)

    for i in range(0, len(coils)):
        col = f"{coils[i]}"
        z = gdf[col].values
        zi = griddata((x, y), z, (xi, yi), method=method)

        im = axes[i].imshow(zi, extent=(x.min(), x.max(), y.min(), y.max()),
                              origin='lower', cmap='viridis', aspect='auto',
                              vmin=vmin,vmax=vmax)
        axes[i].set_title(col)
        plt.colorbar(im, ax=axes[i])



def plot_conductivity_statistics(gdf, coils,
                                 axes,
                                 stat='mean',
                                 grid_res=20,
                                 vmin=0, vmax=50,
                                 save_tif=False,
                                 output_prefix='conductivity_stat'):

    x = gdf.geometry.x.values
    y = gdf.geometry.y.values

    x_edges = np.linspace(x.min(), x.max(), grid_res + 1)
    y_edges = np.linspace(y.min(), y.max(), grid_res + 1)

    x_centers = 0.5 * (x_edges[:-1] + x_edges[1:])
    y_centers = 0.5 * (y_edges[:-1] + y_edges[1:])

    # Prepare for shared colorbar
    shared_norm = (vmin is not None) and (vmax is not None)
    im_list = []

    for i, col in enumerate(coils):
        z = gdf[col].values
        values = np.ones_like(z) if stat == 'count' else z

        grid_stat, _, _, _ = binned_statistic_2d(y, x, values, statistic=stat,
                                                 bins=[y_edges, x_edges])

        im_args = dict(
            extent=(x.min(), x.max(), y.min(), y.max()),
            origin='lower', cmap='viridis', aspect='auto'
        )
        if shared_norm:
            im_args.update(dict(vmin=vmin, vmax=vmax))

        im = axes[i].imshow(grid_stat, **im_args)
        im_list.append(im)
        axes[i].set_title(f"{col} ({stat})")

        if save_tif:
            da = xr.DataArray(grid_stat,
                              coords={'y': y_centers, 'x': x_centers},
                              dims=('y', 'x'),
                              name=col)
            transform = from_bounds(x.min(), y.min(), x.max(), y.max(),
                                    grid_stat.shape[1], grid_stat.shape[0])
            da.rio.write_transform(transform, inplace=True)
            da.rio.write_crs(gdf.crs, inplace=True)
            filename = f"{output_prefix}_{col}_{stat}_{grid_res}.tif"
            da.rio.to_raster(filename)
            print(f"Saved: {filename}")

    # Add a single colorbar if using shared color scale
    # if shared_norm and im_list:
    #     cbar = plt.colorbar(im_list[0], ax=axes, orientation='vertical', fraction=0.015, pad=0.01)
    #     cbar.set_label(f"Conductivity ({stat})")

    if shared_norm and im_list:
        return im_list[0]
    else:
        return None

# def plot_conductivity_statistics(gdf, coils,
#                                  axes,
#                                  stat='mean',
#                                  grid_res=20,
#                                  vmin=0, vmax=50,
#                                  save_tif=False,
#                                  output_prefix='conductivity_stat'):
#     """
#     Aggregates and plots conductivity values per grid cell, and optionally saves them as GeoTIFFs.

#     Parameters:
#     - gdf: GeoDataFrame with geometry and conductivity columns
#     - coils: list of 6 conductivity column names
#     - axes: list/array of matplotlib Axes (length 6)
#     - stat: aggregation method ('mean', 'count', 'min', 'max', 'median')
#     - grid_res: number of grid cells per axis
#     - vmin, vmax: color limits
#     - save_tif: if True, saves each grid_stat as a GeoTIFF
#     - output_prefix: base filename for saved rasters
#     """
#     x = gdf.geometry.x.values
#     y = gdf.geometry.y.values

#     # Define grid edges
#     x_edges = np.linspace(x.min(), x.max(), grid_res + 1)
#     y_edges = np.linspace(y.min(), y.max(), grid_res + 1)

#     # Compute cell centers for coordinate labels
#     x_centers = 0.5 * (x_edges[:-1] + x_edges[1:])
#     y_centers = 0.5 * (y_edges[:-1] + y_edges[1:])

#     for i in range(len(coils)):
#         col = coils[i]
#         z = gdf[col].values

#         # Use 1s for count, otherwise use data
#         values = np.ones_like(z) if stat == 'count' else z

#         grid_stat, _, _, _ = binned_statistic_2d(y, x, values, statistic=stat,
#                                                  bins=[y_edges, x_edges])

#         im = axes[i].imshow(grid_stat, extent=(x.min(), x.max(), y.min(), y.max()),
#                             origin='lower', cmap='viridis', aspect='auto',
#                             vmin=vmin, vmax=vmax)
#         axes[i].set_title(f"{col} ({stat})")
#         plt.colorbar(im, ax=axes[i])

#         # Optionally save as GeoTIFF
#         if save_tif:
#             da = xr.DataArray(grid_stat,
#                               coords={'y': y_centers, 'x': x_centers},
#                               dims=('y', 'x'),
#                               name=col)
#             # Define transform
#             transform = from_bounds(x.min(), y.min(), x.max(), y.max(),
#                                     grid_stat.shape[1], grid_stat.shape[0])
#             da.rio.write_transform(transform, inplace=True)
#             da.rio.write_crs(gdf.crs, inplace=True)

#             filename = f"{output_prefix}_{col}_{stat}_{grid_res}.tif"
#             da.rio.to_raster(filename)
#             print(f"Saved: {filename}")


#%%



# -----------------------------
def find_extreme_coords(da):
    elev = da.values
    x_coords, y_coords = np.meshgrid(da['x'], da['y'])

    max_idx = np.unravel_index(np.nanargmax(elev), elev.shape)
    min_idx = np.unravel_index(np.nanargmin(elev), elev.shape)

    x_max, y_max = x_coords[max_idx], y_coords[max_idx]
    x_min, y_min = x_coords[min_idx], y_coords[min_idx]

    return (x_max, y_max), (x_min, y_min)

# -----------------------------
def create_profile_line(start, end, max_length=71.0):
    line = LineString([start, end])
    if line.length > max_length:
        start_pt = line.interpolate(line.length - max_length)
        end_pt = line.interpolate(line.length)
        return LineString([start_pt, end_pt])
    return line

# -----------------------------
def sample_elevation_along_line(da, line, n_points=72):
    points = [line.interpolate(i / (n_points - 1), normalized=True) for i in range(n_points)]
    xs = [pt.x for pt in points]
    ys = [pt.y for pt in points]

    elevs = da.sel(
        x=xr.DataArray(xs, dims="points"),
        y=xr.DataArray(ys, dims="points"),
        method="nearest"
    ).values

    df = pd.DataFrame({
        "x": xs,
        "y": ys,
        "elevation": elevs
    })
    return df

# -----------------------------
def plot_elevation_profile(profile_df, ax=None):
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 4))

    ax.plot(profile_df["elevation"])
    ax.set_xlabel("Point along line")
    ax.set_ylabel("Elevation (m)")
    ax.set_title("Uphill to Downhill DEM Profile")
    ax.grid(True)
    plt.tight_layout()


# -----------------------------
def plot_profile_on_map(gdf_plot, line, crs, ax=None):
    line_gdf = gpd.GeoSeries([line], crs=crs)

    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 8))
    # gdf_plot.plot(ax=ax, edgecolor="black", facecolor="none", linewidth=1)
    gdf_plot.plot(ax=ax,
                  column="PlotID",
                  legend=True,
                  edgecolor="black",
                  alpha=0.5
                  )
    line_gdf.plot(ax=ax,
                  color="red",
                  linewidth=2,
                  label="DEM Profile Line"
                  )
    ax.set_title("DEM Profile Line on Plot Boundaries")
    # ax.legend()
    plt.grid(True)
    plt.tight_layout()
    # plt.show()

# -----------------------------
def print_profile_stats(profile_df, line):
    print(f"🔼 Max elevation: {np.nanmax(profile_df.elevation):.2f} m")
    print(f"🔽 Min elevation: {np.nanmin(profile_df.elevation):.2f} m")
    print(f"📏 Profile length: {line.length:.2f} meters")

def sample_profile_latlon_elevation(da, line, crs):
    """
    Sample profile every 1 meter along the line and extract lat, lon, elevation.

    Parameters:
        da : xarray.DataArray - DEM data
        line : shapely LineString - profile line in same CRS as da
        crs : CRS object or string - CRS of the DEM (usually from da.rio.crs or gdf.crs)

    Returns:
        pd.DataFrame with columns ['lon', 'lat', 'elevation']
    """
    # Create points every 1 meter
    total_length = line.length
    distances = np.arange(0, total_length + 1, 1.0)
    points = [line.interpolate(d) for d in distances]

    # Extract x, y
    xs = [pt.x for pt in points]
    ys = [pt.y for pt in points]

    # Sample elevation using nearest neighbor
    elevs = da.sel(
        x=xr.DataArray(xs, dims="points"),
        y=xr.DataArray(ys, dims="points"),
        method="nearest"
    ).values

    # Build GeoDataFrame with original CRS
    gdf = gpd.GeoDataFrame({
        "elevation": elevs
    }, geometry=[Point(x, y) for x, y in zip(xs, ys)], crs=crs)

    # Reproject to WGS84
    # gdf_wgs84 = gdf.to_crs(epsg=4326)

    # # Extract lat, lon
    # gdf_wgs84["lon"] = gdf_wgs84.geometry.x
    # gdf_wgs84["lat"] = gdf_wgs84.geometry.y

    # Return DataFrame
    # return gdf_wgs84[["lon", "lat", "elevation"]].reset_index(drop=True)
    return xs, ys, elevs


def create_polygon_from_topo(xs, elevs, thickness, zmax_offset=50, marker=1):
    """
    Create a polygon from topo points (xs, elevs), with thickness downward.

    Parameters
    ----------
    xs : array-like
        X coordinates.
    elevs : array-like
        Elevation values.
    thickness : float or array-like
        Thickness to subtract from top elevations (if array, must match length).
    zmax_offset : float, optional
        Offset below max elevation to define bottom flat elevation (default 50).
    marker : int, optional
        Marker ID for the polygon.

    Returns
    -------
    poly : mt.Polygon
        Pygimli polygon with given thickness.
    """
    topo = np.c_[xs, elevs]
    zmax = np.max(elevs)
    bottom_z = zmax - zmax_offset

    # Adjust top elevations by thickness
    if isinstance(thickness, (int, float)):
        top_coords = [(x, z) for x, z in topo]
    else:
        thickness = np.asarray(thickness)
        if thickness.shape[0] != topo.shape[0]:
            raise ValueError("Thickness array length must match xs/elevs length.")
        top_coords = [(x, z - t) for (x, z), t in zip(topo, thickness)]

    # Bottom edge (right to left), flat at bottom_z
    bottom_coords = [(x, bottom_z) for x, _ in topo[::-1]]

    # Combine and close polygon
    polygon_coords = top_coords + bottom_coords
    # if polygon_coords[0] != polygon_coords[-1]:
    #     polygon_coords.append(polygon_coords[0])

    try:
        poly = mt.createPolygon(polygon_coords, isClosed=True, marker=marker)
        return polygon_coords, poly
    except:
        return polygon_coords



def plot_3d_scene(
    dtm_dataset_cropped,
    dtm_dataset,
    f001_res_mesh=None,
    gdf_Agramon=None,
    ECa_csv_path=None,
    show_mesh=True,
    show_res_mesh=True,
    show_profiles=True,
    show_ECa=True,
    point_size=5,
    cmap="viridis"
):
    plotter = pv.Plotter()

    # Main surface mesh
    if show_mesh:
        mesh = dtm_dataset_cropped.pyvista.mesh(x="x", y="y").warp_by_scalar()
        plotter.add_mesh(mesh, 
                         name="Topography",
                         show_scalar_bar=True,
                         opacity=0.3,
                         )

    # Add result mesh (if available)
    if show_res_mesh and f001_res_mesh is not None:
        plotter.add_mesh(f001_res_mesh, 
                         name="Result Mesh", 
                         # color="white", 
                         opacity=0.6
                         )

    # Add ECa point cloud from CSV
    if show_ECa and ECa_csv_path:
        try:
            ECa_df = pd.read_csv(ECa_csv_path)
            if all(col in ECa_df.columns for col in ['x', 'y', 'elevation']):
                points = ECa_df[['x', 'y', 'elevation']].values
                point_cloud = pv.PolyData(points)

                if 'ECa' in ECa_df.columns:
                    point_cloud['ECa'] = ECa_df['ECa'].values
                    plotter.add_mesh(point_cloud, render_points_as_spheres=True,
                                     point_size=point_size, scalars="ECa", cmap=cmap,
                                     name="ECa Points")
                else:
                    plotter.add_mesh(point_cloud, render_points_as_spheres=True,
                                     point_size=point_size, color="blue", name="ECa Points (No Scalar)")
        except Exception as e:
            print(f"Error reading ECa CSV: {e}")

    # Add profile lines from each DataArray
    if show_profiles and gdf_Agramon is not None:
        for da_name in dtm_dataset.data_vars:
            da = dtm_dataset[da_name]

            try:
                max_pt, min_pt = find_extreme_coords(da)
                profile_line = create_profile_line(max_pt, min_pt, max_length=71.0)

                xs, ys, elevs = sample_profile_latlon_elevation(
                    da=da,
                    line=profile_line,
                    crs=gdf_Agramon.crs
                )

                if len(xs) > 1:
                    line_points = np.column_stack((xs, ys, elevs))
                    polyline = pv.lines_from_points(line_points)
                    plotter.add_mesh(polyline, color="red", line_width=3, label=da_name)
            except Exception as e:
                print(f"Error creating profile for {da_name}: {e}")

    plotter.show_grid()
    plotter.show()



# Function to extract x and y from each polygon
def extract_polygon_coords(gdf):
    records = []

    for idx, row in gdf.iterrows():
        geom = row.geometry

        # Ensure we can iterate over both Polygon and MultiPolygon
        if isinstance(geom, Polygon):
            polygons = [geom]
        elif isinstance(geom, MultiPolygon):
            polygons = list(geom.geoms)
        else:
            continue

        for poly in polygons:
            x_coords, y_coords = poly.exterior.coords.xy
            for x, y in zip(x_coords, y_coords):
                records.append({
                    "PlotID": row["PlotID"],
                    "Id": row["Id"],
                    "x": x,
                    "y": y
                })

    return pd.DataFrame(records)


def extract_profiles_ERT_to_gdf(dtm_dataset, reference_gdf, max_length=71.0):
    """
    Extract profile ERT lines from all data variables in dtm_dataset,
    sample elevation along each profile, and return a GeoDataFrame
    with profile lines and elevation arrays.

    Parameters
    ----------
    dtm_dataset : xarray.Dataset
        Dataset containing DataArrays to extract profiles from.
    reference_gdf : geopandas.GeoDataFrame
        GeoDataFrame used to provide CRS information.
    max_length : float, optional
        Maximum length of profile lines (default 71.0).

    Returns
    -------
    geopandas.GeoDataFrame
        GeoDataFrame with columns:
         - 'profile_name': name of DataArray
         - 'elevations': list/array of elevation values along the profile
         - 'geometry': LineString geometry of the profile line
    """

    profile_gdfs = []

    for da_name in dtm_dataset.data_vars:
        da = dtm_dataset[da_name]
        max_pt, min_pt = find_extreme_coords(da)
        profile_line = create_profile_line(max_pt, min_pt, max_length=max_length)

        xs, ys, elevs = sample_profile_latlon_elevation(
            da=da,
            line=profile_line,
            crs=reference_gdf.crs
        )

        line_geom = LineString(zip(xs, ys))

        gdf_profile = gpd.GeoDataFrame({
            'profile_name': [da_name],
            'elevations': [elevs],
            'geometry': [line_geom]
        }, crs=reference_gdf.crs)

        profile_gdfs.append(gdf_profile)

    all_profiles_gdf = gpd.GeoDataFrame(pd.concat(profile_gdfs, ignore_index=True), crs=reference_gdf.crs)
    return all_profiles_gdf



def build_geodataframe_from_layers(depths, sig, xy, crs):
    """
    Build a GeoDataFrame with repeated (x,y) for each signal layer,
    top and bottom depths for layers, and signal values.

    Parameters
    ----------
    depths : np.ndarray, shape (n_points, n_depths)
        Depths array (top depths per layer except last infinite bottom).
    sig : np.ndarray, shape (n_points, n_sig_layers)
        Signal/model values (should be n_depths + 1 layers).
    xy : np.ndarray, shape (n_points, 2)
        Coordinates (x,y) of each point.
    crs : dict or str
        Coordinate Reference System for GeoDataFrame.

    Returns
    -------
    gdf : geopandas.GeoDataFrame
        GeoDataFrame with columns ['x','y','z_top','z_bottom','value','geometry'].
    """
    n_points, n_depths = depths.shape
    n_sig_layers = sig.shape[1]  # should be n_depths + 1

    # Repeat (x,y) for each sig layer per point
    points_repeated = np.repeat(xy, n_sig_layers, axis=0)

    # Create top and bottom depths for each layer:
    z_top = np.zeros((n_points, n_sig_layers))
    z_bottom = np.zeros((n_points, n_sig_layers))

    # Top depths:
    z_top[:, 0] = 0  # or some starting depth, 0 means surface
    z_top[:, 1:] = depths

    # Bottom depths:
    z_bottom[:, :-1] = depths
    z_bottom[:, -1] = np.inf  # last layer bottom is infinite

    # Flatten arrays for DataFrame
    z_top_flat = z_top.flatten()
    z_bottom_flat = z_bottom.flatten()
    sig_flat = sig.flatten()

    # Build DataFrame
    df = pd.DataFrame({
        'x': points_repeated[:, 0],
        'y': points_repeated[:, 1],
        'z_top': z_top_flat,
        'z_bottom': z_bottom_flat,
        'value': sig_flat
    })

    # Create geometry points from x, y
    df['geometry'] = [Point(xy) for xy in zip(df['x'], df['y'])]

    # Create GeoDataFrame with CRS
    gdf = gpd.GeoDataFrame(df, geometry='geometry', crs=crs)

    return gdf






def load_era5_series(
    root_path: str | Path = Path(".."), 
    start_year: int = 2011, 
    end_year: int = 2025, 
    folder_pattern: str = "ERA5/era5_{year}_100x100km", 
    filename: str = "data_stream-oper_stepType-accum.nc", 
    concat_dim: str = "valid_time",
    drop_expver: bool = True
) -> xr.Dataset | None:
    """
    Load and concatenate ERA5 yearly NetCDF files into a single xarray Dataset.

    Parameters
    ----------
    root_path : str or Path, optional
        Base path containing ERA5 yearly folders. Default is one level up ("..").
    start_year : int, optional
        First year to include. Default is 2011.
    end_year : int, optional
        Last year (exclusive). Default is 2025.
    folder_pattern : str, optional
        Pattern for yearly folders, must include `{year}` placeholder.
    filename : str, optional
        Name of the NetCDF file inside each yearly folder.
    concat_dim : str, optional
        Dimension along which datasets will be concatenated. Default is "valid_time".
    drop_expver : bool, optional
        Whether to drop the 'expver' variable if it exists. Default is True.

    Returns
    -------
    xr.Dataset or None
        Combined dataset, or None if no files were found.
    """
    root_path = Path(root_path).resolve()
    datasets = []

    for year in range(start_year, end_year):
        folder = folder_pattern.format(year=year)
        path = root_path / folder / filename
        
        if path.exists():
            ds_tmp = xr.load_dataset(path)
            datasets.append(ds_tmp)
        else:
            print(f"File not found: {path}")

    if not datasets:
        print("No datasets loaded.")
        return None

    combined = xr.concat(datasets, dim=concat_dim)

    if drop_expver and "expver" in combined.variables:
        combined = combined.drop_vars("expver")

    return combined

def extract_point_timeseries(
    ds: xr.Dataset,
    gdf: gpd.GeoDataFrame,
    vars_to_extract: list[str] = ["pev", "tp"],
    resample_dim: str = "valid_time",
    resample_freq: str = "1D",
    secs_in_hour: int = 3600
) -> dict[str, xr.DataArray]:
    """
    Extract daily time series at the centroid of a plot from a shapefile.

    Parameters
    ----------
    ds : xr.Dataset
        Input xarray dataset with latitude/longitude coordinates.
    gdf : geopandas.GeoDataFrame
        GeoDataFrame containing the plot geometry.
    vars_to_extract : list of str, optional
        Variables to extract. Default is ['pev', 'tp'].
    resample_dim : str, optional
        Dimension to resample along. Default is 'valid_time'.
    resample_freq : str, optional
        Frequency for resampling. Default is '1D'.
    secs_in_hour : int, optional
        Number of seconds per hour for unit conversion. Default is 3600.

    Returns
    -------
    dict[str, xr.DataArray]
        Dictionary with daily resampled time series for each variable.
    """
    # Load shapefile
    # gdf = gpd.read_file(shapefile_path)
    
    # Ensure dataset has CRS and match shapefile
    ds = ds.rio.write_crs("EPSG:4326", inplace=True)
    gdf_proj = gdf.to_crs(ds.rio.crs)
    
    # Centroid
    centroid = gdf_proj.geometry.centroid.iloc[0]
    centroid_lon, centroid_lat = centroid.x, centroid.y
    print(f"Centroid lon, lat: {centroid_lon}, {centroid_lat}")
    
    # Nearest grid point
    lat_vals = ds.latitude.values
    lon_vals = ds.longitude.values
    lat_idx = np.abs(lat_vals - centroid_lat).argmin()
    lon_idx = np.abs(lon_vals - centroid_lon).argmin()
    print(f"Nearest grid point lat, lon: {lat_vals[lat_idx]}, {lon_vals[lon_idx]}")
    
    # Extract and resample variables
    result = {}
    for var in vars_to_extract:
        da_point = ds[var].isel(latitude=lat_idx, longitude=lon_idx).squeeze()
        da_daily = (da_point / secs_in_hour).resample({resample_dim: resample_freq}).mean()
        result[var] = da_daily
    
    return result

# #%%
# gdf = AgUtils.build_geodataframe_from_layers(depths, sig, xy, crs=AgUtils.get_Agramon_EPGS())
# # gdf = build_geodataframe_from_layers(depths, sig, xy, crs=AgUtils.get_Agramon_EPGS())


# import pyvista as pv
# import numpy as np


# # Parameters
# dx = dy = 0.5  # Horizontal cell size
# opacity = 0.7
# max_depth = 10  # Default depth when z_bottom is infinite

# # Extract min/max values for colormap scaling
# vmin = gdf['value'].min()
# vmax = gdf['value'].max()

# # Create PyVista Plotter
# plotter = pv.Plotter()

# # Loop over rows in GeoDataFrame
# for idx, row in gdf.iterrows():
#     x, y = row['x'], row['y']
#     z_top, z_bottom = row['z_top'], row['z_bottom']
#     val = row['value']

#     # Handle infinite bottom depth
#     if np.isinf(z_bottom):
#         z_bottom = z_top + max_depth

#     # Create a cuboid box
#     bounds = (
#         x - dx/2, x + dx/2,
#         y - dy/2, y + dy/2,
#         -z_bottom, -z_top  # Negative Z for downward direction
#     )
#     cube = pv.Box(bounds=bounds)

#     # Apply scalar value to all vertices of the box
#     scalars = np.full(cube.n_points, val)

#     # Add mesh to the plot
#     plotter.add_mesh(
#         cube,
#         scalars=scalars,
#         cmap="viridis",
#         opacity=opacity,
#         clim=[vmin, vmax],
#         show_scalar_bar=False  # Add one later
#     )

# # Add colorbar and axes
# plotter.show_grid()
# plotter.add_scalar_bar(title="Value",)
# plotter.show()
