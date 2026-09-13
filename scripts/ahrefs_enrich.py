#!/usr/bin/env python3
"""Enrich a list of keywords with Ahrefs v3 (country=bg): volume, KD, intent, trend.

Usage: AHREFS_API_KEY=... python3 scripts/ahrefs_enrich.py "kw one" "kw two" ...
Prints a TSV: keyword<TAB>volume<TAB>kd<TAB>intent<TAB>trend
Trend from volume-history: last-3-mo mean vs months 9-12-ago mean (+/-10% band).

Unit protection:
- Results are cached in docs/data/ahrefs-cache.json for AHREFS_CACHE_TTL_DAYS
  (default 30 — Ahrefs volumes are monthly figures, refetching sooner returns
  identical data). Cache hits cost 0 units.
- Before any paid call, remaining units are checked via the free
  subscription-info/limits-and-usage endpoint; below AHREFS_MIN_UNITS
  (default 20000) paid calls are skipped and uncached keywords get blank
  metrics, so the pipeline degrades instead of halting.
"""
import os, sys, json, datetime, urllib.parse, urllib.request

BASE = "https://api.ahrefs.com/v3"
KEY = os.environ.get("AHREFS_API_KEY")
COUNTRY = "bg"
CACHE_FILE = os.environ.get("AHREFS_CACHE_FILE") or os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "docs", "data", "ahrefs-cache.json")
CACHE_TTL_DAYS = int(os.environ.get("AHREFS_CACHE_TTL_DAYS", "30"))
MIN_UNITS = int(os.environ.get("AHREFS_MIN_UNITS", "20000"))


def _get(path, params):
    q = urllib.parse.urlencode(params)
    req = urllib.request.Request(f"{BASE}/{path}?{q}",
                                 headers={"Authorization": f"Bearer {KEY}",
                                          "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def load_cache():
    try:
        with open(CACHE_FILE) as f:
            return json.load(f)
    except Exception:
        return {}


def save_cache(cache):
    try:
        os.makedirs(os.path.dirname(CACHE_FILE), exist_ok=True)
        with open(CACHE_FILE, "w") as f:
            json.dump(cache, f, ensure_ascii=False, indent=0, sort_keys=True)
    except Exception as e:
        print(f"ahrefs_enrich: could not write cache: {e}", file=sys.stderr)


def fresh(entry, today):
    try:
        fetched = datetime.date.fromisoformat(entry["fetched"])
    except Exception:
        return False
    return (today - fetched).days < CACHE_TTL_DAYS


def units_remaining():
    """Remaining workspace units, or None if the check itself failed."""
    try:
        d = _get("subscription-info/limits-and-usage", {})
        lu = d.get("limits_and_usage") or {}
        return int(lu["units_limit_workspace"]) - int(lu["units_usage_workspace"])
    except Exception as e:
        print(f"ahrefs_enrich: units check failed: {e}", file=sys.stderr)
        return None


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
                 {"country": COUNTRY, "keyword": keyword})
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

    today = datetime.date.today()
    cache = load_cache()
    by_kw = {}
    misses = []
    for kw in kws:
        entry = cache.get(f"{COUNTRY}|{kw}")
        if entry and fresh(entry, today):
            by_kw[kw] = entry
        else:
            misses.append(kw)

    allow_paid = True
    if misses:
        remaining = units_remaining()
        if remaining is not None and remaining < MIN_UNITS:
            allow_paid = False
            print(f"ahrefs_enrich: {remaining} units left (< {MIN_UNITS}), "
                  f"skipping paid calls for {len(misses)} uncached keyword(s)",
                  file=sys.stderr)

    if misses and allow_paid:
        try:
            ov = _get("keywords-explorer/overview",
                      {"country": COUNTRY, "keywords": ",".join(misses),
                       "select": "keyword,volume,difficulty,cpc,intents"})
            rows = {k["keyword"]: k for k in ov.get("keywords", [])}
        except Exception as e:
            print(f"ahrefs_enrich: overview fetch failed: {e}", file=sys.stderr)
            rows = None
        if rows is not None:
            for kw in misses:
                entry = {"fetched": today.isoformat(), "row": rows.get(kw, {})}
                cache[f"{COUNTRY}|{kw}"] = entry
                by_kw[kw] = entry

    for kw in kws:
        entry = by_kw.get(kw)
        row = (entry or {}).get("row", {})
        vol = row.get("volume")
        kd = row.get("difficulty")
        intent = primary_intent(row.get("intents"))
        if entry is None or not vol:
            tr = ""
        elif "trend" in entry:
            tr = entry["trend"]
        elif allow_paid:
            tr = trend(kw)
            entry["trend"] = tr
        else:
            tr = ""
        print("\t".join([kw,
                          "" if vol is None else str(vol),
                          "" if kd is None else str(kd),
                          intent, tr]))

    save_cache(cache)


if __name__ == "__main__":
    main()
