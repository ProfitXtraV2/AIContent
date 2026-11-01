"""Brand and account settings for social (product spec D1–D4), from <Brand>/social/settings.md.

The file holds two tables, parsed by header name:
  Brand    | key | value |            one row per D1 setting (plus the B5 word lists)
  Accounts | account_id | network | … | one row per account (D2)

`load()` returns the typed settings with the validation errors of D4. A brand error stops
the whole brand; an account error skips only that account, with a plain message for the
dashboard. Nothing here holds a key or a password.

    python3 scripts/social/settings.py [brand]      # prints the settings and any errors
"""
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from social import brands, mdtable  # noqa: E402

DAYS = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
ON_OFF = {"on": True, "off": False, "yes": True, "no": False, "true": True, "false": False}
NETWORK_MAX_HASHTAGS = {k: v["hashtags"][1] for k, v in brands.NETWORKS.items()}

BRAND_DEFAULTS = {
    "social": "off", "pause": "off", "time_zone": "Europe/Sofia",
    "language": "bg", "voice_notes": "", "compliance_long": "", "compliance_short": "",
    "eligible_types": "guide, comparison, review, news", "allowed_link_areas": "/blog/",
    "operator_names_manual": "", "address_pattern": "", "brand_hashtags": "",
    "image_budget_usd": "60", "packs_per_run": "5", "analytics_source": "ahrefs",
    "identities_verified": "", "offer_words": "", "register_words": "",
    "allowed_number_names": "", "art": "every slide",
}
ACCOUNT_DEFAULTS = {
    "postiz_channel_id": "", "active": "off", "posts_per_article": "1",
    "followup_delay_days": "14", "format": "auto", "slides": "5", "max_hashtags": "", "link": "in post",
    "slots": "daily 12:30, 19:30", "max_per_day": "2", "emoji": "light", "tone_override": "",
    "test_post_seen": "", "profile_link_set": "",
}


@dataclass
class Settings:
    brand_key: str
    brand: dict
    accounts: list
    errors: list = field(default_factory=list)   # [{"scope": "brand" | account_id, "message": str}]

    @property
    def brand_ok(self):
        return not any(e["scope"] == "brand" for e in self.errors)

    @property
    def social_on(self):
        return self.brand_ok and self.brand["social"]

    def account_errors(self, account_id):
        return [e["message"] for e in self.errors if e["scope"] == account_id]

    def account(self, account_id):
        return next((a for a in self.accounts if a["account_id"] == account_id), None)

    def usable_accounts(self):
        """Active accounts with no error, of a brand with no error (the ones that get posts)."""
        if not self.brand_ok:
            return []
        return [a for a in self.accounts if a["active"] and not self.account_errors(a["account_id"])]

    def to_json(self):
        return {"brand_key": self.brand_key, "brand": self.brand, "accounts": self.accounts,
                "errors": self.errors}


def parse_slots(text):
    """'daily 12:30, 19:30; sat 11:00' → [{"days": [0..6], "times": ["12:30", "19:30"]}, ...].
    Raises ValueError with a plain message on anything it cannot read."""
    rules = []
    for part in [p.strip() for p in str(text or "").split(";") if p.strip()]:
        m = re.match(r"^([a-z,\- ]+?)\s+(\d.*)$", part.lower())
        if not m:
            raise ValueError(f"cannot read the slot rule {part!r} (write e.g. 'daily 12:30, 19:30')")
        days = _days(m.group(1).replace(" ", ""))
        times = []
        for t in [t.strip() for t in m.group(2).split(",") if t.strip()]:
            tm = re.fullmatch(r"(\d{1,2}):(\d{2})", t)
            if not tm or not (0 <= int(tm.group(1)) <= 23 and 0 <= int(tm.group(2)) <= 59):
                raise ValueError(f"slot {t!r} is outside 00:00–23:59")
            times.append(f"{int(tm.group(1)):02d}:{tm.group(2)}")
        if not times:
            raise ValueError(f"the slot rule {part!r} has no time")
        rules.append({"days": days, "times": sorted(set(times))})
    if not rules:
        raise ValueError("no posting slots")
    return rules


def _days(spec):
    if spec in ("daily", "everyday", "every-day"):
        return list(range(7))
    out = set()
    for piece in spec.split(","):
        if "-" in piece:
            a, b = piece.split("-", 1)
            if a not in DAYS or b not in DAYS:
                raise ValueError(f"unknown days {piece!r} (use mon … sun, or daily)")
            i, j = DAYS.index(a), DAYS.index(b)
            out.update(range(i, j + 1) if i <= j else list(range(i, 7)) + list(range(0, j + 1)))
        elif piece in DAYS:
            out.add(DAYS.index(piece))
        else:
            raise ValueError(f"unknown day {piece!r} (use mon … sun, or daily)")
    return sorted(out)


def _flag(value, default=False):
    return ON_OFF.get(str(value or "").strip().lower(), default)


def _int(value, default):
    try:
        return int(str(value).strip())
    except (TypeError, ValueError):
        return default


def _hashtags(value):
    return [h if h.startswith("#") else "#" + h for h in re.split(r"[\s,]+", str(value or "")) if h]


def parse(md_text, brand_key="vsichkikazina"):
    """Settings from the text of settings.md, validated (D4)."""
    b = brands.brand(brand_key)
    raw = dict(BRAND_DEFAULTS)
    errors = []
    bt = mdtable.find(md_text, "key", "value")
    if bt is None:
        errors.append({"scope": "brand", "message": "settings.md has no Brand table (| key | value |)"})
    else:
        for row in bt["rows"]:
            key = row.get("key", "").strip().lower()
            if key:
                raw[key] = row.get("value", "").strip()
    brand = {
        "social": _flag(raw["social"]), "pause": _flag(raw["pause"]), "time_zone": raw["time_zone"].strip() or "Europe/Sofia",
        "language": raw["language"].strip(), "voice_notes": raw["voice_notes"],
        "compliance_long": raw["compliance_long"].strip(),
        "compliance_short": raw["compliance_short"].strip() or raw["compliance_long"].strip(),
        "eligible_types": [t.lower() for t in mdtable.split_list(raw["eligible_types"])],
        "allowed_link_areas": mdtable.split_list(raw["allowed_link_areas"]),
        "operator_names_manual": mdtable.split_list(raw["operator_names_manual"]),
        "address_pattern": raw["address_pattern"].strip() or f"{b['site']}/blog/{{slug}}/",
        "brand_hashtags": _hashtags(raw["brand_hashtags"]),
        "image_budget_usd": raw["image_budget_usd"], "packs_per_run": _int(raw["packs_per_run"], 5),
        "analytics_source": raw["analytics_source"].strip(),
        "identities_verified": raw["identities_verified"].strip(),
        "offer_words": [w.lower() for w in mdtable.split_list(raw["offer_words"])],
        "register_words": [w.lower() for w in mdtable.split_list(raw["register_words"])],
        "allowed_number_names": mdtable.split_list(raw["allowed_number_names"]),
        "art": raw["art"].strip().lower() or "every slide",
    }
    try:
        brand["image_budget_usd"] = float(str(raw["image_budget_usd"]).strip() or 60)
    except ValueError:
        errors.append({"scope": "brand", "message": "image_budget_usd must be a number of dollars"})
        brand["image_budget_usd"] = 0.0
    errors += _brand_errors(brand, raw, b)

    accounts = []
    at = mdtable.find(md_text, "account_id", "network")
    seen = set()
    for row in (at["rows"] if at else []):
        r = dict(ACCOUNT_DEFAULTS)
        r.update({k: v for k, v in row.items() if v != ""})
        aid = r.get("account_id", "").strip()
        if not aid:
            continue
        acc, errs = _account(r, brand)
        if aid in seen:
            errs.append(f"account {aid} is listed twice")
        seen.add(aid)
        accounts.append(acc)
        errors += [{"scope": aid, "message": f"{aid}: {m}"} for m in errs]
    return Settings(brand_key, brand, accounts, errors)


def _brand_errors(brand, raw, b):
    errs = []

    def err(m):
        errs.append({"scope": "brand", "message": m})

    if raw["social"].strip().lower() not in ON_OFF:
        err("social must be on or off")
    if brand["social"] and not brand["identities_verified"]:
        err("social can be switched on only after the identities are verified (identities_verified, I6)")
    if not brand["compliance_long"]:
        err("compliance_long (the brand's compliance line) is empty")
    if "hub-intro" in brand["eligible_types"]:
        err("hub-intro can never be an eligible article type (section intros get posts only on request)")
    if not brand["eligible_types"]:
        err("eligible_types is empty")
    try:
        import zoneinfo
        zoneinfo.ZoneInfo(brand["time_zone"])
    except Exception:  # noqa: BLE001
        err(f"unknown time zone {brand['time_zone']!r}")
    for area in brand["allowed_link_areas"]:
        if not _on_brand_domain(area, b):
            err(f"link area {area!r} is outside the brand's own domain ({b['domain']})")
    pat = brand["address_pattern"]
    if "{slug}" not in pat or not _on_brand_domain(pat.replace("{slug}", "x"), b):
        err(f"address_pattern {pat!r} must be on {b['domain']} and contain {{slug}}")
    if not 1 <= brand["packs_per_run"] <= 20:
        err("packs_per_run must be between 1 and 20")
    if brand["image_budget_usd"] < 0:
        err("image_budget_usd cannot be negative")
    if brand["art"] not in ("every slide", "cover"):
        err("art must be every slide or cover")
    for h in brand["brand_hashtags"]:
        if not re.fullmatch(r"#\w+", h):
            err(f"brand hashtag {h!r} is not a single #word")
    return errs


def _on_brand_domain(area, b):
    if area.startswith("/"):
        return True
    m = re.match(r"^https://(?:www\.)?([^/]+)(/.*)?$", area)
    return bool(m) and m.group(1).lower() == b["domain"]


def _account(r, brand):
    errs = []
    net = r.get("network", "").strip().lower()
    acc = {
        "account_id": r["account_id"].strip(), "network": net,
        "postiz_channel_id": r["postiz_channel_id"].strip(),
        "active": _flag(r["active"]), "posts_per_article": _int(r["posts_per_article"], 0),
        "followup_delay_days": _int(r["followup_delay_days"], 0),
        "format": r["format"].strip().lower(), "slides": _int(r["slides"], 0), "link": r["link"].strip().lower(),
        "slots_text": r["slots"].strip(), "slots": [], "max_per_day": _int(r["max_per_day"], 0),
        "emoji": r["emoji"].strip().lower(), "tone_override": r["tone_override"].strip(),
        "test_post_seen": r["test_post_seen"].strip(),
        "profile_link_set": r["profile_link_set"].strip(),
    }
    if net not in brands.NETWORKS:
        errs.append(f"unknown network {net!r} (one of {', '.join(brands.NETWORKS)})")
    net_max = NETWORK_MAX_HASHTAGS.get(net, 5)
    acc["max_hashtags"] = _int(r["max_hashtags"], net_max) if str(r["max_hashtags"]).strip() else net_max
    if not 1 <= acc["posts_per_article"] <= 5:
        errs.append("posts per article must be 1–5")
    if acc["followup_delay_days"] < 1:
        errs.append("follow-up delay must be at least 1 day")
    if acc["format"] not in ("single", "carousel", "auto"):
        errs.append("format must be single, carousel or auto")
    max_slides = brands.NETWORKS.get(net, {}).get("max_slides", 1)
    if max_slides > 1 and not 3 <= acc["slides"] <= max_slides:
        errs.append(f"slides must be 3–{max_slides} (a carousel: cover, points, closing)")
    if acc["link"] not in ("in post", "none", "profile"):
        errs.append("link must be 'in post', 'none' or 'profile'")
    if net == "instagram" and acc["link"] == "in post":
        errs.append("Instagram posts cannot carry a link: set link to profile (or none)")
    if acc["emoji"] not in ("none", "light"):
        errs.append("emoji must be none or light")
    if acc["max_per_day"] < 1:
        errs.append("max posts per day must be at least 1")
    total_tags = acc["max_hashtags"] + len(brand["brand_hashtags"])
    if acc["max_hashtags"] < 0 or total_tags > net_max:
        errs.append(f"hashtags: {acc['max_hashtags']} + {len(brand['brand_hashtags'])} brand "
                    f"hashtag(s) is above the {net} limit of {net_max}")
    try:
        acc["slots"] = parse_slots(acc["slots_text"])
    except ValueError as e:
        errs.append(str(e))
    if acc["active"]:
        if not acc["test_post_seen"]:
            errs.append("active, but no visible test post is recorded (test_post_seen, D3)")
        if not acc["postiz_channel_id"]:
            errs.append("active, but no publishing tool channel is set (postiz_channel_id)")
        if net == "instagram" and not acc["profile_link_set"]:
            errs.append("active, but the Instagram profile link is not recorded as set (profile_link_set, B6)")
    return acc, errs


ACCOUNT_COLS = ["account_id", "network", *ACCOUNT_DEFAULTS]


def update(md_text, brand_changes=None, account_changes=None):
    """The text of settings.md with brand values and account fields changed (the dashboard's
    Settings form, through intake.py; docs/social-md.js updateSettings). Rows keep their order; a
    key or a column the file lacks is added. Raises ValueError on a key, field or account that
    settings.md does not have."""
    out = md_text
    brand_changes, account_changes = brand_changes or {}, account_changes or {}
    for key in brand_changes:
        if key not in BRAND_DEFAULTS:
            raise ValueError(f"unknown setting {key!r}")
    bt = mdtable.find(out, "key", "value")
    if brand_changes:
        if bt is None:
            raise ValueError("settings.md has no Brand table")
        rows = [dict(r) for r in bt["rows"]]
        for key, value in brand_changes.items():
            row = next((r for r in rows if r.get("key", "").strip().lower() == key), None)
            if row:
                row["value"] = mdtable.clean(value)
            else:
                rows.append({"key": key, "value": mdtable.clean(value)})
        out = mdtable.replace(out, bt, rows)
    if account_changes:
        at = mdtable.find(out, "account_id", "network")
        ids = [r.get("account_id", "").strip() for r in (at["rows"] if at else [])]
        for aid, fields in account_changes.items():
            if aid not in ids:
                raise ValueError(f"unknown account {aid!r}")
            for key in fields:
                if key not in ACCOUNT_DEFAULTS:
                    raise ValueError(f"unknown account field {key!r}")
        keys = {k for fields in account_changes.values() for k in fields}
        table = mdtable.with_columns(at, [c for c in ACCOUNT_COLS if c in at["header"] or c in keys])
        rows = [dict(r, **{k: mdtable.clean(v) for k, v in account_changes.get(r.get("account_id", "").strip(), {}).items()})
                for r in at["rows"]]
        out = mdtable.replace(out, table, rows)
    return out


def check_channels(settings, known_channels):
    """Add an error for every active account whose channel the publishing tool does not know
    (D4 'an unknown account'). known_channels: set of channel ids from the tool."""
    for a in settings.accounts:
        if a["active"] and a["postiz_channel_id"] and a["postiz_channel_id"] not in known_channels:
            settings.errors.append({"scope": a["account_id"],
                                    "message": f"{a['account_id']}: the publishing tool has no channel "
                                               f"{a['postiz_channel_id']!r}"})
    return settings


def path(brand_key, root=brands.ROOT):
    return brands.social_dir(brand_key, root) / "settings.md"


def load(brand_key="vsichkikazina", root=brands.ROOT, text=None):
    if text is None:
        p = path(brand_key, root)
        text = p.read_text(encoding="utf-8") if p.exists() else ""
    return parse(text, brand_key)


def main():
    brand_key = sys.argv[1] if len(sys.argv) > 1 else "vsichkikazina"
    s = load(brand_key)
    print(json.dumps(s.to_json(), ensure_ascii=False, indent=2))
    return 1 if s.errors else 0


if __name__ == "__main__":
    sys.exit(main())
