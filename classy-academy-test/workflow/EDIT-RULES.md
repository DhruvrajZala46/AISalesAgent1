# EDIT RULES: copy the owner's videos 99%, every time (written 29 Oct 2026 after the winter v4 was rejected)

The owner's words: "listen to those videos, those clips, that storytelling of visuals... if I use that in my edit,
that means I need it." These rules come from watching her two closest videos second by second, each frame next to
the words being spoken:
- "8 Things Elegant Ladies Never Wear" (My7qteRU9k0, 1.2M views);
- "7 Things Elegant Ladies Avoid in Fall" (Loui0mjLavo).

Study sheets: `winter/study/*.jpg` in the session files; make them again with `tools/sheet1fps.py`.

**They override any idea of mine. If a layout, background or type of clip is in her videos, it is in ours. If it is
not in her videos, it is not in ours.**

## 0. What she loves: her taste in visuals (seen in 4 of her videos, second by second)

Videos: "8 Things Elegant Ladies Never Wear", "7 Things Elegant Ladies Avoid in Fall", "8 Outfit Mistakes That Cheapen
Your Look", "6 Old Money Wardrobe Essentials".

**The women**
- Polished and groomed: glossy long hair (brunette, blonde, black, sometimes silver), soft natural make-up (sometimes a
  red lip), often sunglasses, small gold jewellery.
- Mostly 25-45, with an older woman in many rows (a silver-haired woman in a cream shirt; Milan women over 50).
- Several skin tones in almost every row (Black, Asian, Latina, white).
- Calm and confident: walking towards the camera, turning, a hand in the hair, holding a structured bag or a coffee.
  Mirror selfies and closet try-ons are normal. Never posing awkwardly, never sloppy.
- Even the "mistake" is worn by an attractive, well-groomed woman: the garment is the mistake, not the woman.

**The clothes**
- Neutral, old-money palette: cream, ivory, camel, chocolate, black, navy, grey, burgundy, olive.
- Long wool coats, tailored trousers, fine knits, silk skirts, loafers, knee boots, structured leather bags.
- The mistakes are shown with real examples of exactly that mistake: Gucci-logo outfits, neon sets, big black puffers,
  teddy coats, hoodies with leggings, skinny jeans with ankle boots.

**The places and light**
- European city streets (Paris, London townhouses with white doors and black railings, Milan arcades).
- Bright minimal homes: white panelled walls, herringbone floors, lit walk-in closets, cream sofas.
- Cafes and parks with autumn leaves.
- Soft daylight, warm tones. Never dark, neon or cluttered.

**The shots**
- **Vertical full-length reels** (most of the video): head to toe, the outfit readable.
- **Landscape footage, full screen:**
  - street-style videographer clips (a woman walking, passers-by turning to look);
  - horizontal at-home lifestyle clips (a woman fixing her hair in a cream jacket);
  - beauty close-ups (lipstick, earrings, under a hat) for the guide plug;
  - film scenes of icons (Audrey Hepburn in her hat, Marilyn Monroe in pink).
- **Product cut-outs** on caramel (jeans, trousers, coats, knits), building in rows, or a cut-out model on cream with
  small serif labels ("Bulky coat / Oversized hoodie / Tight leggings").
- **Detail close-ups only rarely**, for the exact detail named (a sweater rib, a label).
- **A small creator caption** in the reel is accepted ("Don't do this / Do this"). Big titles and ads are not.

**Never seen in her videos:** abstract b-roll (animals, raw wool, water drops, hands in a sink), empty rooms, men or
children as the subject, dark or moody footage, low-resolution or blurry clips, AI clips.

## 1. The backdrop: keep it

- **Explanations sit on the soft caramel blurred backdrop.** This is a drifting warm gradient, not a blurred copy of
  the clip. She uses it for most of the video (40% of the time in her top six).
- **Never remove it to "fill the screen".** v4 did, and was rejected.
- **The "instead" part may sit on cream/white** (her newer fall video):
  - framed reels with gaps between them;
  - labelled product cut-outs on cream;
  - a single reel centred on white.

## 2. Never zoom a vertical reel to full screen

- **Full-screen is only for true landscape footage:**
  - street-style videos filmed horizontally, with passers-by in the frame;
  - film scenes;
  - landscape lifestyle clips (a woman at home, the guide plug).
- **A vertical reel is always a tall panel** on the backdrop. It is never blown up to 16:9, and never shown on a
  blurred copy of itself.
- `edit.py` must refuse a full-screen clip whose source is not landscape.

## 3. What a visual is: a woman, head to toe, wearing the exact thing said

- **The default picture is a full-length outfit reel:**
  - one woman, head to toe;
  - a street, a mirror selfie, a closet try-on or a bright home;
  - wearing **the exact garment combination the line names**.
- **Every word that names a thing must show that thing:**
  - "big bulky puffer" shows three women in big bulky puffers;
  - "ankle boots and skinny jeans" shows three women in ankle boots and skinny jeans;
  - "a chunky sweater squeezed under a fitted coat" must show a visibly bulky knit under a tight coat. A normal
    sweater under a trench is wrong.
- **Proof by repetition.** One row holds 2-4 *different* women wearing *the same* named item. The viewer sees the
  pattern, not one example.
- **Close-ups only where the line is about a detail she would show close:**
  - a label;
  - pilling;
  - a sole;
  - a cut-out product.

  Never an abstract shot (sheep, wool roving, water drops, hands in a sink) in place of a woman wearing the item.
- **Product cut-outs** (photos with the background removed, on caramel or cream) are for a list of pieces to wear:
  "Layer a thin turtleneck, a sweater or a fitted long sleeve" shows each garment cut out, one per word, with or
  without a small serif label.
- **Named women are shown** (Audrey, Marilyn, the Princess of Wales): film scenes or photos, in a row or full
  screen.
- **Taste:**
  - women 25-60, several skin tones;
  - polished, old-money, neutral palette (camel, cream, black, chocolate, grey, burgundy);
  - soft daylight, cities and bright homes.
- **Never:**
  - men;
  - kids;
  - shop ads;
  - captions in other languages;
  - AI clips.

## 4. Storytelling: the row tells the whole sentence, before, during and after

- **A row builds left to right, one panel per spoken item, and stays for the whole sentence (6-15 s).**
  - Panel 1 sits in slot 1 and the rest is backdrop until panels 2, 3 and 4 grow in on their words.
  - The whole row is the sentence's picture: what came before the current word stays on screen and still fits.
- **The mistake, then the swap:**
  - the problem rows (caramel);
  - then "Instead..." as one reel, or the good examples on cream;
  - same garment family, done right. The swap must visibly answer the mistake: puffer, then a structured wool coat;
    bulky knit, then a fine knit under a coat.
- **A new layout only at a new sentence or idea.** Not every 2 seconds.
- **The principle line:** white serif with one word in script, on the bare backdrop or beside a reel ("True
  elegance *whispers* / It doesn't shout").

## 5. The fixed parts (unchanged, measured)

- **Hook:**
  - full-screen landscape street style;
  - then a white "in today's video..." card;
  - then "Episode N" and the title in white script over a landscape scene;
  - then the first rows.
- **Number cards:** white, black script wipes in left to right, about 3 s, on the spoken "Number one...".
- **Guide plug:** a landscape close-up of a woman, haze, "Check the description for / Personal Stylist Guide".
- **End:** a white card with the logo.
- **Logo:** top-left on every non-white screen.
- **Motion:**
  - panels grow from their corner, 0.6-0.8 s;
  - a single reel grows from the centre, 1.2 s;
  - dissolves of about 0.4 s;
  - no zoom punches, shakes or glitches.
- **Sound:** one soft piano bed, about 12 dB under the voice. No sound effects.

## 6. Sourcing: find new, find right

- **Search per garment combination**, the way she would ("chunky knit sweater under coat outfit video", "puffer
  coat outfit video"). Search per mood only for the hook.
- **Go deeper than the first page:** Pinterest bookmarks (`tools/pinsearch2.py`), several phrasings, related pins.
- **Use YouTube street-style channels** for landscape footage.
- **Keep a clip only if:**
  - it shows a woman in the exact item;
  - it is head to toe (or a detail close-up the line asks for);
  - it is sharp at 640x1080;
  - there is no text, no logo and no ad;
  - it has not been used in an earlier video.
- **Check every pick on three full-size frames** plus the AI scan (`LEARNINGS.md`).

## 7. The check before delivery

- Make a 1 fps sheet of the render with the spoken words under each frame.
- **For every line, ask: would a viewer with the sound off know what the sentence is about?** If not, replace the
  visual.
- **Compare a 2-minute stretch side by side with the same stretch of her video:**
  - backdrop;
  - panel sizes;
  - how many women per row;
  - how long a row holds;
  - full-screen only for landscape clips.
