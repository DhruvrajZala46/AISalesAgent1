# Learnings - mistakes made once, never again

Each line is a mistake that reached the user, and the check that now stops it.

| Video | What went wrong | What stops it now |
|---|---|---|
| French, Oct 2026 | The script reported what others say (quotes, named people, "Paris" 16.5 per 1,000 words) instead of teaching in the channel's own voice; too little "why" and inner payoff. | `voice.md` "How I teach" + `tools/dna.py` gate in stage 2. |
| French, Oct 2026 | An AI clip (Gemini ✦ sparkle, "scarf9") got into the final video. | `tools/aiscan.py` on every clip + `build.py` refuses flagged clips. |
| Put together, Oct 2026 | AI scan v1 (one median frame) passed 3 AI clips that scored 0.49-0.58; another came from an uploader named "maheez_gemni". | `aiscan.py` v2 (16 frames, the sparkle must repeat at a known spot; cutoff 0.40 because scarf9 scored 0.56); read every uploader name by eye. |
| French, Oct 2026 | 6 clips had built-in dark flashes that looked like glitches. | `tools/flash.py` after every render. |
| French, Oct 2026 | 7 moments showed the empty caramel backdrop while the voice was talking. | Per-second contact sheet watched end to end + `tools/empty.py` (found 2 more in the put-together video); fix every gap. |
| French, Oct 2026 | Thumbnails v1/v2 did not look like the channel ("worst"). | Measured thumbnail DNA + `tools/thumb_make.py`; real named women only. |
| French, Oct 2026 | The thumbnail underline crossed the "y" of "Style". | Underline sits below the lowest descender (`thumb_make.py`). |
| Winter, Oct 2026 | Too many sound effects and the wrong music. | No sound effects (none in the channel); soft solo piano ~12 dB under, steady. |
| All | Rendering took ~11 minutes per minute of video on this machine. | `tools/ffr.py` fast renderer (~4.3 min per minute), checked against browser frames with `ffr_cmp.py` before every full run. |
| Put together, Oct 2026 | The fast renderer placed the blurred backdrop of full-screen clips 120 px off, so caramel showed at the edges. | Fixed in `ffr.py`; `ffr_cmp.py` must include full-screen moments. |
| Put together, Oct 2026 | The user: the pictures did not flow with the clips before and after; the same format every video. | The "stage" edit (3-VIDEO.md step 5): one calm frame per point, pictures change inside it on the exact word (`words.py` + `at()`), the same woman from mistake to fix, from the 79-video replay study. |
| Dressing rules, Oct 2026 | `dlpicks.py` silently skipped every pick whose tag has a digit inside (`over60chic0`): 11 over-60 clips missing. | Tokens now match any tag + number; check `raw/` against `picks.md` after every download. |
| Dressing rules, Oct 2026 | The fast renderer's capture left each mark's svg visible, so it was baked into later sprites (a tick on the white card 5). | `ffr_capture.js` resets every svg before each capture; `ffr_cmp.py` must include a card and the recap. |
| Dressing rules, Oct 2026 | A clip with no watermark was AI (redcoat0): pin title ending in a leftover "Pinterest Description:", an amzn.to affiliate link, exactly 15.15 s at 24 fps, the handbag changing size between frames. | Check every clip's pin title, source link and length (AI tools give 5/6/8/10/15 s at 24 fps) and look at three full-size frames for objects that change; the watermark scan alone is not enough. |
