# Step 7 — Gemini check, pass 1 (initial 05b)

Model: gemini-3.1-pro-preview
Normalized: **"Mostly human-written with lingering AI structural patterns (75% confidence)"** → human-likeness ≈ **75** → just below target (80). Iterate one Humaniser pass on the flagged macro-structure, then re-check. Keep-best tracked (baseline HL 75).

(Note: an earlier attempt hit a transient `GEMINI_ERROR: read operation timed out` on the API; retried successfully — the check itself is available.)

---

### Присъда
**Mostly human-written with lingering AI structural patterns, 75% confidence.**

Много силно на изреченско ниво — идиоматичен български, който LLM рядко генерира органично („само табелата е нова", „без да мести математиката"). Макро-структурата обаче стъпва на класически AI скелет: „кажи какво ще кажеш → кажи го → обобщи".

### Флагнати пасажи
1. **„Surface vs Depth" hook (интро):** „Механиката ѝ е нарочно опростена, но зад плодовете стоят няколко детайла, които решават колко ти струва всяко завъртане." — изкуствен контраст прост-повърхност/скрита-дълбочина.
2. **„Neat bow" заключение:** „Burning Hot дължи популярността си на простата класическа механика и на носталгичната огнена тема. Зад тях стои под-средно ... RTP..." — преразказва увода + обобщава тялото.
3. **Дублиращ caption:** инфографиката повтаря дословно €964.50/€35.50 от параграфа над нея.
4. **„На практика" мост:** „На практика балансът се движи с чести дребни печалби..." — ненужен преходен маркер след техничен факт (2/5).

### Препоръки
- Махни контраста в интрото; кажи директно, че при проста механика разбирането на математиката (RTP, волатилност) е ключът за бюджета.
- Изтрий първите две изречения на заключението; започни направо с практичния съвет.
- Скъси caption-а да не папагалства числата (кратък етикет вместо цяло изречение).
- Махни „На практика"; започни изречението директно.

*(Процес: [VERIFY] за алт. RTP + RG/18+/афилиейт текстове — не се пипат.)*

(Applied in Humaniser pass 1 → re-checked in 07-gemini-check-2.md.)
