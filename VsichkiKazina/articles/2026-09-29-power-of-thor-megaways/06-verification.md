# 06 — VERIFICATION · Power of Thor Megaways (Pragmatic Play): RTP, волатилност и как се играе

STATUS: for human sign-off before publish. FLAGS STAY IN THE TEXT — this file only helps you verify fast.
Type: guide (slot explainer) · byline: Георги Тодоров · gate: PASS 93/100 · humanisation: HUMAN-LIKE (external check offline) · run date: 29.09.2026
Surviving flags (as in-text reviewer-estimate / version-dependence cautions): [VERIFY] 2 · [DATA NEEDED] 0 · [CONFLICT] 0.

## Surviving flags (left IN the body as prose cautions per house rules)
1. [VERIFY] Честота на бонуса ~1 на 510 завъртания и максимум ~1 на 860 000 — оценки на рецензенти,
   НЕ публикувани от Pragmatic. In-text: „Това не са публикувани от Pragmatic числа, а оценки на
   рецензенти ... гледай на тях като на порядък, не като на точна стойност". §„Безплатните завъртания".
2. [VERIFY] Кой RTP вариант е активен (96,55% default vs 95,81%/94,77%) — избор на оператора.
   In-text: „операторът избира коя пуска ... не са гарантирани навсякъде" + caption. §„RTP и конфигурации".

Omitted / not claimed:
- Точен диапазон на залога (~€0.20–€100) → operator/currency-dependent → не се твърди.
- Mystery/Loki символ → NOT FOUND на надеждни източници → омитнат.
- Точна дата на пускане → 2021 потвърдена (ден March/April [VERIFY]) → само годината в текста.

## External checks (finalized by orchestrator)
- Gemini text check (Step 7): SKIPPED — GEMINI_UNAVAILABLE (HTTP 402, probed live 29.09). gemini=skipped. Initial draft stands as final 05b. See 07-gemini-check-1.md.
- Images (Step 8): 1 hand-authored SVG infographic (ways + FS multiplier + FS trigger + buy feature + RTP builds + max win; numbers verbatim to 05b). AI hero SKIPPED (402). Image review SKIPPED (402); manual integrity PASSED. images: 1. See 08-image-review-1.md.

Body word count: ~745 (prose, excluding Title/Meta, ALT/caption, footer). Within the guide band; no padding.

## SOURCES REACHED (29.09.2026)
- Pragmatic Play official — Power of Thor Megaways (RTP 96,55%; up to 117 649 ways; tumble; FS-only multiplier; Hammer→Wild): https://www.pragmaticplay.com/en/games/power-of-thor-megaways/
- AskGamblers — Power of Thor Megaways (2021; 6 reels + top reel; FS 4 scatters = 10, +4, max 30; wilds middle reels; max win 5000x): https://www.askgamblers.com/casino-games/online-slots/reviews/power-of-thor-megaways-pragmatic-play
- FruitySlots — Power of Thor Megaways (volatility 5/5; buy feature 100x, RTP 96,97%; no-cap FS multiplier; hit-freq estimates ~1/510, max ~1/860 000): https://fruityslots.com/slots/reviews/power-of-thor-megaways-slot/
- casino.guru — Power of Thor Megaways (multi-RTP builds 96,55/95,81/94,77): https://casino.guru/power-of-thor-megaways-slot-play-free
- SlotCatalog — Power of Thor Megaways (release 2021): https://slotcatalog.com/en/slots/Power-of-Thor-Megaways

## EVERY SPECIFIC FIGURE → SOURCE
| Figure in body | Value | Source / status |
|---|---|---|
| Разработчик / година | Pragmatic Play; 2021 | Pragmatic; AskGamblers; SlotCatalog |
| Мрежа / начини | 6 барабана + горен ред; до 117 649 начина (7^6, НЕ 46 656) | Pragmatic; AskGamblers |
| Механика | tumble / каскадни печалби | Pragmatic; AskGamblers |
| Chuk (Hammer) / wilds | „чук" → wild под него; wilds на средните барабани | Pragmatic; AskGamblers |
| Множител (FS only) | старт 1x, +1 на каскада, не се нулира в рунда, без обявен таван | Pragmatic; AskGamblers; FruitySlots |
| FS trigger | 4+ THOR = 10 завъртания, +4 за всеки допълнителен, до 30 | AskGamblers; FruitySlots |
| Честота (оценки) | бонус ~1 на 510; максимум ~1 на 860 000 | FruitySlots — [VERIFY] reviewer estimate |
| Buy feature | 100x залога; RTP при купен бонус 96,97%; блокиран част юрисдикции | FruitySlots; casino.guru |
| Worked-€ | €96,55 средно от €100 (дълъг период) | derived: 96,55% × €100 |
| RTP конфигурации | 96,55% default; 95,81%; 94,77% | Pragmatic (96,55%); casino.guru (builds) — [VERIFY] активен вариант |
| Волатилност | 5/5 | Pragmatic; FruitySlots |
| Максимална печалба | 5000x, твърд таван; рундът приключва при достигане | AskGamblers; FruitySlots |

## NOT USED (avoid fabrication)
- Точен диапазон на залога → operator/currency-dependent → не се твърди.
- „46 656 начина" → грешно за това заглавие (7^6 = 117 649) → не се използва.
- Mystery/Loki символ → not found → омитнат.
- „Стратегия за печелене" → изрично оборена (случайност, конфигурируем RTP, buy feature не мени предимството).

## RECALCULATION (with working)
- Worked-€: RTP 96,55% × €100 = €96,55 средно връщане на дълъг период. ✓ Body.
- 7^6 = 117 649 (макс. Megaways начини). ✓ Body.
- Buy feature break-even: 100x залог платен наведнъж → бонусът трябва да върне ≥100x само за нула. ✓ Body.
- SVG numbers ⊂ body numbers: 6, горен ред, 117 649, 1x, 5000x, 4 THOR, 10, +4, 30, 100x, 96,97%, 96,55%, 95,81%, 94,77%, 5/5, ~1/510, ~1/860 000 — all present in 05b. Verified programmatically. ✓

## COMPLIANCE SPOT-CHECK
- RG marker „18+ Хазартът може да пристрасти. Играйте отговорно." — present (in-text + footer). ✓
- RG signposting: /otgovorna-igra/ + регистър на уязвимите лица (НАП) + „Солидарност" 0888 99 18 66. ✓
- Афилиейт footer (1 август 2026 режим), заявление подадено/очаква — БЕЗ издаден лиценз, БЕЗ измислен №. ✓
- Slot explainer: NO BG operator names, NO НАП licence №, NO tax, NO bonus terms, NO affiliate links. Pragmatic Play само като maker. ✓
- Byline Георги Тодоров; „Всички Казина" правилно. ✓ Zero em-dashes. ✓
- Internal links (live in sitemap): /kazino-igri/rotativki/, /blog/pragmatic-play-provajdar/, /kak-ocenyavame/, /otgovorna-igra/. ✓

## ANTI-CANNIBALIZATION (Step-6 human check)
Distinct branded Megaways slot explainer. Различен primary kw (power of thor megaways / пауър ъв тор)
и заглавие; допълва Pragmatic Play профил (vk-0019, live). Distinct от родовия Megaways обяснител
(vk-0041), Gonzo's Quest Megaways (vk-0211, Red Tiger, тази партида) и другите Pragmatic слотове
(Gates/Sweet Bonanza/Sugar Rush) заради механиката (FS-only множител + Hammer→Wild).

## HUMAN-ACTION LIST
1. Попълни „[About Всички Казина boilerplate]" слота.
2. Разреши 2-та [VERIFY]: честотните оценки (reviewer, не Pragmatic) и активния RTP вариант при конкретния оператор.
3. Потвърди афилиейт-лицензния статус на сайта при публикуване (подадено/очаква; никога „издаден").
