# MLE Group 1 · Capstone: weekly flood early warning for Ghana

Should a NADMO regional office or district assembly prepare for flooding this week? For each of Ghana's 16 regions, we predict the chance of at least one reported flood in the coming week from recent rain, soil wetness, terrain and land. A dashboard then shows which regions to watch and why.

ICS553 Machine Learning Essentials, Ashesi University · Alice, Germain, Joseph, Liza · approved 9 Nov 2026 ([decision 0002](docs/decisions/0002-project-flood-early-warning.md))

**New here?** Read [`AGENTS.md`](AGENTS.md) (10 min), then the plan for your issue in [`plans/`](plans/README.md).

## Now

| | |
|---|---|
| **Next milestone** | **Mid-check, Fri 20 Nov:** data in hand, EDA done, baseline running ([W11](plans/W11-mid-check.md)) |
| **Critical path** | [W01 labels](plans/W01-labels.md) + [W02 weather](plans/W02-weather-features.md) + [W05 harness and baselines](plans/W05-evaluation-harness-and-baselines.md), in parallel, all startable today |
| **Waiting on the team** | accept or change [decisions 0001](docs/decisions/0001-working-method.md) and [0003](docs/decisions/0003-region-week-table-contract.md) · register Earth Engine accounts · review the AI-drafted notes for your area |
| **Just finished** | Repo scaffold and first knowledge base ([change 0001](docs/changes/0001-repo-scaffold-and-knowledge-base.md)) |

All workstreams, their owners and status: [`plans/README.md`](plans/README.md).

## Run it

```sh
git clone https://github.com/ASU-MICS-2028/mle-group-1-capstone.git && cd mle-group-1-capstone
uv venv --python 3.12 && uv pip install -r requirements.txt
.venv/bin/python src/synthetic.py      # fake table in the real shape, for building code before the data lands
# real data: download the built tables from the team Drive (link in data/README.md), or rebuild them
```

## Where things are

| Path | What |
|---|---|
| [`AGENTS.md`](AGENTS.md) | How we work (people and AI agents) |
| [`plans/`](plans/README.md) | One plan per workstream / GitHub issue |
| [`docs/decisions/`](docs/decisions/README.md) | One file per decision |
| [`docs/changes/`](docs/changes/README.md) | One file per change: who, what, AI use |
| [`knowledge/`](knowledge/README.md) | Course knowledge as atomic notes (lectures, brief, derivations, datasets) |
| [`learnings/`](learnings/README.md) | What we learned by doing (Prosits 1–2, and this project) · [results index](learnings/results_index.md) |
| [`data/README.md`](data/README.md) | Data sources, licences, columns (the data itself isn't committed) |
| `src/` · `notebooks/` · `app/` · `tests/` · `report/` | Code · exploration · dashboard · checks · report drafts |
