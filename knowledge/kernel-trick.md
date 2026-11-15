---
summary: A kernel computes similarity as if data were mapped to a higher dimension, giving curved boundaries cheaply.
type: concept
tags: [svm]
sources: [lec5 slides]
---
# Kernel trick

Some data cannot be split by a straight line in its original features but can be after mapping to more dimensions.

Example: points on a number line, class A near 0 and class B far out on both sides (−3 and +3). No single threshold separates them. Add a second feature x²: now A has small x² and B has large x², and a straight line splits them.

Building those extra features explicitly can be huge or even infinite. The trick: the SVM's maths only ever needs **dot products** between pairs of points. A **kernel** K(x, z) computes that dot product in the big space directly, without building it.

Common kernels:
- **linear:** plain dot product (no mapping);
- **polynomial:** curved boundaries of a chosen degree;
- **RBF (Gaussian):** K = exp(−γ‖x − z‖²). Similarity falls off with distance. γ sets how far each point's influence reaches: large γ = very local, wiggly boundary (overfitting risk); small γ = smooth boundary;
- sigmoid.

Tune C and γ together by cross-validation. Because the RBF kernel uses distances, features must be standardised first.

## Related
- [Support vector machine](support-vector-machine.md)
- [Hinge loss and soft margin](hinge-loss-and-soft-margin.md)
- [Feature scaling for distance-based methods](feature-scaling-for-distance-based-methods.md)
