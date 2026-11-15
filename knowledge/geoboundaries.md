---
summary: geoBoundaries / HDX — Ghana region and district boundaries used to assign events
type: source
tags: [data, flood, boundaries]
sources: [Flood options report §5 refs 18, 43]
---
# Ghana boundaries (geoBoundaries and HDX)

**What:** Administrative boundaries for Ghana's 16 regions (ADM1) and districts.
**Links:** geoBoundaries ADM1: https://www.geoboundaries.org/api/current/gbOpen/GHA/ADM1/ · HDX COD-AB: https://data.humdata.org/dataset/cod-ab-gha
**Licence:** geoBoundaries gbOpen GHA ADM1 is **CC BY-SA 2.0**, derived from OpenStreetMap, representing 2021 boundaries, built 12 Dec 2023, with 16 units (checked via the API on 2026-11-15). The share-alike licence means any boundary file we redistribute must keep it, so we don't commit the file. HDX boundaries are CC BY-IGO.
**Region codes:** `shapeISO` holds the ISO 3166-2:GH codes, which match `src/synthetic.py` exactly: GH-AA, AF, AH, BE, BO, CP, EP, NE, NP, OT, SV, TV, UE, UW, WN, WP.
**Status:** geoBoundaries used for the team's Groundsource counts.

Caveat from the report: the 16-region boundaries used were simplified, and events were assigned by polygon centre, so rates would shift somewhat with another method.

## For the capstone
Fix one boundary file in the repo's data note and use it for every source, so all features and labels share the same regions. Consider area-overlap assignment for large polygons.

## Related
- [Groundsource dataset](groundsource-dataset.md)
- [Flood report open questions](flood-report-open-questions.md)
