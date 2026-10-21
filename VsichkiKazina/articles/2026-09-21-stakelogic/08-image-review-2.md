# 08 — Image review, pass 2 (Stakelogic, vk-0141)

Script: `python3 scripts/gemini_image_review.py 05b-final-draft.md images/stakelogic-super-stake.svg images/stakelogic-hero.webp`
Model: gemini-3.1-pro-preview · Exit: 0

Score: **65/100** · Verdict: **NEEDS WORK** — hero now flagged as an integrity concern (glamorised winning: upward-trending arrow + glowing treasure chest imply financial growth). Infographic PASS as-is. ALT now matches the image (pass-1 fix accepted).

## VERBATIM VERDICT

**Score: 65/100**
**Verdict:** `NEEDS WORK`

### The Problems

**1. Raster Image (`stakelogic-hero.webp`) — Responsible Gambling / Glamorised Winning (Automatic Fail)**
The hero illustration features an upward-trending arrow wrapping around casino chips and pointing to a glowing treasure chest. In a regulated gambling context, upward arrows are a major compliance red flag because they visually imply financial growth, investment returns, or guaranteed profit. Combined with a glowing treasure chest, this constitutes "glamorised winning." It directly contradicts the article's responsible gambling warning: *"гледай на слота като на платено забавление с известна цена, не като на начин да изкараш пари."*

**2. SVG Infographic (`stakelogic-super-stake.svg`) — Review**
The infographic is excellent. It perfectly matches the article's facts (×2 and ×2.5 multipliers), renders cleanly with no overlapping or clipped text, and prominently features the necessary responsible gambling caveats (budget drain, house edge remaining the same). SEO metadata and ALT text are also perfectly aligned.

### Actionable Fixes

- For the Raster Image (`stakelogic-hero.webp`): regenerate to remove the financial-growth metaphor — drop the upward-trending arrow and the glowing aura around the chest; use a neutral horizontal sequence (toggle + chips + horizontal arrow to a plain slot/book symbol) so it reads "extra bet = bonus feature", not "wealth generation".
- For the SVG Infographic: No changes needed. Ready to publish as-is.

## DECISION
Integrity concern on the hero (glamorised winning) = never ship as-is. Regenerating the hero once (fix pass) with a neutral horizontal metaphor (no upward arrow, no glowing chest). If it clears, keep both; if it still reads as glamorised winning, DROP the hero and ship the infographic alone (already ≥1 image, PASS). The infographic is the primary, accurate illustration either way.
