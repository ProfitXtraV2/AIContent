"""One-off Ahrefs discovery (2026-10-10b): matching-terms for broad seeds, BG market.
Usage: python3 ahrefs_discovery_pull.py <seeds.txt> <out-prefix>. Writes <out-prefix>.json/.md next to this file."""
import json, os, sys, urllib.parse, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__))
KEY = os.environ["AHREFS_API_KEY"]
def get(path, params):
    u = "https://api.ahrefs.com/v3" + path + "?" + urllib.parse.urlencode(params)
    r = urllib.request.Request(u, headers={"Authorization": "Bearer " + KEY, "Accept": "application/json"})
    return json.load(urllib.request.urlopen(r, timeout=90))
seeds = [l.strip() for l in open(os.path.join(HERE, sys.argv[1]), encoding="utf-8") if l.strip()]
out = {"limits_before": get("/subscription-info/limits-and-usage", {}), "seeds": {}}
allrows = {}
for s in seeds:
    for ep in ("matching-terms", "related-terms"):
        try:
            rows = get("/keywords-explorer/" + ep, {"country": "bg", "keywords": s, "limit": 100,
                       "select": "keyword,volume,difficulty,intents,parent_topic", "order_by": "volume:desc"}).get("keywords", [])
        except Exception as e:
            rows = []; out["seeds"].setdefault("_errors", []).append(f"{ep} {s}: {e}")
        for r in rows:
            r["seed"] = s; allrows.setdefault(r["keyword"], r)
out["rows"] = list(allrows.values())
out["limits_after"] = get("/subscription-info/limits-and-usage", {})
p = os.path.join(HERE, sys.argv[2])
json.dump(out, open(p + ".json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
with open(p + ".md", "w", encoding="utf-8") as f:
    f.write("| keyword | vol | kd | seed |\n|---|---|---|---|\n")
    for r in sorted(out["rows"], key=lambda r: -(r.get("volume") or 0)):
        if (r.get("volume") or 0) >= 50:
            f.write(f"| {r['keyword']} | {r.get('volume')} | {r.get('difficulty')} | {r['seed']} |\n")
print("ok", len(out["rows"]))
