# Change summary: video edit for "8 Ways to Make Your Clothes Look New Again"

## What was made
- **The finished video.** 10:38, 1080p, v2, rendered and checked. Rendered from the approved script v2 (`beats.txt`) with no wording changes.
- **Card headings.** The eight `[ON-SCREEN CARD]` headings appear only as white script cards in silent gaps (`gaps.json`). They are never spoken.

## Files in this folder
- `EDITING-DNA.md`: the reference video measured second by second, and the rules copied from it.
- `edit.py`: the beat-by-beat edit, run by `workflow/tools/build.py`.
- `gaps.json`: the card gaps.
- `picks.md`: the Pinterest picks per line.
- `TIMELINE.md`: 133 shots, generated from the rendered page.
- `SOURCES-LOG.md`: the asset ledger for all 105 clips and photos.
- `CREDITS.txt`: for the description.
- `QC-REPORT.md`: the checks and what was fixed.

## Pipeline: kept as it is
- **Voice and music.** Kokoro af_heart at 0.80. Mixkit "Classical" piano about 12 dB under the voice. Master at -14 LUFS.
- **No sound effects.**
- **Look.** CE logo, white end card, haze card for the stylist guide.
- **Process.** Checklist recap. Each clip used once. AI scan. Fast renderer checked against the browser.

## New in this edit (to match the reference)
- **Footage source.** Creators' Pinterest video pins only (48 searches, 140 downloaded, 105 used), as in the user's own videos. Licensed stock (Mixkit, Coverr, Commons) was researched first, then dropped on the user's instruction.
- **Layouts copied from the reference:**
  - photos appearing one by one on white, with the logo hidden on white;
  - an "In today's video" card;
  - an "Episode 14:" title over a full-screen scene;
  - per point: one tall tutorial centred on caramel and held while the voice teaches, with the creator's @handle in small script at its lower right and a short tip in script between asterisks on the left;
  - rows of 3-4 tall panels for lists;
  - the Princess of Wales shown as photos on white;
  - a calm window scene as the outro.
- **New helpers in `edit.py`.** `wbg` and `wrow` (white rows), `row4`, `one`, `credit`, `tip`, `scene`, `cardg`, plus a plain white background clip (`assets/white.mp4`, generated, no footage).
- **Episode number 14.** The last committed edit was Episode 13 (never-say).

## Needs the user
1. **Rights.** Each row in SOURCES-LOG.md is unresolved, with the risk stated. Before publishing, decide whether to accept the risk, or ask the main creators for permission (template: `workflow/ASSET-RESEARCH-GUIDE.md` section 5).
2. **Logo.** The reference shows a "CA" logo, and this repo has only "CE". To switch, swap `assets/logo_ce.png` and `logo_ce_dark.png`.
3. **Review.** Watch v2: ship it, or change it?
