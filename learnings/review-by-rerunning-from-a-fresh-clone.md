---
summary: A step is merged only after a teammate reruns it from a clean checkout and checks numbers
type: procedure
tags: [process, review, reproducibility, git]
sources: [prosit-2 ADR 0011, prosit-2 docs/log.md, prosit-2 ADR 0014, prosit-2 ADR 0015]
---
# Review by rerunning from a fresh clone

Prosit 2's review rule, which caught real bugs:

1. The owner works on their own branch and opens it for review when the step is done.
2. The reviewer clones or checks out fresh, installs from `requirements.txt`, and runs the notebook end to end:
   `.venv/bin/jupyter nbconvert --to notebook --execute --inplace notebooks/<nb>.ipynb`
3. They recompute the headline numbers and compare them with the write-up. One review found 27 of 31 tables identical and 4 differing only in the third decimal (refit noise), with no quoted number changed.
4. They check that no data is committed and no rows are printed.
5. They log the review (date, what was rerun, what matched) and merge.

What reviews found: a stricter split in one step exposed a time leak in an earlier step; an eight-point code review turned up two real defects (a tie-breaking bug that changed a feature for about 6,000 rows on shuffled input, and history dropped for some rows). Each point was *tested* against the data before changing code, and the fixes went into ADRs.

## For the capstone
Use the same rule for the feature pipeline, each model notebook and the Streamlit app. Reviews also double as preparation: the reviewer must be able to explain the step in the debrief.

## Related
- [make-a-fresh-clone-run-without-a-teammate.md](make-a-fresh-clone-run-without-a-teammate.md)
- [time-split-must-respect-when-labels-are-known.md](time-split-must-respect-when-labels-are-known.md)
- [record-decisions-as-adrs.md](record-decisions-as-adrs.md)
