---
summary: Resampling rows when rows are correlated gives intervals far too narrow
type: result
tags: [uncertainty, bootstrap, clustering]
sources: [prosit-1 notebook §4 and §15B, prosit-1 panel_qa, prosit-1 outputs/tables/matrix_B_uncertainty.csv]
---
# Bootstrap by the correlated unit

In Prosit 1, households in the same survey village share mosquitoes, clinics and nets, so they aren't independent. Resampling households pretended they were:

- Northern Region net ownership: naive 95% CI width 0.055 vs **0.120** when resampling whole clusters (2.2× wider).
- Design effect about 5: roughly 1,100 surveyed homes carried the information of about 230 independent ones.
- For malaria prevalence, a simple bootstrap was 1.5–1.7× narrower than the official published interval in every northern region.
- The interval *width* stabilised by B = 2,000 resamples (spread of widths across repeats fell from 0.005 at B = 100 to 0.001).

Using survey weights also mattered for the point estimate: weighted regional ownership matched official figures, unweighted was off by several points.

The rule we carried into Prosit 2: resample the unit that is correlated (customers there, clusters here), never the row.

## For the capstone
Region-weeks are correlated in time (a wet season spans weeks) and in space (neighbouring regions flood together). Resample blocks of consecutive weeks, or whole weeks across all 16 regions, not individual region-weeks. Expect wider intervals than a naive bootstrap and say so.

## Related
- [measure-the-noise-floor-before-claiming-a-win.md](measure-the-noise-floor-before-claiming-a-win.md)
- [report-the-named-subgroup-separately.md](report-the-named-subgroup-separately.md)
- [../knowledge/bootstrap-confidence-interval.md](../knowledge/bootstrap-confidence-interval.md)
