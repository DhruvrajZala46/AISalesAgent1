# Stage 2 - Write the script (the most important stage)

The video is only as good as what she learns. A viewer of this channel clicks to come away with
something she can **use tomorrow**: a piece to swap, a colour to try, a habit to start, told
calmly by a teacher she trusts. Not news, not quotes, not a list of items.

Read first, every time: `classy-academy-test/voice.md` (the "How I teach" section above all) and
the `yt-script` skill.

## Where the tips come from

1. **The approved idea** and its teaching angle (stage 1).
2. **What the winning videos on this topic actually teach.** Pull the transcripts of the 5-10
   biggest outliers on the topic (public captions only) and list every tip they give. Keep a tip
   only if it is **concrete** (a named piece, colour, fabric, habit or step), **true** (no invented
   facts, no statistics) and **useful to a woman on any budget, at any age**.
3. **Our own past videos.** Don't repeat a tip we gave in the last few months unless the new angle
   makes it fresh. Do reuse the channel's own principles and phrasing.
4. **Comments.** What our viewers ask for (part two, budget, over 50, "what to wear instead").

### The proof map - before a word of the script

No tip is invented. Every candidate tip gets a row, and the user sees the map before the script:

| Tip | Niche proof (winners that teach it: multiple, timestamp) | Our viewers (quoted / thanked / asked for, likes) | Pushback | Keep? |
|---|---|---|---|---|

```bash
python3 $T/audience_proof.py <scratchpad>/data                      # our videos ranked by love: like rate, thanks, shares, requests
python3 $T/audience_proof.py <scratchpad>/data --video "<our title>"  # the tips viewers quoted, tried, thanked, pushed back on
python3 $T/audience_proof.py <scratchpad>/data --ask "<topic words>"  # what viewers ask us to make, with likes
```

Keep a tip only with **two proofs**: taught by 2+ niche winners; or 1 winner + our viewers' love or
requests; or quoted/thanked by our viewers with 10+ likes. A tip with pushback is rewritten to
answer it (e.g. "Say that again" felt demanding -> "Pardon?"). Views say what gets clicked; like
rate, thank-you comments, shares and "best tip ever" comments say what was worth watching. Aim for both.
If the winners' transcripts can't be read (YouTube blocks the machine), say so and wait - never fill
the gap with guesses.

Then **rewrite every tip in our own voice**. The research is where the tips come from; it never
appears in the script. No "she says", no book titles, no names, no "one French woman shared".
A culture or a person can be the lens of the title, but the script teaches the principle itself.

## The value test - every point must pass all five

1. **Concrete:** she can picture the exact piece/colour/step (not "dress better").
2. **Actionable today:** she can do it with what she owns, or with one affordable piece.
3. **Explained:** WHY it changes how she looks and how she feels.
4. **Kind:** validates her first, never shames, never calls a colour or culture "not elegant".
5. **Worth a screenshot:** if she wouldn't save it, replace it.

## The shape (8-10 minutes, 1,100-1,600 spoken words)

- **Hook (0:00-0:15):** a relatable scene or a misconception, in the channel's openers ("Have you
  ever seen a woman walk by and thought..." / "You might think... But what if I told you...").
  Write FIVE hooks, run `python3 .claude/skills/yt-script/hookscore.py hooks.txt`, show the top two.
- **The turn:** "In today's video, we're uncovering [N things] ... and the subtle swaps that can
  instantly elevate your style. Some of these may surprise you, but once you see them, you'll
  never unsee them. Let's get started." No channel intro, no subscribe pitch.
- **Each point, the 7 teaching steps:** name it -> validate ("We get it.") -> WHY (effect on her)
  -> the principle line -> what elegant women do -> the swap / how-to with named pieces and
  colours -> the inner payoff. (Examples from our #1 video are in `voice.md`.)
- **Mid-video (after point 3 or 4):** the personal stylist guide, "linked in the description".
- **Recap:** one line per point, in the order given.
- **Close:** "If you'd like a part two, let us know in the comments." -> "A simple like or
  comment would mean so much to us." -> "Until next time, bye everyone."

## File format

`classy-academy-test/videos/<slug>/script.md`:

```
## Hook
[ON SCREEN: full-screen clip, woman walking, cream coat]
**Have you ever seen a woman walk by and thought...**
```

Every spoken line is **bold on its own line**; every beat has an `[ON SCREEN: ...]` line (what the
viewer sees, word by word). After the spoken script, sections `## Proof` (where each tip came
from: video, multiple, timestamp) and `## Final check` (the gates below) - the tools ignore those.

Also write `beats.txt` (one spoken line per line, exactly the bold lines, in order) - this drives
the voice and the edit.

## Gates - all must pass before the user sees it

```bash
T=classy-academy-test/workflow/tools
python3 $T/dna.py classy-academy-test/videos/<slug>/script.md          # -> TEACHES LIKE THE CHANNEL
python3 .claude/skills/content-idea/tools/fit.py check classy-academy-test/videos/<slug>/script.md   # -> FITS THE CHANNEL
python3 .claude/skills/yt-script/hookscore.py --hook "<the hook>"      # STRONG
```

`dna.py` compares the script with the channel's own wardrobe videos (our #1 video passes it with
zero fixes). If it lists fixes, rewrite those points and run it again. Never hand over a script
that has not passed both `dna.py` and `fit.py`.

## Hand back

- the two best hooks with their scores
- the script, beat by beat, with `[ON SCREEN]` on every beat
- runtime estimate (the voice runs at ~132 words per minute)
- the `dna.py` and `fit.py` results, pasted
- one line per point: the tip and why it is valuable to her
- commit `script.md` and `beats.txt`

Last line: **ship it, or change it?** The video is never built before the user approves the script.
