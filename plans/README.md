# Plans

One plan per workstream, each tracked by a GitHub issue. The plan is the source of truth and the issue is the to-do and discussion. Template: [`../docs/templates/plan.md`](../docs/templates/plan.md).

**Independence:** each plan's `needs` field says whether it waits on anything. Streams that need data build against `src/synthetic.py` until the real table exists ([decision 0003](../docs/decisions/0003-region-week-table-contract.md)).

| WS | Plan | Needs | Due | Owner | Status |
|---|---|---|---|---|---|
| W00 | [Repo and working method](W00-repo-and-working-method.md) | — | 16 Nov | Joseph | In review |
| W01 | [Flood labels → region-week](W01-labels.md) | — | 18 Nov | ? | Not started |
| W02 | [Weather features (Earth Engine)](W02-weather-features.md) | — | 19 Nov | ? | Not started |
| W03 | [Land and terrain features](W03-land-and-terrain-features.md) | — | 25 Nov | ? | Not started |
| W04 | [Label audit](W04-label-audit.md) | — | 27 Nov | ? | Not started |
| W05 | [Table builder, evaluation harness, baselines](W05-evaluation-harness-and-baselines.md) | — (synthetic) | 19 Nov | ? | Not started |
| W06 | [Compare ≥4 models](W06-model-comparison.md) | W05 | 27 Nov | ? | Not started |
| W07 | [Derivations (LO3)](W07-derivations.md) | — | 4 Dec | ? | Not started |
| W08 | [Related work (LO7)](W08-related-work.md) | — | 4 Dec | ? | Not started |
| W09 | [Ethics and fairness pack (LO5)](W09-ethics-pack.md) | W06 for the numbers | 11 Dec | ? | Not started |
| W10 | [Streamlit dashboard](W10-dashboard.md) | — (synthetic) | 11 Dec | ? | Not started |
| W11 | [Mid-check, Fri 20 Nov](W11-mid-check.md) | W01, W02, W05 | 20 Nov | everyone | Not started |
| W12 | [Report and slides](W12-report-and-slides.md) | results | 4 / 11 / 14 Dec | everyone | Not started |
| W13 | [Knowledge base and learnings](W13-knowledge-base.md) | — | ongoing | Joseph → everyone | In review |
| W14 | [Land-change add-on (optional)](W14-land-change-addon.md) | W03, W06 | 4 Dec | ? | Not started |
| W15 | [Contribution statements and declarations](W15-contribution-and-declarations.md) | changes log | 11 Dec | each | Not started |

**Critical path to the mid-check:** W01 + W02 + W05 → W11. Those three can start today, in parallel.
