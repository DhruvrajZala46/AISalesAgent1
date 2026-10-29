# QC report: 8 Things Elegant Ladies Never Wear in Winter (v4, after the owner's review)

**Export.** `winter-never-wear_v4.mp4`: 1920x1080, 30 fps, AAC 48 kHz stereo, 14:42 (881.9 s), rendered with
`tools/ffr.py`. The copy sent in chat is a re-encode of it, made to fit the 400 MiB upload limit. Media is not
committed. What changed from v3: `V4-CHANGES.md`.

## Checks run on the exported file

| Check | Tool | Result |
|---|---|---|
| Fast renderer matches the browser | `ffr_cmp.py`, 10 moments covering every layout | 8 of 10 under the limit of 10. Two at 12.0 (52.5 s, the title over the snow scene) and 12.2 (13:38, two women in white berets); both were checked on the comparison sheet: the same frame, the difference is the browser's smoother scaling of falling snow and fine fur |
| Black frames | `qa.py` | **0** |
| Silence (the music never drops) | `qa.py` | only the last second of the end card |
| Bare backdrop while the voice talks | `empty.py` | **0** |
| Integrated loudness | ffmpeg ebur128 | **-14.6 LUFS** |
| Voice above the music | `assets/mix_raw.wav`, speech vs pauses | **12.8 dB** (speech -21.9 dBFS, music alone -34.8 dBFS) |
| Sound effects | edit.py / build.py | **none** |
| AI-generated footage | `aiscan.py` on 365 downloads, including all 200 clips used | 5 flagged (label9, cottonshirt12, scarfwrap26, scarfwrap34, washknit0 borderline), **none used** |
| The same footage shown twice | build.py assert | **0** |
| Clip shorter than its slot | build.py SHORT | **0** |
| Blurred backdrop behind full-screen scenes | edit.py | **none**: every full-screen scene is full-bleed |
| Frozen picture | `qa.py` | 11 holds of 1.4-4.7 s, all intended: the white number cards, "in today's video", and the new-name monogram card |
| Dark frames inside clips | `flash.py` | 5 clips with a few dark frames at the very end of their segment (coatwalk4, f80winter6, waveby2, careabel27, insideout39). Each falls in the last 0.1-0.5 s, where the next scene is already dissolving over it; none is visible at 1 fps |

## Watched end to end, line by line

- **Method:** one frame per second (882 frames), each labelled with the words being spoken at that moment
  (`qc4/s_00-12.jpg` in the session files).
- **Checked on every frame:**
  - that the picture shows what the words say;
  - that the transition is clean;
  - that no caption, logo, man or off-topic clip appears.
- **Result:** every line matched, and nothing had to be replaced after the render. A stretch-by-stretch preview of
  the same edit had already been checked before rendering (`prev/sheet_00-07.jpg`), and the issues found there were
  fixed first:
  - soft over-enlarged shots moved to the caramel layout;
  - three framings changed so the face stays in frame;
  - the guide plug at the end moved to a darker scene so its text reads;
  - a too-early dissolve into the guide plug was fixed.

## Known limits (stated, not hidden)

- **Rights:**
  - 199 Pinterest clips are *unresolved* (found and credited, with no licence).
  - 1 film scene (*Little Women*, 1994) is *unlicensed, owner's decision*.
  - See SOURCES-LOG.md.
- **Small creator captions** remain on a few reels, as in the channel's own videos. Examples: "Check Care Label" at
  12:48; a small Swedish line at 1:47.
- **Logo:** the current CE logo is used until a redesign is approved (LOGO-PROPOSAL.md).
