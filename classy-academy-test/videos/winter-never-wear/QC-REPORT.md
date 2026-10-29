# QC report v5: 8 Things Elegant Ladies Never Wear in Winter (29 Oct 2026)

How v5 was checked before delivery (`workflow/EDIT-RULES.md` section 7).

## 1. The sound-off check, all 78 lines

- **The check.** One frame per second of the render, with the words spoken in that second under each frame: 882 frames
  on 19 sheets. For every line I asked whether a viewer with the sound off would know what the sentence is about.
- **Found in the first v5 render and fixed in v5.1:**

| Time | What was wrong | Fix |
|---|---|---|
| 1:01 | a small creator caption ("cozy sweater haul") at the start of the clip | clip starts 1.4 s later |
| 2:01 | a dark frame inside the "you look bulkier" panel | a later, clean part of the same reel (the arm-knit cardigan) |
| 4:15 | a caption ("4 steps to style a white shirt") appeared as the cotton-shirt row faded out | the caption-free seconds of that reel are used |
| 4:54 | an "Amazon must have" title on the pilling clip | the clip starts after the title |
| 5:23 | a brand mark on the "dense knit" close-up | replaced by a dense brown wool knit pulled on, close |
| 5:57 | a short dark cut at the end of the cream belted-coat panel | the clean first 3.3 s are used |
| 6:43 | brand text across the thick-socks clip | removed; the thick wool socks being pulled on now carry the line |
| 10:43 | a red blur frame at the start of the second blowout reel | starts 1 s later |
| 12:03 | the *Charade* cream-coat shot cut to a boy in a car window | replaced by Audrey Hepburn walking in her cream coat |
| 13:44 | a *Charade* terrace shot full of men at tables | replaced by a row of three women in warm, elegant winter coats |

- **Checked and kept:**
  - one small creator label ("Casual") in a cotton-shirt reel; she accepts small creator captions;
  - the price tag on a cut-out sock;
  - the film scenes, where Audrey Hepburn is the subject and passers-by are in the background.

## 2. Side by side with her videos

Two 2-minute stretches were compared, frame every 6 s, left her video and right ours:
- `My7qteRU9k0` ("8 Things Elegant Ladies Never Wear") 1:00-3:00 against v5 1:18-3:18;
- `Loui0mjLavo` ("7 Things Elegant Ladies Avoid in Fall") 1:00-3:00 against v5 10:00-12:00.

| | Her videos | v5 |
|---|---|---|
| Backdrop | caramel blurred gradient behind every explanation | the same gradient, every explanation |
| Rows | 2-4 whole tall reels side by side, filling in left to right | 3 whole tall reels (608 px each), filling in on the spoken words |
| A single reel | in slot 1 or centred, with the backdrop around it | the same |
| Cut-outs | products cut out on caramel (trousers, coats, knits) | knits, coats, base layers, socks, boots, gloves, mittens, labelled |
| Cards | white, black script wiping in | the same |
| Full screen | landscape only (film icons, street style) | landscape only (*Charade*, 1963) |
| Never zoomed | vertical reels are never blown up | `FS()` refuses a vertical clip; none is zoomed |

## 3. Automatic checks

- **AI watermark scan:** every clip used, none flagged (`aiscan.json`).
- **Duplicates:** none. The perceptual duplicate check (`tools/dedupe.py`) found 186 copies among the downloads, and
  only one copy of each is ever used. The build stops if the same footage appears twice.
- **Dark-frame scan (`flash.py`):** the two real dark frames are fixed (table above). The others are single first
  frames that are invisible because the panel fades in.
- **Empty backdrop while talking (`empty.py`):** 0 runs.
- **Renderer against the browser:** 10 moments covering every layout, mean difference 0.0-8.5. The 53.9 s moment
  showed 20, which is film motion between the two capture times, not a layout difference.
- **Length:** 14:41.9 at 1080p30. Voice loudness and music level are unchanged from v4 (piano about 12 dB under
  the voice, -14 LUFS, no sound effects).
