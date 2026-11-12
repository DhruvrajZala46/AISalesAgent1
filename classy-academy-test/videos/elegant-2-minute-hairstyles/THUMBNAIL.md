# 10 Easy, Elegant 2-Minute Hairstyles - title and three Classy Academy thumbnails (12 Nov 2026)

Built with `workflow/tools/thumb_ca_real.py` (the channel's measured layout and the real CA logo), `thumb_spec_ca.json`
and `make_thumb_frames.py`. Skills used: `yt-viral` (each winner against its own channel), `yt-package` (title lint,
title and thumbnail as one unit), `thumbnail-design` (one promise, phone-size test, three concepts for Test & compare).

No thumbnail can guarantee views. What follows is what the numbers show and what was built from them.

## 1. What was collected (YouTube public listings, 12 Nov 2026)

- 54 new searches (49 returned results; 5 failed twice and were left out: "timeless hairstyles for women", "kate
  middleton hairstyle tutorial", "hair hacks every girl should know", "donut bun tutorial", "easy hairstyles for thin
  fine hair"), added to the 16 hair searches of 11 Nov.
- 1,580 hair videos; 1,361 of them 2 minutes or longer.
- **294 have 1M+ views** (94 have 5M+, 46 have 10M+). 32 were off the lane (men's cuts, children, a music video).
- **All 262 remaining thumbnails were downloaded, read one by one and tagged** (`thumbnail-research-tags.txt`).
- The latest videos of 151 of their channels were listed (14,773 videos) to score 243 winners against their own
  channel's median.
- All 31 Classy Academy thumbnails were read again, with views.

**Limits:**
- Only winners' thumbnails were read. The thumbnails of the videos that stayed small were not.
- A channel's median comes from its latest videos; many of these hits are years old, so the multiples are inflated.
  They rank the formulas against each other; they are not forecasts.
- The tags are one reading by eye.
- vidIQ's scorer was not used (no credits).

## 2. What separates the hair videos that went big from the ones that did not

### 2a. The picture (262 thumbnails with 1M+)

| What the thumbnail is | 1M+ (262) | 10M+ (43) | Median multiple over own channel |
|---|---|---|---|
| A step beside the result, or before / after | 51 | 8 | **454x** |
| One finished style, one photo | 33 | 7 | **400x** |
| Hack or wrong / right marks (content farms) | 19 | 6 | 252x |
| 2 to 4 different finished styles in a row | 42 | 6 | 144x |
| One finished style from 2 or 3 angles | 37 | 4 | 74x |
| A grid of 5 or more styles | 51 | 10 | 70x |
| The creator's own face is the picture | 29 | 2 | **16x** |

| Trait | With it | Without it |
|---|---|---|
| The hair is seen from behind or the side (144 of 262; 25 of the 43 at 10M+) | **295x** | 62x |
| A face looking at the camera (59) | 64x | 193x |
| Any words on the thumbnail (122) | 83x | **279x** |
| A time promise in the words: "2 MINUTE BUN", "60 SECOND" (13) | 193x | 147x |
| A warning: "never", "stop" (7, almost all one large channel) | 13x | 164x |

### 2b. The title (all 1,361 long hair videos: 294 with 1M+ against 658 under 100k)

| In the title | 1M+ | Under 100k |
|---|---|---|
| **A time promise** (2 minutes, 60 seconds) | **14%** | 6% |
| Easy / simple / quick | 48% | 40% |
| Bun / updo / twist / chignon | 34% | 25% |
| A number | 47% | 53% |
| Elegant / classy / chic | 6% | 16% |
| Old money / quiet luxury | 0% | 13% |

- The time promise is the only title trait more than twice as common among the winners.
- "Elegant" and "old money" are more common among the small videos. Part of that is age: those are newer videos and
  newer search terms. It still says the elegance word alone does not carry a hair video; time and ease do.
- Video length does not separate them (median 6.3 against 6.2 minutes).

### 2c. Why a woman clicks a hair thumbnail (what the counts point to)

1. **She sees the result before she clicks.** The finished hair is the proof; she decides "I want that" in under a
   second. That is why the picture matters more than the words (279x without words against 83x with).
2. **From behind, it could be her.** A head seen from the back has no face, so any viewer puts herself in it. A
   creator's face makes it about the creator: the lowest multiple of all (16x).
3. **The cost looks small.** "2 minutes", "60 seconds", "easy" answer the two objections: no time, no skill.
4. **A step beside the result shows the gap is short.** It raises "how?" and answers "I could do that" at once: the
   highest multiple (454x).
5. **She clicks on wanting, not on fear.** Warnings work on "never wear" videos; on hair they sit at the bottom.
6. **For this channel's viewer, it must also look like her world:** black, white and cream, gold jewellery, a clean
   neck and shoulder line.

## 3. Classy Academy's own proof

- 31 videos, median 121k.
- **"The Most Elegant & Easy Hairstyles: For All Hair Types": 967k, 8.0x the median, the channel's second biggest
  video.** Its thumbnail: THE MOST / **Elegant Hairstyles** / ALL HAIR TYPES; two of the three panels show an updo
  from the side or behind, above the words.
- "The Most Elegant Haircuts for Every Hair Type": 245k. Three faces to the camera, no new promise.
- The channel's thumbnails repeat the title's main words (1.2M: "Elegant Ladies / Never Wear"). `yt-package` asks
  for different words on the thumbnail; this channel's own winners say otherwise, so two of the three follow the
  channel and one follows the rule.

## 4. The title

**10 Easy, Elegant 2-Minute Hairstyles** (36 characters; `title.py` 100/100; survives the mobile cut whole).

- It carries all three traits the winners share: a time promise, "easy", a number.
- "Elegant" stays for the channel's own viewers, in second place.
- Ten candidates were linted; the longer ones lose "(No Heat)" or "For All Hair Types" on a phone.

## 5. The three thumbnails (1280x720, the channel's layout, the real CA logo)

| | Words | Pictures | What it copies, and why |
|---|---|---|---|
| **1. In 2 Minutes** | Elegant Hair / **In 2 Minutes** / 10 easy styles | three finished styles from behind: a low twisted chignon with a gold necklace, a French pin bun, a French twist | the time promise as the headline ("2 MINUTE BUN" 14.2M twice, "My 5 Minute Ponytail!" 27.8M, "60 Second" 5.7M and 3.9M) on the "different finished styles in a row" picture (Luxy Hair 20.8M) |
| **2. Elegant Hairstyles** | 2-Minute / **Elegant Hairstyles** / \*no heat\* | a sleek rolled chignon with gold earrings, a sleek wrapped ponytail, a sleek low bun | the channel's own 967k thumbnail, word for word in the headline, with the one new promise (2-Minute) on top |
| **3. Easier Than It Looks** | Elegant Hair / **Easier Than It Looks** / \*2 minutes\* | one French twist in three steps: hair in the hand, the twist, the finished style | the step-beside-result picture (highest multiple, 454x) with the reassurance line of three winners ("Easier Than It Looks Updo" 14.6M, 4.5M, 3.7M); the only one whose words do not repeat the title (`title.py` 98/100) |

- **What changed from the channel's layout:** the words sit 54 px lower (headline top at y 350, not 296), so every
  hairstyle sits clear above them. Heads fill the top third; necks and shoulders carry the words.
- **Every picture is a frame from a clip that is in the video** (table below). The thumbnail shows what the viewer
  will see, and none is AI.
- **Why not Pinterest photos:** 29 were shortlisted. Most polished "low bun" pins were AI images from listicle sites
  (AI file sizes, no real source); they were dropped. The real ones were head-and-shoulder close-ups, so in this
  layout the words would have covered the hair.
- **One retouch:** the lettering on a framed wall sign behind the French twist was painted out (wall only).
- **Checks:** read at phone size (168x94) beside nine hair thumbnails with 2M to 28M views; beside the channel's own
  top five; in black and white. Sharpness: 1.11 to 1.59 source pixels per output pixel, nothing enlarged.
- **Which one:** this is a design call until YouTube has click data.
  - **1** follows the hair numbers most closely (time promise, results from behind).
  - **2** is the safest for the channel's own viewers (their 967k, repeated).
  - **3** is the boldest (the formula with the highest multiple; no title words repeated).
  - Upload all three to **Test & compare**; it picks by watch time, not clicks alone.

## 6. Pictures

| Thumb | Panel | Clip (second) | Creator, as logged in `SOURCES-LOG.md` |
|---|---|---|---|
| 1 | left | cv_dinner13 (29.8) | MetDaan Beauty (@metdaanbeauty1) |
| 1 | centre | s10b30 (0.0 to 1.4) | Beauty Hooked (@Beauty_Hooked) |
| 1 | right | hv_twist13 (20.0) | Easy Hair Tutorial (@easyhairtutorials) |
| 2 | left | hv_chignon38 (19.6) | Ana Benković (@anabenkovic010) |
| 2 | centre | s2b23 (16.2) | Hair Rehab London (@hairrehablondon) |
| 2 | right | cv_dinner43 (0.0) | Stylish Mom (@stylish_mom_28) |
| 3 | all three | hv_twist13 (2.6, 10.0, 18.0) | Easy Hair Tutorial (@easyhairtutorials) |

**Rights:** these are frames of creators' reels; none is licensed. The creator decides.

**Logo:** these thumbnails carry the Classy Academy logo, as asked. The rendered video carries the Classy Elegance
logo, as asked on the same day. Whichever channel it is uploaded to, one of the two needs changing.

**1920x1080 versions (asked for the same day):** `thumb_spec_ca_1080.json` rebuilds all three natively at 1080p
(`"scale": 1.5` in the spec; the builder now multiplies every measure). Words and logo are drawn at full size; the logo
is a sharp copy taken from the channel's public avatar (`"logo"` in the spec). The pictures are 720p video frames, so at
1080p they sit at 0.74 to 1.06 source pixels per output pixel: slightly enlarged, most in thumbnail 2's right panel.
The 1280x720 build is unchanged pixel for pixel.

**Files:** `CA-Hairstyles_Thumbnail1/2/3` (.jpg and .png), two previews, and
`CA-Hairstyles-thumbnails_editable-source.zip` (six layers per thumbnail, the spec, the nine frames, the frame script).
Rebuild: `python3 make_thumb_frames.py` in the video's work folder, then
`python3 workflow/tools/thumb_ca_real.py thumb_spec_ca.json`. The builder gained `logo_dark` (a soft dark patch behind
the logo when it lands on blonde hair or a white wall); earlier thumbnails rebuild unchanged.
