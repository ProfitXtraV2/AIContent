# log — / (home, bg) — 2026-11-15

- Run: manual (owner un-paused BizGrow for manual runs 2026-11-15). Orchestrator: Claude Code subagent; each of steps 1, 1.5, 2, 3, 4, 5, 5b run as a separate fresh-context subagent (Agent tool) reading only that stage's inputs.
- Step 0: read biz-grow @ feature/seo-improvements 528ad25 (bg.ts, types.ts, config.ts, HomePage/Sections/Contact/HeroVisual). Wrote 00-current.md, 00-inventory.md, 00-brief.md. Buyer questions from WebSearch (bg) + Ahrefs SERP files (serp-ai_автоматизация.json is empty; serp-автоматизация.json informational). Site-rules differences: none material (branch adds `page`, `a11y.breadcrumb`, content routes; #ads already removed).
- Step 1 synthesis: started.
- Step 1 synthesis (subagent): 01-synthesis.md; 0 new facts, 6 OWNER CONFIRM.
- Step 1.5 outline (subagent): 01.5-outline.md; 8 anchors kept + new #faq; FAQ canon limits applied (no "timelines in report", no "optional support").
- Step 2 author (subagent): 02-draft.md with PORT KEYS block; inventory check complete.
- Step 3 humaniser (subagent): NEEDS EDIT → edited (03-humanised.md); inventory diff clean.
- Step 4 SEO (subagent): 04-seo.md; relevance 90/100; title 43, meta 149; inventory diff clean.
- Step 5 Brand Gate (subagent): Phase 1 PASS WITH FIXES 90/100 (1 critical: "Всеки месец" for the marketing specialist's report not canon). Phase 2 applied by the gate (resumed same subagent): PASS 93/100, 0 criticals.
- Step 5b light re-check (subagent): no changes; inventory diff clean.
- Step 6 (orchestrator): content/home.md + content/home.port.json from one data structure; self-check all PASS (06-verification.md). Coordinator note applied: booking/email CTAs kept in the port JSON via their dictionary keys.
- Step 7 Gemini: skipped (no GEMINI_API_KEY locally).
- Step 8 images: none.
- STOP for the human. Nothing committed (shared worktree; orchestrator told not to run git).
- 2026-11-15 (porting session): hero.overlayLabel changed „Безплатна диагностика“ → „Изграждане“ at porting, because with the new overlayUnit „обикновено до 2 седмици“ the card read as if the diagnosis took 2 weeks. Canon wording (process step 3). Owner item: confirm, or restore „за дни, не месеци“ under the old label.
