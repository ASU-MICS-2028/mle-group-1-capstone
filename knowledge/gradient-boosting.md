---
summary: Gradient boosting adds shallow trees one at a time, each fitted to the errors of the ensemble so far.
type: concept
tags: [ensembles, trees, boosting]
sources: [lecture-07 recording, lec5 slides]
---
# Gradient boosting

Boosting builds an ensemble **sequentially**. Each new model tries to fix what the current ensemble still gets wrong.

Steps:
1. Start with a constant prediction F₀ (the mean target, or the base rate for classification).
2. Compute the errors. Formally this is the negative gradient of the loss; for squared error it is simply the residuals y − ŷ ("pseudo-residuals" for other losses).
3. Fit a **shallow tree** (depth 1–8) to those errors.
4. Add a small fraction of it: F_new = F_old + η × tree, where η is the learning rate.
5. Repeat for M trees.

Tiny example: targets 10, 20, 30. F₀ = 20, residuals −10, 0, +10. A tree fits them; with η = 0.1 predictions become 19, 20, 21. The next tree fits the remaining −9, 0, +9, and so on.

It is "gradient descent in function space": each tree is a small downhill step on the loss. Any differentiable loss works (MSE, log loss).

Strengths: often the most accurate method on tabular data (XGBoost, LightGBM, CatBoost); captures interactions. Limits: many hyperparameters, trees must be built in order, overfits noisy labels if pushed too far, probabilities need checking.

Correct contrast from class: random forest = independent trees in parallel; boosting = dependent trees in sequence.

## For the capstone
LightGBM is our expected strongest model. Use early stopping on 2023 and `scale_pos_weight` or threshold tuning for the rare flood class.

## Related
- [Boosting learning rate and early stopping](boosting-learning-rate-and-early-stopping.md)
- [AdaBoost vs gradient boosting](adaboost-vs-gradient-boosting.md)
- [Bagging vs boosting](bagging-vs-boosting.md)
- [Gradient boosting derivation](gradient-boosting-derivation.md)
