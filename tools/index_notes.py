"""Rebuild knowledge/README.md and learnings/README.md note tables from frontmatter. Usage: python tools/index_notes.py ."""
import re, sys, pathlib
root = pathlib.Path(sys.argv[1])
def load(d):
    out = []
    for p in sorted((root / d).glob("*.md")):
        if p.name in ("README.md", "results_index.md"): continue
        t = p.read_text(); fm = re.match(r"---\n(.*?)\n---\n", t, re.S).group(1)
        g = lambda k: (re.search(rf"^{k}:\s*(.*)$", fm, re.M) or [None, ""])[1].strip().strip('"')
        tags = {x.strip() for x in g("tags").strip("[]").split(",") if x.strip()}
        title = re.search(r"^# (.+)$", t, re.M).group(1)
        out.append(dict(file=p.name, title=title, summary=g("summary"), type=g("type").split()[0], tags=tags))
    return out
K = [  # (section, test) first match wins
 ("Course rules and what the lecturer stressed", lambda n: n["type"] == "rule" or n["tags"] & {"brief", "course-rules", "lecturer-emphasis"}),
 ("Our project: floods in Ghana", lambda n: "flood" in n["tags"] and n["type"] != "source"),
 ("Datasets", lambda n: n["type"] == "source" and n["tags"] & {"flood", "data", "dataset", "labels"}),
 ("Derivations (LO3)", lambda n: n["type"] == "derivation"),
 ("Ethics and fairness (LO5)", lambda n: n["tags"] & {"fairness", "ethics"}),
 ("Leakage, splitting and validation", lambda n: n["tags"] & {"leakage", "cross-validation", "validation"}),
 ("Evaluation, metrics and uncertainty", lambda n: n["tags"] & {"evaluation", "metrics", "uncertainty"}),
 ("Probability, sampling and statistics", lambda n: n["tags"] & {"probability", "sampling", "statistics"}),
 ("Data and preprocessing", lambda n: n["tags"] & {"data", "preprocessing", "data-quality", "eda"}),
 ("Neural networks", lambda n: "neural-networks" in n["tags"]),
 ("Unsupervised learning", lambda n: n["tags"] & {"unsupervised", "k-means", "pca", "clustering"}),
 ("Supervised models and training", lambda n: n["tags"] & {"classification", "regression", "linear-models", "trees", "ensembles", "loss", "regularisation", "optimisation", "hyperparameters", "model-selection", "supervised"}),
 ("Foundations", lambda n: "foundations" in n["tags"]),
 ("Books and readings", lambda n: n["type"] == "source" or "reading" in n["tags"]),
 ("Other", lambda n: True),
]
L = [("Lessons: what to repeat or avoid", lambda n: n["type"] == "lesson"),
     ("Procedures: how-tos that worked", lambda n: n["type"] == "procedure"),
     ("Results worth remembering", lambda n: True)]
def table(notes, secs):
    groups = {s: [] for s, _ in secs}
    for n in notes: groups[next(s for s, f in secs if f(n))].append(n)
    out = []
    for s, ns in groups.items():
        if not ns: continue
        out += [f"\n## {s} ({len(ns)})\n", "| Note | In one line |", "|---|---|"]
        out += [f"| [{n['title']}]({n['file']}) | {n['summary'].replace('|', '/')} |" for n in sorted(ns, key=lambda n: n["title"].lower())]
    return "\n".join(out) + "\n"
MARK = "<!-- index: generated from each note's frontmatter; edit the notes, not this table -->"
for d, secs in (("knowledge", K), ("learnings", L)):
    p = root / d / "README.md"; head = p.read_text().split(MARK)[0] if p.exists() else ""
    notes = load(d); p.write_text(head.rstrip() + "\n\n" + MARK + "\n" + table(notes, secs)); print(d, len(notes))
