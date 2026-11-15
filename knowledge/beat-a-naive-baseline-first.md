---
summary: Start with the simplest no-learning policy, measure it, and only claim value if the model beats it.
type: lesson
tags: [evaluation, baselines, prosit-2]
sources: [lab-session-1 discussion, lecture-11 recording, lec5 slides]
---
# Beat a naive baseline first

Before training anything, write down the **default approach**: what would happen with no model at all. Then the model's job is to beat it.

In our Prosit 2 loan-default work, the default was "approve everyone". That gave about a 58% default rate. Every model was then judged against that number, which made the story easy to tell: "the model lowers defaults from X to Y".

Why it matters:

- On imbalanced data, a "predict the majority class" baseline can look very accurate. Without it, a weak model can look good.
- It gives non-technical readers a reference point.
- It catches bugs: a model that cannot beat the baseline is often broken or leaking nothing useful.

The supervised-learning survey slides add a model-level version of this rule: **always keep logistic regression as a baseline**, even when you expect a tree ensemble to win.

## For the capstone
We need at least two baselines: "never alert" (majority class) and a simple rainfall rule (e.g. alert when weekly CHIRPS rainfall is above the region's 90th percentile). Logistic regression, random forest, LightGBM and SVM must beat both on the 2024–2025 test years. The mid-check (20 Nov) expects baselines running.

## Related
- [Accuracy misleads on imbalanced data](accuracy-misleads-on-imbalanced-data.md)
- [Prefer the simpler model when scores tie](prefer-the-simpler-model-when-scores-tie.md)
- [Capstone timeline](capstone-timeline.md)
- [Start simple, add complexity only if it helps](start-simple-add-complexity-only-if-it-helps.md)
- [Logistic regression](logistic-regression.md)
