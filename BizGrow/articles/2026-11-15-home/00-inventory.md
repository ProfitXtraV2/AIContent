# 00-inventory — / (bg) home

Source: `00-current.md` (biz-grow @ feature/seo-improvements, 528ad25). Every item must survive
every editing stage with the same meaning (reworded into „Вие“ allowed), unless listed under
REMOVE-BY-BRIEF (owner/owner's session 2026-11-15, see `00-brief.md`).

## CTAs (6)
- C1 nav.cta „Запазете час“ → {{BOOKING_URL}}
- C2 hero.primary „Безплатна диагностика“ → {{BOOKING_URL}} (stays booking, per brief)
- C3 hero.secondary „Разгледайте услугите“ → #services
- C4 cta.button „Запазете безплатна диагностика“ → {{BOOKING_URL}} (#audit)
- C5 contact.book „Запазете видеоразговор сега“ → {{BOOKING_URL}}
- C6 contact.submit „Изпратете“ (form → mailto {{EMAIL}}) + contact.emailBefore „Изпратете ни имейл на“

## Tokens (2)
- T1 {{BOOKING_URL}} (C1, C2, C4, C5)
- T2 {{EMAIL}} (contact block, form, footer)

## Anchors (8)
- #hero, #losses, #services, #process, #results, #reasons, #audit, #contact (nav: #services, #process, #contact; footer same). #top on wrapper.

## Canon facts (9)
- F1 Free diagnosis (безплатна диагностика) — hero, a11y.results, overlayLabel, cta
- F2 30-minute call (30-минутен разговор) — process step 1
- F3 Report with prioritised fixes and clear prices within 48 hours — process step 2
- F4 Build, usually up to 2 weeks („обикновено до 2 седмици“) — process step 2
- F5 Monthly support with a short report — process step 3 („Прозрачен отчет всеки месец“, „кратък отчет“)
- F6 One-off price („Ясна еднократна цена“) — process step 2 title
- F7 „Работим по GDPR“ — reasons
- F8 „Без дългосрочни договори“, „Прозрачни цени“ — reasons
- F9 Diagnosis commits to nothing („не те обвързва с нищо“, metrics „0 обвързване“); „Показваме ти точно какво можем да оправим и колко ще струва“ — cta.body
- (also) Services: automations (chatbots, bookings, invoicing), SEO copywriting, creatives (posts and ads monthly), custom solutions; BizGrow finds where the business loses time and fixes it with AI (footer.descriptor)

## Numbers (8)
- N1 metrics „8 кратки въпроса“ — REMOVE-BY-BRIEF (questionnaire no longer exists; owner decision 2026-11-15)
- N2 metrics „2 мин / за попълване / 2 минути“ — REMOVE-BY-BRIEF (same)
- N3 metrics „0 обвързване“ — keep
- N4 30-минутен — keep; N5 48 часа — keep; N6 до 2 седмици — keep (with „обикновено“)
- N7 results „около 10 часа седмично“, „24/7“ (restaurant) — inside labelled hypothetical example; [OWNER CONFIRM] per canon
- N8 results „80%“ (online shop) — inside labelled hypothetical example; [OWNER CONFIRM] per canon

## Labels (2)
- L1 results.note „Примерни сценарии по нашия метод, не данни от конкретни клиенти.“ — must stay in #results
- L2 „за дни, не месеци“ (hero.body, meta, ogDescription, overlayUnit) — keep only with [OWNER CONFIRM] (canon)

## Example rows (3, hypothetical)
- E1 Ресторант / Никой не вдига в пиковите часове / Резервации 24/7, около 10 часа седмично по-малко ръчна работа.
- E2 Онлайн магазин / Въпроси за пратки остават без отговор с часове / 80% от повтарящите се въпроси с отговор за секунди.
- E3 Дентална клиника / Пропуснати обаждания и разместени часове / Онлайн записване по всяко време.

## Losses (5)
- missed calls/messages after hours; hours on hand-written offers and invoices; no timely reply in Messenger/Instagram/WhatsApp; no time for content and social media while competitors grow; not knowing which business metrics matter

## Reasons (4)
- Работим по GDPR; Без дългосрочни договори; Прозрачни цени; Резултат преди голяма инвестиция

## FAQ (0)
- The current home page has no FAQ. Brief adds one (5–7 questions).

## UI strings to keep (a11y, page, contact.fields, footer)
- a11y.* (10 keys), page.* (4 keys), contact.fields name/email/description, contact.mailSubject, footer.* (6 keys), hero.imageSrc, hero.imageAlt (contains an em-dash → reword), meta.ogLocale.

## REMOVE-BY-BRIEF (owner / owner's session 2026-11-15)
- N1, N2 and process step 1 „Попълваш безплатната 2-минутна AI диагностика на сайта“ → replaced by the free diagnosis page /diagnostika/ and canon figures.
- Services card „Решения по поръчка“ and the four-card set → replaced by six cards, one per service page (site-rules §5, brief).
- #ads section — already removed upstream.
