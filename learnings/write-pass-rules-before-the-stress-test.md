---
summary: Fix what counts as a pass before running stress tests, and report partial passes honestly
type: procedure
tags: [evaluation, decision, honesty]
sources: [prosit-2 ADR 0021, prosit-2 ADR 0020 scenario test]
---
# Write pass rules before the stress test

With hundreds of scenarios it's easy to find one that makes a favoured policy look good. In Prosit 2 we wrote the pass rules down **before** running the tests:

1. List concrete rules, each with a threshold. For example: beats every rival on both data halves *and* in at least 95% of resampled draws; beats rivals in at least 90% of 2,880 assumption combinations; still wins if the risky group defaults twice as often; no more than a fixed amount above the cheapest policy, even when the policy is picked on one half and tested on the other.
2. Run the chosen policy and **every** alternative (729 policies) against the same rules.
3. Report the scorecard as it came out. Ours passed 4 of 6; two failed (77–87% of draws vs 95%; 78% of assumptions vs 90%). No policy passed more than 4.
4. Set the decision's status to match: "accepted as a capped, unproven pilot", with "what would change our mind".

We also noted where the rules weren't fully blind (one main table was already known), which a reader deserves to know.

## For the capstone
Before evaluating on 2024–2025, write the bar in an ADR: e.g. "beats the persistence baseline's PR-AUC beyond the noise floor in both 2024 and 2025, recall at least X in every region with at least N flood-weeks". Then report pass or fail per rule.

## Related
- [measure-the-noise-floor-before-claiming-a-win.md](measure-the-noise-floor-before-claiming-a-win.md)
- [record-decisions-as-adrs.md](record-decisions-as-adrs.md)
- [never-tune-on-the-test-set.md](never-tune-on-the-test-set.md)
