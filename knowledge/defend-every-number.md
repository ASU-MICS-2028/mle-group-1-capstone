---
summary: Every claim in a prosit or capstone must be backed by a number or a simple plot.
type: rule
tags: [course-rules, presentation, evaluation]
sources: [lecture-02 recording, lecture-03 recording]
---
# Defend every number

When launching Prosit 1 the lecturer told groups to be "ready to defend every number". He asked that every claim be backed by a figure or a simple plot, and that the final recommendation rest on data and visuals, not opinion.

He also asked for **uncertainty**, not just point estimates: confidence intervals on the main numbers. And he said he would ask, at the presentation, how the results would differ if a step had been skipped (for example, not fitting a distribution). So you must know *why* each step is there.

What this means in practice:
- For each number on a slide, know where it came from (which data, which split, which code).
- Give a range (confidence interval), not one bare value.
- Be ready for "what if you had not done X?".

## For the capstone
For each reported metric (e.g. recall on 2024–2025), give a bootstrap interval and know which weeks it was computed on. Expect "why not a random split?" and "why should NADMO trust a model trained on news reports?".

## Related
- [Confidence interval](confidence-interval.md)
- [Bootstrap confidence interval](bootstrap-confidence-interval.md)
- [A fitted distribution is a model](fitted-distribution-is-a-model.md)
- [Explain results to non-technical audiences](explain-to-non-technical-audiences.md)
