# 08 — Gemini image review · pass 1

Model: gemini-3.1-pro-preview. Images: swintt-rtp.svg (SVG source), swintt-hero.webp (raster).

**Score: 92/100 — PASS** (no integrity failure). Two minor technical fixes flagged:
1. **SVG layer order:** the `~96%` dashed reference line was drawn before the bar `<rect>`s, so it
   sat behind the opaque bar backgrounds and showed only in the 16px row gaps.
2. **SVG title wording:** „Обявен RTP" (singular) vs the article/ALT „Обявени RTP" (plural).

Hero: no corrections needed — excellent, accurate metadata, concept (SwinttSelect vs SwinttPremium)
visualised without any banned device.

### Fixes applied (pass 1)
- Moved the reference line + `~96%` label to render AFTER all six bars (now visibly on top).
- Title changed to „Обявени RTP на популярни заглавия на Swintt".
