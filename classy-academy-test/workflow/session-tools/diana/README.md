# Working scripts of the Princess Diana build (17 Nov 2026)

Copied from the session's work folder so a new chat does not have to rewrite them. Paths inside them point to the old
scratchpad (`.../scratchpad/cdi`): change them to the new work folder. The general tools are in `workflow/tools/`.

Order used:
1. `queries.py` -> `q.txt` and `briefs.py` (what each search tag must show); `q2.txt`-`q5.txt` are the later rounds
   (`briefs2.py`). `runpins2.py` runs `tools/pin_search.py`. `phsearch.py` searches photo pins.
2. `mkbrief1.py` -> first-screening prompts (contact sheets); results in `sel/`. `sel2picks.py` -> `picks.md`.
3. `pipeline.sh <batch>` (download, `shrink.py`, `post.sh`: shots, frame strips, durations, duplicates, `oldclash.py`,
   AI scan).
4. `mkbrief2.py <batch>` -> second-screening prompts (frame strips); results in `scr/`. `pickhelp.py` lists the clips
   that fit.
5. `vs.py` / `big.py`: large frames of a chosen window, for the eye check.
6. `_helpers.py` + `_body_head.py` + `_body_main.py` -> `edit.py`; `dry2.py` checks phrases, slot lengths and photos
   before a build.
7. `tools/build.py`, then `bgswap.py`, `tools/flash.py`, snapshots (`snapsheet.py`), `render_loop.sh`, `after.sh`.

`NOTES.md` is the running log of the build: what was chosen, rejected and why.
