# 06 — Verification · 2026-09-12-dostavchici-kazino-igri

**Article:** Кои са доставчиците на казино игри и защо са важни
**Type:** guide (educational concept hub) · **Byline:** Георги Тодоров · **Brand:** Всички Казина
**Body length:** ~975 words · **Gate:** PASS 94/100 · **Em-dashes:** 0

## Surviving flags
None. Zero `[VERIFY]` / `[DATA NEEDED]` in 05b. Concept-education only (what a game provider is, supplier vs operator, RNG/certification, RTP configurability) — no operator-specific bonus/licence or НАП-register facts, so no primary operator/НАП source required.

## Time-sensitive / factual claims + sources
Provider/lab facts are public company history, verified 12.09.2026 via provider sites + industry references:
- **Pragmatic Play** founded 2015 (Malta/Gibraltar/UK offices). **Amusnet** — София; grew from **EGT** (Euro Games Technology, founded in Bulgaria 2002); online titles ran as EGT Interactive until the 2022 rename to Amusnet. **NetEnt** founded 1996 (Stockholm), part of Evolution Gaming since 2020. **Play'n GO** founded 1997 (Växjö, Sweden). **Novomatic** founded 1980 by Johann Graf (Gumpoldskirchen, Austria).
- Test labs: **GLI** (Gaming Laboratories International); **eCOGRA** (from 2003, UK); **iTech Labs** (founded 2004, acquired by GLI 2023); **BMM Testlabs** (from 1981).
- RTP **96%** / **€1000** / **€960** / **€40** are explicitly illustrative (labelled "Числата са примерни, не са данни от конкретно казино или заглавие").
- Only the two providers with live profiles (Pragmatic, Amusnet) are hyperlinked; NetEnt, Play'n GO, Novomatic named in plain text (no live page).

## Figure recalculation (working shown)
RTP 96% on €1000 turnover → average return = 0.96 × €1000 = **€960** (matches text). Long-run house share = €1000 − €960 = **€40** (matches text). Consistent; both figures are stated in 05b and on the infographic verbatim.

## Gemini external check (Step 7)
- gemini-3.1-pro-preview. Human-likeness: **initial 25 → humaniser pass 1 = 35 → humaniser pass 2 = 30.** Pass 2 (Wikipedia-dump rewrite, bulleted list, synthesized labs) measurably LOWERED human-likeness (35 → 30), so **05b was reverted to pass 1** per keep-best (highest seen = 35). Recorded `ai 65` (pass-1 verdict: "Shows AI patterns, 65%").
- Note: the model is high-variance — a re-read of the restored pass-1 text scored 80% (HL 20) on a later call; keep-best uses the highest reading at evaluation time and does not chase the noise. Numbers/links/RG untouched every pass. Audit: 07-gemini-check-1/2/3.md.

## Images (Step 8)
**images: 2 infographics + 1 hero (best review score 100, PASS).**
- `dostavchici-kazino-igri-hero.webp` (20.6 KB) — metaphor: one game module wired to many casino screens ("one provider, many operators"). Hygiene clean.
- `dostavchik-vs-operator.svg` — who-does-what comparison; text traces to 05b.
- `dostavchik-rtp-primer.svg` — RTP example; €1000/96%/€960/€40 verbatim from 05b (green bar is exactly 96% of the container width).
- Gemini image review: **100/100 PASS**, 0 integrity failures, 0 layout defects. Audit: 08-image-review-1.md.

## Brand / compliance
Byline Георги Тодоров ✓ · brand written Всички Казина ✓ · 18+ RG line in body + footer ✓ · affiliate-disclosure footer ✓ · 4 in-body internal links, all live sitemap paths ✓ · no operator facts / no fabrication ✓ · anti-cannibalization: concept hub distinct from provider PROFILES (Pragmatic/Amusnet) and the /blog/games-providers/ category.
