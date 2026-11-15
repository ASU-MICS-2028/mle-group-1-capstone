---
summary: Each decision gets a short numbered record of options tested, choice, why, consequences
type: procedure
tags: [process, documentation, decisions]
sources: [prosit-2 ADR 0001, prosit-2 docs/adr/0000-template.md, prosit-2 docs/adr/README.md]
---
# Record decisions as ADRs

Prosit 2 produced 22 architecture decision records (ADRs). Each one is a page with: status, date, owner, step; **context**; **options we tested** (a table with numbers); **decision**; **why**; **consequences**; and "what would change our mind".

What made them useful:
- **Don't reopen a decision without a new ADR.** A changed decision gets a new number that says what it replaces (e.g. a provisional calibration ADR was replaced by the final one; a transfer decision was partly replaced when new evidence arrived). The old ones stay, so the history of our thinking is visible.
- **Status says how strong it is:** "Proposed", "Accepted", "Accepted as a capped, unproven pilot". Honest status kept us from overclaiming.
- **An index** (`docs/adr/README.md`) lists them in one place.
- **They fed the report directly.** The methods and limitations sections were mostly assembled from ADR "why" and "consequences" parts, and the panel answers from the option tables.

Cost: more writing. Benefit: anyone could present any part.

## For the capstone
Start with ADRs for: label definition (what counts as a flood-week), the region boundary mapping, the temporal split, the feature set, the alert threshold, and the fairness measure. Copy the Prosit 2 template.

## Related
- [log-actions-and-ai-use-as-you-go.md](log-actions-and-ai-use-as-you-go.md)
- [test-every-diverging-path-in-a-table.md](test-every-diverging-path-in-a-table.md)
- [review-by-rerunning-from-a-fresh-clone.md](review-by-rerunning-from-a-fresh-clone.md)
