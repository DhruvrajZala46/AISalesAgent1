# HANDOFF - read this first in a new chat (written 18 Oct 2026)

This file carries the full history of the previous chat (Oct 2026) so a new chat can continue without it.
The channel's YouTube name is **Classy Academy** (@ClassyAcademy); the second channel is **The Classy Elegance**. The current branch is named under START HERE.

## START HERE (written 17 Nov 2026 for a new chat)

**Branch: `claude/stoic-tesla-w3up2y`.** All work since 16 Nov is on this branch and is NOT on the repository's default
branch (`claude/youtube-channel-analysis-lghfsv`). A new chat must start on this branch, or fetch and merge it first:
`git fetch origin claude/stoic-tesla-w3up2y && git merge --no-edit FETCH_HEAD`.

**Where things stand**
- **Princess Diana video** (`videos/princess-diana-style-rules/`): script approved; video v1 delivered (12:06); three
  thumbnails delivered and shipped by the user; titles, description and tags delivered (`PACKAGE.md`). **Waiting for
  the user's "ship it, or change it?" on the package.** Nothing else is in progress.
- **Deep channel research (18 Nov 2026, `research-2026-11-18.md` and `research-2026-11-18b.md`):** the user said the
  suggested topics have not brought views and asked for channel-specific research. Found: the channel's audience is its
  Princess Diana story Shorts (13 Shorts, usual 18,000, best 75,000; 319,700 Shorts views against 35,700 long views);
  style-advice long videos sit at a usual 377. No women's style-advice video has reached 10M anywhere (131 searches).
  A live wave: small faceless channels (1,200 to 78,000 subscribers) get 100,000 to 945,000 on true stories about royal
  and iconic women. Fair test on 4,834 videos from 179 small channels gave four ideas, in order: things Diana loved you
  can still buy (3.76x); Diana's jewels, where they are now (2.41x angle); the 10 most elegant royal women ranked
  (1.44x); the story of Diana's wedding dress (the channel's own best Shorts). **Waiting for the user's pick; no script
  started.** Needed from the user: Studio numbers (impressions, click-through, view duration) of the last long videos.
- **New topic and script (17 Nov 2026, later the same day; `research-2026-11-17b.md`,
  `videos/french-beautiful-with-age/script.md` + `beats.txt`):** the user asked again for the one best proven topic
  and its script in The Intemporelle's format. Pick: "French Women Get More Beautiful With Age: 7 Rules" (94/100;
  other title "7 Rules French Women Age By", 100/100). Proof: the "more beautiful / prettier" title family is the
  niche's strongest in six months with losers counted (22 videos, 13 channels, 2.81x, 64% at 2x+ against 21%); the
  French title is its live wave (490,000 and 304,000 in Oct 2026). Told to the user: 36 copies of the exact title in
  six weeks have a usual result of 1.14x, and on channels under 2,000 subscribers a usual 270 views. Script v1: 41
  lines, 1,734 words, seven rules, each on the published words of Ines de la Fressange, Mireille Guiliano or Caroline
  de Maigret (sources in the script's section B); `fit.py` FITS; hook 57. **Waiting for "ship it, or change it?"; no
  voice or video started.** The Diana video is now uploaded to The Classy Elegance (seen in today's list).
- **Charm video** (`videos/unforgettable-charm/`): finished and uploaded by the user to The Classy Elegance.
- **Next topic already researched:** "7 Ways to Look Prettier Without Changing Your Face" (`research-2026-11-16b.md`).
  Second style icon: Carolyn Bessette-Kennedy (`research-2026-11-16c.md`).
- **Open questions the user has not answered:** CA or CE logo on thumbnails (the videos carry CE, the thumbnails CA);
  whether the unnamed faces on the charm thumbnails were checked; YouTube Studio numbers (click-through, retention).

**What a new chat has and does not have**
- Has (in git): every script, edit, clip list, sources log, research report, thumbnail write-up and package; the
  working scripts of the last build (`workflow/session-tools/diana/`, with `NOTES.md`, the search phrases and both
  screening passes); the research data (`research-data/`: the 59-channel niche table, the Diana YouTube search table,
  the Intemporelle transcript the user pasted).
- **Does not have: any media.** Videos, clips, photos, thumbnails and voice files lived in the old session's scratchpad
  and are gone. The user has the delivered files. To change the Diana video, rebuild from
  `videos/princess-diana-style-rules/`: `sources_used.json` (the pin and file link of all 96 clips, 54 photographs and
  the thumbnail photos), `clips.py` (the seconds used), `edit.py`, `beats.txt`, `beats_tts.txt` (the voice text with
  years spelled out), `gaps.json`, `words.json`. Steps: `workflow/setup.sh <work folder>`, voice (`tools/tts.py`,
  Kokoro `af_heart` 0.80), download the clips and photos, `tools/build.py`, `session-tools/diana/bgswap.py`,
  `tools/flash.py`, snapshots, `render_loop.sh`, `after.sh`. Thumbnails: `thumb_spec_ca_1080.json` with
  `tools/thumb_ca_real.py` (A) and `thumb_research/build_bc.py` (B, C).

**Rules the user has set (all still stand)**
- Approve each stage; every hand-back ends "Ship it, or change it?". Plain, direct English. Short progress lines.
- **Never guess**: every topic, tip, title and thumbnail choice proven from data read that day; say what could not be
  checked. No topic or thumbnail can be promised to go viral; say so.
- Real footage only, never AI. Visuals from Pinterest / Instagram / TikTok only, never free stock sites. No clip
  repeated in a video or from an earlier video (`oldclash.py`). Every visual matches its script line. No sound effects.
- No Classy Closet promotion (the personal stylist guide line is allowed). No website on screen. No Meghan Markle.
  No "Part 2". Never say "Classy Academy" in a script. Thumbnails at 1920x1080.
- Never commit media, keys or cookies. Never use the owner's login. No pull request unless asked.

**What does not work on this machine**
- YouTube video pages ("Sign in to confirm you're not a bot"): no video file, captions or comments. Public lists and
  searches work with `yt-dlp --flat-playlist -J` (keep any result with 10+ entries even when it exits non-zero).
- vidIQ: 0 credits until 12 Dec 2026.
- Screening helpers stop at the 5-hour usage limit: resume them with a message, do not start new ones.

**The method that produced the last two videos** (`workflow/LEARNINGS.md` has the checks):
research report -> script in the reference format, every fact sourced -> voice and word timings -> search Pinterest
video pins (phrases ending in "video") -> first screening on contact sheets -> download, shrink, duplicate / reuse /
AI checks -> second screening on frame strips -> every chosen window viewed at large size -> edit in the channel's
own layouts -> snapshots of the whole edit -> render -> QA -> send -> sources log, credits, chapters -> thumbnails
(research winners against losers first) -> titles, description, tags.

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

- **New video (11 Nov 2026): "Understated Winter Footwear Rules That Instantly Elevate Everyday Outfits"**, in
  `videos/winter-footwear/`, from the user's own script (51 voiced lines; the Classy Closet paragraph removed by the standing
  rule; the guide line after rule four kept; no website).
  - Format: the channel's own winter video (`JF7PzFJl4eU`) layouts (`VISUAL-ANALYSIS.md`): number cards, the problem in a
    row of clips, the fix beside its product cut out on the caramel, "the test" written line by line beside a clip.
    Classy Academy's shoe video (`1GLuLkBCIEs`) could not be read: YouTube's sign-in check.
  - 95 clips, each used once; 0 repeats from the eight earlier videos (pin ids, posts, pin images and footage checked);
    0 AI flags; 12 product cut-outs; the CE logo.
  - First render read every 5 s: the "replace the heel tip" clip turned out to be scuff removal with a caption; swapped
    for a cobbler working on a heel, re-rendered (only those 4 s changed).
  - **Video v1 delivered in the chat (11 Nov 2026):** 1080p, 7:33, 262 MiB. QA: -15.0 LUFS, 0 black frames, 0 silence;
    the only freezes are the white rule cards. Chapters in `CHAPTERS.txt`.
  - **Thumbnails (11 Nov 2026, `THUMBNAIL.md`):** copied from the topic's proven winners (24 YouTube searches): A Anna Bey's
    face + red-X layout (3.9M family, 412k boots) with Olivia Palermo; B Carl Murawski's side by side (1.28M) "Tired to
    Elegant"; C Elvira Hartwell's caps + X/tick (622k) "STOP RUINING YOUR BOOTS". **Rejected by the user as "still basic, not great".**
  - **Thumbnails v2 (11 Nov 2026, `THUMBNAIL.md` section A, `make_thumbs_v2.py`):** 42 searches, 38 lane videos with 1M+
    views, every thumbnail read and counted, each winner scored against its own channel (`yt-viral`). Finding: the
    creator's-face formula is the most common (15 of 38) but reaches about 1 view per subscriber; before / after and
    wrong / right reach 6-8 and made small channels' videos travel. Built without a borrowed face: 1 BEFORE / AFTER
    (recommended), 2 WRONG / RIGHT (the heel check), 3 LOOKS CHEAP! (three boots, red X). Suggested title "8 Winter Boot
    Rules That Instantly Elevate Every Outfit". Waiting for the user's review.
  - **Package (11 Nov 2026, `PACKAGE.md`):** three titles (recommended "8 Winter Boot Rules That Instantly Elevate Every
    Outfit", 55 chars), `DESCRIPTION.txt` (3,595 chars: guide + shop links, chapters, credits with the v2 thumbnail 1
    photo), `TAGS.txt` (15). Waiting for the user's review.

- **Classy Academy idea research (11 Nov 2026, `research-2026-11-11.md`):** the user asked for the one next idea with the
  highest odds of 10M views. About 32,000 videos scored. The elegance niche has no 10M video (best: Anna Bey 8.7M);
  hairstyles is the only lane topic with many (24 at 10M+ from 19 channels, small channels included) and it is the
  channel's own second-best video (966k, 8.0x). **The user rejected hairstyles: outside the channel's niche.** Re-ranked
  inside the niche: the pick is "12 Table Manners Elegant Ladies Never Forget" (26 adult etiquette videos at 1M+ from 18
  channels, 7 at 5M+, Jamila Musayeva 7.2M at 124x; new ground for the channel, in its "Never Do" format); second,
  dressing rules; third, the put-together wave. Waiting for the user's choice.

- **Scarf script (12 Nov 2026, `videos/elegant-scarf-ties/`):** the user chose idea 2, "10 Elegant Ways to Tie a Scarf This
  Winter". Script v1 in the hairstyles script's format: 89 lines, 1,550 words, ten ties each proven from written
  tutorials read that day (Proof table), taught in the order of how they begin. Hook 75 STRONG; `dna.py` and `fit.py`
  pass.
  - **v2 (12 Nov 2026):** the user asked for no "Classy Academy" in the script and the channel's exact style. Rewritten on
    the channel's own how-to script (958K hair video) and the phrases of its biggest scripts; the channel's name is
    spoken nowhere. 77 lines, 1,608 words; hook 72 STRONG; `dna.py` and `fit.py` pass. v1 kept as `script_v1.md`.
    **Rule from the user: never say the channel's name in a script.**
- **Scarf video (12 Nov 2026, `videos/elegant-scarf-ties/`):** the user approved script v2 ("ship it, now build the full
  video") and asked for: visuals found very carefully and matched line by line; better music ("BG music of previous video
  was not good, and sound effects are too much"); the channel's own editing, re-researched; Pinterest / Instagram / TikTok
  only; no clip twice.
  - **Edit built:** 10:58, 54 reels and 1 photo, 226 elements; layouts of the channel's own tutorial video (white card per
    tie, vertical clip at the left with stacked step lines, full screen only for hook, guide and ending).
  - **Sound:** no sound effects (none were ever added). The bed changed from "Romantic" (51% of its energy below 120 Hz and
    10 dB swells, measured) to "Piano Reflections" by Ahjay Stelino, levelled to within 0.9 dB, 14 dB under the voice.
    Chosen by measurement, not by ear.
  - **Footage:** 84 Pinterest video searches in four rounds, 537 downloads; every tie verified on large frames before a
    line was assigned. One real photo stands in for "a cream scarf on a camel coat" (no real video exists in the search
    results; the two matches were AI-made).
  - **Logo:** The Classy Elegance mark, as asked for the previous video; flagged to the user in case this one is meant
    for Classy Academy.
  - YouTube is still blocked from this machine, so the channel's look and sound come from the October measurements.
  - Files: `edit.py`, `VISUAL-ANALYSIS.md`, `SOURCES-LOG.md`, `CREDITS.txt`, `CHAPTERS.txt`, `picks.md`.
  - **Delivered in the chat on 12 Nov 2026:** 1080p, 10:58, 258 MiB. QA on the delivered file: 0 black frames, 0 silence,
    -12.7 LUFS; the only still moments are the white cards, three text lines on the caramel and the one photo. The file
    was also read on 262 time-labelled tiles at two offsets.
  - The first render ended on a 15-second plain thank-you screen. The ending was rebuilt over three clips as its own
    short composition (`cws_tail`) and joined on with a half-second dissolve; `edit.py` holds the same ending.
  - **Waiting for the user's review.** Open points told to the user: the music was chosen by measurement, the logo is
    The Classy Elegance, one line uses a photo, and no clip is licensed.
  - The work folders are `cws` and `cws_tail` in the session scratchpad; the media is not in git.
- **Scarf thumbnails (13 Nov 2026, `videos/elegant-scarf-ties/THUMBNAIL.md`):** asked for the three most proven thumbnails
  in the Classy Academy look, with the why behind each.
  - Research: 88 YouTube searches, 832 neck-scarf long-form videos, 58 at 1M+ (2 at 10M+); 214 thumbnails tagged by eye in
    three view tiers (`thumbnail-research-tags.txt`); each winner against its own channel (median 286x).
  - What separates the 1M+ thumbnails from the 2k-100k ones: five or more finished looks at once (17% against 1%), the head
    cropped so the scarf is the subject (31% against 15%), a white or very light background (37% against 15%). Titles: a
    number of ways (67% against 25%); season words are rare among winners (3% against 11%).
  - Built (`make_thumbs.py`, 1920x1080 and 1280x720, CA logo): **A the set** (all ten ties, five by two, "10 WAYS" disc),
    **B one scarf** (one woman holds it open, then three ways; "1 SCARF. 10 WAYS."), **C three knots** (three large ties,
    no words). Every picture is a frame of a clip in the video; nothing is enlarged.
  - Title recommended: "10 Elegant Ways to Tie a Scarf" (the season dropped); the approved title stays as the test title.
  - Told to the user: no guarantee (0.2% of these videos reach 10M); B shows one woman's face four times from a reel that
    may be a repost; B's "1 scarf" is the script's line though ties 9 and 10 need a blanket scarf; the thumbnails carry
    the CA logo while the video carries the CE logo. **Waiting for the user's review.**
- **Scarf package (13 Nov 2026, `videos/elegant-scarf-ties/PACKAGE.md`, `DESCRIPTION.txt`, `TAGS.txt`):** title options
  (recommended "10 Elegant Ways to Tie a Scarf"), a 3,305-character description in the last packages' layout with 13
  chapters and the credits (48 account names, one photo, music, thumbnail line), 15 tags. Told to the user: the credit
  names are Pinterest account names and an @name can link to an unrelated YouTube channel. Waiting for the user's review.
- **Scarf thumbnail D (13 Nov 2026):** the user asked for "one thumbnail exact same as Classy Academy". Built with
  `thumb_ca_real.py` and `videos/elegant-scarf-ties/thumb_spec_ca_1080.json` at the tool's default positions: three panels
  from the video's clips, "10 Elegant Ways / To Tie a Scarf / this winter", CA logo, 1920x1080. Checked among the channel's
  eight top thumbnails. Told to the user: it matches the channel but is the weakest of the four against the scarf research.
  Waiting for the user's review.
- **Diana package (17 Nov 2026, `videos/princess-diana-style-rules/PACKAGE.md`):** the user shipped the thumbnails
  ("ship it, now write the description and tags titles"). Three titles (recommended: "Princess Diana's 8 Timeless
  Style Rules", 100/100; 2: "8 Fashion Rules Princess Diana Lived By"; 3: "The 8 Rules Behind Princess Diana's Most
  Iconic Outfits"), `DESCRIPTION.txt` (4,955 characters, 12 chapters, credits, signed Classy Academy), `TAGS.txt` (15).
  Search words taken from the titles of the 77 Diana style videos with 100k+ views. **Waiting for the user.**
- **Diana thumbnails (17 Nov 2026, `videos/princess-diana-style-rules/THUMBNAIL.md`):** the user asked for the most
  clickable thumbnail, one in the channel's style and one built on the biggest videos, "the one you would bet on".
  Research: 79 YouTube searches (3,480 videos; 690 Diana style videos), 177 thumbnails read, 127 scored against their own
  channels. Findings: Diana herself in a famous outfit 21.4x; one picture 46.2x against 14x for collages; no words
  14.3x against 5.4x (1-3 words) and 2.7x (4+); other royals and tabloid text fail most; 11 of the 13 with 1M+ have no
  words. Three sent at 1920x1080: **A** your three-photo format ("Princess Diana's / Style Rules / *8 timeless
  rules*"), **B** one picture, the black dress, no words (my first choice), **C** two pictures with a gold ring round
  the detail (clutch, flag). Honest limits said: no promise of 10M (one Diana style video above 10M exists), no words
  is new for the channel, photos not licensed, CA logo. **Waiting for the user's choice.**
- **Diana video v1 (17 Nov 2026, `videos/princess-diana-style-rules/`): delivered in the chat on 17 Nov (318 MB re-encode). QA of the render: 12:06, 1080p30, -13.3 LUFS, 0 black frames, 0 silence; the only still stretches are the white cards, the sentence screens and three photograph screens; no dark frames in any prepared clip (`flash.py`); checked at 179 snapshots and 121 frames of the finished file.** The user approved the script
  ("ship it, now build the full video") and asked for unique, all-new clips and the channel's own old style, researched
  first. 12:06, 1080p, voice Kokoro `af_heart` 0.80, one piano bed ("Classical vibes 3", 15 dB under), no sound effects.
  - **96 clips in 105 windows + 54 press photographs of Diana** (about 160 pictures). Every rule is proved with real
    photographs whose pin captions name the moment (AIDS ward April 1987, Japan 1986, the balcony, polo 1988, London
    1994, Bosnia 1997, the Christie's sale June 1997, 29 June 1994), framed on the caramel with the place and year, plus
    13 clips of real archive film. Rule 5 shows two gowns before and after their alteration.
  - **All new:** 602 reels downloaded from 153 search phrases; 106 repeat earlier videos' footage and are not used
    (`oldclash.py`, charm video included). No clip repeated inside the video.
  - **Layouts:** only the channel's own (`VISUAL-ANALYSIS.md`); the named woman shown in photographs and archive film,
    as `VISUAL-EDITING-DNA.md` records for Audrey and Diana.
  - **Rights: nothing is licensed**, and this video carries more press photographs than any before (`SOURCES-LOG.md`:
    every row unresolved). 37 everyday clips are marked PARTLY. The creator decides.
  - Work folder (media, lost with the container): scratchpad `cdi/`. Text is in the repo: `edit.py`, `clips.py`,
    `eye_notes.txt`, `picks.md`, `gen_docs_diana.py`, `SOURCES-LOG.md`, `CREDITS.txt`, `CHAPTERS.txt`,
    `VISUAL-ANALYSIS.md`.
  - **Waiting for the user's review ("ship it, or change it?").** Not made yet: thumbnails, title, description, tags.
- **Diana script v1 (17 Nov 2026, `videos/princess-diana-style-rules/script.md`, `research-2026-11-17.md`):** the user
  asked for the one best proven topic and the script in The Intemporelle's exact format. Pick: "Princess Diana's 8
  Timeless Style Rules" (title 100/100). Script built beat by beat on the pasted Intemporelle transcript (cold-open
  question, "most of us / almost no one", the reframe, the promise and open loop, a definition chapter, named rules with
  "Here's the truth", the "if you're still here" line, a mid-video comment question, the guide as the mid-roll, "let's
  bring it all together", three actions, the closing echo). 43 lines, 1,676 words; every Diana fact sourced (section
  B); fit.py FITS; hook 58. Left out: weights in hems (no source), heel-height claim, green-suit count. **Approved by the user on 17 Nov 2026 ("ship it").**
- **Style-icon videos (16 Nov 2026, `research-2026-11-16c.md`):** the user asked which Intemporelle videos introduce an
  elegant woman, and which woman (Queen Elizabeth, Diana, others) is perfect for the channel. The videos could not be
  watched (YouTube blocks this machine; vidIQ 0 credits). Its two real style introductions (Olivia Palermo, Carolyn
  Bessette) did 0.9x. Across YouTube Princess Diana is the most proven (6 style videos with 1M+; "10 Fashion Tricks
  Princess Diana Used..." 2.37M). Pick: **Princess Diana as style rules** ("8 Things Princess Diana Never Wore",
  100/100). Second: Carolyn Bessette-Kennedy (FX/Hulu "Love Story", Feb 2026). **Waiting for the user.**
- **Next topic from The Intemporelle, after charm (16 Nov 2026, `research-2026-11-16b.md`):** the user asked again for
  one proven topic from that channel. Every topic of its 25 videos was tested (38 YouTube searches, 231 videos against
  their own channels, the 59-channel niche). Pick: **looking prettier without changing your face** (its "Pretty
  Privilege" video, 102k, 1.4x; niche 14 videos, usual 2.16x, 6 at 3x+; 10 how-to videos for women with 1M+). Working
  title "7 Ways to Look Prettier Without Changing Your Face" (94/100). Second: hobbies. **Waiting for the user.**
- **Charm thumbnails (16 Nov 2026, `videos/unforgettable-charm/THUMBNAIL.md`):** the user asked for the three most
  proven thumbnails in the exact Classy Academy format, learned from million-view videos, with the why behind each.
  - Read: 102 YouTube searches (4,442 videos, 2,227 in the lane), all 136 1M+ thumbnails, samples of the middle and low
    tiers, 186 thumbnails scored against their own channel (250 channel lists), the 106 charm/presence thumbnails of the
    59 elegance channels at 3x+ or under 0.7x, and all 32 Classy Academy thumbnails.
  - Found: 1-3 words and an expressive real face separate winners; talking heads and neutral posed faces sit on losers;
    "not your looks" is the strongest niche phrase (5 videos, 5.1x); CA's own winners are "Elegant Ladies / Never ...",
    its trait-label behaviour thumbnails all lost (0.2-0.6x).
  - Built (1920x1080, CA logo, sent to the user, not in git): **C recommended** "Charming Women / Never Do This /
    \*avoid these\*" (Diana, Jackie Kennedy, Kate, all laughing); A "Not Her Looks / It's Charm / \*it can be learned\*";
    B "The Woman People / Never Forget / \*it's not her looks\*". Title kept: "5 Quiet Habits That Make a Woman
    Unforgettable" (94/100). Seven of nine pins do not name the woman; rights unresolved.
  - **Waiting for the user's choice.**
- **Charm video v1 (16 Nov 2026, `videos/unforgettable-charm/`):** the user approved the script ("ship it, now build the
  full video"), said the last music was not good and the sound effects were too much, and asked for the channel's own
  editing re-checked, visuals from Pinterest / Instagram / TikTok only, no clip twice, every visual matched to its line.
  - Sound: Kokoro af_heart 0.80 voice; ONE solo-piano bed, "Classical vibes 3" by Grigoriy Nuzhny (Mixkit), chosen from
    234 measured tracks, evened to within 1.0 dB, 15 dB under the voice, no ducking; **no sound effects**.
  - Look: the channel's behaviour-video layouts (white card per habit; clip on the caramel with the lesson beside it;
    rows with script labels; the speech video's framed clip on cream with the exact words; Marilyn Monroe and Princess
    Diana in real archive film; full clips with the line over a soft dark glow). CE logo; no website; no channel name.
  - Footage: 600 Pinterest video pins of IG / TikTok reels downloaded (169 searches), screened twice, 108 used once each
    from 103 creators; 130 downloads that repeat earlier videos and 9 picks with captions or watermarks thrown out; the
    121 snapshots of the first build led to 4 more fixes, the first render to a fifth (a cinema reel's own fade to
    black cut out; `eye_notes.txt`). 23 of 108 rows are PARTLY a match
    (`SOURCES-LOG.md`, `VISUAL-ANALYSIS.md` section 5). Rights: all unresolved.
  - Finished file (sent to the user, not in git): 10:47.6, 1920x1080, 30 fps, -13.6 LUFS, 0 black frames, 0 silence,
    0 flashes in the 108 clips; still stretches are only the white cards and the text screens. Delivery copy 274 MB
    (libx264 crf 18). Render: segmented capture stalled twice; `--resume` kept the finished segments.
  - **Waiting for the user's review ("Ship it, or change it?").** No title package or thumbnails made yet.
- **Charm script v1 (16 Nov 2026, `videos/unforgettable-charm/script.md`, `beats.txt`):** the user accepted the topic,
  pasted the transcript of the reference video and asked for it in Classy Academy's exact format and DNA, "no other
  changes", after checking every channel script.
  - Read in full first: all 11 Classy Academy behaviour and speech transcripts, and the three behaviour scripts made here.
  - The script keeps the reference's five rules in order (attention on one person, contrasts, how they feel about
    themselves, calm inside, discover you slowly) and its closing "your own charm"; each is told as a named habit with a
    practice and exact words (15 sentences). Working title "5 Quiet Habits That Make a Woman Unforgettable". 57 lines,
    1,514 words, about 10:40.
  - Changed on purpose, and told to the user: the "are you just pretty" framing, the science and nervous-system wording,
    the lines about God, the newsletter promotion and channel intro, slang. Mystery is the one rule the channel has
    taught before.
  - Sources read today for each habit are in the script's section C. Hook 70 (workable); `fit.py` no red lines; style
    rates measured against the channel's 11 behaviour scripts (the first draft was too low on "inner world" and was
    rewritten). **Waiting for the user's review; no voice or video started.**
- **Next topic from a reference channel (16 Nov 2026, `research-2026-11-16.md`):** the user approved the French winter
  package and sent The Intemporelle (`@theintemporelle`) to analyse fully, asking for ONE topic that is proven on that
  channel, not a guess.
  - The channel: 67,100 subscribers, 25 long videos since Nov 2025, usual video 75,000 views. One clear winner: "Give
    Me 10 Minutes and I'll Make You Unforgettable" (500,000; 6.7x; thumbnail "the science of charm"). It is slowing:
    first eight videos median 179,500, last eight 36,500.
  - The pick: **how to be unforgettable, told as the small habits of charming women**. Working title "7 Tiny Habits
    That Make a Woman Unforgettable" (94/100). Across YouTube: 13 charm videos at 1M+ on 11 channels; 25 of 32 big ones
    did 4x their own channel or more, on 19 channels. Neither of the user's channels has made it.
  - Told to the user: the reference video's contents could not be read (YouTube pages blocked here, vidIQ 0 credits
    until 12 Dec), so the pick copies the topic, not its points; that channel's two other charm videos did 1.1x and
    0.4x; in the 59 elegance channels the word family is usual 1.0x; the user's behaviour videos are usual 0.9x and
    win only as concrete lists. **Waiting for the user's answer; no script started.**
- **French winter package (16 Nov 2026, `videos/french-winter-eight/PACKAGE.md`, `DESCRIPTION.txt`, `TAGS.txt`):** the
  user approved the thumbnails ("ship it") and asked for the description, tags and titles.
  - Titles: 1 "The Only 8 Winter Pieces You Need (The French Way)" (recommended, with thumbnail A), 2 "8 Things Elegant
    French Women Wear All Winter", 3 "What French Women Wear All Winter (Only 8 Things)" (2 and 3 pair with thumbnail C).
  - Description: 4,869 characters in the last packages' layout (two search lines, stan.store guide link, shopmy link, 12
    chapters, hook, the eight pieces, four outfits, comment ask without "part two", signature, 3 hashtags, credits for
    113 clip accounts and 18 photo accounts, music, thumbnail line). No website, no Classy Closet.
  - Tags: 15, 374 characters. Search words taken from the most frequent phrases in the 251 topic titles with 100k+
    views (no keyword tool available).
  - Told to the user: credit names are Pinterest account names (an @name can link to an unrelated YouTube channel); the
    thumbnail line credits where photos were found and does not name the women; the description signs as Classy Academy
    while the video carries the CE logo. **Waiting for the user's review.**
- **French winter thumbnails and title (16 Nov 2026, `videos/french-winter-eight/THUMBNAIL.md`):** asked for the three
  most proven thumbnails in the exact Classy Academy format, learned from million-view videos, with the why, and a title.
  - Research: 87 YouTube searches, 1,290 long videos on the topic, 21 at 1M+ (none at 10M); 228 thumbnails tagged by
    eye in three view tiers; plus 42 over-performers against 45 under-performers from the 59 niche channels, each
    against its own channel; phrase table from all niche titles (`thumbnail-research-tags.txt`).
  - What separates winners: a claim, not a label (60% against 33%); 3 words or fewer (86% against 44%); for French
    topics a well-known real woman (56% against 6%); few collages of cut-out items (5% against 27%).
  - Title: "The Only 8 Winter Pieces You Need (The French Way)".
  - Built (`thumb_spec_ca_1080.json`, `tools/thumb_ca_real.py`, 1920x1080, CA logo): **A** "French Women / Always Wear /
    \*all winter\*" (Caroline de Maigret, Ines de la Fressange, Catherine Deneuve; recommended), **B** "All Winter / Only 8
    Pieces / \*the French way\*" (Marion Cotillard, Camille Charriere, Lea Seydoux), **C** "This Winter / Stop Buying /
    \*wear these 8 instead\*" (Caroline de Maigret, Juliette Binoche, Ines de la Fressange; the long shot).
  - Backgrounds softly blurred behind each woman (`thumb_soften.py`); the small line now matches the real thumbnails
    (`small_cap` 35, asterisks; the builder's default was 25% too small and is corrected).
  - Told to the user: no guarantee; five of the nine pins do not name the woman; press and agency photos are not
    licensed; "Always Wear" is a generalisation; B repeats the title; C is hit-or-miss; the CA logo is on the thumbnails
    while the video carries the CE logo. **Waiting for the user's review.** The files are in the session scratchpad only.
- **French winter video (15 Nov 2026, `videos/french-winter-eight/`):** the user approved script v2 ("ship it, now build
  the full video") with the same rules as the scarf video: every visual matched to its line, never guess, better music,
  no sound effects, Pinterest / Instagram / TikTok only, no clip twice, none from earlier videos, photos where no clip exists.
  - **Edit built and rendered:** 12:08, 65 lines, 117 different clips (each once; one market film gives two shots back to
    back), 14 real photos, 11 product cut-outs, 295 elements. Layouts of the channel's wardrobe videos; CE logo.
  - **Footage:** 207 search phrases in six rounds, 584 clips downloaded, screened twice on frame strips, then every chosen
    window viewed by me (`eye_notes.txt`). 0 repeats from the eleven earlier videos, 0 duplicates, 0 AI-scan flags used.
    Removed by eye as AI-made or suspect: three near-still clips from one account, an "...ai" account, a clip with a
    computer-made closet, a machine-smooth product clip.
  - **Where no true clip exists the line shows a real photo or the piece itself** (labels, linings, a V-neck over a
    turtleneck, a turtleneck under a dress, a V-neck tucked into a skirt, a back slit, matched and burgundy gloves, the
    two boot colours). The recap shows the eight cut-outs appearing as they are named.
  - **Honest limits told to the user:** 58 of the 117 clip rows are marked PARTLY in `SOURCES-LOG.md` (the dinner outfit,
    boots under trousers not jeans, wide or flared jeans in the hem shots, the belted coat by day, tights with a skirt
    above the knee, fabric gloves at the sleeve, two skirts that are not wool, two small clips shown soft).
  - **Sound:** "Classical 4" by Jonny S. (Mixkit) alone, evened, 15 dB under the voice; no ducking; no sound effects.
    It is the first track of the bed of the user's favourite build; chosen by measurement, not by ear.
  - **Rights:** nothing shown is licensed; every row is unresolved. Music cleared.
  - Files: `edit.py`, `clips.py` (slot -> clip and seconds, crops, slow limits), `eye_notes.txt`, `VISUAL-ANALYSIS.md`,
    `SOURCES-LOG.md`, `CREDITS.txt`, `CHAPTERS.txt`. Media is in the session scratchpad only.
  - **Video v1 delivered in the chat (15 Nov 2026):** 1080p, 12:08, 304 MiB send copy. QA: -12.5 LUFS, 0 black frames,
    0 silence; the only freezes are the white cards, the photo screens, the cut-out grids and the text-only lines.
    The render took 83 minutes. Waiting for the user's review.
  - **Still unanswered by the user:** which title to use; one logo for thumbnails; Studio numbers. Next after the review:
    thumbnails (1920x1080) and the upload package.
- **French winter script v2 (14 Nov 2026, `videos/french-winter-eight/script.md`; v1 kept as `script_v1.md`):** the user
  sent a nine-step brief: analyse the 30 channel scripts, check each piece for overlap, upgrade every tip, make the
  French angle credible, fact-check, rewrite, and score it honestly. Proposed title: "8 French-Inspired Winter Wardrobe
  Essentials for Effortless Elegance".
  - Overlap search of all 28 different scripts found three v1 tips the channel had already taught (puffer opening,
    sweater draped over the shoulders, jeans hem over the boot). All three are gone.
  - Final eight: long wool coat, fine turtleneck, V-neck sweater, wool blazer, dark straight-leg jeans, **wool midi skirt
    (replaces the scarf)**, tall leather boots, leather gloves; then four outfits by number.
  - Language changed to "French-inspired" and "Parisian street style"; no claim about what French women all wear. The
    "masculin-feminin" name was dropped (one source only); the Christmas tree expression is kept (two sources).
  - Fact check table in `script.md` (wool label, thin layers, shoulders and tailoring, leather and suede, glove fit).
  - 65 lines, 1,716 words (7% over the 1,600 asked for; first cuts listed in the file). Hook 74 STRONG; `fit.py` FITS;
    `dna.py` one flag ("French" said 8 times).
  - Title recommended: "The Only 8 Winter Pieces You Need (The French Way)"; the proposed title is 68 characters.
  - Scorecard given: 7 to 8.5 out of 10 per line. Waiting for the user's review; then voice and clips.
- **French winter script (14 Nov 2026, `videos/french-winter-eight/`):** the user approved the idea ("I like this topic
  ... ship it, now write the script") and asked for the exact Classy Academy script style, proven tips that are not
  basic, and said "my channel is a clone of Classy Academy".
  - Script v1 "The Only 8 Things French Women Wear All Winter": long wool coat, fine turtleneck, classic sweater, wool
    blazer, dark straight jeans, leather boots, big scarf, leather gloves; then three outfits from the eight. 74 lines,
    1,589 words.
  - Read first: five Classy Academy wardrobe scripts in full and the script of the French video that got 25,000 views.
  - Every tip from 11 pages read that day (French and Paris-based women quoted in Who What Wear, PureWow, My Chic
    Obsession); table in `script.md`, Proof. The winners' captions could not be read (YouTube block, no vidIQ credits).
  - Hook 77 STRONG (The Warning, the formula of the French hit); `fit.py` FITS; `dna.py` one flag ("French" said 16
    times; the tool expects none; the French hit scores higher on the same line).
  - No names, quotes, brands, statistics, channel name, Classy Closet or website.
  - Told to the user: the coat length differs from the winter-expensive video's advice. Waiting for the user's review;
    then voice and clips.
- **Next idea after the scarf video (14 Nov 2026, `research-2026-11-14.md`):** the user said "my videos are not getting
  views" and asked for the one proven next topic.
  - **Found: the videos made here are uploaded to The Classy Elegance** (`@TheClassyElegance`, 301 subscribers, 21 long
    videos, 19 Shorts), not to Classy Academy. Read that channel's public list first in every idea or packaging task.
  - Its usual long video has 377 views. One broke out: "7 Things Elegant French Women Never Wear", 25,000 (66x). Its
    second-fastest is "8 Ways to Look Expensive in Winter". The hairstyles (69 views) and scarf (33) videos were under
    two days old and cannot be judged yet. The scarf video went up with thumbnail D.
  - About half its thumbnails carry the CA logo and half the CE logo.
  - Classy Academy (136k): last upload 24 Oct; its videos of the last 6 months have a median of 66k against 208k before,
    while the niche is flat (44 channels, -4%).
  - The French-women wave is live on nine channels, small new ones included: French Fashion (8,750 subscribers) "The
    Only 10 Clothes You Need All Winter (The French Way, 50+)" 658k in 22 days; Graceful Aging with Ruby (5,850) 565k in
    22 days; Paris Never Ages 1.0M.
  - **Pick: "The Only 8 Things French Women Wear All Winter"** (94/100; 117 Pinterest video pins counted, not screened).
    Series after it: French never-wear in winter, French dressing rules, French women and age. The bun script stays a
    marked extra (the only topic with many 10M videos).
  - Told to the user: no topic guarantees views; no French-style video from an individual creator has reached 10M;
    test scarf thumbnails A and C against D; use one logo; send Studio numbers. Waiting for the user's choice.
- **Next idea after the hairstyles video (12 Nov 2026, `research-2026-11-12.md`):** every topic given the same search
  depth (16 topics x 8 searches) and checked for this year. Hair is the only makeable topic near the lane where many
  small creators reach 10M (37 at 10M+ from 29 channels), and it is live this year (Moni Hairstyle, 100k subscribers,
  "5 Quick Bun Styles / Perfect for Work & Busy Morning", 11.1M). **Pick: "5 Elegant Buns You Can Do in 2 Minutes"**
  (five buns not in the two-minute video). 2nd: "10 Elegant Ways to Tie a Scarf This Winter" (in-niche, seasonal).
  3rd: table manners. Base rate told to the user: 10M is 83x the channel's median; 0.1% of elegance-channel videos and
  about 1.1% of hair-channel videos reach 80x. Waiting for the user's choice.
- **Bun video script (12 Nov 2026, `videos/five-elegant-buns/`):** the user approved the idea ("ship it, now write the
  script"). Script v1 "5 Elegant Buns You Can Do in 2 Minutes": claw-clip bun, knotted bun, braided bun, half-up bun (for
  bobs), ballerina bun; none is in either earlier hair video. 59 lines, 1,257 words (about 8.5 min). Every step from a
  written tutorial read that day (`script.md`, Proof). Hook 72 STRONG; `fit.py` FITS; `dna.py` TEACHES LIKE THE CHANNEL
  (the first draft was all steps: a "what makes it so elegant" line and a payoff were added to every bun). Thin proof:
  knotted and ballerina buns have no 1M+ winner in the data. Waiting for the user's review; then voice and clips.
- **Classy Academy hairstyles script (12 Nov 2026, `videos/elegant-2-minute-hairstyles/`):** the user came back to the
  hairstyles idea ("ship it") and uploaded all the channel's scripts (`MY_CHANNEL_SCRIPT.txt`, 30 entries, 28 different).
  Script v1 "10 Easy, Elegant 2-Minute Hairstyles" written in the format of the channel's own two hair scripts: 91 lines,
  1,554 words, hook 72 STRONG. Every step read in a written tutorial (proof table in `script.md`); the winners'
  captions and comments could not be read (YouTube block, no vidIQ credits). Checkers: `fit.py` one flag, `dna.py` one (inner-world words); the
  channel's own hair scripts get the same kind of flags (both tools are tuned on wardrobe videos). Rights for whole tutorial clips to be settled before the build. Waiting for the
  user's review of the script.

- **Classy Academy hairstyles video (12 Nov 2026, `videos/elegant-2-minute-hairstyles/`):** the user approved the script
  ("ship it, now build the full video") and said the last video's music was not good and its sound effects too much.
  - Sound: no sound effects exist in any build; the music bed was changed after measuring 40 piano tracks (new: Mixkit
    "Romantic" by Francisco Alvear, 13 dB under the voice). Chosen by measurement, not by ear (`VISUAL-ANALYSIS.md`).
  - Footage: 367 Pinterest video pins downloaded in three rounds, screened on time-labelled frame strips, every pick
    verified again at large size; 61 clips used; 0 AI flags; 0 duplicates; 0 repeats from the nine earlier videos.
  - Layout: the channel's hairstyles video (replay peaks = vertical tutorial clips on caramel): a clip at the left, the step
    words stacking beside it, the tool cut out as it is named, white script cards, the CA logo.
  - Style 8 (tucked side) uses five real photos: no clean video of it on a bob was found.
  - Builder additions: `MAXSLOW` (per-clip slow motion up to 2x), `FLIP` (mirrored clip), `TRACKS_EDIT` / `MUSIC_DB` /
    `MUSIC_CREDIT` / `ENDLOGO` (set in `edit.py`).
  - Docs: `SOURCES-LOG.md` (61 clips, 16 photos, all unresolved), `CREDITS.txt`, `CHAPTERS.txt`, `edit.py`, `picks.md`.
  - Render started 12 Nov 2026 (10:47, 1080p); see the chat for the delivered file.
  - Render QA (12 Nov 2026): the first render was read every 2.5 s and every clip scanned for black frames. Four flaws
    fixed before delivery: the hook title's line spacing; a two-frame black flash at the end of the toothbrush clip
    (source); two seconds of bare wall in style 9 (the window began with the woman out of frame); a TikTok watermark in
    one style 10 window (per-window crop). A 720p preview of the first render was sent; the corrected render followed.
  - **Delivered 12 Nov 2026:** `10-Easy-Elegant-2-Minute-Hairstyles_1080p.mp4` (1920x1080, 30 fps, 10:47, 233 MiB,
    crf 18; the send limit is now 400 MiB, not 500). QA on the final render: no black frames, no silence, -13.8 LUFS,
    peak -1.8 dBFS; freezes only on cards, photos and the end card; the four fixed spots and the CE logo checked by eye;
    the clip panel scanned for black flashes across the whole video (none). The three thumbnails were also rebuilt
    natively at 1920x1080 on request (`thumb_spec_ca_1080.json`). Waiting for the user's review.
  - **Thumbnails v2 (12 Nov 2026, `THUMBNAIL.md` section A, `make_thumbs_v2.py`):** the user called v1 "still basic".
    Added research: the 262 winners against 84 low-view hair videos from the same searches, hits against the same
    channel's usual videos (13 channels), brightness measured. What separates winners: a step beside the result (19%
    against 1%), hair from behind, brightness 147 against 126, fewer words; v1 measured 85-98. Three new thumbnails at
    1920x1080: A three steps of the claw-clip French twist + a "2 MIN" badge (lead), B a set of four results + band
    "10 Easy, Elegant HAIRSTYLES", C one large twist with a gold clip + "1 CLIP. 2 MIN." (a Princess Polly product
    photo, not in the video). Waiting for the user's choice.
  - **Upload package (12 Nov 2026):** `PACKAGE.md` (title kept: "10 Easy, Elegant 2-Minute Hairstyles", 100/100),
    `DESCRIPTION.txt` (3,514 chars: guide + shop links, 13 chapters, credits, thumbnail A's credit), `TAGS.txt` (15).
    Signed as Classy Academy; the video carries the CE logo, so the user must say which channel it goes to.
  - **The user then asked for the Classy Elegance logo on this video, not the Classy Academy logo** (corner logo and end
    card swapped to `logo_ce.png` / `logo_ce_dark.png`), and to keep the current voice (a directed-pacing voice test,
    `B_directed.mp3`, was offered and declined).
  - **Title and Classy Academy thumbnails (12 Nov 2026, `THUMBNAIL.md`):** 294 hair videos with 1M+ views found (70
    searches); 262 thumbnails read and tagged; 243 scored against their own channel. Findings: the hair seen from behind
    or the side (295x against 62x), a step beside the result (454x) and a time promise in the title (14% of the 1M+
    titles against 6% under 100k) mark the winners; creators' faces and warnings sit at the bottom. Title kept: "10 Easy,
    Elegant 2-Minute Hairstyles". Three thumbnails in the channel's layout, built from frames of the video's own clips:
    1 "Elegant Hair / In 2 Minutes", 2 "2-Minute / Elegant Hairstyles" (the channel's own 967k thumbnail plus the new
    promise), 3 "Elegant Hair / Easier Than It Looks" (one French twist in three steps). The thumbnails carry the CA
    logo and the video the CE logo, both as asked; the user decides which channel it goes to.

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
