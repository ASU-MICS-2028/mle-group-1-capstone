---
summary: Swapping models barely changed the answer; one coarse input swapped four of ten
type: result
tags: [sensitivity, data-quality, decision]
sources: [prosit-1 notebook §15D, prosit-1 personal notes §9, prosit-1 reflection]
---
# Data gaps moved decisions more than models

Prosit 1's 168-configuration matrix asked which choices actually change the top-10 priority list.

- Distribution family, imputation method, bootstrap method and shrinkage: little or no change. Empirical-Bayes shrinkage did nothing (rank correlation 1.0) because every district had the same 48 months of data, so all were shrunk equally.
- Raw counts vs rates: shared only 5 of 10 (counts just rank population).
- **Including the regional net-coverage figure swapped 4 of the top 10.** And that figure was coarse (one value per region) and measured five years after the case data.

Five districts stayed in the top 10 in at least 80% of rate-based configurations, which gave a robust core recommendation. The headline for the minister became: better coverage data matters more than a fancier model. The reflection also named the open doubt about using a later, coarser number.

## For the capstone
Run the same kind of sensitivity table: which choice changes which regions get alerts in 2024–2025, the model family or the inputs (rainfall product, soil-moisture source, label definition such as one report vs two)? Report the regions that alert under almost every configuration as the robust core.

## Related
- [test-every-diverging-path-in-a-table.md](test-every-diverging-path-in-a-table.md)
- [rank-on-the-upper-bound-under-uncertainty.md](rank-on-the-upper-bound-under-uncertainty.md)
- [normalise-by-exposure-before-comparing-regions.md](normalise-by-exposure-before-comparing-regions.md)
