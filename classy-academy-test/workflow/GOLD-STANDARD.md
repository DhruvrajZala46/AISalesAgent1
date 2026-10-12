# The gold standard: how "8 Dressing Rules Every Woman Should Know" was made

The user's favourite video (Oct 2026): idea, script, video, thumbnail and package. **Every new video
is made this way, and may only get better.** The stage playbooks (1-TOPIC ... 5-PACKAGE) hold the
commands; this page holds the recipe and the bar.

## The way of thinking (the user's, never break it)

- **Copy what is proven, never guess.** If it worked for the winners, it can work for us. Every
  decision (topic, tip, line, clip, cut, thumbnail, word) has a number or a quote behind it.
- **Proven twice:** by views (what gets clicked) AND by love (like rate, thank-you comments, "best
  tip ever", saves, shares, requests). One without the other is not enough.
- **Real is non-negotiable:** real women, real footage, real tips, real numbers. Never AI, never an
  invented tip, quote, number or personal story.
- **Our voice, our look.** We copy the proven structure, then tell it calmly and kindly, in the
  channel's words, on the caramel backdrop.
- **The user approves each stage** (idea -> script -> video -> thumbnail -> package). Show progress
  often, deliver fast, and say plainly what is proven and what is thin.

## 1. The idea: proven by views AND by love

What was done:
1. **The whole niche, all time:** every video of 60 niche channels (14,127 videos), each scored by
   how far it beat its own channel's median (the multiple). Saved as `alltime.json`.
2. **Find the shape that wins again and again**, not one lucky video: "Dressing Rules EVERYONE
   Should Learn" 8.0M (71x), the series 1.86M / 1.4M / 1.2M; the "rules" shape had 34 winners at 5x+
   from 16 different channels.
3. **Who it is told to:** "every woman" titles in the niche had a median of 630k views and 3.31%
   liked, against 113k and 1.13% for age-targeted titles -> "Every Woman", shown with women of all ages.
4. **Our own viewers:** `tools/audience_proof.py` on our 29 videos and 2,685 comments (like rate,
   thanks, shares, requests, pushback) -> the idea must fit what they already love and ask for.
5. **New ground:** nothing repeated from our last videos (listed in the script's Proof section).

When YouTube blocks the machine: the user may give a cookies file. Use it only with `yt-dlp
--cookies` for public captions, comments and listings, slowly (YouTube rate-limits after ~30
videos), never print it, read it or commit it.

## 2. The script: every tip proven, told in our voice

The exact steps (Dressing Rules), in order. The `yt-script` skill's rules are built in.
1. **Read first:** `voice.md` ("How I teach"), `2-SCRIPT.md`, the craft rules
   (`research-2026-10-12-craft.md`), LEARNINGS.
2. **Study the winners' insides, never guess:** the 8-15 biggest videos on the topic (multiple + like
   rate), with `yt-dlp` captions + top 100 comments (+ info.json) -> one study file each: the full
   timestamped transcript and the comments sorted by likes. Read every file to the end.
   What to check in every winner:
   - every concrete tip (piece, colour, fabric, fit rule, habit, step) with its timestamp and exact words;
   - HOW it is taught (why, example, demo, before/after, swap, rule of thumb, story, humour);
   - the hook (first lines) and the structure (point names, order, length);
   - the comments: the tips viewers quote, list, thank for, or say they tried (with likes);
     their requests; their pushback (with likes); shares/saves; the feelings they express.
3. **Our own viewers:** `audience_proof.py --video` / `--ask` on our videos near the topic.
4. **The proof map** (a table in `script.md`, section Proof): a tip stays only with two proofs
   (taught by 2+ winners, or 1 winner + our viewers' love/requests, or quoted/thanked by viewers with
   10+ likes). Every tip's top pushback becomes its exception line ("if you love X, keep it, just...").
   Nothing repeated from our last videos. Never invent a tip, number, quote or story.
5. **Write in our voice:** every point = the 7 teaching steps (name -> validate -> why -> principle ->
   what elegant women do -> swap / how-to with named pieces, colours, fabrics -> inner payoff), plus
   "show it" (a before/after, a demo, a test she can do now). Kind, calm, never fear, never shame,
   never "hide flaws". No quotes, no named people, no culture reports, no statistics.
6. **The shape:**
   - **Hook** (~10 s): write 5 against the 21 formulas (`yt-script/hooks.json`), run
     `hookscore.py`, show the top 2 with scores. Barrier removed, a question she can't close.
   - **The turn**: no channel intro, no subscribe pitch; pass-it-down framing; **point 1 by 0:30**.
   - **8 points**, each with a 2-5 word name she can list; one self-identifying question mid-video;
     the guide plug at the END of point 4; recap of the names.
   - **Close**: the family/personal question + part two + "A simple like or comment would mean so
     much to us. Until next time, bye everyone."
   - `[ON SCREEN: ...]` on every beat (DO / DON'T, women of every age, size and skin tone).
   - ~1,300 words, ~9.5 min (our voice: ~138 words/min at speed 0.80).
7. **Gates before the user sees it:** `dna.py` TEACHES LIKE THE CHANNEL, `fit.py check` FITS THE
   CHANNEL, hook score STRONG. Fix and re-run until all pass.
8. **Hand back:** the 2 hooks with scores, the full script with [ON SCREEN], the runtime, both check
   results, one line per point (the tip and why it is valuable to her), the proof table; commit
   `script.md` + `beats.txt`. Last line: **ship it, or change it?** Never build before "ship it".
9. **What the user corrected, and is now the rule:** proven, never invented; in MY voice; never vague;
   valuable enough to like, share and subscribe; the intro short; take time on the research, but
   keep the user posted while working.

## 3. The video: the "stage" edit (from the replay data of 79 videos)

Full rules in `3-VIDEO.md` step 5; the evidence in `research-2026-10-12-edit-evidence.md`.
1. **Sourcing per beat:** ~26 Pinterest searches; prefer try-ons, before -> after by the same
   woman, hands doing it, women 30-70+, several sizes and skin tones. Pick 2-3 options per beat.
2. **Every clip checked before it is used:** `aiscan.py` + the AI tells in the metadata (pin title
   with "Description:", affiliate links, exactly 5/6/8/10/15 s at 24 fps, digit-only uploader names)
   + three frames at full size by eye. Captions/logos over the subject = do not use.
3. **Look inside every take:** `strips.py` (a frame every ~2 s, `key:a:b` to zoom) -> cut to the second.
4. **Word timing:** `words.py` -> every picture lands on the word it shows (`at(i, "red coat")`).
5. **The edit:** white number card -> one calm centred frame per point, the pictures change inside
   it every <=5 s; the same woman from the mistake (red cross) to the fix (green tick); one word-timed
   row only where the script lists things; full-screen only for hook, title, guide, ending; text only
   as card, mark word or row label; one storytelling beat per video where the picture says it
   (rule 6: the screen fills up as "they compete", then one calm red coat).
6. **QA before sending:** `ffr_cmp.py` (every diff < 10, include a card and the recap), render with
   `ffr.py`, `qa.py` (-14 LUFS, 0 black, 0 silence), `empty.py` (0 while talking), `flash.py`, and a
   **per-second contact sheet watched end to end**; fix (burned-in prices, captions, dark frames,
   off-tone shots), re-render, re-check. Deliver 1080p + CREDITS.txt on Gofile.

## 4. The thumbnail: the winners' format, in our look

1. Download the thumbnails of the exact topic's winners (`i.ytimg.com/vi/<id>/maxresdefault.jpg`)
   and count which format wins: here the **same woman twice, red cross / green tick** (8.0M, 1.8M,
   1.2M, 0.84M; median ~1.0M vs ~0.15M for the others).
2. Make three for Test & compare:
   - **A, the winning format in our brand** (`tools/thumb_xo.py`): the same woman from ONE creator's
     own do/don't video (never put a cross on a woman who did not label that look herself);
   - **B, the same image with new words** (`title.py` 100/100);
   - **C, the channel's own layout** (`thumb_make.py`, from our 1.24M video) with women 50-70+,
     because our viewers ask for women their age (39 comments, 1,119 likes).
3. **Feed test** at 320x180 next to the winners: the words read at a glance, the faces stay clear.
4. Real photos only, checked like clips (an AI clip with no watermark was caught here, see LEARNINGS).

## 5. The package

- **Title:** the winner's topic phrase + a number, <= 40 characters, 100/100 on `title.py`.
- **Description:** two search lines in the words she types -> the guide link -> chapters from
  `beats.json` (YouTube's three rules) -> three short paragraphs in our voice -> the family question
  + part two -> 3 hashtags -> every creator credited + thumbnail photos + music.
- **Tags:** 15 real search phrases. **Query test:** the 3 target searches are in the title + first 2 lines.

## The quality bar (check before saying "done")

- [ ] Idea proven by views AND love, with numbers, and new for our channel
- [ ] Every tip has two proofs; every pushback answered with an exception line
- [ ] dna.py + fit.py pass, hook STRONG, point 1 by 0:30
- [ ] Every picture matches its word; the same woman mistake -> fix where possible
- [ ] Zero AI (scan + metadata + eyes), every creator credited, women of all ages
- [ ] QA clean and the whole video watched second by second
- [ ] 3 thumbnails from the winners' format + feed test; package with chapters, tags, query test
- [ ] Everything (text only) committed under `classy-academy-test/videos/<slug>/`

## To make the next one better

- Run the AI metadata check while sourcing, not after: the red-coat clip (redcoat0) passed the
  watermark scan and reached the video. It still has to be swapped out (6:34 and 9:01).
- Pick the thumbnail's mistake -> fix footage while sourcing (one creator's own do/don't clip, no captions).
- Avoid clips with burned-in captions, prices or brand cards from the start.
- Keep the user posted with short progress lines; never go quiet for long.
