# 08 — Gemini image review · pass 1
Model: gemini-3.1-pro-preview (scripts/gemini_image_review.py) · run 24.09.2026
Images: bankrol-razpredelenie-zalog-limiti.svg (infographic) + bankrol-byudzhet-hero.webp (decorative hero)

VERDICT: **90/100 — PASS** (≥80, no integrity failure).
- Infographic accuracy: every figure matches 05b 1:1 (€200, 1%/€2, 2%/€4, 5%/€10, 4×€50, €50 stop-loss, €75→€50 win-limit). No overlap, no clipped text, filenames + ALT good, „18+ Играйте отговорно" present.
- Hero: strong visual metaphor (wallet + safe + portioned chip tray), neutral tone, no faces, no glamorised winning, no logos.

Minor recs (non-blocking):
1. SVG: the colored left accent strips have square corners that poke past the cards' rounded corners → round/inset the strips. (Applied as image fix pass 1.)
2. Hero: chip tray shows 3 compartments vs the text's 4 sessions — metaphorical, not fatal; a future-prompt nicety only. Left as-is (regeneration risks a weaker image; keep-best).
