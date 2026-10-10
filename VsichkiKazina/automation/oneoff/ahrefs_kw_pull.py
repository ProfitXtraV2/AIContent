"""One-off Ahrefs pull (2026-10-10): overview metrics for candidate keywords +
matching-terms discovery on a few seeds. Writes kw-pull-2026-10-10.json/.md next to this file."""
import json, os, sys, urllib.parse, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__))
KEY = os.environ["AHREFS_API_KEY"]
def get(path, params):
    u = "https://api.ahrefs.com/v3" + path + "?" + urllib.parse.urlencode(params)
    r = urllib.request.Request(u, headers={"Authorization": "Bearer " + KEY, "Accept": "application/json"})
    return json.load(urllib.request.urlopen(r, timeout=60))
out = {"limits_before": get("/subscription-info/limits-and-usage", {})}
kws = [l.strip() for l in open(os.path.join(HERE, "kw-candidates-2026-10-10.txt"), encoding="utf-8") if l.strip()]
rows = []
for i in range(0, len(kws), 50):
    rows += get("/keywords-explorer/overview", {"country": "bg", "keywords": ",".join(kws[i:i+50]),
                "select": "keyword,volume,difficulty,cpc,intents,parent_topic"}).get("keywords", [])
out["overview"] = rows
out["discovery"] = {}
for seed in ["хазарт", "хазартна зависимост", "закон за хазарта", "забрана за хазарт"]:
    try:
        out["discovery"][seed] = get("/keywords-explorer/matching-terms", {"country": "bg", "keywords": seed,
            "select": "keyword,volume,difficulty", "match_mode": "terms", "order_by": "volume:desc", "limit": 40}).get("keywords", [])
    except Exception as e:
        out["discovery"][seed] = {"error": str(e)}
json.dump(out, open(os.path.join(HERE, "kw-pull-2026-10-10.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
with open(os.path.join(HERE, "kw-pull-2026-10-10.md"), "w", encoding="utf-8") as f:
    f.write("| keyword | vol | kd |\n|---|---|---|\n")
    for r in sorted(rows, key=lambda r: -(r.get("volume") or 0)):
        f.write(f"| {r.get('keyword')} | {r.get('volume')} | {r.get('difficulty')} |\n")
print("ok", len(rows))
