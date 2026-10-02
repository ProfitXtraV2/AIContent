# 06 — Verification (for the human · Step 6)

Content type: guide (generic concept). No operator/НАП primary source required.
Byline: Георги Тодоров. Surviving in-text flags: **0**.

## Claims & figures (all illustrative — labelled примерни; generic concept)
1. **Лимит на масата = диапазон мин–макс на кръг; видим на живо, в настройката при RNG; различен по
   маса/игра; отделни лимити по вид залог** (рулетка: външни залози по-висок таван от вътрешните).
   Source: en.wikipedia.org/wiki/Table_limit; generic casino practice.
2. **Таванът спира прогресивни системи (Мартингейл и др.).** Source: en.wikipedia.org/wiki/Martingale_(betting_system);
   vegas-aces.com/articles/martingale-system-doesnt-work/; gamblingsite.com.
3. **Трите грешни допускания на Мартингейл** (безкраен банкрол, маса без таван, игра без домашно
   предимство). Standard analysis, sources above.
4. **Прогресиите Labouchere / Д'Аламбер / Фибоначи** опират в същия таван. Generic betting-systems fact.

## Recalculated figures (working shown)
- Мартингейл от €10, удвояване: 10, 20, 40, 80, 160, 320 → сума на 6 загуби = **€630**.
  Седми залог = 2 × €320 = **€640** > таван **€500** → поредицата спира след 6 загуби. ✓
- Цел на Мартингейл = базовия залог = **€10** нетна печалба. ✓ (рискувате €630 за €10)
- Вероятност за 6 поредни загуби на „червено", единична нула: (19/37)^6 = **1,83% ≈ 1,8%**. ✓
  (двойна нула: (20/38)^6 = 2,13%, „още по-често" ✓)
- Дължина на сесия: €100 ÷ €1 = 100 кръга; €100 ÷ €10 = 10 кръга. ✓

## Numbers diff (02-draft → 05b after 2 humaniser passes)
€10, €20, €40, €80, €160, €320, €640, €500, €630, €100, €1, €5 000, 1,8% — all preserved; none changed/dropped. ✓

## Gemini (Step 7)
Model gemini-3.1-pro-preview. Human-likeness: initial **25** · pass1 **20** (noisy dip) · pass2 **85** (PASS).
Kept pass 2 (highest HL). gemini = human 85. Trail: 07-gemini-check-1..3.md.

## Images (Step 8)
images: 2 (Martingale infographic 100 + capped-staircase hero 100) — Gemini review **100 PASS**,
0 integrity failures, 0 layout defects; infographic numbers trace verbatim to 05b. Trail: 08-image-review-1.md.

## Human to decide
- None blocking. Table-limit figures are illustrative by design (vary by operator/table). FLAGS STAY IN THE TEXT: none here.
