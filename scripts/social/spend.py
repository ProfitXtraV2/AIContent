"""The monthly budget for social image work (product spec C7; tech spec flow 11, step 1).

<Brand>/social/image-spend.json counts, per UTC month and brand, what generation and review
cost on the social Gemini key. A call may start only if the spend so far plus its estimate stays
within the brand's monthly budget. A payment or credit error marks "social image credits
exhausted" for the month, and packs then use fallback visuals.
"""
import json
from datetime import datetime, timezone
from pathlib import Path

PRICES = Path(__file__).resolve().parent / "prices.json"
CREDIT_SIGNS = ("prepayment credits are depleted", "resource_exhausted", "billing", "quota exceeded")


def prices():
    return json.loads(PRICES.read_text(encoding="utf-8"))


def month(now=None):
    return (now or datetime.now(timezone.utc)).strftime("%Y-%m")


class Spend:
    def __init__(self, path, brand_key, budget_usd, now=None):
        self.path, self.brand, self.budget = Path(path), brand_key, float(budget_usd)
        self.month = month(now)
        try:
            self.data = json.loads(self.path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            self.data = {"months": {}}
        self.data.setdefault("months", {})

    @property
    def entry(self):
        m = self.data["months"].setdefault(self.month, {})
        return m.setdefault(self.brand, {"usd": 0.0, "images": 0, "reviews": 0, "credits_exhausted": False})

    @property
    def spent(self):
        return round(self.entry["usd"], 4)

    def can_spend(self, estimate_usd):
        """(ok, reason): reason is 'budget reached' or 'credits exhausted' when not ok."""
        if self.entry.get("credits_exhausted"):
            return False, "credits exhausted"
        if self.entry["usd"] + estimate_usd > self.budget:
            return False, "budget reached"
        return True, ""

    def add_image(self, usd=None):
        self.entry["usd"] += prices()["image_generation_usd"] if usd is None else usd
        self.entry["images"] += 1

    def add_review(self, usage=None):
        """Price a review from its usageMetadata (token counts), else the estimate."""
        p = prices()["review"]
        meta = (usage or {}).get("usageMetadata") or {}
        if meta:
            usd = (meta.get("promptTokenCount", 0) * p["input_usd_per_million_tokens"]
                   + (meta.get("candidatesTokenCount", 0) + meta.get("thoughtsTokenCount", 0))
                   * p["output_usd_per_million_tokens"]) / 1e6
        else:
            usd = p["estimate_usd"]
        self.entry["usd"] += usd
        self.entry["reviews"] += 1
        return usd

    def note_error(self, text):
        """Mark the credits exhausted when an error says the account cannot pay. True if so."""
        low = str(text or "").lower()
        if ("402" in low or "429" in low or "resource_exhausted" in low) and any(s in low for s in CREDIT_SIGNS):
            self.entry["credits_exhausted"] = True
            return True
        return False

    def save(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(self.data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def estimate_attempt(images=1):
    """The generated artworks of one attempt (a cover, and a carousel's point pictures) plus its review."""
    p = prices()
    return p["image_generation_usd"] * images + p["review"]["estimate_usd"]
