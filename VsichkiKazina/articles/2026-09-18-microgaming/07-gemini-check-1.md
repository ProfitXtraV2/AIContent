# 07 — Gemini external check, pass 1 — Microgaming provider-hub profile

Model: gemini (scripts/gemini_check.py, gemini-3.1-pro-preview) · 18.09.2026
Command: `python3 scripts/gemini_check.py VsichkiKazina/articles/2026-09-18-microgaming/05b-final-draft.md`

Human-likeness: verdict „Shows AI patterns, 75% confidence" → human-likeness = 100 − 75 = **25**. Below target (80). Iterate via fresh Humaniser pass (step-7b), preserve every number/link/RG/date/byline/brand. (No bullet-list rec issued, so no brand-gate conflict.)

Verbatim output:

```
**Verdict: Shows AI patterns, 75% confidence.**

While this article is highly factual, well-researched, and features excellent localized context (like the specific mentions of НАП and Bulgarian licensing), its underlying structural scaffolding gives it away as likely AI-generated or heavily AI-edited. It relies on classic LLM crutches: explicit signposting in the intro, rigid "firstly/secondly" enumerations, repetitive sentence structures when listing items, and didactic "neat bow" summaries that tell the reader exactly what to think about the data just presented.

Here are the specific patterns that triggered this assessment and how to fix them.

### 1. The "Table of Contents" Signposting
**The Pattern:** AI models love to end an introduction by explicitly mapping out exactly what the article will cover. It feels like a high-school essay thesis statement rather than engaging web copy.
**The Quote:** *"Тук ще намерите кой стои зад студиото, какво се промени със собствеността, кои са фирмените механики и кои заглавия с числата им си струва да познавате."*
**The Recommendation:** Delete this sentence entirely. Your H2s already do the job of guiding the reader. The preceding sentence about Games Global is a much stronger, more natural hook to end the introduction on.

### 2. Forced Conversational Hooks (Meta-commentary)
**The Pattern:** To sound "human," LLMs often use dramatic, slightly unnatural meta-commentary to introduce a fact, framing it as a "twist" or a "commonly misunderstood fact."
**The Quotes:**
* *"Има обаче обрат, който трябва да се знае още в началото, защото се вижда трудно от името върху играта..."*
* *"Тук е фактът, който най-често се разказва грешно."*
**The Recommendation:** Remove the dramatic buildup. Just state the facts directly. For the first quote, transition straight into: *"Въпреки името върху играта, от 2022 г. заглавията на Microgaming се разпространяват от Games Global."* For the second, simply start the paragraph with: *"През 2022 г. Microgaming продаде..."*

### 3. Formulaic Enumeration (The "First / Second" Structure)
**The Pattern:** When explaining concepts, AI defaults to rigid, highly structured lists disguised as paragraphs.
**The Quote:** *"Почеркът на студиото стъпва на две основи, а не на дълъг списък с функции. Първата е двигателят „243 начина за печалба“... Втората основа е прогресивната джакпот мрежа..."*
**The Recommendation:** Break the mechanical "first/second" framing. Introduce the 243-ways mechanic naturally as a core innovation, and then transition to the progressive network as a separate, equally important pillar without numbering them.

### 4. Repetitive Syntax (The "Listicle Paragraph")
**The Pattern:** When an LLM is asked to describe multiple items in a paragraph, it often uses the exact same sentence structure for every single item (Subject + Year + "is" + Description). It creates a robotic, staccato rhythm.
**The Quote:** *"Immortal Romance (2011) е може би най-разпознаваемото заглавие... Thunderstruck II (2010) е неговият по-спокоен събрат... Break da Bank Again (2008) е по-класическа ротативка... Mega Moolah (2006) стои отделно от останалите..."*
**The Recommendation:** Vary the syntax. Instead of starting every sentence with the game title, mix it up. For example, start one sentence with the mechanic (*"За любителите на класиката, Break da Bank Again предлага..."*), combine two related games into one sentence (like Immortal Romance and Thunderstruck II, since they share an engine), and use active verbs instead of relying on "е" (is).

### 5. The "Neat Bow" Didactic Summary
**The Pattern:** AI struggles to let facts speak for themselves. It frequently adds a concluding sentence to a section that explicitly tells the reader how to interpret the data, often using phrases like "If you compare X, you can see Y."
**The Quote:** *"Ако сравните тези проценти, се вижда логиката на цялото портфолио: обикновените заглавия връщат около и над средното, а прогресивът плаща за шанса за милиони с по-ниско базово връщане."*
**The Recommendation:** Soften the didactic tone. Remove the "Ако сравните..." framing. Just state the contrast directly as a feature of the portfolio: *"Портфолиото балансира между стандартни игри с по-висока възвръщаемост и прогресивни джакпоти, които компенсират ниския базов RTP с шанс за милиони."*

*(Note: The responsible gambling language, 18+ markers, and affiliate disclosures at the end are perfectly integrated and should remain exactly as they are.)*
```

Decision: human-likeness 25 < 80 → apply recs 1-5 via fresh Humaniser pass (step-7b-apply-gemini-recs). All facts/numbers/links/RG untouchable; rephrase for voice only (never paste Gemini's exact suggested sentences). Then Brand-Gate re-check + re-run gemini_check.
