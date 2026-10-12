# Stage 1 - Find the topic

Goal: three ideas the **niche** is rewarding right now **and** that **our viewers** already love,
told the way this channel teaches. Never a guess, never a title from memory.

## Steps

1. Run the `content-idea` skill (`.claude/skills/content-idea/SKILL.md`), all six steps. It does
   the collecting, ranking, shapes, timing and audience fit. Work folder: `<scratchpad>/idea`.
2. Before ranking, refresh our own baseline if new videos are out since the last run: add each new
   transcript to `.claude/skills/content-idea/audience/transcripts/` (first line `# <title>`,
   second `# views=<n> date=<yyyymmdd> id=<id>`), then `python3 .claude/skills/content-idea/tools/fit.py build`.
   Captions come from the public video only (`yt-dlp --skip-download --write-auto-subs
   --extractor-args "youtube:player_client=web_embedded"`). If YouTube blocks it, say so and go
   on with the baseline we have.
3. For each of the 3 ideas, also write **the teaching angle** in one line: what will she know or be
   able to do after watching that she can't today? ("She will know which 7 pieces quietly make an
   outfit look cheap, and the exact swap for each.") If the idea can only be told as news,
   quotes or a culture report, drop it: that is not how this channel teaches.
4. Check what we already covered (cut C) so the idea is a new angle, not a repeat.

## Rules

- Public listings only. Never a logged-in session, never the user's cookies or account.
- Every number comes from this run's output. Never invent a multiple, a view count or a trend.
- Red lines in a title: calling a colour or culture "not elegant", "quiet luxury is over",
  shaming, rich-vs-poor, statistics.
- The skill finds ideas only. It does not write the script.

## Hand back

The `content-idea` report (how it was found, the right-now and season tables, the one shared
structure, 3 ranked ideas with title score, evidence, audience fit, teaching angle), saved as
`classy-academy-test/research-<YYYY-MM-DD>.md` and committed. Last line: **ship it, or change it?**
