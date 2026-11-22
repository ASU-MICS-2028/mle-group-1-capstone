---
id: 0006
status: Accepted
date: 2026-11-22
owner: Joseph (project manager)
issue: "#1"
---
# 0006 · Workstream owners: Joseph holds the critical path, the rest drawn at random

## Context
The 16 workstreams had no owners. Joseph manages the project, so the streams that block others (labels, weather features, the evaluation harness, the mid-check) sit with him; if they slip, everything slips. The other streams were split at random so no one picks the easy ones.

## Options we tested
| Option | What happened | Verdict |
|---|---|---|
| Pick by preference | Not tried; slow, and the team asked for random | Rejected |
| Random for everything | Could put a blocker with someone who is not managing the schedule | Rejected |
| Joseph takes the blockers, random for the rest | Draw below | **Chosen** |

## Decision
- **Joseph (@josetseph):** W00 repo, W01 labels, W02 weather features, W05 harness and baselines, W11 mid-check (coordinates), W13 knowledge base set-up.
- **Alice (@thealiceiris):** W03 land and terrain, W06 model comparison, W10 dashboard.
- **Germain (@germainemil1):** W04 label audit, W09 ethics pack, W14 land-change add-on.
- **Liza (@lnaikins):** W07 derivations, W08 related work, editor for W12 report and slides.
- **Everyone:** writes their own sections of W12, keeps up W13, writes their own W15 statement.

## Why
The draw is reproducible:
```python
import random
r = random.Random(553)
ws = ['W03','W04','W06','W07','W08','W09','W10','W14','W12-editor']
people = ['lnaikins','thealiceiris','germainemil1']
r.shuffle(ws); r.shuffle(people)
for i, w in enumerate(ws): print(w, people[i % 3])
```
Three streams each.

## Consequences
- Swaps are allowed: agree on them in the group chat, then write a new decision that replaces this one.
- W14 (Germain) needs W03 and W06 (both Alice), so those two should agree early on the column names they hand over.
- W06 (Alice) builds on W05 (Joseph); until W05 lands, use `src/synthetic.py`.

## Links
[plans/README.md](../../plans/README.md)
