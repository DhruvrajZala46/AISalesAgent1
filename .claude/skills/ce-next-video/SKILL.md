---
name: ce-next-video
description: >-
  The Classy Elegance end-to-end video workflow: find the next topic with real
  niche data, write the script in the channel voice, build the full video from
  real credited Pinterest/TikTok clips in the channel's edit style, render 1080p,
  and package it (title, 3 test thumbnails, description, tags, captions). Use when
  the user says "ce-next-video", "make my next video", "next video", or names any
  step of it. Runs ce-idea -> ce-script -> ce-video -> ce-package with a user
  approval gate between each.
---

# ce-next-video: the whole Classy Elegance pipeline

This is how the winter video ("7 Things Elegant Ladies Never Wear in Winter", Oct 2026) was made
and approved. Follow it in order. Each step is its own skill. Read that step's SKILL.md before you
start it.

| Step | Skill | Output | Gate (wait for the user) |
|---|---|---|---|
| 1 | `ce-idea` | 3 ranked ideas from niche data, with evidence | User picks one |
| 2 | `ce-script` | `script.md` + `beats.txt` in the channel voice, hook scored | User approves the script |
| 3 | `ce-video` | Full 1080p video, every line visually checked | User reviews the video (times to fix) |
| 4 | `ce-package` | Title, 3 Test & compare thumbnails, description, tags, chapters, captions | "Ship it, or change it?" |

## Before anything
1. Read `channel/voice.md`, `channel/how-you-edit.md`, `channel/RULES.md` and `channel/LESSONS.md`.
   LESSONS.md is the user's own feedback across the winter video. Every line there is a hard
   requirement.
2. Work in a scratch folder (the session scratchpad), never in the repo: footage is third-party
   and large. Commit only text deliverables to `videos/<slug>/` (research, script, package,
   credits, captions). `.gitignore` already blocks media.
3. The user writes in short, urgent messages. They want the result, not a menu. Give short,
   honest progress updates during long steps (renders take about an hour). Never claim a check
   that wasn't run.

## The non-negotiables (from the user, word for word in spirit)
- **Real clips only.** Pinterest, TikTok and Instagram, with every creator credited. **Never AI
  clips.**
- **Every visual must earn its place.** With the sound off, the viewer must understand the tip:
  real before/after, the actual item named, real elegant women.
- **No clip is used twice** in a video. Fresh footage keeps arriving.
- **The channel's pace:** about 126 words a minute (Kokoro `af_heart`, speed 0.80), calm, smooth,
  never rushed.
- **Continuous warm music from the first second to the last.** Soft, audible sound effects.
- **The CE logo** (The Classy Elegance), not the old CA logo.
- **Deliver the full-quality 1080p file as a download link** (the chat limit is 30 MB). Gofile
  works.
