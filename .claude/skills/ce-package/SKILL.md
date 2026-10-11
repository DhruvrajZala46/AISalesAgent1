---
name: ce-package
description: >-
  Package a finished Classy Elegance video for upload: 10 titles linted with
  yt-package/title.py, 3 thumbnails for YouTube Test & compare built on the
  niche's proven outlier patterns, description with chapters (yt-seo +
  yt-chapters rules), 15 tags, exact SRT captions from the beats, and the Studio
  upload checklist. Use for "ce-package", "title and thumbnail", "description and
  tags", "upload settings", after ce-video.
---

# ce-package: title, thumbnails, description, upload

Read `.claude/skills/yt-package/SKILL.md`, `yt-seo/SKILL.md` and `yt-chapters/SKILL.md`. Their
rules apply.

## Title
Write 10, then rank them with `python3 .claude/skills/yt-package/title.py titles.txt`. Keep 60
characters or fewer, a number, the subject up front, and no vague adjectives. Mirroring the
channel's own winning shapes works ("N Things Elegant Ladies Never Wear…" = 1.2M).

## Thumbnails: 3 variants for Test & compare
1. Use `rank.py`'s `outlier_thumbs.jpg` (from ce-idea) to see what's winning. The patterns proven
   in Oct 2026, with multiples:
   - a face looking at the viewer, cut out with a white outline (12-13×)
   - products floating around a person (9×)
   - wrong vs right ✕ / ✓ (6-9×)
   - a short spoken statement, not a title ("do less. look better." 8×)
   - mood-board collage (15×)
2. Build each variant by **combining 2-3 patterns**, plus one in the channel's proven 3-panel serif
   formula as the control. The winter set was D Cheap/Chic products ✕/✓ around a smiling woman,
   E "cold, but chic." mood board, and A the 3-panel "Avoid These".
3. Templates: `tools/thumbs_outlier_patterns.py` (D/E/F) and `tools/thumbs_round1.py` (A/B/C).
   Point `SRC`, `FONTS`, `V4` at the work dir. 1280×720. Use the warm caramel glow, Playfair +
   Pinyon, the white sticker outline (clean the alpha first), the CE logo, and real Pinterest
   photos (credit them).
4. Every variant must pass `title.py --title "<title>" --thumb "<words>"`: 3 words or fewer, no
   word shared with the title. Check each at feed size (360 px and 168 px wide) before sending.

## Description, chapters, tags, captions
- The first two lines say what the video gives, in search words. Then the stylist-guide link
  placeholder, then chapters from `beats.json` (first entry 00:00, at least 3, each at least 10
  s), then the longer paragraph, the part-two ask, 3 hashtags, and credits.
- 15 tags, comma-separated, under 500 characters, for spellings and exact search phrases only.
- Captions: `python3 .claude/skills/ce-package/tools/srt.py <work>/beats.json videos/<slug>/captions-en.srt`.
  It's exact text from the script. Upload under Subtitles → Upload file → With timing.

## Studio checklist (tell the user)
- Category **Howto & Style**, language English, Comments on with Top sort.
- End screen: the channel's best video plus Subscribe. Card at the stylist-guide moment.
- After upload: Thumbnail → **Test & compare**. Don't change the title during the test.
- The altered-content disclosure isn't needed for real clips with a non-impersonating narration
  voice. Say so honestly and let the user decide.

Save `videos/<slug>/PACKAGE.md` + thumbnails (jpg is gitignored; send them with SendUserFile),
commit, and end with **"Ship it, or change it?"**
