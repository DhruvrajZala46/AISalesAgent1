# "8 Things That Make You Look Older: What to Wear Instead": title, thumbnail, description, tags (22 Oct 2026)

**Built with:** the `yt-package` and `yt-seo` skills, on the channel's own data. The video and script are unchanged.

**Copy-ready files in this folder:**
- `DESCRIPTION.txt` (1,869 characters);
- `PINNED-COMMENT.txt` (7,542 characters, every creator credited, under YouTube's 10,000-character comment limit);
- `TAGS.txt`.

**Thumbnails:** sent in the chat. They are media and not in git; how to rebuild them is in `edit/thumbnail_specs.json`.

## 1. What works for THIS channel (@ClassyAcademy, read 22 Oct 2026)

**The data:**
- **Uploads:** 30 public long videos, 135k subscribers.
- **Median views:** 129k all-time. The ten newest (Jun–Sep 2026) sit at 31k–75k, 0.2–0.6× that median.
- **Fastest current pace:** "6 Old Money Wardrobe Essentials" at 2,379 views a day (29 days old).

**Sources:**
- public channel listing (views, durations);
- upload dates from the 19 Oct downloads;
- the 30 thumbnails;
- descriptions and tags;
- YouTube search autocomplete (US, UK, Germany).

**Studio analytics:** these could not be accessed: impressions, CTR, audience countries, when viewers are online. The US/UK/Germany audience is not verified here.

| What wins on your channel | Evidence |
|---|---|
| "Elegant" in the title | in all 6 of your videos above 3× the median: 1.25M, 951k, 698k, 637k, 498k, 388k |
| The list + "What to Wear Instead" shape | 1.25M "8 Things Elegant Ladies Never Wear: What to Wear Instead" (9.3×). The same suffix also got 149k (1.2×) and 31k ("8 Outfit Mistakes That Cheapen Your Look (What to Wear Instead)", 0.2×), so the suffix alone does not carry a video: the front of the title does. |
| "Instantly" | in 3 of your top 8 titles (698k, 334k, 316k) |
| One thumbnail template on all 30 | 3 women; small serif top line; huge bold keyword; small *qualifier*. The 1.25M adds a dark-red rule under its negative word ("Never"). |
| Descriptions | short (median about 450 characters): a hook line, "⚜️Access the Personal Stylist Guide here:" and the link, sometimes a paragraph, then #classy #elegance #elegant. Your 1.25M has no chapters, credits or hashtags. |
| Upload time | your top 3 went up at 00:06–01:43 UTC: 7–10 pm US Eastern, 1–3 am UK, 2–4 am Germany. Recent uploads go up Thursday/Friday at about 23:00–00:00 UTC. |

**What the niche shows for this exact concept** (`research-2026-10-21-proven-concept.md`):
- **Wording:** "make you look older" is the shared wording of 13 independent 1M+ clothing videos.
- **Thumbnail text:** about 22 of 25 winners put the age verdict ("LOOK OLDER") in the biggest text on the thumbnail.
- **Autocomplete:** "things that make you look older" is YouTube's own top suggestion for the phrase in the US, UK and Germany. Related suggestions are:
  - "clothes that make you look older";
  - "style mistakes that make you look older";
  - "what makes you look older than your age";
  - "how to not look older than your age";
  - "what to wear to look younger".
- **"Instantly", in 233 attempts from the last 13 months:**
  - with "instantly": median 1.92× their channel, 41 % beat 3× (49 videos);
  - without: 1.24×, 24 % (184 videos).
  - This is a correlation, not proof.

## 2. Title

**Recommended:** **8 Things That Make You Look Older: What to Wear Instead**
- 55 characters, so desktop shows it in full. A phone shows "8 Things That Make You Look Older: What…", so the subject survives the cut.
- `title.py` 94/100.
- `fit.py` places it with your 1.25M.
- It joins the niche's proven phrase to your #1 video's shape. It is also the exact top autocomplete phrase.

**Runner-ups,** for YouTube's Test & compare if your Studio offers title tests:

| Title | Chars | Score | Why | Watch out |
|---|---:|---:|---|---|
| 8 Things That Instantly Make You Look Older | 43 | 94 | "Instantly" (your top 8, and the niche's recent data); MM Personal Styling 1.53M uses "That Instantly Make You Look Older" | loses the fix ("what to wear instead"); a narrow phone feed cuts it before "Older" |
| 8 Things That Make You Look Older Than You Are | 46 | 94 | the script's own words; autocomplete "…older than your age"; Diana GOSS 1.35M "…Than You Are" | no fix in the title, so the thumbnail must carry the promise |

**Also scored, not recommended:**
- "8 Things That Make You Look Older (What Elegant Women Wear Instead)": 67 characters, 76/100. It adds your proven word "Elegant", but desktop cuts the tail.
- "8 Style Mistakes That Make You Look Older: What to Wear Instead": 63 characters, 76/100.
- "Elegant Women Never Wear These 8 Things That Make You Look Older": 64 characters, 76/100. It also echoes your 1.25M too closely.
- "Stop Wearing These 8 Things If You Don't Want to Look Older": 59 characters, 94/100. Its scolding tone is not your voice.
- "How to Not Look Older: 8 Things to Stop Wearing": 47 characters, 94/100.
- "8 Things Elegant Women Avoid (They Make You Look Older)": 55 characters, 94/100. A good fallback if you want "Elegant" in the title.

The full list is in `edit/titles.txt`.

**`title.py` warning:** it flags that the thumbnail repeats "Look Older". This is deliberate: every one of your winners restates the title's keyword ("Never Wear", "Expensive", "Elegant Hairstyles"), and your own template wins over the generic rule (`workflow/4-THUMBNAIL.md`).

## 3. Thumbnails (your template, exactly: `workflow/tools/thumb_ce.py`)

**Superseded (22 Oct 2026):** the current thumbnails are the v3 set in `THUMBNAIL-PHOTOS.md`, with the same template and cleared Unsplash/Pexels photos. This section records v1.

| | Top line | Headline | Small line | Photos | Purpose |
|---|---|---|---|---|---|
| **A (recommended)** | Things That Make You | **Look Older** (dark-red rule under "Older") | \*avoid these\* | Set 1 | your 1.25M thumbnail's exact shape and wording style, plus the niche's proven words |
| B | Why You Look | **Older** (rule under "Older") | \*it's not your face\* | Set 1 | copy test: the hook's own twist ("it isn't your face at all") |
| C | Things That Make You | **Look Older** | \*avoid these\* | Set 2 | photo test: visibly mature women. Test variant only, never the main thumbnail (LEARNINGS: the older-women-only "at any age" thumbnail got 3.0 % CTR on Put Together) |

**Logo versions:** each is built twice, `_CE` (The Classy Elegance logo, as in the delivered video) and `_CA` (the Classy Academy monogram from your channel's thumbnails). Use the one that matches the channel you upload to.

**Feed test** (`feed_test.jpg`, sent): at 320×180, next to your 1.25M, 951k and 698k and the niche's 1.53M, 1.35M and 1.25M:
- "Look Older" reads in one glance;
- all faces stay clear;
- the three thumbnails read as the same family as your winners.

**Photos:** every one is a real photo from the creator's or photographer's own Instagram post. The author and the exact slide were confirmed by Instagram's embed (`igcheck.js`, slide screenshots, and a perceptual-hash match of 3 bits or fewer out of 256).

| Set | Panel | Creator | Post | Photo |
|---|---|---|---|---|
| 1 | left | @e.linkaa (photographer; model @melnikovakristina) | https://www.instagram.com/p/DA_5-H1usxa/ (slide 2) | profile, sleek braided ponytail, gold drop earring, black |
| 1 | centre | @jastookes | https://www.instagram.com/p/Cw-fA_WrHnK/ (slide 3) | sleek bun, gold earrings, black blazer, eyes down, rain, umbrella |
| 1 | right | @signebaekgaard | https://www.instagram.com/p/DLwxoQXNXTr/ (slide 1) | white blazer, sleek ponytail, gold rings, stone wall |
| 2 | left | @thetennillelife_ | https://www.instagram.com/p/C5yo_JoIPHx/ (slide 1) | salt-and-pepper updo, black blazer, gold hoops, Paris |
| 2 | centre | @jandevilleneuve (photo: Sybille Walter for ENCENS magazine) | https://www.instagram.com/p/CeqtjE5MAQ-/ | camel trench |
| 2 | right | @mayemusk | https://www.instagram.com/p/CCYwp3ypI0f/ | ivory dress, gold buckle and earrings |

Backups:
- Set 1: @avahadams_ https://www.instagram.com/p/Ddj7W6HEviD/, @constanza.tognarelli https://www.instagram.com/p/DAec9nrSsYW/;
- Set 2: @greceghanem https://www.instagram.com/p/CN79xZgFxxM/ and https://www.instagram.com/p/BaX2asFh_bP/.

**Permission:** none of these photos is licensed and no one has been asked. That is the same status as your existing thumbnails' photos. Nothing is sent without your OK.

## 4. Description, chapters, hashtags, pinned comment

`DESCRIPTION.txt` follows your channel's layout:
1. two search lines;
2. the guide link;
3. chapters;
4. two short paragraphs in the video's own words;
5. the comment question;
6. your three hashtags (#elegance #classy #elegant);
7. a credits note.

**Replace `[YOUR GUIDE LINK]`:**
- On Classy Academy it is the link your descriptions already use (https://classyladyacademy.com).
- On The Classy Elegance, use that channel's guide link. On 19 Oct you said not to use classyladyacademy.com there.

**Spelling:** US spelling ("color"), as in your titles and in US search.

**Chapters,** from the final video's timing:
- the point cards;
- the hook at 00:00;
- the close at 08:12.

They pass YouTube's rules: the first is at 00:00, there are 10, and the shortest is 41 s.

**Pinned comment:** the question, then every creator in order of appearance:
- Instagram authors confirmed by Instagram's embed, with post links;
- Pinterest uploaders, with pin links;
- the film, press and product credits;
- the music.

## 5. Tags (15, 378 characters): `TAGS.txt`

Exact search phrases from YouTube's autocomplete, plus your channel's own recurring tags (elegant style tips, classy style, old money style). Tags are a weak signal; the title and the first two description lines do the work.

## 6. The searches this video should win

| Search (YouTube autocomplete, US/UK/DE) | Where it appears |
|---|---|
| things that make you look older | title, exact |
| clothes / style mistakes that make you look older | description line 1: "The clothes and style details that make you look older" |
| what makes you look older than your age | description line 1: "make you look older than you are" |
| what to wear to look younger | title "What to Wear…" + description line 2 "look younger" |

## 7. Test plan

**Thumbnails:** run YouTube's **Test & compare** with A, B and C from the moment of upload. YouTube picks the winner by watch time share, usually within about 2 weeks.

**Titles:** if your Studio offers title testing, test the recommended title against the "Instantly" runner-up.

**Do not change the title in the first 48 hours** unless a test says so.

**Upload time:** the same slot as your top 3, about 7–9 pm US Eastern (00:00–02:00 UTC). This could not be checked against your viewers' online times, because Studio analytics are not accessible here.

**Ship it, or change it?**
