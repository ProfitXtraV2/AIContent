import tomllib, json, re, sys, os
D = sys.argv[1]
md = open(os.path.join(D,"content/en-home.md")).read()
pj = json.load(open(os.path.join(D,"content/en-home.port.json")))
_, fm, body = md.split("+++", 2)
t = tomllib.loads(fm)
r = {}
r["toml"] = f"PASS ({len(t['sections'])} sections, {len(t['faq'])} faq, {len(t['owner_items'])} owner_items)"
r["title"] = len(t["title"]); r["meta"] = len(t["meta_description"])
r["meta_has_term"] = "ai automation for small business" in t["meta_description"].lower()
ids = re.findall(r"^## (.+) \{#(\w+)\}$", body, re.M)
r["sections_match"] = [(s["heading"], s["id"]) for s in t["sections"]] == ids
r["bg_ids"] = [s["id"] for s in t["sections"]]
allj = json.dumps(pj, ensure_ascii=False)
r["emdash"] = (md.count("—"), allj.count("—"))
r["markers"] = len(re.findall(r"\[(VERIFY|OWNER CONFIRM|DATA NEEDED|LINK NEEDED)", md+allj))
banned = r"guarantee|revolutionary|magic|game-chang|cutting-edge|next level|seamless|effortless|unlock|supercharg|skyrocket|limitless|10x|double your|certified|discount|promo|voucher|testimonial|last chance|limited spots|hurry|\bthe best\b|leading|delve|robust|leverage|empower|tailored|holistic|synergy|!"
r["banned"] = re.findall(banned, (body+allj).lower())
r["price"] = re.findall(r"\d\s*(лв|лева|евро|€|eur|bgn|\$)", (body+allj).lower())
first100 = " ".join(body.split("{#hero}")[1].split()[:100]).lower()
r["term_first100"] = "ai automation for small business" in first100
r["term_counts_body_h2"] = sum("ai automation for small business" in h.lower() for h,_ in ids)
r["links"] = sorted(set(re.findall(r"\]\(([^)]+)\)", md+allj)))
r["json_keys"] = list(pj.keys())
r["svc"] = [(s["icon"], "href" in s) for s in pj["services"]["items"]]
r["losses_link"] = "link" in pj["losses"]
# every json string appears in md (except unchanged UI chrome)
skip = {"a11y","page","nav","footer","meta"}
miss = []
def walk(o, path):
    if isinstance(o, dict):
        for k,v in o.items(): walk(v, path+[k])
    elif isinstance(o, list):
        for v in o: walk(v, path)
    elif isinstance(o, str) and path[0] not in skip and path[-1] not in ("icon","imageSrc","imageAlt","overlayLabel","overlayUnit","label","n","mailSubject","href"):
        if o not in md: miss.append((".".join(path), o))
walk(pj, [])
r["json_strings_missing_in_md"] = miss
for k in ("title","description","ogTitle","ogDescription"):
    pass
r["meta_equal"] = (pj["meta"]["title"]==t["title"], pj["meta"]["description"]==t["meta_description"])
wb = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", body); wb = re.sub(r"[#*|{}\-]+", " ", wb)
r["body_words"] = len(re.findall(r"[A-Za-z0-9’'%/]+", re.sub(r"\{#\w+\}","",wb)))
for k,v in r.items(): print(k, ":", v)
