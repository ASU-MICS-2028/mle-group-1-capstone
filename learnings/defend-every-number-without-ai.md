---
summary: Work in small explained steps and keep a panel Q&A sheet so anyone can defend any number
type: procedure
tags: [process, debrief, ai-use]
sources: [prosit-2 AGENTS.md rule 1, prosit-1 panel_qa, prosit-1 personal notes "defence scripts", prosit-2 reflections/README]
---
# Defend every number without AI

Both debriefs ended with a live Q&A where any member could be asked about any part, with no AI. Two things helped.

**Small explained steps.** Prosit 2's first working rule: before each step, say in plain words what will be done and why; after it, explain what the result means; then stop and confirm before moving on. Each step's `learnings/` write-up had to be understandable by someone who never ran the code, with likely Q&A questions at the end. Where a step was built mostly by AI, the gap showed: the owner still needed a walkthrough before they could defend it.

**A panel Q&A sheet.** In Prosit 1 we kept one document: likely question → short answer → the number → the notebook section it comes from (e.g. "Why Negative Binomial? Variance ≈ 77,000× the mean; AIC 1,309 vs 4.4 million [§3]"). We assigned who answers which, and updated it whenever a number changed.

Useful self-test from the reflection prompts: which number would you find hardest to explain without notes? Fix that one first.

## For the capstone
Keep `docs/panel_qa.md` from the first result onward, with file references to `learnings/tables/`. Each member should rehearse questions on parts they didn't build, especially the label definition, split, threshold and regional fairness.

## Related
- [ai-drafts-must-match-the-house-format.md](ai-drafts-must-match-the-house-format.md)
- [review-by-rerunning-from-a-fresh-clone.md](review-by-rerunning-from-a-fresh-clone.md)
- [save-every-result-to-a-results-index.md](save-every-result-to-a-results-index.md)
