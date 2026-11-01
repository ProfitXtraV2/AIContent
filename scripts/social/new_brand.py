#!/usr/bin/env python3
"""A new brand for social posts, from its topic (the dashboard's "New brand", through intake.py).

    python3 scripts/social/new_brand.py --name "Футбол 24" --site https://futbol24.bg --topic sport [--language bg]

Writes the brand's entry in social/brands.json and its folder <Dir>/social/: settings.md (the
topic's rules and first values, every account switched off), the board files (packs.md,
requests.md, image-spend.json), the writing and picture prompts and the house style, all from
social/templates/ and social/topics/<topic>.json. Nothing goes out until someone switches the
brand on in the dashboard's Settings tab and its accounts are linked. Prints the files written.
"""
import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from social import brands  # noqa: E402

LANGUAGES = {"bg": "Bulgarian", "en": "English", "de": "German", "ro": "Romanian", "el": "Greek",
             "es": "Spanish", "it": "Italian", "fr": "French", "pl": "Polish", "pt": "Portuguese"}
NETWORK_ROWS = [("fb", "facebook", "carousel", "5", "3", "in post", "light"),
                ("ig", "instagram", "carousel", "5", "5", "profile", "light"),
                ("x", "x", "single", "", "2", "in post", "light"),
                ("li", "linkedin-page", "auto", "5", "5", "in post", "none")]
FONTS = {"title": "Onest", "body": "Onest", "serif": "Literata"}      # bundled in scripts/social/fonts


def key_from(site):
    """futbol24 from https://www.futbol24.bg/…"""
    host = urlsplit(site).hostname or ""
    host = re.sub(r"^www\.", "", host.lower())
    return re.sub(r"[^a-z0-9]+", "", host.rsplit(".", 1)[0]) if "." in host else ""


def dir_for(key):
    return "".join(p.capitalize() for p in re.split(r"[^a-z0-9]+", key) if p) or key


def prefix_for(key, taken):
    """Two or three letters of the key that no other brand uses (vk, dv, …)."""
    letters = [c for c in key if c.isalpha()] or list("xx")
    tries = [letters[0] + c for c in letters[1:]] + [letters[0] + a + b for a in letters[1:] for b in letters[1:]]
    for p in tries:
        if p not in taken:
            return p
    raise ValueError("no free ID prefix for this brand")


def _cell(v):
    return str(v or "").replace("|", "/").replace("\n", " ").strip()


def settings_text(name, site, key, language, preset):
    values = (preset.get("settings") or {}).get(language) or (preset.get("settings") or {}).get("en") or {}
    keep_lines = language in (preset.get("settings") or {})          # another language writes its own lines
    rows = [("social", "off"), ("pause", "off"), ("publisher", ""), ("time_zone", "Europe/Sofia"), ("language", language),
            ("voice_notes", values.get("voice_notes", "")),
            ("compliance_long", values.get("compliance_long", "") if keep_lines else ""),
            ("compliance_short", values.get("compliance_short", "") if keep_lines else ""),
            ("eligible_types", values.get("eligible_types", "guide, comparison, review, news")),
            ("allowed_link_areas", "/"), ("operator_names_manual", ""), ("address_pattern", f"{site.rstrip('/')}/{{slug}}/"),
            ("brand_hashtags", ""), ("image_budget_usd", "30"), ("art", "cover"), ("packs_per_run", "3"),
            ("analytics_source", ""), ("identities_verified", ""),
            ("offer_words", values.get("offer_words", "") if keep_lines else ""),
            ("register_words", values.get("register_words", "") if keep_lines else ""),
            ("allowed_number_names", "")]
    head = (f"# Social settings — {name}\n\n"
            f"Brand and account settings for social posts of {name} ({site}). Read by the drafting run, the PR\n"
            "checks and the publishing check (`scripts/social/settings.py`).\n\n"
            "**Change them in the dashboard's Settings tab** (or with a PR). A change counts once someone with\n"
            "write access to this repository merges its PR; the person who made it may merge it. No passwords\n"
            "or keys ever go in this file.\n\n"
            "- `publisher`: the GitHub login of the person whose computer publishes this brand (its Postiz\n"
            "  and its publishing check). Only that computer hands posts over, so nothing goes out twice.\n"
            "- An account is linked to its Postiz channel by the local setup (`scripts/social/local/setup.py`).\n\n"
            "## Brand\n\n| key | value |\n|---|---|\n")
    acc_head = ("\n## Accounts\n\n| account_id | network | postiz_channel_id | active | posts_per_article | followup_delay_days "
                "| format | slides | max_hashtags | link | slots | max_per_day | emoji | tone_override | test_post_seen "
                "| profile_link_set |\n|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|\n")
    accounts = "".join(f"| {code}-{key} | {net} |  | off | 1 | 14 | {fmt} | {slides} | {tags} | {link} | daily 12:30, 19:30 "
                       f"| 2 | {emoji} |  |  |  |\n" for code, net, fmt, slides, tags, link, emoji in NETWORK_ROWS)
    return head + "".join(f"| {k} | {_cell(v)} |\n" for k, v in rows) + acc_head + accounts


def board_file(template, name):
    """The board file of an existing brand, emptied: its text and table headers, no rows."""
    out, in_table, seen_rule = [], False, False
    for line in template.splitlines():
        if line.startswith("# "):
            line = re.sub(r"—.*$", f"— {name}", line)
        if line.startswith("|"):
            if in_table and seen_rule:
                continue                                  # a row: dropped
            in_table = True
            seen_rule = seen_rule or bool(re.fullmatch(r"\|[-| ]+\|", line.strip()))
        else:
            in_table, seen_rule = False, False
        out.append(line)
    return "\n".join(out).rstrip() + "\n"


def fill(template, values):
    return re.sub(r"\{\{(\w+)\}\}", lambda m: str(values.get(m.group(1), m.group(0))), template)


def create(root, name, site, topic, language="bg", key=None, registry=None):
    """Write the new brand. Returns (key, [paths written, relative to root]). Raises ValueError."""
    root = Path(root)
    registry = Path(registry or root / "social" / "brands.json")
    name, site, language = str(name or "").strip(), str(site or "").strip().rstrip("/"), str(language or "bg").strip().lower()
    if not name:
        raise ValueError("the brand needs a name")
    if not re.fullmatch(r"https://[a-z0-9.-]+\.[a-z]{2,}", site.lower()):
        raise ValueError(f"the site must be an address like https://example.bg, not {site!r}")
    presets = brands.topics(root / "social" / "topics")
    if topic not in presets:
        raise ValueError(f"unknown topic {topic!r} (one of: {', '.join(presets)})")
    if not re.fullmatch(r"[a-z]{2}", language):
        raise ValueError(f"language must be a two-letter code such as bg or en, not {language!r}")
    data = json.loads(registry.read_text(encoding="utf-8"))
    known = data["brands"]
    key = key or key_from(site)
    if not re.fullmatch(r"[a-z0-9]{3,30}", key or ""):
        raise ValueError(f"cannot make a brand key from {site!r}")
    domain = re.sub(r"^www\.", "", urlsplit(site).hostname or "")
    if key in known or any(b.get("domain") == domain for b in known.values()):
        raise ValueError(f"the brand {key} ({domain}) is already there")
    folder = dir_for(key)
    if (root / folder).exists():
        raise ValueError(f"the folder {folder}/ already exists")
    preset = presets[topic]
    prefix = prefix_for(key, {b["prefix"] for b in known.values()})
    palette = dict(preset.get("palette") or {"green": "#2F6F5E", "gold": "#D9A441", "ink": "#15181C", "paper": "#F6F5F1"})
    known[key] = {"dir": folder, "name": name, "prefix": prefix, "domain": domain, "site": site, "topic": topic,
                  "language": language, "forbidden_paths": [], "palette": palette, "fonts": dict(FONTS),
                  "mark_18": bool(preset.get("mark_18"))}
    values = (preset.get("settings") or {}).get(language) or {}
    rules = preset.get("writing_rules") or []
    mark = bool(preset.get("mark_18"))
    long_line, short_line = values.get("compliance_long", ""), values.get("compliance_short", "")
    fills = dict(palette, brand_name=name, brand_key=key, prefix=prefix, site=site, domain=domain,
                 language_name=LANGUAGES.get(language, language),
                 topic_about=(preset.get("about") or "site.").rstrip(".") + ".",
                 writing_rules="\n".join(f"  - {r}" for r in rules) or "  - None beyond the ones above.",
                 compliance_rule=(f"word for word at the end of every post: „{long_line}“."
                                  + (f" On X the short form „{short_line}“ is enough." if short_line else "")
                                  if long_line else "the one in `settings.md` (`compliance_long`), word for word at the "
                                  "end of every post; none when the brand has no such line."),
                 compliance_example=(f"\\n\\n{long_line}" if long_line else ""),
                 art_rules=preset.get("art_rules", ""), review_rules=preset.get("review_rules", ""),
                 mark_18_layout=" and 18+" if mark else "", mark_18_allowed=" and the mark 18+" if mark else "",
                 mark_18_frame=", and the mark 18+" if mark else "")
    social = root / folder / "social"
    templates = root / "social" / "templates"
    model = brands.social_dir("vsichkikazina", root)
    files = {
        social / "settings.md": settings_text(name, site, key, language, preset),
        social / "packs.md": board_file((model / "packs.md").read_text(encoding="utf-8"), name),
        social / "requests.md": board_file((model / "requests.md").read_text(encoding="utf-8"), name),
        social / "image-spend.json": json.dumps({"budget_note": "Social image generation and review only, on the social "
                                                 "Gemini key. Counted by UTC month.", "months": {}}, indent=2) + "\n",
        social / "prompts" / "post-writing.md": fill((templates / "post-writing.md").read_text(encoding="utf-8"), fills),
        social / "prompts" / "visual-art.md": fill((templates / "visual-art.md").read_text(encoding="utf-8"), fills),
        social / "prompts" / "visual-review.md": fill((templates / "visual-review.md").read_text(encoding="utf-8"), fills),
        social / "style" / "style.md": fill((templates / "style.md").read_text(encoding="utf-8"), fills),
    }
    for path, text in files.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8", newline="\n")
    registry.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    written = [registry] + list(files)
    return key, [str(p.relative_to(root)).replace("\\", "/") for p in written]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--name", required=True)
    ap.add_argument("--site", required=True)
    ap.add_argument("--topic", required=True)
    ap.add_argument("--language", default="bg")
    ap.add_argument("--key")
    a = ap.parse_args(argv)
    try:
        key, written = create(brands.ROOT, a.name, a.site, a.topic, a.language, a.key)
    except ValueError as e:
        print(f"not created: {e}", file=sys.stderr)
        return 1
    print(f"brand {key}:\n" + "\n".join(f"  {p}" for p in written))
    return 0


if __name__ == "__main__":
    sys.exit(main())
