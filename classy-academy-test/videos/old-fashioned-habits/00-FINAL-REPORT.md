# Final report: "7 Old-Fashioned Habits That Make Any Outfit Look Expensive" (27 Nov 2026)

## The deliverable
- **File:** `old-fashioned-habits_final.mp4`
  - 1920x1080, 30 fps, H.264, AAC 48 kHz, 271 MB;
  - kept in the session work folder `DELIVERABLES/` (media is never committed).
- **Duration: 6:37.70** (397.7 s), inside the 6:00-7:00 limit.

## 1. Why this topic was selected (`01-TOPIC-RESEARCH.md`)
- **Data:**
  - fresh public listings of 59 niche channels (3,432 long videos), each video scored against its own channel's
    median;
  - exact view, date and subscriber counts for 22 reference videos;
  - top comments on three of them;
  - YouTube autocomplete;
  - Google Trends (YouTube search, 5 years).
- **The format:** a numbered *habits* list has the widest proof: 24 winners at 5x or more from 14 channels in 12
  months.
- **The promise:** "always looking polished / expensive" has the highest evergreen median (1.35x). Its lead example
  got 1,151,081 views on a 92,500-subscriber channel (Julianna Lee, published 25 Sep 2026).
- **Search demand:** "look elegant" has grown every year in YouTube search (Trends 3.8 to 6.8).
- **Viewer comments:** they name the habits used here: posture (4,100 likes), ironing (592), hair and care of
  clothes. One comment calls them "everything they used to teach at charm school".

**Not proven:**
- the "old-fashioned" angle itself;
- there are no absolute search volumes (vidIQ has 0 credits);
- one "put together habits" video flopped (0.04 views per subscriber);
- the reference creator's own habits videos have a median of 0.9x.

## 2. How it follows the Classy Academy style (`../../STYLE-DECODE-5-videos.md`)
- **Palette:** caramel `#C48D5D` as a *moving* blurred-light backdrop, white `#FFFFFF`, cream `#F7F5F1`, ink
  `#0B0B0B` (`05-FONTS-COLOURS.md`).
- **Type:**
  - Pinyon Script for the number cards and the "feeling" half of each principle line;
  - Prata for the plain half;
  - spaced Cormorant capitals for the thread-colour labels.
- **Layouts:**
  - white number card with a left-to-right script write-on;
  - clip on the left third with the principle line on caramel;
  - panels that grow from the top, one per spoken item;
  - single clip framed on cream (square corners, no shadow);
  - white quote cards;
  - full-screen footage;
  - title over footage.
- **Pace:** something on screen changes about every 2-3 s, mostly with cuts and 0.3 s dissolves. There are no
  zooms, shakes, glitches, emoji or sound effects.
- **Captions:** no subtitles; only the number cards, one principle line per point, and colour labels.

## 3. Assets used and their permission status
- **Film footage:** 96 uses from **11 public-domain films** in the Prelinger Archives on the Internet Archive.
  Every item carries the archive's public-domain mark.
  - `SOURCES.csv` has one row per use: video time, film, source in/out, item URL, file URL, resolution, rights,
    attribution.
  - The films: *How to Be Well Groomed* (1949), *Habit Patterns* (1954), *Speech: Platform Posture and Appearance*
    (1949), *Body Care and Grooming* (1948), *Office Etiquette* (1950), *Aristocrats of Fashion* (c. 1940),
    *Fashion Horizons* (1940), *Design for Dreaming* (1956), *The Girl on the Magazine Cover* (1940), *Harper's
    Bazaar Talks Fashion* (c. 1971), *A Story of Shoes II*.
- **Removed before export:**
  - *Charade* (1963) and *Royal Wedding* (1951): public domain in the US only, with unclear music and
    story rights;
  - all Pinterest, Instagram and TikTok footage: no permission could be obtained from here.
- **Music:** Chopin Nocturnes Op. 55 No. 2 and Op. 72 No. 1 from Musopen's complete Chopin collection, released
  under **CC0**. The bed sits ~12.5 dB under the voice and stays steady.
- **Voice:** Kokoro-82M (Apache-2.0), voice `af_heart`, speed 0.80. ElevenLabs had only 2,783 characters left.
- **Fonts:** Pinyon Script, Prata, Cormorant (SIL Open Font License).
- **Logo:** your uploaded file (1254x1254 JPEG, sha256 `4b3b3c04…`).
  - It is only resized, keeping its proportions: never recoloured, cut out, faded or redrawn.
  - Corner: 104 px, top-left, on footage, caramel and cream screens; left off the white cards.
  - Intro (~2 s) and end card (~12 s): centred on black.
  - The Classy Academy CA monogram is not used anywhere.

## 4. Quality control on the final file
| Check | Result |
|---|---|
| Duration | 6:37.70 ✔ |
| Spoken words vs script | Whisper transcript vs script: 98.8% word match. The differences are digits ("1940s") and spelling ("grey"). Two lines were rephrased earlier for pronunciation. |
| Captions synced | Every caption is timed to a word timestamp from the voice. |
| Fonts | Rendered from the font files; checked on stills. |
| Colours | Backgrounds drawn from the decode's hex values. |
| Animations | Write-on, panel growth, dissolves and fade-to-white checked in second-by-second sheets. |
| Black frames | Only the two logo cards (0:00-0:02 and 6:26-6:37), which are black on purpose. |
| Frozen picture > 4 s | none |
| Stretched footage | none: 4:3 films are shown full height over a blurred copy, or cropped in proportion. |
| Loudness | −14.2 LUFS integrated, true peak −1.2 dB |
| Silence | only the first 2 s logo card |
| Repeated footage | none, except the deliberate recap callbacks |
| Copyright | only public-domain-marked films, CC0 music and an Apache-2.0 voice |
| Every visual traceable | yes, `SOURCES.csv` |
| Whole video watched | yes: second-by-second contact sheets of the whole render, plus 2 fps spot renders of every fix |

## 5. Remaining limitations
- **Rights are the archive's determination, not a legal opinion.** The Internet Archive says it can't guarantee
  rights information.
  - *Harper's Bazaar Talks Fashion* has no date or creator on its archive page. The magazine's name is not shown
    on screen.
  - *Design for Dreaming* and *The Girl on the Magazine Cover* are sponsored films with brand context (GM,
    Chevrolet). Only shots without logos are used.
- **YouTube may still raise automatic claims** on public-domain films that others have uploaded. If one appears,
  dispute it as public domain, citing the archive item URL in `SOURCES.csv`.
- **The source films are 640x480.** They are sharp enough at full height, but softer than modern footage.
- **The narration is synthetic.** Consider YouTube's altered-or-synthetic-content disclosure and a line in the
  description.
- **No Pinterest, Instagram or TikTok creator footage is in the video**, by your copyright rule.

## 6. Where everything is
- **In git, under `classy-academy-test/videos/old-fashioned-habits/`:**
  - this report;
  - `01-TOPIC-RESEARCH.md` and `research-data/`;
  - `03-SCRIPT.md` (with fact sources);
  - `04-STORYBOARD.md`;
  - `05-FONTS-COLOURS.md`;
  - `SOURCES.csv`;
  - `CREDITS.txt`;
  - `project/`: the renderer (`engine.py`, `scenes.py`, `edit.py`, `voice.py`, `mix.py`, `qc.py`,
    `render_all.sh`) plus `beats.txt`, `beats.json` and `words.json`.
- **Media (not in git), in the session work folder `DELIVERABLES/`:**
  - the MP4;
  - `thumbnails/` (three options, T2 recommended);
  - `audio/`: voice.wav, mix.wav and the two CC0 music files;
  - the style board.
