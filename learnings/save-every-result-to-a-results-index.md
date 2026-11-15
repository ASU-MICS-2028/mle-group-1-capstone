---
summary: Every printed result, including failures, goes to a file listed in a results index
type: procedure
tags: [process, reproducibility, reporting]
sources: [prosit-2 AGENTS.md rule 8, prosit-2 learnings/results_index.md, prosit-2 docs/log.md 7 Nov]
---
# Save every result to a results index

A number that exists only in a terminal or a chat doesn't count as saved. In Prosit 2 we added this rule late (7 Nov, three weeks in), after hunting through notebook outputs for numbers to put in the report. From then on:

1. Anything a script prints as a result also goes to `learnings/tables/*.csv` or `learnings/figures/*.png`, named by step (`07_operating_points.csv`).
2. That includes **failed tests and rejected options**: the report needs "we tried X, it was worse by Y".
3. Scores typed in from a website (leaderboard) go in a table too.
4. Each file gets one line in `learnings/results_index.md`, grouped by step, saying what it shows. Mark superseded files ("use this one: ...").
5. Aggregates only, never rows.

By the end about 100 tables and figures were saved, and every number in the report and slides could be traced to one.

## For the capstone
Set up `learnings/tables/`, `learnings/figures/` and the index on day one, not week three. Each notebook ends by writing its tables; the report cites file names.

## Related
- [test-every-diverging-path-in-a-table.md](test-every-diverging-path-in-a-table.md)
- [audit-leaks-by-building-the-cheating-version.md](audit-leaks-by-building-the-cheating-version.md)
- [make-a-fresh-clone-run-without-a-teammate.md](make-a-fresh-clone-run-without-a-teammate.md)
