---
summary: Most group-fairness definitions are independence, separation or sufficiency
type: concept
tags: [fairness, reading]
sources: [Barocas, Hardt & Narayanan, FML ch. 3, https://fairmlbook.org/classification.html; Hardt et al. 2016]
---
# Fairness definitions: independence, separation, sufficiency

Notation: $A$ group, $Y$ true outcome, $R$ score, $\hat Y$ decision.

| Criterion | Condition | Binary version | Plain meaning |
|---|---|---|---|
| **Independence** (demographic parity) | $R\perp A$ | Equal alert/positive rate per group | Every group flagged equally often, whatever its real rate |
| **Separation** (equalised odds; *equal opportunity* = equal TPR only) | $R\perp A\mid Y$ | Equal TPR and FPR per group | Among real events, each group is caught equally; among non-events, each is falsely flagged equally |
| **Sufficiency** (calibration by group, predictive parity) | $Y\perp A\mid R$ | Equal PPV/NPV; $P(Y=1\mid R=r,A=a)=r$ | A given score means the same thing in every group |

Notes from FML: calibration by group implies sufficiency; an unconstrained, well-fitted score tends to be roughly sufficient already, while separation must be worked for. Fairness should be checked **at the decision threshold**, because thresholding can break calibration across groups.

## For the capstone
Groups are regions (or urban/rural). The protective criterion is the **recall half of separation**: is a real flood week in Oti as likely to trigger an alert as one in Greater Accra? Independence (equal alert rates) is not the goal when flood rates truly differ, but report it. Caveat: our $Y$ is *reported* floods, so even "equal recall" is measured against biased labels.

## Related
- [Fairness impossibility](fairness-impossibility.md)
- [Proxy variables](proxy-variables.md)
- [Fairness mitigation options](fairness-mitigation-options.md)
- [News label bias](news-label-bias.md)
