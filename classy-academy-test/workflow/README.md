# The Classy Elegance - video workflow

Everything needed to make a new video the way this channel makes them, measured from its own 37
uploads, 29 transcripts and 2,685 comments. To start a new video, send the prompts in
[`PROMPTS.md`](PROMPTS.md).

**The bar: [`GOLD-STANDARD.md`](GOLD-STANDARD.md)** - how the user's favourite video, "8 Dressing Rules
Every Woman Should Know", was made (idea, script, video, thumbnail, package). Every new video is
made that way and may only get better.

## The five stages

| Stage | Playbook | Skills | Ends with |
|---|---|---|---|
| 1. Topic | [1-TOPIC.md](1-TOPIC.md) | `content-idea` (+ `yt-viral`) | 3 ideas with evidence, user picks one |
| 2. Script | [2-SCRIPT.md](2-SCRIPT.md) | `yt-script` | script that passes `dna.py` + `fit.py`, user approves |
| 3. Video | [3-VIDEO.md](3-VIDEO.md) | - | full 1080p Gofile link + credits |
| 4. Thumbnails | [4-THUMBNAIL.md](4-THUMBNAIL.md) | `yt-package` | 3 thumbnails in the channel's layout |
| 5. Package | [5-PACKAGE.md](5-PACKAGE.md) | `yt-package`, `yt-seo`, `yt-chapters` | title, description, tags, chapters |

Each stage ends with the question **ship it, or change it?** Nothing moves on without the user.

## Rules that never change

0. **`EDIT-RULES.md` before every edit.** Copy the owner's videos 99%: the caramel backdrop with rows of
   full-length women wearing the exact named item, full-screen only for landscape footage (never a zoomed
   vertical reel), product cut-outs for lists, the mistake then the swap. Her videos decide, not my ideas.
1. **Teach, don't report - in the creator's habit structure** (`../CHANNEL-DNA.md`, sections 2-3 and the
   value test in 7). A named woman may be a brief example she can see or hear; never a story about her.
   No culture reports. Only tips that are concrete, true and useful on any budget, at any age.
2. **Real footage only. Never AI** - in the video and in the thumbnails.
3. **Every clip researched and logged before use** (`ASSET-RESEARCH-GUIDE.md`, `SOURCES-LOG-TEMPLATE.md`):
   licence or permission, evidence, decision. Credit is not permission. Each clip used once.
4. **No sound effects.** One soft solo-piano bed ~12 dB under the voice (measured on two of her videos;
   the speech videos' sound is not measured - `../VISUAL-EDITING-DNA.md` section 6).
5. **Voice: Kokoro `af_heart`, speed 0.80.**
6. **Never build the video before the script is approved.**
7. **Public data only.** If YouTube blocks the machine, the user may hand over a cookies file: use
   it only with `yt-dlp --cookies` for public captions, comments and listings, slowly; never print,
   read or commit it.
8. **Never commit** media, keys or cookies. Text (scripts, edits, packages) goes in git under
   `classy-academy-test/videos/<slug>/`; media stays in the scratchpad work folder.
9. Full 1080p, delivered as a Gofile link.

## Folder map

```
workflow/
  PROMPTS.md          the prompts to send, stage by stage, plus an all-in-one
  1-TOPIC.md ... 5-PACKAGE.md   the playbooks
  LEARNINGS.md        every mistake that reached the user, and the check that stops it now
  ASSET-RESEARCH-GUIDE.md   visual brief per line, where to look, provenance, rights, final audit
  SOURCES-LOG-TEMPLATE.md   one row per clip: source, licence, evidence, decision
  setup.sh            installs the renderer, voice model, fonts, music into a new work folder
  assets/             fonts, CE logos, GSAP, the AI-sparkle template
  tools/
    dna.py            does the script teach like the channel? (stage 2 gate)
    hookscore.py      hook scores (from the youtube-agent skill)
    tts.py            the voice, one wav per line
    revsearch.py      reverse image search (Yandex) -> pages holding the same frame + review sheet
    pin_search.py     Pinterest video search -> contact sheets
    dlpicks.py, pin_dl.py   download the picked clips (+ creator credits)
    shots.py, grid.py       scene cuts and frame sheets for checking every clip
    aiscan.py         AI-watermark scan (stage 3 gate)
    build.py          voice timing + edit + music mix -> index.html (refuses AI-flagged clips)
    template.tpl      the page the edit is drawn on (caramel backdrop, cards, fonts)
    edit_example_french.py  a complete beat-by-beat edit to start from
    words.py          word timing of the voice, so each picture lands on its word
    strips.py         frames inside every clip (a frame every ~2 s, key:a:b to zoom)
    ffr.py, ffr_capture.js, ffr_cmp.py   the fast renderer and its check against the browser
    qa.py, flash.py, empty.py   checks after rendering
    audience_proof.py what our own viewers like, thank, share and ask for
    real_search.py, crop.py, thumb_make.py   thumbnails in the channel's layout
    thumb_xo.py       the winners' "same woman, red cross / green tick" thumbnail in our look
    chapters.py       chapters from a transcript
```

Reference measurements: `../edit-style-measured.md` (editing and sound), `../how-you-edit.md`
(the #1 video second by second), `../voice.md` (how the channel talks and teaches),
`../french-PACKAGE.md` (a finished title/description/tags package).

`hookscore.py`, `hooks.json`, `chapters.py` and the `yt-*` skills in `.claude/skills/` come from
the MIT-licensed youtube-agent skill pack by Jake Schincariol (see `tools/LICENSE-youtube-agent`).
