# 08 — Gemini image review, pass 2 (Бундеслига) — after fixes

Reviewed: `images/bundesliga-format.svg` + `images/bundesliga-stadion-hero.webp` (regenerated). 2026-11-01.

Fixes applied since pass 1:
- SVG: right-column labels nudged x=500 → x=516 (more breathing room; polish only).
- Hero: regenerated with an improved prompt (accurate pitch — halfway line + centre circle + a
  penalty box at each end + goals at the ends; simple soft dotted crowd, no maze/QR artifacts).

## Result
**Score: 100 · Verdict: PASS.** 0 integrity issues. Keep-best = this pass (100 > pass-1 75).

Verbatim highlights:
- Accuracy: flawless — every SVG number matches the article (1963/64, 18, 34, 306, 3, 2+1 relegation,
  34 Bayern titles, 13 champions, 602 Körbel, 365 Müller); footnotes reflect the tie-breaker + 50+1.
- Integrity & hygiene: perfect — clean stylised vector, no fake logos, no human faces, no glamorised
  winning; infographic purely informational.
- RG: neutral tone; „18+ Играйте отговорно." footer in the infographic noted as excellent practice.
- SEO: descriptive lowercase-hyphenated filenames + specific accurate ALT text.
- Layout: no overlaps, no clipping, ample margins; longest footer (91 chars) fits the 804px card.
- Specific problems: none. Ready to publish as-is.

## Final image set
2 images — infographic (score 100) + decorative hero (score 100). Both ship in this PR.
