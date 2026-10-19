# How the channel's videos are made: the 30 uploads, watched second by second (19 Oct 2026)

The owner asked for a deep study before any edit: every video watched with its sound, second by second, best performers first.
No overviews and no guessing. This file is that list. Every rule below was seen in the videos and carries times as evidence.
Rules marked **(all)** held in every video that has that moment.

## How the study was done

- **Downloads:** all 30 public uploads at 480p with their sound, YouTube captions, stats and storyboards.
  Folder: `scratchpad/hairvid/own/`. Kit: `workflow/tools/study.py`, `resheet.py`, `sound_quick.py`, `sound_study.py`.
- **Per video:**
  - one frame per second, on readable half-minute sheets, each frame labelled with the layout, cut or dissolve, and the words spoken in that second;
  - every picture change measured at 10 fps;
  - loudness per 50 ms;
  - for the Hairstyles video, the voice and the music separated (Demucs) to measure the music bed exactly.
- **Watching:** 11 watchers read every half-minute sheet of 2–3 videos each, from the first second to the last. They pulled full-size frames
  for any small text or transition and wrote a full timeline, 76–213 entries per video, about 4,300 in all.
- **Records:** the notes are in `videos/expensive-hair/channel-study/notes/<id>.json`, and the per-video numbers are in `channel-study/table.json`.

## The 30 videos, best first

| # | Video | Ep. | Uploaded | Views | Likes | Comments | Changes/min | Loudness |
|---|---|---|---|---|---|---|---|---|
| 1 | 8 Things Elegant Ladies Never Wear (My7qteRU9k0) | 5 | 2025-05-28 | 1,251,210 | 27,858 | 574 | 13.5 | -17.5 LUFS |
| 2 | The Most Elegant & Easy Hairstyles (A-JRkjQs2XI) | 3 | 2025-01-31 | 951,434 | 24,241 | 429 | 15.5 | -19.3 |
| 3 | How to Instantly Look More Elegant & Expensive (QOEUbAZB07o) | 7 | 2025-06-30 | 697,719 | 16,360 | 293 | 16.4 | -16.6 |
| 4 | How to Dress Elegant: A Beginner's Guide (q78t2KbuePk) | 2 | 2024-11-15 | 636,062 | 15,692 | 333 | 12.4 | -18.7 |
| 5 | 7 Things Elegant Ladies Never Do in Public (oHh4T67jJNM) | 16 | 2026-01-24 | 497,571 | 11,767 | 171 | 14.9 | -21.9 |
| 6 | 10 Signs You're an Elegant Woman (RiTnYAqtD68) | 6 | 2025-06-11 | 387,580 | 11,135 | 255 | 16.3 | -17.7 |
| 7 | 6 Ways to INSTANTLY Sound More Elegant (RUDXBR8nyHw) | 14 | 2025-12-11 | 332,952 | 16,293 | 187 | 16.0 | -21.3 |
| 8 | 7 Body Language Habits (r_mYSc7FHvk) | 22 | 2026-04-30 | 315,610 | 9,284 | 174 | 13.2 | -22.3 |
| 9 | 8 Color Combos (sgKAHqv3krg) | 11 | 2025-10-17 | 295,953 | 6,755 | 110 | 12.5 | -22.2 |
| 10 | The Most Elegant Haircuts for Every Hair Type (g_e16qpg9HA) | 15 | 2026-01-04 | 242,230 | 7,153 | 153 | 12.1 | -22.2 |
| 11–30 | the other 20 (all in `table.json`) | 1–30 | 2024-11 → 2026-09 | 30,728–168,362 | | | 10.9–20.1 | -16.9 to -22.3 |

The latest upload of the numbered series is Episode 30 ("How to Own Any Room", 2026-09-03). The 2026-09-23 video is a separate
"Classy Academy Lookbook / Episode 01". **The next video in the main series is Episode 31.**

### What the winners do that the rest don't (numbers, not opinion)

- **More time on caramel with one centred vertical clip.** The top 4 spend 23–51 % of their seconds in this layout.
  Most 2026 uploads spend 11–15 %.
- **Calmer cutting.** The top 4 change picture 12.4–16.4 times a minute. The two newest low performers change 17.5–20.1 times.
  OSAN1fG23P8 (31k) cuts every 3.0 s and carries the most text, against 4.8 s and 3.7 s for q78t and RiTn.
- **Long single-creator holds.**
  - Hairstyles holds one TikTok tutorial for 25–44 s per style.
  - My7 holds one try-on reel for 6–12 s per point.
  - Haircuts, the weaker hair video, holds its tutorials for 7–22 s.
- **Louder masters.** The top 4 are at -16.6 to -19.3 LUFS. Most 2026 uploads are at about -22.
- **Famous women as unlabelled examples, often.** RiTn has one about every 1–2 minutes. oHh4 uses about 25 film, celebrity and royal clips.

## The format, rule by rule

### 1. Opening and hook (first 15–35 s) — (all)

- **Voice from the first frame.** The voice starts at 0.0–0.4 s, with no music intro and no title first (sound_quick: first word at 0.0–0.6 s in all 30).
- **No text in the hook,** except the CA logo. The newest videos open on footage with no text at all.
- **One picture per spoken line, about every 2–5 s,** joined by soft dissolves.
  - Pictures: FULL creator clips, film scenes, a royal or celebrity clip, and sometimes one caramel-centred clip or a 3-panel row.
  - Examples: MVrYflIex4c has 12 FULL clips in 33 s; Hairstyles has 3 pictures in 10 s; My7 has 5 in 24 s.
- **The pictures act out the words literally.** "Turns heads" shows strangers turning (q78t 0:04, My7 0:08). "Born with it" shows an heiress (-1BAN 0:04).
- **Hook wording:**
  - a question or a myth, then the twist ("It's not X, it's not Y. It's…");
  - then the promise.

### 2. "In today's video", title, first guide mention

- **"In today's video" card:** white card, black script, written on left to right.
  Hairstyles 10.3–13.2, My7 0:24, QOE 0:16, MVr 0:33.8, Haircuts 10–12.2, -1BAN 0:31, rHI 0:28.5.
  Most newer videos instead show the title over the "today you'll learn" line (MNEo 0:24.6, mFLq 0:21).
- **Title** — (all numbered videos):
  - "Episode N" in small white serif, above a short white script title, centred, over a FULL clip that is often darkened;
  - it writes on and holds 3–6 s;
  - the title is a short form of the YouTube title: "Elegant Haircuts", "10 Habits of an Elegant Woman", "8 Habits That Command Respect".
- **First guide mention ("linked below"):**
  - it comes right after the title, often still under it (MVr 0:46);
  - when it has its own shot, it is the 3-line guide call-out (§9).

### 3. Points: the white card — (all, except the lookbook and the Episode 1 colour video)

- **Card look:**
  - plain white;
  - black calligraphic script "N. Title" in Title Case, one line, centred, about 40 % of the frame wide;
  - written on left to right in about 1 s;
  - held 2.5–7 s, typically 3–5 s.
- **Before the card:** the picture fades or dissolves to white, sometimes through a one-frame caramel flash.
- **Reading the card:**
  - 2024–25 winners: the narrator reads the title ("Number one, loud, oversized logos", My7).
  - Newer uploads (MNEo, mFLq, oHh4, HhJI, -pOz): the title is never read. The first sentence of the point is spoken over the card.
- **Leaving the card:**
  - the text fades, then a hard cut (MNEo, all 8 cards) or a short dissolve through caramel or cream (Haircuts);
  - RiTn exits with a 3–4-step "flash-dim" into caramel.
- **What follows the card:** a FULL clip that acts out the first example, or a caramel-centred clip.
  Hairstyles: "after the card a film scene or a celebrity row, never the tutorial first".

### 4. Inside a point (MNEo, the most regular)

Each point follows this order:

1. Full-frame clips.
2. Caramel-centred clips or photos.
3. Caramel rows built one panel at a time.
4. A caramel split quote that rewords the voice, with its last words in script.

The point closes on:

- a quote (MNEo, mFLq, RiTn, oHh4, Haircuts, -dfv);
- or the finished result with a one-line verdict ("absolutely stunning", "it's that simple": Hairstyles);
- or a calm FULL clip held 4–8 s.

The point then fades to white for the next card.

### 5. The layouts, with measured geometry (1920×1080 equivalents, measured on 854×480 frames)

- **FULL:** vertical creator clips are cropped to fill. There is no blurred filler anywhere.
- **CARAMEL + centre:**
  - one vertical clip about 608 px wide (27–35 % of the width), full height, on the blurred caramel;
  - clips change by dissolve or hard cut;
  - it sometimes grows from small (RiTn 1:12, RUDX 2:37, Hairstyles photo 127–129).
- **ROW of 3:**
  - three 608 px vertical panels with 48 px caramel gutters, edge to edge (MNEo 1:26: gutters at 271–291 and 562–583 of 854);
  - older videos have them touching (Hairstyles);
  - each panel fades or pops in its slot on its spoken item, about 1 s apart.
- **ROW of 4:** four touching panels, each a quarter of the width (QOE 4:07, RiTn 5:35, B5jf 0:16).
- **ROW of 2:** two framed near-squares (about 853×846) with about 100 px between them and caramel all round (MNEo 2:49).
- **SPLIT:**
  - the clip fills the left 42 % (about 810 px);
  - the quote sits centred on the caramel right, white serif with the key words in white script;
  - each line is revealed left to right as it is spoken (MNEo 1:09, 2:07, 2:59, 3:39; -dfv; rHI);
  - also used for the comment question as text (MNEo 7:51).
- **QUOTE on caramel:** the same text style, centred, full frame (MNEo 2:25, 5:45).
- **CREAM:**
  - flat cream (about RGB 239,237,233) for "teaching" screens;
  - black serif with black script key words (MNEo 1:30, 4:07);
  - cream centred photos (MNEo 1:27);
  - "Ask your stylist for:" splits (Haircuts 2:19, 2:24, 3:41, 6:52).
- **STRIP:** 5–10 small photos, one per spoken hair type or style. New in Haircuts (44.5–52.9, 248–261, 453–470).
- **Rounded frames:** rounded-corner photos and clips on caramel or cream (Haircuts, oHh4, bYdm).
- **Logo:**
  - white CA monogram with a tiny spaced "Classy Academy" line under it, top-left on every picture (measured: about 166 px wide, 47 px from the left, 51 px from the top);
  - never on white cards.

### 6. Pictures follow the words exactly — (all)

- **One picture per item, on the item's word:**
  - rows build one panel per spoken item ("coffee date / business meeting / formal event", RiTn 2:57–3:00);
  - product cut-outs pop in one per word (q78t, B5jf, 1GLu);
  - each colour in a list gets its own panel (My7 1:48–1:54).
- **Every instruction gets its own picture showing that exact gesture** (r_mY, 316k).
- **Inclusivity is shown on the exact words:**
  - "with all hair types" shows a sleek bun, a coily updo and a straight twist (Hairstyles 66.4–70);
  - "flattering on everyone" shows a dark-skinned woman, a light-skinned woman and a woman of 55–65 with grey hair (122–126);
  - different ages (20s to 60s+) and skin tones appear in almost every row.

### 7. Named and famous women

- **No name is ever written on screen** — (all).
- **When the voice names a woman,** her picture lands exactly on her name:
  - a FULL film scene of about 3 s (Hairstyles: Audrey Hepburn 42.3, Grace Kelly 45.4, Marilyn Monroe 291.6);
  - or her photo is added to a row on her name (Haircuts 361–364, My7 2:27, HhJI 5:40).
- **Famous women also appear unnamed,** as one panel among ordinary women or as a FULL interview or film clip:
  Kate Middleton, Audrey Hepburn, Grace Kelly, Monica Bellucci, Amal Clooney.
- **Real voices:** twice the narration pauses so the real voice is heard (RUDX: Breakfast at Tiffany's 0:33, Diana's interview 1:48).

### 8. Tutorials and demos

- **Hairstyles:** each style gets ONE creator's TikTok tutorial, held on caramel-centre for 25–44 s.
  - The narration describes each step as it happens.
  - It starts on the finished result ("to create this classic look").
  - There are no cuts inside it except the creator's own.
  - Once, a 3 s music-only pause lets an action play (260–263).
- **Elsewhere:** one creator's reel is held 6–15 s when it acts out the point (My7 6–12 s, RiTn 10–14 s, QOE 6–10 s).
- **Tutorial with swapping side panels (QOE 4:34–4:59):** the centre tutorial plays while the side panels swap to match each spoken variation.

### 9. Guide, like and comment asks

- **Guide call-out:**
  - a darkened FULL clip carrying "Check the description for" (small serif), "Personal Stylist Guide" (large script) and "www.classyladyacademy.com" (small serif);
  - the newest videos add a QR code in the end mention;
  - placed mid-video after the most related point (QOE: after the hair point, "the exact hairstyles, colors, and clothing that flatter you best"; Haircuts 5:01–5:32), and again at the end.
- **Comment and like asks:**
  - no text and no graphics: the voice over calm clips ("A simple like or comment would truly mean so much to us", "let us know if you'd like a part two");
  - MNEo shows the comment question as split-screen text;
  - **no subscribe ask** (all).

### 10. Ending — (all)

- **Last 30 s:**
  - calm FULL clips, often one held 15–19 s under the thank-you (Hairstyles 467.5–486.7, B5jf 18 s, My7 15.8 s);
  - often the opening clip again as a bookend (q78t, WWIJ, HhJI, mFLq).
- **Goodbye:** "Until next time. Bye, my loves", "bye everyone" or "Goodbye, my dears".
- **Then the end card:** a dissolve (often through beige) to a **white card with the tan CA monogram and the spaced "Classy Academy" line**, centred (about 438 px wide).
  - It is held about 6–40 s, typically 10–12 s.
  - **There is no black card in any of the 30.**

### 11. Text — what never appears

- **Never added by the channel:**
  - no on-screen subtitles in 26 of 30 (burned-in captions only in sgKA, -1BAN, o-X and part of eDGH);
  - no celebrity names, product names or ticks and crosses;
  - creator credits are rare: "@handle via TikTok" for the Hairstyles tutorials, q78t's single 15 s demo (4:45–5:00) and o-X's single demo (6:33).
  - No credits at all in Haircuts, QOE, MNEo, RiTn or most of the 2026 uploads.
- **Left in:** the creators' own captions and watermarks are left in the clips ("Do this ✅", "how to tie your sweater").

### 12. Transitions and motion

- **Changes:** mostly soft dissolves of 0.4–1.2 s (median 0.6–1.3 s per video, measured).
  - Hard cuts mainly within one creator's reel, between centred clips, and out of white cards.
  - Long dissolves of 3–12 s only in the hook, film scenes and the outro.
- **The "caramel flash":** one frame of caramel between clips (mFLq, about 27 times).
- **Stills:** mostly static, some with a slow push-in of about 5 % over 4 s (mFLq centred photos, q78t 4:33).
- **No effects:** no whooshes, no zoom transitions, no sound effects.

### 13. Sound

- **Voice:** one calm, warm female narrator at about 152–169 wpm; small natural slips are left in.
- **Music bed:** very soft and continuous, about 20 dB under the voice.
  - Separated stems of Hairstyles: 15.7 dB. Mix floors of the others: 18–25 dB.
  - Some videos are almost voice-only.
  - No swells inside the video, no ducking, **no sound effects** (all).
- **End:** the voice and the bed stop together, then 0.3–0.6 s of digital silence.
  Then the same short logo sting on the white end card, the same notes in every video: about 5 s, about 6.5 LU louder than the voice, then digital silence to the end.
  - Measured in MNEo, -pOz, rHI, -1BAN and DVRB.
- **Programme loudness:** -16.6 to -19.3 LUFS in the top 4; about -22 in most 2026 uploads.

### 14. Where the footage comes from (by eye, all 30)

- **Mostly creators' vertical TikTok and Instagram reels:** outfits, hair tutorials, routines.
- **Also:**
  - classic and recent film scenes (Audrey Hepburn, Grace Kelly, Marilyn Monroe, Devil Wears Prada, Friends);
  - royal and celebrity press photos and interviews;
  - a few stock-like lifestyle clips.
- **Reuse:** the same clips are reused across videos and within one video.
- **Possible AI images:** watchers flagged a few possible AI images (QOE 5:04, rHI 0:46, L251 lookbook). They are the exception, and our rule stays: real footage only.

## Hair videos specifically (Hairstyles 951k, Haircuts 242k, QOE point 4, HhJI)

- **Hook template:** the hook script is the same in both hair videos, word for word ("hairstyle" became "haircut").
  Hook, then "In today's video", then 2–3 FULL hair clips, then the title.
- **Each style or cut:**
  1. a lead-in clip or row;
  2. the white card;
  3. a film scene or celebrity row;
  4. the creator demo (long in Hairstyles);
  5. a verdict line or quote;
  6. a dissolve through caramel or white.
- **Proof by hair type:** every point shows a row or strip, in the order of the words.
- **The hair point sells the guide:** QOE pitches the guide right after its hair point, "the exact hairstyles, colors, and clothing that flatter you".

## Applied to Episode 31, "Why Her Hair Always Looks Expensive"

All of the above is built into `videos/expensive-hair/project`:

- `render.py`: the formats and geometry above;
- `build_timeline.py` and `overrides.json`: which layout is used where;
- `mix.py`: the sound above.

Where the video differs from the channel, it is listed in `videos/expensive-hair/EDIT-PROMISE.md`, "What cannot be identical": the voice, the music, the fonts.
