import json
W = "/Users/georgitodorov/Work/CoWork/ContentWrite/AIContent-bizgrow/BizGrow/articles/2026-11-15-kakvo-pravi-kopiraytar/"
p = json.load(open(W + "_tmp/page.json", encoding="utf-8"))
def q(s): return json.dumps(s, ensure_ascii=False)
kind = lambda s: "steps" if "steps" in s else ("list" if "bullets" in s else "paragraphs")
L = ["+++",
 f"title = {q(p['meta']['title'])}",
 f"meta_description = {q(p['meta']['description'])}",
 f"h1 = {q(p['h1'])}",
 'slug = "kakvo-pravi-kopiraytar"', 'locale = "bg"', f"primary_keyword = {q(p['primaryKeyword'])}",
 'secondary_keywords = ["какво е копирайтър", "копирайтър значение", "добър копирайтър"]',
 'status = "draft"', 'last_updated = "2026-11-15"',
 f"path = {q(p['path'])}", f"eyebrow = {q(p['eyebrow'])}", f"label = {q(p['label'])}", f"summary = {q(p['summary'])}",
 "related = [" + ", ".join(q(r) for r in p["related"]) + "]", ""]
L += ["[[sections]]", 'id = "hero"', f"heading = {q(p['h1'])}", 'kind = "hero"', 'dictionary_key = ""', ""]
for s in p["sections"]:
    L += ["[[sections]]", f"id = {q(s['id'])}", f"heading = {q(s['title'])}", f"kind = {q(kind(s))}", 'dictionary_key = ""', ""]
for f in p["faq"]:
    L += ["[[faq]]", f"q = {q(f['question'])}", f"a = {q(f['answer'])}", ""]
L += ["[[sources]]",
 'title = "Google Search Central: Creating helpful, reliable, people-first content"',
 'url = "https://developers.google.com/search/docs/fundamentals/creating-helpful-content"',
 'checked_by = ""', 'checked_on = ""', ""]
owner = [
 "H1 (new page): „Какво прави копирайтърът и кога Ви трябва“, taken from the keyword-map.md proposal. Please confirm.",
 "Example kept in #zadanie: a hypothetical brief for a beauty-salon service page (no numbers), labelled „Примерно задание (пример, не реален случай)“. Please confirm the example and the label.",
 "Content tool review: the page states only that nothing is published before the client approves it. Does anyone at BizGrow (editor or copywriter) review the tool's output before the client sees it? If yes, the owner may add it; the page never implies that BizGrow employs copywriters.",
 "New sourced fact in #seo-avtor: „Според насоките на Google автоматичните системи за класиране в търсачката са създадени да показват полезна и надеждна информация, написана преди всичко в полза на хората.“ Source: https://developers.google.com/search/docs/fundamentals/creating-helpful-content (HTTP 200 on 2026-11-15). Quote: \"Google's automated ranking systems are designed to prioritize helpful, reliable information that's created to benefit people, not content that's created to manipulate search engine rankings.\" Note: the source says „prioritize“ (дават предимство на); the page says „показват“. Confirm or ask for „да дават предимство на“.",
 "Article fields for the /saveti/ hub: eyebrow „Съвети“, label „Какво прави копирайтърът“, summary (135 characters), related /seo-statii/, /seo-optimizacia/, /socialni-mrezhi/. The summary and the meta description open with the same words; confirm or vary.",
]
for o in owner:
    L += ["[[owner_items]]", f"item = {q(o)}", 'decision = ""', 'decided_by = ""', 'decided_on = ""', ""]
L += ["+++", "", f"## {p['h1']} {{#hero}}", "", p["lead"], ""]
for s in p["sections"]:
    L += [f"## {s['title']} {{#{s['id']}}}", ""]
    for x in s["paragraphs"]: L += [x, ""]
    if "steps" in s: L += [f"{i}. {x}" for i, x in enumerate(s["steps"], 1)] + [""]
    if "bullets" in s: L += [f"- {x}" for x in s["bullets"]] + [""]
    for x in s.get("closing", []): L += [x, ""]
open(W + "content/kakvo-pravi-kopiraytar.md", "w", encoding="utf-8").write("\n".join(L).rstrip() + "\n")
json.dump(p, open(W + "content/kakvo-pravi-kopiraytar.port.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
open(W + "content/kakvo-pravi-kopiraytar.port.json", "a").write("\n")
