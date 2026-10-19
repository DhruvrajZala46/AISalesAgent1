# Brief: watch Classy Academy videos second by second and write down exactly how each one is made

Folder: `/tmp/claude-0/-home-user-AISalesAgent1/73fc3aa5-807d-530d-b865-5c7bcc671679/scratchpad/hairvid/own`

The channel owner wants their next video made EXACTLY like their own 30 videos ("0% difference"). Your job is to watch
the videos assigned to you completely, second by second, and record every editing decision. **No overview, no guessing.**
Describe only what you see in the frames and read in the data.

## What you have, per video id
- `study/<id>/half_MM_a.jpg` and `half_MM_b.jpg`: one sheet per HALF minute (a = seconds 0-29 of minute MM,
  b = seconds 30-59), 30 frames (one per second). Under each frame: the time, the measured layout (CARAMEL+centre,
  ROW/PANELS(n), FULL, WHITE/CARD, CARAMEL(text/empty), CREAM/WHITE+picture, BLACK), CUT/DISS in red if the
  picture changed in that second, and the words spoken in that second.
  **Read EVERY half sheet of the video, in order, from the first to the last. Do not skip any.** The measured
  layout is a machine guess: trust your eyes over it (for example, a 3-panel row sometimes reads as PANELS(2)).
  Ignore the older `sheet_MM.jpg` files (too small to read).
- `study/<id>/seconds.json`: the same per second (layout, words, change, loudness in dB).
- `study/<id>/cuts.json`: every picture change, as a cut or a dissolve with its length.
- `study/<id>/audio.json`: voice level, music level in pauses, possible sound effects.
- `vid/<id>.info.json`: title, views, likes, comments, upload date. Read only these fields with python. The file is large.
- `vid/<id>.en.json3`: the captions with timing.
- You may extract extra frames at full size to read text or check a detail:
  `ffmpeg -v error -ss <sec> -i vid/<id>.mp4 -frames:v 1 /tmp/claude-0/-home-user-AISalesAgent1/73fc3aa5-807d-530d-b865-5c7bcc671679/scratchpad/hairvid/own/study/<id>/f_<sec>.png`.
  Then Read the image. Do this whenever on-screen text, a credit, a label or a transition is too small to read on the sheet.

## Write, per video, `study/<id>/notes.json` (JSON; do NOT write .md files). Keys:
- `"stats"`: {title, upload_date, duration, views, likes, comments}
- `"structure"`: ordered list of sections. Each section is {from, to, part, what_is_said, how_it_is_shown}:
  - `part` is one of: hook, title, intro, guide mention, point N card, point N body, comment ask, conclusion, outro, end card.
  - `what_is_said` is a short summary of the words.
  - `how_it_is_shown` lists the layouts used in order, with times.
- `"timeline"`: one entry for EVERY picture change. For each: from, to, layout, exactly what is on screen, the words being said
  at that moment, how the picture relates to those words, any text on screen (exact wording, font look: script/serif,
  colour, position), and how it entered and left (cut, dissolve, grow from centre/corner, wipe, fade to white or black).
  - **The source** of the picture, judged by eye: creator reel (vertical phone video), film scene, celebrity event/press
    photo, interview, product photo, stock-like, or possibly AI.
  - **Who is shown:** age range, skin tone, man or woman.
- `"text_treatments"`: every kind of on-screen text with an example, its timing and its position.
- `"tricks"`: every repeated technique you notice. Be specific, with times as evidence. For example:
  - how long one tutorial clip is held;
  - how rows build;
  - when a named woman appears;
  - how a point opens and closes;
  - how the hook is cut;
  - what appears under the guide mention;
  - how the ending runs.
- `"sound"`: the music feel and level, any sound effects (and when), and pauses. Base this on audio.json and the loudness per second.
- `"retention_notes"`: what keeps attention changing (picture change rate per section).

Be exhaustive: a 9-minute video should have well over 100 timeline entries. Accuracy beats speed. When you are not sure,
write "unclear" instead of guessing.

## Questions your notes must answer (put the answers in `tricks`, with times as evidence)
1. Hook (first 20-40 s): what is shown on each line, how fast it changes, is there text, where does the title appear.
2. How a point opens (card wording and font, what comes right before and after the card) and how it closes.
3. How long one clip stays on screen in each layout; when ONE creator's clip is held long (tutorials, demos) and for how long.
4. Rows: how many panels, are they the same creator/look or different women, do they build one by one, on which words.
5. Small text anywhere on the picture (for example a tip note like "* We recommend using a french pin *",
   creator credits like "@handle on TikTok", labels, names of celebrities, product names): exact wording, position, font, when.
6. Named women (celebrities, royals): how they are shown (photo or video, full screen, panel, frame) and for how long.
7. Do/don't or before/after moments: how they are shown (side by side? text? marks?). Report exactly; never assume.
8. Guide/description mention and any comment/subscribe ask: words, picture, text on screen.
9. Ending: the last 30 s, every picture, any end screen, logo cards, how the music ends.
10. Anything you see that a careful editor would copy that is not covered above.

Your final message: only the list of notes.json files you wrote and one line per video with its most important finding.
