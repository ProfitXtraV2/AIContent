# Step 7 — Gemini check, pass 1 — danaci-pechalbi-onlajn-kazino

Run: 2026-10-28 · model gemini-3.1-pro-preview · file 05b-final-draft.md
Normalized human-likeness = 100 − 85 = **15** (verdict: Shows AI patterns, 85%). BELOW target 80 → humaniser pass 1 required (keep-best).

---
## Gemini verbatim verdict + recommendations

**Verdict: Shows AI patterns, 85% confidence.**

While the text is grammatically flawless and accurately adopts a neutral editorial register, it suffers heavily from "AI safety syndrome" and token-padding. Because this is a YMYL (Your Money or Your Life) topic regarding taxes, the LLM’s safety guardrails have triggered massive over-hedging. Furthermore, the AI stretches a single, simple legal fact across multiple sections using circular repetition and didactic signposting. 

Here is the breakdown of the specific patterns that gave it away, followed by actionable recommendations.

### 1. Pattern: YMYL Over-Hedging (The "Consult a Professional" Loop)
AI models are hardcoded to avoid giving definitive financial or legal advice. When forced to write about taxes, they compulsively insert disclaimers into almost every paragraph, apologizing for not being an accountant. 

*   **Flagged Passages:**
    *   *"Извън него има положения, в които отговорът вече е за счетоводител или за НАП."* (Intro)
    *   *"...ако мислите в тази посока, поставете въпроса пред счетоводител, вместо да разчитате на общо правило."* (Section: Признават ли се загубите)
    *   *"Това е разговор със счетоводител за конкретната ви дейност, а не въпрос с готов отговор на страница като тази."* (Section: Кога въпросът вече е за счетоводител...)
    *   *"Как се третира такава печалба не е нещо, което тази статия може да ви каже с число; тук отговорът е от НАП."* (Section: Кога въпросът вече е за счетоводител...)
    *   *"...най-добре потвърдете с НАП или със счетоводител; това е извън обхвата на тази статия."* (FAQ 1)
*   **Recommendation:** You already have a perfectly good legal disclaimer at the bottom of the article (*"Това не е данъчна консултация..."*). Rely on it. Strip out the repetitive, conversational apologies ("не е нещо, което тази статия може да ви каже", "извън обхвата на тази статия") from the body text. State the limitations of the law objectively, rather than narrating the limitations of the article itself.

### 2. Pattern: Circular Repetition (The Echo Effect)
Because the core answer is very short (if the casino is licensed, there is no tax), the AI struggles to hit a standard article length. It solves this by repeating the exact same dichotomy—license vs. amount, online vs. offline—in the intro, the first H2, and the FAQ.

*   **Flagged Passages:**
    *   *Intro:* "Решаващият фактор... е лицензът на организатора, а не размерът на печалбата и не дали играта е онлайн или в наземно казино."
    *   *H2 1:* "Текстът на закона не се интересува колко сте спечелили. Интересува се кой е организирал играта... независимо дали става дума за €20 или за сериозна сума."
    *   *H2 1 (end):* "Онлайн или на живо не променя правилото. Законът не прави разлика между рулетка в наземно казино и същата игра през телефона..."
    *   *FAQ 2:* "За данъка върху дохода на физическото лице онлайн или наземна игра няма значение; значение има лицензът."
*   **Recommendation:** Consolidate the core rule. Merge the explanation in the intro with the first H2. Once you have established that the law only cares about the license (not the amount, not the medium), do not re-explain the mechanics of the law in the subsequent paragraphs or FAQs. Let the FAQs be direct, one-sentence answers rather than mini-essays repeating the H2s.

### 3. Pattern: Didactic Signposting & Formulaic Transitions
AI loves to set up a paragraph by summarizing the previous one and then announcing a pivot. It creates a robotic, patronizing rhythm ("Thing A is one thing, but Thing B is another").

*   **Flagged Passages:**
    *   *"Необлагаемостта на печалбата е едно, а как банката гледа на движението по сметката ви е друго."*
    *   *"Простото правило покрива масовия случай: играч, който играе при лицензиран организатор, спечелва и прибира. Има обаче положения, в които не бива да спирате дотук."*
*   **Recommendation:** Flatten these transitions. Delete the setup sentences entirely and start the paragraphs directly with the new information. For example, instead of the "Простото правило..." setup, just start the paragraph with: *"Ако хазартът е основният ви източник на доход..."* 

### 4. Process Note: Unresolved Editorial Tags
*   **Flagged Passages:** 
    *   ``[VERIFY: конкретни AML прагове...]``
    *   ``[VERIFY: третиране на хазартни загуби...]``
    *   ``[VERIFY: данъчно третиране на печалба...]``
    *   ``[About boilerplate slot - Всички Казина]``
*   **Observation:** These internal prompting/editorial tags have survived into the "finished" article. Per my strict instructions, I am flagging this as a failure in the editorial pipeline, but **I am not recommending their removal or touching them myself.** They indicate that the text was copy-pasted directly from an LLM output window without a final human scrub of the bracketed commands.
