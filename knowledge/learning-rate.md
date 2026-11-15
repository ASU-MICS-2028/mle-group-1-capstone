---
summary: The learning rate sets the gradient-descent step size; too small is slow, too large overshoots.
type: concept
tags: [optimisation, hyperparameters]
sources: [lecture-06 recording, lec4 slides, lec5 slides]
---
# Learning rate

The learning rate α is the size of each gradient-descent step. It is a **hyperparameter**: you choose it, the model does not learn it.

- **Too small:** each step is tiny, so reaching the minimum takes very many steps.
- **Too large:** steps jump over the valley, bounce from side to side, and may never settle or even fly off (diverge).

Ways to pick it, from the lecture:
- **Line search:** at each update try a few values (0.1, 0.01, 0.001) and keep the one that lowers the loss most.
- **Decaying schedule:** big steps while far from the minimum, smaller steps near it. The lecturer's analogy: take a bus most of the way, then a short ride for the last stretch.

For stochastic gradient descent, the step size must shrink over time for it to settle (for example α = 1/t).

The same word appears in **gradient boosting**, where the learning rate (shrinkage) scales how much each new tree is allowed to correct. Small values (0.01–0.1) need more trees but usually generalise better.

## For the capstone
LightGBM's `learning_rate` and number of trees trade off against each other. Tune them together on the 2023 tuning year, with early stopping on that year, never on the 2024–2025 test years.

## Related
- [Gradient descent](gradient-descent.md)
- [Gradient boosting](gradient-boosting.md)
- [Hyperparameters](hyperparameters.md)
