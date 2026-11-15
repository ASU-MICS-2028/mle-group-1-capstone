---
summary: Use existing simple models first; move to complex ones only when evidence shows the simple ones fall short.
type: rule
tags: [model-selection, lecturer-emphasis, course-rules]
sources: [lecture-05 recording, lec5 slides]
---
# Start simple; add complexity only if it helps

Two linked pieces of advice from the course:

1. **From the lecturer (lecture 5):** a student asked about designing your own algorithm. The answer was that this is what research does, but you only change or invent a model after you have shown **empirically** that existing models fall short for your problem. Choosing a model family is a decision you must justify with evidence, not taste.
2. **From the survey slides (pitfalls):** "more complexity ≠ better". Start with a simple model and add complexity only if cross-validation shows a real improvement. Also count training cost and prediction speed, not just the score.

In practice:
- begin with baselines (no-skill, simple rule), then logistic regression;
- add trees, forests, boosting or kernels one step at a time;
- keep each step only if the validation score improves by more than the noise (check with a confidence interval);
- if two models tie, prefer the simpler, cheaper, more explainable one.

## For the capstone
Our model ladder is: never-alert and rainfall-rule baselines → logistic regression → random forest → LightGBM, with SVM for comparison. Report each step's gain on 2023 and only claim that a complex model is "better" if the gain is clearly beyond noise.

## Related
- [Beat a naive baseline first](beat-a-naive-baseline-first.md)
- [Choosing a model](choosing-a-model.md)
- [Defend every number](defend-every-number.md)
- [Prefer the simpler model when scores tie](prefer-the-simpler-model-when-scores-tie.md)
