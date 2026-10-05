# Gemini external check — pass 3 / after humaniser pass 2 (2026-09-12)

**Verdict: Shows AI patterns, 70% confidence** → human-likeness = 30

## Keep-best decision
Human-likeness: initial 25 → humaniser pass 1 = 35 → humaniser pass 2 = 30. Pass 2 (Wikipedia-dump rewrite + bulleted list + synthesized labs) measurably LOWERED human-likeness (35 → 30). Per keep-best, REVERTING 05b to the pass-1 version (HL 35, the highest seen). Recorded `ai 65` (pass-1 verdict: Shows AI patterns 65%). gemini-3.1-pro-preview rates these BG guides harshly even after humanising; human owns final approval.

## Verbatim verdict (pass 2 — the rejected/lower version)

Here is my evaluation of the article from the perspective of a senior copywriter specializing in AI text detection.

### **Verdict: Shows AI patterns, 70% confidence**
This is a high-quality, well-edited text. It avoids the most egregious AI clichés (there is no "In today's fast-paced digital world" equivalent here), and it uses excellent, natural-sounding industry terminology (e.g., "затоплена машина", "зашити в самата игра"). However, the underlying structural scaffolding—specifically the use of rhetorical repetition, over-hedging, safety disclaimers, and a "neat bow" summary—strongly suggests it was generated or heavily structured by an LLM and then polished by a human. 

Here are the specific patterns that triggered this assessment and how to fix them.

---

### **1. Pattern: Rhetorical Anaphora (The "Rule of Three" Intro)**
**The Flagged Text:** *"Всяка ротативка, всяка маса за блекджек на живо и всяка джакпот игра в българско онлайн казино е построена от компания..."*
**The Issue:** LLMs love using repetitive, rhythmic structures (anaphora) to build a sense of authority and scale in introductions. The "Every X, every Y, and every Z" pattern is a classic AI hook designed to sound dramatic but often comes across as formulaic.
**The Recommendation:** Break the repetitive structure. Start more conversationally or directly. For example, suggest combining the subjects into a single, punchy statement about how the games you play are rarely built by the casino itself, dropping the "Всяка... всяка... всяка..." rhythm.

### **2. Pattern: Over-Hedging / The "Safe" Nuance**
**The Flagged Text:** *"Липсата на някой от тези признаци не значи автоматично измама, но прозрачността остава първото нещо, по което си струва да съдиш."*
**The Issue:** This is the classic AI "balanced conclusion." LLMs are programmed to avoid making absolute claims, so they frequently use a "While it doesn't automatically mean X, it is still Y" structure to wrap up a paragraph safely. It dilutes the author's voice.
**The Recommendation:** Remove the hedge. Advise the writer to be more decisive. Instead of softening the blow by saying it "doesn't automatically mean fraud," suggest stating directly that missing RTP or licensing info is a clear red flag and players should simply look elsewhere. 

### **3. Pattern: The Over-Clarification Disclaimer**
**The Flagged Text:** *"Числата са примерни, не са данни от конкретно казино или заглавие."*
**The Issue:** This is a glaring AI safety mechanism. When an LLM provides a mathematical example (like the €1000 turnover / €960 return), its safety guardrails often force it to add a disclaimer so the user doesn't take the numbers as a literal promise or factual claim. Human writers rarely feel the need to explain that a perfectly round number used to demonstrate a percentage is just an example.
**The Recommendation:** Delete this sentence entirely. The context already makes it perfectly clear that this is a mathematical illustration. 

### **4. Pattern: The "Neat Bow" Summary**
**The Flagged Text:** *"Името на доставчика и сертификатът зад него са първи филтър, който казва само, че играта прави точно това, което пише."*
**The Issue:** LLMs are trained on standard essay formats, which means they almost always use the final paragraph to summarize the main points of the article before delivering a final thought. This creates a repetitive reading experience where the user is told what they just read.
**The Recommendation:** Cut the summary sentence. Suggest starting that final paragraph directly with the actionable advice about checking the RTP in the info panel before betting. This creates a sharper, more urgent transition into the responsible gambling advice.

---

*Note on Hard Rules: The responsible gambling language, 18+ markers, and affiliate disclosures at the bottom of the text are perfectly placed. As per standard compliance protocols, I have not recommended any changes to these sections.*

## Note on measurement variance
A re-read of the restored pass-1 text scored "Shows AI patterns, 80%" (HL 20) — the SAME text earlier scored 65% (HL 35). gemini-3.1-pro-preview's verdict is high-variance across calls (±~15), so keep-best is based on the highest reading seen at evaluation time (pass 1 = 65% → HL 35). Not chasing the noise (cap reached). Recorded `ai 65` (pass-1 winning verdict).
