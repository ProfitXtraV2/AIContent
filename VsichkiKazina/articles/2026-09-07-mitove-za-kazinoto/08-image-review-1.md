# Image Review Pass 1 — mitove-za-kazinoto

**Script:** `python3 scripts/gemini_image_review.py VsichkiKazina/articles/2026-09-07-mitove-za-kazinoto/05b-final-draft.md mitove-kazino-domashno-predimstvo-hero.webp martingale-progresiya-tavan.svg`

**Combined Score: hero 100/100 (PASS), SVG 65/100 (NEEDS WORK)**

### Hero (mitove-kazino-domashno-predimstvo-hero.webp): PASS (100/100)
Excellent balance-scale metaphor for the house edge. No issues.

### SVG (martingale-progresiya-tavan.svg): NEEDS WORK (65/100)

**Problems:**
1. **Fabricated data in result box:** Added `€1+€2+...+€512 = €1023` total — not in the article text. Article only says "оставаш с реализирана загуба". Must remove.
2. **aria-label** also contained "Реализираната загуба е €1023." — same issue.

**Fixes applied:**
- Result box text changed to "10 поредни загуби → оставаш с реализирана загуба"
- aria-label updated to remove €1023 figure
- Removed horizontal red dashed limit line that caused visual contradiction (10th bar appeared to cross the €500 line while being shown as accepted)

### Pipeline decision

SVG fixed (hand-fix, all numbers still trace to 05b). Hero and SVG both re-reviewed in pass 2.
