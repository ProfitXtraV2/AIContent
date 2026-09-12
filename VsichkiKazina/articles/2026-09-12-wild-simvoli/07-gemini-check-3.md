# Gemini external check — pass 3 / after humaniser pass 2 (2026-09-12)

**Verdict: Shows AI patterns, 75% confidence** → human-likeness = 25

## Keep-best decision
Human-likeness across versions: initial draft 20 · humaniser pass 1 = 25 · humaniser pass 2 = 25. Cap (MAX_GEMINI_PASSES=2) reached. Highest human-likeness = 25; pass 2 kept (tied-highest, plus removes the redundant scatter sentence and converts the type paragraph to a list). Recorded as `ai 75`. gemini-3.1-pro-preview rates these guides harshly even after humanising (cf. posted rotativki-s-plodove HL 30); human owns final approval.

## Verbatim verdict + recommendations

**Verdict: Shows AI patterns, 75% confidence.**

While the article is highly informative, factually dense, and features excellent integration of responsible gambling protocols and localized Bulgarian context, the underlying skeleton relies heavily on standard LLM writing tropes. It suffers from formulaic transitions, didactic "lecturing," symmetrical phrasing, and ChatGPT’s default list formatting. 

Here is the breakdown of the specific patterns that triggered this assessment, along with actionable recommendations to humanize the text.

### 1. Signposting and Formulaic Transitions
AI struggles to move from one point to another without announcing what it is about to do. It frequently uses setup phrases to group concepts before explaining them.

*   **Flagged text:** *"Общото между всички: wild символът замества..."*
*   **Flagged text:** *"Оттук нататък всеки тип добавя свое движение:"*
*   **Flagged text:** *"Натрупаният (stacked) wild е друг подход към същата цел:"*
*   **Recommendation:** Delete the setup phrases. You don't need to announce that things have something in common or that they are "another approach." Start the sentences directly with the core information. For example, jump straight into how the wild symbol substitutes others, or simply begin describing the specific movements of the expanding/sticky wilds without the introductory announcement.

### 2. Symmetrical / Over-polished Subheadings
LLMs love balanced, poetic, or symmetrical phrasing (X and Y, A and B), which rarely occurs in natural, intent-driven web copywriting.

*   **Flagged text:** *"Две познати игри, две различни движения"*
*   **Recommendation:** Break the symmetry. Change this H2 to something more direct and functional that a human would actually search for or write, such as focusing on the game titles themselves or simply "Примери от популярни ротативки".

### 3. Default LLM List Formatting
ChatGPT has a very specific, rigid way of formatting lists: Bullet point, bolded term, period or colon, followed by the explanation. 

*   **Flagged text:** 
    *   *- **Разширяващ се (expanding).** Щом кацне...*
    *   *- **Залепващ (sticky).** Остава на мястото си...*
    *   *- **Вървящ, или местещ се (walking).** Пада, задейства...*
*   **Recommendation:** Break the dictionary-definition format. Either remove the periods after the bolded terms and let them flow into the sentence, or rewrite the bullets so the bolded terms are integrated naturally into the middle of the sentences rather than sitting at the very front as labels.

### 4. The Didactic / Preachy Tone
AI often adopts the tone of a slightly condescending teacher giving "useful tips" or pointing out "common misconceptions" using absolute, instructional language.

*   **Flagged text:** *"Полезно е да държиш двете неща разделени: ефектите на екрана са за гледане, а дългосрочното връщане си стои в RTP числото..."*
*   **Flagged text:** *"Едно и също име на тип не значи еднакво поведение:"*
*   **Recommendation:** Soften the lecturing tone. Remove phrases like "Полезно е да държиш двете неща разделени" and "Едно и също име на тип не значи еднакво поведение". Just state the facts: explain that visual effects don't impact RTP, and note that wild behavior varies depending on the specific game's paytable. 

### 5. Melodramatic Hook / "The Catch" (Narrated Emotion)
When transitioning to warnings or conclusions, AI often contrasts a positive visual/emotion with a dramatic "trap" or "catch" to create artificial engagement.

*   **Flagged text:** *"Разширяващ се барабан, сериен залепващ wild или дълга разходка на символ през цялата мрежа наистина изглеждат страхотно, и точно там е капанът:"*
*   **Recommendation:** Tone down the melodrama. Remove the phrase "и точно там е капанът". You can acknowledge that the visual effects are highly engaging and entertaining, and use that as a natural, neutral bridge into the responsible gambling advice. *(Note: Do not alter or remove any of the actual responsible gambling language, 18+ markers, or links that follow this sentence—only adjust the dramatic lead-in).*
