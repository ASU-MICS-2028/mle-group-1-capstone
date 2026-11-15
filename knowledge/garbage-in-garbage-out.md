---
summary: Data quality matters more than the algorithm; most ML project time goes into data work.
type: concept
tags: [preprocessing, data-quality]
sources: [lecture-04 recording, preprocessing & leakage slides]
---
# Garbage in, garbage out

No algorithm can learn something useful from bad data. If the inputs are wrong, incomplete or inconsistent, the outputs will be too.

The lecturer estimated that **about 60–70% of a traditional ML project is working on the data**, and said model choice matters less than data quality. Real data is rarely ready: sensors fail, survey fields are skipped, records get lost.

Good preprocessing pays off in:
- faster training (no redundant rows or columns);
- higher accuracy (better generalisation);
- simpler, more explainable models;
- fewer attributes to collect in future.

The four classic preprocessing tasks: **cleaning → integration → transformation → reduction**. Then the biggest trap of all: leakage.

## For the capstone
Budget most of the time on building a clean region-week table (matching Groundsource events to regions and weeks, aligning CHIRPS/ERA5 grids to region boundaries) before tuning models.

## Related
- [Dirty data](dirty-data.md)
- [Data integration](data-integration.md)
- [Data leakage](data-leakage.md)
