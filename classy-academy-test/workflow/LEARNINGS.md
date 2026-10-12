# Learnings - mistakes made once, never again

Each line is a mistake that reached the user, and the check that now stops it.

| Video | What went wrong | What stops it now |
|---|---|---|
| French, Oct 2026 | The script reported what others say (quotes, named people, "Paris" 16.5 per 1,000 words) instead of teaching in the channel's own voice; too little "why" and inner payoff. | `voice.md` "How I teach" + `tools/dna.py` gate in stage 2. |
| French, Oct 2026 | An AI clip (Gemini ✦ sparkle, "scarf9") got into the final video. | `tools/aiscan.py` on every clip + `build.py` refuses flagged clips. |
| French, Oct 2026 | 6 clips had built-in dark flashes that looked like glitches. | `tools/flash.py` after every render. |
| French, Oct 2026 | 7 moments showed the empty caramel backdrop while the voice was talking. | Per-second contact sheet watched end to end; fix every gap. |
| French, Oct 2026 | Thumbnails v1/v2 did not look like the channel ("worst"). | Measured thumbnail DNA + `tools/thumb_make.py`; real named women only. |
| French, Oct 2026 | The thumbnail underline crossed the "y" of "Style". | Underline sits below the lowest descender (`thumb_make.py`). |
| Winter, Oct 2026 | Too many sound effects and the wrong music. | No sound effects (none in the channel); soft solo piano ~12 dB under, steady. |
| All | Rendering takes ~11 minutes per minute of video on this machine. | Start the render in the background; a faster FFmpeg renderer is being tested (`fr2/ff/` prototype). |
