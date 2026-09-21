# 06 — Verification (Stakelogic, vk-0141)

## Surviving flags (STAY IN THE TEXT — human resolves at Step 6)
- [VERIFY: founding year] — „стартира около 2014 г." Most game-DB profiles say founded 2014 as part of
  Greentube/Novomatic; one (casinohawks) says „launched 2015". Hedged in prose („около 2014 г."), not a hard figure.
- [VERIFY: Sega Sammy deal] — „през 2024 г. … се договаря да го придобие". Cross-DB: agreement announced July 2024,
  enterprise value ~€130m + earn-out, completion ~2025. Only „през 2024 г." asserted in text; the sum/dates sit in the flag.
- [VERIFY: Book of Adventure Super Stake Edition ~96.68%] — single game-DB (bestslotsjournal). Hedged „по игрална база".
- [VERIFY: Twin Joker 97.79%] — single source. Hedged „по единичен източник".
- Non-fabrication guardrails held: HQ town NOT named (sources split Eindhoven / generic „Netherlands"; brief anchor
  „Reeuwijk" unconfirmed). „Fruit Party" kept OUT (Pragmatic Play, corrected in the misattribution section).
  „Xnudge" never introduced (Nolimit City). No invented RTP, licence №, seed/cap, or max-win beyond sourced figures.

## Sourced claims (provider site + international game-DBs, NOT operator T&C / НАП)
- B2B supplier of online slots + live casino, reaches players via licensed operators — stakelogic.com (home);
  fruityslots.com/slots/providers/stakelogic.
- Netherlands base, offices incl. Malta — fruityslots; casinohawks.com/providers/stakelogic.
- Origin inside Greentube (Novomatic interactive arm), ~2014; later to outside owners; acquired by Sega Sammy
  (2024 agreement) — fruityslots; bestslotsjournal.com/slot-studios/stakelogic-slots; casinohawks; en.wikipedia.org/wiki/Novomatic. [VERIFY dates/sum]
- B2B licences MGA (MGA/CRP/322/2016) + UKGC, among others — stakelogic.com; casinohawks.
- Stakelogic Live launched 2021 (roulette/blackjack/baccarat; Super Stake live variants) — casinohawks; stakelogic.com news.
- Super Stake = optional bet-boost doubling the spin stake (×2) for a higher chance to trigger the bonus/free spins;
  Mega Super Stake ~×2.5 — fruityslots; casinohawks; primecasino.co.uk provider guide.
- Book of Adventure: RTP 96.21%, 5 reels, 10 lines, high volatility, max 5,000× — bigwinboard.com/book-of-adventure-stakelogic;
  askgamblers.com book-of-adventure-stakelogic. Book of Dead-style „book" slot — bigwinboard, askgamblers.
- Super Joker Megaways ~96.5% RTP — bestslotsjournal; casinohawks. Twin Joker ~97.79% RTP — bestslotsjournal [single-source, VERIFY].
- „Fruit Party" = Pragmatic Play (NOT Stakelogic) — general game-DB knowledge; kept out of the Stakelogic catalogue.

## Recalculated figure (with working)
- Super Stake economics (the article's honest angle). Claim in text: doubling the stake for a higher bonus chance
  does NOT change the house edge. Working: expected value EV = stake × (RTP − 1). If Super Stake sets stake' = 2 × stake
  at the same configured RTP, then EV' = 2 × stake × (RTP − 1) = 2 × EV. The expected loss scales linearly with the
  stake; the *rate* of loss (house edge = 1 − RTP) is unchanged. So a player who turns Super Stake on pays a higher
  expected cost per spin for a higher feature-trigger frequency — the extra stake buys frequency, not edge. Example at
  RTP 96.21% (Book of Adventure), €1 spin: expected cost ≈ €0.0379/spin; with Super Stake at €2: ≈ €0.0758/spin (2×),
  same 3.79% house edge. This confirms the text's „плащаш пропорционално повече … домашното предимство не се мени".

## Gemini Step-7 (external, cross-model, gemini-3.1-pro-preview)
- Check 1 (initial 05b): „Likely human-written, 85% confidence" → human-likeness 85 → PASS (≥ 80). No Humaniser pass
  needed; 05b kept unchanged (best-seen 85). Five optional style notes recorded, not applied (over-editing a passing
  draft strips voice; facts/flags/RG untouched). gemini column: `human 85`. Verdict verbatim in 07-gemini-check-1.md.

## Step-8 images
- images: 2 (Super Stake infographic SVG + decorative hero WebP 8.5 KB). Best review score: 100/100.
  - Review 1: 75 (hero ALT mismatch) → ALT fix. Review 2: 65 (hero flagged glamorised winning: upward arrow + glowing
    chest) → hero regenerated to a neutral horizontal metaphor (toggle + chips + flat arrow + book). Review 3: 100/100
    PASS both, 0 integrity, 0 layout defects. Keep-best = 100. Verdicts verbatim in 08-image-review-1/2/3.md.
  - Every infographic number traces to 05b: ×2, ×2.5, „домашното предимство не се мени", „плащаш пропорционално
    повече", „изразходваш бюджета си по-бързо". No fabricated logos/numbers/UI, no people/faces, no glamorised winning.

## Compliance
- Byline Георги Тодоров; brand „Всички Казина" exact; pub + updated dates 21.09.2026; About slot; verbatim RG line +
  /otgovorna-igra/ + НАП регистър на уязвимите лица; affiliate footer verbatim (site licence pending, not issued).
  Guide → no operator recommended → no affiliate link, no НАП licence № required. 0 em-dashes.
- Internal links (3 body + 1 RG, all verified live in sitemap.xml 21.09.2026): /blog/games-providers/,
  /blog/proverka-licenz-kazino/, /kak-ocenyavame/, /otgovorna-igra/.
- Brand Gate 92/100, 0 critical. Word count (article body, excl. footer/flags) ≈ 740 words (reference Blueprint ≈ 850).
