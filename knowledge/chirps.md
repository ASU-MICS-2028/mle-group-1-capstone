---
summary: CHIRPS — long daily satellite-plus-gauge rainfall record; our main rainfall feature source
type: source
tags: [data, flood, rainfall]
sources: [Flood options report §5 refs 20, 21, 40; Funk et al. 2015 doi:10.1038/sdata.2015.66]
---
# CHIRPS rainfall

**What:** Climate Hazards Group InfraRed Precipitation with Stations — daily rainfall estimates combining satellite infrared and rain gauges, long record (1981 onward).
**Links:** https://www.chc.ucsb.edu/data/chirps · CHIRPS v3: https://chc.ucsb.edu/data/chirps3 · paper: Funk C et al. (2015), *Scientific Data* 2, 150066, doi:10.1038/sdata.2015.66. Also available in Google Earth Engine.
**Licence:** v2 public domain; v3 CC BY 4.0.
**Status:** terms read; not downloaded yet.
**Watch out:** **v2 production ends on 31 Dec 2026**, as confirmed by the Climate Hazards Center (CHC) July 2026 newsletter and the chirps R package docs (checked 2026-11-15); CHC asks users to move to v3, so decide whether to use v3 (check consistency over 2015–2025).

## For the capstone
Features: rainfall over the past 1, 3, 7, 14 and 30 days per region, using only days up to the prediction date. Aggregate grid cells to regions (mean, and possibly max or wettest-cell share).

## Related
- [ERA5-Land](era5-land.md)
- [CHIRPS-GEFS](chirps-gefs.md)
- [Forecast leakage](forecast-leakage.md)
- [Flood problem formulation](flood-problem-formulation.md)
