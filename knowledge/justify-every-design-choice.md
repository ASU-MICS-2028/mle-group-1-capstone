---
summary: Assessments ask why each step was done; know the reason behind every design choice, not just the result.
type: rule
tags: [course-rules, assessment, lecturer-emphasis]
sources: [lecture-08 recording, lecture-06 recording]
---
# Justify every design choice

At the end of lecture 8 the lecturer described the next assessment (on supervised learning): a similar format to the first, probably with more questions, and students would be asked to **explain concepts and design choices** — "why do we do this, why do we do that" — not only compute. (The recording here is partly garbled, but this part is clear.) The second prosit, also on supervised learning, was to follow.

In lecture 6 the lecturer also said students would test the different classification losses themselves in the next prosit, so expect to be asked why you used the loss you did.

Typical "why" questions this course points to:
- why this loss (log loss over linear or exponential)?
- why this split (time-ordered, not shuffled)? why not tune on the test set?
- why scale for logistic regression and SVM but not for trees?
- why this metric (PR-AUC, not accuracy)? why this threshold?
- why this model over a simpler one?
- what would change if you skipped a step?

A good answer names the alternative, the reason, and the evidence (a number or plot).

## For the capstone
Keep a short decision log (ADRs) with one line of "why" and the evidence for each choice. It feeds the report and the 10-minute defence directly.

## Related
- [Defend every number](defend-every-number.md)
- [Classification loss functions compared](classification-loss-functions-compared.md)
- [Temporal leakage in cross-validation](temporal-leakage-in-cross-validation.md)
- [Start simple, add complexity only if it helps](start-simple-add-complexity-only-if-it-helps.md)
