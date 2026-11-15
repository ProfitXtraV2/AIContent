# 04 · Step 4 SEO: follow-up 2026-11-15 (items A, B, C)

Inputs: 03-humanised/{saveti,home-cards,reklama}.json, baseline `_tmp/reklama.current.json`, keyword-map.md, conversion-links.md, site-rules.md §6, markets/bg/author.md.
Counts and term matches were made with a script (Python `len()` on the JSON strings; regex term scan over every string field, all keyword-map main terms plus the /reklama-vav-facebook/ cluster). Checks on all outputs: em/en-dashes 0, „ти“ forms 0, prices 0, delivery periods 0, guarantees 0, JSON keys/ids/hrefs/tokens unchanged (reklama key structure compared programmatically: identical).

Outputs: 04-seo/saveti.json (unchanged copy), 04-seo/home-cards.json (unchanged copy), 04-seo/reklama.json (2 edits).

---

## A. /saveti/ (hub)

```
SEO AUDIT: /saveti/ (bg)
Main term: none (hub, keyword-map primary „—“) | Intent: navigational/informational
Placement: n/a. Check instead: no other address's main term targeted.
Relevance score: 90/100 (alignment 25 | entities 30 | questions 20 | on-page 15)
MISSING ENTITIES: none required for a hub (the site lists the articles itself)
DEFECTS: none
LINKS: /diagnostika/ in lead (from conversion-links); related /avtomatizacii/, /seo-statii/, /seo-optimizacia/
FAQ CANDIDATES: none (faq [] by inventory)
```

| Field | Value | Chars | Limit | OK |
|---|---|---|---|---|
| meta.title | Съвети за малкия бизнес: AI, SEO и реклама \| BizGrow | 52 | ≤ 60 | yes |
| meta.description | Практични съвети за собственици на малък бизнес: AI и автоматизации, SEO, съдържание и реклама, обяснени с ясни думи и конкретни стъпки. | 136 | 120–160 | yes |
| summary | Практични съвети за малкия бизнес за AI, автоматизации, SEO, съдържание и реклама. | 82 | ≤ 160 | yes |

Cannibalisation scan (title, meta, summary, h1, eyebrow, lead): 0 matches for „ai автоматизация“ (only „AI и автоматизации“ / „AI, автоматизации“, topic words, not the term), „seo оптимизация“, „реклама в гугъл/google“, „seo копирайтинг“, „ai асистент“, „автоматизация на бизнес процеси“, „маркетинг в социалните мрежи“, „изработка на сайт/онлайн магазин“, Facebook cluster, and the three article terms („копирайтър“, „бизнес профил в гугъл“, „ключови думи“). „SEO“ and „реклама“ appear only as topic words.
Note: h1 „Съвети за малкия бизнес“ extends the keyword-map h1 „Съвети“; acceptable for a hub, no change.

Change list: none.

---

## B. Home service cards + nav

```
SEO AUDIT: / #services cards (bg)
Main term of /: „ai автоматизация“ | services_title keeps it (already in the live title; no new instance added)
Relevance score: 92/100
DEFECTS: none
```

| Card | Term matched | Assessment |
|---|---|---|
| AI асистент и чатбот | „ai асистент“ (title) | names the service, links to its own page; unchanged live card |
| Изработка на сайт | „изработка на сайт“ (title) | names the service, links to /izrabotka-na-sait/; supports that page; body has no term repeat |
| Онлайн магазини | none | no stuffing („изработка на онлайн магазин“ not repeated) |
| SEO оптимизация | „seo оптимизация“ (title) | unchanged live card, links to own page |
| Реклама в Google | „реклама в google“ (title) | one instance, body uses „рекламите Ви в Google“ (not the term) |
| Реклама във Facebook и Instagram | title + body „платените Ви реклами във Facebook и Instagram“ | links to /reklama-vav-facebook/, so it supports that page; 2 mentions in a 2-sentence card is the service name plus a natural description, not stuffing |
| services_title | „AI автоматизация, сайтове, съдържание и реклама на едно място“ (61 chars) | home's own main term, already present in the live title; only „сайтове“ added |

Nav: „Съвети“ → /saveti/ placed between „Процес“ and „Свържете се с нас“; other links unchanged.
Change list: none.

---

## C. /reklama/ (minimal Google-only edit)

```
SEO AUDIT: /reklama/ (bg)
Main term: „реклама в гугъл“ | Intent: commercial + informational
Placement: title Y | H1 Y (Latin „Google“) | first 100 words Y | H2 Y („Как работи рекламата в Гугъл за малък бизнес“) | meta Y
Relevance score: 88/100 (alignment 23 | entities 31 | questions 22 | on-page 12 → 14 after edits)
DEFECTS (fixed): /reklama-vav-facebook/ term phrase „Рекламата във Facebook и Instagram“ written next to an identical anchor twice (section facebook-instagram, FAQ 6) → body phrase de-flooded, anchors kept
MISSING ENTITIES: none the canon can cover beyond what is present
UNANSWERED QUESTIONS: none new (price, position, PPC, reporting, visuals, channel, contract, timing already answered)
LINKS TO ADD: none
```

### Character counts

| Field | Chars | Limit | OK |
|---|---|---|---|
| meta.title „Реклама в Гугъл с маркетинг специалист \| BizGrow“ | 48 | ≤ 60 | yes |
| meta.description „Реклама в Гугъл и управление на Google Ads от маркетинг специалист, който планира, пуска, следи и отчита с числа. Безплатна диагностика и оферта с ясни цени.“ | 157 | 120–160 | yes, contains main term |
| summary | 121 | ≤ 160 | yes |
| lead | 39 words (whole lead within first 100 words) | | main term in sentence 1 |

### Placement table

| Term | Title | Meta | H1 | First 100 | H2 | Body / FAQ | Status |
|---|---|---|---|---|---|---|---|
| реклама в гугъл (main) | 1 | 1 | 1 (Google) | 1 (lead s1) | 1 (kak-raboti) | label/service „Реклама в Google“ (UI fields); FAQ 1 „рекламата в Google Ads“ | once each, no flood |
| google ads управление (sec.) | 0 | 1 („управление на Google Ads“) | 0 | 0 | 0 | specialist p1 „управлява кампаниите в Google Ads“ | natural phrase variant |
| google ads специалист (sec.) | 0 | 0 | 0 | 0 | 0 | 0 | NOT used, owner item O1 |
| гугъл реклама | | | | | | kak-raboti p1 „Гугъл реклама“ | present |
| google ads реклама / google реклама | | | | | | eyebrow „Google Ads с маркетинг специалист“, summary „Кампании в Google Ads“ | present as variants |
| ppc реклама | | | | | | kak-raboti p1, FAQ 3 | present |
| онлайн реклама | | | | | | za-kogo p1 | present |
| маркетинг специалист | 1 | 1 | 1 | 1 | 1 | throughout | secondary, canon |
| /reklama-vav-facebook/ cluster | 0 | 0 | 0 | 0 | 0 („Кампании извън Google“) | anchors only: section facebook-instagram, FAQ 6 (+ FAQ 6 question, inventory wording „рекламирам … във Facebook и Instagram“) | zero targeting |

Label „Реклама в Google“, summary and service: no Facebook/Instagram terms. Other addresses' main terms: „seo оптимизация“ only inside the anchor to /seo-optimizacia/ (passing mention with link, fine); „ключови думи“ (main term of /saveti/klyuchovi-dumi/) appears once as a jargon explanation in kak-raboti p2 (owner-approved string, not targeted; see O3).

### Change list (reklama)

1. sections[2].paragraphs[0], s1: „Рекламата във Facebook и Instagram е отделна услуга, описана на страницата [реклама във Facebook и Instagram](/reklama-vav-facebook/)“ → „Кампаниите във Facebook и Instagram са отделна услуга, описана на страницата [реклама във Facebook и Instagram](/reklama-vav-facebook/)“. Reason: the other page's term was written twice in one sentence; the anchor keeps it as a link, the body no longer repeats it.
2. faq[5].answer, s3: „Рекламата във Facebook и Instagram е описана на страницата […]“ → „Кампаниите във Facebook и Instagram са описани на страницата […]“. Same reason; link unchanged.
3. Nothing else touched: title, meta, H1, lead, H2s, label, summary, eyebrow, service, related kept as Step 3 left them (all within limits).

Secondary keywords used: гугъл реклама, ppc реклама, онлайн реклама, google ads управление (as „управление на Google Ads“), маркетинг специалист, Google Ads variants.
FAQ list: 8, questions unchanged (see below).

### Inventory diff (04-seo/reklama.json)

| Item | Present | Where |
|---|---|---|
| C1 | yes | proces: „[Запазете безплатна диагностика]({{BOOKING_URL}})“ |
| C2 | yes | diagnostika: „[Запазете час]({{BOOKING_URL}})“ |
| C3 | yes | diagnostika: „… или да ни пишете на {{EMAIL}}.“ |
| C4 | yes | proces step 1: „[безплатна диагностика](/diagnostika/)“ |
| C5 | yes | kak-raboti p4: „[SEO оптимизация на сайтове](/seo-optimizacia/)“ |
| C6 | yes | facebook-instagram p1 + FAQ 5 → /socialni-mrezhi/ |
| C7 | yes | lead: „жив маркетинг специалист планира, пуска и следи вместо Вас“ |
| C8 | yes | lead, otchet, FAQ 4 |
| C9 | yes | lead, summary, „Проследяване“ bullet, otchet, FAQ 4 |
| C10 | yes | specialist p1: „поема планирането и изпълнението, а при Вас остава отчетът“ |
| C11 | yes | „Кампании на база данни“ bullet |
| C12 | yes | facebook-instagram p1 („Брандирани визии, публикации и рекламни материали … всеки месец“) + FAQ 5 |
| C13 | yes | za-kogo: three „подходящо, ако“ situations + 6 bullets |
| C14 | yes | proces steps 1–4, „оферта“, no delivery period |
| C15 | yes | cena p1 + FAQ 1 |
| C16 | yes | lead, cena, FAQ 7 |
| C17 | yes | cena: „Работим по GDPR.“ |
| C18 | yes | FAQ 8 |
| C19 | yes | kak-raboti p1, cena p2, FAQ 1, FAQ 3 |
| C20 | yes | kak-raboti p2, cena p2, FAQ 1 |
| C21 | yes | kak-raboti p3, FAQ 2 |
| C22 | yes | kak-raboti p1 (PPC), p4 (SEO separate), FAQ 3 |
| Section ids | yes | specialist, kak-raboti, facebook-instagram, za-kogo, otchet, proces, cena, diagnostika |
| Tokens/links | yes | {{BOOKING_URL}} ×2, {{EMAIL}} ×1, /diagnostika/ ×1, /seo-optimizacia/ ×1, /socialni-mrezhi/ ×2, /reklama-vav-facebook/ ×2 |
| R1–R4 | applied | unchanged from Step 3 |

FAQ (8, questions verbatim):
1. Колко струва рекламата в Google Ads? (yes, unchanged)
2. Ако платя повече, ще се показва ли рекламата ми най-отгоре? (yes, unchanged)
3. Какво е PPC реклама? (yes, unchanged)
4. Как ще видя дали рекламата ми носи клиенти? (yes, unchanged)
5. Кой подготвя визиите за рекламите? (yes, unchanged)
6. По-добре ли е да рекламирам в Google или във Facebook и Instagram? (yes, answer s3 edited, link kept)
7. Трябва ли да подпиша дългосрочен договор? (yes, unchanged)
8. Колко време отнема, докато започнем? (yes, unchanged)

---

## Owner items

- O1. „google ads специалист“ (20/mo) is not used. The canon says a real marketing specialist plans, runs and tracks the ads; calling him a „Google Ads специалист“ could read as a platform specialisation or certification the canon does not state. If the owner confirms the wording, the natural spot is the eyebrow („Google Ads специалист“) or specialist p1.
- O2. H1 uses the Latin „Google“ while title/lead/H2 use „Гугъл“ (accepted as before); the owner may choose one script for the H1.
- O3. kak-raboti p2 explains „ключови думи“ (main term of /saveti/klyuchovi-dumi/) in passing. Not targeted; if the owner wants, the phrase could link to /saveti/klyuchovi-dumi/ once that article is live (owner-approved string, so not changed here).
