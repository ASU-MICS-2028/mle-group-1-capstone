---
summary: Ghana's 2018 region split and district renames need an explicit crosswalk before joins
type: procedure
tags: [data, geospatial, ghana]
sources: [prosit-1 notebook §1 and §12, prosit-1 notebooks/district_crosswalk.csv, prosit-1 personal notes §6 step 3]
---
# Harmonise boundaries before joining

Prosit 1's case data used 2014–2017 boundaries; the maps used 2021 ones. In December 2018 Ghana went from 10 to 16 regions (Northern split into Northern, Savannah and North East; Brong-Ahafo into Bono, Bono East and Ahafo; Volta into Volta and Oti; Western into Western and Western North), and many districts were renamed or split.

What we did:
1. Listed every name that didn't match between sources: 17 districts, mostly spelling and "Municipal" suffixes.
2. Hand-built a crosswalk CSV mapping each old name to its new one(s), committed to the repo (names only, no data).
3. For 5 districts split in two, dissolved the new polygons back into the old shape in GeoPandas (`.dissolve(by="district")`) so the old data joined one-to-one with no missing shapes.
4. Flagged in the write-up which present-day regions had no historical data at all.

## For the capstone
Training data (2015–2022) straddles the 2018 split, and the label is defined on today's 16 regions. Decide one geography (present-day 16 regions), map any pre-2018 locations by coordinates rather than region names, keep the crosswalk in the repo, and note which regions' early years rest on reassigned records.

## Related
- [check-the-data-against-the-brief-first.md](check-the-data-against-the-brief-first.md)
- [normalise-by-exposure-before-comparing-regions.md](normalise-by-exposure-before-comparing-regions.md)
- [record-decisions-as-adrs.md](record-decisions-as-adrs.md)
