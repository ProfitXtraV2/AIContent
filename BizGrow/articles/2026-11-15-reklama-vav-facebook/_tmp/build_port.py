import json, re, sys, tomllib

md_path, out_path = sys.argv[1], sys.argv[2]
text = open(md_path, encoding="utf-8").read()
_, fm, body = text.split("+++", 2)
d = tomllib.loads(fm)

blocks = re.split(r"^## ", body.strip(), flags=re.M)
blocks = [b for b in blocks if b.strip()]
parsed = []
for b in blocks:
    head, _, rest = b.partition("\n")
    m = re.match(r"(.*) \{#([a-z0-9-]+)\}$", head.strip())
    title, sid = m.group(1), m.group(2)
    paras, bullets, steps, closing = [], [], [], []
    for chunk in [c.strip() for c in rest.strip().split("\n\n") if c.strip()]:
        lines = chunk.split("\n")
        if all(l.startswith("- ") for l in lines):
            bullets += [l[2:] for l in lines]
        elif all(re.match(r"\d+\. ", l) for l in lines):
            steps += [re.sub(r"^\d+\. ", "", l) for l in lines]
        else:
            (closing if (bullets or steps) else paras).append(" ".join(lines))
    parsed.append((sid, title, paras, bullets, steps, closing))

hero = parsed[0]
assert hero[0] == "hero"
sections = []
for sid, title, paras, bullets, steps, closing in parsed[1:]:
    s = {"id": sid, "title": title, "paragraphs": paras}
    if bullets: s["bullets"] = bullets
    if steps: s["steps"] = steps
    if closing: s["closing"] = closing
    sections.append(s)

page = {
    "path": "/reklama-vav-facebook/",
    "locale": "bg",
    "status": "published",
    "updated": "2026-11-15",
    "primaryKeyword": d["primary_keyword"],
    "meta": {"title": d["title"], "description": d["meta_description"]},
    "label": d["label"],
    "summary": d["summary"],
    "eyebrow": d["eyebrow"],
    "h1": d["h1"],
    "lead": " ".join(hero[2]),
    "sections": sections,
    "faq": [{"question": f["q"], "answer": f["a"]} for f in d["faq"]],
    "related": d["related"],
    "service": "Реклама във Facebook и Instagram",
}
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(page, f, ensure_ascii=False, indent=2)
    f.write("\n")
