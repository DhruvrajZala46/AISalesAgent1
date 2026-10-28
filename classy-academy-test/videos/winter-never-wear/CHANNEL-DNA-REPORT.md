# Channel visual and editing DNA: measured 28 Oct 2026

**Channel:** Classy Academy (@ClassyAcademy, channel ID UCJUn02MVnahA9My9-DUkTBQ, 135K subscribers).

**What was analysed.**
- All 31 long uploads and 6 of the 7 Shorts, downloaded at 360p with the owner's cookies for analysis only. One Short (1TmBO5FuzE8) returned HTTP 403 twice and was **not analysed**.
- For each video:
  - hard cuts (ffmpeg scene detection);
  - a frame every second, classified as white / caramel / picture;
  - a contact sheet with one frame every 3 s (`winter/an/<id>_sheet.jpg`);
  - EBU R128 loudness.
- The voice and music of "7 Things Elegant Ladies Avoid in Fall" (the closest format to this winter video) were separated with Demucs (htdemucs) and measured on their own.
- The motion timings come from the frame-by-frame study of "8 Things Elegant Ladies Never Wear" (`how-you-edit.md`), and were checked again on today's contact sheets.

**Limits.**
- Scene detection counts hard cuts only. Soft dissolves and panels growing in are not counted, so the "cuts per minute" figures below are lower bounds.
- At 360p, very small text cannot be read.

## 1. Numbers (31 long videos)

| Measure | Channel median | Range | Top 6 by views |
|---|---|---|---|
| Length | 8:37 | 4:15-10:50 | |
| Hard cuts per minute | 4.9 | 0.9-12.1 | 3.6 |
| Median shot between hard cuts | 5.3 s | 2.9-26.3 s | 3.9 s |
| Time on white cards | 10% | 0-21% | 9% |
| Time on the caramel blurred backdrop | 21% | 0-57% | **40%** |
| Loudness (integrated) | -21.7 LUFS | -22.4 to -16.6 | -18.2 |
| Voice above the music (speech vs. music-only floor) | 17.2 dB | 10.1-23.1 dB | 15.7 dB |

The most-viewed videos spend about twice as long on the caramel backdrop and cut less often than the rest. They are calmer.

## 2. Layout grammar (seen on the contact sheets of every wardrobe video)

1. **Hook, 0:00-0:25:** full-screen vertical street-style reels of one polished woman (coat, blazer, sunglasses). Each fills the frame over a blurred copy of itself.
2. **"In today's video…"** as black script on a white card, wiping in from the left.
3. **Episode title over a clip:** "Episode 9" in a small serif, with the title in large white script (for example "7 Things Elegant Women Never Wear in Fall").
4. **Each point:**
   - A white card, "1. Oversized Puffer Coats", in black script, about 3 s, on the spoken "Number one…".
   - Then the **caramel blurred backdrop** with **rows of 2-4 tall vertical reels** that grow in one by one on the spoken items: the mistake first, then the swap.
   - **Single centred reels** for the "Instead…" part.
   - One **principle line on caramel** in white serif with one word in script ("Elegant women choose tones that feel more *refined*…").
5. **Guide plug:** a full-screen clip with "Check the description for / *Personal Stylist Guide*", in white serif and script.
6. **End:** a white card with the logo.

**Logo:** the "CA" monogram, top-left, on non-white screens.

**Recent videos only:**
- a flat taupe or chocolate background with gaps between panels;
- labelled product cut-outs on white ("Bulky coat / Oversized hoodie / Tight leggings", Avoid in Fall 5:51-6:15);
- an app-promo segment ("Your Personal Virtual Fitting Room", Avoid in Fall 3:00-3:27).

## 3. Footage DNA

- **Mostly creators' vertical fashion reels** from Instagram, TikTok and Pinterest: one woman, outfit-led, softly lit city streets or cream interiors, with warm neutral colours (camel, black, cream, chocolate, burgundy).
- **Classic film and TV scenes** where a line calls for an icon. Seen on the sheets:
  - Marilyn Monroe, "Diamonds Are a Girl's Best Friend" (*Gentlemen Prefer Blondes*, 1953), "8 Things…" 2:27-2:33;
  - Grace Kelly in a convertible (*To Catch a Thief*, 1955), "7 Ways to Be More Confident…" 6:48;
  - an evening-party film scene, same video 0:00-0:12;
  - a black-and-white ballroom scene, same video 0:51-0:57.
- **Close-ups of the detail being named:** jewellery on a hand, a sweater rib, a shoe on a step.

## 4. Motion DNA (measured frame by frame on the #1 video; consistent on today's sheets)

- **Fade-ins and fades:**
  - fade in from black, 1.0 s;
  - short dissolves between clips;
  - fade to white, 0.4 s, before each number card;
  - number-card text wipes in from left to right in about 1.2 s and fades out in 0.5 s.
- **Panels:** each grows from its corner (about 55% to 100%) while fading in, over 0.6-0.8 s, one per spoken item. A centred clip grows from the centre over 1.2 s. The caramel backdrop drifts slowly.
- **Never:** zoom punches, shakes, spins, glitches, or fast animation.

## 5. Sound DNA

Measured on the separated stems of "Avoid in Fall":
- **Levels:**
  - voice -18.9 dBFS while speaking;
  - music under the speech -38.5 dBFS, so about 19-20 dB under the voice;
  - music in the pauses -32.1 dBFS.
- **Timing:** the music starts at 0.5 s with the first word and ends about 5 s after the last word.
- **Character:** soft and warm. 87% of its energy is below 300 Hz, it has almost nothing above 4 kHz, and there are no drums.
- **Sound effects:** none at the cuts. At 17 of the 18 cuts, the high-frequency band of the music stem is between -60 and -73 dBFS, which is silence-level; a whoosh would reach about -30. One quiet event sits at 0:57 (-37.5 dBFS).
- **Earlier measurements agree:** the #1 video and "Old Money" show music 11.5-13 dB under the voice, steady, with no sound effects (`edit-style-measured.md`).
- **Rule for this video:** one soft instrumental bed, about 12-14 dB under the voice, steady, from the first word to the end card. No sound effects. Film scenes are used **silent**, under the voice-over.

## 6. Current logo (analysed for the redesign)

- **YouTube avatar:** a "CA" monogram (high-contrast serif C overlapping an A) in light taupe on white, a thin gold ring, and "Classy Academy" in a widely spaced sans.
- **At 48 px and 32 px:** the taupe-on-white monogram fades, and the wordmark is unreadable.
- **New name:** the script announces "The Classy Elegance". The repo already has its "CE" mark in the same monogram style, in camel and white versions (`workflow/assets/logo_ce*.png`).
- **The redesign directions** (in `logo/logo_options.jpg`) keep that monogram and fix the small-size problem. They wait for approval; nothing has been changed on the channel.
