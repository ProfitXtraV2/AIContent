# 06 — Verification (vk-0290 канаста)

## Surviving flags
NONE. 0 [VERIFY] / 0 [DATA NEEDED] / 0 [CONFLICT] in the final 05b.
Two [VERIFY] flags raised upstream were resolved from the reachable primary source (pagat.com), not by guessing:
- [VERIFY #1] §2 "stock/talon count after deal": the body makes NO numeric claim about the remaining stock, so there was nothing unverified to carry. The flag was removed (no number invented).
- [VERIFY #2] §12 "is the final discard mandatory on every go-out": pagat states both methods — "meld all but one and discard the last, OR meld everything at once." The body already states both correctly; wording tightened to "...или сваля цялата си ръка наведнъж, без последно изхвърляне." Sourced, not guessed.
This is a народна/международна card-game rules guide with 0 operator-specific facts, 0 НАП-register facts, 0 tax figures, 0 € amounts → nothing requiring further human source verification remains.

## Time-sensitive claims
- None in the body. Canasta rules are evergreen.
- Byline dates 24.10.2026 (today, UTC). No affiliate footer (no operator recommended) → no dated licensing boilerplate in this piece.

## Figure recalculation (working shown) — every number re-derived from the sourced rules in 05b
- Deck: 2 × 52 + 4 джокера = 104 + 4 = **108** ✓ (matches 05b + infographic; "108 карти").
- Card points: Джокер 50; Асо/двойка 20; Поп/дама/вале/10/9/8 = 10; 7/6/5/4 = 5; черна тройка 5 ✓ (all match 05b values list + infographic).
- Red threes: 4 × 100 = **400**, "удвоените 800" → 4-of-a-kind bonus doubles to **800** (symmetric −800) ✓ (matches 05b "не 400, а удвоените 800" + infographic "800, всяка поотделно носи 100"). Each single red three = 100 / −100 ✓.
- Canasta bonus: чиста (no wild) 500; смесена (≥1 wild) 300 ✓.
- Initial-meld minimum by cumulative team score: отрицателен 15; 0–1495 → 50; 1500–2995 → 90; 3000+ → 120 ✓ (bands non-overlapping, ascending; matches 05b list).
- Go-out: обикновено излизане 100; скрито излизане +100 → **200** total ✓ (100 + 100 = 200).
- Target: 5000 ✓.
All figures internally consistent; no value changed across stages 02 → 05b (diffed). Every infographic number traces 1:1 to 05b.

## Sources (card-game rules — reachable, non-operator)
- pagat.com/rummy/canasta.html (John McLeod, Classic Canasta) — fetched 24.10.2026. Primary source for ALL figures: 108 cards; deals 11/15/13; 2-player draw-two / two-canastas-to-go-out; card point values; wild cards (jokers + twos); red threes 100/−100 and four = 800/−800; meld ≥3 / ≥2 natural / ≤3 wild; canasta 7+ natural 500 / mixed 300; initial-meld minimum 15/50/90/120 by score band; freeze/take-the-pile rules; black threes; going out + concealed +100→200; scoring; target 5000.
- en.wikipedia.org/wiki/Canasta — corroboration only (108 cards, some decks add a 3rd joker → 110; 2p=15 / 3p=13; 500/300; target 5000 classic with higher modern-American variants). Used to frame the 110-card / higher-target variant note, not as a primary figure source.
- Dedup: live sitemap https://vsichkikazina.bg/sitemap.xml (137 URLs, 24.10.2026) — 0 канаста/canasta coverage; queue + backlog also 0. No cannibalization. Distinct card-game-cluster pillar (siblings белот/сантасе/свара/табла are still in open PRs, баккара published).

## Gemini Step-7 (text) — keep-best
- Initial draft 05b: Shows strong AI patterns 90% → HL **10**.
- Humaniser pass 1 (apply Gemini recs): Shows AI patterns 75% → HL **25**.
- Humaniser pass 2: Likely AI-generated 85% → HL **15** (lower; noisy/adversarial detector raised new anglicism/POV flags not seen before).
- MAX_GEMINI_PASSES (2) reached. KEEP-BEST = pass 1 (HL **25**, highest seen). Final 05b restored to the pass-1 version.
- gemini column: `ai 75` (pass-1's own verdict, verbatim scale). Human voice polish advised downstream (same noisy-detector pattern as siblings vk-0279/0283/0285 on dry rules-dense content).

## Step-8 images
images: 2 (infographic 100/flawless, hero 65 keep-best). Gemini image review ×2:
- Infographic kanasta-stoynost-karti-bonusi.svg: "excellent / no problems / publish as-is" both passes; every number verified 1:1 vs 05b; layout clean, no overlap/clip; specific aria-label ALT.
- Hero kanasta-karti-kosnica-hero.webp (24→41 KB WebP, 1200×509): pass 1 had corner-vs-center suit mismatches → regenerated with centered-suit-only cards (pass 2). Remaining critique is stylized suit palette (flat casino-green+red), an aesthetic preference, NOT an integrity failure (no operator logos/names, no invented numbers, no people/faces, no glamorised winning). Kept per keep-best. Specific Bulgarian ALT added; hero under H1, infographic beside the card-values data with a one-line caption.
- Overall review score 65 (dragged by the decorative hero; infographic is flawless). Images never block the PR.

## Brand Gate
PASS WITH FIXES → 85/100, 0 criticals after mechanical fixes (em-dash purge in H1/footer; dates inserted; byline rendered "Автор: Георги Тодоров, Всички Казина"). Per-pillar: Personality 18/20 · Tone 14/15 · E-E-A-T 16/20 · Trust 12/15 · Language&Style 11/15 · RG 14/15. Byline Георги Тодоров, brand "Всички Казина", verbatim 18+ line, RG signposting (/otgovorna-igra/ + регистър на уязвимите лица) all present. No operator → no НАП-№ / affiliate-link obligation. 0 em-dashes at publish.
