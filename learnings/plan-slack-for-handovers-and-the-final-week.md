---
summary: Dependent steps slipped and changed hands; plan buffer, early provisional outputs and owners' sign-off
type: lesson
tags: [process, planning, teamwork]
sources: [prosit-2 docs/plan.md tracker, prosit-2 docs/log.md, prosit-2 reflections/README]
---
# Plan slack for handovers and the final week

Prosit 2 had 13 numbered steps with owners, due dates and a "waits on" column. It worked for coordination, but:

- the debrief date passed with steps still unfinished, and the report, slides and reflections step was the one left open;
- several steps changed owner mid-stream when a dependency ran late, so work fell unevenly;
- a step built in full by AI for its owner still needed a walkthrough before that owner could defend it.

What helped: a **provisional model** step early (a plain logistic regression) so later steps could start before the final model existed; the README's "Now" box showing the current step and owner; reviews that doubled as handovers.

What we'd change:
1. Put the report and slides on the critical path from the start, with a draft due a week before the debrief, not after the last analysis step.
2. Leave a buffer of a few days per dependency chain.
3. When a step is taken over, log it and agree how the original owner will still learn and present it.
4. Get sign-off on the plan from everyone in the first days (the Prosit 2 sign-off table stayed unsigned).

## For the capstone
Draw the dependency chain (data → features → baselines → models → threshold → fairness → dashboard → report), put a provisional end-to-end version in week one, and set the report draft date well before the debrief.

## Related
- [defend-every-number-without-ai.md](defend-every-number-without-ai.md)
- [review-by-rerunning-from-a-fresh-clone.md](review-by-rerunning-from-a-fresh-clone.md)
- [pre-submission-check-against-the-rubric.md](pre-submission-check-against-the-rubric.md)
