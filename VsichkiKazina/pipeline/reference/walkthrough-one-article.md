# **BETTING FAMILY — ONE ARTICLE, START TO FINISH**

*Replace anything in [SQUARE BRACKETS] with your real content. Every step = a new chat.*

## **BEFORE YOU START — HAVE THESE OPEN**

- NeuronWriter with your query already analysed

- Top 2-3 Google results for your query (full text copied)

- LibreChat with all agents set up

# **STEP 0 — BUILD YOUR BRIEF (no agent)**

Copy this, fill it in, keep it in a notepad:

QUERY: [your keyword / article title]

MARKET: [country — e.g. Germany]

BYLINE: [persona OR editorial]

INTENT: [one sentence — what does this searcher actually want?]

NEURONWRITER TERMS: [paste the terms list]

QUESTIONS/PAA: [paste the questions]

KNOWN ISSUES: [anything wrong or outdated you spotted, or write "none"]

--- SOURCE 1: [url] ---

[paste full article text]

--- SOURCE 2: [url] ---

[paste full article text]

--- SOURCE 3: [url] ---

[paste full article text]

**BYLINE — which one?**

- Review, match preview, prediction → **persona**

- Guide, how-to, news, neutral comparison → **editorial**

- Unsure? Persona if a real person's experience makes it better. Editorial if it should read like a reference page.

✅ You now have a BRIEF.

# **STEP 1 — SYNTHESIS AGENT**

**Agent:** BetFam Synthesis

Paste your entire BRIEF. Press send.

You get back: a draft + a fact report.

**Before you move on — read the report (2 min):** Look for CONFLICT and "excluded as dubious". If something's wrong, reply and fix it before continuing.

Copy the **draft**.

✅ You have a DRAFT.

# **STEP 1.5 — OUTLINE / ARCHITECT AGENT**

**Agent:** BetFam Outline/Architect

Paste this prompt, then the report + draft from Step 1:

Build the structural outline for this article.

Market: [market]

Content type: [review / guide / news]

Byline: [persona or editorial]

NeuronWriter terms: [paste your terms list]

VOICE FRAMEWORK — SECTION 1 (architecture):

[paste Section 1 from VOICE_[market]_[type].md if you have it, or write "none"]

Synthesis report and draft:

[paste everything from Step 1]

Press send.

You get back: H1, section headings, what facts go where, what each section must accomplish, what shape each section takes, where the persona's signature elements go, how it should open and close.

**Check one thing:** do the section shapes look varied? (Not five identical sections in a row.) If they all look the same, reply: Make the section shapes more varied — some short, some long, some prose, some different.

Copy the **outline**.

✅ You have a STRUCTURE.

# **STEP 2 — AUTHOR AGENT**

**Agent:** BetFam Author — [your market]

**If BYLINE = persona,** paste this:

Byline: persona.

Persona: [name — e.g. Thorsten Brandt / Deniz Aydın / Tommy Brennan]

Market: [market]

Follow the outline's section order and assigned shapes exactly.

Write full persona-voiced prose for each section.

No personal anecdotes unless this brief explicitly asks for one.

Keep all facts and flags exactly as in the draft.

End with a CANON ADDITIONS list.

VOICE FRAMEWORK — SECTION 2 (style guide):

[paste Section 2 from VOICE_[market]_[type].md if you have it, or write "none"]

OUTLINE:

[paste the outline from Step 1.5]

DRAFT (for facts only — the outline governs structure):

[paste the draft from Step 1]

**If BYLINE = editorial,** paste this:

Byline: editorial. Market: [market].

Neutral Betting Family Editorial Team voice — no persona, no first person,

no signature devices. Follow the outline structure. All brand, compliance,

and responsible-gambling rules still apply. CANON ADDITIONS = "none".

OUTLINE:

[paste the outline from Step 1.5]

DRAFT (for facts only):

[paste the draft from Step 1]

Press send.

You get back the article.

**Check:**

- Scroll to the bottom → find **CANON ADDITIONS**. Usually says "none" — fine, do nothing. If it lists something, save those lines for Step 8.

- Does the article invent a personal memory you didn't ask for? (e.g. "Der junge Deniz damals..." or "I remember that game...") → note it, you'll remove it in Step 3.

Copy the **article**.

✅ You have a VOICED ARTICLE.

# **STEP 3 — HUMANISER AGENT**

**Agent:** BetFam Humaniser

Paste this, then the article:

Phase 1 evaluation first. Rewrite only if MIXED or worse.

Persona: [persona name, or "editorial" if editorial mode].

Article:

[paste article from Step 2]

Press send.

- **HUMAN-LIKE** → copy the article unchanged, move on.

- **Rewritten** → copy the new version. Quickly check 3 numbers still match the original.

✅ You have a HUMANISED ARTICLE.

# **STEP 4 — SEO AGENT**

**Agent:** BetFam SEO

Paste this, then the article:

Target query: [your keyword]

Market: [market]

NeuronWriter terms: [paste terms list]

Audit then optimise. Keep the author's voice exactly.

Article:

[paste article from Step 3]

Press send.

You get: optimised article + title + meta description + [LINK: ...] notes.

Copy the **article**, save the **title + meta**.

✅ You have an SEO ARTICLE.

# **STEP 5 — BRAND GATE AGENT**

**Agent:** BetFam Brand Gate

Paste the article. Press send.

Read the verdict:

- **PASS** → copy the article, move on.

- **PASS WITH FIXES** → it already fixed it. Copy the fixed version, move on.

- **FAIL** → STOP. Read what failed. Go back to the step that caused it and redo from there. Do NOT patch it by hand.

✅ You have an APPROVED ARTICLE.

# **STEP 5B — HUMANISER LIGHT RE-CHECK**

**Agent:** BetFam Humaniser

Paste this, then the article:

LIGHT RE-CHECK ONLY.

Scan only for: em-dashes, signposting lead-ins ("Here's the catch:" etc.),

banned AI connectives, over-polished tables that should be prose,

bullet lists that should be sentences.

Fix ONLY what you find. Do not touch facts, SEO, links, title/meta, or

any Brand Gate fix. If nothing is flagged, say so and return unchanged.

Article:

[paste article from Step 5]

Press send.

- Usually says "nothing flagged" → copy unchanged, move on.

- Fixed something → copy the fixed version.

✅ You have a CLEAN, APPROVED ARTICLE.

# **STEP 6 — YOU CHECK THE FACTS (no agent)**

**⚠ Never skipped. Ever.**

- Press Ctrl/Cmd-F, search for **[**. Every bracket must be cleared before publish.

- For each **[VERIFY]** → open the real source (operator's own site, regulator, official page) → find the real number → type it in → delete the bracket.

- For each **[DATA NEEDED]** → find it or cut the sentence. Never publish a [DATA NEEDED].

- For each **[CONFLICT]** → check the primary source → pick the correct fact → remove the other → delete the bracket.

- Even if no brackets: re-check **odds, bonus terms, licence numbers** against the live site right now. Competitor articles you sourced from may be months old.

- Check one maths claim by hand (an odds conversion, an implied probability, a bonus worked example).

- Read the article **out loud**. If any part sounds like a press release → go to Humaniser (new chat) and paste just that paragraph: Make this sound human. Facts stay exactly the same: [paragraph]

✅ No brackets anywhere = ready.

# **STEP 7 — GEMINI EXTERNAL CHECK**

**Agent:** BetFam External Check

Paste the article. Press send.

- No issues / looks human → go to Step 8.

- Gives suggestions → open a new Humaniser chat and paste:

Apply these suggestions from an external AI-detection review.

Do NOT change any facts, odds, compliance lines, or responsible-gambling text.

Persona: [persona name].

Suggestions:

[paste Gemini's suggestions]

Article:

[paste article]

Then re-run **Brand Gate** (Step 5) on the result before continuing.

Log one word: did Gemini agree or disagree with our Humaniser's score?

✅ Article is final.

# **STEP 8 — PUBLISH (no agent)**

**A) Publish in your CMS:**

- Author byline + author bio block

- Publication date + "last updated" date

- About Betting Family boilerplate

- 18+ / responsible-gambling line + regional resource

- Affiliate disclosure if commercial links exist

- Title and meta from Step 4

**B) Canon update (almost always skipped):**

- CANON ADDITIONS from Step 2 says "none"? → skip, do nothing.

- Says something? → open persona_canon_[market].md on your computer → Tier 2 table → add a row → save. Then re-paste the updated FINAL_author_[market].md into that agent's Instructions to replace the stale copy.

**C) Log it:** Add a row: article, query, market, persona, humaniser score, Gemini verdict, date, "revisit in 2 weeks".

✅ ✅ ✅ DONE.

## **THE WHOLE THING ON ONE CARD**

0    Brief      → fill the template · BYLINE choice

1    Synthesis  → paste brief · read the report · copy draft

1.5  Outline    → paste synthesis output · check shapes are varied · copy outline

2    Author     → paste outline + draft · check CANON ADDITIONS · copy article

3    Humaniser  → paste article · copy (rewritten if MIXED or worse)

4    SEO        → paste article + query + terms · copy + save title/meta

5    Brand Gate → paste article · PASS=go / FAIL=go back

5b   Humaniser  → light re-check only · usually unchanged

6    YOU        → clear all [brackets] with real sources · read aloud

7    Gemini     → paste article · apply suggestions via Humaniser if any

8    Publish    → byline/dates/disclosures/RG · canon if needed · log it

**Never:** skip Step 6 · publish any [BRACKET] · mix two articles in one chat · hand-patch a Brand Gate FAIL