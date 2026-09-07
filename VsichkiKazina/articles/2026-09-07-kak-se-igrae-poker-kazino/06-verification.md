# 06-VERIFICATION — Всички Казина · 2026-09-07-kak-se-igrae-poker-kazino
*For the human at Step 6. FLAGS STAY IN THE TEXT — this file only helps you verify fast. Nothing here has been resolved by the autopilot.*

Article: **Как се играе покер в казино: видовете игри и правилата зад тях** · type: guide · byline: editorial (signed Георги Тодоров) · gate: PASS WITH FIXES 95/100 · humanisation: HUMAN-LIKE ~50/60 · Gemini Step-7: ai 75 (kept best; see below) · run date: 07.09.2026

## Surviving flags
**0.** No [VERIFY], [CONFLICT], or [DATA NEEDED] flags. Evergreen concept guide; no claim about
any real operator, paytable, licence number, or tax. Paytables are stated to vary by игра/оператор
and must be checked (не се твърди конкретна таблица като факт). Every € figure is explicitly
ILLUSTRATIVE.

## Time-sensitive claims needing a primary-source check
**None.** No operator terms, no live offers, no НАП licence numbers, no tax thresholds. Dated
strings are only the run date 07.09.2026 and the verbatim affiliate footer's legal citation
("ДВ, бр. 69 от 31.07.2026 г." / "от 1 август 2026 г.").

## Illustrative numbers used (all hypothetical, none sourced)
| Where | Figure | Note |
|---|---|---|
| Домашно предимство и RTP | RTP ~98% → домашно предимство ~2% | hypothetical, explicitly labelled „илюстративни" |
| Same | на всеки заложен €100 → средно ~€2 остават при казиното (долгосрочно) | illustrative |
| Видео покер | Jacks or Better: изплащане от чифт валета нагоре | game-rule description, not an operator paytable |
| Стълбица на ръцете | висока карта → роял флъш (десетка, вале, дама, поп, асо от една боя) | standard poker hand ranking |

## Recalculation shown (per Step-6 requirement)
- House edge from RTP: 100% − 98% = **2%**. ✓ matches text.
- Long-run cost: 2% × €100 = **€2** expected house take per €100 wagered, over a long period. ✓
  matches "на всеки заложен €100 ... остават средно към €2". Single-session variance is far larger
  (stated in text). ✓
- Hand ranking order internally consistent (чифт < два чифта < трипс < кента < флъш < фул хаус <
  каре < стрейт флъш < роял флъш); note three-card poker's stated inversion (кента бие флъша) is a
  real rule of that variant. ✓

## Compliance spot-check (verbatim untouchables present)
- RG marker line "18+ Хазартът може да пристрасти. Играйте отговорно." — present (inline RG touch + footer). ✓
- RG signposting: /otgovorna-igra/ + национален регистър на уязвимите лица (НАП) + Солидарност
  0888 99 18 66 (10:00–17:00). ✓
- Affiliate footer (1 Aug 2026 regime), pending-application wording, NO issued-licence claim, NO
  invented number. ✓
- Internal links: only the approved set (/kazino-igri/, /kak-ocenyavame/, /otgovorna-igra/), 3 distinct. ✓
- Zero em-dashes (incl. meta). ✓ No operator names, no specific paytable claimed as fact, no sports,
  no promise/hype/FOMO words, no tax figures. ✓ Домашно предимство framed as долгосрочна statistic;
  „правилната стратегия свива предимството, но не го маха" stated. ✓ No card-counting-as-winning-system claim.

## External check (Step 7 — Gemini cross-model)
Model gemini-3.1-pro-preview. Pass 1 (as-delivered 05b): "Shows AI patterns 75%" → hl 25. Applied
Gemini's style recs via Humaniser pass 1 → pass 2 check "Shows AI patterns 80%" → hl 20 (regressed:
a new rule-of-three fragment). Humaniser pass 2 (fixed the fragment, removed the „другата страна на
монетата" cliché, dismantled the Goldilocks synthesis) → pass 3 check "Shows AI patterns 75%" → hl
25. MAX_GEMINI_PASSES (2) reached. **Kept best = pass 2 (hl 25, tied-highest and cleanest).**
Recorded `ai 75`. Remaining Gemini flags target the brand's own required style (asymmetric
opinionated close, dry per-format verdicts), which are style-only recs that do not override brand
voice — not applied. All numbers, links, RG lines, 18+, dates, byline, brand untouched across passes.

## Anti-cannibalization note (Step-6 human check)
No poker page exists in the live sitemap — clean pillar for „как се играе покер". `/kazino-igri/` is
an upward hub link, not a competing target. A future commercial poker listing would link to this guide.

## Human-action list (owned by you, Step 6 / Step 8)
1. Fill the "[About Всички Казина boilerplate]" slot.
2. Confirm the site's affiliate-licence status at publish (footer says filed/awaiting; never claim issued).
3. Optional: at publish, add a contextual cross-link between this guide and /kazino-igri/ sub-pages.
