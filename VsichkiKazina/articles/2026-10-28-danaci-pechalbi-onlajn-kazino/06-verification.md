# 06 — Verification report (for the human) — danaci-pechalbi-onlajn-kazino

**Article:** Данък върху печалба от хазарт и онлайн казино в България (2026)
**Type:** guide (YMYL, tax). **Folder:** 2026-10-28-danaci-pechalbi-onlajn-kazino (REFRESH, same slug/URL).
**Status handed over:** DRAFTED — do NOT publish until the flags below are resolved by a human.

## Sourced claim that is NOT flagged (owner-authorised, primary-source backed)
The single tax assertion stated as settled fact is backed by the verified source pack and must
stay as fact (it is NOT a [VERIFY] item):
- **Claim:** печалбите на физическото лице от хазартна игра, организирана с лиценз по ЗХ или по
  законодателството на друга държава от ЕС/ЕИП, не са облагаем доход по **чл. 13, ал. 1, т. 20
  ЗДДФЛ** (в сила от **01.01.2017 г.**); освобождаването е обвързано с лиценза на организатора;
  тото/лотария от лицензиран организатор попадат под същото правило.
- **Primary source:** `VsichkiKazina/source-packs/zddfl-gambling-winnings-2026-10-28.md`
  (verbatim ЗДДФЛ чл. 13, ал. 1, т. 20; lex.bg consolidated text `https://lex.bg/laws/ldoc/2135538631`,
  посл. изм. ДВ, бр. 113/2025; т. 20 изм. ДВ, бр. 97/2016, в сила 01.01.2017).
- The pack lifts the guides-only „0 данък claim" rule ONLY for the above. Everything else stays flagged.

## Surviving flags — HUMAN MUST RESOLVE (flags stay in the text until resolved)
1. `[VERIFY: конкретни AML прагове/задължения при входящ превод]` — §Голям превод към сметката.
   - Off-pack. The article only says the bank may ask about the source of funds under AML rules
     (not a tax) and that thresholds/procedures depend on the bank. NEVER state a figure.
   - Check: the player's own bank / общите правила по ЗМИП. Keep hedged or point to the bank.
2. `[VERIFY: третиране на хазартни загуби по ЗДДФЛ]` — §Признават ли се загубите.
   - Off-pack. One hedged sentence (losses not a deductible expense against other income),
     routed to счетоводител. Confirm with счетоводител/НАП or drop. Never a figure.
3. `[VERIFY: данъчно третиране на печалба от нелицензиран / извън-ЕС/ЕИП организатор]`
   — §Кога въпросът вече е за счетоводител или НАП.
   - Off-pack. Article states only that the т. 20 exemption is tied to the licence, so it does
     NOT apply without one; the actual treatment is routed to НАП. NEVER a ставка/праг.
   - Check: НАП (binding ruling for the specific case).

Also: `[About boilerplate slot - Всички Казина]` — fill with the site's standard About block at publish.

## Time-sensitive / factual claims to re-verify at publish
- Legal reference чл. 13, ал. 1, т. 20 ЗДДФЛ and effective date 01.01.2017 г. — verified verbatim
  against the source pack; re-confirm the article is still in force at publish (lex.bg consolidated).
- Affiliate-licensing footer disclosure (1 август 2026 г., ДВ, бр. 69 от 31.07.2026 г.; site =
  заявление подадено, очаква издаване) — verbatim brand untouchable; confirm the site's licence is
  still PENDING (never claim „issued").

## Recalculation / figures check
No odds/wagering/€ arithmetic in this article (tax guide). The only money figure, **€20**, is an
illustrative amount showing the exemption does not depend on size (чл. 13, ал. 1, т. 20 does not
condition on amount) — not a calculation. No percentage or tax rate appears anywhere (confirmed: 0 `%`).

## Pipeline outcomes
- Brand Gate (Step 5): **PASS 92/100**, zero CRITICALs (tax-override applied: чл. 13 т. 20 claim NOT
  flagged; 3 off-pack [VERIFY] flags preserved; zero em-dashes in body prose).
  - Gate advisory MODERATES (human judgement, non-blocking): (a) no extra in-body natural-voice RG
    touch beyond the footer block (floor met via 18+ line + /otgovorna-igra/ + register signposting);
    (b) no separate author-bio slot (only the About slot is present).
- Gemini text check (Step 7): keep-best over initial + 2 humaniser passes. Human-likeness 15 → 15 → 25;
  kept **pass 2 (HL 25)**, verdict „Shows AI patterns, 75%". Below the 80 target; the external detector
  runs noisy on BG YMYL legal/tax copy (documented across this repo). Content is clean, gate-passed,
  facts locked to the source pack. gemini column = `ai 75`. Trail: 07-gemini-check-1/2/3.md.
- Images (Step 8): **2** — decorative hero (webp, 18 KB) + decision-flow infographic (SVG, every figure
  traces to 05b: чл. 13 ал. 1 т. 20 ЗДДФЛ, 01.01.2017 г., €20, ЗХ/ЕС-ЕИП, питайте НАП). Gemini image
  review 75 → fix (label overlap) → **95 PASS**, 0 integrity failures. Trail: 08-image-review-1/2.md.
- Length: ~929 words. Internal links (4, approved set): /blog/proverka-licenz-kazino/, /sravni-kazina/,
  /zakonno-li-e/ (body) + hub /blog/regulations-taxes/ (footer). Byline: Георги Тодоров. No affiliate links.
