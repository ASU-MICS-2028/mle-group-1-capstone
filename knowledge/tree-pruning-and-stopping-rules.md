---
summary: Limit tree growth early (pre-pruning) or cut back a full tree (post-pruning) to stop overfitting.
type: concept
tags: [trees, regularisation, hyperparameters]
sources: [lec5 slides, MIT 6.390 ch9, lecture-07 recording]
---
# Tree pruning and stopping rules

A tree grown until every leaf is pure memorises noise. With enough splits it can give one leaf per training row. Controlling its size is **model selection for trees**.

**Pre-pruning (stop early)** with hyperparameters:
- `max_depth` – how many questions deep;
- `min_samples_split` – a node needs at least this many rows to split;
- `min_samples_leaf` – every leaf must keep at least this many rows;
- a minimum gain threshold.

**Post-pruning (grow, then cut):** grow a full tree, then remove branches that do not earn their keep. **Cost-complexity pruning** scores a tree as total error + α × (number of leaves) and removes the weakest splits first. α (`ccp_alpha` in scikit-learn) is chosen by cross-validation.

Why post-pruning can beat stopping early: some splits look useless alone but pay off after a further split (the XOR pattern). A short-sighted stopping rule would never find them.

Random forests usually skip pruning: they grow deep trees and let averaging control variance. Boosting uses deliberately shallow trees instead.

## For the capstone
For any single tree we show (for explanation on the dashboard), set `min_samples_leaf` high enough that each leaf has several flood weeks, otherwise leaves just memorise individual events.

## Related
- [Decision tree](decision-tree.md)
- [Overfitting](overfitting.md)
- [Hyperparameters](hyperparameters.md)
