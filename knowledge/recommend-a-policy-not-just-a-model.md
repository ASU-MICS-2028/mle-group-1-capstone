---
summary: Turn model output into an action plan that works for real people, not the strictest metric-optimal rule.
type: lesson
tags: [decision, deployment, prosit-2, ethics]
sources: [lab-session-1 discussion, lecture-09 recording]
---
# Recommend a policy, not just a model

In Prosit 2, optimising purely for low default would have meant rejecting almost every Ghanaian applicant, because they had no repayment history. That "wins" on the metric but fails the people and the lender's goal.

The final recommendation was a **policy**: give first-time applicants small, limited loans as a test; keep lending to those who repay; collect data and retrain over time. The model supported that plan rather than replacing it.

The lecturer's framing for the capstone fits this: the product should help a real decision-maker decide something, at a specific time.

Ask:

- Who acts on the output, and what exactly do they do?
- What happens to people the model screens out?
- How will new data flow back in to improve the model?

## For the capstone
Do not just ship flood probabilities. Recommend what a NADMO regional office does at each alert level (e.g. "check drains and alert district officers when probability > t"), and how new flood reports will update the model next season.

## Related
- [Capstone scope rules](capstone-scope-rules.md)
- [Cost-based threshold derivation](cost-threshold-derivation.md)
- [Model transfer across places](model-transfer-across-places.md)
