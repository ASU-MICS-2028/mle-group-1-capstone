---
summary: A decision tree predicts by asking a chain of yes/no questions, learned by greedy splitting.
type: concept
tags: [trees, classification, regression]
sources: [lecture-07 recording, lec5 slides, MIT 6.390 ch9]
---
# Decision tree

A decision tree is an upside-down tree of questions. The **root** at the top asks the first question, **branches** are the answers, **internal nodes** ask more questions, and **leaves** at the bottom give the prediction.

Example from the slides (will a customer buy?):
- Income > 50k? No → no purchase.
- Yes → Age > 30? No → no purchase.
- Yes → Previous purchases > 0? Yes → purchase; No → no purchase.

**How it is built (greedy recursive splitting):**
1. Start with all the data at the root.
2. Try every feature and threshold; pick the question that best separates the classes (largest information gain or Gini drop).
3. Split, then repeat on each impure branch using only the rows that reached it.
4. Stop when leaves are pure or a stopping rule (like max depth) is hit.

A student asked whether a person chooses the questions. No, the algorithm computes them; the lecturer only did it by hand to show the mechanics. "Greedy" means each split is the best one *right now*, not the best for the tree as a whole.

**Prediction:** follow the questions down to a leaf. Classification leaves give the majority class; regression leaves give the average target of their training rows.

Strengths: very interpretable (white box), no feature scaling, mixed feature types, fast. Weaknesses: **high variance** (small data changes give a different tree), overfits without limits, axis-aligned splits struggle with diagonal boundaries.

## Related
- [Entropy and information gain](entropy-and-information-gain.md)
- [Gini impurity](gini-impurity.md)
- [Tree pruning and stopping rules](tree-pruning-and-stopping-rules.md)
- [Random forest](random-forest.md)
- [Black-box models and explainability](black-box-models-and-explainability.md)
