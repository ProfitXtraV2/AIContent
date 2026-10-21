**Score: 98/100**
**Verdict:** `PASS`

### Evaluation Breakdown

*   **Relevance & value:** Excellent. The hero image perfectly captures the specific Asian motifs (Koi fish, coins) and mechanics (gears, magnifying glass) discussed in the article without looking like generic filler. The infographic visualizes the exact €1000 turnover example provided in the text, adding immense value for the reader.
*   **Accuracy:** Flawless. The SVG infographic matches the article’s math exactly (`~96%` RTP, `€1000` turnover, `~€960` return, `~€40` house edge). The deduction of a `~4%` house edge is mathematically accurate and directly supported by the 96% RTP figure.
*   **Integrity / hygiene:** Perfect. No fabricated operator logos, no fake UI screenshots, no faces, and no glamorized winning. The hero image uses a clean, abstract 3D vector style that is safe and professional.
*   **Responsible gambling:** Highly appropriate. The tone is neutral and educational. The infographic explicitly includes "18+ Играйте отговорно" and reminds the user to check the real RTP, reinforcing the article's safety message.
*   **SEO metadata:** Both filenames (`habanero-hero.webp`, `habanero-rtp.svg`) are lowercase, hyphenated, and descriptive. The Bulgarian ALT texts are highly specific, accurate, and perfectly describe the visual contents.
*   **Technical quality & Layout integrity:** The SVG layout is mathematically pristine. 
    *   No text overlaps or touches the edges. 
    *   The main title (y=34) and footer text (y=308) have comfortable margins within the 320px canvas. 
    *   The text inside the boxes (`Обратно към играча`, `За казиното`) is perfectly centered and fits well within the 220px widths. 
    *   Contrast is excellent across all elements.

### Minor Polish Suggestion (Not a defect)
*   **SVG Bar Construction:** In `habanero-rtp.svg`, the red "House" bar (`width="20"`, `rx="4"`) is drawn directly on top of the green "Player" bar (`width="500"`). Because the red bar has rounded corners (`rx="4"`) on its left side as well, a microscopic sliver of the green bar underneath will technically peek through those left corners. 
    *   *Actionable fix (optional):* For absolute pixel-perfection, you could use a `<clipPath>` for the bars, or simply remove the `rx` attribute from the red bar so it sits perfectly flush against the green bar, though at web sizes this current setup is virtually unnoticeable and perfectly acceptable to publish.
