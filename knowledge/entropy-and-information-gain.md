---
summary: Entropy measures how mixed a node is; information gain is how much a split reduces it.
type: concept
tags: [trees]
sources: [lecture-07 recording, lec5 slides]
---
# Entropy and information gain

**Entropy** measures uncertainty in a node:

H = − Σ p_c log₂ p_c (sum over classes c, p_c = share of class c)

- Pure node (all one class): H = 0.
- 50/50 binary node: H = 1, the most uncertain.
- The minus sign is there because the log of a probability is negative or zero, so H comes out non-negative. (Students asked about this.)

**Information gain** = entropy before the split − weighted entropy after:

IG = H(parent) − Σ (n_child / n) · H(child)

Pick the split with the highest gain.

**Worked example from class** (8 students, 5 pass, 3 fail):
- Parent: H = −(5/8)log₂(5/8) − (3/8)log₂(3/8) ≈ 0.954. (The recording says 0.94; 0.954 is correct.)
- Split on *Studied*: yes = 4 pass / 0 fail (H = 0); no = 1 pass / 3 fail (H ≈ 0.811). Weighted ≈ 0.406, so **IG ≈ 0.549**.
- Split on *Attendance*: high = 3/1 (H ≈ 0.811); low = 2/2 (H = 1). Weighted ≈ 0.906, so **IG ≈ 0.049**.
- *Studied* wins and becomes the root.

The lecturer also noted splits do not need equal-sized branches; the aim is separating classes, not equal counts. Regression trees use the same idea with variance (MSE) instead of entropy.

## Related
- [Decision tree](decision-tree.md)
- [Gini impurity](gini-impurity.md)
- [Decision tree split derivation](decision-tree-split-derivation.md)
