# HANDOFF - read this first in a new chat (written 18 Oct 2026)

This file carries the full history of the previous chat (Oct 2026) so a new chat can continue without it.
Branch: `claude/youtube-channel-analysis-lghfsv`. The channel's YouTube name is **Classy Academy** (@ClassyAcademy).

## 1. Where things stand right now

**Latest (19 Oct 2026):** the dinner-table topic and script (`videos/dinner-table/`) were REJECTED as basic etiquette (see LEARNINGS). New shortlist in `research-2026-10-19-three-new-topics.md`: (1) Why Some Hair Always Looks Expensive (It's Not the Cut), (2) The Length Rules That Make Every Outfit Look More Elegant, (3) Why Elegant Women Never Have to Fix Their Clothes. 19 Oct: the user asked for ONE topic; after a fresh comparison: "Why Her Hair Always Looks Expensive (It's Not the Cut)" (`research-2026-10-19-final-topic.md`). Topic APPROVED; script written 19 Oct: `videos/expensive-hair/script.md` (1,674 words, 7 points, every claim sourced; reference style = the Grooming Habits and Old Money Fall transcripts, since the user's own script files are not in the repo). Script approved by the user's edit brief (19 Oct). Edit plan written: `videos/expensive-hair/EDIT-PLAN.md` (reference sheet, 84-scene plan covering all 111 sentences, 140 asset briefs, QC, 8 questions). NO footage selected: the user said do not use Pexels/Pixabay/Unsplash or any free stock site, and to ask which sources they use rather than guess. Waiting on Part 5 answers (Q1 sources is blocking). The user declined the yt-dlp storyboard download; do not retry it without permission. Never country-specific.

**The user REJECTED the last video.** That is "6 More Ways to INSTANTLY Sound More Elegant (Part 2)", in
`videos/speak-elegantly-2/` (Gofile v1.1: https://gofile.io/d/lNo4i7J3).

Their verdict was "you have messed up my video again". Their complaints, in their own words:

1. **"You changed my visuals."**
   - I replaced the creator's kind of footage with generic free Mixkit stock: podcast-studio actors, sofa chats,
     New Year parties.
   - The creator's own videos use recognisable elegant women: film scenes (Audrey Hepburn, Grace Kelly, Margot
     Robbie...), interviews (Princess Diana, Emma Watson, Angelina Jolie), and refined lifestyle and fashion reels.
   - "Do not mistake accessibility for suitability."
2. **"You changed my original video formula and format."**
   - I imposed my own template: white cards, caramel quote cards, cream "framed clip + phrase" screens, word cards,
     comment cards, a numbered recap list.
   - "My original video is the evidence. Your preferred template is not."
3. **"Stop turning my new videos into Part Two or sequels."**
   - The title said "Part 2" and the intro said "In our first video...".
   - The rule: **same channel format, new standalone video**, with no reference to earlier videos.
4. **"Do not add commentary or visual elements that I never use."**
   - I invented "from your comments" cards, quote overlays, labels ("a calmer way", "at a wedding"), the
     "Audrey Hepburn · Charade, 1963" caption, and a recap list.
5. **The whole video must feel like the channel**, not only the opening.

### The task the user gave next (DONE 18 Oct: `videos/speak-elegantly-2/FAILURE-ANALYSIS.md`; waiting on the user's answers in its section 8)

**Do NOT make another video.** The user asked for an evidence-based failure investigation of the Part 2 video vs
the original "6 Ways to INSTANTLY Sound More Elegant" (https://youtu.be/RUDXBR8nyHw), with these deliverables:

1. A direct diagnosis.
2. A timestamped comparison table with these columns: Timestamp in new video | What the original demonstrates |
   What I did | Exact mistake | Evidence and channel impact | Required correction.
   - Label each row Confirmed mistake / Likely mistake / Unresolved.
3. A visual mismatch report, clip by clip: why each was inappropriate and what a better-matched clip needs.
4. A format comparison: opening, promise, development, transitions, examples, text use, pacing, ending.
5. A standalone-video assessment.
6. A root-cause analysis: which stage caused each failure (script, visual research, edit plan, asset choice, final
   review).
7. A corrected production specification (A-G):
   - A. format;
   - B. visuals;
   - C. sourcing;
   - D. script-to-visual;
   - E. standalone;
   - F. on-screen text;
   - G. final review.

   Mark each rule confirmed / provisional / unresolved.
8. Missing materials: only what is genuinely needed.

User rules for that answer:
- Don't defend, don't give generic advice, don't promise.
- Never invent observations, sources or timestamps.
- Say plainly what could not be watched.

## 2. Key facts the new chat needs

**The reference video's file cannot be downloaded here.**
- YouTube answers "Sign in to confirm you're not a bot" on every client.
- An attempt to run a token helper was blocked by the permission system; don't retry it.
- What IS available:
  - storyboards (one 160x90 frame every ~5 s);
  - word-timed captions;
  - the "most replayed" heatmap;
  - 20 HD frames of the #1 video;
  - all 30 own transcripts.
- **The best fix: ask the user to upload the reference video file** (and 2-3 other own videos). This is a genuine
  missing material.

**The Part 2 render DOES exist and can be analysed:**
- the edit source is `videos/speak-elegantly-2/edit.py`;
- the script is `script.md`;
- the clip list is `SOURCES-LOG.md`;
- the rendered file is on Gofile (link above). The scratchpad copy may be gone in a new container.

**What the reference actually contains** (`reference-breakdown-RUDXBR8nyHw.md`, `source-trace-2026-10-17.md`):

| Source | Confirmed or likely clips |
|---|---|
| Film scenes | Breakfast at Tiffany's (x2, incl. Audrey's own audio), Sabrina, To Catch a Thief, Scent of a Woman, The Wolf of Wall Street, The Pink Panther, a Monica Bellucci film, Angelina Jolie on a train (the 3.13x replay peak) |
| Interviews | Diana (her own voice), Emma Watson at the UN, Jolie's THR roundtable, Tracee Ellis Ross, Gwyneth Paltrow (Vogue), Amal Clooney, Sofía Vergara |
| Stock | Pexels 8922355, 9520296, 6000621 |
| Creators' and brands' reels | from Pinterest |

- Layout share: full-screen 39%, framed single clip 23%, white cards 20%, caramel/quote cards 12%.
- The heaviest replay is on the before/after phrase moments.
- Its own text: number cards, a few caramel quote lines, phrases beside a framed clip, chat bubbles, the "Like"
  word card. **Check carefully which of my text treatments the reference really had before calling any of them
  "hers".** The user says several were mine.

**Rights:** the creator's footage is mostly unlicensed film/TV and creator clips; that status is unresolved.
- The user wants footage that matches her visual world. Licensing is a separate check that the creator decides.
  Log it in `SOURCES-LOG.md` (`workflow/SOURCES-LOG-TEMPLATE.md`).
- Never silently swap in generic stock because it is free.

## 3. What was built in the previous chat (all in git)

**Analysis**
- `CHANNEL-DNA.md`: teaching / scripting / content DNA.
- `CHANNEL-DNA-diagnosis.md`: why "Never Say" failed.
- `VISUAL-EDITING-DNA.md`.
- `reference-breakdown-RUDXBR8nyHw.md`: a segment-by-segment blueprint.
- `editing-blueprints-top-videos.md`: 5 more top videos.
- `source-trace-2026-10-17.md`: reverse-image trace of about 170 frames.

**Process**
- `workflow/ASSET-RESEARCH-GUIDE.md`.
- `workflow/SOURCES-LOG-TEMPLATE.md`.
- `workflow/tools/revsearch.py`: Yandex reverse image search.
- `workflow/LEARNINGS.md`: every mistake that reached the user.

**Videos made earlier (both rejected)**
- `videos/never-say/`: "8 Things Elegant Women Never Say". Rejected as generic: a phrase-list structure, "We get it"
  templates, stock actors.
- `videos/speak-elegantly-2/`: Part 2, rejected as described above.

**Tools**
- Pipeline: `workflow/tools/build.py` (edit.py -> index.html; it now also has `FILMAUDIO` for a woman's own voice),
  then `npx hyperframes render` (the browser renderer, ~95 min for 8 min).
- `ffr.py`, the fast renderer, does not support the newer layouts.
- Voice: Kokoro `af_heart`, speed 0.80.
- Music: Mixkit "Classical" piano, ~12 dB under the voice, no sound effects.
- Delivery via Gofile.

## 4. Lessons already learned (don't repeat)

- **Start every video from the creator's own videos**, not from competitors or my templates.
- **Never add an empathy line, label or card to pass a checker or "look active".**
- **The teaching unit is a habit**, with the exact words inside it. It is not a list of phrases.
- **Named, recognisable elegant women seen and heard** are a core part of her look; stock actors are not a
  substitute.
- **A new video is standalone**: no "Part 2", no "in our first video".
- **Say what could not be inspected. Never claim a frame, source or licence that wasn't seen.**
- **Mixkit:** only clips whose `-1080.mp4` file returns 200 are free-licence; many are "Restricted".
- **Disk:** `df -h` > 4 GB before rendering.

## 5. User preferences

- Answers in plain, direct English.
- The user approves each stage ("ship it, or change it?").
- Never commit media, keys or cookies. Never use the owner's login.
- Commits go to `claude/youtube-channel-analysis-lghfsv`. No PR unless asked.
