# 06-verification: /socialni-mrezhi/ (bg) · Step 6 (2026-11-15)

Inputs: 05b-final-draft.md, 00-current.md, 00-inventory.md, 05-gate-report.md (OWNER ITEMS), 00-brief.md, 01-synthesis.md (excluded claims).
Deliverables: `content/socialni-mrezhi.md` (Markdown + TOML porting source), `content/socialni-mrezhi.port.json` (ContentPage).

## RESOLVED-TO-OWNER-ITEMS

### V1 [VERIFY] Google Business Profile definition (#google-profil): CONFIRMED, sentence kept
- Claim kept: „Google Business профилът е информацията за Вашия бизнес, която клиентите виждат в Google Търсене и Google Maps.“
- URL: https://www.google.com/business/ (`curl -sIL`: 302 consent → 303 → 301 → **HTTP/2 200** at https://business.google.com/en-all/business-profile/; Google's own product page, Tier B).
- Quotes (fetched page text, 2026-11-15):
  - „Stand out on Google with a free Business Profile. Take control of how your free Business Profile appears on Google Search and Maps“
  - „Google Business Profile: List your business on Search and Maps“
  - „Be found when people are searching on Google Maps and Search for businesses just like yours“
- Added to `[[sources]]` (checked_by/checked_on empty) and `[[owner_items]]` #1.

### OWNER CONFIRM flags → `[[owner_items]]` (markers removed, only known text kept)
| # | flag | where | text kept on page |
|---|---|---|---|
| 2 | F1 posting cadence / posts per month | #publikacii, FAQ 4 | „Честотата … се уточняват в доклада след диагностиката“ (gate: process inference covered by F1) |
| 3 | F2 which networks the tool publishes to | #publikacii, FAQ 5 | „Конкретните мрежи се уточняват след диагностиката“ (covered by F2) |
| 4 | F3 community management (replies to comments) | FAQ 8 | not promised; FAQ 8 points to /ai-asistent/ for messages |
| 5 | F4 Google review replies: this service or /ai-asistent/ | #google-profil | canon capability kept: watching ratings/comments in Google and preparing a reply for approval; owner decides removal |
| 6 | Gate note on F4: does BizGrow publish the approved reply itself? | #google-profil | text states only preparing a reply for approval |
| 7 | F5 pricing of ongoing monthly work under the one-off price model | #cena, FAQ 2 | canon wording only |
| 8 | F6 H1 change: „Поддръжка на социални мрежи и криейтиви“ → „Маркетинг в социалните мрежи: поддръжка и криейтиви“ | H1 | Step 4 H1 kept; keyword-map h1 update only if approved |

Step 6 item 3 extra entries: „ти“→„Вие“ conversion of a heading or CTA: none (no heading/CTA taken from the „ти“-form checker; the CTA is the approved „Запазете безплатна диагностика“). Example scenarios kept: none.

## REMAINING FOR HUMAN
- No `[LINK NEEDED]` markers. No unreachable/disagreeing sources.
- Not added as owner items (01-synthesis.md logged them only under "Excluded claims", not as OWNER CONFIRM): „без дизайнер на щат“ (synthesis: "Left out; the owner may add it back"), „без да наемаш екип“ / „присъствие като на голям бранд“, „с едно докосване“. If the owner wants any back, it re-enters at Stage 2 with the comparative-claim rules.
- Self-check tooling: system `python3` is 3.9.6 (no `tomllib`); checks ran with `/opt/homebrew/bin/python3.14`.

## PORTING NOTES
- Target: new file `site/src/content/pages/bg/socialni-mrezhi.ts` exporting a `ContentPage` (same pattern as `seo-statii.ts`), registered in `site/src/content/index.ts`. Copy `content/socialni-mrezhi.port.json` verbatim. No `Dictionary` (`site/src/i18n/types.ts`) keys change and no new keys are needed; every `dictionary_key` in the content file is "" because the copy lives in the ContentPage object, not the dictionaries.
- Hero: `[[sections]]` entry `hero` maps to `h1` + `lead` (+ `eyebrow`, `label`, `summary`, `service`, `related`, stored as extra top-level front-matter keys). The port JSON `sections[]` holds only the 8 H2 sections.
- Tokens: per the orchestrator's syntax update and confirmed in the site source (`site/src/content/types.ts` doc comment; `components/RichText.tsx` replaces `{{BOOKING_URL}}` with `site.bookingUrl` inside `[label](…)` and prints a bare `{{EMAIL}}` as a `mailto:` link), the #kontakt strings keep `[Запазете безплатна диагностика]({{BOOKING_URL}})` and `{{EMAIL}}` exactly as in the content file.
- Booking CTA duplication: `components/ContentPageView.tsx` already renders a `BookingLink` button (`t.nav.cta`) and a „/diagnostika/“ button under the lead, plus `CtaBand` at the end of the page. The in-section CTA in #kontakt is therefore an extra text link (same as `seo-statii.ts`); the porter may keep it (inventory item 1 requires it in the content) or let the template's buttons carry it, as an owner/porter choice.
- #proces uses `steps` (ordered list). `ContentPageView` renders all paragraphs before steps, so the closing paragraph („Ако искате първо да прецените сами, [безплатната диагностика](/diagnostika/) …“) shows above the numbered list instead of after it. Wording unchanged; it reads correctly in either position.
- #za-kogo and #cena use `bullets`. Bullet „**Title.** Body.“ uses `**bold**` only.
- `status` = "published" in the port JSON as instructed by the orchestrator; the content file stays `status = "draft"`. The owner's approval is still pending (8 owner items).
- `related`: /seo-statii/, /reklama/, /diagnostika/; `ContentPageView` shows a related card only for pages that exist in `getPages`, so cards appear once those pages are ported.
- `[[sources]]` is not rendered; the human decides whether to show the Google source.

## SELF-CHECK (content file + port JSON; Python 3.14 tomllib/json)
| check | result | detail |
|---|---|---|
| TOML parses | PASS | 9 sections, 8 faq, 1 source, 8 owner_items |
| port JSON parses (json.load) | PASS | |
| primary_keyword = keyword-map term | PASS | „маркетинг в социалните мрежи“ |
| title ≤ 60 incl. „ \| BizGrow“, no em-dash | PASS | 50 chars |
| meta_description 120–160, contains main term | PASS | 149 chars |
| main term once in title / H1 / first 100 words / one H2 | PASS | H2 = #proces „Маркетинг в социалните мрежи стъпка по стъпка“ |
| `[[sections]]` ids + headings = body blocks, same order | PASS | 9 blocks (hero + 8 H2) |
| zero em-dash / en-dash (md + json) | PASS | 0 / 0 |
| zero bracketed markers; no `[` outside Markdown links | PASS | md values + body, all JSON strings |
| JSON: no `{` except `{{BOOKING_URL}}` / `{{EMAIL}}` | PASS | |
| zero „ти“ forms | PASS (manual) | regex flagged „Те са описани“ twice (md + json): 3rd-person plural subject „They“, not a „ти“ form; 0 lowercase ви/вас/ваш |
| zero banned claims / hype (site-rules §2) | PASS | безплатн* only with диагностика |
| zero PRICE / OFFER / TESTIMONIAL | PASS | |
| numbers canon / labelled / sourced | PASS | digits 2, 30, 48 (canon) |
| example scenarios labelled | N/A | none used |
| inventory 17/17 | PASS | see below |
| links only from conversion-links.md | PASS | /seo-statii/, /reklama/, /diagnostika/, /ai-asistent/, {{BOOKING_URL}} |
| CTA via {{BOOKING_URL}} (1), email via {{EMAIL}} (1) | PASS | #kontakt |
| related = 3 siblings (not /, not itself) | PASS | |
| JSON strings identical to content file | PASS | meta, h1, lead, sections, faq |
| sources/owner decision fields empty | PASS | |

Result: 51/51 PASS (1 regex hit resolved manually as a false positive). No stage failure.

### Inventory (00-inventory.md, 17 items)
1. „[Запазете безплатна диагностика]({{BOOKING_URL}})“ (#kontakt) · 2. „изпратете ни имейл на {{EMAIL}}“ · 3. „[Реклама в Google и Facebook](/reklama/)“ (#platena-reklama, FAQ 6) · 4. „[безплатната диагностика](/diagnostika/)“ (#proces) · 5. „[SEO статии и копирайтинг](/seo-statii/)“ · 6. „пише текста на публикацията, създава изображение към нея и я публикува в социалните мрежи по предварително зададен график“ · 7. „В профилите Ви излиза само съдържание, което Вие сте одобрили.“ · 8. „Всеки месец подготвяме брандирани визии, публикации и рекламни материали“ · 9. „Криейтиви и рекламни визии всеки месец“ / „подходящи … и за реклама“ · 10. „Поддържаме профила актуален всеки месец: добавяме публикации, нови снимки и текуща информация“ · 11. „30-минутен разговор“, „Доклад до 48 часа … приоритизирани решения и ясни еднократни цени“, „обикновено до 2 седмици“, „кратък месечен отчет“ · 12. „Работим без дългосрочни договори.“, „Цените са прозрачни“, „Работим по GDPR.“ · 13. „Цената зависи от това, какво изграждаме … в доклада след безплатната диагностика“ · 14. digits 30, 48, 2 only · 15. no example scenarios · 16. 8 FAQ, price FAQ without a number · 17. 8 H2, service „Поддръжка на социални мрежи и криейтиви“, H1 change → owner item F6.

### Counts
- Body word count (H1 + lead + section headings and text, excluding FAQ and front matter): **672**
- H2 sections: 8 · FAQ: 8 · body links: 3 + FAQ links 2 (/reklama/, /ai-asistent/) · booking CTA: 1 · {{EMAIL}}: 1
- new facts: 1
- owner items added: 8
