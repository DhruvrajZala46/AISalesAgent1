# The Classy Elegance - video workflow

Everything needed to make a new video the way this channel makes them, measured from its own 37
uploads, 29 transcripts and 2,685 comments. To start a new video, send the prompts in
[`PROMPTS.md`](PROMPTS.md).

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

1. **Teach, don't report.** Every point: name it -> validate -> why (effect on her) -> principle
   -> what elegant women do -> swap / how-to -> inner payoff. No quotes, no named people, no
   culture reports. Only tips that are concrete, true and useful on any budget, at any age.
2. **Real footage only. Never AI** - in the video and in the thumbnails.
3. **Every creator credited, each clip used once.**
4. **No sound effects.** One soft solo-piano bed ~12 dB under the voice.
5. **Voice: Kokoro `af_heart`, speed 0.80.**
6. **Never build the video before the script is approved.**
7. **Public data only.** Never a logged-in session, never the user's cookies or account.
8. **Never commit** media, keys or cookies. Text (scripts, edits, packages) goes in git under
   `classy-academy-test/videos/<slug>/`; media stays in the scratchpad work folder.
9. Full 1080p, delivered as a Gofile link.

## Folder map

```
workflow/
  PROMPTS.md          the prompts to send, stage by stage, plus an all-in-one
  1-TOPIC.md ... 5-PACKAGE.md   the playbooks
  LEARNINGS.md        every mistake that reached the user, and the check that stops it now
  setup.sh            installs the renderer, voice model, fonts, music into a new work folder
  assets/             fonts, CE logos, GSAP, the AI-sparkle template
  tools/
    dna.py            does the script teach like the channel? (stage 2 gate)
    hookscore.py      hook scores (from the youtube-agent skill)
    tts.py            the voice, one wav per line
    pin_search.py     Pinterest video search -> contact sheets
    dlpicks.py, pin_dl.py   download the picked clips (+ creator credits)
    shots.py, grid.py       scene cuts and frame sheets for checking every clip
    aiscan.py         AI-watermark scan (stage 3 gate)
    build.py          voice timing + edit + music mix -> index.html (refuses AI-flagged clips)
    template.tpl      the page the edit is drawn on (caramel backdrop, cards, fonts)
    edit_example_french.py  a complete beat-by-beat edit to start from
    qa.py, flash.py   checks after rendering
    real_search.py, crop.py, thumb_make.py   thumbnails
    chapters.py       chapters from a transcript
```

Reference measurements: `../edit-style-measured.md` (editing and sound), `../how-you-edit.md`
(the #1 video second by second), `../voice.md` (how the channel talks and teaches),
`../french-PACKAGE.md` (a finished title/description/tags package).

`hookscore.py`, `hooks.json`, `chapters.py` and the `yt-*` skills in `.claude/skills/` come from
the MIT-licensed youtube-agent skill pack by Jake Schincariol (see `tools/LICENSE-youtube-agent`).
