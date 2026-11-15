import sys; sys.path.insert(0, sys.argv[3]); import tomli as tomllib, json, re
src = sys.argv[1]; out = sys.argv[2]
txt = open(src, encoding="utf-8").read()
_, fm, body = txt.split("+++", 2)
d = tomllib.loads(fm)
blocks = re.split(r"^## (.+?) \{#([a-z0-9-]+)\}\s*$", body, flags=re.M)
secs = []
for i in range(1, len(blocks), 3):
    secs.append((blocks[i], blocks[i+1], blocks[i+2].strip()))
assert [s[1] for s in secs] == [s["id"] for s in d["sections"]], "id order"
assert [s[0] for s in secs] == [s["heading"] for s in d["sections"]], "heading order"
def parse(b):
    paras, bullets, steps, closing = [], [], [], []
    seen_list = False
    for chunk in re.split(r"\n\s*\n", b):
        lines = chunk.strip().split("\n")
        if all(l.startswith("- ") for l in lines):
            bullets += [l[2:] for l in lines]; seen_list = True
        elif all(re.match(r"\d+\. ", l) for l in lines):
            steps += [re.sub(r"^\d+\. ", "", l) for l in lines]; seen_list = True
        else:
            p = " ".join(l.strip() for l in lines)
            (closing if seen_list else paras).append(p)
    return paras, bullets, steps, closing
hero = secs[0]; assert hero[1] == "hero"
lead_p, *_ = parse(hero[2]); assert len(lead_p) == 1
sections = []
for h, i, b in secs[1:]:
    p, bl, st, cl = parse(b)
    s = {"id": i, "title": h, "paragraphs": p}
    if bl: s["bullets"] = bl
    if st: s["steps"] = st
    if cl: s["closing"] = cl
    sections.append(s)
page = {"path": "/izrabotka-na-sait/", "locale": "bg", "status": "published", "updated": "2026-11-15",
 "primaryKeyword": d["primary_keyword"], "meta": {"title": d["title"], "description": d["meta_description"]},
 "label": d["label"], "summary": d["summary"], "eyebrow": d["eyebrow"], "h1": d["h1"], "lead": lead_p[0],
 "sections": sections, "faq": [{"question": f["q"], "answer": f["a"]} for f in d["faq"]],
 "related": d["related"], "service": d["service"]}
json.dump(page, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
open(out, "a").write("\n")
