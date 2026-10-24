# 06 — VERIFICATION · vk-0183 · Mines (Майнс)

STATUS: for human sign-off before publish.
Surviving flags: [VERIFY] 1 (RTP 97% — provider-cited, confirm in-game) · [DATA NEEDED] 0 · [CONFLICT] 0.
The [VERIFY] flag is intentionally left IN the body per house rules (a [VERIFY] does not block publish; the human resolves it at Step 6).

## External checks (finalized by orchestrator)
- Gemini text check (Step 7): SKIPPED — GEMINI_UNAVAILABLE (HTTP 402, prepayment credits depleted). gemini=skipped.
  Initial draft stands as final 05b. See 07-gemini-check-1.md.
- Images (Step 8): 1 hand-authored SVG infographic (round flow + key numbers; numbers verbatim to 05b).
  AI hero SKIPPED (402). Image review SKIPPED (402); manual integrity PASSED. images: 1 (infographic, review skipped — API down).
  See 08-image-review-1.md.

Body word count: 1067 (prose, excluding image ALT/caption and footer blocks). Within the 1000–1500 guide band.

## EVERY SPECIFIC FIGURE → SOURCE
Sources reached 26.09.2026 (provider page JS-rendered/unread; figures corroborated across third-party databases).
- slotcatalog — Mines (Spribe): https://slotcatalog.com/en/slots/Mines-Spribe
- casinosblockchain — Mines by Spribe: https://casinosblockchain.io/mines-by-spribe/
- tomscasinoguide — Mines: https://tomscasinoguide.com/ke/crash-games/mines/
- Spribe official (attempted, JS-rendered, NOT read): https://spribe.co/games/mines

| Figure in body | Value | Source / status |
|---|---|---|
| Мрежа | 5x5 = 25 полета | slotcatalog, casinosblockchain, tomscasinoguide (generic) |
| Брой мини | обикновено 1 до 24 (version-specific) | tomscasinoguide (1–24); others 1–20/3–20 → stated as version-specific |
| Механика | reveal poле по поле; safe → множител↑; мина → загуба; cash-out по всяко време | all three (generic) |
| Множител | обратна вероятност за оцеляване минус предимство; повече мини → по-бърз растеж | casinosblockchain, tomscasinoguide (generic principle) |
| Пример множител | 24 мини → ≈24× (едно безопасно поле от 25) | tomscasinoguide — labelled примерни; не като таблица |
| RTP | ≈97% (посочен от Spribe) | slotcatalog/casinosblockchain/tomscasinoguide — [VERIFY] (not read from spribe.co directly) |
| Домашно предимство | ≈3% (= 100% − 97%) | derived from RTP |
| Таван на печалбата | ≈ x10 000 (version-specific) | slotcatalog/casinosblockchain — stated as version-specific |
| Provably fair | сървърно + клиентско зърно, SHA-256 хеш | tomscasinoguide, casinosblockchain (generic) |
| Волатилност | висока, регулируема чрез броя мини | tomscasinoguide, casinosblockchain (qualitative) |

## NOT USED (avoid fabrication)
- „5,044,291x" theoretical max — single unverified source → NOT stated; only ≈ x10,000 (version-specific) used.
- No per-config multiplier table (none reliably sourced) → only the one illustrative 24-mines example, labelled примерни.

## RECALCULATION (with working)
- House edge = 100% − RTP = 100% − 97% = 3% → body states ≈3%. ✓ (both marked long-run, not a session promise)
- 24-mines example: 25 tiles, 1 safe → fair ≈25×; minus ~3% edge ≈ 24× → body states ≈24 пъти, labelled примерни. ✓

## INTERNAL LINKS USED (4, all live in sitemap 26.09.2026)
1. /kazino-igri/ — anchor „казиното"
2. /blog/krash-igri-aviator/ — anchor „краш игрите като Aviator" (contrast: crash multiplier rises automatically)
3. /otgovorna-igra/ — anchor „инструментите за отговорна игра" (RG touch)
4. /kak-ocenyavame/ — anchor „публична методика, а не на усещане"

## HUMAN CHECK BEFORE PUBLISH
- CONFIRM the 97% RTP on the in-game info panel (currently provider-cited/third-party-corroborated, NOT read from spribe.co) — resolve the [VERIFY].
- Confirm the ≈ x10,000 max win and the selectable mines range for the specific version served (both version-specific).
- No operator named, no НАП/tax claim, no affiliate — correct for a provider game explainer (Spribe named only as the game maker).
- Fill [About Всички Казина boilerplate] + [author-bio] at publish.
