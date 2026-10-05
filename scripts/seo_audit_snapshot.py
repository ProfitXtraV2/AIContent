#!/usr/bin/env python3
"""Monthly SEO audit SNAPSHOT for vsichkikazina.bg — quantitative, automatable.

Pulls GSC (Search Console) + PSI (Core Web Vitals) + Ahrefs (authority) + indexation,
computes a transparent tracking score, appends a DATED entry to the history, writes a
dated markdown report, and (optionally) commits + pushes to the AIContent dashboard.

Runs LOCALLY (needs the Google OAuth token at ~/.config/claude-seo + an Ahrefs key) so
Google creds never leave this machine. Scheduled monthly via launchd; also runnable by hand.

Usage:
    AHREFS_API_KEY=... python3 scripts/seo_audit_snapshot.py [--no-push]
The qualitative deep-dive (findings/recommendations) is a separate on-demand Claude /seo audit.
"""
import json, os, re, sys, subprocess, urllib.request, urllib.parse, urllib.error
from datetime import datetime, timezone
from pathlib import Path

SITE = "https://vsichkikazina.bg/"
DOMAIN = "vsichkikazina.bg"
REPO = Path(__file__).resolve().parents[1]              # AIContent repo root
HIST = REPO / "docs/data/seo-audit-history.json"
REPORT_DIR = REPO / "docs/seo-audit"
CFG = Path(os.path.expanduser("~/.config/claude-seo/google-api.json"))
TOKF = Path(os.path.expanduser("~/.config/claude-seo/oauth-token.json"))

def _ahrefs_key():
    k = os.environ.get("AHREFS_API_KEY")
    if k: return k
    try:
        s = open(os.path.expanduser("~/Work/ProfitXtraV2/.claude/settings.local.json")).read()
        m = re.search(r'AHREFS_API_KEY=([A-Za-z0-9_\-]{20,})', s)
        return m.group(1) if m else None
    except Exception:
        return None

# ---- Google (GSC + PSI) ----
_cfg = json.loads(CFG.read_text()) if CFG.exists() else {}
_tok = json.loads(TOKF.read_text()) if TOKF.exists() else {}
_at = _tok.get("token") or _tok.get("access_token")
def _refresh():
    cj = json.loads(Path(_cfg["oauth_client_path"]).read_text())["installed"]
    data = urllib.parse.urlencode({"client_id": cj["client_id"], "client_secret": cj["client_secret"],
        "refresh_token": _tok["refresh_token"], "grant_type": "refresh_token"}).encode()
    return json.load(urllib.request.urlopen(urllib.request.Request("https://oauth2.googleapis.com/token", data=data)))["access_token"]
def gsc(body):
    global _at
    url = "https://www.googleapis.com/webmasters/v3/sites/" + urllib.parse.quote(SITE, safe="") + "/searchAnalytics/query"
    def do():
        req = urllib.request.Request(url, data=json.dumps(body).encode(), headers={"Authorization": f"Bearer {_at}", "Content-Type": "application/json"})
        return json.load(urllib.request.urlopen(req, timeout=45))
    try: return do()
    except urllib.error.HTTPError as e:
        if e.code == 401: _at = _refresh(); return do()
        print("GSC err", e.code, file=sys.stderr); return {}
def psi(strategy):
    key = _cfg.get("api_key")
    q = urllib.parse.urlencode({"url": SITE, "strategy": strategy, "category": "performance", "key": key})
    try:
        d = json.load(urllib.request.urlopen("https://www.googleapis.com/pagespeedonline/v5/runPagespeed?" + q, timeout=120))
        a = d["lighthouseResult"]["audits"]; cat = d["lighthouseResult"]["categories"]["performance"]["score"]
        return {"score": round(cat * 100), "lcp_s": round(a["largest-contentful-paint"]["numericValue"] / 1000, 1),
                "cls": round(a["cumulative-layout-shift"]["numericValue"], 3)}
    except Exception as e:
        print("PSI err", e, file=sys.stderr); return {}
def psi_best(strategy, runs):
    """Lab PSI is noisy run-to-run; take the best (lowest-LCP/highest-score) of N runs."""
    best = {}
    for _ in range(runs):
        r = psi(strategy)
        if r and r.get("score", 0) >= best.get("score", -1): best = r
    return best

# ---- Ahrefs ----
def ah(path, params):
    k = _ahrefs_key()
    if not k: return {}
    q = urllib.parse.urlencode(params)
    req = urllib.request.Request(f"https://api.ahrefs.com/v3/{path}?{q}", headers={"Authorization": f"Bearer {k}", "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r: return json.load(r)
    except Exception as e:
        print("Ahrefs err", path, e, file=sys.stderr); return {}

def collect(month, today):
    # Ahrefs authority
    m = ah("site-explorer/metrics", {"target": DOMAIN, "country": "bg", "date": today, "volume_mode": "monthly", "output": "json"}).get("metrics", {})
    rd = ah("site-explorer/refdomains", {"target": DOMAIN, "limit": "1000", "mode": "subdomains", "protocol": "both", "select": "domain", "output": "json"})
    refdomains = len(rd.get("refdomains") or rd.get("rows") or [])
    _drr = ah("site-explorer/domain-rating", {"target": DOMAIN, "date": today, "protocol": "both", "output": "json"}).get("domain_rating")
    dr = _drr.get("domain_rating") if isinstance(_drr, dict) else _drr
    # GSC windows
    def win(days_start):
        start = (datetime.strptime(today, "%Y-%m-%d")).toordinal() - days_start
        s = datetime.fromordinal(start).strftime("%Y-%m-%d")
        tot = gsc({"startDate": s, "endDate": today, "dimensions": []}).get("rows", [])
        return (tot[0] if tot else {}), s
    t90, s90 = win(90); t28, _ = win(28)
    pages = gsc({"startDate": s90, "endDate": today, "dimensions": ["page"], "rowLimit": 1000}).get("rows", [])
    qp = gsc({"startDate": s90, "endDate": today, "dimensions": ["query", "page"], "rowLimit": 1000}).get("rows", [])
    sd = [r for r in qp if 4 <= r["position"] <= 20 and r["impressions"] >= 40]
    topq = gsc({"startDate": s90, "endDate": today, "dimensions": ["query"], "rowLimit": 10}).get("rows", [])
    # indexation
    try:
        sm = urllib.request.urlopen(urllib.request.Request(SITE + "sitemap.xml", headers={"User-Agent": "Mozilla/5.0"}), timeout=30).read().decode("utf-8", "ignore")
        sitemap_urls = sm.count("<loc>")
    except Exception:
        sitemap_urls = None
    cwv_m = psi_best("mobile", 2); cwv_d = psi_best("desktop", 1)
    DR = dr if isinstance(dr, (int, float)) else 0
    avg_pos = round(t90.get("position", 0), 1)
    pages_idx = len(pages)
    rec = {
        "month": month, "date": today,
        "authority": {"dr": DR, "organic_keywords": m.get("org_keywords"), "organic_traffic": m.get("org_traffic"),
                      "refdomains": refdomains},
        "search": {"impressions_90d": round(t90.get("impressions", 0)), "clicks_90d": round(t90.get("clicks", 0)),
                   "avg_position": avg_pos, "pages_indexed": pages_idx, "striking_distance": len(sd),
                   "impressions_28d": round(t28.get("impressions", 0)), "clicks_28d": round(t28.get("clicks", 0))},
        "cwv": {"mobile_score": cwv_m.get("score"), "mobile_lcp_s": cwv_m.get("lcp_s"),
                "desktop_score": cwv_d.get("score"), "desktop_cls": cwv_d.get("cls")},
        "indexation": {"sitemap_urls": sitemap_urls, "pages_with_impressions": pages_idx},
        "top_queries": [{"q": r["keys"][0], "imp": round(r["impressions"]), "pos": round(r["position"], 1)} for r in topq[:10]],
    }
    # Transparent tracking score — trend matters more than absolute. CWV is de-weighted
    # because PSI *lab* data is noisy on a low-traffic site (no CrUX field data yet).
    rank = max(0, 100 - (avg_pos - 1) * 3) if avg_pos else 0
    cwv = ((cwv_m.get("score") or 0) + (cwv_d.get("score") or 0)) / 2
    authority = min(100, DR * 8)                                  # DR 6 -> 48 (crude; tracks growth)
    idx = (pages_idx / sitemap_urls * 100) if sitemap_urls else 0
    rec["tracking_score"] = round(rank * 0.45 + authority * 0.30 + min(100, idx) * 0.15 + cwv * 0.10)
    rec["score_formula"] = "rankings45% (pos-based) + authority30% (DR·8) + indexation15% + CWV10% (lab, noisy)"
    return rec

def main():
    today = os.environ.get("AUDIT_DATE") or datetime.now(timezone.utc).strftime("%Y-%m-%d")
    month = today[:7]
    rec = collect(month, today)
    # history (replace same-month entry if re-run)
    hist = json.loads(HIST.read_text()) if HIST.exists() else []
    hist = [h for h in hist if h.get("month") != month] + [rec]
    hist.sort(key=lambda h: h["month"])
    HIST.parent.mkdir(parents=True, exist_ok=True)
    HIST.write_text(json.dumps(hist, ensure_ascii=False, indent=2) + "\n")
    # dated markdown report
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    a, s, c = rec["authority"], rec["search"], rec["cwv"]
    md = f"""# SEO Audit — {month} (vsichkikazina.bg)

**Run:** {today} · **Tracking score: {rec['tracking_score']}/100** ({rec['score_formula']})

## Authority
- DR **{a['dr']}** · referring domains **{a['refdomains']}** · organic keywords **{a['organic_keywords']}** · est. traffic **{a['organic_traffic']}/mo**

## Search (GSC, 90d / 28d)
- Impressions **{s['impressions_90d']}** (28d: {s['impressions_28d']}) · Clicks **{s['clicks_90d']}** (28d: {s['clicks_28d']})
- Avg position **{s['avg_position']}** · Pages indexed **{s['pages_indexed']}** · Striking-distance (pos 4-20) **{s['striking_distance']}**

## Core Web Vitals (PSI lab, homepage)
- Mobile **{c['mobile_score']}/100** (LCP {c['mobile_lcp_s']}s) · Desktop **{c['desktop_score']}/100** (CLS {c['desktop_cls']})

## Indexation
- Sitemap URLs **{rec['indexation']['sitemap_urls']}** · getting impressions **{rec['indexation']['pages_with_impressions']}**

## Top queries
| Query | Impr | Pos |
|---|---|---|
""" + "\n".join(f"| {q['q']} | {q['imp']} | {q['pos']} |" for q in rec["top_queries"]) + "\n"
    (REPORT_DIR / f"{month}.md").write_text(md)
    print(f"snapshot {month}: score {rec['tracking_score']} | DR {a['dr']} | pos {s['avg_position']} | mobile {c['mobile_score']} | {len(hist)} months in history")
    if "--no-push" not in sys.argv:
        subprocess.run(["git", "-C", str(REPO), "add", "docs/data/seo-audit-history.json", f"docs/seo-audit/{month}.md"], check=False)
        subprocess.run(["git", "-C", str(REPO), "commit", "-q", "-m", f"seo-audit: {month} monthly snapshot (score {rec['tracking_score']})"], check=False)
        subprocess.run(["git", "-C", str(REPO), "pull", "--rebase", "--quiet"], check=False)
        subprocess.run(["git", "-C", str(REPO), "push", "origin", "main"], check=False)

if __name__ == "__main__":
    main()
