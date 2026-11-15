# Learnings: what we learned by doing

`knowledge/` is what the course says. `learnings/` is **what we found out ourselves**: lessons from Prosits 1 and 2 (including the marks we lost), procedures that worked and results worth remembering. Notes from this project go here too, one idea per file, in plain words, with the real numbers pasted in.

> **The Prosit notes were drafted with AI from our Prosit 1–2 repos, notes and grade, and are unchecked until a human reads them** ([W13](../plans/W13-knowledge-base.md)).

**How to add one:** copy [`../docs/templates/note.md`](../docs/templates/note.md) and use `type: lesson | procedure | result`. Paste the actual numbers in, and save the tables and figures behind them in `tables/` and `figures/`, listed in [`results_index.md`](results_index.md). Say what you'd do differently, then run `python tools/index_notes.py .` to rebuild this index.

## The five that matter most for the floods project
1. [Time split must respect when labels are known](time-split-must-respect-when-labels-are-known.md): news dates may lag the floods.
2. [Missing is not zero](missing-is-not-zero.md): no report doesn't mean no flood.
3. [Make a fresh clone run without a teammate](make-a-fresh-clone-run-without-a-teammate.md): our biggest Prosit 1 loss.
4. [Calibrate before applying a cost cutoff](calibrate-before-applying-a-cost-cutoff.md) and [derive the cutoff from a cost matrix](derive-the-cutoff-from-a-cost-matrix.md).
5. [Simple models held up better over time](simple-models-held-up-better-over-time.md) and [measure the noise floor before claiming a win](measure-the-noise-floor-before-claiming-a-win.md).

<!-- index: generated from each note's frontmatter; edit the notes, not this table -->

## Lessons: what to repeat or avoid (15)

| Note | In one line |
|---|---|
| [A time split must respect when labels are known](time-split-must-respect-when-labels-are-known.md) | A time split must train only on outcomes known before the test period starts |
| [AI drafts must match the house format](ai-drafts-must-match-the-house-format.md) | AI-drafted report and slides had to be rebuilt in Ashesi templates and our own style |
| [Calibrate before applying a cost cut-off](calibrate-before-applying-a-cost-cutoff.md) | A cost-derived cut-off is only valid on calibrated probabilities; class weights break them |
| [Check the data against the brief first](check-the-data-against-the-brief-first.md) | Inspect the delivered data and dictionary against the brief before writing any model code |
| [Choose the fairness measure before the fix](choose-the-fairness-measure-before-the-fix.md) | Decide which fairness criterion comes first, then compare mitigations against it |
| [Make a fresh clone run without a teammate](make-a-fresh-clone-run-without-a-teammate.md) | Reproducibility lost two marks because a clone needed data handed over by a teammate |
| [Missing is not zero](missing-is-not-zero.md) | An unreported value is missing, often not at random, and must not be coded as zero |
| [Never show raw rows to an AI tool](never-show-raw-rows-to-an-ai-tool.md) | AI tools see shapes, counts, aggregates and made-up rows, never real data rows |
| [Never tune on the test set](never-tune-on-the-test-set.md) | Anything learned from the test set contaminates every later score on it |
| [Normalise by exposure before comparing regions](normalise-by-exposure-before-comparing-regions.md) | Counts across units of different size mostly measure size; model or map rates instead |
| [Plan slack for handovers and the final week](plan-slack-for-handovers-and-the-final-week.md) | Dependent steps slipped and changed hands; plan buffer, early provisional outputs and owners' sign-off |
| [Rank on the upper bound under uncertainty](rank-on-the-upper-bound-under-uncertainty.md) | When data is thin and stakes are high, rank on the upper bound so doubt favours the vulnerable |
| [Report the named subgroup separately](report-the-named-subgroup-separately.md) | When the brief names a subgroup, give its own number, not a table of every group |
| [Source or stress-test every assumed number](source-or-stress-test-every-assumed-number.md) | An unsourced planning number costs marks; measure it, cite it, or show sensitivity |
| [Stratify and group the split](stratify-and-group-the-split.md) | A split can be grouped by cluster and still lose marks if it isn't stratified |

## Procedures: how-tos that worked (16)

| Note | In one line |
|---|---|
| [Audit leaks by building the cheating version](audit-leaks-by-building-the-cheating-version.md) | Quantify each suspected leak by scoring a leaky and a clean model on one test set |
| [Check domain shift with a domain classifier](check-domain-shift-with-a-domain-classifier.md) | Train a classifier to tell old from new data; high AUC means expect transfer failure |
| [Defend every number without AI](defend-every-number-without-ai.md) | Work in small explained steps and keep a panel Q&A sheet so anyone can defend any number |
| [Derive the cut-off from a cost matrix](derive-the-cutoff-from-a-cost-matrix.md) | Set the decision threshold from the costs of each error, then stress-test the costs |
| [Faithful reason codes from a linear model](faithful-reason-codes-from-a-linear-model.md) | For a logistic model, weight × (value − reference) gives exact, checkable reasons |
| [Fit preprocessing inside the fold](fit-preprocessing-inside-the-fold.md) | Every imputer, scaler, encoder, sampler and calibrator is fitted only on training rows |
| [Harmonise boundaries before joining](harmonise-boundaries-before-joining.md) | Ghana's 2018 region split and district renames need an explicit crosswalk before joins |
| [Log actions and AI use as you go](log-actions-and-ai-use-as-you-go.md) | Keep a one-line action log and an AI-use log daily; they become the declaration |
| [Measure the noise floor before claiming a win](measure-the-noise-floor-before-claiming-a-win.md) | Use paired bootstrap intervals and a noise floor before saying one model beats another |
| [One shared feature module](one-shared-feature-module.md) | All notebooks and the deployed app build features from one tested module |
| [Pre-submission check against the rubric](pre-submission-check-against-the-rubric.md) | Before submitting, walk the rubric and last grade line by line and clean out draft traces |
| [Record decisions as ADRs](record-decisions-as-adrs.md) | Each decision gets a short numbered record of options tested, choice, why, consequences |
| [Review by rerunning from a fresh clone](review-by-rerunning-from-a-fresh-clone.md) | A step is merged only after a teammate reruns it from a clean checkout and checks numbers |
| [Save every result to a results index](save-every-result-to-a-results-index.md) | Every printed result, including failures, goes to a file listed in a results index |
| [Test every diverging path in a table](test-every-diverging-path-in-a-table.md) | Where two reasonable choices exist, run both and pick with numbers in a saved table |
| [Write pass rules before the stress test](write-pass-rules-before-the-stress-test.md) | Fix what counts as a pass before running stress tests, and report partial passes honestly |

## Results worth remembering (9)

| Note | In one line |
|---|---|
| [Bootstrap by the correlated unit](bootstrap-by-the-correlated-unit.md) | Resampling rows when rows are correlated gives intervals far too narrow |
| [Calibration data must span all periods](calibration-data-must-span-all-periods.md) | Calibrating on only the newest slice priced everyone at that slice's base rate |
| [Data gaps moved decisions more than models](data-gaps-moved-decisions-more-than-models.md) | Swapping models barely changed the answer; one coarse input swapped four of ten |
| [Features that encode the period hurt on the future](features-that-encode-the-period-hurt-on-the-future.md) | Calendar and slow macro features learn which period a row came from, not risk |
| [Hiding a column does not hide the group](hiding-a-column-does-not-hide-the-group.md) | Dropping a sensitive column rarely removes the group; other features act as proxies |
| [Leaky features top the leaderboard](leaky-features-top-the-leaderboard.md) | When many configurations are compared, the top scorers are usually the leaky ones |
| [Scorer tests catch what metrics miss](scorer-tests-catch-what-metrics-miss.md) | Unit tests on the deployed scorer found gaps that aggregate metrics never showed |
| [Shuffled validation inflates scores](shuffled-validation-inflates-scores.md) | Shuffled splits overstate scores, most for flexible models that memorise units |
| [Simple models held up better over time](simple-models-held-up-better-over-time.md) | On future data, regularised logistic regression beat random forest and LightGBM |
