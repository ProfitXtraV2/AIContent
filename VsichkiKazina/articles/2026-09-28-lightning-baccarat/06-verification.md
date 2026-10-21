# 06 — VERIFICATION · Lightning Baccarat (Evolution): как се играе, множители и RTP

STATUS: for human sign-off before publish. FLAGS STAY IN THE TEXT.
Type: guide (branded live-game explainer) · byline: Георги Тодоров · gate: PASS 93/100 · humanisation: single draft (external check offline) · run date: 28.09.2026
Surviving flags: [VERIFY] 3 · [DATA NEEDED] 0 · [CONFLICT] 0.

## Surviving flags (left IN the body / carried for human)
1. [VERIFY] Player vs Banker RTP: източниците се разминават (livecasinocomparer: Player 98,59 / Banker 98,76; casinos.com + livecasinos.com: разменени). Задържано Banker ≥ Player по логиката на изплащанията. §„RTP и домашно предимство".
2. [VERIFY] Tie максимален множител 262 144x (Evolution, теоретичен = 8^6) срещу 310 720 (livecasinocomparer, изведено при таван 500 000 €). Задържано 262 144x като теоретичен максимум. §„Какво добавя Lightning рундът".
3. [VERIFY] Прозорец за залагане ≈ 12 сек (един източник) — НЕ е твърдян в тялото; носи се само тук.

## External checks (finalized by orchestrator)
- Gemini text check (Step 7): SKIPPED — GEMINI_UNAVAILABLE (HTTP 402, probed live 28.09.2026). gemini=skipped. See 07-gemini-check-1.md.
- Images (Step 8): 1 hand-authored SVG infographic (numbers verbatim to 05b). AI hero SKIPPED (402). Image review SKIPPED (402); manual integrity PASSED. images: 1. See 08-image-review-1.md.

Body word count: ~1,230 prose (excluding Title/Meta, ALT/caption, footer). Within the 1,000–1,800 guide band.

## SOURCES REACHED (28.09.2026)
- Evolution — Lightning Baccarat press release (Lightning range, multipliers 2x–8x, P/B 512x, Tie 262,144x): https://www.evolution.com/news/lightning-baccarat-added-evolutions-award-winning-lightning-range/
- Evolution — Lightning Baccarat game page (mechanic, Lightning cards, fee): https://games.evolution.com/live-casino/live-baccarat/lightning-baccarat/
- LiveCasinoComparer — baccarat odds/payouts (per-bet RTP/edge; payouts 1:1 / 0.95:1 / 5:1): https://www.livecasinocomparer.com/casino-guides/baccarat-odds-payouts/
- casinos.com — Lightning Baccarat (release 2020, €500,000 cap, 20% fee): https://www.casinos.com/games/lightning-baccarat

## EVERY SPECIFIC FIGURE → SOURCE
| Figure in body | Value | Source / status |
|---|---|---|
| Пусната | 30.01.2020 | evolution.com press release; casinos.com |
| Тестета | 8 | casinos.com; livecasinos.com |
| Светкавични карти на рунд | 1–5 | evolution.com game page |
| Множител на карта | 2x/3x/4x/5x/8x | evolution.com game page |
| Комбиниране | мултипликативно | evolution.com |
| Lightning такса | 20% върху залога | evolution.com; casinos.com |
| Player / Banker / Tie изплащане | 1:1 / 0,95:1 / 5:1 | livecasinocomparer |
| RTP Player | ≈ 98,59% (edge 1,41%) | livecasinocomparer — [VERIFY] (P/B conflict) |
| RTP Banker | ≈ 98,76% (edge 1,24%) | livecasinocomparer — [VERIFY] (P/B conflict) |
| RTP Tie | ≈ 94,51% (edge 5,49%) | livecasinocomparer; casinos.com; livecasinos.com (agreed) |
| Класическа бакара (сравнение) | Player 98,76 / Banker 98,94 / Tie 85,64 | livecasinocomparer |
| Макс множител P/B | 512x | evolution.com press release |
| Макс множител Tie | 262 144x | evolution.com — [VERIFY] (vs 310 720 lcc) |
| Таван на печалбата | 500 000 € | casinos.com; livecasinos.com; livecasinocomparer |

## NOT USED (avoid fabrication)
- Reversed P/B RTP from casinos.com/livecasinos.com → not adopted; flagged.
- 310 720 Tie ceiling → noted as source disagreement, not stated as the figure.
- Exact betting window in body → single source only; kept out of body, flagged here.

## RECALCULATION (with working)
- 20% fee: залог 10 € → плащаш 12 € (10 × 1,20). ✓
- Multiplicative combine: 8 × 8 × 8 = 512 (P/B, up to 3 cards). ✓ ; 8^6 = 262 144 (Tie, up to 6 cards). ✓
- P/B vs classic delta: 98,76 − 98,59 = 0,17; 98,94 − 98,76 = 0,18 п.п. lower → matches "≈0,17–0,18". ✓
- Tie nuance: 94,51% (Lightning) > 85,64% (classic Tie); still edge 5,49% (worst on table). ✓
- SVG numbers ⊂ body numbers. Verified programmatically. ✓

## COMPLIANCE SPOT-CHECK
- RG marker „18+ Хазартът може да пристрасти. Играйте отговорно." — present (in-text + footer). ✓
- RG signposting: /otgovorna-igra/ + регистър на уязвимите лица (НАП) + „Солидарност" 0888 99 18 66. ✓
- Афилиейт footer (1 август 2026 режим), заявление подадено/очаква — без издаден лиценз, без измислен №. ✓
- Game explainer: NO BG operator, NO НАП licence №, NO tax, NO bonus terms, NO affiliate links. Evolution само като maker. ✓
- Byline Георги Тодоров; „Всички Казина" правилно. ✓ Zero em-dashes. ✓
- Internal links (live in sitemap): /blog/bakara-pravila/, /blog/live-game-shows/, /kazino-igri/kazino-na-zhivo/, /kak-ocenyavame/, /otgovorna-igra/. ✓

## ANTI-CANNIBALIZATION (Step-6 human check)
Lightning Baccarat branded live-game spoke. Distinct primary kw (lightning baccarat / лайтнинг бакара)
from card-baccarat pillar (vk-0012 /blog/bakara-pravila/), Bac Bo (vk-0197, dice baccarat) and
Lightning Roulette (vk-0186, different Lightning game). No other Lightning Baccarat page in queue/sitemap.

## HUMAN-ACTION LIST
1. Confirm the Player/Banker RTP orientation against Evolution's own game info; resolve [VERIFY] 1.
2. Confirm Tie max-multiplier figure; resolve [VERIFY] 2.
3. Optional: when Gemini credits return, run Step-7 text + Step-8 image backfill.
