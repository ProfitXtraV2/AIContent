# 00-current — /seo-optimizacia/ (new page)

Source: desislavamit/biz-grow @ feature/seo-improvements, commit 528ad25c3b7be5a9a48d38740ab1bc955512d2a9.

There is NO current copy for /seo-optimizacia/: the page does not exist yet
(`site/src/content/index.ts` registers only a temporary test fixture `_sample.ts`).

Site context the new page sits in (verbatim, for reference only, not inventory):
- Home services card (bg.ts `services.items[1]`): title „SEO копирайтинг“, body „Съдържание, което те извежда в Google.“ (this card belongs to /seo-statii/, not to this page; „ти“-era wording).
- Page template strings (bg.ts `page`): „Начало“, „Често задавани въпроси“, „Свързани услуги“, „Безплатна диагностика“; nav CTA „Запазете час“.
- Template `ContentPageView.tsx` renders: breadcrumb (label), eyebrow, H1, lead, booking button „Запазете час“ ({{BOOKING_URL}} via BookingLink), button „Безплатна диагностика“ → /diagnostika/, sections, FAQ, related, CTA band.
