# Step 8 — Image review, pass 1

## Environment
- AI hero generation: **SKIPPED** — image API offline (HTTP 402, probed 29.09.2026).
- Gemini visual review: **SKIPPED** — Gemini offline (HTTP 402, probed 29.09.2026).
- No Gemini/image script was called. Fallback: MANUAL INTEGRITY CHECK by the writer.

## Image 1 — images/extremely-hot-rtp-infografika.svg (hand-authored infographic)
MANUAL INTEGRITY CHECK:
- **Every SVG number ⊂ body (05b):** 95.74%, 4.26%, €1000, €957.40, €42.60, „5000 пъти залога на линия", „3 от 5", „5 фиксирани" — all present in the body prose. Verified grep-verbatim. ✓
- aria-label figures (95.74% / 4.26% / €1000 / €957.40 / €42.60 / 5 фиксирани линии / 5000 пъти залога на линия / 3 от 5) all trace to body. ✓
- **No logos, no operator screenshots, no faces, no invented numbers, no glamorised winning.** Neutral RTP/house split + key-facts panel. ✓
- **Filename** descriptive lowercase-hyphenated (extremely-hot-rtp-infografika.svg). **ALT** full Bulgarian, describes every data point. **Caption** marks „Примерни стойности" and „активният RTP зависи от оператора". ✓
- **Layout hygiene:** dark 720×512 card (rect 8/8/704/496 rx18 #0f172a); labels start x=32/48/52; all lines end ≤688 (right rail); rows spaced ≥20px; two rounded sub-panels (#111f38); bottom strip present („Примерни стойности; активният RTP зависи от оператора. 18+ Играйте отговорно."). NO em-dash. ✓
- Bar geometry: player 628 px + house 28 px inside the 32..688 track; no overflow. ✓

## Conclusion
images: 1 (infographic; Gemini score n/a — offline; manual integrity PASS)
