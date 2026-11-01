"""The brands of social posts and what does not change per post.

The brands are data: social/brands.json (one entry per brand: its folder, name, ID prefix, site,
topic, language, layout palette and fonts). A brand is added from the dashboard ("New brand"),
which opens a PR (new_brand.py). Each topic (social/topics/<topic>.json: casino, betting, sport,
dental, general) gives a new brand its rules and the first values of its settings. Settings
live in <Brand>/social/settings.md. Paths are relative to the repository root.

    python3 scripts/social/brands.py list                 # the brand keys, one per line
    python3 scripts/social/brands.py dashboard <file>     # the brand list the dashboard reads
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "social" / "brands.json"
TOPICS = ROOT / "social" / "topics"


def load_registry(path=REGISTRY):
    return json.loads(Path(path).read_text(encoding="utf-8"))["brands"]


BRANDS = load_registry()


def topics(folder=TOPICS):
    """{topic key: preset} from social/topics/*.json."""
    got = {f.stem: json.loads(f.read_text(encoding="utf-8")) for f in Path(folder).glob("*.json")}
    return dict(sorted(got.items(), key=lambda kv: (kv[1].get("order", 50), kv[0])))


def topic(key):
    """The preset of a brand's topic ({} when it has none)."""
    name = BRANDS.get(key, {}).get("topic", "")
    f = TOPICS / f"{name}.json"
    return json.loads(f.read_text(encoding="utf-8")) if name and f.exists() else {}


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


def dashboard_list(root=ROOT):
    """What the dashboard shows of each brand, and the topics a new brand can take."""
    root = Path(root)
    return {"brands": [{"key": k, "name": b["name"], "prefix": b["prefix"], "site": b["site"], "dir": b["dir"],
                        "topic": b.get("topic", ""), "language": b.get("language", ""),
                        "social": (root / b["dir"] / "social" / "settings.md").exists()}
                       for k, b in BRANDS.items()],
            "topics": [{"key": k, "label": t.get("label", {}), "about": t.get("about", "")} for k, t in topics().items()]}


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if argv[:1] == ["list"]:
        print("\n".join(k for k in BRANDS if (ROOT / BRANDS[k]["dir"] / "social" / "settings.md").exists()))
        return 0
    if argv[:1] == ["dashboard"] and len(argv) == 2:
        Path(argv[1]).parent.mkdir(parents=True, exist_ok=True)
        Path(argv[1]).write_text(json.dumps(dashboard_list(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main())
