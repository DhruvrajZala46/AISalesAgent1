---
name: ce-script
description: >-
  Write the Classy Elegance script for a chosen idea in the channel's own voice:
  5 hooks scored with hookscore.py, the channel's fixed structure (hook, "In
  today's video", numbered points with validate -> principle -> swap, stylist
  guide mid-roll, recap, part-two close), then split into beats.txt for voice
  and edit. Use for "ce-script", "write the script", after ce-idea.
---

# ce-script: the script in her voice

1. Read `channel/voice.md` (copied to `~/.claude/youtube/voice.md` by setup) and
   `.claude/skills/yt-script/SKILL.md`. Follow yt-script for hooks: write 5 off its 21 formulas,
   score them with `python3 .claude/skills/yt-script/hookscore.py --hook "..."`, and offer the top
   2.
2. Model it on `example-winter-script.md`, which the user approved. Use the same structure, tone,
   length (about 1,150 words → about 9 min at 126 wpm) and on-screen notes.
3. **Structure:** hook (number + "number X is in almost every closet" style curiosity) → "In
   today's video, we're revealing…" → each point: "Number one. [item]." → validate ("We get it.")
   → why it fails → principle line ("It's not about X. It's about Y.") → the swap with **named
   pieces and colours** → mid-video stylist guide → recap checklist → "If you'd like a part two…"
   → thanks.
4. **Write for the visuals.** Every sentence names something that can be shown with real footage:
   a garment, a colour, a before/after, a habit. A sentence that can't be shown gets rewritten.
5. **Never invent** a number, study or result.
6. **Make `beats.txt`:** one line per beat, at most one visual idea per line. List items get their
   own lines ("A fine knit," / "a smooth wool trouser," / "and a soft leather glove."). The winter
   video had 120 beats. Number cards are their own beat ("Number two. Pilled, tired knitwear.").
7. Save `videos/<slug>/script.md` and `videos/<slug>/beats.txt`, commit, and ask for approval.
