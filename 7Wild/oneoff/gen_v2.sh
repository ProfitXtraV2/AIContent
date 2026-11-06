#!/usr/bin/env bash
# One-off v2: fiercer jaguar (snarling, like the Heat concept) with the 7 kept SEPARATE behind it, plus lobby promo art.
set -u
cd "$(git rev-parse --show-toplevel)"
OUT=7Wild/oneoff/out-v2; REF=7Wild/oneoff/ref/heat-hero.jpg
mkdir -p "$OUT"; LOG="$OUT/log.txt"; : > "$LOG"
STYLE='Use the attached image ONLY as a style reference for mood, lighting and colour. Do NOT copy its text, buttons or layout. Premium online-casino key art in a hyper-detailed semi-realistic digital-painting style, deep near-black background (#0E0C0B), warm heat palette only: near-black, charcoal, tangerine #FF6A13, ember #C2410C, a touch of amber #FFB020. Cinematic, adult, high contrast, glossy orange light streaks and floating embers. Absolutely no green, purple or blue.'
JAG='A FEROCIOUS black jaguar head, snarling and roaring: mouth wide open baring long sharp white fangs, wrinkled snarling snout, ears pinned back, intense glowing ember-orange eyes, fur rim-lit in hot tangerine light. Aggressive and threatening, like a predator about to strike, but no blood or gore.'
SEVEN='A huge bold geometric orange "7" symbol with a squared top bar and a thick diagonal stem, glossy tangerine-to-ember gradient, a small flame licking off the top-left corner of the bar.'
SEP='IMPORTANT LAYOUT RULE: the 7 and the jaguar are two SEPARATE objects side by side. The 7 stands BEHIND and to the LEFT of the jaguar. The jaguar is NOT inside the 7, NOT framed by the 7 and NOT enclosed by it; at most the jaguar overlaps the lower part of the 7 stem slightly.'
NOTEXT='No text, no words, no letters, no numbers other than the 7 symbol, no buttons, no UI, no watermark.'
run () { echo "== $1" >> "$LOG"; ASPECT="$2" python3 7Wild/oneoff/gen_from_ref.py "$3" "$OUT/$1.webp" "$REF" >> "$LOG" 2>&1; echo "exit=$?" >> "$LOG"; }
run hero-wide-snarl-a 16:9 "$STYLE $JAG $SEVEN $SEP Composition: the 7 sits in the centre-right of the frame; the snarling jaguar head fills the far-right 35% of the frame, partly cropped by the right edge, facing left toward the 7 and the centre. The LEFT 45% of the frame stays calm near-black with only a faint orange haze so a headline can sit there. $NOTEXT"
run hero-wide-snarl-b 16:9 "$STYLE $JAG $SEP Instead of a solid 7, the 7 is built from three thick parallel slanted glossy orange bars with hard light edges. Composition: the bar-7 sits in the centre-right; the snarling jaguar head fills the far-right 35%, partly cropped by the right edge, facing left. The LEFT 45% stays calm near-black for a headline. $NOTEXT"
run hero-mobile-snarl 4:5 "$STYLE $JAG $SEVEN $SEP Composition for a phone screen: the 7 is in the upper-left area, the snarling jaguar head in the upper-right, facing left, cropped by the right edge; the bottom 40% of the frame fades smoothly to solid near-black so headline text can sit there. $NOTEXT"
run promo-tournament 1:1 "$STYLE Instead of the jaguar: a glossy black-and-orange trophy cup with a bold orange 7 emblem on it, standing on a dark plinth, orange light beams and embers behind. Object centred with generous empty dark space around it. $NOTEXT"
run promo-cashback 1:1 "$STYLE Instead of the jaguar: a swirl of glossy orange-and-black casino chips spinning in a circular arrow motion around an empty dark centre, suggesting money coming back, embers and light streaks. $NOTEXT"
run promo-vip 1:1 "$STYLE Instead of the jaguar: a premium matte-black metal membership card with an embossed orange jaguar-head emblem, floating at a slight angle, orange rim light, embers. The card has NO text. $NOTEXT"
run live-roulette 4:3 "$STYLE Instead of the jaguar: a close-up of a real casino roulette wheel in a dark live-casino studio, warm orange lighting, the ball mid-spin, shallow depth of field. No people. $NOTEXT"
run live-blackjack 4:3 "$STYLE Instead of the jaguar: a dark live-casino blackjack table seen from a low angle, playing cards and black-and-orange chips on dark felt, warm orange studio lighting, shallow depth of field. No people, no readable card text. $NOTEXT"
cat "$LOG"
