# Thumbnail: "8 Ways to Make Your Clothes Look New Again (Without Buying More)"

The title and script were checked on 26 Oct 2026: `script.md` v2 is the latest approved script. This file replaces round 1 (the ✗/✓ "Don't Toss It" set), which is still in git history and in the scratchpad `thumb/`.

**Final:** `old-clothes-new_thumbnail_final.jpg`, 1280x720, JPEG RGB, quality 95. The media is not in git (repo rule); it is in the scratchpad `old-clothes-new/thumbnail/` and was sent in chat.
**Editable source:** `thumbnail/ca_thumb.py` plus `thumbnail/spec_*.json`. Run `python3 ca_thumb.py spec_FINAL_restore_it.json` inside a folder whose `real/` holds the photos.

## 1. Thumbnail DNA report: all 31 long videos on youtube.com/@ClassyAcademy

**Method.**
- Every `maxresdefault` thumbnail was downloaded with yt-dlp on 26 Oct 2026 and looked at by eye (`thumb2/ca_sheet_a.jpg`, `ca_sheet_b.jpg`).
- The view counts are public figures. The channel median is 119k views.
- No CTR or impression data was available (vidIQ needs re-authorising, and YouTube Studio is not reachable from here). So "strong" below means views, which also depend on impressions, age and topic. It does **not** mean CTR.

**Constant on 31 of 31 thumbnails (the brand rules):**

| Element | What the thumbnails show |
|---|---|
| Layout | **Three tall photo panels edge to edge**, with thin light dividers. No exceptions: no single-image, split-screen, ✗/✓ or before/after thumbnails |
| Subjects | Polished women, waist-up or seated, faces in the top third, mostly looking away or past the camera; café tables, gold jewellery, sunglasses, coffee or wine. Mixed ages and skin tones (Princess of Wales on 5). Detail panels without a face are allowed: the jewellery thumbnail (#12) and the shoes thumbnail (#23) |
| Palette | Warm neutrals: black, cream, camel, chocolate. Slightly dark, gentle contrast, a soft dark vignette behind the words |
| Top line | Small caps serif (Cormorant SC), white, 1-3 words ("How to Look", "Elegant Ladies", "Become") |
| Headline | Bold geometric sans in **Title Case** (not capitals), white, 1-3 words, soft shadow, centred across all three panels |
| Small line | Small caps serif in asterisks: `*avoid these*`, `*instantly*`, `*any budget*`. Present on about two thirds |
| Red underline | Under the first headline word on the **"Never ..."** thumbnails only (#6, #15, #22, #26) |
| Logo | "CA" monogram, top-left |
| Title vs thumbnail | The thumbnail carries the promise in 2-4 words and the title gives the specifics ("Expensive" with the title "How to Instantly Look More Elegant & Expensive...") |

**What varies:** the headline words, and whether one panel is an object. Nothing else.

**Strongest references** (views as a multiple of the channel median):

| Video | Views | Multiple | Thumbnail |
|---|---|---|---|
| My7qteRU9k0, Never Wear | 1.2M | 10.1x | Elegant Ladies / **Never Wear** (underlined) / \*avoid these\* |
| A-JRkjQs2XI, Hairstyles | 957k | 8.0x | The Most / **Elegant Hairstyles** / \*all hair types\* |
| QOEUbAZB07o, Look Expensive | 705k | 5.9x | How to Look / **Expensive** / \*instantly\* |
| q78t2KbuePk, Dress Elegant | 640k | 5.4x | How To / **Dress Elegant** |
| oHh4T67jJNM, Never Do in Public | 502k | 4.2x | Elegant Ladies / **Never Do In Public** (underlined) / \*Avoid These\* |

**Correction to round 1.** My first set used capital headlines and ✗/✓ badges on caramel. The channel never does either. The DNA layout (`tools/thumb_make.py`) was right. The new final follows it exactly.

## 2. Concept comparison

**Topic research** (40 topic videos, each scored by views ÷ its own channel's median; `thumb/winners.jpg`):
- Same garment before ✗ → after ✓: 330x (a small channel).
- Three elegant women + one line: 341x (Classy Woman).
- One older woman: 241x.
- A steamer in hand: Melissa Maker, 91x.

These are view multiples, not CTR.

| | C1: Polished trio | **C2: The care ritual (chosen)** | C3: Tired → restored |
|---|---|---|---|
| Visual idea | Three women in fresh classics | Two polished women + **a white shirt being steamed** (the restoring act) | One woman holding her faded jeans ✗, then the same jeans black ✓ |
| Subject and placement | Three faces, top third | Women left and centre (faces above the words); the steamer, steam and hand on the right, clear of the words | Two cut-outs at the edges, words in the middle |
| Composition / background | Pure DNA | DNA plus one detail panel (as on #12 and #23) | Caramel backdrop, cut-outs, badges |
| Colour / contrast | Cream on cream, low contrast | Camel / cream / white, with the dark steamer as the accent | Red hair and black denim on caramel: the most contrast |
| Text | Elegant Ladies / **Never Rebuy** / \*they do this instead\* | Don't Replace It / **Restore It** / \*8 elegant ways\* | Don't / **Toss It** / \*bring it back\* |
| Channel fit | Highest | High (one product panel, within the DNA) | **Low**: the channel has never used ✗/✓ or cut-outs |
| Why it could earn the click | Copies the 10.1x "Elegant Ladies Never..." formula | Shows *how* (care, not shopping) and makes "how do I restore mine?" the curiosity | The clearest transformation |
| Weak at small size | Says nothing about clothing care, a generic look; "Rebuy" is an awkward word | The steam is faint (the steamer still reads at 168 px); the centre face is a video frame, a little softer than the stills | Busy; looks like another channel |

**Selection: C2.**
- It keeps all eleven brand rules.
- It is the only concept whose picture states the promise (restoring with care, not buying).
- The words are honest to the script ("None of this needs a new wardrobe"; card 1 even says when to let go, which "Restore It" doesn't contradict).
- `title.py` confirms the thumbnail words don't repeat the title.

C1 is the A/B alternative for YouTube's Test & compare. C3 is kept only as a reference.

**Fix made while designing:**
- The first C2 put the steamed shirt in the centre panel. At phone size the words covered it.
- In the final, the shirt and steamer moved to the right panel, mirrored so the steamer, steam and hand sit right of the headline.
- The headline weight was raised to Bold 700 to match the channel.

## 3. Final audit (the exported file, inspected)

- 1280x720, 16:9, JPEG, RGB, quality 95. Within YouTube's limits (under 2 MB).
- **Spelling.** "Don't Replace It / Restore It / \*8 elegant ways\*" is correct, and "8" matches the video's eight points.
- **Edges and artefacts.** Zoomed to 2x at the dividers, the face and the steamer (`thumb2/final_zoom.jpg`): no watermarks, no captions, no stray borders.
- **Mobile test.** `thumb2/final_mobile.jpg` sets it at 168 px and 246 px wide beside the channel's five strongest thumbnails. "Restore It" reads at once, the camel-coat face and the dark steamer are visible, and it sits in the same family.
- **Brand.** Three panels, the type system, the warm palette, the vignette, the logo top-left. The underline is off, as on the channel's non-"Never" thumbnails.
- **Honesty.** It shows steaming, which the video teaches (point 3). There is no fake transformation and no luxury logo.
- **Logo: unresolved.** It carries this repo's **CE** logo. This repo's channel is "The Classy Elegance", and earlier the user described @ClassyAcademy as a competitor. Not reproducing the CA monogram is deliberate. If the video is going to the Classy Academy channel, replace `assets/logo_ce.png` with the owner's CA logo file and re-run the spec.
- **CTR.** Not predicted. Test it: upload the final (C2) and C1 to YouTube Studio's Test & compare, and read watch-time share after about 2 weeks or once enough impressions build up.

## 4. Asset ledger

| Panel | Asset | Creator / owner | Where found | Original | Rights status |
|---|---|---|---|---|---|
| Left | Frame 2.0 s of the camel wool coat reel (clip `airing20`, also in the video) | Norwegian Wool (@norwegianwool), brand | Pinterest video pin | instagram.com/reel/DDLAL6oxqNI | **Unresolved**: brand content, no licence |
| Centre | Frame 6.8 s of the cream knit reel (clip `sweaterwoman30`, also in the video) | pinned by @craftinaroundbunches; the original is a TikTok creator, not yet traced | Pinterest video pin | TikTok (watermark in the source clip, not in this frame) | **Unresolved**: trace the creator first |
| Right | Photo of a white shirt steamed on a hanger, mirrored and cropped | Eleonora Carla Torre (@eleonorstorre); a sponsored post (#adv, @steamone_official) | Pinterest pin of `i.pinimg.com/originals/84/36/ab/8436ab48ac446c9a50496f4089a9f2e5.jpg` (3277x4096) | instagram.com/p/DYgwCZICPMR | **Unresolved**: ask her permission |
| Fonts | Montserrat, Cormorant SC | Google Fonts | repo `workflow/assets/fonts` | | SIL OFL: cleared |
| Logo | CE monogram | the channel | repo `workflow/assets/logo_ce.png` | | own |

**AI and quality check.**
- The two video frames come from clips that passed `aiscan.py` (0.00).
- The steamer photo is a 3277x4096 original from a named creator's sponsored post. Real hands, rings, fabric weave and steam all look genuine.
- Rejected:
  - Pinterest "elegant woman café / black blazer" photos: many are AI. One carried the Gemini sparkle and one a "ChatGPT" mark.
  - The PROPRESS photo (a brand page).
  - A CHANEL-bag shirt photo (luxury logo).

**Description credit:** `Thumbnail: @norwegianwool · @eleonorstorre · (centre: TikTok creator, to be credited once traced)`

**Before publishing:** all three images are Pinterest finds with credit only. Under this repo's rules that is *unresolved*, not cleared. Ask @eleonorstorre and @norwegianwool for permission (template: `workflow/ASSET-RESEARCH-GUIDE.md` §5), or swap in owned or licensed photos using the same spec.


# Round 3: the topic's proven thumbnails (research on every 1M+ video found)

**Method.**
- 42 YouTube searches a viewer types, 50 results each: 2,000 results, which is 1,176 unique long videos (yt-dlp, 26 Oct 2026). The searches cover making old clothes look new, clothing care, laundry, pilling, faded black, shrunk or stretched knits, steaming and ironing, whites, alterations, look expensive, dressing better without buying, and Diana.
- 158 of them have 1M+ views. Kids', craft-hack-farm (5-Minute Crafts, 123 GO, Blossom), prank, men's-tailoring and off-topic videos were dropped, leaving **51 relevant 1M+ videos**.
- Each one's views were divided by the median of its own channel's last 80 videos. That multiple measures how far the video beat what its channel normally gets. It is a view multiple, **not CTR**: no tool here can see other channels' CTR.
- Every thumbnail was looked at and tagged by hand (`thumb3/rel_0-2.jpg`).

| What the thumbnail shows | n | Median multiple | Others |
|---|---|---|---|
| **The garment is the subject** (no face needed) | 16 | **212.9x** | 20.6x |
| Red ✗ / green ✓ drawn on | 5 | 143.3x | 40.5x |
| Same garment or person, **before \| after side by side** | 14 | 51.7x | 33.8x |
| No text at all | 15 | 121.3x | 26.5x |
| **The creator's face** as the hook | 17 | **7.2x** | 104.7x |

The **care / restore** videos alone (n=21) show the same thing: garment-first 212.9x against 88.3x; creator face 54.5x against 206.9x.

**The winners copied:**

| Video | Views | Multiple | Pattern |
|---|---|---|---|
| Smart Fox, "White Laundry REALLY WHITE again" | 1.60M | 371x | grey tee → white tee, arrow, no words |
| Miarti, "fix a stretched sweater band" | 1.29M | 219x | stretched cuff ✗ → fixed cuff ✓, no words |
| JairWoo, "RE-DYE FADED BLACK JEANS" | 1.95M | 197x | faded jeans \| black jeans |
| Jordan O'Brien, "Stretch Your Small Clothes" | 1.33M | 121x | the same sweater, "TIGHT → LOOSE" |
| Ramya Vasudev, "Faded Jeans Black Again" | 1.70M | 77x | faded \| black jeans, "BEFORE → AFTER" |
| Trefa Craft, "expand the sweater by 20cm" | 1.81M | 75x | the same sweater, arrow, "+20cm" |
| Star News Today, *our exact title*, Diana | 2.37M | 56x | the same dress twice, yellow circles |

**The proven recipe:** one garment, the same piece twice (before | after), an arrow or ✗/✓, and at most two words.

## The thumbnails built from it (real footage, the channel's type and logo)

1. **PROVEN T1 (recommended): `old-clothes-new_thumbnail_PROVEN_faded_black.jpg`, "Faded → Black".**
   - Christie Moeller (@icanstyleu) holds the **same jeans** by the waistband twice in her own reel: faded at 7.0 s, restored at 28.3 s.
   - It copies JairWoo (197x), Ramya (77x) and Jordan O'Brien's word-arrow-word (121x).
   - Our video teaches it: point 5, "a fabric dye can restore it".
   - Look: Montserrat Bold Title Case, the red underline, the CE logo, a gentle warm grade.
   - At phone size it reads in one glance (`thumb3/feed3.jpg`, next to the winners).
2. **PROVEN T2: `T2_pilled_smooth.jpg`, "Pilled → Smooth" with ✗/✓.**
   - The same black knit before and after a fabric shaver (clip `shaver41`), following Miarti 219x.
   - Weaker at phone size: both halves are dark knit, so the words carry the difference.
3. **Channel-DNA final (round 2): "Don't Replace It / Restore It".** This is the brand-safe option.

**Test & compare: T1 + T2 + the round-2 final.** Then let YouTube's watch-time result decide.

Nothing guarantees CTR. These patterns are the ones whose videos most outperformed their own channels on this topic.

**Rights:**
- T1 uses @icanstyleu's frames.
- T2 uses an Amazon influencer post re-pinned on Pinterest; the original creator is not traced.

Both are **unresolved** under `SOURCES-LOG-TEMPLATE.md`. Ask @icanstyleu for permission before publishing T1 (template: `workflow/ASSET-RESEARCH-GUIDE.md` §5).

**Editable source:** `thumbnail/thumb_ba.py` plus `spec_PROVEN_T1_faded_black.json` and `spec_PROVEN_T2_pilled_smooth.json`.


# Round 4: Version 2 in the channel's own style (the user's "French Women Never Wear" thumbnail as the reference)

**Final V2:** `old-clothes-new_thumbnail_V2_same_gown.jpg`, 1280x720, reading **Same Gown, / 4 Years Later / \*altered, not replaced\***, with "2019" and "2023" under the outer panels.
**Version 1** stays `old-clothes-new_thumbnail_PROVEN_faded_black.jpg`. Upload both to Test & compare.
**Backup copy:** `old-clothes-new_thumbnail_V2_alt_rewear.jpg` (Elegant Ladies / Re-Wear It, underlined), on the same photos.

**Why this picture.**
- The reference style is three tall photos of real, well-known elegant women. That is the user's French thumbnail and Classy Academy's own, which often shows the Princess of Wales.
- The script's point 6 has exactly one such woman and one such story: the Princess of Wales at the 2023 BAFTAs wore the white Alexander McQueen gown first worn at the 2019 BAFTAs, altered at the shoulder and with black opera gloves (fact-checked in `script.md`; CNN, PureWow).
- Royal re-wear is also the angle of the biggest video with our exact title: Star News Today, "10 Fashion Tricks Princess Diana Used to Make Old Clothes Look New Again", 2.37M views, 56x its channel. Royal thumbnails on the topic have a median of 100x (n=4, round 3).

**Copy.** "Same Gown, 4 Years Later" asks the viewer to compare the panels, which opens a curiosity gap. "Altered, not replaced" is the video's promise in three words.
- It is true: 2019 → 2023 is four years, and the dress was altered.
- It does not repeat the title's words (`title.py`).
- Title and thumbnail read as one unit: the thumbnail gives the proof, and the title gives the how.

**The channel's type, exactly.** Top line Cormorant SC (cap 46), headline Montserrat Bold 700 (cap 108) in Title Case, small line Cormorant SC in asterisks, panels at x 0-401 / 403-850 / 852-1280 with light dividers, the warm grade, a vignette behind the words, the CE logo top-left.

**Checks.**
- Built at 1280x720.
- At phone size (`thumb4/feed_v2.jpg`, 168 px and 246 px wide, beside Never Wear 1.2M and Hairstyles 957k), "4 Years Later" reads in one glance, she is recognisable, and it sits in the same family.
- The vignette was deepened (dark 125) because the white gowns sit behind the words.
- Every photo is a high-resolution original (2045-3456 px wide) with no watermark; Getty-watermarked pins were rejected.

| Panel | Photo | Found on | Source page | Rights |
|---|---|---|---|---|
| Left, 2019 | BAFTA red carpet, 10 Feb 2019 (2045x3422) | Pinterest, pinned by @catharinaleroux | people.com/royals/kate-middleton-princess-diana-earrings-bafta-look | press-agency photo: **unresolved** |
| Centre, 2023 | BAFTA, 19 Feb 2023 (3456x5192) | Pinterest (Grazia's own pin) | graziamagazine.com/articles/kate-middleton-baftas-2023 | press-agency photo: **unresolved** |
| Right, 2023 | BAFTA, 19 Feb 2023 (2867x4300) | Pinterest (RegalFille's pin) | regalfille.com/2023/02/prince-princess-wales-attended-2023-bafta-night | press-agency photo: **unresolved** |

**Public figure:** `SOURCES-LOG-TEMPLATE.md` warns against a famous face in a thumbnail where it could suggest endorsement. Here she is shown as the subject of a factual story the video tells, as on Classy Academy's own Kate thumbnails. Still, the photos are agency-owned. Before publishing, either license them (Getty / PA / Shutterstock editorial) or accept the risk in writing.

**Editable source:** `thumbnail/ca_thumb.py` (now with year labels) plus `spec_V2_same_gown.json` and `spec_V2_alt_rewear.json`.
