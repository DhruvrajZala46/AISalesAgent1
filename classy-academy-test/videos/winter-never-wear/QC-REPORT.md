# QC report: 8 Things Elegant Ladies Never Wear in Winter (v2)

**Export.** `winter-never-wear_v2.mp4`: 1920x1080, 30 fps, AAC 48 kHz stereo, 14:42 (881.9 s), 696 MB, rendered with
`tools/ffr.py`. Media is not committed; the file is in the session scratchpad (`winter/work/out/`).

## Checks run on the exported file

| Check | Tool | v1 | v2 |
|---|---|---|---|
| Fast renderer matches the browser | `ffr_cmp.py`, 15 moments covering every layout | mean differences 0.0-8.8 (limit 10) | same page |
| Black frames | `qa.py` | 0 | **0** |
| Silence (music never drops) | `qa.py` | only the last second of the end card | **same** |
| Integrated loudness | ffmpeg ebur128 | -14.6 LUFS | **-14.6 LUFS** |
| Voice above the music | `assets/mix_raw.wav`, speech vs pauses | | **12.8 dB** (speech -21.9 dBFS, music alone -34.8 dBFS) |
| Sound effects | edit.py / build.py | none | **none** |
| AI-generated footage | `aiscan.py` on all 248 clips | 3 flagged (label9, scarfwrap26, scarfwrap34), none used | **0 used at 0.40 or above** |
| The same footage shown twice | build.py assert | 0 | **0** |
| Clip shorter than its slot | build.py SHORT | 0 | **0** |
| Bare backdrop while the voice talks | `empty.py` | 4 runs | **3 runs, all intended** (see below) |

**The 3 "bare backdrop" runs in v2** are the principle-line screens: white serif text on caramel, which `empty.py`
counts as empty.
- 4:44 "*toasty* one minute / and strangely clammy the next"
- 8:18 "fewer than *one in 10* / met their minimum standard for grip"
- 10:53 "That's actually a *myth*."

**Frozen-picture holds** (`qa.py`):
- the eight white number cards and the three text screens above, all intended;
- 11:50 (1.4 s): a still beanie photo inside the reel.

## Watched end to end

One frame per second of v1 (882 frames, `qc/s_01-10.jpg`). Found and fixed in v2:

1. **5:44:** a "giive" brand caption on the cardigan clip (label18). Now trimmed before it appears, with a knitting
   close-up (chunky34) after it.
2. **4:44:** about 2 s of bare caramel before the "toasty" line. The line now arrives as the panels leave.
3. **8:46:** a motion-blur flash and a grey frame in treadboots10. Replaced with cobbler2_13 (polishing brown leather
   loafers), on "brown leather that look just as polished".
4. **11:43:** captions ("This is how I wear it", "How most people wear it") on the beret clip. Trimmed to 3.0-5.8 s.
5. **10:54:** the *Little Women* scene did not match "researchers... an old military experiment". It is replaced by
   loose hair in the snow (snowwalk23). *Little Women* now sits under "I always love hearing from you" (14:01), where
   the March family reads a letter from home.
6. **Dark frames at clip starts** (`flash.py`): beanie5, coatwalk4, cobbler2_22, socks18, wintercafe2 and wintercafe37
   were trimmed. label35 (a dark dip) was removed.

## Known limits (stated, not hidden)

- **8:54 (0.4 s):** the cobbler reel (cobbler2_22) dips to black between two of its own shots. The fix (trim to
  0.4-6.25 s) is prepared but not yet rendered.
- **Rights:** 147 Pinterest clips are *unresolved* and 2 film scenes are *unlicensed, owner's decision*. See
  SOURCES-LOG.md.
- **Burned-in creator text:** some reels still carry a small creator caption, as reels in the channel's own videos do,
  for example "Check Care Label" at 12:48.
- **Logo:** the current CE logo is used until a redesign direction is approved (LOGO-PROPOSAL.md).
