---
id: 0002
status: Accepted
date: 2026-11-09
owner: Dr. Albert Dede (instructor), on the group's three-option proposal
issue: "—"
---
# 0002 · Project: weekly flood early warning for Ghana's regions (Option B)

## Context
On 7 Nov 2026 we sent a proposal with three options and asked the instructor to choose:
- **A:** galamsey spread with SmallMinesDS;
- **B:** flood early warning with Groundsource;
- **C:** next-day ECG outage risk with nLine GridWatch.

## Decision
The instructor replied on 9 Nov 2026: *"Approved."* He recommended **Option B**:
- The Groundsource file is already downloaded.
- It allows a true split: train on the past, test on the future.

**Galamsey (A) is the fallback.** C is dropped.

## Consequences
- The proposal's Option B scope is the contract we're held to (brief §4.1). Changing it needs the instructor's agreement.
- Within B, the fallback is a Greater Accra flood-susceptibility map (F3 in the flood options report).
- Keeping the train-on-past, test-on-future split is non-negotiable: it is why he picked B ([0004](0004-temporal-split.md)).

## Links
[knowledge/groundsource-dataset.md](../../knowledge/groundsource-dataset.md) · [knowledge/fallback-plans.md](../../knowledge/fallback-plans.md)
