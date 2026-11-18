# How "7 Things Princess Diana Loved" is edited, and why (18 Nov 2026)

The user asked for the channel's own editing re-checked across all its videos before the build: visuals, animation,
music, sound effects. This file says what was inspected today, what was found, and what the new video takes from it.

## What was inspected today

| Evidence | What it shows |
|---|---|
| YouTube storyboards of 49 of the 56 long videos on Classy Academy and The Classy Elegance (5,572 frames, one every ~5 s), fetched today. 7 more were refused (YouTube rate limit) | layouts, text, products, named women, order |
| The reference video "7 Things Elegant Ladies Never Do in Public" (oHh4T67jJNM): all 80 storyboard frames read by eye | the format this video copies |
| "6 Elegant Summer Shoes Every Woman Should Own": all 89 frames read by eye | how the channel shows products |
| The channel's two measured files, measured frame by frame and with the voice separated in October (`../../edit-style-measured.md`, `../../how-you-edit.md`, `../../VISUAL-EDITING-DNA.md`) | transitions, motion, music level, sound effects |

**Not inspected:** the video files of the reference or of any other upload. YouTube listed the files today but refused
the download (HTTP 403, then "Sign in to confirm you're not a bot"), and no login or token workaround was used. So the
reference's own motion, music and sound are taken from the two measured files.

A colour-based classifier was tried on all 5,572 frames to measure the layout mix automatically. It misread the caramel
and cream backdrops at this size, so its numbers were thrown away; the layouts below are read by eye.

## 1. Layouts (only these are used)

From the reference (all confirmed again today on its 80 frames):
- full-screen clips of elegant women in cafés, restaurants and streets, and film scenes (the hook);
- the title over a full clip;
- a white card per point, the point's name in black script;
- a rounded vertical clip on the blurred caramel backdrop, alone or with the line written beside it;
- the line alone on the caramel;
- rows of three panels (and one row of five);
- a vertical clip on cream;
- the guide over full clips; the outro over clips; the logo on the white end card.

From the shoes video (read today):
- **products cut out on the caramel backdrop, three in a row** (loafers, ballet flats, slingbacks, pumps, sandals),
  next to the white card for each point and rows of women wearing them;
- a framed product photo on the caramel.

From the channel's named-woman videos (`../../VISUAL-EDITING-DNA.md` section 3): a named woman is shown as she is
named, in real photographs and archive film.

Never seen in the reference, so not used: chat bubbles, comment cards, crosses and ticks, word cards, a recap list.

## 2. Pictures

- **Princess Diana:** 49 real press photographs found as Pinterest pins, each read at full size: Balmoral, 6 May 1981
  (green Hunter wellies); the sheep jumper, 1981 and its 1983 replacement; the real 1981 Buckingham Palace letter about
  mending it; the jumper on display at the 2023 sale; her 1980s blue eyeliner; the December 1991 British Vogue cover;
  the light blue suede loafers; the bamboo-handle tote in London; Paris with Bernadette Chirac, 1995; the Lady Dior,
  including the Met Gala, December 1996; the wedding, 29 July 1981. Pins with Getty or agency watermarks were left out.
- **Real archive film of Diana** where it exists (the wedding); none of the actresses from The Crown or Spencer.
- **Products** cut out from brand and retailer photos: the Gommino in beige suede, light blue suede and tan leather;
  the Hunter boot; the Gucci bamboo tote; the Lady Dior; Quelques Fleurs; First.
- **Everyday scenes:** Instagram and TikTok reels found as Pinterest video pins, as the creator does; no free-stock site.
  233 downloaded from 50 searches; 40 left out before download because their accounts appear in earlier videos; 6
  left out because their footage repeats the last Diana video (frame hashes of its 96 clips). Every clip is used once.

## 3. Motion (measured on the channel's two files)

Fade in from black (1.0 s); soft dissolves between clips; fade to white before a card (~0.4 s); card text wipes in left
to right (~1.2 s); panels grow in softly from a corner (0.6-0.8 s), one per spoken item; the caramel backdrop drifts;
photos get a slow push-in so a still never sits dead. Never: zoom punches, shakes, spins, glitches.

## 4. Sound

| | The channel (two files measured) | Last two videos | This video |
|---|---|---|---|
| Sound effects | none | none | **none** |
| Music | one soft, sparse solo piano | "Classical vibes 3" (Mixkit) | **"Gymnopedie No 1", Kevin MacLeod** (Satie; CC BY 4.0) |
| Note onsets per second | sparse | 1.39 | **1.02** |
| Energy below 120 Hz | - | 9.0% | **2.3%** |
| Level over 5-second windows | steady | within 1.0 dB | **within 1.9 dB** (10 dB before evening) |
| Music under the voice | 11.5 and 13 dB | 15 dB | **13 dB** |

**Why this track:** the user has disliked every Mixkit bed, so this one comes from somewhere else: a slow, sparse, very
well-known solo-piano piece, close to the channel's measured bed and almost without low drone. **Honest limit: I cannot
hear.** If it is still not right, the fastest fix is for the creator to name or send the track she uses.

## 5. What the build used, and the checks before the render (18 Nov 2026)

- **65 clips** (8 of them real archive film of Diana), **45 photographs and product cut-outs**, every clip used once
  (`clips.py`, `SOURCES-LOG.md`). 723 s, 137 words a minute, no sound effects, "Gymnopedie No 1" at 13 dB under the voice.
- **Checks:** every used window sheeted at three moments; the last frame of every used clip read; the finished edit read
  at 161 snapshots, then 24 re-checks of every changed screen; a dark-frame scan of all 65 prepared clips.
- **Swapped or cut after those checks:** a scarf tutorial and the clip under the comment ask (both reels end on a company card); a
  brown-liner clip (its caption named a cosmetics brand); a coming-home clip under "usually today" (wrong action, and a
  caption); a folding clip with "FOLLOW ME" text; Diana's close-up (out of its black letterbox, and cut before a
  microphone crosses her face); 6 crops past captions, a box label and a fan watermark; two clips trimmed before a dip
  to black or a shop logo; two overlapping text lines separated; row labels shortened so none is cut off.
- **Left as it is, said plainly:** two screens are the line alone on the caramel for about 9-10 s (the "fashionable
  version" line, and "a soft flat loafer in beige, navy or tan"); no clean clip of a heeled rain boot or of a soft
  loafer in those three colours was found, and the Gommino photographs are already used as cut-outs. The close repeats
  four cut-outs as a recap of the seven things, because the script names all seven there. The perfume-counter clip shows
  an Armani Prive sign behind (every perfume-shop clip found shows a brand name).
