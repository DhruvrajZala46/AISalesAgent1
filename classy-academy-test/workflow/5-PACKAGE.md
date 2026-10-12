# Stage 5 - Title, description, tags, chapters

Use the skills `yt-package` (title), `yt-seo` (description, tags, query test) and `yt-chapters`
(chapters checked against YouTube's rules). The model to copy: `classy-academy-test/french-PACKAGE.md`.

## Title

- Write ten, run them all: `python3 .claude/skills/yt-package/title.py titles.txt`.
- 60 characters or fewer (40 or fewer fits the mobile feed in full), a number, the subject up
  front, at most two all-caps words, no hype words.
- Prefer the channel's proven shapes: "N Things Elegant Ladies Never Wear: What to Wear Instead"
  (9.1x), "How to Look Elegant & Expensive" (5.0x).
- Show the top three with scores; the winner plus two runner-ups for Test & compare.

## Description (the channel's layout)

1. **Two search lines** - what the video gives her, in the words she would type (they show above
   "...more" and are the search snippet).
2. `⚜️ Access the Personal Stylist Guide here:` + `https://classyladyacademy.com`
3. **Chapters** - from the final video's timing (`beats.json`): first at 00:00, at least three,
   each at least 10 seconds; one per numbered point plus the hook, the guide and the recap.
   Check with `python3 .claude/skills/yt-chapters/chapters.py` or by its three rules. Retitle each
   as the promise of that section, 3-5 words, in our voice.
4. Two or three short paragraphs in the voice: the opening scene, what is covered, the inner payoff.
5. The question + part-two ask: "Which of these will you try first? ... if you'd like a part two,
   let us know." 🤍
6. Three hashtags.
7. `VISUAL CREDITS` - every creator from CREDITS.txt (minus any clip removed), thumbnail photo
   sources, and the music line: "Classical 4", "Classical 5", "Classical 9", "Classical 10" by
   Jonny S. (Mixkit).

Keep it under 5,000 characters (YouTube's limit).

## Tags

At most 15, about 300-400 characters in total: the exact search phrases, spellings and variants
people type. No unrelated tags.

## The query test

Write the three searches this video should win. Their words must be in the title or the first two
description lines. If not, fix the title.

## Hand back

`classy-academy-test/videos/<slug>/PACKAGE.md` (title + runner-ups, thumbnails order, the full
description in one copy block, tags in one copy block, the query test), committed.
Last line: **ship it, or change it?**
