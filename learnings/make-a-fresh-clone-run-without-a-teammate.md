---
summary: Reproducibility lost two marks because a clone needed data handed over by a teammate
type: lesson
tags: [reproducibility, grading, repo]
sources: [prosit-1 grade (reproducibility, −2), prosit-1 README]
---
# Make a fresh clone run without a teammate

Prosit 1 lost the most marks (2 of 8) on reproducibility. The notebook ran top to bottom with fixed seeds and pinned requirements, but the README said to get the `data/` folder "from a teammate". A grader cloning the repo couldn't run it. The data was licensed, so committing it wasn't an option, but we gave no route that worked without us.

What a grader needs:
- one command sequence from clone to results, tested on a clean machine;
- a script that downloads every public input from its source (with a checksum or row-count check), or exact registration and download steps for licensed data;
- a small synthetic or aggregate sample that lets the code run end to end if the real data can't be shared;
- pinned versions and fixed seeds;
- the runtime stated (Prosit 1: about six minutes).

Prosit 2 improved this with download notes in `docs/01_data.md` and a fresh-clone rerun as part of every review.

## For the capstone
Groundsource, CHIRPS/ERA5 rainfall, soil moisture and terrain are public. Write `make data` (or one script) that fetches and builds the region-week table from the sources, documents any Earth Engine authentication step, and caches nothing the grader can't regenerate.

## Related
- [review-by-rerunning-from-a-fresh-clone.md](review-by-rerunning-from-a-fresh-clone.md)
- [pre-submission-check-against-the-rubric.md](pre-submission-check-against-the-rubric.md)
- [../knowledge/runs-top-to-bottom-from-fresh-clone.md](../knowledge/runs-top-to-bottom-from-fresh-clone.md)
