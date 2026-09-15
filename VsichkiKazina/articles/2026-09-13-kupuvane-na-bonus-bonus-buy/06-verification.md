# 06 — Verification · vk-0059 „Купуване на бонус (bonus buy)"

**Type:** guide (feature explainer + decision help). Byline: Георги Тодоров. Brand: Всички Казина.
**Brand Gate:** 94/100 — PASS WITH FIXES (0 criticals).
**Gemini Step-7 (gemini-3.1-pro-preview):** **Likely human-written, 85% → human-likeness 85 (PASS on initial draft)**. No humaniser pass needed; v0 kept (`human 85`). Trail: 07-gemini-check-1.md.
**Images:** 3 — hero 82 (PASS), bonus-buy-kak-raboti.svg 85 (PASS), bonus-buy-rtp-variance.svg 100 (PASS, after 2 fixes: bar/label overlap, then decimal-point match + footer spacing). Best 100; **0 integrity failures**. Trail: 08-image-review-1..3.md.

## Surviving flags
**One `[VERIFY]` (intentional, kept in text):** `[VERIFY: наличност на „купи бонус" при лицензирани в България оператори]` — BG availability is operator/regulator-dependent and geo-blocked to confirm; left for the human per policy. Gemini noted it as a "process issue" (expected); NOT removed.

## Specific claims + primary sources
- Sweet Bonanza (Pragmatic Play) buy free spins = 100× total bet, guarantees 4+ scatters on the triggering spin.
  · Source: Pragmatic Play game guides / game databases (checked 13.09.2026).
- Sweet Bonanza 1000: theoretical RTP 94.51% vs BUY FREE SPINS RTP 94.53% (near-identical → buy is not a house-edge discount).
  · Source: Pragmatic Play game guide (MSport support doc) / game databases (checked 13.09.2026).
- UK prohibits the bonus-buy on UK-licensed sites (regulator: accelerates spend / masks per-session loss). Exact ban DATE deliberately omitted — sources conflict (2019 / 2021 / 2026), so no date is stated rather than a contested one.
- Sweet Bonanza IS live → linked /blog/sweet-bonanza/.

## Recalculated figures (working shown)
- Cost of a buy: 100 × €0.50 = **€50** per attempt (примерни). Matches text.
- House take is unchanged by buying: at ~94.5% RTP, €100 of turnover returns ≈ €94.50, so the theoretical house take ≈ €100 × (1 − 0.945) = **€5.50** — the same whether you wait for the bonus or buy it. Matches text.

## Internal links (all live)
/blog/sweet-bonanza/ · /blog/kak-raboti-razigravaneto/ · /blog/bezplatni-kazino-igri/ · /blog/rechnik-kazino-termini/ · /otgovorna-igra/

## Note
The single `[VERIFY]` stays in the text. Do NOT resolve it, post, or merge — human owns Step 6 and publishing.
