"""The visible text of a live page (tech spec flow 6, step 4; A2 source records).

<article>, else <main>, else <body>; scripts, styles, nav, header, footer and forms dropped;
non-breaking spaces made plain; whitespace collapsed. Used to confirm that a quoted line is on
a page word for word, and that every number a post quotes is still on the live page.
"""
import re
from html import unescape
from html.parser import HTMLParser

DROP = {"script", "style", "noscript", "template", "nav", "header", "footer", "form", "svg", "aside"}
BLOCK = {"p", "div", "li", "h1", "h2", "h3", "h4", "h5", "h6", "tr", "br", "section", "article",
         "main", "table", "ul", "ol", "blockquote", "figcaption", "td", "th"}


class _Text(HTMLParser):
    def __init__(self, want):
        super().__init__(convert_charrefs=True)
        self.want, self.depth_want, self.drop, self.parts = want, 0, 0, []

    def handle_starttag(self, tag, attrs):
        if tag in DROP:
            self.drop += 1
        if tag == self.want:
            self.depth_want += 1
        if tag in BLOCK and self.depth_want:
            self.parts.append("\n")

    def handle_startendtag(self, tag, attrs):
        if tag == "br" and self.depth_want:
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in DROP and self.drop:
            self.drop -= 1
        if tag in BLOCK and self.depth_want:
            self.parts.append("\n")
        if tag == self.want and self.depth_want:
            self.depth_want -= 1

    def handle_data(self, data):
        if self.depth_want and not self.drop:
            self.parts.append(data)


def visible_text(html):
    """The page's readable text, one block per line."""
    html = str(html or "")
    for want in ("article", "main", "body"):
        if re.search(rf"<{want}[\s>]", html, re.I):
            p = _Text(want)
            p.feed(html)
            text = "".join(p.parts)
            if text.strip():
                break
    else:
        text = re.sub(r"<[^>]+>", " ", html)
    text = unescape(text).replace(" ", " ").replace(" ", " ")
    lines = [re.sub(r"[ \t\r\f\v]+", " ", ln).strip() for ln in text.split("\n")]
    return "\n".join(ln for ln in lines if ln)


def flat(text):
    """All whitespace collapsed to single spaces (for word-for-word matching across lines)."""
    return re.sub(r"\s+", " ", str(text or "").replace(" ", " ").replace(" ", " ")).strip()


def contains(page_text, line):
    return flat(line) in flat(page_text)
