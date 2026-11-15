---
summary: An unreported value is missing, often not at random, and must not be coded as zero
type: lesson
tags: [missing-data, labels, equity]
sources: [prosit-1 notebook §5–6, prosit-1 personal notes §5, prosit-1 grade (B1 7/7, equity 7/7)]
---
# Missing is not zero

Two findings from Prosit 1 that earned full marks on data gaps and equity:

- **Blank months had been filled with zero.** Seven district-months had no case count, and the summary file treated them as zero cases, implying nobody had malaria that month. We imputed each district's own median month instead (using only that district's history), and a sensitivity check showed rates moved 1–5% and the priority list didn't change. Both the fix and the check were reported.
- **Whole regions were invisible.** Routine district data existed for only 5 of 16 regions; 79% of districts had none. That absence wasn't random: it tracked weak health infrastructure, so it was likely *missing not at random*, and the most burdened places could be the least visible.

The general lesson: absence of a record is evidence about the recording process, not about the thing recorded.

## For the capstone
This is the core risk of a news-based label. "No reported flood" in a region-week may mean no flood, or no journalist, no connectivity, or a flood too small to report. Expect under-reporting in rural and northern regions, describe it in the Datasheet, and read low recall or low flood counts in those regions as possibly a label problem, not only a model problem.

## Related
- [rank-on-the-upper-bound-under-uncertainty.md](rank-on-the-upper-bound-under-uncertainty.md)
- [check-the-data-against-the-brief-first.md](check-the-data-against-the-brief-first.md)
- [../knowledge/missing-value-imputation.md](../knowledge/missing-value-imputation.md)
