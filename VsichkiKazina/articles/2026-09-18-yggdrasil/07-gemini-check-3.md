# 07 — Gemini text check · pass 3 (after humaniser pass 2)

Command: `python3 scripts/gemini_check.py VsichkiKazina/articles/2026-09-18-yggdrasil/05b-final-draft.md`
Exit: 0

Normalized human-likeness: verdict "Likely human-written, 80% confidence" -> human-likeness = **80**. Meets target 80 -> **PASS**.

Progression: check 1 HL 15 -> pass 1 -> check 2 HL 25 -> pass 2 -> check 3 HL 80. Keep-best = this version (highest HL seen). gemini column = `human 80`.

Residual recs (NOT applied - would either break brand rules or risk facts, and the piece already passed at 80): #1/#3 "convert the round-up to a bulleted list" is declined for the same brand-gate anti-list reason as pass 2 (the SVG carries the scannable data); the remaining suggestions are optional style trims below the pass threshold. No further pass taken (cap of 2 humaniser passes reached and target met).

## Gemini verdict (verbatim)

Here is my evaluation of the article based on LLM writing patterns and AI text detection.

### **Verdict: Likely human-written (or heavily human-edited), 80% confidence.**
This text is remarkably clean and avoids almost all of the classic AI "fluff" words (*in the ever-evolving landscape, crucial, delve, testament, seamless*). The writer demonstrates deep domain expertise—specifically the nuanced distinction between a B2B provider license and a B2C operator license, and the difference between volatility and RTP. 

However, there are a few structural rigidities, repetitive phrasing loops, and data-stuffed sentences that occasionally give it a slightly robotic, AI-assisted cadence. 

***

### **Flagged Passages, Patterns, and Recommendations**

#### **1. Pattern: Formulaic Cataloging / "The Listicle Paragraph"**
> *"Splitz е двигателят, при който символите се разцепват на по-малки и така умножават начините за печалба, докато в Temple Stacks броят им стига до 248 832. GigaBlox работи в обратната посока: пуска огромни символи, до 6 на 6 позиции, които покриват цели участъци от барабаните, и дебютира в Lucky Neko. Multiplier Wilds са лепкавите диви символи, които носят множител и остават на място за няколко завъртания..."*

*   **Why it triggered:** This reads exactly like a bulleted list that an AI was instructed to compress into a single paragraph. The rhythm is highly mechanical: [Feature A] does X. [Feature B] does Y. [Feature C] does Z. 
*   **Recommendation:** Break this up to make it read more naturally. You can either format these as actual bullet points (which is better for UX anyway), or vary the sentence structures so they don't all follow the exact same subject-verb-definition syntax. 

#### **2. Pattern: Repetitive Paraphrasing / Over-explaining**
> *"Splitz с неговите стотици хиляди начини за печалба и GigaBlox с гигантските символи менят формата на играта и тавана на едно попадение, не домашното предимство. Голямото число „248 832 начина" и рекламният таван от десетки хиляди пъти залога са волатилност, не стойност: същите функции, които могат да върнат едро, водят и до дълги сухи серии, докато чакате да се подредят. RTP и предимството на казиното остават заложени в математиката на конкретната версия, независимо колко зрелищна е анимацията отгоре. Визуалната част вдига дисперсията, без да пипа програмирания RTP."*

*   **Why it triggered:** AI models frequently use "rhetorical hammering"—stating the exact same concept three or four times in consecutive sentences using slightly different words to hit a word count. Here, the text says "mechanics change volatility, not RTP/math" four separate times in four sentences.
*   **Recommendation:** Keep the strongest, most human phrasing (the excellent *"са волатилност, не стойност"* and the point about dry spells) and delete the redundant sentences. You can safely cut the final sentence (*"Визуалната част вдига дисперсията..."*) entirely, as it just repeats the first sentence.

#### **3. Pattern: Data-Stuffed Sentences / Robotic Rhythm**
> *"Най-старата от тях, Valley of the Gods (2017), още стъпва на респини и разрастващо се поле: висока волатилност, RTP 96.20% и таван до 5 800x залога. Splitz двигателят се показа в пълния си вид в Temple Stacks: Splitz (2020), който разгъва до 248 832 начина за печалба при RTP 96.10% и таван от 25 000x. Същата година GigaBlox дебютира в Lucky Neko: Gigablox (2020) с гигантските си символи, RTP 96.40% и таван 6 950x."*

*   **Why it triggered:** When asked to summarize data, AI tends to force every single metric into the sentence, creating a dense, catalog-like rhythm. Every sentence here follows the exact same formula: [Game Name] + [Year] + [Feature] + [RTP] + [Max Win]. 
*   **Recommendation:** Since you already have an infographic/table right above this paragraph doing the heavy lifting for the raw numbers, use the text to tell the *story* of the games. Vary the sentence structure. You don't need to list the exact RTP and Max Win in every single sentence if the table already shows it.

#### **4. Pattern: The Breathless Run-on (Over-connected clauses)**
> *"Преди реален залог повечето слот игри на Yggdrasil имат демо режим, в който да усетите темпото и волатилността без пари, а при студио, което залага на функции като Splitz и GigaBlox, това е още по-полезно от обичайното, защото формата на тези игри се усеща едва след няколко завъртания."*

*   **Why it triggered:** This is a 47-word sentence. AI often creates these sprawling, multi-clause sentences when trying to logically connect a feature (demo mode) to a specific context (Splitz/GigaBlox) and a user benefit (feeling the format). 
*   **Recommendation:** Split this into two distinct sentences. Place a period after "без пари". Start the next sentence with something like: "При студио, което залага на функции като..." This will immediately improve the readability and human pacing of the conclusion. 

*(Note: The responsible gambling language, 18+ markers, and affiliate disclosures at the end of the text are perfectly placed and should remain exactly as they are.)*
