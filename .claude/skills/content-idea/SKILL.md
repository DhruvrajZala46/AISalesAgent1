---
name: content-idea
description: >-
  Find the next video idea for The Classy Elegance from real YouTube data, never
  from a guess. Collects fresh public video lists from the niche's channels, ranks
  every video by how far it beat its OWN channel's median views, cuts the results
  by our lane, the last 6 months, the same season last year and our own audience,
  checks every idea for audience fit against the channel's own transcripts and
  comments, then hands back 3 ideas with their evidence and linted titles. Use for
  "content-idea", "find my next video idea", "what should I make next", "what's
  trending in my niche", "topic research".
---

# content-idea

Raw view counts rank channel size, not ideas. A 400k video on a channel that usually gets 3 million
is a flop; a 184k video on a channel that usually gets 3,600 is a 51× signal. Every video here is
scored as a **multiple of its own channel's median**, so the ranking is about the idea.

This skill does one job: **it finds the next idea.** It does not write the script, the title
package or the video.

```bash
W=<session scratchpad>/idea; mkdir -p $W; T=.claude/skills/content-idea/tools
python3 $T/collect.py $W                         # fresh lists from every channel in channels.json
python3 $T/rank.py $W --today $(date +%F)        # multiples, formulas, the four cuts, thumbnail sheet
python3 $T/title.py $W/titles.txt                # lint the candidate titles
python3 $T/fit.py idea "Title one" "Title two"   # audience fit: does OUR audience want this topic?
python3 $T/fit.py check script.md --expect trend # audience fit for the script written from the idea
python3 $T/discover.py $W                        # optional: niche channels we don't track yet
```

## Step 1 - Refresh the channel list (once a month, or when asked)

Run `discover.py`. It searches the niche's core queries and lists channels that keep appearing but
aren't in `channels.json`. Add the ones that are really in our lane (elegance, classy, old money,
French chic, style over 40/50/60, women's style) with `--add N`, or by editing the file. Skip
beauty-only, men's style and lifestyle vlogs: a 75× there is not our idea.

## Step 2 - Collect

`collect.py` pulls up to 60 latest videos per channel with `yt-dlp --flat-playlist`. These are
public listings only: never a logged-in session, never the user's cookies. It keeps long-form
videos (3 minutes or more) and records the publish date. A channel needs **at least four videos**
or its median means nothing; the ranking skips thinner channels and says so. Takes 2-4 minutes.

## Step 3 - Rank and cut

`rank.py` scores every video with `swipe.py` (multiple over its channel's median, plus the title
formula from `hooks.json`), then prints four cuts:

| Cut | Question it answers |
|---|---|
| **A. Right now** | What in our lane beat its channel by 2× or more in the last 6 months? |
| **B. Season** | What won in the same 3-month window last year? The video goes out into that season. |
| **C. Our audience** | Which of our own videos beat our median? What our viewers already reward. |
| **D. Evergreen** | What in our lane ever did 10× or more? Formats that keep working. |

It also saves `outlier_thumbs.jpg`. Open it and look. What the winning thumbnails share is half the
idea.

## Step 4 - Read it like an editor

1. **Drop the off-lane rows** even when the multiple is huge (mindset, beauty-only, men's).
2. **Name the one structural thing** the top lane outliers share. Example from 11 Oct 2026: "a
   numbered list that sorts things into elegant vs not: avoid / mistakes / cheapen / IN & OUT".
3. **Cross it with timing.** Cut B tells you what this season rewards. A trend wave that is
   live in cut A right now (several channels at 10×+ in the last two months) beats an old
   evergreen.
4. **Cross it with our audience.** Cut C shows which shapes our viewers already chose ("Never
   Wear" 9.4×, "Look Expensive" 5.4×).
5. **Don't repeat ourselves.** If cut C shows we covered it in the last few months, change the
   angle or drop it.

## Step 5 - Audience fit: what THIS channel's viewers love

The multiple says the niche wants a topic. It does not say **our** viewers want it, or that the tips
inside are the kind the channel is known for. A hot topic told the wrong way upsets the audience
that built the channel. So every idea passes this step before it's shown to the user.

The baseline is the channel's own words: `audience/transcripts/` (29 own videos with views) and
`audience/dna.json` (tip-type rates plus 2,685 comment themes). See it with `python3 $T/fit.py
profile`. What it says today:
- **What we teach:** timeless principles and simple swaps ("instead of X, try Y", named pieces and
  colours). Not fashion news: "runway" is 0.46 per 1,000 words, luxury brands almost never.
- **Our stance on trends, in our own words:** "Elegant women don't chase every trend." "It's all
  about choosing quality over trends." "If a cute trend pops up that you love, get it."
- **What viewers reward:** the calm voice (255 comments), asking for part two (253), timeless
  advice, budget, women 40-70+ ("I am 74… elegance should not end with age"), sharing with
  daughters and friends.
- **Red lines:**
  - calling a colour "not elegant" (667- and 424-like pushback)
  - saying quiet luxury is over
  - shaming or rich-vs-poor language
  - statistics

For each idea, run `fit.py idea "<title>"` and report:
1. **Our audience on this topic:** the closest own videos and their median multiple. Example: habits
   / presence = 2.5×, seasonal wardrobe = 0.8×. Put this next to the niche multiple. A topic the
   niche loves but our viewers have rewarded below 1× must be flagged plainly to the user, never
   hidden.
2. **The lens:** if the idea touches trends, news or luxury, write how it will be told through the
   channel's stance (for trends: "don't chase, choose what works for you", with the timeless version
   you may already own).
3. **Red lines in the title:** none allowed.

When an idea becomes a script, the script must pass `fit.py check script.md` (use `--expect` for the
topic word, e.g. `trend`) with **"FITS THE CHANNEL"** before it goes to the user. The winter-trends
script went from "6 things to fix" (runway talk at 20× the channel's level, "the end of quiet
luxury", a ✕ on bright violet) to FITS after it was rewritten through the channel's lens.

Refresh the baseline when new videos are out: add their transcripts to `audience/transcripts/`
(first line `# <title>`, second line `# views=<n> date=<yyyymmdd> id=<id>`), then run
`python3 $T/fit.py build`.

## Step 6 - Write the 3 ideas

For each idea:
- **A working title.** Write at least 6 titles across the ideas into `titles.txt`, run
  `title.py`, and keep the best per idea with its score. The rules: 60 characters or fewer, a
  number, the subject up front, no vague adjectives.
- **The evidence.** The exact outliers behind it: multiple, views, channel, title.
- **Why now**, in one line (the season, a live trend wave, or our audience).
- **Audience fit**, in one line: our audience's multiple on this topic, and the lens if needed.
- **The promise**, in one sentence: what the viewer gets.

Rank the three by strength of evidence (niche multiple **and** our audience's multiple), not by
taste. When the two disagree, say so, and give the timing reason if a seasonal idea goes first. **Never invent** a multiple, a view count or
a trend. Every number must come from this run's output.

## What to hand back

1. Two or three plain sentences on how the ideas were found (the multiple method, how many channels
   and videos, today's date).
2. The **right now** table and the **season** table: the top 5 each, with multiples.
3. The one shared structure.
4. The 3 ideas, ranked, each with its title score, evidence and audience fit. Star the first one.
5. Honest limits: publish dates are month-accurate; older videos have had more time to collect
   views (so recent high multiples are even stronger than they look); the formula label describes
   the title, not why the video worked.
6. Save it as `classy-academy-test/research-<YYYY-MM-DD>.md` and commit it.

## The gate

Nothing here publishes and nothing here decides for the user. The skill researches; the user picks.
The last line of every run is the question: **ship it, or change it?**

---
`swipe.py`, `hooks.json` and `title.py` come from the MIT-licensed youtube-agent skill pack by Jake
Schincariol (see `LICENSE-youtube-agent`).
