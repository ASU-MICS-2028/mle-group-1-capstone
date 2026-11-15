---
summary: Submitted code must run start to finish from a fresh clone or a restarted kernel.
type: rule
tags: [course-rules, reproducibility]
sources: [lecture-02 recording]
---
# Code must run top to bottom from a fresh start

In the Prosit 1 pre-submission checklist the lecturer said the work must run **top to bottom from a fresh clone or a fresh kernel**:
- one notebook → all cells run in order with no errors after "restart and run all";
- several scripts → clone the repo, follow the instructions, and it works.

Notebooks or scripts are both allowed, in any language (Python suggested).

Why it matters: a notebook run out of order can show results that the code, as written, can no longer produce. That is a hidden reproducibility bug.

The same checklist also asked for statistics, sources and an AI-use declaration in the write-up.

## For the capstone
Before each submission, clone the repo into an empty folder, set up the environment from the lock file and run the full pipeline end to end. Pin random seeds and data versions. (Our Prosit 1 grade lost marks on reproducibility.)

## Related
- [Leakage audit with before/after numbers](leakage-audit-before-after.md)
- [The ML pipeline](ml-pipeline.md)
