# 06 — VERIFICATION (Step 6) · vk-0015
## Нови казино игри 2026: как да оцените ново заглавие
Status: PRE-PUBLISH. FLAGS STAY IN THE TEXT until the human resolves them. This file makes the human's check fast; it does not resolve anything.

Type: guide · byline: editorial (signed Георги Тодоров) · gate: PASS WITH FIXES 93/100 · humanisation: HUMAN-LIKE ~50/60 · Gemini Step-7: **ai 65** (hl 35, kept pass 2 after MAX_GEMINI_PASSES=2; high-variance reads 25/15/35) · run date: 08.09.2026

## SURVIVING IN-TEXT FLAGS: 0 (resolved by human at Step 6, 09.09.2026)
| # | Flag (verbatim, in text) | Section | Owner action |
|---|---|---|---|
| 1 | `[VERIFY: допустимост на bonus buy при лицензирани BG оператори]` | „Механиката: линии, начини за печалба и решетки" | Confirm whether feature-buy/bonus-buy is permitted for BG-licensed operators against НАП guidance / operator T&C. **RESOLVED 09.09.2026:** flag removed from 05b; sentence keeps only the generic, non-BG-specific wording „ограничена в редица юрисдикции", so the text makes no claim about BG-licensed operators and needs no primary source. |

No [DATA NEEDED], no unresolved [CONFLICT], no Version A/B structure.

## TIME-SENSITIVE / CLAIMS-TO-CONFIRM (format-education only; no BG operator T&C used)
All claims are stable public-knowledge about game FORMATS and well-known provider/game names. None is a specific-slot RTP, release date, or jackpot figure. Confirm attributions against the cited sources at revision time.

| Claim in text | Type | Source URL | What the source shows |
|---|---|---|---|
| RTP is a long-run aggregate over millions of spins; slot benchmark ~96%; remainder = house edge/„цена на развлечението" | concept/range | https://casino.betmgm.com/en/blog/guides/what-is-rtp-in-slots/ | RTP = aggregate return over time, ~96% industry standard, remainder is the cost the casino keeps; RTP ≠ session outcome |
| Волатилност = честота срещу размер; висок RTP може при всяка волатилност | concept | https://casino.betmgm.com/en/blog/guides/what-is-rtp-in-slots/ | Volatility distinct from RTP; high-RTP game can be any volatility |
| Crash: множител от 1.00x, кешаут преди срив; кръгове ~5–30 сек; provably fair е проверка, НЕ замества лицензирана RNG сертификация | mechanic + caveat | https://game-ace.com/blog/crash-games-explained/ | Multiplier rises from 1.00x, cash out before crash; rounds 5–30 s; „provably fair is verification of fairness, not a replacement for licensed RNG certification" |
| Aviator = крах игра на Spribe; JetX = Smartsoft Gaming; Cash or Crash = Evolution (live) | provider/game names | https://game-ace.com/blog/crash-games-explained/ | Names Spribe's Aviator, JetX (Smartsoft Gaming), Evolution's Cash or Crash |
| Megaways = механика на Big Time Gaming; до 117 649 начина при шест барабана | mechanic + math fact (7^6) | https://www.vegas-aces.com/articles/hold-and-win-megaways-and-cluster-pays-modern-slot-mechanics-explained + https://www.gamingsoft.com/blog/2026/05/big-time-gaming-casino-games/ | Megaways by Big Time Gaming; „up to 117,649 possible winning combinations"; high volatility |
| Cluster pays = 5+ съседни еднакви символа, каскади; hold-and-win заключва символи за повторни завъртания | mechanic | https://www.vegas-aces.com/articles/hold-and-win-megaways-and-cluster-pays-modern-slot-mechanics-explained | Clusters of 5+ adjacent matching symbols, cascades; hold & win locks symbols for respins until grid fills |
| Live game shows с водещ, напр. Crazy Time (Evolution) | format/name | https://www.gamingsoft.com/blog/2026/05/big-time-gaming-casino-games/ (+ SERP) | Crazy Time listed as an Evolution live game show |

## ILLUSTRATIVE (HYPOTHETICAL) NUMBERS — clearly generic, not operator facts
| Figure in text | Nature | Basis |
|---|---|---|
| Хиляди завъртания по €0.20 при ~96% RTP → връщат близо 96% от вложеното само като обща сметка за дългата серия; отделна вечер от няколкостотин микрозалога свършва далеч над/под тази граница | ILLUSTRATIVE, hypothetical (micro-stakes reframe, Gemini pass-2 de-cliché of the €100/€96/€4 trope) | Demonstrates ~96% RTP as a long-run average that only converges over a very large number of spins; a session does not track it |
| ~96% RTP | concept/range, not a specific-slot claim | Industry benchmark spoken about as a range, never asserted as one game's fixed RTP |
| до 117 649 начина за печалба | fixed mathematical fact (7^6) | Six-reel Megaways maximum; not fragile/time-sensitive |
| множител от 1.00x; кръгове 5–30 сек; клъстер 5+ символа | format definitions | Stable mechanic descriptions from sources above |

## ONE RECALCULATION SHOWN
RTP illustrative example (micro-stakes framing in the final text): at ~96% RTP the long-run expected return is 0.96 of turnover. Over a large series — e.g. 10 000 spins × €0.20 = €2 000 turnover — the average return converges toward 0.96 × €2 000 = €1 920, with ~4% (€80) retained as house edge; the point in the text is that this convergence needs the whole long series, while any single session of a few hundred spins lands far above or below. No fixed €-return figure is asserted in the body (only the ~96% share and the €0.20 unit stake), so nothing here is a specific-slot claim. Number set consistent across stages; the €100/€96/€4 triple present in the initial draft was deliberately reframed at Gemini pass 2 (recorded in 07-gemini-check-2/-3.md).

## COMPLIANCE SPOT-CHECK
- Em-dashes (—) in the published article + footer: 0 (verified). En-dash „–" appears only in „10:00–17:00" (allowed).
- Byline: **Георги Тодоров** present. No team/editorial byline. ✓
- Brand name exact „Всички Казина" everywhere; no transliteration. ✓
- Publication + last-edit dates present: „Публикувано: 08.09.2026 · Последна редакция: 08.09.2026". ✓
- About Всички Казина boilerplate slot present. ✓
- Verbatim RG block present: the exact line „18+ Хазартът може да пристрасти. Играйте отговорно." (also inline in the high-risk section) + /otgovorna-igra/ + национален регистър на уязвимите лица (НАП) + Солидарност 0888 99 18 66, делнични дни 10:00–17:00. ✓
- Verbatim affiliate-licensing disclosure (1 Aug 2026 regime, ДВ бр. 69 от 31.07.2026 г., „подало заявление … очаква издаването му"). No „issued" claim, no invented licence №. ✓
- Internal links (3, all approved): /kak-ocenyavame/ (RTP as a real number in the method), /kazino-igri/ (games hub), /otgovorna-igra/ (RG). No non-approved link (/slot-igri/, /novi-kazina/ routed in prose only). ✓
- Banned promise/hype/FOMO words: none. Banned AI connectives: none. ✓
- RG doctrine: хазартът = платено развлечение, не финансова стратегия; budget you can lose entirely; лимити before first deposit. ✓
- No fabricated operator fact, release date, jackpot figure, or specific-slot RTP. ✓

## EXTERNAL CHECK (Step 7 — Gemini cross-model)
Model gemini-3.1-pro-preview. Three reads (07-gemini-check-1/-2/-3.md persist as the audit trail):
- initial 05b → "Shows AI patterns, 75%" → hl 25
- Humaniser pass 1 (compliant style recs) → "Shows strong AI patterns, 85%" → hl 15
- Humaniser pass 2 (info-dump split, micro-stakes RTP reframe, softened tone, trimmed recap) → "Shows AI patterns, 65%" → **hl 35 (highest) → KEPT**

MAX_GEMINI_PASSES=2 reached; kept the highest-hl version (pass 2). Ends below 80 → gemini column `ai 65`. Gemini's score is low and high-variance on this piece (25/15/35), while the internal Brand Gate passed it 93/100 (zero criticals) and the Humaniser rated it ~50/60. Rejected as non-compliant across the loop: adding bullets/inline subheads, removing the required worked € example, and removing the [VERIFY] flag. All numbers, links, RG lines, 18+, disclosures, dates, byline and brand were preserved across every pass; nothing here resolved a flag.

## ANTI-CANNIBALIZATION NOTE
This is the site's evaluation-framework guide for judging ANY new title (RTP/волатилност/механика/провайдер/демо) plus a stable 2026 format overview. It targets „нови казино игри / как да оцените нова игра" and routes UP to /kazino-igri/ (hub) and across to /kak-ocenyavame/ (methodology), so it complements rather than competes with them. It deliberately does NOT target operator/review or single-format deep-dive queries. Overlap with a dedicated crash-games explainer (e.g. „Краш игри и Aviator") is limited to a few sentences of format context inside a broader multi-format frame; the crash piece owns the mechanic deep-dive, this piece owns the cross-format „how to judge a new game" intent. No two site pages should chase this evaluation-framework query; keep this as the canonical one.

## HUMAN-ACTION LIST
1. Resolve flag #1 (bonus-buy legality for BG-licensed operators) against НАП / operator T&C; edit 05b in place, then delete the flag.
2. Fill the [About Всички Казина boilerplate] slot at publish (Step 8).
3. Confirm publish/last-edit dates if publish slips from 08.09.2026.
4. Optional at revision: re-confirm the provider/game/format attributions against the four cited sources (formats and provider names are stable, but re-check on the 2-week cycle).
5. Do NOT publish 05b as-is: one [VERIFY] flag is still in the text by design.
