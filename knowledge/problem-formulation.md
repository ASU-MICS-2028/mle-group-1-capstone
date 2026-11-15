---
summary: Before any data work, state the target, the prediction moment and what success means.
type: procedure
tags: [foundations, pipeline]
sources: [intro slides, Terms notes, lecture-01 recording, lecture-02 recording]
---
# Problem formulation

Step one of every ML project is to turn a real-world problem into a precise ML task. Being able to do this is the first learning outcome of the course.

Write down:
- **The target** (the thing you predict) and its type: a number (regression) or a category (classification).
- **The unit of prediction**: one row = what? A patient, a loan, a district-year?
- **The prediction moment**: when is the prediction made, and what information exists at that moment? This one question prevents most leakage later.
- **Who uses the prediction and what they do with it.**
- **Success**: the metric, and what level is good enough to be useful. Compare against a simple baseline.

The lecturer described prosits as *ill-structured* problems: there is no single right answer, so read and understand the problem before analysing anything.

Example: "help the malaria programme" is not a task. "For each district, estimate malaria prevalence with a confidence interval, to rank districts for net delivery" is.

## For the capstone
Target: 1 if at least one news-reported flood happens in a region that week, else 0 (binary classification). Unit: region-week (16 regions). Prediction moment: must be fixed explicitly (e.g. start of the week), because it decides which rainfall values are allowed as features. User: NADMO regional offices.

## Related
- [What machine learning is](what-is-machine-learning.md)
- [Regression vs classification](regression-vs-classification.md)
- [Target leakage](target-leakage.md)
- [Ill-structured problems](ill-structured-problems.md)
