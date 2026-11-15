# 00-current — / (bg) home, verbatim

Source: desislavamit/biz-grow @ feature/seo-improvements (local ~/Work/biz-grow-seo), commit 528ad25c3b7be5a9a48d38740ab1bc955512d2a9, read 2026-11-15.
Files: site/src/i18n/dictionaries/bg.ts (copy, verbatim below); rendered by site/src/components/HomePage.tsx (order: Hero, Losses, Services, Process, Results, Reasons, CtaBand, Contact, Footer), Sections.tsx, Contact.tsx, HeroVisual.tsx.

Render notes (from components):
- #hero: H1 = hero.line1 + hero.line2; hero.body; primary CTA hero.primary -> BookingLink ({{BOOKING_URL}}, new tab); secondary hero.secondary -> #services; figures = metrics[] (aria-label a11y.results); HeroVisual overlay = overlayLabel + overlayUnit (no overlayValue).
- #losses: losses.title + items[]. #services: services.title + items[] {icon,title,body} (no link today). #process: title, lead, steps[]. #results: title, note (label), rows[]. #reasons: title, lead, items[]. #audit: cta.title, cta.body, cta.button -> BookingLink. #contact: contact.title, contact.book -> BookingLink, emailBefore + mailto {{EMAIL}}, form fields, submit (mailto with subject mailSubject).
- Nav links #services #process #contact, nav.cta -> BookingLink. Footer links #services #process #contact, email, privacy (hidden).

```ts
import type { Dictionary } from "../types";

export const bg: Dictionary = {
  meta: {
    title: "BizGrow — Открий къде бизнесът губи време",
    description:
      "Безплатна диагностика на бизнеса ти, точно кои AI решения си заслужават, и изграждането им вместо теб — за дни, не месеци.",
    ogTitle: "BizGrow — Открий къде губиш време. После го поправи с AI.",
    ogDescription: "Безплатна диагностика. Без обвързване. Изграждаме решението за дни, не месеци.",
    ogLocale: "bg_BG",
  },
  a11y: {
    skipToContent: "Към съдържанието",
    primaryNav: "Основна навигация",
    home: "BizGrow – начало",
    openMenu: "Отваряне на менюто",
    closeMenu: "Затваряне на менюто",
    newTab: "(отваря се в нов раздел)",
    language: "Език",
    results: "Безплатна диагностика",
    step: "Стъпка",
    breadcrumb: "Навигационна пътека",
  },
  page: {
    home: "Начало",
    faq: "Често задавани въпроси",
    related: "Свързани услуги",
    diagnosis: "Безплатна диагностика",
  },
  nav: {
    links: [
      { label: "Услуги", href: "#services" },
      { label: "Процес", href: "#process" },
      { label: "Свържете се с нас", href: "#contact" },
    ],
    cta: "Запазете час",
  },
  hero: {
    line1: "По-малко рутина.",
    line2: "Повече бизнес.",
    body: "Безплатна диагностика на бизнеса ти, точно кои AI решения си заслужават, и изграждането им вместо теб — за дни, не месеци.",
    primary: "Безплатна диагностика",
    secondary: "Разгледайте услугите",
    imageSrc: "/bizgrow-banner-bg.webp",
    imageAlt:
      "BizGrow — AI и автоматизация за малкия бизнес: внедряване на AI, автоматизирани процеси, спестено време и разходи, растеж на бизнеса.",
    overlayLabel: "Безплатна диагностика",
    overlayUnit: "за дни, не месеци",
  },
  metrics: [
    { value: "8", caption: "кратки въпроса" },
    { value: "2 мин", caption: "за попълване", label: "2 минути" },
    { value: "0", caption: "обвързване" },
  ],
  losses: {
    title: "Всеки ден губиш клиенти и часове",
    items: [
      "Пропуснати обаждания и съобщения след работно време",
      "Часове, изгубени в ръчно писане на оферти и фактури",
      "Никой не отговаря навреме в Messenger, Instagram или WhatsApp",
      "Нямаш време за съдържание и социални мрежи, а конкуренцията расте",
      "Не знаеш кои показатели на бизнеса ти всъщност имат значение",
    ],
  },
  services: {
    title: "Каквото и да ти губи време",
    items: [
      {
        icon: "loop",
        title: "Автоматизации",
        body: "Чатботове, резервации, фактуриране.",
      },
      {
        icon: "spark",
        title: "SEO копирайтинг",
        body: "Съдържание, което те извежда в Google.",
      },
      {
        icon: "brain",
        title: "Креативи",
        body: "Публикации и реклами всеки месец.",
      },
      {
        icon: "spark",
        title: "Решения по поръчка",
        body: "Изградени точно за твоя бизнес.",
      },
    ],
  },
  process: {
    title: "Три стъпки до работещо решение",
    lead: "От разговор до работещо решение.",
    steps: [
      {
        n: "1",
        label: "Диагноза",
        title: "Къде се губят време и пари",
        body: "Попълваш безплатната 2-минутна AI диагностика на сайта. После 30-минутен разговор, в който откриваме къде точно бизнесът ти губи пари.",
      },
      {
        n: "2",
        label: "Изграждане",
        title: "Ясна еднократна цена",
        body: "Доклад с приоритизирани решения и ясни цени до 48 часа. Изграждаме конкретното AI решение, обикновено до 2 седмици.",
      },
      {
        n: "3",
        label: "Поддръжка",
        title: "Прозрачен отчет всеки месец",
        body: "Следим и подобряваме решението. Всеки месец получаваш кратък отчет за свършеното.",
      },
    ],
  },
  results: {
    title: "Как изглежда резултатът",
    note: "Примерни сценарии по нашия метод, не данни от конкретни клиенти.",
    rows: [
      {
        business: "Ресторант",
        problem: "Никой не вдига в пиковите часове.",
        outcome: "Резервации 24/7, около 10 часа седмично по-малко ръчна работа.",
      },
      {
        business: "Онлайн магазин",
        problem: "Въпроси за пратки остават без отговор с часове.",
        outcome: "80% от повтарящите се въпроси с отговор за секунди.",
      },
      {
        business: "Дентална клиника",
        problem: "Пропуснати обаждания и разместени часове.",
        outcome: "Онлайн записване по всяко време.",
      },
    ],
  },
  reasons: {
    title: "Малкото „екстра“, което променя резултата",
    lead: "Без жаргон и без решения „за всеки случай“. Само работещи инструменти, съобразени с твоя бизнес.",
    items: [
      "Работим по GDPR",
      "Без дългосрочни договори",
      "Прозрачни цени",
      "Резултат преди голяма инвестиция",
    ],
  },
  cta: {
    title: "Първата стъпка е безплатна",
    body: "Диагностиката не те обвързва с нищо. Показваме ти точно какво можем да оправим и колко ще струва.",
    button: "Запазете безплатна диагностика",
  },
  contact: {
    title: "Свържете се с нас",
    book: "Запазете видеоразговор сега",
    emailBefore: "Изпратете ни имейл на",
    fields: {
      name: "Име",
      email: "Имейл",
      description: "Описание",
    },
    submit: "Изпратете",
    mailSubject: "Съобщение до BizGrow от",
  },
  footer: {
    descriptor: "Намираме къде бизнесът губи време и го поправяме с AI.",
    services: "Услуги",
    process: "Процес",
    contact: "Свържете се с нас",
    privacy: "Поверителност",
    rights: "Всички права запазени.",
  },
};
```
