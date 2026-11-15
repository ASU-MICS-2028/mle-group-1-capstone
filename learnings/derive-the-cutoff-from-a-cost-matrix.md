---
summary: Set the decision threshold from the costs of each error, then stress-test the costs
type: procedure
tags: [threshold, cost-matrix, decision]
sources: [prosit-2 ADR 0007, prosit-2 ADR 0016, prosit-2 learnings/04_cost_matrix]
---
# Derive the cut-off from a cost matrix

Steps we used in Prosit 2:
1. Price each error in money from the brief and the data: a missed default (FN) cost about 4,700 KES, a wrongly declined good payer (FP) about 100 KES (lost fee).
2. Threshold = cost FP ÷ (cost FP + cost FN) → 2.1%. A different country's costs gave 3.2%.
3. Vary every guessed input (recovery 0–30%, double collection cost) and report the range (1.9–2.6%). Add the big structural alternative separately (counting lost repeat business moved it to 9.6%).
4. Compare the cost cut-off against rival policies on each future time block: approve everyone, the alternative cut-off, and fixed "approve the lowest-risk 70/80/90%".

Result: the cost cut-off had the lowest cost per loan (51.1 vs 54.5–85.3 KES). Fixed approval targets lost because they can't tighten when risk rises; the probability cut-off approved 94–98% in the quiet period and far fewer when defaults rose, which was correct, not a fault.

## For the capstone
Price a missed flood week (no warning) against a false alarm (cost of a warning, alert fatigue), cite where each number comes from, and derive the alert threshold. Compare it with "alert the top-k regions each week" across 2024–2025, and show the threshold's range under the cost assumptions.

## Related
- [calibrate-before-applying-a-cost-cutoff.md](calibrate-before-applying-a-cost-cutoff.md)
- [source-or-stress-test-every-assumed-number.md](source-or-stress-test-every-assumed-number.md)
- [../knowledge/cost-threshold-derivation.md](../knowledge/cost-threshold-derivation.md)
