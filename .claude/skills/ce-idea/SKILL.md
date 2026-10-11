---
name: ce-idea
description: >-
  Find the next Classy Elegance video topic from real data, never a guess: collect
  fresh public video lists from 45 niche channels, rank every video by how far it
  beat its OWN channel's median (yt-viral method), cut by lane / last 6 months /
  same season last year / own channel, then hand back 3 ideas with evidence and
  scored titles. Use for "ce-idea", "find my next video idea", "what should I make
  next", "what's trending in my niche".
---

# ce-idea: the next topic, from data

Raw views rank channel size, not ideas. This ranks each video as a **multiple of its own channel's
median** (the `yt-viral` skill: read `.claude/skills/yt-viral/SKILL.md`). It's the method behind
the "Winter 2026 Trends" pick that the user loved.

## Run it
```bash
W=<scratch>/idea; mkdir -p $W
python3 .claude/skills/ce-idea/tools/collect.py $W          # ~2-4 min: 45 channels x 60 videos, long-form only
python3 .claude/skills/ce-idea/tools/rank.py $W --today $(date +%F)
```
`rank.py` calls `yt-viral/swipe.py` for the multiples and title formulas, then prints:
- **A. Right now:** our lane (elegance, classy, style, fashion, seasons), last 6 months, 2× or more.
- **B. Season:** our lane, the same ~3-month window last year (what this time of year rewards).
- **C. Our audience:** the user's own channel(s) ranked by multiple.
- **D. Evergreen:** our lane, 10× or more, any date.

It also writes `outlier_thumbs.jpg`. Look at it, because what the winning thumbnails share is half
the idea.

## Read it like this
1. Ignore beauty-only and mindset-only channels: wrong lane even when the multiple is huge.
2. Find the **one structural thing** the top lane outliers share. In Oct 2026 it was "a numbered
   list that sorts things into elegant vs not: avoid / mistakes / cheapen / IN & OUT".
3. Cross it with timing (B: the video goes out next month, so what does that season reward?) and
   with C (the user's own audience: "Never Wear" 9.4×, "Look Expensive" 5.4×).
4. Don't repeat the channel's last video. Check `videos/` and section C.

## Hand back (exactly this shape)
- Short "how the skill finds ideas" (one paragraph, plain words).
- Table: what's working right now (multiple, title, channel). Then last year's season.
- The one shared structure.
- **3 ideas ranked by evidence.** Each gets a title scored with
  `python3 .claude/skills/yt-package/title.py <titles.txt>` (write 6+, keep the best per idea) and
  the exact outliers that back it.
- Honest limits: dates are month-accurate; older videos have had more time to collect views; the
  formula labels describe titles, not causes.
- Save it as `videos/<slug>/research.md`, commit, and end with **"Ship it, or change it?"**

## Keep the channel list fresh
`channels.json` holds 45 channel IDs (elegance, classy, old money, French chic, style over 40/50,
etc.). When a new competitor shows up in the outliers or the user names one, add its channel ID.
Public listings only. Never log in.
