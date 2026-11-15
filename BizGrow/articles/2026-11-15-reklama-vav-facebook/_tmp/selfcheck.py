import json, re, sys, tomllib

md_path, js_path, links_path = sys.argv[1:4]
text = open(md_path, encoding="utf-8").read()
_, fm, body = text.split("+++", 2)
d = tomllib.loads(fm)
p = json.load(open(js_path, encoding="utf-8"))
links_md = open(links_path, encoding="utf-8").read()
allowed = set(re.findall(r"^\| (/[^ |]*) \|", links_md, flags=re.M))
anchors_own = {s["id"] for s in d["sections"]}
res = []
def chk(name, ok, info=""):
    res.append((name, ok, info))

title, meta = d["title"], d["meta_description"]
chk("TOML parses", True)
chk("title <= 60 incl suffix", len(title) <= 60 and title.endswith(" | BizGrow"), len(title))
chk("meta 120-160", 120 <= len(meta) <= 160, len(meta))
pk = d["primary_keyword"]
chk("meta contains primary kw", pk in meta.lower())
chk("JSON meta == TOML", p["meta"]["title"] == title and p["meta"]["description"] == meta)
low = body.lower()
first100 = " ".join(body.split("{#hero}", 1)[1].split()[:100]).lower()
chk("pk in title", pk in title.lower())
chk("pk in H1 (Latin variant)", "платена реклама във facebook" in d["h1"].lower())
chk("pk in first 100 words", pk in first100)
h2s = re.findall(r"^## (.*) \{#", body, flags=re.M)
chk("pk in one H2 (definite variant „платената“)", sum(("платената реклама във фейсбук" in h.lower()) or (pk in h.lower()) for h in h2s[1:]) == 1)
ids_body = re.findall(r"\{#([a-z0-9-]+)\}", body)
heads_body = h2s
chk("sections <-> body ids/headings in order",
    ids_body == [s["id"] for s in d["sections"]] and heads_body == [s["heading"] for s in d["sections"]])
chk("JSON section ids == body (minus hero)", [s["id"] for s in p["sections"]] == ids_body[1:])
alltext = text + json.dumps(p, ensure_ascii=False)
chk("zero em-dashes (md+json)", "—" not in alltext)
chk("zero bracketed markers", not re.search(r"\[(VERIFY|OWNER CONFIRM|DATA NEEDED|LINK NEEDED)", alltext))
visible = body + " ".join(f["q"] + " " + f["a"] for f in d["faq"]) + title + meta + d["h1"] + d["summary"]
ti = re.findall(r"\b(ти|те|твой\w*|теб|тебе|губиш|получаваш|попълваш|Открий|Запази|поправи)\b", visible)
ti_ctx = re.findall(r"\w+ те \w+", visible)
ti = [x for x in ti if x != "те"] + [c for c in ti_ctx if c != "защото те зависят"]
chk("zero „ти“ forms (\"защото те зависят\" = 3rd-person „they“, reviewed)", not ti, ti)
chk("zero „доклад“", "доклад" not in alltext.lower())
chk("zero delivery periods", not re.search(r"48 часа|седмиц|за дни|до \d+ (дни|часа)", alltext.lower()))
banned = r"гарантир|гаранци|първо място|топ позиции|лидер|най-добр|революцион|магия|магическ|невероят|уникал|безпрецедент|следващо ниво|напълно автоматично|мощен ai|10x|удвои|сертифицира"
chk("zero banned words", not re.search(banned, visible.lower()), re.findall(banned, visible.lower()))
chk("zero PRICE/OFFER/TESTIMONIAL", not re.search(r"\d\s*(лв|лева|евро|€|eur|bgn|\$)|промоци|отстъпк|ваучер|отзив|доволни клиенти", visible.lower()))
nums = sorted(set(re.findall(r"(?<![A-Za-z])\d+(?![A-Za-z])", re.sub(r"(?m)^\d+\. ", "", re.sub(r"\{#.*?\}", "", visible)))))
chk("numbers only canon (30)", nums == ["30"], nums)
lk = re.findall(r"\]\(([^)]+)\)", alltext)
bad = [l for l in lk if not (l in allowed or l == "{{BOOKING_URL}}" or (l.startswith("#") and l[1:] in anchors_own))]
chk("every link in conversion-links.md", not bad, sorted(set(lk)))
rel = p["related"]
chk("related = 3 allowed, not / nor self", len(rel) == 3 and all(r in allowed and r not in ("/", "/reklama-vav-facebook/") for r in rel), rel)
chk("BOOKING_URL x2 body, EMAIL x1 body", body.count("{{BOOKING_URL}}") == 2 and body.count("{{EMAIL}}") == 1)
chk("max one booking CTA per section", all(b.count("{{BOOKING_URL}}") <= 1 for b in body.split("\n## ")))
chk("no hard-coded email/URL", not re.search(r"@|https?://", body))
inv = {"I3": "/diagnostika/", "I4": "/reklama/", "I5": "реален маркетинг специалист", "I6": "отчита се пред вас с конкретни числа",
       "I7": "какво връща всяко вложено евро", "I8": "отчет вместо задачи", "I9": "кой какво купува, кога се връща",
       "I11": "/socialni-mrezhi/", "I12": "30-минутен разговор", "I13": "оферта с приоритизирани решения и ясни еднократни цени",
       "I14": "срокът зависи от решението и го посочваме в офертата", "I15": "кратък месечен отчет", "I16": "без дългосрочни договори",
       "I17": "цените са прозрачни", "I18": "работим по gdpr", "I19": "не ви задължава с нищо", "I1": "[запазете безплатна диагностика]({{booking_url}})",
       "I2": "{{email}}", "I10": "facebook и instagram"}
miss = [k for k, v in inv.items() if v not in low]
chk("inventory I1-I19 present (I20 n/a)", not miss, miss)
chk("no budget separate/included statement", not re.search(r"(бюджет\w*).{0,60}(отделно|включен)", visible.lower()))
chk("JSON strings exact vs md (lead/faq/h1)", p["h1"] == d["h1"] and p["faq"][0]["answer"] == d["faq"][0]["a"] and p["lead"] in body)
chk("JSON required keys", all(k in p for k in ["path","locale","status","updated","primaryKeyword","meta","label","summary","eyebrow","h1","lead","sections","faq","related","service"]))
chk("decision/checked fields empty", all(o["decision"] == o["decided_by"] == o["decided_on"] == "" for o in d["owner_items"]) and all(s["checked_by"] == s["checked_on"] == "" for s in d["sources"]))

def words(s): return len(re.findall(r"[\wА-Яа-я{}-]+", re.sub(r"\]\([^)]*\)", "]", s)))
sec_text = []
for s in p["sections"]:
    for k in ("paragraphs", "bullets", "steps", "closing"):
        sec_text += s.get(k, [])
body_wc = words(" ".join(sec_text))
lead_wc = words(p["lead"])
faq_wc = words(" ".join(f["question"] + " " + f["answer"] for f in p["faq"]))
for n, ok, info in res:
    print(("PASS" if ok else "FAIL"), "|", n, "|", info)
print("passed", sum(ok for _, ok, _ in res), "/", len(res))
print("body words (sections only)", body_wc, "| lead", lead_wc, "| faq words", faq_wc, "| owner_items", len(d["owner_items"]))
