---
summary: An SVM picks the separating boundary with the widest gap to the nearest points of each class.
type: concept
tags: [svm, classification]
sources: [lec5 slides, lecture-07 recording]
---
# Support vector machine (SVM)

Many lines can separate two classes. An SVM picks the one that is **as far as possible from the nearest points** of both classes. That gap is the **margin**; a wide margin leaves room for noise in new points.

- Boundary: w·x + b = 0; predict the sign of w·x + b.
- Margin width = 2 / ‖w‖, so maximising the margin means minimising ‖w‖².
- Only the points closest to the boundary, the **support vectors**, decide where it goes. Moving any other point (without crossing the margin) changes nothing.

Real data overlap, so the practical version is the **soft margin**, which lets some points sit inside the margin or on the wrong side at a cost set by C. With a **kernel**, the boundary can be curved.

Strengths: works well with many features (text, genes); kernels handle non-linear boundaries; convex training, so a unique best answer.

Limits: training gets slow as rows grow (roughly quadratic or worse); **needs standardised features**; C, kernel and γ must be tuned together; hard to interpret; outputs a score, **not a probability** — it needs calibration (Platt scaling) if you want one.

The lecture listed SVM as the "margin-based" family but ran out of time to cover it in the recording; this note follows the slides.

## For the capstone
Our SVM must sit inside a pipeline with a scaler, use `class_weight="balanced"` or threshold tuning, and be calibrated before its outputs are compared with other models' probabilities. A few thousand region-weeks is small enough for an RBF kernel.

## Related
- [Hinge loss and soft margin](hinge-loss-and-soft-margin.md)
- [Kernel trick](kernel-trick.md)
- [Linear classifier](linear-classifier.md)
- [Probability calibration](probability-calibration.md)
- [SVM derivation](svm-derivation.md)
