---
workstream: W03
issue: "#4"
owner: unassigned
status: Not started
needs: none
due: 2026-11-25
---
# W03 · Static and land features per region

## Goal
`data/processed/static.parquet`, which holds the terrain, river, built-up and population features for each region. Features that change over time (built-up land, population) are keyed by `year`, and each year uses only data from earlier years.

## Inputs
All via Earth Engine or a direct download:
- Copernicus DEM (elevation, slope);
- HydroSHEDS (river density);
- JRC Global Surface Water;
- GHSL built-up (5-year steps; interpolate, and never use a step published after the year);
- WorldPop.
- Optional: Dynamic World land cover (2015 onward), for the land-change add-on (W14).

## Outputs
- **`src/static_features.py`**, with columns such as `elev_mean_m`, `slope_mean`, `river_density_km_per_km2`, `surface_water_share`, `builtup_share`, `pop_density`. List them in `data/README.md`.

## Steps
- [ ] Choose the features, then write their source, licence and unit in `data/README.md`.
- [ ] Write the extraction script and region aggregates.
- [ ] Check that each value is plausible: Greater Accra should have the highest built-up share and the north the lowest density.
- [ ] Record the choice for years between GHSL's 5-year steps (interpolate or hold forward) as a decision.

## Read first
[knowledge/ghsl-built-up.md](../knowledge/ghsl-built-up.md) and the other dataset notes in [knowledge/README.md](../knowledge/README.md).
