# Knowledge: what the course and the sources say

Atomic notes (Zettelkasten): one idea per file, written in our own words from the lecture recordings, slides, the capstone brief, the textbooks and the flood options report. This file is the map. The repo is public, so the original slides, PDFs and transcripts are **not** here.

> **The first pass was drafted with AI and is unchecked until a human reads it** ([W13](../plans/W13-knowledge-base.md)). If you find something wrong, fix the note and mention the fix in your change file. Notes flag mistakes found in the slides and transcripts rather than copying them.

**How to add a note:** copy [`../docs/templates/note.md`](../docs/templates/note.md). Name the file after the idea (`kebab-case.md`), fill in `summary:`, link related notes, then run `python tools/index_notes.py .` (and `python tools/check_notes.py .` for broken links).

## Start here
1. [Capstone rubric](capstone-rubric.md) · [deliverables](capstone-deliverables.md) · [timeline](capstone-timeline.md) · [AI-use policy](ai-use-policy.md)
2. [Flood problem formulation](flood-problem-formulation.md) · [Groundsource dataset](groundsource-dataset.md) · [news label bias](news-label-bias.md)
3. [Data leakage](data-leakage.md) · [temporal split](temporal-split.md) · [forecast leakage](forecast-leakage.md)
4. The notes for your workstream: each plan in [`../plans/`](../plans/README.md) has a "Read first" list.

<!-- index: generated from each note's frontmatter; edit the notes, not this table -->

## Course rules and what the lecturer stressed (41)

| Note | In one line |
|---|---|
| [A fitted distribution is a model](fitted-distribution-is-a-model.md) | Fitting a distribution is modelling; be ready to say what it adds over raw summaries. |
| [Accuracy misleads on imbalanced data](accuracy-misleads-on-imbalanced-data.md) | When one class is rare, a useless model can still score high accuracy. |
| [AI-use policy](ai-use-policy.md) | AI may support learning; private data never goes in; every deliverable needs a declaration |
| [Capstone deliverables](capstone-deliverables.md) | The full list of group and individual capstone deliverables and what each must contain |
| [Capstone learning outcomes (LO1–LO7)](capstone-learning-outcomes.md) | Which of LO1–LO7 the capstone assesses and where each must show up |
| [Capstone proposal requirements](capstone-proposal-requirements.md) | What the one-page proposal had to contain and how approval binds the team to its scope |
| [Capstone resources (from the brief)](capstone-resources.md) | Books, must-read papers, tools and African data portals the brief points to |
| [Capstone rubric](capstone-rubric.md) | The 100-point capstone rubric (worth 40% of the course) by criterion |
| [Capstone scope rules](capstone-scope-rules.md) | What makes a capstone topic acceptable — African, decision-relevant, five-week scope, honest data |
| [Capstone timeline](capstone-timeline.md) | Capstone milestones Weeks 9–15 with what must be ready at each |
| [Choosing a classification threshold](classification-threshold.md) | A probability becomes a yes/no via a threshold; lower it when misses are costly, raise it when false alarms are. |
| [Choosing a supervised model](choosing-a-model.md) | Choose a model by its boundary shape, assumptions, cost, interpretability and data needs, then let validation decide. |
| [Code must run top to bottom from a fresh start](runs-top-to-bottom-from-fresh-clone.md) | Submitted code must run start to finish from a fresh clone or a restarted kernel. |
| [Contribution statement](contribution-statement.md) | Each member writes a half-page contribution statement, submitted with the repo |
| [Course grading and late policy](course-grading-and-late-policy.md) | ICS553 grade weights, the −25%/day late rule, attendance and pass mark |
| [Defend every number](defend-every-number.md) | Every claim in a prosit or capstone must be backed by a number or a simple plot. |
| [Ethics and fairness review pack](ethics-and-fairness-review-pack.md) | The ethics pack needs a Datasheet, Model Card, disaggregated results, proxy analysis, regulatory mapping and a mitigation |
| [Ethics is required in every project](ethics-is-required-in-every-project.md) | The lecturer expects a bias, fairness and ethics discussion in every ML project. |
| [Explain results to non-technical audiences](explain-to-non-technical-audiences.md) | Explaining ML results to non-experts is an assessed skill in every prosit and the defence. |
| [Feature scaling for distance-based methods](feature-scaling-for-distance-based-methods.md) | Standardise features before k-means, PCA or any distance-based method, or big-range features dominate. |
| [Ill-structured problems](ill-structured-problems.md) | Prosits are ill-structured problems with no single right answer; understand before solving. |
| [Justify every design choice](justify-every-design-choice.md) | Assessments ask why each step was done; know the reason behind every design choice, not just the result. |
| [Leakage audit with before/after numbers](leakage-audit-before-after.md) | Reports must include a leakage audit naming each leak with before-and-after scores. |
| [Linear vs exponential vs logistic loss](classification-loss-functions-compared.md) | Linear, exponential and logistic losses compared; logistic loss is the default for binary classification. |
| [Literature review assignment](literature-review-assignment.md) | Individual 10% critical review of one classical-ML topic, at least 10 peer-reviewed sources, 3 compared in depth. |
| [Literature reviews critique, not summarise](literature-review-critiques-not-summarises.md) | A literature review must criticise papers and find gaps, not retell them. |
| [Network depth and width](network-depth-and-width.md) | Depth is layer count, width is neurons per layer; both add capacity, need more data and risk overfitting. |
| [Never tune on the test set](never-tune-on-the-test-set.md) | Touching the test set during model selection is cheating and makes the reported score too optimistic. |
| [Output-layer activation](output-layer-activation.md) | Regression uses a linear output, binary classification one sigmoid, multi-class a softmax. |
| [Presentation and defence format](presentation-and-defence-format.md) | Week 15 talk is ~15 min plus 8–10 min Q&A, six fixed slots, every member speaks |
| [Regulatory mapping for the flood project](regulatory-mapping.md) | Which laws and licences bear on the flood model — data protection, disaster management, data licences |
| [Split first, fit on train](split-first-fit-on-train.md) | Golden rule — split first, learn every preprocessing statistic from training data, apply unchanged elsewhere. |
| [Start simple; add complexity only if it helps](start-simple-add-complexity-only-if-it-helps.md) | Use existing simple models first; move to complex ones only when evidence shows the simple ones fall short. |
| [Team roles](team-roles.md) | Four suggested capstone roles; everyone owns something and can explain the whole system |
| [Technical report structure](technical-report-structure.md) | The capstone report is an 8–12 page research-paper PDF with a fixed section list |
| [Temporal leakage in cross-validation](temporal-leakage-in-cross-validation.md) | Shuffled CV on time-ordered data lets the model peek at the future; splits must keep time order. |
| [Temporal split](temporal-split.md) | For time-ordered data, train on the past and test on the future, never a random shuffle. |
| [The capstone must be end-to-end](end-to-end-pipeline-requirement.md) | The capstone must run the whole ML pipeline, from problem to defensible story, not stop at a score |
| [Training loss vs evaluation metric](training-loss-vs-evaluation-metric.md) | Train on a maths-friendly loss, report a human-readable metric, and make sure the two move together. |
| [Usable artefact requirement](usable-artefact-requirement.md) | The capstone must ship something a non-expert can use by following written instructions |
| [Vanishing gradients](vanishing-gradients.md) | In deep networks, gradients multiplied through many layers can shrink toward zero, so early layers stop learning. |

## Our project: floods in Ghana (13)

| Note | In one line |
|---|---|
| [Existing flood tools and studies](existing-flood-tools.md) | What already exists — Flood Hub, GloFAS, Ghana susceptibility maps, satellite mapping — and the gap left |
| [Fallback plans](fallback-plans.md) | Fallbacks — Greater Accra only, F3 static susceptibility map, or the galamsey spread topic |
| [Flood cost of errors](flood-cost-of-errors.md) | A missed flood leaves people unprepared; a false alert wastes resources and erodes trust in alerts |
| [Flood decision and stakeholders](flood-decision-and-stakeholders.md) | NADMO regional offices and assemblies are the decision-makers; none consulted yet |
| [Flood ethics concerns](flood-ethics-concerns.md) | Unequal visibility drives the flood ethics review — rural under-warning, proxies, false comfort, eviction risk |
| [Flood problem formulation (Option B, approved)](flood-problem-formulation.md) | Approved Option B spec — weekly region-level flood-report classifier with temporal split |
| [Flood project risks](flood-project-risks.md) | Register of flood-project risks and planned responses, from the options report |
| [Flood report: unverified items and open questions](flood-report-open-questions.md) | What the flood options report explicitly did not verify, plus open team questions |
| [Forecast leakage](forecast-leakage.md) | Using rain observed during the predicted week gives great scores for a tool no one could run |
| [Ghana flood context](ghana-flood-context.md) | Why floods matter in Ghana — June 2015 Accra disaster, 2023 Akosombo spillage, structural urban causes |
| [Land-change added value (F2)](land-change-added-value.md) | Research add-on F2 — measure how much land-cover change improves prediction beyond rainfall |
| [News label bias](news-label-bias.md) | News-derived labels measure where reporters are as well as where floods are; silence is not "no flood |
| [Reporting drift](reporting-drift.md) | Rising online news makes later years look floodier; train from 2015, drop the year, validate forward in time |

## Datasets (15)

| Note | In one line |
|---|---|
| [CHIRPS rainfall](chirps.md) | CHIRPS — long daily satellite-plus-gauge rainfall record; our main rainfall feature source |
| [CHIRPS-GEFS rainfall forecasts](chirps-gefs.md) | CHIRPS-GEFS — rainfall forecasts needed for a true forward-looking warning; archive not checked |
| [Copernicus DEM (GLO-30)](copernicus-dem.md) | Copernicus DEM GLO-30 — 30 m elevation for terrain features |
| [Datasheets for datasets (Gebru et al. 2021)](datasheets-for-datasets.md) | A datasheet answers seven groups of questions so users can judge a dataset's fitness and biases |
| [Dynamic World](dynamic-world.md) | Dynamic World — near-real-time 10 m land cover from 2015 (CC BY 4.0) |
| [EM-DAT](em-dat.md) | EM-DAT — international disaster records with impacts; free for non-commercial use after registration |
| [ERA5-Land](era5-land.md) | ERA5-Land — daily reanalysis soil moisture, rain and temperature since 1950 (Copernicus licence) |
| [Ghana boundaries (geoBoundaries and HDX)](geoboundaries.md) | geoBoundaries / HDX — Ghana region and district boundaries used to assign events |
| [GHSL built-up surface](ghsl-built-up.md) | GHSL built-up surface — built-up area in five-year steps from 1975; our urbanisation feature |
| [Global Flood Database](global-flood-database.md) | Global Flood Database — satellite-mapped flood extents 2000–2018, our check on news bias |
| [Groundsource dataset](groundsource-dataset.md) | Groundsource — Google's news-derived global flood events (CC BY 4.0); 2,688 Ghana events, our label source |
| [HydroSHEDS](hydrosheds.md) | HydroSHEDS — river networks and catchments for river-density features |
| [JRC Global Surface Water](jrc-global-surface-water.md) | JRC Global Surface Water — where water has occurred, 1984–2021, from Landsat |
| [OpenStreetMap](openstreetmap.md) | OpenStreetMap — roads, drains and health facilities under ODbL, for an exposure layer |
| [WorldPop](worldpop.md) | WorldPop — 100 m gridded population 2000–2021 (CC BY 4.0) |

## Derivations (LO3) (10)

| Note | In one line |
|---|---|
| [Chain rule in backpropagation](chain-rule-in-backpropagation.md) | A weight's gradient is the product of local derivatives along the path from that weight to the loss. |
| [Class weights distort probabilities (derivation)](class-weights-calibration-derivation.md) | Class weights shift every predicted log-odds by log(w₁/w₀), so weighted models are miscalibrated |
| [Cost-based threshold derivation](cost-threshold-derivation.md) | With calibrated p, act when p > C_FP / (C_FP + C_FN) |
| [Decision tree split criteria and pruning (derivation)](decision-tree-split-derivation.md) | Trees split greedily to maximise impurity decrease (RSS, Gini, entropy) and are pruned by cost complexity |
| [Gradient boosting derivation](gradient-boosting-derivation.md) | Boosting is gradient descent in function space — each tree fits the negative gradient of the loss |
| [K-means objective and convergence](k-means-objective-and-convergence.md) | K-means lowers the within-cluster squared distance every step, so it stops, but often at a local optimum. |
| [Linear regression derivation (MLE → least squares → normal equations)](linear-regression-derivation.md) | Least squares equals Gaussian maximum likelihood, and setting the gradient to zero gives the normal equations |
| [Logistic regression derivation](logistic-regression-derivation.md) | Linear log-odds give the sigmoid; the Bernoulli NLL is log-loss with gradient Xᵀ(p−y) and is convex |
| [Ridge regression derivation](ridge-regression-derivation.md) | Adding λ‖β‖² gives β = (XᵀX+λI)⁻¹Xᵀy, always invertible; lasso instead soft-thresholds |
| [SVM as loss + penalty](svm-derivation.md) | The soft-margin SVM is hinge loss plus a ridge penalty; it outputs distances, not probabilities |

## Ethics and fairness (LO5) (12)

| Note | In one line |
|---|---|
| [Black-box models and explainability](black-box-models-and-explainability.md) | Neural networks are black boxes; you see every number but cannot trace why a decision was made. |
| [Book: Fairness and Machine Learning (FML)](book-fml.md) | Barocas, Hardt & Narayanan's Fairness and Machine Learning — free book behind our fairness criteria |
| [Disaggregated evaluation](disaggregated-evaluation.md) | Report every metric per group and per intersection, with confidence intervals, not just overall |
| [Fairness definitions: independence, separation, sufficiency](fairness-definitions.md) | Most group-fairness definitions are independence, separation or sufficiency |
| [Fairness impossibility results](fairness-impossibility.md) | With unequal base rates, independence, separation and sufficiency cannot all hold, so pick one and justify it |
| [Fairness mitigation options](fairness-mitigation-options.md) | Mitigations act before (reweighting), during (constraints) or after training (group thresholds) |
| [Gender Shades (Buolamwini & Gebru 2018)](gender-shades.md) | Gender Shades showed good average accuracy hiding large intersectional failures, found by auditing data first |
| [Model cards (Mitchell et al. 2019)](model-cards.md) | A Model Card reports a model's intended use and its performance per group, like a nutrition label |
| [Model transfer across places](model-transfer-across-places.md) | A model trained mostly on one country or region may not hold in another with different data. |
| [Proxy variables and redundant encodings](proxy-variables.md) | Dropping a sensitive attribute fails when other features encode it; test by predicting the attribute |
| [Recommend a policy, not just a model](recommend-a-policy-not-just-a-model.md) | Turn model output into an action plan that works for real people, not the strictest metric-optimal rule. |
| [Sampling bias](sampling-bias.md) | Selection, coverage and non-response bias do not shrink with more data; ask who is missing. |

## Leakage, splitting and validation (12)

| Note | In one line |
|---|---|
| [Calibrate on held-out data and keep raw scores](calibrate-on-held-out-data-and-keep-raw-scores.md) | Fit probability calibration on a separate held-out set, and store the uncalibrated scores too. |
| [Cross-validation evaluates the algorithm, not the model](cross-validation-evaluates-the-algorithm.md) | A cross-validation score rates a learning procedure and its settings, not one particular fitted model. |
| [Data leakage](data-leakage.md) | Leakage is information unavailable at prediction time sneaking into training, inflating scores. |
| [Duplicate leakage](duplicate-leakage.md) | The same or near-identical record in both train and test lets the model memorise answers. |
| [K-fold cross-validation](k-fold-cross-validation.md) | K-fold CV rotates which slice of the training data is held out, then averages the K scores. |
| [Leakage red flags](leakage-red-flags.md) | Suspiciously high scores or one dominant feature usually mean leakage, not a great model. |
| [Nested cross-validation](nested-cross-validation.md) | Nested CV tunes in an inner loop and scores in an outer loop, giving an honest estimate. |
| [Out-of-bag (OOB) error](out-of-bag-error.md) | Out-of-bag error tests each tree on the rows its bootstrap missed; it leaks on time or grouped data. |
| [Preprocessing inside cross-validation](preprocessing-inside-cross-validation.md) | In cross-validation, refit preprocessing inside each fold; scikit-learn Pipelines do this automatically. |
| [Target leakage](target-leakage.md) | Target leakage is a feature that exists or takes its value because of the outcome. |
| [Temporal leakage](temporal-leakage.md) | Temporal leakage is using information from after the prediction time to predict earlier events. |
| [Train-test contamination](train-test-contamination.md) | Computing preprocessing statistics on all data before splitting lets the test set leak in. |

## Evaluation, metrics and uncertainty (18)

| Note | In one line |
|---|---|
| [Beat a naive baseline first](beat-a-naive-baseline-first.md) | Start with the simplest no-learning policy, measure it, and only claim value if the model beats it. |
| [Bootstrap confidence interval](bootstrap-confidence-interval.md) | Resample your data with replacement many times to see how much a statistic varies. |
| [Class imbalance and what to do about it](class-imbalance.md) | When one class is rare, use class weights, resampling or threshold tuning, and rare-class metrics. |
| [Cluster bootstrap](cluster-bootstrap.md) | When data come in groups, bootstrap whole groups, or the interval is falsely narrow. |
| [Cluster sampling](cluster-sampling.md) | Cluster sampling picks whole groups; units inside a group are alike, so not independent. |
| [Confidence interval](confidence-interval.md) | A confidence interval is a range of plausible values for a parameter at a stated coverage. |
| [Confusion matrix](confusion-matrix.md) | A confusion matrix counts true/false positives and negatives; most classification metrics come from it. |
| [Design effect](design-effect.md) | Design effect measures how much clustering shrinks the real information in a sample. |
| [F1 score](f1-score.md) | F1 is the harmonic mean of precision and recall; high only when both are high. |
| [Generalisation](generalisation.md) | A model is only useful if it works on new data, not just the data it trained on. |
| [Mean squared error (MSE)](mean-squared-error.md) | MSE averages the squared gaps between predictions and true values; squaring punishes big errors more. |
| [Precision and recall](precision-and-recall.md) | Precision asks how many alarms were real; recall asks how many real cases were caught. |
| [Precision-recall curve and PR-AUC](precision-recall-auc.md) | PR-AUC summarises the precision-recall trade-off over all thresholds; the honest ranking metric for rare events. |
| [Probability calibration](probability-calibration.md) | A model is calibrated when its predicted probabilities match how often the event really happens. |
| [RMSE and MAE](rmse-and-mae.md) | RMSE and MAE report regression error in the target's own units; RMSE weights big errors more. |
| [ROC curve and ROC-AUC](roc-auc.md) | ROC-AUC is the chance a random positive is scored above a random negative; it flatters rare-class models. |
| [Sampling distribution and standard error](sampling-distribution-and-standard-error.md) | A statistic varies from sample to sample; its spread is the standard error (precision, not correctness). |
| [Train, validation and test sets](train-validation-test-split.md) | Train fits the model, validation picks between models, test grades the final choice once. |

## Probability, sampling and statistics (20)

| Note | In one line |
|---|---|
| [Bernoulli distribution](bernoulli-distribution.md) | Bernoulli(p) models one yes/no outcome; its log gives the log-loss used in classification. |
| [Binomial distribution](binomial-distribution.md) | Binomial(n, p) counts successes in n independent trials that share the same p. |
| [Central limit theorem](central-limit-theorem.md) | The mean of many independent observations is roughly normal, even if the data are not. |
| [Choosing a distribution](choosing-a-distribution.md) | Pick a distribution from how the data were generated, not from convenience. |
| [Covariance matrix](covariance-matrix.md) | The covariance matrix holds every feature's variance and every pair's co-movement; PCA starts from it. |
| [Descriptive statistics](descriptive-statistics.md) | Describe data by its centre (mean, median, mode), spread (SD, IQR) and shape (skew, tails). |
| [Law of large numbers](law-of-large-numbers.md) | Sample averages settle on the true average as n grows, but this does not remove bias. |
| [Maximum a posteriori (MAP) estimation](maximum-a-posteriori-estimation.md) | MAP combines the likelihood with a prior belief; with a Gaussian prior it equals L2 regularisation. |
| [Maximum likelihood estimation (MLE)](maximum-likelihood-estimation.md) | MLE picks the parameter values that make the observed data most probable. |
| [Mean vs median for skewed data](mean-vs-median-for-skewed-data.md) | For skewed data the median is a safer centre than the mean, including for imputation. |
| [Naive Bayes](naive-bayes.md) | Naive Bayes applies Bayes' rule assuming features are independent given the class; fast but poorly calibrated. |
| [Negative binomial distribution](negative-binomial-distribution.md) | The negative binomial is a count model that lets the rate vary, so it handles over-dispersion. |
| [Normal (Gaussian) distribution](normal-distribution.md) | The normal is the symmetric bell curve; 68% within 1 SD, 95% within 2 SD. |
| [Over-dispersion](over-dispersion.md) | Count data whose variance exceeds the mean break the Poisson; check variance/mean first. |
| [PMF vs PDF](pmf-vs-pdf.md) | Counts use a PMF (probabilities); measurements use a PDF (densities, only intervals have probability). |
| [Poisson distribution](poisson-distribution.md) | Poisson(λ) models event counts in a window; its mean equals its variance. |
| [Population, sample, parameter, statistic](population-sample-parameter-statistic.md) | We compute statistics on a sample to estimate unknown parameters of the population. |
| [Random variable and distribution](random-variable-and-distribution.md) | A random variable is a numeric outcome; its distribution gives each value's probability. |
| [Sampling weights](sampling-weights.md) | A sampling weight is how many population units each sampled unit represents. |
| [Stratified sampling](stratified-sampling.md) | Stratified sampling splits the population into groups and samples from every group. |

## Data and preprocessing (14)

| Note | In one line |
|---|---|
| [Categorical encoding](categorical-encoding.md) | Turn categories into numbers with one-hot, ordinal, label or target encoding. |
| [Curse of dimensionality](curse-of-dimensionality.md) | With many features, data gets sparse, distances blur and you need far more rows. |
| [Data collection](data-collection.md) | Gather relevant real data, and record where it came from, how and who it misses. |
| [Data integration](data-integration.md) | Merging data sources needs matching entities, resolving code/unit conflicts and dropping redundant columns. |
| [Dataset size and diversity](dataset-size-and-diversity.md) | A dataset is judged by how many examples it has and how much variety they cover. |
| [Dirty data](dirty-data.md) | Real data is dirty in three ways: incomplete, noisy and inconsistent. |
| [Exploratory data analysis (EDA)](exploratory-data-analysis.md) | EDA means summarising and plotting data to find patterns and problems before modelling. |
| [Feature engineering](feature-engineering.md) | Feature engineering builds and picks inputs that expose the signal, using domain knowledge. |
| [Feature selection](feature-selection.md) | Keep only helpful features via forward, backward, bidirectional or tree-based selection. |
| [Garbage in, garbage out](garbage-in-garbage-out.md) | Data quality matters more than the algorithm; most ML project time goes into data work. |
| [Missing value imputation](missing-value-imputation.md) | Options for missing values, from dropping rows to predicting them; fit any filler on train only. |
| [Outlier detection](outlier-detection.md) | Find outliers with z-scores, the IQR rule or clustering; then decide if they are errors. |
| [Smoothing noisy data by binning](smoothing-by-binning.md) | Binning smooths noise by sorting values into bins and replacing each by its bin mean. |
| [Unresolved outcomes at the data cutoff](unresolved-outcomes-at-data-cutoff.md) | Cases whose outcome is not yet known at the data cutoff must not be treated as negatives. |

## Neural networks (12)

| Note | In one line |
|---|---|
| [A single neuron is a linear model](single-neuron-is-a-linear-model.md) | One neuron with a linear (identity) activation is exactly a linear model; non-linear activation changes that. |
| [Activation functions](activation-functions.md) | Activation functions add non-linearity; ReLU is the usual hidden-layer choice, sigmoid/softmax for outputs. |
| [Backpropagation](backpropagation.md) | Backpropagation sends the error backward through the network to get every weight's gradient. |
| [Binary cross-entropy (log loss)](binary-cross-entropy.md) | Binary cross-entropy punishes confident wrong probabilities hard; it is the standard loss for yes/no outputs. |
| [Multi-class vs multi-label classification](multiclass-vs-multilabel-classification.md) | Multi-class picks exactly one class per example; multi-label allows several classes at once. |
| [Multilayer perceptron (MLP)](multilayer-perceptron.md) | An MLP is a feedforward network with one or more hidden layers of non-linear neurons. |
| [Neural network](neural-network.md) | A neural network is layers of neurons; each neuron takes a weighted sum then applies an activation. |
| [Neural network training loop](neural-network-training-loop.md) | Initialise randomly, forward pass, compute loss, backpropagate, update, repeat until the loss stops improving. |
| [Optimisers](optimisers.md) | Optimisers such as momentum and Adam turn gradients into better steps than plain gradient descent. |
| [The XOR problem](xor-problem.md) | No single straight line separates XOR's outputs, so one neuron fails and hidden layers are needed. |
| [Types of neural networks](types-of-neural-networks.md) | Feedforward, CNN, RNN, transformer, autoencoder and GAN suit different kinds of data. |
| [Universal approximation theorem](universal-approximation-theorem.md) | One hidden layer with enough neurons and a non-linear activation can approximate any continuous function. |

## Unsupervised learning (11)

| Note | In one line |
|---|---|
| [Choosing k with the elbow method](elbow-method.md) | Plot k-means loss against k and pick the k where extra clusters stop helping much. |
| [Clustering](clustering.md) | Clustering groups unlabelled points so that close points share a group. |
| [Dimensionality reduction](dimensionality-reduction.md) | Dimensionality reduction re-describes each point with far fewer numbers while keeping most information. |
| [Eigenvectors and eigenvalues in PCA](eigenvectors-and-eigenvalues-in-pca.md) | In PCA, eigenvectors of the covariance matrix give component directions; eigenvalues give their variance. |
| [Explained variance ratio](explained-variance-ratio.md) | Each component's share of total variance, used to decide how many PCA components to keep. |
| [K-means clustering](k-means-clustering.md) | K-means alternates between assigning points to the nearest centre and moving centres to the mean. |
| [K-means limitations](k-means-limitations.md) | K-means needs k fixed in advance, likes round blobs, and is pulled by outliers and unscaled features. |
| [K-means worked example](k-means-worked-example.md) | A two-cluster k-means run by hand on five points, converging after two iterations. |
| [K-means++ initialisation](k-means-plus-plus-initialisation.md) | K-means++ picks starting centres far apart, chosen with probability proportional to squared distance. |
| [PCA limitations](pca-limitations.md) | PCA components are hard to interpret, linear only, sensitive to scale and outliers, and lose some information. |
| [Principal component analysis (PCA)](principal-component-analysis.md) | PCA rotates the data onto new uncorrelated axes ordered by how much variance each one captures. |

## Supervised models and training (35)

| Note | In one line |
|---|---|
| [AdaBoost vs gradient boosting](adaboost-vs-gradient-boosting.md) | AdaBoost re-weights misclassified points; gradient boosting fits the loss gradient and handles noise better. |
| [Bagging (bootstrap aggregating)](bagging.md) | Bagging trains many models on bootstrap resamples and averages them to cut variance. |
| [Bagging vs boosting](bagging-vs-boosting.md) | Bagging averages independent deep trees to cut variance; boosting chains shallow trees to cut bias. |
| [Batch, stochastic and mini-batch gradient descent](batch-stochastic-minibatch-gradient-descent.md) | Batch, stochastic and mini-batch gradient descent differ in how many examples each update uses. |
| [Bias term (intercept)](bias-term-intercept.md) | The intercept is the prediction when all features are zero; a constant feature 1 absorbs it. |
| [Bias-variance trade-off](bias-variance-tradeoff.md) | Test error comes from a too-simple model (bias) or an unstable, data-hungry one (variance). |
| [Boosting: learning rate, tree count and early stopping](boosting-learning-rate-and-early-stopping.md) | In boosting, a small learning rate needs more trees; early stopping on validation data picks the count. |
| [Classification margin](classification-margin.md) | The margin y times score is positive when correct, negative when wrong, and its size shows confidence. |
| [Convexity and local minima](convexity-and-local-minima.md) | A convex loss has one bowl-shaped minimum, so gradient descent cannot get stuck in a worse dip. |
| [Decision tree](decision-tree.md) | A decision tree predicts by asking a chain of yes/no questions, learned by greedy splitting. |
| [Entropy and information gain](entropy-and-information-gain.md) | Entropy measures how mixed a node is; information gain is how much a split reduces it. |
| [Feature importance](feature-importance.md) | Impurity importance comes free from trees; permutation importance is more reliable; neither is causal. |
| [Gini impurity](gini-impurity.md) | Gini impurity is the chance of mislabelling a random item; 0 when pure, 0.5 for a 50/50 binary node. |
| [Gradient boosting](gradient-boosting.md) | Gradient boosting adds shallow trees one at a time, each fitted to the errors of the ensemble so far. |
| [Gradient descent](gradient-descent.md) | Gradient descent finds good parameters by repeatedly stepping downhill on the loss. |
| [Hinge loss and the soft margin](hinge-loss-and-soft-margin.md) | The soft-margin SVM uses hinge loss; C sets how strictly margin violations are punished. |
| [Hyperparameter tuning](hyperparameter-tuning.md) | Try hyperparameter settings on validation data (grid or random search) and keep the best. |
| [k-nearest neighbours (kNN)](k-nearest-neighbours.md) | kNN stores the training data and predicts from the k closest examples by vote or average. |
| [Lasso regression (L1 regularisation)](lasso-regression.md) | Lasso penalises the absolute size of weights and can set some exactly to zero, selecting features. |
| [Learning rate](learning-rate.md) | The learning rate sets the gradient-descent step size; too small is slow, too large overshoots. |
| [Linear classifier](linear-classifier.md) | A linear classifier computes a score and predicts the class from its sign; the boundary is a line. |
| [Linear regression](linear-regression.md) | Linear regression predicts a number as a weighted sum of the features plus a bias. |
| [Logistic regression](logistic-regression.md) | Logistic regression is a linear classifier that turns its score into a probability with the sigmoid. |
| [Normal equation (closed-form least squares)](normal-equation.md) | Ordinary least squares has an exact formula for the best weights, theta = (XᵀX)⁻¹Xᵀy. |
| [Overfitting](overfitting.md) | Overfitting is memorising training noise - low training error, high validation error. |
| [Parameters vs hyperparameters](hyperparameters.md) | Parameters are learned from data; hyperparameters are settings you choose before training. |
| [Prefer the simpler model when scores tie](prefer-the-simpler-model-when-scores-tie.md) | If a simple model matches complex ones on most metrics, ship the simple one. |
| [Random forest](random-forest.md) | A random forest is bagged decision trees that also see only a random subset of features at each split. |
| [Ridge regression (L2 regularisation)](ridge-regression.md) | Ridge adds a penalty on squared weights to the loss, shrinking them and stabilising the fit. |
| [Support vector machine (SVM)](support-vector-machine.md) | An SVM picks the separating boundary with the widest gap to the nearest points of each class. |
| [The supervised learning recipe](supervised-learning-pipeline.md) | Every supervised algorithm follows four steps - hypothesis space, loss, optimiser, validation. |
| [Tree pruning and stopping rules](tree-pruning-and-stopping-rules.md) | Limit tree growth early (pre-pruning) or cut back a full tree (post-pruning) to stop overfitting. |
| [What a good surrogate loss needs](surrogate-loss-requirements.md) | A good classification training loss must decrease with the margin, be convex and be differentiable. |
| [Why logistic regression needs regularisation](logistic-regression-needs-regularisation.md) | Without a penalty, logistic regression on separable data pushes weights to infinity and becomes overconfident. |
| [Zero-one loss](zero-one-loss.md) | The 0-1 loss counts mistakes; fine for evaluation, useless for training because it has no slope. |

## Foundations (10)

| Note | In one line |
|---|---|
| [Problem formulation](problem-formulation.md) | Before any data work, state the target, the prediction moment and what success means. |
| [Regression vs classification](regression-vs-classification.md) | Regression predicts a number; classification predicts a category. |
| [Reinforcement learning](reinforcement-learning.md) | Reinforcement learning learns actions by trial, reward and penalty in an environment. |
| [Semi-supervised learning](semi-supervised-learning.md) | Semi-supervised learning uses a few labelled examples plus many unlabelled ones. |
| [Supervised learning](supervised-learning.md) | Supervised learning learns a mapping from inputs to outputs using labelled examples. |
| [The ML pipeline](ml-pipeline.md) | The standard ordered steps from a vague problem to a deployed ML model. |
| [Types of supervision](types-of-supervision.md) | Supervised, unsupervised, self-supervised and weakly supervised learning differ in where labels come from. |
| [Unsupervised learning](unsupervised-learning.md) | Unsupervised learning finds structure in data that has no labels. |
| [What machine learning is](what-is-machine-learning.md) | ML is software that improves at a task from examples instead of hand-written rules. |
| [When to use machine learning](when-to-use-machine-learning.md) | Use ML when rules are too hard to write and data is plentiful; skip it otherwise. |

## Books and readings (3)

| Note | In one line |
|---|---|
| [Book: HOMLP (Hands-On Machine Learning, Géron)](book-homlp.md) | Géron's HOMLP (Scikit-Learn & PyTorch, 2025) — practical chapters mapped to capstone steps |
| [Book: Interpretable Machine Learning (Molnar)](book-molnar-iml.md) | Molnar's Interpretable Machine Learning — free guide to explaining models (permutation importance, PDP, SHAP) |
| [Book: ISLR (An Introduction to Statistical Learning)](book-islr.md) | ISLR/ISLP — the main free textbook; chapters 2–9 mapped to capstone steps |

## Other (3)

| Note | In one line |
|---|---|
| [Decision log in the repo](decision-log-in-the-repo.md) | Keep a folder recording every decision and why, linked from the README. |
| [Kernel trick](kernel-trick.md) | A kernel computes similarity as if data were mapped to a higher dimension, giving curved boundaries cheaply. |
| [Reproducible literature search strategy](reproducible-literature-search-strategy.md) | Record search strings, databases and a search-dedupe-screen-read funnel so others reach the same papers. |
