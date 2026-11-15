import json, re, sys
W = "/Users/georgitodorov/Work/CoWork/ContentWrite/AIContent-bizgrow/BizGrow/articles/2026-11-15-kakvo-pravi-kopiraytar/"
src = open(W + "05b-final-draft.md", encoding="utf-8").read()

def strip_flags(s):
    s = re.sub(r"\s*\[(VERIFY|OWNER CONFIRM|DATA NEEDED|LINK NEEDED):[^\]]*\]", "", s)
    return s.strip()

def field(name):
    return re.search(r"^- " + name + r": (.*)$", src, re.M).group(1)

title = re.search(r'^title = "(.*?)"', src, re.M).group(1)
meta = re.search(r'^meta_description = "(.*?)"', src, re.M).group(1)
h1 = strip_flags(field("h1"))
lead = field("lead").strip()
label = field("label").strip()
summary = re.sub(r"\s*\(\d+ знака\)$", "", field("summary")).strip()

body = src.split("# BODY", 1)[1].split("\n# FAQ", 1)[0]
blocks = re.split(r"^## ", body, flags=re.M)[1:]
sections = []
for b in blocks:
    head, rest = b.split("\n", 1)
    m = re.match(r"(.*?) \{#([a-z0-9-]+)\}", head.strip())
    t, sid = m.group(1), m.group(2)
    paras, steps, bullets, closing = [], [], [], []
    seen_list = False
    for chunk in [c.strip() for c in rest.strip().split("\n\n") if c.strip()]:
        lines = chunk.split("\n")
        if all(re.match(r"\d+\. ", l) for l in lines):
            steps += [strip_flags(re.sub(r"^\d+\. ", "", l)) for l in lines]; seen_list = True
        elif all(l.startswith("- ") for l in lines):
            bullets += [strip_flags(l[2:]) for l in lines]; seen_list = True
        else:
            (closing if seen_list else paras).append(strip_flags(" ".join(lines)))
    sec = {"id": sid, "title": t, "paragraphs": paras}
    if steps: sec["steps"] = steps
    if bullets: sec["bullets"] = bullets
    if closing: sec["closing"] = closing
    sections.append(sec)

faqtxt = src.split("\n# FAQ", 1)[1].split("\n# FLAGS", 1)[0]
faq = [{"question": q, "answer": a} for q, a in re.findall(r'q = "(.*?)"\na = "(.*?)"', faqtxt)]

page = {
  "path": "/saveti/kakvo-pravi-kopiraytar/", "locale": "bg", "status": "published", "updated": "2026-11-15",
  "primaryKeyword": "копирайтър", "meta": {"title": title, "description": meta},
  "label": label, "summary": summary, "eyebrow": "Съвети", "h1": h1, "lead": lead,
  "sections": sections, "faq": faq,
  "related": ["/seo-statii/", "/seo-optimizacia/", "/socialni-mrezhi/"],
}
json.dump(page, open(W + "_tmp/page.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(json.dumps({k: (v if k not in ("sections","faq") else len(v)) for k, v in page.items()}, ensure_ascii=False, indent=1))
for s in sections: print(s["id"], {k: len(v) for k, v in s.items() if isinstance(v, list)})
