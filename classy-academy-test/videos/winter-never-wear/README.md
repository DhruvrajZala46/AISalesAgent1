# 8 Things Elegant Ladies Never Wear in Winter (Episode 32): deliverables

The script was used word for word (`beats.txt`, 78 lines, 2,063 words). The video is 14:42, 1080p.

| # | Deliverable (from the brief) | File |
|---|---|---|
| 1 | Complete channel visual DNA analysis | `CHANNEL-DNA-REPORT.md` |
| 2 | Editing, animation, music and sound-effect breakdown | `CHANNEL-DNA-REPORT.md` sections 2, 4, 5 |
| 3 | Detailed, line-by-line visual storyboard | `STORYBOARD.md` (generated from the rendered edit, so it matches the video exactly) |
| 4 | Visual references and verified asset sources | `SOURCES-LOG.md` (149 clips), `ok.txt` (what every checked clip shows and which seconds are usable), `picks.md` (every Pinterest search and pick), `CREDITS.txt` |
| 5 | Music and sound-design plan | `MUSIC-SOUND-PLAN.md` |
| 6 | Proposed redesigned channel logo | `LOGO-PROPOSAL.md`; the board `logo_options.jpg` is in chat. **Waiting for your choice**: nothing is changed until you approve. |
| 7 | The final edited video | not committed (media); sent in chat (v3). Checks in `QC-REPORT.md` |

## How it was made (the order the brief asked for)

1. **Analyse.**
   - All 31 long uploads were measured: cuts, white and caramel screen time, loudness.
   - The voice and music of the closest-format video ("7 Things Elegant Ladies Avoid in Fall") were separated with
     Demucs and measured on their own.
   - A contact sheet (one frame every 3 s) was made for every video.
2. **Research.**
   - 60 Pinterest video searches; 248 clips kept after removing duplicates.
   - Every clip was checked frame by frame on strips (`ok.txt`) and scanned for AI.
   - 1980s-90s film scenes were searched; two are used where the line matches:
     - *You've Got Mail*, 1998: in the hook, Meg Ryan walking a city street in a long coat, and at her shop counter;
     - *Little Women*, 1994: "I always love hearing from you" over the family reading a letter from home.
3. **Plan.** The storyboard was written in the channel's own "Never Wear" format, and so was the music plan.
4. **Edit.**
   - `edit.py` is run by `workflow/tools/build.py`.
   - The fast renderer was checked against the browser at 15 layouts.
   - v1 was rendered and watched at one frame per second; six issues were fixed in v2 and one more in v3 (`QC-REPORT.md`).

## Needs you

1. **Rights.**
   - 147 Pinterest clips are *unresolved* (found and credited, no licence).
   - 2 film scenes are *unlicensed, owner's decision*.
   - See `SOURCES-LOG.md`.
2. **Logo.** Choose A, B or C (or ask for changes) in `LOGO-PROPOSAL.md`.
3. **The video.** Ship it, or change it?
