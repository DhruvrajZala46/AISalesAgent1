# QC report: 8 Ways to Make Your Clothes Look New Again (v2)

**Export.** `old-clothes-new_v2.mp4`, 1920x1080, 30 fps, AAC 48 kHz stereo, 10:38 (638.3 s), 370 MB. It was rendered with `tools/ffr.py`. Media is not committed: the file is in the session scratchpad `old-clothes-new/out/`, and the link is given in chat.

## Checks run on the exported file (not on the plan)

| Check | Tool | v1 result | v2 result |
|---|---|---|---|
| Fast renderer matches the browser at every layout | `ffr_cmp.py`, 12 moments | all mean differences 0.2-7.6 (limit 10) | same page |
| Black frames | `qa.py` | 0 | **0** |
| Silence (music must never drop) | `qa.py` | 0 | **0** |
| Bare backdrop while the voice talks | `empty.py` | **3** (1:04, 1:10, 6:54) | **0** |
| Frozen picture | `qa.py` | 16 holds of 1.5-3.7 s | 13 holds of 1.5-2.3 s |
| Integrated loudness | ffmpeg ebur128 | -14.6 LUFS | **-14.6 LUFS**, LRA 2.9 LU |
| Voice above the music | `mix_raw.wav`, speech vs pauses | | **12.2 dB** (speech -22.1 dBFS, music alone -34.3 dBFS) |
| Sound effects | edit.py / build.py | none | **none** |
| AI-generated footage | `aiscan.py`, 140 downloads | 2 flagged, both removed | 0 used above 0.40 |
| Same footage shown twice | build.py assert | 0 | **0** |
| Clip shorter than its slot | build.py SHORT | 1 (0.4 s) | **0** |

**What the 13 "frozen" holds in v2 are.** All of them were checked on the frames, and every one is intended:
- the white number cards and the "In today's video" card (0:32, 0:49, 1:56, 2:59, 4:09, 5:19, 6:38, 8:00, 9:06);
- the Princess of Wales photos held on white (7:44-7:50, as in the reference at 6:58-7:06);
- the end card.

None is a stuck video.

## Watched end to end

I extracted one frame per second (638 frames, `qc/sheet_0-6.jpg`) and looked at every second. Found in v1 and fixed in v2:

1. **2:03-2:05 and 2:10:** a clip (depill19) had burned-in Spanish text ("Exfoliado", "Sin exfoliar"). It is replaced by shaver8 (a fabric shaver on a pilled knit) and shaver25 (a shaver on a pilled sweater). No foreign text remains.
2. **1:04-1:05:** bare caramel between the daylight point and the "Lint, fuzz, creases" row. The sweater frame is now held until "Lint".
3. **1:10-1:11:** bare caramel under "Some need a small repair". Added a needle stitching fabric (buttons10, 20.5-28 s).
4. **6:54-6:57:** bare caramel under "Some alterations make a big difference". Added a sewing machine on a linen hem (taperpants34).
5. **Dark frames at the end of the guide-plug clip** (`flash.py`): trimmed it by 0.6 s.
6. **buttons3** was 0.4 s short: its two segments were re-cut so the clip covers its slot.

The v2 frames at each fixed spot were re-checked (`qc/v2_fixes.jpg`).

## Known limits (stated, not hidden)

- **Rights.** All 105 clips and photos are Pinterest pins with credit only: *unresolved* under `workflow/SOURCES-LOG-TEMPLATE.md`. See SOURCES-LOG.md. This needs the user's decision, or creators' permission, before publishing.
- **Burned-in creator text.** Some tutorials still carry small English captions or handles from the original reel, as reels in the reference do (for example "Sewing on buttons", "Do you hang up your sweaters like this?"). Pins with large promos or other languages were skipped.
- **Logo.** The CE logo is used. The reference's "CA" logo is not in the repo and was not recreated.
- **Loudness.** The master is -14.6 LUFS (YouTube normalises to -14). The reference upload measures -19.3 LUFS integrated, after YouTube's own processing.
