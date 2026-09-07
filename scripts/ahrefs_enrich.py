#!/usr/bin/env python3
"""Enrich a list of keywords with Ahrefs v3 (country=bg): volume, KD, intent, trend.

Usage: AHREFS_API_KEY=... python3 scripts/ahrefs_enrich.py "kw one" "kw two" ...
Prints a TSV: keyword<TAB>volume<TAB>kd<TAB>intent<TAB>trend
Trend from volume-history: last-3-mo mean vs months 9-12-ago mean (+/-10% band).
"""
import os, sys, json, urllib.parse, urllib.request

BASE = "https://api.ahrefs.com/v3"
KEY = os.environ.get("AHREFS_API_KEY")


def _get(path, params):
    q = urllib.parse.urlencode(params)
    req = urllib.request.Request(f"{BASE}/{path}?{q}",
                                 headers={"Authorization": f"Bearer {KEY}",
                                          "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def primary_intent(intents):
    if not isinstance(intents, dict):
        return ""
    # priority order for a casino comparison site
    for k in ("transactional", "commercial", "navigational", "informational", "local", "branded"):
        if intents.get(k):
            return k
    return ""


def trend(keyword):
    try:
        d = _get("keywords-explorer/volume-history",
                 {"country": "bg", "keyword": keyword})
    except Exception:
        return ""
    pts = d.get("metrics") or []
    vals = [p.get("volume") or 0 for p in pts]
    if len(vals) < 13:
        return ""
    recent = sum(vals[-3:]) / 3
    base = sum(vals[-12:-9]) / 3
    if base == 0:
        return "up" if recent > 0 else "flat"
    ratio = recent / base
    return "up" if ratio > 1.10 else "down" if ratio < 0.90 else "flat"


def main():
    kws = sys.argv[1:]
    if not kws:
        print("no keywords", file=sys.stderr); sys.exit(1)
    ov = _get("keywords-explorer/overview",
              {"country": "bg", "keywords": ",".join(kws),
               "select": "keyword,volume,difficulty,cpc,intents"})
    by_kw = {k["keyword"]: k for k in ov.get("keywords", [])}
    for kw in kws:
        row = by_kw.get(kw, {})
        vol = row.get("volume")
        kd = row.get("difficulty")
        intent = primary_intent(row.get("intents"))
        tr = trend(kw) if vol else ""
        print("\t".join([kw,
                          "" if vol is None else str(vol),
                          "" if kd is None else str(kd),
                          intent, tr]))


if __name__ == "__main__":
    main()
