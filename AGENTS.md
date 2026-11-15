# AGENTS.md: how we work in this repo (people and their AI agents)

Claude Code (via `CLAUDE.md`), Codex, Cursor and Copilot read this file. Humans: same rules.

## The project in one paragraph
ICS553 Final Capstone (40% of the course), MLE Group 1: Alice, Germain, Joseph, Liza.
- **The question:** should a NADMO regional office or district assembly prepare for flooding this week?
- **The ML task:** for each of Ghana's 16 regions and each week, predict the chance of at least one news-reported flood, from rain, soil wetness, terrain and land. Labels come from Google's Groundsource. Train 2015–2022, tune on 2023, test on 2024–2025.
- **The artefact:** a Streamlit dashboard showing each region's risk this week, the rain behind it, and an honest caveat about what the label means.
- **Approved** by Dr. Dede on 9 Nov 2026 ([decision 0002](docs/decisions/0002-project-flood-early-warning.md)). The fallback is galamsey spread prediction.
- **Dates:** mid-check **Fri 20 Nov** (data in hand, EDA, baseline running) · repo due **Fri 11 Dec** · presentations **14–18 Dec**.

## The system: issues → plans → changes, decisions, learnings

| Thing | Where | One file per… | Index |
|---|---|---|---|
| **Task** | GitHub issue + `plans/WNN-<slug>.md` | workstream/task | [`plans/README.md`](plans/README.md) |
| **Decision** | `docs/decisions/NNNN-<slug>.md` | decision | [`docs/decisions/README.md`](docs/decisions/README.md) |
| **Change** (incl. who + AI use) | `docs/changes/NNNN-<slug>.md` | change / PR | [`docs/changes/README.md`](docs/changes/README.md) |
| **Course knowledge** | `knowledge/<idea>.md` | idea | [`knowledge/README.md`](knowledge/README.md) |
| **What we learned doing it** | `learnings/<idea>.md` | lesson / result / procedure | [`learnings/README.md`](learnings/README.md) |
| **Saved results** | `learnings/tables/`, `learnings/figures/` | result | [`learnings/results_index.md`](learnings/results_index.md) |

Templates for each are in [`docs/templates/`](docs/templates/).

## The working rules
1. **Every task is a GitHub issue with a plan file.** The plan (`plans/WNN-*.md`) is the source of truth: the goal, inputs, the exact outputs others rely on, steps, and done-when. The issue links it, tracks the checklist and is where we discuss. No work without an issue.
2. **Workstreams don't wait on each other.** Each plan states what it `needs`. If it needs another stream's output, it builds against the **shared contract** ([decision 0003](docs/decisions/0003-region-week-table-contract.md)) using the synthetic table until the real one lands. Waiting is allowed only where a plan says so explicitly.
3. **Every change gets a change file, and the change file records AI use.** Copy [`docs/templates/change.md`](docs/templates/change.md), take the next number, and add a row to the index. It says what we did, which files changed and who was in charge. It also has the **AI-use table**: which part, which tool, what the AI did, and what the human checked. These files feed the report's AI declaration and the contribution statements.
4. **Every decision gets its own decision file.** Whenever there's more than one reasonable way to do something, try them, put the numbers in a table and choose using the numbers. Never reopen a decision silently: write a new one that replaces it.
5. **Notes are atomic (Zettelkasten).** One idea per file, a kebab-case name after the idea, a `summary:` line in the frontmatter, and relative links to related notes. Each folder's `README.md` is the index (the "map of content"). Add a line there whenever you add a note.
6. **Write simply.** Use short sentences, explain every term, and add a small example when an idea is abstract. Each of us must be able to explain the whole system in the defence **without AI**.
7. **Save every result**, including failures and rejected options, to `learnings/tables/` or `learnings/figures/`, and add a line to `learnings/results_index.md`. A number that exists only in a terminal or a chat doesn't count.
8. **The README shows only the current state:** the Now box, the workstream board and how to run. History lives in the change files.

## Data rules (hard rules; the repo is public)
- **`data/` is never committed.** Only `data/README.md` is, recording each source, its link, licence, and how to fetch it.
- **Never paste raw data rows into an AI tool or a chat.** Print shapes, counts, value counts, summaries or scores only. Groundsource is public CC BY 4.0, but the rule still holds; the course AI policy forbids uploading private data.
- **No time leakage.** A feature for week *t* may use only information available before week *t* starts ([decision 0004](docs/decisions/0004-temporal-split.md)). Never use year as a feature. Never shuffle across time.
- **Fix random seeds.** Notebooks must run top to bottom from a fresh clone.

## Git
- Each member works on a branch named `wNN-<slug>` and commits from their own account.
- **Commit messages say how AI was used** (the lecturer asked for this in lecture 11). End each one with a line such as `AI: Claude Code drafted evaluate.py; Ama reran the checks`, or `AI: none`.
- PR titles use the form `WNN: <what>`. The PR includes the change file, and closes the issue once someone else has reviewed it (rerun it fresh and spot-check the numbers).
- Never force-push `main`.

## Done means
- [ ] runs from a fresh clone
- [ ] options compared in a table, results saved and indexed
- [ ] decision file(s), a change file with the AI-use table, and learning note(s), each added to its index
- [ ] plan status set to Done, issue closed after review
- [ ] README Now box updated

## Commands
```sh
uv venv --python 3.12 && uv pip install -r requirements.txt
```
New dependency: `uv pip install <pkg>`, then pin it in `requirements.txt`.
