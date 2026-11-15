---
summary: Fallbacks — Greater Accra only, F3 static susceptibility map, or the galamsey spread topic
type: concept
tags: [flood, planning, fallback, galamsey]
sources: [Flood options report §4 F3–F6, §6; proposal Options A and B]
---
# Fallback plans

**Within floods**
- **Greater Accra only.** Richest labels (21.6% of weeks positive) at the cost of fewer people covered.
- **F3 — Greater Accra susceptibility map (Plan B, safest).** Decision: which neighbourhoods an assembly should prioritise for drain clearing and enforcement before the rains. Binary classification on a grid ("has this cell had a reported flood?") with terrain, drainage, buildings (Open Buildings V3, CC BY 4.0, https://developers.google.com/earth-engine/datasets/catalog/GOOGLE_Research_open-buildings_v3_polygons), land cover (ESA WorldCover v200, CC BY 4.0, https://developers.google.com/earth-engine/datasets/catalog/ESA_WorldCover_v200) and population. Validation: spatial block CV (Roberts et al. 2017) with an earlier train and later test period. Risks: lower novelty (similar Ghana maps exist), event locations may be too coarse, non-flooded cells uncertain, eviction-map ethics.
- Rejected or add-on options: F4 roads/facilities cut off (mostly an overlay — dashboard feature only); F5 Lower Volta dam spillage (too few events, no open release data); F6 Sentinel-1 radar segmentation (off-theme, needs GPU, no advance warning).

**Different topic: galamsey spread (Option A).** Decision: where district teams or NAIMOS should survey next. Label: patches free of mining in 2016 that show mining by 2022 (SmallMinesDS, https://huggingface.co/datasets/ellaampy/SmallMinesDS, CC BY-SA 4.0, 4,270 patches, ~3.3 GB; 450 of 1,156 unmined patches, 39%, became mined). Spatial block CV by district; PR-AUC, recall in top 10% of risk. Weakness: a single change window shows where, not when.

## For the capstone
Any switch needs instructor agreement; tell the instructor immediately if data fall through.

## Related
- [Capstone scope rules](capstone-scope-rules.md)
- [Flood project risks](flood-project-risks.md)
- [Flood ethics concerns](flood-ethics-concerns.md)
