"""The operator list, and the A7 screen of operator and bonus articles (product spec A7, B5, D1).

The list is rebuilt at every drafting run from:
  - VsichkiKazina/affiliate-links.md (operator column);
  - every /casino/<slug>/ page in the site's sitemap.xml, plus the <h1> of that page;
  - the names in settings (operator_names_manual).
The last good copy is kept in <Brand>/social/operators.json, so a run without the site still
has a list, and so the PR checks and the library build (which do not fetch) can use it.

Matching is case-insensitive and whole-word, on the title, the slug (hyphens read as spaces)
and the keywords. A title with a currency amount or a percentage next to an offer word also
makes an article an operator or bonus article.
"""
import json
import re
import sys
import urllib.request
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from social import brands, mdtable  # noqa: E402

USER_AGENT = "PX-Social-Check (+https://github.com/ProfitXtraV2/AIContent)"
GENERIC = {"казино", "casino", "ревю", "review", "отзиви", "онлайн", "online", "бонус", "бонуси",
           "bonus", "bonuses", "bg", "българия", "мнения", "оценка", "регистрация", "вход", "login",
           "app", "приложение", "и", "&", "в", "за", "–", "—", "-"}
AMOUNT = r"(?:[€$£]\s?\d[\d\s.,]*|\d[\d\s.,]*\s?(?:%|€|\$|£|лв\.?|лева|евро|EUR|BGN|free spins|спина|завъртания))"


def from_affiliate(md_text):
    t = mdtable.find(md_text, "operator")
    return [r["operator"].strip() for r in (t["rows"] if t else []) if r.get("operator", "").strip()]


def casino_pages(sitemap_xml):
    """The /casino/<slug>/ addresses of a sitemap, without the /casino/ home itself."""
    urls = re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", sitemap_xml or "")
    return sorted({u for u in urls if re.search(r"/casino/[a-z0-9-]+/?$", u)})


class _H1(HTMLParser):
    def __init__(self):
        super().__init__()
        self.depth, self.text, self.done = 0, [], False

    def handle_starttag(self, tag, attrs):
        if tag == "h1" and not self.done:
            self.depth += 1

    def handle_endtag(self, tag):
        if tag == "h1" and self.depth:
            self.depth -= 1
            self.done = True

    def handle_data(self, data):
        if self.depth and not self.done:
            self.text.append(data)


def h1_of(html):
    p = _H1()
    p.feed(html or "")
    return re.sub(r"\s+", " ", "".join(p.text)).strip()


def name_from_h1(h1):
    """The operator's name from a page title such as „Betano казино ревю 2026 — …“: the words
    before the first separator, without the generic ones."""
    head = re.split(r"[:|—–(]| - ", h1 or "", maxsplit=1)[0]
    words = [w for w in head.split() if w.lower() not in GENERIC and not re.fullmatch(r"\d{4}", w)]
    return " ".join(words) if 1 <= len(words) <= 4 else ""


def name_from_slug(url):
    slug = re.search(r"/casino/([a-z0-9-]+)/?$", url).group(1)
    return slug.replace("-", " ")


def build_list(affiliate_names=(), casino=(), manual=()):
    """The operator names, de-duplicated case-insensitively. casino: [(url, h1)]."""
    names = list(affiliate_names) + list(manual)
    for url, h1 in casino:
        slug_name = name_from_slug(url)
        names.append(slug_name)
        n = name_from_h1(h1)
        # the page title's name only when it adds a spelling (Ефбет next to efbet), never a
        # shorter piece of the slug name (NV next to nv casino)
        if n and not set(n.lower().split()) <= set(slug_name.split()):
            names.append(n)
    seen, out = set(), []
    for n in names:
        k = n.strip().lower()
        if len(k) >= 2 and k not in seen:
            seen.add(k)
            out.append(n.strip())
    return out


def fetch(url, timeout=20):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", "replace")


def refresh(brand_key="vsichkikazina", root=brands.ROOT, manual=(), get=fetch):
    """Rebuild the list from the affiliate file, the site map and settings, and keep it in
    operators.json. When the site cannot be read, the last good site part is kept."""
    b = brands.brand(brand_key)
    aff_path = Path(root) / b["dir"] / "affiliate-links.md"
    affiliate = from_affiliate(aff_path.read_text(encoding="utf-8")) if aff_path.exists() else []
    cache = load_cache(brand_key, root)
    casino, site_ok = cache.get("casino", []), False
    try:
        pages = casino_pages(get(b["site"] + "/sitemap.xml"))
        fresh = []
        for url in pages:
            try:
                fresh.append([url, h1_of(get(url))])
            except Exception:  # noqa: BLE001 — a page that fails keeps only its slug name
                fresh.append([url, ""])
        casino, site_ok = fresh, True
    except Exception:  # noqa: BLE001
        pass
    names = build_list(affiliate, [tuple(c) for c in casino], manual)
    data = {"built_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "site_read": site_ok, "casino": casino, "affiliate": affiliate,
            "manual": list(manual), "names": names}
    p = cache_path(brand_key, root)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return names


def cache_path(brand_key, root=brands.ROOT):
    return brands.social_dir(brand_key, root) / "operators.json"


def load_cache(brand_key, root=brands.ROOT):
    p = cache_path(brand_key, root)
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def current(brand_key="vsichkikazina", root=brands.ROOT, manual=()):
    """The list without fetching anything: the cached site part, the affiliate file and the
    manual names (for the PR checks and the library build)."""
    b = brands.brand(brand_key)
    aff_path = Path(root) / b["dir"] / "affiliate-links.md"
    affiliate = from_affiliate(aff_path.read_text(encoding="utf-8")) if aff_path.exists() else []
    casino = [tuple(c) for c in load_cache(brand_key, root).get("casino", [])]
    return build_list(affiliate, casino, manual)


# --- matching -----------------------------------------------------------------------------

def _word_re(name):
    words = [re.escape(w) for w in name.split()]
    return re.compile(r"(?<![\w])" + r"[\s\-]+".join(words) + r"(?![\w])", re.IGNORECASE)


def named(text, operators):
    """The operators named in a text (whole words, any case)."""
    t = str(text or "")
    return [n for n in operators if _word_re(n).search(t)]


def offer_amount(text, offer_words):
    """A currency amount or a percentage next to an offer word (B5, A7), or ''.
    Next to: in the same clause, at most four words apart."""
    t = str(text or "")
    for m in re.finditer(AMOUNT, t, re.IGNORECASE):
        lo, hi = max(0, m.start() - 60), min(len(t), m.end() + 60)
        window = re.split(r"[.!?;\n]", t[lo:m.start()])[-1] + m.group(0) + re.split(r"[.!?;\n]", t[m.end():hi])[0]
        words = window.lower()
        for w in offer_words:
            if re.search(r"(?<![\w])" + re.escape(w.lower()) + r"(?![\w])", words):
                return m.group(0).strip()
    return ""


def screen(title, slug, keywords, operators, offer_words):
    """A7: (True, reason) when an article is an operator or bonus article."""
    fields = [title or "", (slug or "").replace("-", " "), ", ".join(keywords or [])]
    for f in fields:
        hit = named(f, operators)
        if hit:
            return True, f"names the operator {hit[0]}"
    amt = offer_amount(title, offer_words)
    if amt:
        return True, f"its title states a bonus amount ({amt})"
    return False, ""


def main(argv=None):
    """python3 scripts/social/operators.py refresh [brand]  — rebuild operators.json from the site."""
    import sys
    from social import settings as settingsmod
    args = list(sys.argv[1:] if argv is None else argv)
    if not args or args[0] != "refresh":
        print(main.__doc__)
        return 2
    brand_key = args[1] if len(args) > 1 else "vsichkikazina"
    s = settingsmod.load(brand_key)
    names = refresh(brand_key, manual=s.brand["operator_names_manual"])
    print(f"operators: {len(names)} names ({'site read' if load_cache(brand_key).get('site_read') else 'site NOT read: last good list kept'})")
    return 0


if __name__ == "__main__":
    import sys as _sys
    _sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    raise SystemExit(main())
