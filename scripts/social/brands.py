"""Per-brand constants that are code, not settings (settings live in <Brand>/social/settings.md).

Paths are relative to the repository root.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

BRANDS = {
    "vsichkikazina": {
        "dir": "VsichkiKazina",
        "name": "Всички Казина",
        "prefix": "vk",                      # queue ids vk-0300, request ids vk-req-012
        "domain": "vsichkikazina.bg",
        "site": "https://vsichkikazina.bg",
        "queue_format": "vsichkikazina",     # build_dashboard.parse_queue brand
        # B6: never these, whatever the settings say (operator, bonus and listing pages)
        "forbidden_paths": ["/casino/", "/bonusi/", "/bonus-ruletka/", "/bonus-category/",
                            "/sravni-kazina/", "/novi-kazina/", "/kazino-nisak-depozit/", "/go/"],
        "palette": {"green": "#0F7B5A", "gold": "#C9962C", "ink": "#14161A", "paper": "#F7F4EC"},
        "fonts": {"title": "Onest", "body": "Onest", "serif": "Literata"},
        "mark_18": True,
        # the publisher's record in WebPortals (read only): the live path of each slug (F2)
        "publisher_record": "VsichkiKazina/_publisher/.published-state.json",
    },
    "dentalvia": {
        "dir": "DentalVia",
        "name": "DentalVia",
        "prefix": "dv",
        "domain": "dentalvia.de",
        "site": "https://www.dentalvia.de",
        "queue_format": "dentalvia",
        "forbidden_paths": [],
        "palette": {"green": "#1B6F8C", "gold": "#E3B04B", "ink": "#16242C", "paper": "#F5F8FA"},
        "fonts": {"title": "Noto Sans", "body": "Noto Sans", "serif": "Noto Sans"},
        "mark_18": False,
        "publisher_record": "DentalVia/_publisher/.published-state.json",   # settled with Open question 18
    },
}

# B2: what each network takes. `limit` is the hard limit, `aim` the range we write for.
NETWORKS = {
    "facebook": {"code": "fb", "limit": 63206, "aim": (300, 700), "hashtags": (0, 3),
                 "carousel": True, "max_slides": 10, "utm": "facebook"},
    "instagram": {"code": "ig", "limit": 2200, "aim": (600, 1500), "hashtags": (3, 5),
                  "carousel": True, "max_slides": 10, "utm": "instagram"},
    "x": {"code": "x", "limit": 280, "aim": (0, 280), "hashtags": (1, 2),
          "carousel": False, "max_slides": 1, "utm": "x"},
    "linkedin-page": {"code": "li", "limit": 3000, "aim": (600, 1300), "hashtags": (3, 5),
                      "carousel": True, "max_slides": 10, "utm": "linkedin"},
    "linkedin-profile": {"code": "li", "limit": 3000, "aim": (600, 1300), "hashtags": (3, 5),
                         "carousel": False, "max_slides": 1, "utm": "linkedin"},
}

# C1: pixel sizes. Single image and carousel slides per network.
SIZES = {
    "facebook": {"single": (1080, 1350), "square": (1080, 1080), "slide": (1080, 1080)},
    "instagram": {"single": (1080, 1350), "square": (1080, 1080), "slide": (1080, 1350)},
    "x": {"single": (1600, 900), "square": (1600, 900), "slide": (1600, 900)},
    "linkedin-page": {"single": (1080, 1080), "square": (1080, 1080), "slide": (1080, 1350)},
    "linkedin-profile": {"single": (1080, 1080), "square": (1080, 1080), "slide": (1080, 1080)},
}

ASPECTS = {(1080, 1350): "4:5", (1080, 1080): "1:1", (1600, 900): "16:9"}


def brand(key):
    if key not in BRANDS:
        raise KeyError(f"unknown brand {key!r}; one of: {', '.join(BRANDS)}")
    return BRANDS[key]


def social_dir(key, root=ROOT):
    return Path(root) / BRANDS[key]["dir"] / "social"


def brand_of_prefix(prefix):
    for key, b in BRANDS.items():
        if b["prefix"] == prefix:
            return key
    return None
