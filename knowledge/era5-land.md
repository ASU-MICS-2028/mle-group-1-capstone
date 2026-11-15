---
summary: ERA5-Land — daily reanalysis soil moisture, rain and temperature since 1950 (Copernicus licence)
type: source
tags: [data, flood, soil-moisture]
sources: [Flood options report §5 refs 22, 23, 42; Muñoz-Sabater et al. 2021 doi:10.5194/essd-13-4349-2021; Hersbach et al. 2020 doi:10.1002/qj.3803]
---
# ERA5-Land

**What:** ECMWF land reanalysis — daily soil moisture, rainfall and temperature, 1950 to present, ~9 km grid.
**Links:** Earth Engine "ERA5-Land Daily Aggregated": https://developers.google.com/earth-engine/datasets/catalog/ECMWF_ERA5_LAND_DAILY_AGGR · paper: Muñoz-Sabater J et al. (2021), *ESSD* 13, 4349–4383, doi:10.5194/essd-13-4349-2021 · parent ERA5: Hersbach H et al. (2020), *QJRMS* 146, 1999–2049, doi:10.1002/qj.3803.
**Licence:** Copernicus licence, attribution required.
**Status:** terms read; needs an Earth Engine account.

## For the capstone
Antecedent soil wetness: saturated ground turns moderate rain into floods. Use top-layer volumetric soil water on the day before the prediction date, averaged per region.

## Related
- [CHIRPS](chirps.md)
- [Forecast leakage](forecast-leakage.md)
- [Flood problem formulation](flood-problem-formulation.md)
