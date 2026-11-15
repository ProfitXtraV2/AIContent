# Keyword Map — BizGrow (one main term per address)

Single source of truth for **which search term each address targets**. Filled by the owner's
session; empty at onboarding (2026-11-15). The pipeline reads it at Step 0 (brief), Step 4 (SEO)
and Step 5 (Brand Gate, one-term-per-page check). A page whose address has no row here is not
written.

Rules:
- One `primary_keyword` per address; no two addresses share a primary keyword.
- `secondary_keywords` are supporting terms for that page only; a term that is another address's
  primary keyword may not appear here.
- `status` ∈ live | planned | parked. A `new-page` is eligible for the pipeline only at `planned`
  (approved by the owner or the owner's session; record who/when in `notes`).
- Bulgarian and English pages are separate rows (`locale`), paired by `pair`.
- `volume`/`kd` from Ahrefs with the date; blank if not measured (never estimated).

| address | locale | pair | slug | primary_keyword | secondary_keywords | h1 | volume | kd | checked | status | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| / | bg | /en/ | home | ai автоматизация | автоматизация (150, KD 0); ai за бизнеса; изкуствен интелект в бизнеса (10); ai агенция (10); ai решения за бизнеса; автоматизация за малък бизнес | AI автоматизация за малкия бизнес | 40 |  | 2026-11-15 | planned | page-rewrite; owner's session 2026-11-15 |
| /en/ | en | / | en-home | ai automation for small business | ai automation agency, business automation | AI automation for small businesses |  |  |  | planned | page-rewrite after `/`; EN demand in BG not measured |
| /ai-asistent/ | bg |  | ai-asistent | ai асистент | ai чатбот (20); виртуален асистент (30, KD 0); чатбот за бизнес; чатбот за фейсбук; чатбот messenger; whatsapp чатбот; чатбот за сайт; ai асистент за бизнеса | AI асистент и чатбот за Вашия бизнес | 150 |  | 2026-11-15 | planned | „чатбот“ (400, KD 24) is an informational SERP; reserved for a /saveti/ article |
| /avtomatizacii/ | bg |  | avtomatizacii | автоматизация на бизнес процеси | софтуер за автоматизация (100); софтуерна автоматизация (60); онлайн записване; онлайн резервации (10, KD 2); автоматични оферти; автоматизация на документи; автоматично фактуриране; sms напомняне; табло с показатели | Автоматизация на бизнес процеси | 10 |  | 2026-11-15 | planned | collects many low-volume terms on one strong page |
| /seo-statii/ | bg |  | seo-statii | seo копирайтинг | копирайтинг услуги (150, KD 0); копирайтинг (100, KD 0); seo статии (90, KD 0); копирайтинг услуги цени (60); seo текстове (20); писане на статии (20, KD 0); описания на продукти | SEO копирайтинг и SEO статии | 100 | 0 | 2026-11-15 | planned | SERP: DR 4 sites at #2 and #6 |
| /socialni-mrezhi/ | bg |  | socialni-mrezhi | маркетинг в социалните мрежи | управление на социални мрежи (80); реклама в социалните мрежи (90); поддръжка на социални мрежи (30); поддръжка на социални мрежи цена (60, KD 0); социални мрежи реклама (60); рекламни визии; криейтиви | Поддръжка на социални мрежи и криейтиви | 150 | 0 | 2026-11-15 | planned |  |
| /reklama/ | bg |  | reklama | реклама в гугъл | гугъл реклама (100, KD 0); google реклама (80, KD 5); google ads реклама (90, KD 0); реклама в google (50, KD 1); реклама в гугъл цена (50, KD 0); онлайн реклама (150, KD 2); реклама в интернет (150, KD 0); ppc реклама (150, KD 0); фейсбук реклама (150, KD 0); реклама в инстаграм (50, KD 0); маркетинг специалист (150, KD 0; jobs SERP, secondary only) | Реклама в Google и Facebook с маркетинг специалист | 400 | 0 | 2026-11-15 | planned | biggest commercial cluster; groweasy.bg (DR 30) #1 with an article |
| /seo-optimizacia/ | bg |  | seo-optimizacia | seo оптимизация | seo услуги (300, KD 4); seo агенция (200, KD 2); seo експерт (200, KD 1); seo оптимизация на сайт (200, KD 6); seo оптимизация на сайтове (200, KD 9); seo фирма (150, KD 12); seo компания (100, KD 0); seo услуги цена (150, KD 0); seo оптимизация цена (150, KD 0); seo цена (90, KD 0); seo за онлайн магазин (100); seo оптимизация на онлайн магазин (60, KD 0); техническо seo (250) | SEO оптимизация на сайтове | 600 | 29 | 2026-11-15 | planned | owner confirmed full SEO 2026-11-15 |
| /diagnostika/ | bg |  | diagnostika | безплатна диагностика за бизнеса | дигитализация на бизнеса; къде губи време бизнесът | Безплатна диагностика: къде губи време Вашият бизнес |  |  | 2026-11-15 | planned | conversion page built from the owner's "Скрити проблеми" checker; no measurable search term |
| /seo-optimizacia/lokalno-seo/ | bg |  | lokalno-seo | локално seo | seo оптимизация софия (150, KD 30); seo пловдив (60); seo оптимизация варна (200); seo оптимизация бургас (90) | Локално SEO | 200 | 0 | 2026-11-15 | parked | phase 2 |
| /seo-optimizacia/seo-odit/ | bg |  | seo-odit | seo одит | seo одит на сайт (100); безплатен сео одит (50, KD 0); seo анализ цени (60) | SEO одит на сайт | 150 | 0 | 2026-11-15 | parked | phase 2 |

Source: biz-grow `docs/seo-audit/NICHE-ANALYSIS-2026-11-15.md` and `keyword-map.md` (Ahrefs, country bg, 2026-11-15). Advice articles (`/saveti/`) are listed there and get rows here when approved.
