"""Numbers in posts, and how long a post is per network (product spec B2, B4).

B4: every number in a post or on its images appears exactly as in its source, formatting
included. The exceptions are: „18+“; slide counters such as „3/6“; numbers that are part of a
name the source uses (and hashtags made from such a name); the link and its tags.
"""
import re
import unicodedata

from social import links

NBSP = {" ": " ", " ": " ", " ": " ", " ": " "}
# A number core: digits, optionally grouped or with decimals (1 000 · 1,06 · 1.000,50 · 96.5)
_CORE = r"\d+(?:[   .,]\d+)*"
# Attached marks that are part of how a number is written: €100, x30, х40, ~1,06%, 8:1, 3/6
NUMBER_RE = re.compile(
    r"(?<![\w])"                                   # not inside a word
    r"(?P<tok>"
    r"[~≈±]?"                                      # about
    r"(?:[€$£]|[xх×](?=\d))?"                      # currency or multiplier in front
    + _CORE +
    r"(?:[:/]\d+)?"                                # ratios 8:1 and counters 3/6
    r"(?:%|€|\$|£|[xх×](?![\w])|\+)?"              # percent, currency, multiplier or plus after
    r")",
)
URL_RE = re.compile(r"https?://\S+|www\.\S+")


def normalize(text):
    """Non-breaking and thin spaces become plain spaces; nothing else changes."""
    t = str(text or "")
    for k, v in NBSP.items():
        t = t.replace(k, v)
    return t


def tokens(text):
    """The numbers written in a text, as written (normalized spaces), in order. The link
    placeholder and web addresses are skipped (B4: the link and its tags)."""
    t = normalize(text).replace(links.LINK, " ")
    t = URL_RE.sub(" ", t)
    out = []
    for m in NUMBER_RE.finditer(t):
        tok = m.group("tok").strip()
        if any(ch.isdigit() for ch in tok):
            out.append(tok)
    return out


def _core(tok):
    m = re.search(_CORE, tok)
    return m.group(0) if m else tok


def occurs(token, text):
    """True when `token` is written in `text` as a whole number (10 is not found inside 100 or
    1 000; 1,06% is found in ~1,06%)."""
    t = normalize(text)
    tok = normalize(token)
    start = 0
    while True:
        i = t.find(tok, start)
        if i < 0:
            return False
        before = t[i - 1] if i > 0 else ""
        before2 = t[i - 2] if i > 1 else ""
        after = t[i + len(tok)] if i + len(tok) < len(t) else ""
        after2 = t[i + len(tok) + 1] if i + len(tok) + 1 < len(t) else ""
        cont_before = before.isdigit() or (before in " .," and before2.isdigit() and tok[:1].isdigit())
        cont_after = after.isdigit() or (after in " .," and after2.isdigit() and tok[-1:].isdigit())
        if not cont_before and not cont_after:
            return True
        start = i + 1


def is_exception(tok, where="text"):
    """B4 exceptions. where: text | image (slide counters count only on images)."""
    if re.fullmatch(r"18\+", tok):
        return True
    if where == "image" and re.fullmatch(r"\d{1,2}/\d{1,2}", tok):
        return True
    return False


def without_names(text, names):
    """The text with every named game or product written in it taken out, so the number that
    is part of a name („20 Super Hot“) is no fact to check (B4). A name counts only where it is
    written; „100%“ is still a number even when „100 Super Hot“ is a known name."""
    t = normalize(text)
    for name in sorted(names, key=len, reverse=True):
        t = re.sub(r"(?<![\w])" + re.escape(normalize(name)) + r"(?![\w])", " ", t, flags=re.IGNORECASE)
    return t


def hashtag_ok(tag, names, source_text):
    """A hashtag with digits passes when it is a name the source uses, spaces removed
    (#GatesOfOlympus1000 for „Gates of Olympus 1000“)."""
    body = tag.lstrip("#").lower()
    if not any(ch.isdigit() for ch in body):
        return True
    squash = lambda s: re.sub(r"[\s\-_]+", "", normalize(s).lower())  # noqa: E731
    if any(squash(n) == body for n in names):
        return True
    return body in squash(source_text)


def unmatched(text, source_lines, where="text", names=()):
    """The numbers of `text` that no source line backs, B4 exceptions apart."""
    missing = []
    for tok in tokens(without_names(text, names)):
        if is_exception(tok, where):
            continue
        if any(occurs(tok, line) for line in source_lines):
            continue
        missing.append(tok)
    return missing


# --- length (B2) --------------------------------------------------------------------------

def _weight(cp):
    """twitter-text v3: these ranges weigh 1, everything else 2."""
    return 1 if (cp <= 0x10FF or 0x2000 <= cp <= 0x200D or 0x2010 <= cp <= 0x201F
                 or 0x2032 <= cp <= 0x2037) else 2


def _is_emoji_base(cp):
    return (0x1F000 <= cp <= 0x1FAFF or 0x2600 <= cp <= 0x27BF or 0x2B00 <= cp <= 0x2BFF
            or 0x1F1E6 <= cp <= 0x1F1FF)


def x_length(text, link_length=23):
    """X's weighted length: Latin and Cyrillic count 1, most other characters 2, each emoji 2,
    each link 23 (the placeholder counts as a link)."""
    t = unicodedata.normalize("NFC", str(text or ""))
    n = 0
    for _ in re.finditer(re.escape(links.LINK) + r"|https?://\S+", t):
        n += link_length
    t = re.sub(re.escape(links.LINK) + r"|https?://\S+", "", t)
    cps = [ord(c) for c in t]
    i = 0
    while i < len(cps):
        cp = cps[i]
        if _is_emoji_base(cp):
            n += 2
            i += 1
            while i < len(cps) and (cps[i] in (0xFE0F, 0xFE0E) or 0x1F3FB <= cps[i] <= 0x1F3FF
                                    or (0x1F1E6 <= cp <= 0x1F1FF and 0x1F1E6 <= cps[i] <= 0x1F1FF)):
                i += 1
            while i + 1 < len(cps) and cps[i] == 0x200D and _is_emoji_base(cps[i + 1]):
                i += 2
                while i < len(cps) and (cps[i] in (0xFE0F, 0xFE0E) or 0x1F3FB <= cps[i] <= 0x1F3FF):
                    i += 1
            continue
        if cp in (0xFE0F, 0xFE0E):
            i += 1
            continue
        n += _weight(cp)
        i += 1
    return n


def length(text, network, link_length=None):
    """Characters as the network counts them. On Facebook, Instagram and LinkedIn: code points,
    with the placeholder counted as the tagged link it becomes (link_length, default 120)."""
    if network == "x":
        return x_length(text)
    t = str(text or "")
    count = len(t.replace(links.LINK, ""))
    return count + (t.count(links.LINK) * (link_length if link_length is not None else 120))


def emoji_count(text):
    return sum(1 for c in str(text or "") if _is_emoji_base(ord(c)))
