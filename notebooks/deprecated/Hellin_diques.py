#!/usr/bin/env python
# coding: utf-8

# # 🪨 Hellín — Sediment Check Dams
# 
# ```{contents} On this page
# :depth: 2
# :local:
# ```
# 
# ---
# 
# ## 👥 Authors
# 
# ```{admonition} Contributors
# :class: tip
# **Benjamin Mary** — [benjamin.mary@ica.csic.es](mailto:benjamin.mary@ica.csic.es)
# ICA-CSIC, Madrid, Spain
# 
# <!-- TODO: add co-authors -->
# ```
# ---

# In[2]:
from resipy import Project
import numpy as np

k = Project(typ='R2')

# ─────────────────────────────────────────
# DAM GEOMETRY PARAMETERS
# ─────────────────────────────────────────
# Surface profile: flat ground → left slope up → dam crest → right slope down → flat ground
# Coordinates (x, z) — z positive upward

dam_height   = 8.0    # m above ground surface
dam_crest_w  = 6.0    # m wide crest
slope_h      = 3.0    # horizontal run per unit vertical rise (3:1 slope)
dam_base_x0  = 10.0   # x where left toe of dam starts
dam_base_x1  = dam_base_x0 + 2 * slope_h * dam_height + dam_crest_w  # right toe

x_min, x_max = 0, dam_base_x1 + 10
depth        = -15.0  # bottom of model

# Key x-coordinates of dam cross-section
x_left_toe   = dam_base_x0
x_left_crest = dam_base_x0 + slope_h * dam_height
x_right_crest= x_left_crest + dam_crest_w
x_right_toe  = x_right_crest + slope_h * dam_height

# ─────────────────────────────────────────
# ELECTRODES along surface profile (follow dam shape)
# ─────────────────────────────────────────
def surface_z(x):
    """Returns surface elevation z at position x (follows dam profile)."""
    if x <= x_left_toe:
        return 0.0
    elif x <= x_left_crest:
        return (x - x_left_toe) / (slope_h)
    elif x <= x_right_crest:
        return float(dam_height)
    elif x <= x_right_toe:
        return dam_height - (x - x_right_crest) / slope_h
    else:
        return 0.0

# Place electrodes every 1 m along x, following topography
x_elec = np.linspace(2, x_max - 2, 60)
elec   = np.array([[x, surface_z(x)] for x in x_elec])
k.setElec(elec)

# ─────────────────────────────────────────
# REGION POLYGONS
# ─────────────────────────────────────────

# 1. Dam embankment body (trapezoidal, compacted fill)
dam_body = np.array([
    [x_left_toe,   0.0],
    [x_left_crest, dam_height],
    [x_right_crest,dam_height],
    [x_right_toe,  0.0],
    [x_left_toe,   0.0],
])

# 2. Saturated zone (upstream half of dam + foundation, water-filled)
sat_top = dam_height * 0.75   # water table at 75% of dam height
x_sat_right = x_left_crest + dam_crest_w * 0.4  # water table reaches partway into crest
sat_zone = np.array([
    [x_left_toe,          0.0],
    [x_left_toe,          -3.0],
    [x_sat_right,         -3.0],
    [x_sat_right,         sat_top],
    [x_left_crest,        dam_height],
    [x_left_crest - 0.1,  dam_height],
    [x_left_toe,          sat_top],
    [x_left_toe,          0.0],
])

# 3. Foundation alluvium (below dam, shallow permeable layer)
foundation = np.array([
    [x_left_toe - 5,  0.0],
    [x_right_toe + 5, 0.0],
    [x_right_toe + 5, -5.0],
    [x_left_toe - 5,  -5.0],
    [x_left_toe - 5,  0.0],
])

# 4. Bedrock (deep layer)
bedrock = np.array([
    [x_min,  -5.0],
    [x_max,  -5.0],
    [x_max,  depth],
    [x_min,  depth],
    [x_min,  -5.0],
])

# ─────────────────────────────────────────
# MESH — pass topography so mesh follows dam surface
# ─────────────────────────────────────────
topo = np.array([[x, surface_z(x)] for x in np.linspace(x_min, x_max, 200)])

k.createMesh(
    cl      = 1.0,     # mesh refinement
    res0    = 300,     # background resistivity
    # topo    = topo,    # <-- surface follows dam shape
)

# ─────────────────────────────────────────
# ASSIGN RESISTIVITIES
# ─────────────────────────────────────────
# Saturated zone first (so it overrides dam body where they overlap)
k.addRegion(bedrock,    res0=2000,  iplot=False)   # Competent bedrock  — very resistive
k.addRegion(foundation, res0=400,   iplot=False)   # Alluvial foundation — moderate
k.addRegion(dam_body,   res0=800,   iplot=False)   # Compacted fill      — resistive
k.addRegion(sat_zone,   res0=30,    iplot=True)    # Saturated/leakage   — conductive

# ─────────────────────────────────────────
# FORWARD MODEL + INVERSION
# ─────────────────────────────────────────
k.forward(noise=0.03, iplot=True)
k.invert()

# ─────────────────────────────────────────
# RESULTS
# ─────────────────────────────────────────
k.showResults(index=0, electrodes=True, hor_cbar=False)  # True model
k.showResults(index=1, electrodes=True)                  # Inverted model


#%%
from resipy import Project
import numpy as np

k = Project(typ='R2')

# ─────────────────────────────────────────
# GEOMETRY — river bank cross-section
# x = 0 (left floodplain) → x = 60 m (right floodplain)
# The minor bed (active channel) is centred at x=30
# Topography: flat floodplain → bank slope → river bed → bank slope → flat
# ─────────────────────────────────────────

total_length   = 60.0    # m total profile

# River channel geometry
river_center   = 30.0    # m — centre of channel
river_width    = 10.0    # m — minor bed width (water surface)
river_depth    = 1.5     # m — water depth at centre
bank_height    = 2.0     # m — bank top above river bed
bank_slope_w   = 4.0     # m — horizontal width of bank slope

# Key x-coordinates
x_left_top     = river_center - river_width/2 - bank_slope_w   # left bank top
x_left_toe     = river_center - river_width/2                  # left bank toe (water edge)
x_right_toe    = river_center + river_width/2                  # right bank toe
x_right_top    = river_center + river_width/2 + bank_slope_w   # right bank top

# z references
z_floodplain   = 0.0                  # floodplain elevation
z_bank_top     = 0.0                  # bank crest = floodplain level
z_river_bed    = -(bank_height)       # river bed below floodplain
z_water_surf   = z_river_bed + river_depth   # water surface (below floodplain)

def topo_z(x):
    """
    Surface elevation profile (what electrodes sit on):
    flat floodplain → slope down left bank → flat river bed → slope up right bank → flat
    """
    if x <= x_left_top:
        return z_bank_top
    elif x <= x_left_toe:
        # Left bank slope
        t = (x - x_left_top) / (x_left_toe - x_left_top)
        return z_bank_top + t * (z_river_bed - z_bank_top)
    elif x <= x_right_toe:
        return z_river_bed          # flat river bed
    elif x <= x_right_top:
        # Right bank slope
        t = (x - x_right_toe) / (x_right_top - x_right_toe)
        return z_river_bed + t * (z_bank_top - z_river_bed)
    else:
        return z_bank_top

# ─────────────────────────────────────────
# ELECTRODES — full cross-section, no gap
# Covers: left floodplain → left bank slope → river bed → right bank slope → right floodplain
# ─────────────────────────────────────────
spacing = 1.0   # m electrode spacing

x_elec = np.arange(2.0, total_length - 1.0, spacing)   # continuous, no gap
z_elec = np.array([topo_z(x) for x in x_elec])          # follows full topo including river bed
elec   = np.column_stack([x_elec, z_elec])

k.setElec(elec)

# ─────────────────────────────────────────
# FULL TOPOGRAPHY for mesh (including river bed)
# ─────────────────────────────────────────
x_topo = np.linspace(0, total_length, 600)
z_topo = np.array([topo_z(x) for x in x_topo])
topo   = np.column_stack([x_topo, z_topo])

# ─────────────────────────────────────────
# REGION POLYGONS
# ─────────────────────────────────────────

def floor_z(x):
    """Valley/channel floor for polygon bases."""
    return topo_z(x)

# 4. Unsaturated bank material (silty/sandy fill above water table)
#    Water table is at river bed level on both banks, slopes up away from river
def water_table_z(x):
    """Water table: at river bed level near channel, rises gently outward."""
    dist = max(0, abs(x - river_center) - river_width/2)
    return z_river_bed + dist * 0.04   # 4% gradient away from channel

# 5. Saturated alluvium (below water table, above bedrock — both banks)
sat_alluvium = np.array([
    [0.0,          water_table_z(0.0)],
    [total_length, water_table_z(total_length)],
    [total_length, z_river_bed - 4.0],
    [0.0,          z_river_bed - 4.0],
    [0.0,          water_table_z(0.0)],
])

# 7. Weathered bedrock
w_bedrock = np.array([
    [0.0,          z_river_bed - 4.0],
    [total_length, z_river_bed - 4.0],
    [total_length, z_river_bed - 9.0],
    [0.0,          z_river_bed - 9.0],
    [0.0,          z_river_bed - 4.0],
])

# 8. Competent bedrock
bedrock = np.array([
    [0.0,          z_river_bed - 9.0],
    [total_length, z_river_bed - 9.0],
    [total_length, -20.0],
    [0.0,          -20.0],
    [0.0,          z_river_bed - 9.0],
])

# ─────────────────────────────────────────
# MESH
# ─────────────────────────────────────────
k.createMesh(
    cl   = 0.5,
    res0 = 300,
)

# ─────────────────────────────────────────
# ASSIGN RESISTIVITIES (ohm.m)
# ─────────────────────────────────────────
k.addRegion(bedrock,          res0=2500, iplot=False)  # Competent bedrock
k.addRegion(w_bedrock,        res0=600,  iplot=False)  # Weathered bedrock
# k.addRegion(sat_alluvium,     res0=80,   iplot=False)  # Saturated alluvium

# ─────────────────────────────────────────
# PLOT INITIAL MODEL (no inversion needed)
# ─────────────────────────────────────────
# k.showMesh()   # <-- inspect geometry + resistivity zones first
k.mesh.show(attr='res0')  # plot the resistivity attribute on the mesh
# ─────────────────────────────────────────
# FORWARD MODEL + INVERSION
# ─────────────────────────────────────────
k.createSequence([('dpdp', 1, 8, 1, 8), ('wenner', 1, 4), ('ws', 1, 8, 1, 8)]) # dipole-dipole sequence
k.forward(noise=0.03, iplot=True)
k.invert()

k.showResults(index=0, electrodes=True, hor_cbar=False)  # True model
k.showResults(index=1, electrodes=True)                  # Inverted model
