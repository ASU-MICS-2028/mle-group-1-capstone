---
summary: Merging data sources needs matching entities, resolving code/unit conflicts and dropping redundant columns.
type: procedure
tags: [preprocessing, data-quality]
sources: [preprocessing & leakage slides, lecture-04 recording]
---
# Data integration

**Data integration** is combining several sources into one consistent dataset without creating duplicates, conflicts or noise. Three problems to solve:

- **Entity identification** – the same thing has different names in different systems, e.g. `cust_id` vs `customer_number`. Also, two IDs that look alike may mean different things (student number vs applicant number).
- **Schema and value conflicts** – the same fact encoded differently: pay type "H"/"S" in one source and 1/0 in another; height in cm vs m. Convert to one unit and one code first.
- **Redundant attributes** – two columns carrying the same information (date of birth and age). Find them with correlation analysis and keep one. The lecturer's reasoning: a near-duplicate column adds little new information for the model.

Rule of thumb: when two sources describe the same entity, **resolve the conflict before training**.

## For the capstone
We join Groundsource events, CHIRPS rainfall, ERA5-Land soil moisture, terrain and built-up land on (region, week). Watch region names and boundaries (old 10-region vs current 16-region map), week definitions (which day a week starts) and units (mm vs m of water).

## Related
- [Dirty data](dirty-data.md)
- [Garbage in, garbage out](garbage-in-garbage-out.md)
- [Duplicate leakage](duplicate-leakage.md)
