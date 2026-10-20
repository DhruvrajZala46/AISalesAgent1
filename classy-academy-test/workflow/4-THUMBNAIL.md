# Stage 4 - Thumbnails

The thumbnail is half the click. It must look like OUR thumbnails (measured, below), carry words
the title doesn't use, and show real women, never AI.

Read first: the `yt-package` skill (title and thumbnail are one unit).

## The channel's thumbnail DNA (re-measured 19 Oct 2026 by pixel overlay on the 1.25M, 951k, 698k and 242k uploads)

All 30 uploads use ONE template. `tools/thumb_ce.py` builds it exactly; use it for every video unless the user asks otherwise.

| Part | Exact value |
|---|---|
| Canvas | 1280x720 |
| Photos | 3 real women edge to edge: x 0-402, 404-851, 853-1280, thin light dividers; waist-up or closer, faces in the top third (above the words), centre face to camera; cream/white/black/camel clothes, warm light; one Black woman in most; pure aspiration (no before/after, no cross/tick, no arrows) |
| Top line | Cormorant SC Regular, cap height 54, letter-spacing 2, top y=193 ("How to Look", "The Most") |
| Headline | **League Spartan Bold** (not Montserrat), 166 px, smaller only to fit ~1,110 px, cap top y=296 ("Expensive", "Elegant Hairstyles") |
| Small line | Cormorant SC Regular, cap height 30, letter-spacing 3, 84 px under the headline ("\*Instantly\*", "All Hair Types") |
| Words | the title's own keyword, restated; the three lines read as one phrase. Red underline only under "Never" |
| Depth | soft drop shadow on all text, gentle darkening behind the text block |
| Logo | the channel's logo top-left (box x 59-143, y 43-106); for The Classy Elegance the CE logo |

For a do / don't topic (rules, mistakes), the winners' format is the same woman twice, red cross on the
mistake and green tick on the fix (8.0M "Dressing Rules EVERYONE Should Learn"): `tools/thumb_xo.py` builds it
in our look from two frames of ONE creator's own before/after video (never put a cross on a woman who did not
present that look as a mistake herself). It erases a burned-in caption line and cuts her out (rembg).

For a body-shape / fit / proportion topic, the winners add **lines drawn on her body** (42 body-shape winners: same
woman mistake -> fix 67.5x her channel's median, same woman + lines on her 56.8x and 1.84M median views, shape icons
14.0x; `videos/body-shape/THUMBNAIL.md`): `tools/thumb_shape.py spec.json` builds it - our look, ✗/✓, dashed lines and
small white labels placed in canvas coordinates (render once with `"grid": true` to read them). Draw only what the
woman shows or explains herself. Frame above a burned-in caption rather than erasing it over a bag or a pattern.

`tools/thumb_ce.py` builds exactly this. (`thumb_make.py` used Montserrat and smaller serif lines: superseded.) Never change the layout
to "try something new" without the user asking; the do/don't and body-shape formats below are only for when the user asks for them.

## Visual selection: what the 1.25M, 951k and 698k winners show (decoded 20 Oct 2026; `videos/put-together/THUMBNAIL-v3.md`)

- **Grooming is the hero:**
  - 6 of 9 women have a sleek bun or a sleek ponytail;
  - gold earrings, rings and bracelets show;
  - manicured hands are raised to the face.
- **Clothes are only black, ivory and gold.** No other colour, no busy background (no kitchen, no café clutter, no blue jeans).
- **The mood is calm and aloof:** eyes closed, profile, back of the head, a hat, at most one pair of sunglasses. At most one direct gaze.
  Never mid-speech, never a big smile.
- **Luxury cues:** a Paris street, candles, a car interior, a yacht, designer sunglasses.
- **Crops are tight, head and torso.** The woman fills her panel.
- **The centre face sits above y≈195,** where the top line starts on all three winners (measured: 194-216). The chin may touch the top line.
  A tight close-up portrait cannot be the centre.
- **One Black woman in most thumbnails.**
- **The source:** a creator's own Instagram post, with the author confirmed by Instagram's embed (`tools/ig_pins.py`, `tools/igcheck.js`,
  `tools/embshot.js`, `tools/igslides.js` for multi-photo posts). Brand and jewellery accounts often post AI images: look for the Gemini ✦
  and "AI influencer" or Higgsfield captions.

## Words

- Headline 2-3 words, max 3 words in the big line; together with the top line it reads as one
  phrase ("French Women / Never Wear").
- The channel restates the title's keyword ("How to Look / Expensive / *Instantly*" for "How to Instantly Look More Elegant &
  Expensive"). Follow the channel, not the generic "never repeat the title" lint rule.
- Make three versions: the channel's #1 format, a variant with other words, and an "at any age"
  (40-70+) version.

## Photos - real, named, verified

```bash
cd <scratchpad>/<slug>-thumb; T=/home/user/AISalesAgent1/classy-academy-test/workflow/tools
python3 $T/real_search.py tag="search words" tag2="..."   # drops AI sizes / AI words / small images -> real/keep.json + sheet
python3 $T/crop.py key1 key2 ...                          # crops.jpg: each photo framed like the channel
python3 $T/thumb_make.py T1.jpg "Top Line" "Big Words" "*small line*" key1 key2 key3
```

Every photo is checked by eye before use:
- real photography (skin texture, real hands, real background text), not AI;
- from a real source (the person's own account, a magazine, a known photographer), not a content
  farm (`zentrosy`-type pins were AI);
- the woman matches the promise (e.g. a real, well-known woman of that style for a culture topic;
  women 40-70+ for the "any age" version);
- sharp at 427x720.
Write each photo's source and creator in the package credits.

## Test at feed size

Make a sheet with the three candidates at 320x180 next to 6 real competitor thumbnails from the
same search. The headline must read in one glance and the faces must still be clear.

## Hand back

The three thumbnails (send the files), the photo sources, and which one is recommended and why.
Last line: **ship it, or change it?**
