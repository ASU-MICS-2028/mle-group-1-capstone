---
summary: Reinforcement learning learns actions by trial, reward and penalty in an environment.
type: concept
tags: [foundations, types-of-learning]
sources: [intro slides]
---
# Reinforcement learning

In reinforcement learning (RL) an **agent** (the decision maker) acts inside an **environment** and tries to collect as much **reward** as possible over time. There is no list of correct answers; there are only better and worse actions.

At each step the agent:
1. sees the current **state**;
2. picks an **action**;
3. gets a **reward** (or penalty) and lands in a new state.

The slides describe this as a loop: perceive → act → get feedback → learn. Example: a game-playing agent that slowly learns which moves lead to winning.

## Related
- [Types of supervision](types-of-supervision.md)
- [Supervised learning](supervised-learning.md)
- [Unsupervised learning](unsupervised-learning.md)
