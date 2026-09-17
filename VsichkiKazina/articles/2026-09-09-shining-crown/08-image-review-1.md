# Gemini image review — pass 1

Images: `shining-crown-harakteristiki-infografika.svg`, `shining-crown-plodov-slot-hero.webp`
Model: gemini-3.1-pro-preview · **Score 35/100 · NEEDS WORK** · **INTEGRITY FAILURE on the hero** (fabricated slot-machine UI/grid).

---

**Score: 35/100 — NEEDS WORK**

1. **Hero `shining-crown-plodov-slot-hero.webp` — fake UI (integrity):** the AI generated a non-existent, illogical slot structure (3 reels + two black strips with floating crowns) — a fake game interface, which violates the strict no-fake-UI hygiene rule. Also contradicts the text's "разтяга се вертикално и покрива целия барабан" (crowns shown small, not stretched).
2. **Infographic `shining-crown-harakteristiki-infografika.svg` — flawless:** every number (96.37%, 3.6 цента, 5000x, 95.98%, 96.50%) and fact matches the text exactly; no hygiene violations; metadata correct. Reviewer: "publish-ready as is, change nothing."

**Action for pass 2:** regenerate the hero with an ABSTRACT composition prompt (classic fruits + a crown arranged abstractly, NO slot-machine UI, NO reels, NO grid). If the regeneration still fabricates UI, drop the hero per the integrity-exception rule and ship the infographic alone.
