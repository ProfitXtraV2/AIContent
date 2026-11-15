# Report: BizGrow follow-up 2026-11-15 (A /saveti/, B home cards, C /reklama/)

Light path: Step 2 author (orchestrator) → Step 3 humaniser → Step 4 SEO → Step 5 Brand Gate → Step 5b light re-check. Steps 3 to 5b each ran as a fresh-context subagent. The inventory was diffed at every stage. Step 7 Gemini: **skipped (no GEMINI_API_KEY locally)**. Site source: biz-grow-seo a1ccf8f, read-only.

## Gate results

| Item | Step 3 | Step 4 SEO | Step 5 Gate | Step 5b |
|---|---|---|---|---|
| A /saveti/ | PUBLISH-READY (9/9/9/8/9) | pass, no edits (title 52, meta 136, summary 82) | PASS 92/100, 0 critical; fix: 38-word lead sentence split | PUBLISH-READY, no edits |
| B home cards + nav | PUBLISH-READY (9/9/9/9/9) | pass, no edits | PASS 93/100, 0 critical | PUBLISH-READY, no edits |
| C /reklama/ | NEEDS EDIT → 4 edits (word order in meta, repetition, run-on, FAQ 6 split; restored „публикации“) | 2 edits (stopped repeating the Facebook term next to its own link); main term once each in title / H1 (Google) / lead / H2; title 48, meta 157 | PASS 92/100, 0 critical, all 11 blocking checks PASS | PUBLISH-READY, no edits |

Scripted checks, all three files: 0 em/en dashes, 0 „ти“ forms, 0 „доклад“, 0 delivery periods, 0 prices, 0 guarantees or hype. „безплатн*“ appears only with the diagnosis. The only number is the canon „30-минутен“. All links and tokens are in conversion-links.md.

Inventory C (/reklama/): C1 to C22, all 8 section ids and all 8 FAQ questions (verbatim) are present. Removed by the brief: R1 (Facebook/Instagram as a channel of this page), R2 (FB section cut to 3 sentences pointing to /reklama-vav-facebook/), R4 (related /socialni-mrezhi/ → /reklama-vav-facebook/; /socialni-mrezhi/ still linked in the body and FAQ 5). R3: no FAQ was only about Facebook, so none was dropped. FAQ 6 (Google or Facebook?) is kept and its answer now points to the Facebook page. No /reklama-vav-facebook/ term appears in the title, meta, H1, H2, label, summary, service or eyebrow.

## C. Every changed string on /reklama/ (before → after)

- `meta.title`
  - before: "Реклама в Гугъл и Facebook с маркетинг специалист | BizGrow"
  - after: "Реклама в Гугъл с маркетинг специалист | BizGrow"
- `meta.description`
  - before: "Реклама в Гугъл, Facebook и Instagram, която маркетинг специалист планира, пуска, следи и отчита с числа. Безплатна диагностика и оферта с ясни цени."
  - after: "Реклама в Гугъл и управление на Google Ads от маркетинг специалист, който планира, пуска, следи и отчита с числа. Безплатна диагностика и оферта с ясни цени."
- `label`
  - before: "Реклама в Google и Facebook"
  - after: "Реклама в Google"
- `summary`
  - before: "Кампании в Google Ads, Facebook и Instagram, които маркетинг специалист планира, пуска и следи, като Ви показва какво връща всяко вложено евро."
  - after: "Кампании в Google Ads, които маркетинг специалист планира, пуска и следи, като Ви показва какво връща всяко вложено евро."
- `eyebrow`
  - before: "Маркетинг специалист"
  - after: "Google Ads с маркетинг специалист"
- `h1`
  - before: "Реклама в Google и Facebook с маркетинг специалист"
  - after: "Реклама в Google с маркетинг специалист"
- `lead`
  - before: "Предлагаме реклама в Гугъл, Facebook и Instagram, която жив маркетинг специалист планира, пуска и следи вместо Вас. Той отговаря пред Вас с числа и Ви показва какво връща всяко вложено евро. Първата стъпка е безплатна диагностика, която не Ви обвързва с нищо."
  - after: "Предлагаме реклама в Гугъл, която жив маркетинг специалист планира, пуска и следи вместо Вас. Той отговаря пред Вас с числа и Ви показва какво връща всяко вложено евро. Първата стъпка е безплатна диагностика, която не Ви обвързва с нищо."
- `sections[specialist].paragraphs[0]`
  - before: "Маркетинг специалистът на BizGrow е реален човек, който поема рекламата на Вашия бизнес от планирането до отчета. Той работи с кампании, като кампания означава една реклама или група реклами с обща цел и бюджет. Специалистът поема планирането и изпълнението, а при Вас остава отчетът с резултатите."
  - after: "Маркетинг специалистът на BizGrow е реален човек, който поема рекламата на Вашия бизнес от планирането до отчета. Той работи с кампании, като кампания означава една реклама или група реклами с обща цел и бюджет. Специалистът управлява кампаниите в Google Ads, като поема планирането и изпълнението, а при Вас остава отчетът с резултатите."
- `sections[specialist].bullets[0]`
  - before: "**Планиране.** Специалистът планира в кои канали да се показва рекламата: Google, Facebook, Instagram или няколко от тях."
  - after: "**Планиране.** Специалистът планира кои кампании да се пуснат в Google Ads и към какви търсения да бъдат насочени."
- `sections[facebook-instagram].title`
  - before: "Реклама във Facebook и Instagram"
  - after: "Кампании извън Google"
- `sections[facebook-instagram].paragraphs`
  - before: ["Освен в Google, маркетинг специалистът планира и пуска реклама във Facebook и Instagram. При планирането се решава дали да използвате само един от тези канали или комбинация от тях.", "Рекламите имат нужда от визии и текстове. Брандирани визии, публикации и рекламни материали можем да подготвяме всеки месец, без да Ви е нужен дизайнер на щат. Повече за това ще намерите на страницата [поддръжка на социални мрежи и криейтиви](/socialni-mrezhi/)."]
  - after: ["Кампаниите във Facebook и Instagram са отделна услуга, описана на страницата [реклама във Facebook и Instagram](/reklama-vav-facebook/). Там маркетинг специалистът също планира, пуска и следи кампаниите и Ви отчита резултатите с числа. Брандирани визии, публикации и рекламни материали за кампаниите можем да подготвяме всеки месец в рамките на услугата [поддръжка на социални мрежи и криейтиви](/socialni-mrezhi/)."]
- `faq[5].answer`
  - before: "Това се решава при планирането, след като специалистът разгледа Вашия бизнес. Той планира и пуска реклами и в Google, и във Facebook и Instagram, така че можете да използвате един канал или няколко."
  - after: "Това се решава при планирането, след като специалистът разгледа Вашия бизнес. Можете да използвате един канал или няколко. Кампаниите във Facebook и Instagram са описани на страницата [реклама във Facebook и Instagram](/reklama-vav-facebook/)."
- `related[0]`
  - before: "/socialni-mrezhi/"
  - after: "/reklama-vav-facebook/"
- `service`
  - before: "Реклама в Google и Facebook"
  - after: "Реклама в Google"

Unchanged: everything else, including `kak-raboti`, `za-kogo`, `otchet`, `proces`, `cena`, `diagnostika`, FAQs 1–5 and 7–8, the section ids and the sourced facts (Google Ads help pages 6227565 and 2472742, carried in the pipeline's content file, not in the ContentPage).

## B. Home cards: new/changed strings
- services.title: „AI автоматизация, съдържание и реклама на едно място“ → „AI автоматизация, сайтове, съдържание и реклама на едно място“
- /reklama/ card: title „Реклама в Google и Facebook“ → „Реклама в Google“; body „Реален маркетинг специалист планира, пуска и следи рекламите Ви. Отчита Ви резултатите с конкретни числа.“ → „Реален маркетинг специалист планира, пуска и следи рекламите Ви в Google. Отчита Ви резултатите с конкретни числа и Ви показва какво връща всяко вложено евро.“
- New cards: /izrabotka-na-sait/ (spark) „Изработка на сайт“, /izrabotka-na-onlain-magazin/ (brain) „Онлайн магазини“, /reklama-vav-facebook/ (chart) „Реклама във Facebook и Instagram“. The other 5 cards are verbatim live copy. Order is as in the brief.
- nav.links: „Съвети“ → /saveti/ inserted between „Процес“ and „Свържете се с нас“; page.updated „Обновено“, page.articles „Статии“.

## Owner items
1. /saveti/ H1 is „Съвети за малкия бизнес“, but keyword-map plans „Съвети“. `primaryKeyword` is "" (the hub has no term). Confirm both.
2. Approve the new home copy: 3 new cards, the Google-only /reklama/ card and services.title.
3. The website card says maintenance comes with a „кратък месечен отчет“. This applies the canon's general support step to service 6. Confirm.
4. Both ad cards use the "chart" icon, as the brief set. Change one if you prefer.
5. „google ads специалист“ is NOT used. The canon says only "a real marketing specialist", and calling him a Google Ads specialist implies a specialisation or certification. Add it (eyebrow or specialist paragraph) only if the owner confirms. „google ads управление“ is used as „управление на Google Ads“ (meta) and „управлява кампаниите в Google Ads“ (body).
6. The /reklama/ H1 uses Latin „Google“, while the title, lead and H2 use „Гугъл“. Keep this or use one form.
7. The /reklama/ section id `facebook-instagram` is kept (ids are fixed by the inventory), although the heading is now „Кампании извън Google“. Rename it when porting if wanted.
8. Under R2, the approved phrase „без да Ви е нужен дизайнер на щат“ was dropped from /reklama/. Confirm. It still lives on /socialni-mrezhi/ if that page carries it.
9. keyword-map.md still lists the old /reklama/ H1 „Реклама в Google и Facebook с маркетинг специалист“. Update it to „Реклама в Google с маркетинг специалист“ (not edited here).
10. Optional: on /reklama/, „ключови думи“ in `kak-raboti` could link to /saveti/klyuchovi-dumi/.
11. The open owner items from the original /reklama/ run still apply (whose ad account, minimum budget, whether ad spend is separate from the fee, the pricing model of ongoing work, diagnosis scope, F1 to F3 source confirmation).
