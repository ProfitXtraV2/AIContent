# 06 — Verification · Лига 1 (Ligue 1)

## Surviving flags
- **0 [VERIFY] / 0 [DATA NEEDED] / 0 [CONFLICT]** in 05b. Every figure is sourced and
  evergreen-stamped where it can change.

## Recalculated figure (working shown)
- **306 мача за сезон.** 18 отбора, всеки среща всеки друг два пъти →
  18 × (18 − 1) = 18 × 17 = **306** мача. Кръстосана проверка: 34 кръга × 9 мача на кръг
  (18 ÷ 2) = **306**. ✓ Съвпада с текста.

## Time-sensitive / changeable claims — handling
| Claim | Handling | Source |
|---|---|---|
| ПСЖ 14 титли, Сент Етиен 10, Марсилия 9 | стъмпнато „към есента на 2026 г." | EN Wikipedia „Ligue 1"; потвърдено web (ПСЖ печели 2025/26 → 14) |
| ПСЖ 5 поредни 2021/22–2025/26; Лион 7 (2002–2008); Марсилия 4 | историческа справка, стъмпнато | EN Wikipedia „Ligue 1" |
| 18 отбора (от 2023/24) | стъмпнато „както е от сезон 2023/24" | LFP решение юни 2021 (20→18) |
| Европейски квоти (топ4 ШЛ, 5-и ЛЕ, 6-и ЛК…) | рамкирано принципно + препратка към официален източник (коефициент-зависимо) | EN Wikipedia „Ligue 1" (as of 2023/24) |
| Брой директни изпадащи | НЕ е закован — рамкирано „по регламента за конкретния сезон" | EN Wikipedia (историята редува правила) |
| Ландро 618 мача; Онис 299 гола | рекорди, стъмпнати | EN Wikipedia „Ligue 1" |
| Трофей „Хексагол" → нов дизайн 2024 | историческа справка | web (Hexagoal 2007–2024; ребрандинг 2024) |

Primary-source base: https://en.wikipedia.org/wiki/Ligue_1 (format, history, records);
web verification of PSG title tally after 2025/26 and the trophy history (2026-11-10).

## Gemini Step-7 (external check)
- `gemini_check.py` → **GEMINI_UNAVAILABLE (HTTP 402, credits depleted)**. Skipped per
  daily-run Step 7. No humaniser pass; kept initial 05b. gemini column = `skipped`.
- Passes applied: 0 (API unavailable). Human-likeness: not measured this run.

## Step-8 images
- **images: 1 (infographic liga-1-format.svg — numbers 1:1 vs 05b, hand-verified, 0 fabrication).**
- AI hero: skipped (Gemini image gen HTTP 402). Gemini image review: skipped (HTTP 402).
  No integrity failure (manual trace clean).

## Brand Gate
- PASS 94/100, 0 critical. Byline Георги Тодоров; brand Всички Казина; guides-only;
  0 operator/НАП/affiliate; RG + disclosure footers intact; 0 em-dash.
