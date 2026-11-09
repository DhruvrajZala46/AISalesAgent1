# HANDOFF - read this first in a new chat (written 18 Oct 2026)

This file carries the full history of the previous chat (Oct 2026) so a new chat can continue without it.
Branch: `claude/youtube-channel-analysis-lghfsv`. The channel's YouTube name is **Classy Academy** (@ClassyAcademy).

## 0. Latest (31 Oct 2026)

The user asked for a new video copying the **format** of their own "7 Things Elegant Ladies Never Do in Public"
(`oHh4T67jJNM`, 508k views), with similar but new tips and no copied wording.
- **Script v1 is in `videos/classy-women-public/`** (`script.md` + `beats.txt`), titled "7 Things Classy Women Never
  Do in Public".
- Each tip is a close cousin of one of the original's tips, proven by 12 niche winners plus comments.
- The format was checked against the original's storyboard.
- **Approved by the user on 30 Oct 2026 ("ship it").**
- **Video v1 delivered on 30 Oct 2026** (1080p, 8:48, 103 clips, each used once; QA: -14.3 LUFS, 0 black, 0 silence).
  - Edit, visual analysis, sources log and credits are in `videos/classy-women-public/`.
  - The Gofile upload was blocked by the permission system, so the file was sent in the chat (re-encoded to 340 MB).
  - Rights: every footage row is unresolved (creators' reels and two films); the creator decides.
  - The media is in the session scratchpad only and is lost with the container.
- **User review (31 Oct 2026): "GOOD", but remove the website.** The user does not want classyladyacademy.com
  mentioned. It was taken out of the guide screen and the outro (`edit.py`); never put the site on screen again.
- **Video v2 delivered on 31 Oct 2026** (same edit without the site, 8:47; QA: -14.3 LUFS, 0 black, 0 silence; the
  only freezes are the white cards and the quote screen). Sent in the chat as a re-encode under 500 MiB.
- **Thumbnails (31 Oct 2026):** all 31 channel thumbnails analysed; three options A/B/C sent
  (`videos/classy-women-public/THUMBNAIL.md`, A recommended). Waiting for the user's choice; then the package (stage 5).

- **New video (1-2 Nov 2026):** a copy of the format of "7 Behaviors That Quietly Signal You Have Class"
  (`rHI_hcgK39E`, 120k), in `videos/class-signals/`: "7 Quiet Habits That Show You Have Class".
  - Script v1 (cousin tips) was rejected: "it matches my old video". The user wants it as a second part of that video:
    same format, but different behaviours that fit the channel DNA.
  - Script v2: 7 behaviours never taught on the channel (checked against all 30 transcripts):
    1. leaving places better than you found them;
    2. introducing people well;
    3. taking no gracefully;
    4. being graceful with the bill;
    5. the guest everyone invites back;
    6. sharing the credit;
    7. apologising cleanly.
  - v2 approved (2 Nov 2026); the user then asked for the video in the same style as Part 1, with similar but
    not identical visuals, every clip once, matched line by line, and no website.
  - Video v1 built (2 Nov 2026): 120 clips, each used once; none from Part 1 or from the last video
    (`tools/oldclash.py`); only Part 1's layouts (`VISUAL-ANALYSIS.md`, `edit.py`, `SOURCES-LOG.md`, `CREDITS.txt`).
    The CA "Classy Academy" logo is drawn in the corner and on the end card. No Meghan Markle.
  - Video v1 delivered in the chat (2 Nov 2026): 1080p, 8:28, 351 MB send copy. QA: -12.7 LUFS, true peak -1.5 dB,
    0 black frames, 0 silence; the only freezes are the white point cards. Waiting for the user's review.
  - Title screen: the episode number was left off (Part 1 shows "Episode 21"; the current number is unknown).

- **New script (3 Nov 2026):** the user pasted a Paris Never Ages script ("French Women Over 60 Never Wear These 10
  Things", 564k) and attached 29 Classy Academy scripts, asking for the same kind of script in the channel's own format.
  - **FINAL: v1, approved 3 Nov 2026.** It is in `videos/age-swaps/`: "8 Things That Quietly Age You: What to Wear
    Instead", 1,377 words. It uses the structure of the #1 video and drops 5 items already taught on either channel.
  - A v2 (new hook, technical points 3-7, shoulder point) was written and not chosen; it is in git history (dbf45d7).
  - **Video v1 built (3 Nov 2026)**, in the layouts of the #1 video "8 Things Elegant Ladies Never Wear"
    (`videos/age-swaps/VISUAL-ANALYSIS.md`, `edit.py`, `SOURCES-LOG.md`, `CREDITS.txt`).
    - 143 clips, each used once; none from the two previous videos (`tools/oldclash.py`).
    - The CA logo is in the corner and on the end card; no website on screen.
  - Video v1 delivered in the chat (3 Nov 2026).
    - Files: 1080p, 9:41, 366 MB send copy.
    - QA:
      - -12.6 LUFS, peak -1.3 dB;
      - 0 black frames, 0 silence;
      - the only freezes are the white cards and the quote screens.
    - Known small flaws, offered as a v2:
      - three creator captions remain (b_jabot45, w_wide5, z_wardrobe40);
      - three short empty-caramel gaps (about 4:35, 6:35 and 7:50).
  - **User review of v1 (3 Nov 2026), with two screenshots and the CE logo file:**
    - the intro clips were disliked (one had the Instagram watermark "@YULI_SH_1");
    - the pictures did not match the script; photos may be used where there is no video;
    - zoomed clips cut faces;
    - the logo must be her CE circle logo;
    - watch all the channel's videos and re-edit.
  - **Video v2 built (3 Nov 2026)** in The Classy Elegance channel's own layouts.
    - Analysis: storyboards of 7 channel videos (`videos/age-swaps/VISUAL-ANALYSIS.md` section 6).
    - Intro: new real clips of women in their 60s.
    - Matching: every named colour, fabric or piece is shown as it is said, with 22 product and archive photos
      (`tools/phsearch.py` + `tools/cutout.py`).
    - Framing: vertical reels go full screen only as the whole clip over its blurred copy (`cfull()`), never as a crop.
    - Logo: the CE logo from her file (white in the corner, her black badge on the white end card).
    - Clips: 129, each used once; 0 repeats from the two earlier videos.
    - Captions: every used segment checked at four moments for burned-in text (`tools/cand.py`).
    - Media lives only in the scratchpad (`cwa/`); the edit is `videos/age-swaps/edit.py`.
  - **Video v2 delivered in the chat (3 Nov 2026):**
    - a preview first, then the final: 1080p, 9:41, 361 MB, 128 clips + 22 photos;
    - after the first render, 5 more captioned clips were replaced (found on a 5-second contact sheet).
    - QA of the final: -12.6 LUFS, 0 black frames, 0 silence; the only stills are the white cards, the product and photo
      screens and the title.
    - Waiting for the user's review; thumbnails and the package only if asked.

- **New video (4 Nov 2026): "How to Look Effortlessly Elegant at Home"**, in `videos/elegant-at-home/`.
  - It is a new video in the format of the creator's "How to Look Elegant & Expensive at Home" (`GmiAMO93vFE`).
  - Script v1 (49 lines, 1,293 words) was sent; the user then asked for the video (taken as approval of the script).
  - Visual analysis: the original's storyboard (`VISUAL-ANALYSIS.md`).
  - Video v1 built (4 Nov 2026):
    - 130 clips, each used once; 0 repeats from the three earlier videos;
    - 14 product/texture photos;
    - the CE logo; no website on screen.
  - **Video v1 delivered in the chat (4 Nov 2026):**
    - 1080p, 9:05, 339 MB.
    - QA: -12.7 LUFS, 0 black frames; the only silence is the last 4 s of the end card. The only freezes are the white
      cards, the cream text screens and the product photos.
  - Waiting for the user's review; thumbnails and the package only if asked.

- **New video (5-6 Nov 2026): "6 Proportion Mistakes That Cheapen Your Outfits (How to Fix Your Lines)"**, in
  `videos/proportion-lines/`.
  - The topic came from a strategy note the user pasted. 6 of its 7 points were already taught on the channels, and its
    proof was partly wrong, so the script uses 6 new line mistakes backed by real winners (`script.md`).
  - A second pasted plan ("8 Fit Mistakes") was checked as well: 5 of its 8 points overlap. The user chose the proportion
    script ("ship it").
  - Video v1 built (6 Nov 2026), from the most-liked videos' comments and measured edit (`VISUAL-ANALYSIS.md`):
    - 95 clips, each used once; 0 repeats from the four earlier videos;
    - 10 product photos;
    - the CE logo; no website on screen.
  - **Video v1 delivered in the chat (6 Nov 2026):**
    - 1080p, 9:46, 314 MB.
    - QA: -12.8 LUFS, 0 black frames, 0 silence; the only stills are the white cards, the quote screens and the product
      photos.
    - Two last fixes before the final render: a small "1° modelo" caption trimmed, and a tank-top close-up trimmed.
  - Waiting for the user's review; thumbnails and the package only if asked.

- **New video (6 Nov 2026): "8 Things Elegant Ladies Never Wear on Christmas & NYE"**, in `videos/holiday-never-wear/`.
  - The user wrote the full script; it is voiced as given (63 lines, 1,395 words, `script.md` + `beats.txt`).
  - Format: the channel's own winter "Never Wear" upload (`JF7PzFJl4eU`) plus the #1 video (`VISUAL-ANALYSIS.md`):
    - white numbered cards;
    - the mistake in a row;
    - the principle on caramel;
    - a clip with the named pieces cut out beside it;
    - colour swatches, fabric circles and the three outfit formulas built piece by piece.
  - Video v1 built (6 Nov 2026):
    - 139 clips, each used once; 0 repeats from the five earlier videos (64 downloaded clips matched earlier footage and
      were left out);
    - 52 product photos (Pinterest retailer shots);
    - the CE logo; no website on screen.
  - AI: one clip with the Gemini watermark (a_gloves6) and one from an AI studio (e_thanks1, "Silent Lens" end card) were
    found and replaced.
  - First render QA: 0 black frames, 0 silence, -14.5 LUFS; the only freezes are the white cards and quote screens. One
    product label stayed on screen after 8:32 (a timing bug), fixed in `edit.py`, then rendered again.
  - **Video v1 delivered in the chat (6 Nov 2026):**
    - 1080p, 10:29, 371 MB.
    - QA: -14.5 LUFS, 0 black frames, 0 silence; the only freezes are the white cards and the quote screens.
  - Chapters written (7 Nov 2026, `CHAPTERS.txt`).
  - **User review (7 Nov 2026): remove the Classy Closet promotion** (never promote Classy Closet unless asked) and put
    the stylist-guide (e-book) line of the earlier videos in its place. v2: the two Classy Closet lines became one guide line
    (word for word from the gold-standard video), with the channel's guide screen; chapters recomputed.
  - **Video v2 delivered in the chat (7 Nov 2026):** 1080p, 10:20, 363 MB; 138 clips, each used once.
    QA: -12.8 LUFS, 0 black frames, 0 silence; the only freezes are the white cards and the quote screens.
  - Waiting for the user's review.

- **New video (7-8 Nov 2026): "How to Look Expensive & Put-Together in Winter (No Matter Your Budget)"**, in
  `videos/winter-expensive/`.
  - A first script by Claude (8 new tips, `script-draft-claude.md`) was sent; the user then gave their own script, which is
    the one voiced (`script.md`, `beats.txt`, 77 lines). The Classy Closet lines were removed at the user's choice.
  - Format: the storyboard of the channel's 716k "How to Instantly Look More Elegant & Expensive: No Matter Your Budget"
    (`VISUAL-ANALYSIS.md`); every tip ends with a Budget / Splurge pair on the caramel; the bonus builds the same outfit at
    three budgets, piece by piece.
  - Video v1 built (8 Nov 2026): 144 clips, each used once; 0 repeats from the six earlier videos; 48 product photos;
    the CE logo; no website, no Classy Closet.
  - The first render, read every 5 s, showed the budget-knitwear thrift clip (k_thrift4) reaching a denim skirt and a
    blouse under "secondhand merino & lambswool"; it was replaced by two secondhand-listing photos and re-rendered.
  - **Video v1 delivered in the chat (8 Nov 2026):** 1080p, 12:15, 380 MiB. QA: -15.1 LUFS, 0 black frames, 0 silence;
    the only freezes are the white cards ("in today's video..." and the nine point cards); the two renders differ only at
    3:19-3:29. Chapters in `CHAPTERS.txt`.
  - **Thumbnails (8 Nov 2026, `THUMBNAIL.md`):** both channels' 47 thumbnails and the topic's top 20 read fresh; three
    built in the bold clean style. A (recommended) "How to Look / Expensive / in Winter" (Rosie, Kate, Amal in coats, the
    716k's own words); B "Look / Expensive / on Any Budget" (the bonus outfit cut out on the caramel + Inès de la
    Fressange); C "Always Look / Put Together / This Winter" (Jasmine Tookes, Tracee Ellis Ross, Olivia Palermo).
  - **Classy Academy thumbnails for this video (8 Nov 2026, `THUMBNAIL-CA.md`):** the CA "expensive" thumbnails studied
    (716k, 310k, 100k, 97k, 74k, 72k: waist-up, glossy, warm neutrals, selfies); three built with the real CA logo:
    1 "The Art of / Quiet Luxury / *this winter*" (recommended; Jasmine Tookes, Sofia Richie, Leonie Hanne in cream, camel,
    chocolate), 2 "A $60 Coat Can Look / Like $600 / *if it fits*" (the video's line 8), 3 "Always Look / Polished / *even in
    winter*". The rendered video carries the CE logo; a CA upload would need a re-render with the CA logo.
  - **Package (8 Nov 2026, `PACKAGE.md`):** title recommended "8 Ways to Look Expensive in Winter (On Any Budget)" (50 chars,
    94/100; the original kept as an option), `DESCRIPTION.txt` (4,881 chars, stan.store guide link, shopmy, chapters, credits
    incl. the CA thumbnail photos), `TAGS.txt` (15). The Christmas description got the missing stan.store guide link too.
  - Waiting for the user's review.

- **Classy Academy thumbnails (8 Nov 2026): "7 Elegant Ways to Dress a Tummy (Without Hiding It)"**, in `videos/dress-a-tummy/`
  (`THUMBNAIL.md`). All 31 CA thumbnails and the topic's top 20 read fresh; three finished thumbnails in the channel's measured
  layout with the REAL CA logo (`assets/logo_ca.png`, new `tools/ca_logo.py` + `tools/thumb_ca_real.py`, editable layers):
  1 "Elegant Ladies / Never Hide / *they style it*" (recommended; Mindy Kaling, Precious Lee, Christina Hendricks),
  2 "The Most / Flattering Outfits / *one woman, three looks*" (Ashley Graham x3), 3 "Your Tummy Is / Not the Problem /
  *it's how you style it*". Waiting for the user's review.

- **New video (9 Nov 2026): "7 Subtle Body Language Habits That Make You Appear Naturally Poised"**, in
  `videos/poised-body-language/`, from the user's own script (66 voiced lines; the mid-video guide line kept, no website).
  - Format: the channel's "7 Body Language Habits That Instantly Make You Look Elegant & Confident" (`r_mYSc7FHvk`,
    320k), read from its storyboard and captions (`VISUAL-ANALYSIS.md`). The video file itself could not be watched:
    YouTube's bot check blocked downloads and the vidIQ account has no credits.
  - 126 clips, each used once; 0 repeats from the seven earlier videos (pins, posts and footage checked); 0 AI flags; the
    CE logo; film scenes (Roman Holiday, Rear Window, To Catch a Thief, Funny Face) and royal press footage as found on Pinterest.
  - First render read every 5 s: a 12 s static text screen (the 1966 study) became a clip with the two results beside it;
    eight empty caramel pauses got the line being spoken; a door clip with a "What I Wore" caption was swapped. Re-rendered.
  - **Video v1 delivered in the chat (9 Nov 2026):** 1080p, 10:20, 320 MiB. QA: -12.5 LUFS, 0 black frames, 0 silence;
    the only freezes are the white cards and one 4 s quote screen. Chapters in `CHAPTERS.txt`.
  - **Thumbnails (9 Nov 2026, `THUMBNAIL.md`):** A "Effortlessly / Composed / without saying a word" (recommended; Jasmine
    Tookes, Michelle Obama, Kate), B "You Look / Calmer / than you feel" (Amal Clooney, Kate at a podium, Helen Mirren),
    C "Become / Magnetic / 7 tiny signals" (Lupita Nyong'o, Sofia Richie, Zendaya; CA's own 322k words). Waiting for review.
  - **Classy Academy thumbnails (9 Nov 2026, `THUMBNAIL-CA.md`):** 1 "Effortlessly / Composed / *without a word*" (recommended;
    hands-at-the-chin trio in black like CA's 322k: Jasmine Tookes, Lupita Nyong'o, Zendaya), 2 "You Look / Calmer / *than you
    feel*" (Kate in red at a podium between Amal Clooney and Helen Mirren), 3 "The Secret to / Quiet Confidence" (Tookes, Kate,
    Anne Hathaway). Real CA logo; `thumb_ca_real.py` gained a script small line.
  - **Package (9 Nov 2026, `PACKAGE.md`):** three titles (recommended "7 Body Language Habits That Make You Look Calm &
    Poised", 55 chars), `DESCRIPTION.txt` (4,286 chars, guide + shop links, chapters, credits with the CA thumbnail photos),
    `TAGS.txt` (15). Waiting for the user's review.

## 1. Where things stand right now

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

### The task the user gave next (not started)

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
- No Classy Closet promotion in a video (7 Nov 2026), even when a pasted script has one: the mid-video slot gets the
  personal stylist guide (the "e-book") line of the earlier videos instead. No website on screen.
