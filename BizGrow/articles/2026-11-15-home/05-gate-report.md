# 05-gate-report: / (bg) home

Gate run 2026-11-15 on `04-seo.md` (OPTIMISED PAGE, FAQ block and PORT KEYS, lines 74-282; PORT KEYS
strings gated as visible copy). Phase 1 only: this stage was instructed not to edit the page, so
every fix below names the stage that applies it. Inputs read: agent + prompt files, site-rules.md,
markets/bg/author.md (canon), keyword-map.md, conversion-links.md, 00-brief.md, 00-inventory.md,
04-seo.md; 00-current.md spot-checked by grep for verbatim comparison (check 1).

```
BRAND COMPLIANCE SCORECARD — / (bg)
Verdict: PASS WITH FIXES
Total: 90/100
Voice 18/20 | Language 13/15 | Trust & claims 17/20 | Usefulness 14/15 | Anti-AI 14/15 | SEO 14/15
```

Verdict basis: score ≥ 85, but one CRITICAL on check 2 (non-canon fact in services card 5). It is
mechanically fixable (04-seo.md already gives the canon fallback), so PASS WITH FIXES, not FAIL.
After the fix below the page meets PASS.

---

## MECHANICAL CHECKS (script: `scratchpad/gate.py`, python3 -I, over 04-seo.md lines 74-282)

| check | result |
|---|---|
| Em-dashes / en-dashes (— –) | 0 |
| „ти“ verbs (губиш, попълваш, получаваш, можеш, имаш, знаеш, отбелязваш, …) | 0 |
| Singular imperatives (Открий, Запази, Поправи, Разгледай, Изпрати, Виж, Започни, …) | 0 |
| твой*/теб/тебе/ти/те as pronouns | 0 |
| Lowercase вие/ви/вас/ваш* in direct address | 0 |
| Banned terms (site-rules §2, §3 incl. hype, guarantee, №1, 100%, сертифиц*, urgency, промоц*, отстъпк*, ваучер*, отзив*) | 0 real hits (11 raw hits were substrings: „док**умен**ти“, „вс**яко**“) |
| „безплатн*“ | 18, every one refers to the diagnosis (or „Първата стъпка е безплатна“ = the diagnosis) |
| Prices (digit + лв/лева/евро/€/EUR/BGN/$) | 0 |
| Exclamation marks | 0 |
| Question marks | 7, all FAQ questions (allowed); 0 rhetorical questions in body |
| AI-tell connectives/boilerplate list (освен това, в заключение, именно, ето как, съобразени, иновативн, не просто, …) | 0 |
| „не …, а …“ endings | 0 (see Anti-AI note on „дни, не месеци“) |
| Hard-coded URL / email | 0 |
| `{{BOOKING_URL}}` | 3 in body (#hero, #audit, #contact) + 4 in PORT KEYS (nav, hero, cta, contact) |
| `{{EMAIL}}` | present (#contact body, form, PORT KEYS contact) |
| Link targets | `{{BOOKING_URL}}`, `#services`, `/diagnostika/` ×3 in body (+ losses.link key), card hrefs /ai-asistent/, /avtomatizacii/, /seo-statii/, /socialni-mrezhi/, /reklama/, /seo-optimizacia/ — all in conversion-links.md |
| title | „AI автоматизация за малкия бизнес \| BizGrow“ = 43 chars (≤ 60), no em-dash |
| meta description | 149 chars (120-160), starts with the main term, no em-dash |
| ogTitle / ogDescription | 42 / 130 chars, no em-dash |

---

## BLOCKING CHECKS

1. **NOTHING LOST — PASS.** C1-C6, T1-T2, all 8 anchors (+ #faq by brief), F1-F9, N3-N8, L1, L2
   (flagged), E1-E3 verbatim, losses 5/5, reasons 4/4, footer.descriptor verbatim, UI strings kept.
   N1/N2, the questionnaire step wording and „Решения по поръчка“ are REMOVE-BY-BRIEF. Rewordings
   checked against 00-current.md keep meaning: reasons.lead („Без жаргон … съобразени с твоя
   бизнес“ → „Обясняваме всяко решение на разбираем език … във Вашия бизнес“), process step 3
   („Следим и подобряваме решението“ → „следим решението и го подобряваме“), results.title gains
   „може да“ (safer, same meaning), hero.imageAlt reworded from the em-dash version.
2. **FACTS ALLOWED LIST — FAIL (CRITICAL, mechanically fixable).**
   - Quote: services card 5 body (#services line 117 and PORT KEYS services.items[5], line 239)
     „**Всеки месец** Ви отчита резултатите с конкретни числа.“ Canon (Service 4) says only that
     the specialist „reports with numbers“; a monthly cadence for the specialist's report is not
     canon and not current-page copy. → Fix: use the fallback already given in 04-seo.md:
     „Отчита Ви резултатите с конкретни числа.“ in both places; move the monthly cadence to OWNER
     ITEMS. **Stage: Step 5 Phase-2 apply pass (orchestrator), before Step 6.**
   - Card 5 title „Реклама в Google и Facebook“: platform names not in canon, but taken from the
     owner's-session H1 for /reklama/ in keyword-map.md and flagged [OWNER CONFIRM]. Accepted as
     owner-session sourced; stays an owner item (not a critical).
   - „за дни, не месеци“ (hero.body, hero.overlayUnit): canon explicitly allows it only with
     [OWNER CONFIRM]; flag and canon fallback present. PASS.
   - All other BizGrow statements (cards 1-4 and 6, process, FAQ 1-7, reasons, audience list in
     FAQ 6) match the canon wording.
3. **BANNED CLAIMS — PASS.** No guarantee, ranking, №1/лидер/най-добр*, price, offer,
   testimonial, hype; „безплатн*“ only for the diagnosis.
4. **NUMBERS — PASS.** 30 мин/30-минутен, 48 ч/48 часа, „обикновено до 2 седмици“ (qualifier
   present in all 5 occurrences: #process 2, FAQ 4, meta, og, hero fallback), „0 обвързване“
   (current-page figure, canon „commits to nothing“). „24/7“, „около 10 часа седмично“, „80%“ only
   inside the labelled #results rows, flagged [OWNER CONFIRM]. 0 [VERIFY] facts.
5. **HYPOTHETICAL LABEL — PASS.** „Примерни сценарии по нашия метод, не данни от конкретни
   клиенти.“ verbatim above the rows in #results and in results.note.
6. **GDPR WORDING — PASS.** Only „Работим по GDPR“ (#reasons).
7. **REGISTER — PASS.** 0 „ти“ forms in body, headings, CTAs, lists, FAQ, title, meta, og, ALT,
   PORT KEYS. Courtesy forms capitalised. FAQ questions in the reader's first person („екипа ми“,
   „да започна“) are not „ти“ forms.
8. **CTA RULES — PASS.** Every booking CTA → `{{BOOKING_URL}}`; email only `{{EMAIL}}`; wording
   from the approved set („Безплатна диагностика“ noun CTA allowed, „Запазете час“, „Запазете
   безплатна диагностика“, „Запазете видеоразговор сега“); one booking CTA per section. Note:
   „сега“ in C5 is current-page copy (inventory C5), not on the urgency list; kept.
9. **ONE TERM PER PAGE — PASS.** „ai автоматизация“ (keyword-map row `/`) exactly once each in
   title, H1 (hero.line1), first 100 words (hero.body sentence 1) and one H2 (#services); also in
   meta/og. Sibling terms appear only as card titles linking to their pages („AI асистент и
   чатбот“, „SEO оптимизация“), as the brief allows; none in title, H1 or an H2.
10. **LINKS & ANCHORS — PASS (with a housekeeping note).** All paths/tokens/anchors are in
    conversion-links.md; existing anchors unchanged and in order. The new `#faq` anchor is added by
    the brief but has no row in conversion-links.md yet (see MODERATE 1). EN parity: N/A (bg page;
    /en/ must reuse `faq` when rewritten).
11. **BIZGROW VOICE — PASS.** No fragment paragraphs, rhetorical questions, verdict lines, slang,
    hype or exclamation marks in body copy. H1 line 2 „По-малко рутина, повече бизнес.“ is the
    owner's slogan kept by brief; metric captions and list items are UI labels.

---

## CRITICAL (blocks)

1. „Всеки месец Ви отчита резултатите с конкретни числа.“ (#services card 5, line 117; PORT KEYS
   services.items[5], line 239) → check 2 (non-canon fact: monthly cadence of the specialist's
   report) → replace with „Отчита Ви резултатите с конкретни числа.“ in both places; keep the
   title flag; add the cadence as an owner item. **Applied by: Step 5 Phase-2 apply pass.**

## MODERATE

1. `#faq` is not listed in `BizGrow/conversion-links.md` (Section anchors table). The anchor is
   binding by brief, so the page is right; the reference file needs a row („#faq | FAQ | buyer
   questions“). **Fix by: human / owner's session maintaining conversion-links.md (no page stage
   writes it).**
2. hero.imageAlt „…, с внедряване на AI, автоматизирани процеси, спестено време и разходи и
   растеж на бизнеса.“: the double „и … и“ reads awkwardly, and „спестено … разходи“/„растеж“
   reads as an outcome claim if taken out of the banner context. It mirrors the text on the banner
   image (current ALT), so it is not a guarantee. Suggested: „BizGrow: AI и автоматизация за
   малкия бизнес. На изображението: внедряване на AI, автоматизирани процеси, спестено време и
   разходи, растеж на бизнеса.“ **Fix by: Step 5 apply pass (optional) or Step 6 owner item.**
3. Hero body sentence 2 „…е въпрос на дни, не на месеци.“ is an antithesis of the „не A, а B“
   family and a non-canon speed statement; it is correctly flagged with a canon fallback. Gate
   recommendation to the owner: prefer the fallback („…а изграждането обикновено отнема до 2
   седмици.“) for both hero.body and hero.overlayUnit. **Owner decision (Step 6).**
4. Jargon not explained on first use: „техническото SEO“ (card 6) and „B2B фирми“ (FAQ 6). Any
   gloss must not add service detail beyond the canon (canon: „technical SEO, on-page
   optimisation and links. Nothing more specific“). Suggested: „B2B фирми (фирми, които работят
   с други фирми)“; card 6 may stay as is. **Fix by: Step 5 apply pass (optional).**
5. Three body links go to the same `/diagnostika/` target (losses link, process step 1, FAQ 3).
   Within the 1-3 contextual-links rule and each is useful in place; no change required. Process
   step 1 and FAQ 3 inline links need inline-link rendering in the component (already in flag 6).
6. Final content file must carry no `[OWNER CONFIRM]` markers: every flag below becomes an
   `[[owner_items]]` entry when `content/home.port.json` / the content file is finalised.
   **Fix by: Step 6.**

---

## OWNER ITEMS TO RAISE (for Step 6)

1. H1 change: hero.line1 „AI автоматизация за малкия бизнес.“ + hero.line2 „По-малко рутина,
   повече бизнес.“ (current „По-малко рутина. / Повече бизнес.“).
2. „за дни, не месеци“ in hero.body and hero.overlayUnit: confirm, or use the canon fallback
   „обикновено до 2 седмици“ (gate recommends the fallback).
3. Six service cards with new `href` field, replacing the four cards incl. „Решения по поръчка“.
4. Card 5 title „Реклама в Google и Facebook“ (platform names, from the /reklama/ keyword-map H1).
5. NEW from gate: whether the marketing specialist reports **monthly**. Gate removes „Всеки месец“
   from card 5; it can return only if the owner adds it to the canon.
6. Example rows E1-E3 with „24/7“, „около 10 часа седмично“, „80%“ (#results; label kept).
7. New hero metrics (30 мин разговор / 48 ч до доклада с цени / 0 обвързване) replacing the
   removed questionnaire figures.
8. Port/structure: new #faq section + `faq` key + component; new `losses.link` key; new
   `services.items[].href`; inline links in process step 1 body and FAQ 3 answer need link
   rendering (or the link is dropped and the words kept).
9. Optional: a GDPR/data FAQ was not added (canon answer is one phrase); owner may supply wording.
10. NEW from gate: add `#faq` to conversion-links.md section anchors (and use it on /en/).
11. NEW from gate (optional): hero.imageAlt wording (MODERATE 2).

## VOICE NOTES (protect during fixes)

- Card bodies are concrete and canon-exact (Messenger/Instagram/WhatsApp, online booking with
  reminders, form → PDF, approval before publication, real specialist); keep the wording.
- Jargon glosses already good: „Чатботът е асистент в чата, който…“, „табло (дашборд)“, „(SEO)“,
  „връзките (линковете)“. Do not remove.
- FAQ answers are 1-3 complete formal sentences that do not echo headings; keep.
- Keep „обикновено“ wherever „до 2 седмици“ appears, and the example label directly above the
  #results rows.
- Do not touch the main-term placements (title, hero.line1, hero.body sentence 1, #services H2).

## PILLAR NOTES

- Voice 18/20: calm consultancy register throughout; minus for the slogan-led hero and the
  „дни, не месеци“ line.
- Language 13/15: native word order and agreement; minus for the ALT „и … и“ chain and two long
  sentences (card 2 sentence 1, FAQ 1 sentence 2, both about 25 words).
- Trust & claims 17/20: canon-tight apart from the card 5 monthly cadence (critical) and the two
  flagged non-canon items awaiting the owner.
- Usefulness 14/15: tasks named concretely; next steps clear (diagnosis → 48 h report → build →
  monthly support), cost of starting stated (free, no commitment).
- Anti-AI 14/15: no tells found by script or read; minus for the „дни, не месеци“ antithesis.
- SEO 14/15: placements exact, lengths in range; minus for the unregistered #faq anchor.

---
---

# PHASE 2 — APPLICATION (run 2026-11-15, after the orchestrator confirmed Phase 2 belongs to this stage; 04-seo.md itself untouched)

## Changes applied (6 replacements, made by script `scratchpad/apply.py` on a copy of 04-seo.md lines 74-282)

1. CRITICAL fixed (check 2): card 5 body „Всеки месец Ви отчита резултатите с конкретни числа.“ → „Отчита Ви резултатите с конкретни числа.“ in #services and in PORT KEYS services.items[5] (2 places).
2. Card 5 flag texts updated in both places to record that the Brand Gate removed the monthly cadence. The flag itself kept (platform names in the title still need the owner).
3. Card 6 jargon: „техническото SEO на сайта“ → „техническото SEO на сайта (техническата му настройка за търсенето в Google)“ in #services and PORT KEYS (2 places). Definition only, no new service detail.
4. FAQ 6 jargon: „B2B фирми“ → „B2B фирми (фирми, които продават на други фирми)“.
5. hero.imageAlt: „…, с внедряване на AI, автоматизирани процеси, спестено време и разходи и растеж на бизнеса.“ → „BizGrow: AI и автоматизация за малкия бизнес. На изображението: внедряване на AI, автоматизирани процеси, спестено време и разходи, растеж на бизнеса.“ (removes the „и … и“ chain; marks the list as the banner's text, not a promise).
6. Not changed: „за дни, не месеци“ (owner decision, flagged with fallback); „Запазете видеоразговор сега“ (inventory C5). No source, CTA, token, anchor, example label or flag removed: `[OWNER CONFIRM]` count in the page = 9 before, 9 after.

## Re-run of gate checks on the corrected page (`gate.py`, python3 -I)

| check | result |
|---|---|
| Em-dashes / en-dashes | 0 |
| „ти“ verbs, singular imperatives, твой*/теб/ти/те | 0 / 0 / 0 |
| Lowercase courtesy forms | 0 |
| Banned terms | 0 real (11 raw substring hits: „документи“, „всяко“) |
| Prices / exclamation marks / AI-tell list / „не …, а …“ | 0 / 0 / 0 / 0 |
| Hard-coded URL or email | 0 |
| `{{BOOKING_URL}}` / `{{EMAIL}}` | 7 (3 body + 4 PORT KEYS) / 3 |
| title / meta / ogTitle / ogDescription | 43 / 149 / 42 / 130 chars |
| main term | once each in title, H1, hero.body sentence 1, #services H2 (unchanged) |
| „Всеки месец“ remaining | only canon uses: card 4 (криейтиви всеки месец), process step 3 title and body (monthly support report) |

## UPDATED SCORECARD

```
BRAND COMPLIANCE SCORECARD — / (bg)
Verdict: PASS
Total: 93/100
Voice 18/20 | Language 14/15 | Trust & claims 19/20 | Usefulness 14/15 | Anti-AI 14/15 | SEO 14/15
BLOCKING CHECKS: 1 PASS | 2 PASS (card 5 fixed) | 3 PASS | 4 PASS | 5 PASS | 6 PASS | 7 PASS | 8 PASS | 9 PASS | 10 PASS (#faq row still to add to conversion-links.md) | 11 PASS
CRITICAL: none
MODERATE (remaining): #faq not yet in conversion-links.md (reference-file housekeeping, human/owner's session); „дни, не месеци“ awaiting owner (fallback recommended); [OWNER CONFIRM] markers become [[owner_items]] at Step 6.
```

Remaining deductions: hero slogan line and „дни, не месеци“ (Voice, Anti-AI), two long sentences (card 2 s1, FAQ 1 s2), unregistered #faq anchor (SEO), owner-pending non-canon items (Trust).

## REMAINING OWNER LIST (for Step 6)

1. H1 change: line1 „AI автоматизация за малкия бизнес.“ + line2 „По-малко рутина, повече бизнес.“.
2. „за дни, не месеци“ in hero.body and hero.overlayUnit: confirm, or use the fallback „обикновено до 2 седмици“ (gate recommends the fallback).
3. Six service cards with new `href` field, replacing the four cards incl. „Решения по поръчка“.
4. Card 5 title „Реклама в Google и Facebook“ (platform names from the /reklama/ keyword-map H1).
5. Whether the marketing specialist reports monthly; removed by the gate, restored only if added to the canon.
6. Example rows E1-E3 with „24/7“, „около 10 часа седмично“, „80%“ (label kept).
7. New hero metrics (30 мин / 48 ч / 0 обвързване) replacing the questionnaire figures.
8. Port/structure: #faq section + `faq` key + component; `losses.link` key; `services.items[].href`; inline links in process step 1 and FAQ 3 need link rendering.
9. Optional GDPR/data FAQ if the owner supplies wording.
10. Add `#faq` to conversion-links.md section anchors (and reuse on /en/).
11. Confirm the new hero.imageAlt wording and the two jargon glosses (card 6, FAQ 6).

---

## CORRECTED PAGE (body + FAQ + PORT KEYS; supersedes 04-seo.md lines 74-282 for Step 6)

## OPTIMISED PAGE

Page: / | Locale: bg | Type: page-rewrite | Main term: ai автоматизация

---

## AI автоматизация за малкия бизнес. По-малко рутина, повече бизнес. {#hero}

H1 (two lines):
- hero.line1: AI автоматизация за малкия бизнес.
- hero.line2: По-малко рутина, повече бизнес.

[OWNER CONFIRM: H1 change. Current „По-малко рутина. / Повече бизнес.“ becomes line1 „AI автоматизация за малкия бизнес.“ + line2 „По-малко рутина, повече бизнес.“ (slogan kept as line 2).]

BizGrow открива къде Вашият бизнес губи време, подбира подходящите решения за AI автоматизация и ги изгражда вместо Вас. Започваме с безплатна диагностика и 30-минутен разговор, а изграждането на решенията е въпрос на дни, не на месеци. [OWNER CONFIRM: „дни, не месеци“ is kept from the current page and is not in the 2026-11-15 canon. If not confirmed, the second sentence becomes: „Започваме с безплатна диагностика и 30-минутен разговор, а изграждането обикновено отнема до 2 седмици.“]

[Безплатна диагностика]({{BOOKING_URL}})

[Разгледайте услугите](#services)

Metrics (replace „8 кратки въпроса“ / „2 мин за попълване“, REMOVE-BY-BRIEF; canon figures only):
- **30 мин** разговор за диагностика (label „30 минути“)
- **48 ч** до доклада с цени (label „48 часа“)
- **0** обвързване

## Къде губите клиенти и часове всеки ден {#losses}

- Пропуснати обаждания и съобщения след работно време
- Часове, изгубени в ръчно писане на оферти и фактури
- Съобщения в Messenger, Instagram или WhatsApp, които остават без навременен отговор
- Липса на време за съдържание и социални мрежи, докато конкуренцията расте
- Неяснота кои показатели на бизнеса Ви имат значение

[Вижте примерите за Вашия бранш в безплатната диагностика](/diagnostika/)

## AI автоматизация, съдържание и реклама на едно място {#services}

[OWNER CONFIRM: six cards, one per service page, replace the four current cards incl. „Решения по поръчка“; each card gets a new `href`.]

- **AI асистент и чатбот** (icon brain, href /ai-asistent/). Чатботът е асистент в чата, който отговаря на повтарящите се въпроси в Messenger, Instagram и WhatsApp. Когато не може да помогне, той събира контакта на клиента.
- **Автоматизации** (icon loop, href /avtomatizacii/). Изграждаме онлайн записване с напомняния, оферти от попълнен формуляр до готов PDF и автоматична обработка на документи и фактури. Свързваме програмите, които вече ползвате, и подготвяме табло (дашборд) с основните показатели.
- **SEO статии и текстове** (icon spark, href /seo-statii/). Собственият ни инструмент за съдържание пише статии за Вашия бранш и град, подготвени за търсенията в Google (SEO). Всяка статия се публикува след Вашето одобрение.
- **Социални мрежи и криейтиви** (icon spark, href /socialni-mrezhi/). Публикациите с текст и изображение излизат по график, след като ги одобрите. Всеки месец подготвяме също брандирани визии и рекламни материали.
- **Реклама в Google и Facebook** (icon loop, href /reklama/). Реален маркетинг специалист планира, пуска и следи рекламите Ви. Отчита Ви резултатите с конкретни числа. [OWNER CONFIRM: platform names in the title come from the keyword-map H1 of /reklama/; canon says „реклама и маркетинг“ only. „Всеки месец“ for the specialist's report removed by the Brand Gate (not canon); restore only if the owner adds a monthly report to the canon.]
- **SEO оптимизация** (icon brain, href /seo-optimizacia/). Работим по техническото SEO на сайта (техническата му настройка за търсенето в Google), по оптимизацията на отделните страници и по връзките (линковете) към него.

## Три стъпки до работещо решение {#process}

Работата минава през три стъпки, от първия разговор до поддръжката на готовото решение.

1. **Диагноза · Къде се губят време и пари.** Започвате от [безплатната диагностика](/diagnostika/), където отбелязвате проблемите, които познавате от своя бизнес. След това в 30-минутен разговор уточняваме къде точно бизнесът Ви губи време и пари.
2. **Изграждане · Ясна еднократна цена.** До 48 часа получавате доклад с приоритизирани решения и ясни еднократни цени. След това изграждаме конкретното AI решение, обикновено до 2 седмици.
3. **Поддръжка · Прозрачен отчет всеки месец.** След пускането следим решението и го подобряваме. Всеки месец получавате кратък отчет за свършената работа.

## Как може да изглежда резултатът {#results}

Примерни сценарии по нашия метод, не данни от конкретни клиенти.

[OWNER CONFIRM: the three example rows (incl. „24/7“, „около 10 часа седмично“, „80%“) are kept verbatim from the current page; canon requires owner confirmation. The label above stays with the rows.]

| Бизнес | Проблем | Резултат |
|---|---|---|
| Ресторант | Никой не вдига в пиковите часове. | Резервации 24/7, около 10 часа седмично по-малко ръчна работа. |
| Онлайн магазин | Въпроси за пратки остават без отговор с часове. | 80% от повтарящите се въпроси с отговор за секунди. |
| Дентална клиника | Пропуснати обаждания и разместени часове. | Онлайн записване по всяко време. |

## Малкото „екстра“, което променя резултата {#reasons}

Обясняваме всяко решение на разбираем език и изграждаме само AI инструменти, които решават конкретен проблем във Вашия бизнес.

- Работим по GDPR
- Без дългосрочни договори
- Прозрачни цени
- Резултат преди голяма инвестиция

## Първата стъпка е безплатна {#audit}

Диагностиката не Ви обвързва с нищо. Показваме Ви точно какво можем да поправим и колко ще струва.

[Запазете безплатна диагностика]({{BOOKING_URL}})

## Често задавани въпроси {#faq}

(New section between #audit and #contact, new anchor `#faq`, new dictionary key `faq`. Items in the FAQ block below.)

## Свържете се с нас {#contact}

[Запазете видеоразговор сега]({{BOOKING_URL}})

Изпратете ни имейл на {{EMAIL}}

Форма: Име / Имейл / Описание; бутон „Изпратете“ (mailto {{EMAIL}}, тема „Съобщение до BizGrow от“).

---

## FAQ

[[faq]]

1. q: Какво може да се автоматизира в малък бизнес?
   a: Най-често това са отговорите на повтарящи се въпроси в Messenger, Instagram и WhatsApp, онлайн записването с напомняния, офертите, документите и фактурите. Свързваме и програмите, които вече ползвате, така че данните да се попълват сами, и подготвяме табло с основните показатели на едно място.

2. q: Колко струва изграждането на едно решение?
   a: Всяко решение има еднократна цена, която зависи от това какво точно се изгражда. Цената е посочена в доклада, който получавате до 48 часа след диагностиката. Работим без дългосрочни договори.

3. q: Откъде да започна, ако не знам какво да автоматизирам?
   a: Започнете от [безплатната диагностика](/diagnostika/), където отбелязвате проблемите, които познавате от своя бизнес, и запазвате 30-минутен разговор. Диагностиката не Ви обвързва с нищо.

4. q: Колко време отнема изграждането?
   a: След като получите доклада, изграждаме конкретното решение обикновено до 2 седмици.

5. q: Заменя ли изкуственият интелект хората в екипа ми?
   a: AI поема повтарящите се задачи, като контролът остава при Вас. Статиите и публикациите излизат след Вашето одобрение, а рекламата се води от реален маркетинг специалист. Когато асистентът в чата не може да помогне, той събира контакта на клиента.

6. q: Подходящо ли е за моя бранш?
   a: Работим с малки бизнеси: ресторанти и кафенета, хотели и къщи за гости, салони, онлайн магазини, магазини и шоуруми, клиники и кабинети, автосервизи и майстори, недвижими имоти и B2B фирми (фирми, които продават на други фирми). В диагностиката можете да видите примери за Вашия тип бизнес.

7. q: Трябва ли да подписвам дългосрочен договор?
   a: Не, работим без дългосрочни договори. По време на поддръжката следим решението и всеки месец получавате кратък отчет за свършената работа.

---

## PORT KEYS

Non-body dictionary strings that change (or are confirmed unchanged) for `site/src/i18n/dictionaries/bg.ts`. Body-mapped keys repeat the copy above so later stages edit both together.

### meta
- meta.title: AI автоматизация за малкия бизнес | BizGrow
- meta.description: AI автоматизация за малкия бизнес: безплатна диагностика, доклад с приоритизирани решения и ясни цени до 48 часа, изграждане обикновено до 2 седмици.
- meta.ogTitle: BizGrow: AI автоматизация за малкия бизнес
- meta.ogDescription: Безплатна диагностика без обвързване. Доклад с ясни еднократни цени до 48 часа и изграждане на решенията, обикновено до 2 седмици.
- meta.ogLocale: bg_BG (unchanged)

### nav (unchanged)
- nav.links: Услуги → #services; Процес → #process; Свържете се с нас → #contact
- nav.cta: Запазете час → {{BOOKING_URL}}

### hero
- hero.line1: AI автоматизация за малкия бизнес.
- hero.line2: По-малко рутина, повече бизнес.
- hero.body: BizGrow открива къде Вашият бизнес губи време, подбира подходящите решения за AI автоматизация и ги изгражда вместо Вас. Започваме с безплатна диагностика и 30-минутен разговор, а изграждането на решенията е въпрос на дни, не на месеци. [OWNER CONFIRM: fallback second sentence „Започваме с безплатна диагностика и 30-минутен разговор, а изграждането обикновено отнема до 2 седмици.“]
- hero.primary: Безплатна диагностика → {{BOOKING_URL}}
- hero.secondary: Разгледайте услугите → #services
- hero.imageSrc: /bizgrow-banner-bg.webp (unchanged)
- hero.imageAlt: BizGrow: AI и автоматизация за малкия бизнес. На изображението: внедряване на AI, автоматизирани процеси, спестено време и разходи, растеж на бизнеса.
- hero.overlayLabel: Безплатна диагностика
- hero.overlayUnit: за дни, не месеци [OWNER CONFIRM: fallback „обикновено до 2 седмици“]

### metrics
- { value: "30 мин", caption: "разговор за диагностика", label: "30 минути" }
- { value: "48 ч", caption: "до доклада с цени", label: "48 часа" }
- { value: "0", caption: "обвързване" }

### losses
- losses.title: Къде губите клиенти и часове всеки ден
- losses.items: (5, as in #losses above)
- losses.link (NEW key): { label: "Вижте примерите за Вашия бранш в безплатната диагностика", href: "/diagnostika/" }

### services
- services.title: AI автоматизация, съдържание и реклама на едно място
- services.items (6, NEW field `href`):
  1. { icon: "brain", title: "AI асистент и чатбот", href: "/ai-asistent/", body: "Чатботът е асистент в чата, който отговаря на повтарящите се въпроси в Messenger, Instagram и WhatsApp. Когато не може да помогне, той събира контакта на клиента." }
  2. { icon: "loop", title: "Автоматизации", href: "/avtomatizacii/", body: "Изграждаме онлайн записване с напомняния, оферти от попълнен формуляр до готов PDF и автоматична обработка на документи и фактури. Свързваме програмите, които вече ползвате, и подготвяме табло (дашборд) с основните показатели." }
  3. { icon: "spark", title: "SEO статии и текстове", href: "/seo-statii/", body: "Собственият ни инструмент за съдържание пише статии за Вашия бранш и град, подготвени за търсенията в Google (SEO). Всяка статия се публикува след Вашето одобрение." }
  4. { icon: "spark", title: "Социални мрежи и криейтиви", href: "/socialni-mrezhi/", body: "Публикациите с текст и изображение излизат по график, след като ги одобрите. Всеки месец подготвяме също брандирани визии и рекламни материали." }
  5. { icon: "loop", title: "Реклама в Google и Facebook", href: "/reklama/", body: "Реален маркетинг специалист планира, пуска и следи рекламите Ви. Отчита Ви резултатите с конкретни числа." } [OWNER CONFIRM: platforms in title; monthly report cadence removed by the Brand Gate, restore only if the owner confirms]
  6. { icon: "brain", title: "SEO оптимизация", href: "/seo-optimizacia/", body: "Работим по техническото SEO на сайта (техническата му настройка за търсенето в Google), по оптимизацията на отделните страници и по връзките (линковете) към него." }

### process
- process.title: Три стъпки до работещо решение (unchanged)
- process.lead: Работата минава през три стъпки, от първия разговор до поддръжката на готовото решение.
- process.steps:
  1. { n: "1", label: "Диагноза", title: "Къде се губят време и пари", body: "Започвате от [безплатната диагностика](/diagnostika/), където отбелязвате проблемите, които познавате от своя бизнес. След това в 30-минутен разговор уточняваме къде точно бизнесът Ви губи време и пари." } (port note: the current step body is plain text; the link needs inline-link rendering in the component, or the human drops the link syntax and keeps the words)
  2. { n: "2", label: "Изграждане", title: "Ясна еднократна цена", body: "До 48 часа получавате доклад с приоритизирани решения и ясни еднократни цени. След това изграждаме конкретното AI решение, обикновено до 2 седмици." }
  3. { n: "3", label: "Поддръжка", title: "Прозрачен отчет всеки месец", body: "След пускането следим решението и го подобряваме. Всеки месец получавате кратък отчет за свършената работа." }

### results
- results.title: Как може да изглежда резултатът
- results.note: Примерни сценарии по нашия метод, не данни от конкретни клиенти. (unchanged)
- results.rows: unchanged (3 rows, verbatim) [OWNER CONFIRM]

### reasons
- reasons.title: Малкото „екстра“, което променя резултата (unchanged)
- reasons.lead: Обясняваме всяко решение на разбираем език и изграждаме само AI инструменти, които решават конкретен проблем във Вашия бизнес.
- reasons.items: unchanged (4)

### cta (#audit)
- cta.title: Първата стъпка е безплатна (unchanged)
- cta.body: Диагностиката не Ви обвързва с нищо. Показваме Ви точно какво можем да поправим и колко ще струва.
- cta.button: Запазете безплатна диагностика → {{BOOKING_URL}} (unchanged)

### faq (NEW key)
- faq.title: Често задавани въпроси (equals page.faq)
- faq.items: the 7 { question, answer } pairs from the FAQ block above (FAQ 3 answer contains a /diagnostika/ link; same inline-link note as process step 1)

### contact (unchanged)
- contact.title: Свържете се с нас
- contact.book: Запазете видеоразговор сега → {{BOOKING_URL}}
- contact.emailBefore: Изпратете ни имейл на (+ {{EMAIL}})
- contact.fields: Име / Имейл / Описание
- contact.submit: Изпратете
- contact.mailSubject: Съобщение до BizGrow от

### footer (unchanged)
- footer.descriptor: Намираме къде бизнесът губи време и го поправяме с AI.
- footer.services / process / contact / privacy / rights: unchanged

### a11y, page: unchanged

