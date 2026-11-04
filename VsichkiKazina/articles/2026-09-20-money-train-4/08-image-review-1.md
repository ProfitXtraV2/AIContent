# 08 — Gemini image review, pass 1 (gemini_image_review.py, vision)

## Image 1 — money-train-4-rtp-cena.svg (infographic)
Score: **85/100** · Verdict: PASS on accuracy/integrity, BUT a layout-integrity note → treat as fix.
- Data matches 05b perfectly (96.10% RTP, 150 000× таван, 100×/500× цена на бонус, €0.10–€6 залог). SEO metadata clean; neutral RG tone. No integrity issue.
- Layout note: bottom-middle box subtext „залога (връх на разпределението)" (32 chars) is too long for the 170px box at 10px font, risks touching/exceeding the box edges; smaller risk on „залога (достъп, не резултат)".
- Fix: shorten the two subtexts (or split to two lines) to keep ≥15px inner margin.

## Image 2 — money-train-4-hero.webp (AI hero)
Score: **65/100** · Verdict: NEEDS WORK.
- Integrity clean: no fake UI, logos, faces, or glamorised winning. Metadata correct.
- Relevance: article says MT4's theme shifts to „мрачно sci-fi, ръждив метал и неон", but the hero shows a classic 19th-century steam locomotive (steampunk), no sci-fi/neon → thematic mismatch, reads as generic filler. Minor AI „muddy" artefacts on the foreground gears.
- Fix: regenerate with a sci-fi armored/futuristic train + subtle neon accents + dystopian atmosphere, keeping all hygiene constraints (no text/numbers/logos/people/UI).

## Decision
- Infographic: iterate to clear the layout note (numbers stay traced to 05b), re-review.
- Hero (optional): iterate the prompt toward the article's sci-fi theme, re-review. Keep-best applies; integrity is clean so a hero < 80 may be kept, but attempt improvement first.
