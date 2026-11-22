# Plans

One plan per workstream, each tracked by a GitHub issue. The plan is the source of truth and the issue is the to-do and discussion. Template: [`../docs/templates/plan.md`](../docs/templates/plan.md).

**Independence:** each plan's `needs` field says whether it waits on anything. Streams that need data build against `src/synthetic.py` until the real table exists ([decision 0003](../docs/decisions/0003-region-week-table-contract.md)).

| WS | Issue | Plan | Needs | Due | Owner | Status |
|---|---|---|---|---|---|---|
| W00 | [#1](https://github.com/ASU-MICS-2028/mle-group-1-capstone/issues/1) | [Repo and working method](W00-repo-and-working-method.md) | — | 16 Nov | Joseph | In review |
| W01 | [#2](https://github.com/ASU-MICS-2028/mle-group-1-capstone/issues/2) | [Flood labels → region-week](W01-labels.md) | — | 18 Nov | Joseph | Not started |
| W02 | [#3](https://github.com/ASU-MICS-2028/mle-group-1-capstone/issues/3) | [Weather features (Earth Engine)](W02-weather-features.md) | — | 19 Nov | Joseph | Not started |
| W03 | [#4](https://github.com/ASU-MICS-2028/mle-group-1-capstone/issues/4) | [Land and terrain features](W03-land-and-terrain-features.md) | — | 25 Nov | Alice | Not started |
| W04 | [#5](https://github.com/ASU-MICS-2028/mle-group-1-capstone/issues/5) | [Label audit](W04-label-audit.md) | — | 27 Nov | Germain | Not started |
| W05 | [#6](https://github.com/ASU-MICS-2028/mle-group-1-capstone/issues/6) | [Table builder, evaluation harness, baselines](W05-evaluation-harness-and-baselines.md) | — (synthetic) | 19 Nov | Joseph | Not started |
| W06 | [#7](https://github.com/ASU-MICS-2028/mle-group-1-capstone/issues/7) | [Compare ≥4 models](W06-model-comparison.md) | W05 | 27 Nov | Alice | Not started |
| W07 | [#8](https://github.com/ASU-MICS-2028/mle-group-1-capstone/issues/8) | [Derivations (LO3)](W07-derivations.md) | — | 4 Dec | Liza | Not started |
| W08 | [#9](https://github.com/ASU-MICS-2028/mle-group-1-capstone/issues/9) | [Related work (LO7)](W08-related-work.md) | — | 4 Dec | Liza | Not started |
| W09 | [#10](https://github.com/ASU-MICS-2028/mle-group-1-capstone/issues/10) | [Ethics and fairness pack (LO5)](W09-ethics-pack.md) | W06 for the numbers | 11 Dec | Germain | Not started |
| W10 | [#11](https://github.com/ASU-MICS-2028/mle-group-1-capstone/issues/11) | [Streamlit dashboard](W10-dashboard.md) | — (synthetic) | 11 Dec | Alice | Not started |
| W11 | [#12](https://github.com/ASU-MICS-2028/mle-group-1-capstone/issues/12) | [Mid-check, Fri 20 Nov](W11-mid-check.md) | W01, W02, W05 | 20 Nov | everyone (Joseph coordinates) | Not started |
| W12 | [#13](https://github.com/ASU-MICS-2028/mle-group-1-capstone/issues/13) | [Report and slides](W12-report-and-slides.md) | results | 4 / 11 / 14 Dec | everyone (Liza edits) | Not started |
| W13 | [#14](https://github.com/ASU-MICS-2028/mle-group-1-capstone/issues/14) | [Knowledge base and learnings](W13-knowledge-base.md) | — | ongoing | Joseph → everyone | In review |
| W14 | [#15](https://github.com/ASU-MICS-2028/mle-group-1-capstone/issues/15) | [Land-change add-on (optional)](W14-land-change-addon.md) | W03, W06 | 4 Dec | Germain | Not started |
| W15 | [#16](https://github.com/ASU-MICS-2028/mle-group-1-capstone/issues/16) | [Contribution statements and declarations](W15-contribution-and-declarations.md) | changes log | 11 Dec | each | Not started |

**Owners** were drawn at random with seed 553, except the critical path, which Joseph holds as project manager ([decision 0006](../docs/decisions/0006-workstream-owners.md)).

**Critical path to the mid-check:** W01 + W02 + W05 → W11. Those three can start today, in parallel.
