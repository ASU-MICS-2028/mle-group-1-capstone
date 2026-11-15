---
summary: The 0-1 loss counts mistakes; fine for evaluation, useless for training because it has no slope.
type: concept
tags: [loss, classification]
sources: [lecture-06 recording, lec4 slides, MIT 6.390 ch4]
---
# Zero-one loss

The 0-1 loss gives 0 for a correct prediction and 1 for a wrong one. Averaged over a dataset it is the **error rate**; one minus it is **accuracy**. Example: 8 wrong out of 100 means 8% error, 92% accuracy.

**Good for evaluation.** It is easy to explain.

**Bad for training,** as the lecturer stressed:
- It is a step function. Moving the boundary a little usually changes nothing, then suddenly flips one point. There is no smooth slope, so gradient descent has nothing to follow.
- It ignores how wrong you are. Two models with the same number of mistakes look identical, even if one is nearly right on every mistake and the other is far off.
- Minimising it exactly is computationally very hard (NP-hard) in general.

So we train on a smooth **surrogate** loss (usually logistic loss) and only use 0-1-style metrics to judge the result.

And even as an evaluation metric, accuracy misleads badly when one class is rare.

## Related
- [Surrogate loss requirements](surrogate-loss-requirements.md)
- [Accuracy misleads on imbalanced data](accuracy-misleads-on-imbalanced-data.md)
- [Training loss vs evaluation metric](training-loss-vs-evaluation-metric.md)
