"""Report notes: frontmatter, broken relative links, likely duplicates. Usage: python tools/check_notes.py ."""
import re, sys, pathlib, difflib, collections
root = pathlib.Path(sys.argv[1])
notes = {}
for d in ("knowledge", "learnings"):
    for p in sorted((root / d).glob("*.md")):
        if p.name == "README.md" or p.name == "results_index.md": continue
        t = p.read_text()
        fm = re.match(r"---\n(.*?)\n---\n", t, re.S)
        meta = dict(re.findall(r"^(\w+):\s*(.*)$", fm.group(1), re.M)) if fm else {}
        title = (re.search(r"^# (.+)$", t, re.M) or [None, p.stem])[1]
        notes[p] = (meta, title, t)
bad_fm = [p.name for p, (m, _, _) in notes.items() if not m.get("summary") or not m.get("type")]
broken = collections.Counter()
for p, (_, _, t) in notes.items():
    for link in re.findall(r"\]\(([^)#\s]+\.md)", t):
        if link.startswith("http"): continue
        if not (p.parent / link).resolve().exists(): broken[(p.parent.name + "/" + p.name, link)] += 1
names = [p.stem for p in notes if p.parent.name == "knowledge"]
dups = [(a, b) for i, a in enumerate(names) for b in names[i+1:] if difflib.SequenceMatcher(None, a, b).ratio() > 0.85]
types = collections.Counter(m.get("type", "?").split()[0] for m, _, _ in notes.values())
print("notes:", collections.Counter(p.parent.name for p in notes), "types:", dict(types))
print("missing summary/type:", bad_fm)
print("broken links (%d):" % len(broken)); [print("  ", k[0], "->", k[1]) for k in sorted(broken)]
print("possible duplicates:", dups)
