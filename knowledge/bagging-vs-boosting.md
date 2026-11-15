---
summary: Bagging averages independent deep trees to cut variance; boosting chains shallow trees to cut bias.
type: concept
tags: [ensembles]
sources: [lecture-07 recording, lec5 slides]
---
# Bagging vs boosting

Both combine many trees into one stronger model (an **ensemble**), but in opposite ways.

| | Bagging (random forest) | Boosting (gradient boosting) |
|---|---|---|
| how trees are built | independently, in parallel | one after another, each fits the remaining errors |
| tree size | deep | shallow |
| what it reduces | variance | bias |
| tuning | little | more (learning rate, trees, depth) |
| noise | fairly robust | can chase noise and outliers |
| training | parallelises easily | sequential |

A simple picture: bagging is a committee of independent experts who vote; boosting is a relay where each runner corrects the previous runner's mistakes.

Both lose the easy interpretability of a single tree, and neither gives calibrated probabilities by default.

The slide's advice: random forest when you want robustness with minimal tuning; gradient boosting when you want maximum accuracy on tabular data and can afford tuning.

## For the capstone
We run both (random forest and LightGBM). If LightGBM only beats the forest by a hair on 2023, the forest's simpler tuning is an argument worth making.

## Related
- [Bagging](bagging.md)
- [Gradient boosting](gradient-boosting.md)
- [Bias-variance trade-off](bias-variance-tradeoff.md)
