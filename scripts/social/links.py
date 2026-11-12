"""Where posts may link, and how links are tagged (product spec B6, B7).

Posts are drafted with the placeholder [[LINK]]. The publishing check fills it at hand-over with
the item's live address plus four tags, and nothing else in the text changes.
"""
import re
from urllib.parse import urlsplit, urlencode

from social import brands

LINK = "[[LINK]]"
NO_LINK_REASONS = ("link in profile", "no link: account setting", "no link: no fitting page",
                   "no link: none given")                    # the last: a post a person wrote without a link

# A number next to one of these in an address is a bonus amount, not a year or a game name.
AMOUNT_WORDS = {"eur", "euro", "evro", "evra", "leva", "lv", "bgn", "procenta", "procent", "pct",
                "percent", "spins", "spina", "spinove", "fs", "zavartania", "zavartaniya", "free"}
WEB_ADDRESS = re.compile(r"(https?://|www\.|\b[a-z0-9-]+\.(?:bg|com|de|eu|net|org|io|info)\b(?:/|\b))",
                         re.IGNORECASE)


def address_for(slug, brand_settings):
    """The address an article has by the brand's pattern (never used for section intros)."""
    return brand_settings["address_pattern"].replace("{slug}", slug)


def tagged(url, network, campaign, content):
    """The live address with its four tags (B6): source, medium, campaign, content."""
    utm = {"utm_source": brands.NETWORKS[network]["utm"], "utm_medium": "social",
           "utm_campaign": campaign, "utm_content": content}
    sep = "&" if urlsplit(url).query else "?"
    return url + sep + urlencode(utm)


def profile_link(brand_key, account_id, blog_path="/blog/"):
    """The Instagram profile link (B6): the blog home, tagged per account."""
    b = brands.brand(brand_key)
    return (f"{b['site']}{blog_path}?" +
            urlencode({"utm_source": "instagram", "utm_medium": "social",
                       "utm_campaign": "profile", "utm_content": account_id}))


def _slug_words(path):
    return [w for w in re.split(r"[^a-z0-9]+", path.lower()) if w]


def bonus_amount_in(path):
    """True when an address shows a bonus amount: a number next to a currency, percent or spins
    word (years such as 2026 and plain game numbers do not count)."""
    words = _slug_words(path)
    for i, w in enumerate(words):
        if not w.isdigit() or re.fullmatch(r"(19|20)\d\d", w):
            continue
        near = set(words[max(0, i - 1):i]) | set(words[i + 1:i + 2])
        if near & AMOUNT_WORDS:
            return True
    return bool(re.search(r"\d+(?:%|eur|evro|lv)\b", path.lower()))


def operator_in(path, operators):
    """The first operator whose name appears as whole words in the address, or None."""
    words = _slug_words(path)
    joined = " " + " ".join(words) + " "
    for name in operators:
        slugged = " ".join(_slug_words(_translit(name)))
        if slugged and f" {slugged} " in joined:
            return name
    return None


_BG = str.maketrans({"а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e", "ж": "zh", "з": "z",
                     "и": "i", "й": "y", "к": "k", "л": "l", "м": "m", "н": "n", "о": "o", "п": "p",
                     "р": "r", "с": "s", "т": "t", "у": "u", "ф": "f", "х": "h", "ц": "ts", "ч": "ch",
                     "ш": "sh", "щ": "sht", "ъ": "a", "ь": "y", "ю": "yu", "я": "ya"})


def _translit(name):
    return str(name).lower().translate(_BG)


def allowed(url, brand_key, brand_settings, operators=()):
    """(True, "") when the address is an allowed editorial page of the brand (B6); otherwise
    (False, reason). Allowed areas such as /blog/ cover the area's home and one level below it
    (articles and categories)."""
    b = brands.brand(brand_key)
    parts = urlsplit(str(url or ""))
    host = (parts.hostname or "").lower()
    if parts.scheme != "https":
        return False, "not an https address"
    if host not in (b["domain"], "www." + b["domain"]):
        return False, f"not on {b['domain']}"
    path = parts.path or "/"
    if not path.endswith("/"):
        path += "/"
    for bad in b["forbidden_paths"]:
        if path.startswith(bad):
            return False, f"operator, bonus or listing page ({bad})"
    areas = []
    for a in brand_settings.get("allowed_link_areas") or []:
        p = urlsplit(a).path if a.startswith("http") else a
        areas.append(p if p.endswith("/") else p + "/")
    if not any(path == a or re.fullmatch(re.escape(a) + r"[a-z0-9-]+/", path) for a in areas):
        return False, "outside the allowed link areas (" + ", ".join(areas or ["none set"]) + ")"
    op = operator_in(path, operators)
    if op:
        return False, f"the address names the operator {op}"
    if bonus_amount_in(path):
        return False, "the address shows a bonus amount"
    return True, ""


def has_web_address(text):
    """True when the text holds a web address (Instagram text never may, B6)."""
    return LINK in str(text or "") or bool(WEB_ADDRESS.search(str(text or "")))
