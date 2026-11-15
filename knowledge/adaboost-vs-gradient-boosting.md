---
summary: AdaBoost re-weights misclassified points; gradient boosting fits the loss gradient and handles noise better.
type: concept
tags: [boosting, ensembles]
sources: [lec5 slides]
---
# AdaBoost vs gradient boosting

Both are boosting: models added one after another, each correcting the last. They differ in *how* the next model is told what to fix.

- **AdaBoost:** after each round, increase the weight of the points that were misclassified, so the next model (usually a depth-1 stump) focuses on them. It implicitly minimises the exponential loss.
- **Gradient boosting:** fit the next tree to the negative gradient of an explicit loss you choose (residuals for MSE, a probability-based error for log loss). Base learners are shallow trees of depth 3–8.

Consequences:
- AdaBoost is **sensitive to noise and outliers**. A mislabelled point keeps getting misclassified, its weight keeps growing, and later models chase it. This matches the exponential loss "blowing up" for badly wrong points.
- Gradient boosting with log loss grows more gently, so noisy labels hurt less.
- Gradient boosting lets you pick the loss, which suits large tabular data and is what XGBoost and LightGBM implement.

## For the capstone
Our news-based labels are noisy (missed and mis-dated floods), which is a reason to prefer gradient boosting (LightGBM, log loss) over AdaBoost.

## Related
- [Gradient boosting](gradient-boosting.md)
- [Classification loss functions compared](classification-loss-functions-compared.md)
