---
summary: Gini impurity is the chance of mislabelling a random item; 0 when pure, 0.5 for a 50/50 binary node.
type: concept
tags: [trees]
sources: [lecture-07 recording, lec5 slides]
---
# Gini impurity

Gini impurity is the other common way to score how mixed a tree node is:

Gini = 1 − Σ p_c²

It is the probability you would mislabel a randomly picked item if you labelled it randomly according to the node's class mix.

- Pure node: Gini = 0.
- 50/50 binary node: 1 − (0.25 + 0.25) = **0.5** (entropy gives 1 here).
- Example: 3 pass, 1 fail → 1 − (0.75² + 0.25²) = 1 − 0.625 = 0.375.

Gini vs entropy:
- both are 0 for pure nodes and largest for even mixes;
- they almost always pick the same splits;
- Gini is slightly cheaper (no logarithms);
- **CART**, the algorithm in scikit-learn, uses Gini by default; ID3 and C4.5 use information gain.

Correction: one auto-generated lecture summary wrote the formula as 1 − p²; the correct form sums the squares over all classes.

## Related
- [Entropy and information gain](entropy-and-information-gain.md)
- [Decision tree](decision-tree.md)
- [Feature importance](feature-importance.md)
