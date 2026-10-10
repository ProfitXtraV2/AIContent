# Step 8 — Image review, pass 1

## Environment
- AI hero generation: **SKIPPED** — image API offline (Gemini HTTP 402, probed 30.09.2026).
- Gemini visual review: **SKIPPED** — Gemini offline (HTTP 402, probed 30.09.2026).
- No Gemini/image script was called. Fallback: MANUAL INTEGRITY CHECK by the writer.

## Image 1 — images/avatarux-popwins-klyuchovi-fakti.svg (hand-authored infographic)
MANUAL INTEGRITY CHECK:
- **Every SVG number/label ⊂ body (05b):** 2019, Малта, Epic88, Yggdrasil, „YG Masters", Relax Gaming, PopWins, „два нови", PopRocks, CherryPop, TikiPop, HippoPop, BountyPop, „висока волатилност", 96.14%, 96.2% — all present in body prose. Verified grep-verbatim 30.09. ✓ No stray CJK/fullwidth chars.
- aria-label figures all trace to body. ✓
- **No operator logos, no operator screenshots, no faces/people, no invented numbers, no glamorised winning.** Neutral key-facts + mechanic panel. ✓
- **Filename** descriptive lowercase-hyphenated (avatarux-popwins-klyuchovi-fakti.svg). **ALT** full Bulgarian, describes every data point + mechanic. **Caption** notes „Публично обявени числа" + „активният RTP се вижда в инфо-панела". ✓
- **Layout hygiene:** dark 720×560 card (rect 8/8/704/544 rx18 #0f172a); labels start x=32/52; text lines end within right rail; rounded sub-panels (#111f38); bottom strip present. NO em-dash. ✓

## Conclusion
images: 1 (infographic; Gemini score n/a — offline; manual integrity PASS)
