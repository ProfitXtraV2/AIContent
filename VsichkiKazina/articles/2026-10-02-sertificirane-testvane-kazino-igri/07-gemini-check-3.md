# 07 — Gemini check 3 (Step 7, after humaniser pass 2)

Human-likeness (normalized): **90** (Likely human-written, 90%) → PASS (≥80).

KEEP-BEST ledger: initial 25 · pass1 25 · pass2 **90** → keep pass 2 (highest HL seen). gemini = human 90.

```
**Verdict: Likely human-written (or heavily and expertly human-edited), 90% confidence.**

This is an excellent piece of Bulgarian copywriting. It successfully avoids almost all the classic traps of AI-generated Bulgarian text (which usually suffers from clunky passive voice, overly formal transitions like "Важно е да се отбележи," and a sickeningly enthusiastic tone). 

The text features a distinct, slightly cynical, and highly practical voice. Phrases like *"не си пишат домашното сами"* (they don't do their own homework), *"измие сметката"* (wipe your account), and *"и толкова"* (and that's it) are strong human signals. The logic is sharp and player-centric. 

However, there are a few structural remnants that feel slightly formulaic or AI-adjacent. If an LLM was used to draft or outline this, these are the seams where it shows.

Here is the breakdown of the minor AI patterns detected and how to polish them out.

### 1. Pattern: The "Wikipedia Dump" (Information Density)
**The Passage:** 
> "GLI (Gaming Laboratories International) е основана през 1989 г. в Томс Ривър, Ню Джърси, и е сред най-старите и най-големите: тествала е оборудване за над 480 юрисдикции и поддържа собствени стандарти, например GLI-19 за онлайн игри с генератор на случайни числа. eCOGRA работи от 2003 г. със седалище в Лондон и е позната с печата си за честност и с периодичните доклади за реалната възвръщаемост на някои оператори. iTech Labs тества онлайн игрални системи от 2004 г. от Австралия и през 2023 г. влезе в групата на GLI. Най-старата от всички е BMM Testlabs, основана през 1981 г. в Лас Вегас."

**Why it flagged:** When asked to list entities, LLMs tend to generate dense, uniform blocks of text where every sentence follows the exact same structure: *[Name] was founded in [Year] in [Location] and does [Fact].* It creates a monotonous, encyclopedic rhythm that disrupts the otherwise conversational tone of your article.

**Recommendation:** 
Do not change any of the dates, names, or facts. Instead, break this dense paragraph into a bulleted list. Give each laboratory its own bullet point. This breaks up the visual wall of text and makes it look like a human-designed reference section rather than an AI data dump.

### 2. Pattern: Didactic Signposting
**The Passage:** 
> "Две неща интересуват лабораторията, защото играчът не може да ги провери сам: дали генераторът на случайни числа е наистина случаен и дали играта връща обявеното. [...] Математиката на играта е другата половина."

**Why it flagged:** LLMs love to announce exactly what they are going to do before they do it, and then rigidly check off the list. Announcing "Two things..." and then later transitioning with "The math is the other half" is a very common AI structural crutch used to maintain coherence. 

**Recommendation:** 
Remove the rigid numbering. You can simply state that laboratories focus on things the player cannot check themselves, such as the RNG and the RTP. Then, just start a new paragraph for the math/RTP section without explicitly calling it "the other half." Let the concepts flow naturally into one another.

### 3. Pattern: The "Double Conclusion" (Over-summarization)
**The Passage:** 
> "Сертификатът е добра основа за доверие, но не е причина да играете повече. Домашното предимство, което печатът потвърждава, работи срещу вас при всяко завъртане, затова бюджетът и лимитите на депозита се слагат преди първия депозит, а инструментите за отговорна игра са там за момента, в който сметката спре да е забавление.
> 
> Търсете печата на eCOGRA, iTech Labs или GLI, защото превръща „вярвай ни" в „проверено отвън". Но честността е най-малкото, което бива да искате от една игра. Коя версия въртите, го пише в информационния панел. А дали изобщо има кой да ви защити, когато нещо се обърка, зависи от лиценза от НАП, не от логото в долния ъгъл."

**Why it flagged:** LLMs are hardwired to summarize the entire article at the end. Here, you have two distinct concluding paragraphs that essentially do the same job: they both summarize the main takeaways (RTP vs. House Edge, checking the panel, relying on the NAP license). It feels like the text is trying to end twice.

**Recommendation:** 
Merge these two paragraphs into one tight, punchy conclusion. Keep the excellent responsible gambling tie-in ("бюджетът и лимитите..."), but strip out the repetitive summary points. End abruptly on your strongest thought—that the NAP license protects you, not the logo in the corner. 

***

**A Note on Process:** 
The responsible gambling language, 18+ markers, author bio, and affiliate disclosures at the bottom are perfectly formatted and placed. Do not touch them. They are exactly where they need to be for compliance and trust.
```
