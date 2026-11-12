"""Is the page live, and does it still show what the post quotes (product spec F2, F5; tech
spec flows 6 and 9).

An article is live when its address answers and either its queue row is `posted` or the
publisher's record lists its slug. A section intro is live when the record lists
`hub-intro-<category>` with the path `blog/<category>` and that address answers; its queue
status is never used. Record deploy times are never compared with anything.

The live-page check at hand-over: every number of the post (B4 exceptions apart) and every
phrase it puts in quotation marks must be on each page the post draws on.

The site is fetched with the User-Agent PX-Social-Check, each address at most once a run.
Redirects are followed only while they stay on the brand's domain.
"""
import re
import urllib.error
import urllib.parse
import urllib.request

from social import brands, links, pagetext
from social import postnumbers as numbers

UA = "PX-Social-Check"
QUOTED = re.compile(r"[„“\"«]([^„“”\"«»\n]{2,200}?)[“”\"»]")


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def http_get(url, timeout=20):
    """(status, body text) of one request, without following redirects; (status, location)
    for a redirect; (0, error) when the site cannot be reached."""
    opener = urllib.request.build_opener(_NoRedirect)
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html"})
    try:
        with opener.open(req, timeout=timeout) as resp:
            return resp.status, resp.read(3_000_000).decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        if e.code in (301, 302, 303, 307, 308):
            return e.code, e.headers.get("Location", "")
        return e.code, ""
    except (urllib.error.URLError, TimeoutError, OSError, ValueError) as e:
        return 0, str(e)


class Site:
    """The brand's own pages, fetched once per run. get(url) → (status, text or location)."""

    def __init__(self, brand_key, get=http_get, max_redirects=5):
        self.domain = brands.brand(brand_key)["domain"]
        self.get, self.max_redirects, self.cache = get, max_redirects, {}

    def _ours(self, url):
        host = (urllib.parse.urlsplit(url).hostname or "").lower()
        return host in (self.domain, "www." + self.domain)

    def fetch(self, url):
        """{"ok": status 200 on our domain, "status", "url": final address, "text", "error"}."""
        if url in self.cache:
            return self.cache[url]
        cur, out = url, None
        for _ in range(self.max_redirects + 1):
            if not self._ours(cur):
                out = {"ok": False, "status": 0, "url": cur, "text": "", "error": "leaves the brand's domain"}
                break
            status, text = self.get(cur)
            if status in (301, 302, 303, 307, 308):
                cur = urllib.parse.urljoin(cur, text)
                continue
            out = {"ok": status == 200, "status": status, "url": cur, "text": text if status == 200 else "",
                   "error": "" if status == 200 else (text if status == 0 else f"HTTP {status}")}
            break
        if out is None:
            out = {"ok": False, "status": 0, "url": cur, "text": "", "error": "too many redirects"}
        self.cache[url] = out
        return out


def record_entries(record):
    """{slug: {"path", …}} from the publisher record (WebPortals .published-state.json)."""
    if not isinstance(record, dict):
        return {}
    for key in ("articles", "pages", "items", "published"):
        if isinstance(record.get(key), dict):
            return record[key]
    return {k: v for k, v in record.items() if isinstance(v, dict) and v.get("path")}


def intro_category(slug):
    return slug[len("hub-intro-"):] if str(slug).startswith("hub-intro-") else None


def live_address(item, record, brand_settings, brand_key):
    """The address an item has on the site: from the publisher record, else (articles only)
    from the brand's address pattern. None for an intro the record does not list."""
    site = brands.brand(brand_key)["site"]
    entry = record_entries(record).get(item["slug"]) or {}
    path = str(entry.get("path") or "").strip("/")
    cat = intro_category(item["slug"])
    if cat is not None or item.get("kind") == "hub-intro":
        return f"{site}/{path}/" if path == f"blog/{cat}" else None
    if path:
        return f"{site}/{path}/"
    return links.address_for(item["slug"], brand_settings)


def is_live(item, record, brand_settings, brand_key, site):
    """(live, address, why not) for a library item (F2)."""
    address = live_address(item, record, brand_settings, brand_key)
    if address is None:
        return False, None, "the publisher's record has no address for this section intro"
    in_record = item["slug"] in record_entries(record)
    is_intro = intro_category(item["slug"]) is not None or item.get("kind") == "hub-intro"
    if not is_intro and item.get("board_status") != "posted" and not in_record:
        return False, address, "not deployed yet (board not posted, not in the publisher's record)"
    got = site.fetch(address)
    if not got["ok"]:
        return False, address, f"the address does not answer ({got['error'] or got['status']})"
    return True, address, ""


def quoted_phrases(text):
    return [m.group(1).strip() for m in QUOTED.finditer(str(text or "")) if m.group(1).strip()]


def missing_on_pages(fields, page_texts, names=()):
    """What a post quotes that the pages do not show: its numbers (B4 exceptions apart) and the
    phrases it puts in quotation marks."""
    joined = "\n".join(pagetext.flat(t) for t in page_texts)
    missing = []
    for where, value in (("text", fields.get("text", "")), ("image", "\n".join(fields.get("image_text") or [])),
                         ("text", fields.get("alt_text", ""))):
        for tok in numbers.tokens(numbers.without_names(value, names)):
            if numbers.is_exception(tok, where) or numbers.occurs(tok, joined):
                continue
            missing.append(tok)
        for phrase in quoted_phrases(value):
            if not pagetext.contains(joined, phrase):
                missing.append(phrase)
    return list(dict.fromkeys(missing))
