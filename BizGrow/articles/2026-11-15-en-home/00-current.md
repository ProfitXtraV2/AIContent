# 00-current — /en/ (en) en-home, verbatim

Source: desislavamit/biz-grow @ feature/seo-improvements (local ~/Work/biz-grow-seo), commit 528ad25c3b7be5a9a48d38740ab1bc955512d2a9, read 2026-11-15.
Files: site/src/i18n/dictionaries/en.ts (copy, verbatim below); type site/src/i18n/types.ts; rendered by site/src/components/HomePage.tsx (order: Hero, Losses, Services, Process, Results, Reasons, CtaBand, Contact, Footer), Sections.tsx, Contact.tsx, HeroVisual.tsx. Same components as the Bulgarian home page.

Render notes (from components, identical to the bg home page):
- #hero: H1 = hero.line1 + hero.line2; hero.body; primary CTA hero.primary -> BookingLink ({{BOOKING_URL}}, new tab); secondary hero.secondary -> #services; figures = metrics[] (aria-label a11y.results); HeroVisual overlay = overlayLabel + overlayUnit (no overlayValue).
- #losses: losses.title + items[] (optional link, new in types.ts). #services: services.title + items[] {icon,title,body,href?}. #process: title, lead, steps[]. #results: title, note (label), rows[]. #reasons: title, lead, items[]. #audit: cta.title, cta.body, cta.button -> BookingLink. #contact: contact.title, contact.book -> BookingLink, emailBefore + mailto {{EMAIL}}, form fields, submit (mailto with subject mailSubject).
- Nav links #services #process #contact, nav.cta -> BookingLink. Footer links #services #process #contact, email, privacy (hidden).
- The English site has NO content/service pages: all routes under site/src/app/(en)/ are the home page only.

```ts
import type { Dictionary } from "../types";

export const en: Dictionary = {
  meta: {
    title: "BizGrow — Find where the business loses time",
    description:
      "A free diagnosis of your business, exactly which AI fixes are worth it, and we build them for you — in days, not months.",
    ogTitle: "BizGrow — Find where you lose time. Then fix it with AI.",
    ogDescription: "A free diagnosis. No obligation. We build the solution in days, not months.",
    ogLocale: "en_US",
  },
  a11y: {
    skipToContent: "Skip to content",
    primaryNav: "Primary",
    home: "BizGrow home",
    openMenu: "Open menu",
    closeMenu: "Close menu",
    newTab: "(opens in a new tab)",
    language: "Language",
    results: "Free diagnosis",
    step: "Step",
    breadcrumb: "Breadcrumb",
  },
  page: {
    home: "Home",
    faq: "Frequently asked questions",
    related: "Related services",
    diagnosis: "Free diagnosis",
  },
  nav: {
    links: [
      { label: "Services", href: "#services" },
      { label: "Process", href: "#process" },
      { label: "Contact us", href: "#contact" },
    ],
    cta: "Book a call",
  },
  hero: {
    line1: "Less busywork.",
    line2: "More business.",
    body: "A free diagnosis of your business, exactly which AI fixes are worth it, and we build them for you — in days, not months.",
    primary: "Free diagnosis",
    secondary: "Explore services",
    imageSrc: "/bizgrow-banner.webp",
    imageAlt:
      "BizGrow — AI and automation for small businesses: integrate AI, automate workflows, save time and costs, grow your business.",
    overlayLabel: "Free diagnosis",
    overlayUnit: "in days, not months",
  },
  metrics: [
    { value: "8", caption: "short questions" },
    { value: "2 min", caption: "to fill in", label: "2 minutes" },
    { value: "0", caption: "obligation" },
  ],
  losses: {
    title: "Every day you lose customers and hours",
    items: [
      "Missed calls and messages after working hours",
      "Hours lost writing quotes and invoices by hand",
      "Nobody replies in time on Messenger, Instagram or WhatsApp",
      "No time for content and social networks, while competitors grow",
      "You don't know which numbers in the business actually matter",
    ],
  },
  services: {
    title: "Whatever is costing you time",
    items: [
      {
        icon: "loop",
        title: "Automations",
        body: "Chatbots, bookings, invoicing.",
      },
      {
        icon: "spark",
        title: "SEO copywriting",
        body: "Content that gets you into Google.",
      },
      {
        icon: "brain",
        title: "Creatives",
        body: "Posts and ads every month.",
      },
      {
        icon: "spark",
        title: "Custom solutions",
        body: "Built exactly for your business.",
      },
    ],
  },
  process: {
    title: "Three steps to a working solution",
    lead: "From a conversation to a solution that works.",
    steps: [
      {
        n: "1",
        label: "Diagnosis",
        title: "Where time and money leak",
        body: "You fill in a free 2-minute AI diagnosis of the site. Then a 30-minute conversation where we find exactly where the business loses money.",
      },
      {
        n: "2",
        label: "Build",
        title: "A clear one-time price",
        body: "A report with prioritised solutions and clear prices within 48 hours. We build that specific AI solution, usually within 2 weeks.",
      },
      {
        n: "3",
        label: "Support",
        title: "A transparent report every month",
        body: "We watch the solution and improve it. Every month you get a short report of what was done.",
      },
    ],
  },
  results: {
    title: "What the result looks like",
    note: "Example scenarios from our method, not figures from specific clients.",
    rows: [
      {
        business: "Restaurant",
        problem: "Nobody picks up at peak hours.",
        outcome: "Bookings 24/7, about 10 hours less manual work a week.",
      },
      {
        business: "Online shop",
        problem: "Questions about deliveries sit unanswered for hours.",
        outcome: "80% of the repeated questions answered in seconds.",
      },
      {
        business: "Dental clinic",
        problem: "Missed calls and appointments moved around.",
        outcome: "Online booking at any time.",
      },
    ],
  },
  reasons: {
    title: "The little “extra” that changes the result",
    lead: "No jargon, and no solutions “just in case”. Only tools that work, shaped to your business.",
    items: ["We work under GDPR", "No long-term contracts", "Transparent prices", "A result before a large investment"],
  },
  cta: {
    title: "The first step is free",
    body: "The diagnosis commits you to nothing. We show you exactly what we can fix and what it will cost.",
    button: "Book a free diagnosis",
  },
  contact: {
    title: "Contact us",
    book: "Book a video call now",
    emailBefore: "Send us an email at",
    fields: {
      name: "Names",
      email: "Email",
      description: "Description",
    },
    submit: "Submit",
    mailSubject: "BizGrow message from",
  },
  footer: {
    descriptor: "We find where the business loses time and fix it with AI.",
    services: "Services",
    process: "Process",
    contact: "Contact us",
    privacy: "Privacy",
    rights: "All rights reserved.",
  },
};
```
