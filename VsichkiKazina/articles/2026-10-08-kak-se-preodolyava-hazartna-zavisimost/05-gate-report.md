# BRAND COMPLIANCE SCORECARD — „Как се преодолява хазартна зависимост: лечение и реалният път към възстановяване"

**Brand:** Всички Казина (vsichkikazina.bg) · **Content type:** RG / здравна образователна статия · **Date:** 08.10.2026
**Gate:** Step 5 — brand-gate-vsichkikazina.md (authoritative brand gate)

## Verdict: PASS WITH FIXES
**Total: 94/100** (post-fix) — one mechanical CRITICAL fixed in place; remaining flags are intended Step-6 human-verification items, not gate failures.

| Pillar | Score |
|---|---|
| 1. Brand personality fit | 19/20 |
| 2. Tone of voice | 14/15 |
| 3. E-E-A-T signals | 18/20 |
| 4. Trust signals & disclosures | 14/15 |
| 5. Language & anti-AI style | 14/15 |
| 6. Responsible-gambling framework | 15/15 |

---

## CRITICAL (blocks publish) — 1 found, FIXED

1. **Byline was a forbidden team/editorial byline.**
   - Quote (original L16): `Byline: Editorial Team (публикуван автор: Георги Тодоров)`
   - Rule violated: Pillar 4 / Trust — "Byline ALWAYS Георги Тодоров; a team/„Екипът на Всички Казина"/editorial byline is a CRITICAL flag."
   - Fix applied: byline front matter now reads `Автор: Георги Тодоров | Brand: „Всички Казина" | Market: BG.` The visible/published author is Георги Тодоров; the "Editorial Team" label is removed. This is a mechanical, voice-neutral fix (metadata line only; no body prose touched).

No other CRITICAL flags. No banned promise words, no hype, no FOMO/urgency, no fabricated anecdote, no Version A/B dilemma, no unscoped tax claim, no invented licence number, no operator/affiliate content, no признаци/self-screening list, no medical advice beyond "само през психиатър".

## MODERATE — 2 found

1. **Em-dashes present only in upstream production scaffolding** (SEO audit HTML comment, byline metadata line, and "— N chars" annotations), not in the article body.
   - Fix applied: removed the em-dash from the byline/front-matter line (`BG — ` → `BG. `) and converted the "— N chars" deliverable annotations to `(N chars)`. The published surface (title tag, meta description, byline, body) is now em-dash-free. The en-dashes on the diagnosis line (4–5, 6–7, 8–9) are legitimate numeric ranges and were intentionally left intact.
2. **Three-item bullet list in „Лечение... в България"** (личен лекар → психиатър/РЦПЗ → група). Assessed against Pillar 5's "excessive bullet list" tell and KEPT: it is a genuine sequential care pathway (first stop → then → in parallel), which is the legitimate use the rule preserves. No change.

## VERIFY QUEUE (route to human, Step 6 — NOT resolved by gate)

- `[VERIFY: редовни присъствени 12-стъпкови групи в България]`
- `[VERIFY: официален публичен списък на БГ клиники/центрове/психиатри с програма за хазарт]`
- `[VERIFY: статус на наредбата на Здравното министерство]`
- `[VERIFY: рамката „сред хората в лечение" да остане ограничена, да не се чете като обща популация]`
- `[DATA NEEDED: потвърди работещ телефон/часове на линия „Солидарност" 0888 99 18 66 към датата на публикуване]` (on the Солидарност line)
- Trailing `[DATA NEEDED]` summary block (Солидарност line confirmation) — left in place.

All four [VERIFY] + both [DATA NEEDED] left verbatim and untouched per instruction.

## MATHS RECALC

- "Около девет от десет души... така и не потърсват помощ" ⇒ ~10% do seek help. 1/10 = 10%. Internally consistent with the closing line "да останеш сред деветте от десет, които така и не правят първата крачка." No error.
- Diagnostic criteria 4 от 9 / 12 месеца; степени 4–5 / 6–7 / 8–9; ремисия три месеца (<12) / дванайсет месеца — all consistent, no overlap or gap. No error.
- Suicide figures "до половината суицидни мисли / ~17% суициден опит" are correctly scoped СРЕД хората в лечение (not general population); presented as reported ranges, not computed — nothing to recompute. Scoping preserved.
- "над 44 000 (средата на 2025)" — reported register figure, not derived. No error.

## VOICE NOTES (protected during fix)

- Neutral „ние" register, dry compassion (RG = solidarity not sermon) preserved verbatim; no body prose altered.
- Honest downside kept intact ("КПТ не е гаранция", high dropout, relapse expected, ~10% seek help).
- Asymmetric, opinionated ending kept ("Най-лошият избор е да останеш сред деветте от десет...").

---

## MUST-HOLD CONFIRMATION (verified post-fix)

- [x] Byline/author = **Георги Тодоров** (team/editorial byline removed). Brand spelled exactly **„Всички Казина"**.
- [x] Numbers EXACT and intact: 4 от 9 / 12 месеца · тежест 4–5 / 6–7 / 8–9 · ремисия три месеца (<12) / дванайсет месеца · девет от десет (~10%) · до половината суицидни мисли / 17% опит СРЕД хората в лечение · Солидарност 0888 99 18 66, 10:00–17:00 · НАП над 44 000 (средата на 2025) · 112 · 18+.
- [x] Verbatim line present: „18+ Хазартът може да пристрасти. Играйте отговорно." + RG signposting to /otgovorna-igra/ and националния регистър на уязвимите лица (НАП).
- [x] Internal links = only the two live ones: /otgovorna-igra/ and /blog/responsible-gambling/. [LINK] suggestion markers left for the human. No affiliate link, no operator recommendation, no licence №.
- [x] No признаци/self-screening list. No medical advice (medication framed "само през психиатър").
- [x] Disclosures, RG lines, 18+ marker, counter-arguments and dates not weakened. All [VERIFY]/[DATA NEEDED] flags left for the human.

**No pillar FAILS. No rewrite required.** Gated article saved to `05-gated-article.md`.
