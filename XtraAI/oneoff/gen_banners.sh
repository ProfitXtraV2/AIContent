#!/usr/bin/env bash
# One-off: replace the "BizGrow" wordmark with "Xtra AI" on the two site banners (BG + EN).
# Gemini edits the existing banner (image-to-image) so everything else stays the same.
# Two variants per language so the owner can pick. Output: XtraAI/oneoff/out/
set -u
cd "$(dirname "$0")"
mkdir -p out
export ASPECT=4:3
P_COMMON='Edit this image. Change ONLY the large brand wordmark at the top: replace the word "BizGrow" with the brand name "Xtra AI" (exactly this spelling: capital X, lowercase "tra", a space, capital "AI"). Use the same modern geometric sans-serif typeface, the same size, weight, position, centring and two-tone colour treatment as the original: "Xtra" in the dark navy blue, "AI" in the sage green. Keep the bar-chart icon with the curved arrow to the left of the wordmark. Keep EVERYTHING else exactly as it is, pixel for pixel: the subtitle lettering under the wordmark, the glass ribbons, pebbles and stones, the four round icons, the four captions with their icons along the bottom, the background and the rounded corners. Do not add, remove, translate or re-letter any other text.'
P_BG="$P_COMMON The subtitle must stay exactly \"AI И АВТОМАТИЗАЦИЯ ЗА МАЛКИЯ БИЗНЕС\" in Cyrillic, and the bottom captions must stay exactly \"ВНЕДРЕТЕ AI\", \"АВТОМАТИЗИРАЙТЕ ПРОЦЕСИТЕ\", \"СПЕСТЕТЕ ВРЕМЕ И РАЗХОДИ\", \"РАЗВИЙТЕ БИЗНЕСА СИ\"."
P_EN="$P_COMMON The subtitle must stay exactly \"AI & AUTOMATION FOR SMALL BUSINESSES\", and the bottom captions must stay exactly \"INTEGRATE AI\", \"AUTOMATE WORKFLOWS\", \"SAVE TIME & COSTS\", \"GROW YOUR BUSINESS\"."
{
for v in 1 2; do
  python3 gen_from_ref.py "$P_BG" "out/xtra-ai-banner-bg-v$v.webp" ref/banner-bg.jpg || echo "FAILED bg v$v"
  python3 gen_from_ref.py "$P_EN" "out/xtra-ai-banner-en-v$v.webp" ref/banner-en.jpg || echo "FAILED en v$v"
done
} 2>&1 | tee out/log.txt
ls -la out
