#!/usr/bin/env bash
# One-off: 7WILD casino hero art (Heat direction) for the lobby mockups. Style-guided by ref/heat-hero.jpg.
set -u
cd "$(git rev-parse --show-toplevel)"
OUT=7Wild/oneoff/out-hero; REF=7Wild/oneoff/ref/heat-hero.jpg
mkdir -p "$OUT"; LOG="$OUT/log.txt"; : > "$LOG"
STYLE='Use the attached image ONLY as a style reference for mood, lighting and colour. Do NOT copy its text, buttons or layout. Create a NEW, original, premium online-casino hero artwork: a black-and-charcoal jaguar head in a hyper-detailed semi-realistic digital-painting style, one eye glowing ember orange, the fur rim-lit in hot tangerine light, emerging out of deep near-black darkness (#0E0C0B). Warm heat palette only: near-black, charcoal, tangerine #FF6A13, ember #C2410C, a touch of amber #FFB020. Cinematic, adult, high contrast, glossy orange light streaks and a few floating embers. Absolutely no green, purple or blue.'
NOTEXT='No text, no words, no letters, no numbers other than the 7 symbol, no buttons, no UI, no watermark.'
SEVEN_STROKE='Behind the jaguar a huge bold geometric "7" symbol: one thick confident stroke with a squared top bar and a diagonal stem, glowing tangerine-to-ember gradient, the top-left end of the bar finishing in a small subtle flame tip.'
SEVEN_BARS='Behind the jaguar a huge bold "7" symbol built from three thick parallel slanted orange bars with glossy tangerine-to-ember gradient and hard light edges.'
run () { echo "== $1" >> "$LOG"; ASPECT="$2" python3 7Wild/oneoff/gen_from_ref.py "$3" "$OUT/$1.webp" "$REF" >> "$LOG" 2>&1; echo "exit=$?" >> "$LOG"; }
run hero-wide-stroke 16:9 "$STYLE $SEVEN_STROKE Composition: the jaguar head and the 7 fill the RIGHT 55% of the frame, the jaguar facing left toward the centre; the LEFT 45% stays calm near-black with only a faint orange haze so a headline can sit there. $NOTEXT"
run hero-wide-bars 16:9 "$STYLE $SEVEN_BARS Composition: the jaguar head and the 7 fill the RIGHT 55% of the frame, the jaguar facing left toward the centre; the LEFT 45% stays calm near-black with only a faint orange haze so a headline can sit there. $NOTEXT"
run hero-wide-logo 16:9 "$STYLE $SEVEN_STROKE Composition: the jaguar head and the 7 fill the RIGHT 55% of the frame, the jaguar facing left; the LEFT 45% is calm near-black. In the left area render the brand wordmark exactly as: 7WILD. (the digit 7, then the capital letters W I L D, then a full stop) in a heavy, chunky, slightly rounded grotesque sans-serif, cream-white letters #F6EFE4, tight letter spacing, and ONLY the final full stop in bright safety orange #FF6A13. Spell it exactly 7WILD. with nothing else written anywhere. No buttons, no UI, no other text."
run hero-mobile-stroke 4:5 "$STYLE $SEVEN_STROKE Composition for a phone screen: the jaguar head fills the upper-right two thirds, facing down-left, the 7 glowing behind it; the bottom 40% of the frame fades smoothly to solid near-black so white headline text can sit there. $NOTEXT"
run bonus-chip 1:1 "$STYLE Instead of the jaguar, show a single glossy black-and-orange casino chip in a dynamic three-quarter tilted view, with a bold orange 7 emblem in its centre and orange edge inserts, floating on near-black with orange light streaks and embers. $NOTEXT"
cat "$LOG"
