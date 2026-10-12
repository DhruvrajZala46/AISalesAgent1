# Editing rules from moment-level data: The Classy Elegance (12 Oct 2026)

Every number below comes from files in this folder. "Our channel" means the 30 uploads in `data/v`.
Their metadata names the channel "Classy Academy".

## 1. The 12 rules (short version)

| # | Rule | Key number | Confidence |
|---|---|---|---|
| 1 | Start every list item with a full-screen white number/title card (2-3 s, item name in script) | White cards show up **2.67x** more often than chance at our replay peaks (28 frames vs 10.5 expected, p<0.001). They lift their segment **+13.3%** above the local trend (p=0.0002). Competitors' text cards: **2.33x** at peaks (p=0.0003). | High. They work as landmarks that viewers jump to (see caveat in 2.4). |
| 2 | Reach item #1 by **0:30** at the latest. Keep the hook at about 15 s, then go straight to the title card | From 0:15 to the first item, replay runs at **0.41x** each video's median, and it is below the median in **18 of 18** of our videos. Intro talk is **0%** of our peaks and **11.7%** of our dips (p=0.0001). Our first item comes at a median of 35 s. | Medium. We can't prove a shorter intro wins views, because intro length vs views gives rho -0.15, p=0.55. |
| 3 | Cut abstract "why/philosophy" talk to one sentence per item | Abstract explanation is **24.2%** of our dips and **5.0%** of our peaks (p<0.001). For competitors: **31.8% vs 7.7%** (p<0.001). | High |
| 4 | Spend the screen time on the fix (the "instead"), not on describing the mistake | Swap or before/after moments are **5.8%** of our peaks and **0%** of our dips (p=0.014). At faceless competitors, describing the mistake is **21.2%** of dips and **1.2%** of peaks (p=0.0001). | Medium-high |
| 5 | Demonstrate (hands doing it, step by step, a try-on) instead of describing | Demo/how-to moments are **22.5%** of our peaks vs **13.3%** of dips (p=0.09). For competitors: **23.2% vs 12.3%** (p=0.004). Our #2 video (942k, hairstyles) has 4 of its 5 peaks on step-by-step demo clips. | Medium |
| 6 | Cut full-screen "cinematic" filler clips (film scenes, celebrities, mood shots). Use them only as 1-shot transitions | Full-screen clips show up **0.62x** as often as chance at our peaks (p=0.007) and **1.31x** at our dips (p=0.023). Their segments sit **-4.3%** below the local trend (n=564, p<0.001), and **-7.9%** when one shot is held 5 s or more (n=29, p=0.0003). | High (our channel) |
| 7 | Show the content on the caramel backdrop: one centred vertical clip, or a row of 2-4 clips | Competitors' centred clip on a backdrop: **1.45x** at peaks (p=0.01). Ours: single clip is neutral (+0.5%, p=0.54), and rows of clips show up only **0.69x** at dips (p=0.037). | Medium |
| 8 | Put a new picture on screen at least every **5 s**, but keep **one layout** for a whole item | When the picture doesn't change, the segment drops **-3.7%** vs trend on our channel (p=0.01) and **-17.9%** at faceless competitors (p=0.004). Faceless videos with higher like rates switch layout type **2.4/min** vs **3.3/min** for lower ones (p=0.08). | Picture change: medium-high. Layout calm: low. |
| 9 | Use on-screen text only for the item title or card and one key word. Drop long quote overlays | Text on cards: **+13.3%** (ours), **+42.7%** (competitors). Text on footage or backdrop outside cards: **-1.8%** on ours (p=0.04) and **+4.7%** at competitors (p=0.056). | Medium |
| 10 | Put the guide plug (10 s or less) at the end of an item, immediately followed by the next number card. Never put it mid-item | Promo/CTA is **13.3%** of our dips and **0.8%** of our peaks (p=0.0002). CTA segments drop **-5.5%** (p=0.018). **13** peaks (7 ours, 6 competitors) are the next reveal landing right after a plug. | Medium |
| 11 | Cast the footage to match the audience (ages 30-70+, real bodies, mixed skin tones), use real women, no AI people, and no polarising celebrities | "Models too young/thin": **39** comments, **1,119** likes, 11 of them on our channel. Diversity praised or requested: **8** comments, **143** likes. AI visuals criticised: **6** comments. Meghan Markle images: **3** negative comments on our channel (24 likes). | Medium (comments, not watch data) |
| 12 | The picture must show exactly the item being named. Mark good vs bad clearly. Follow one real woman through a section when you can | "Pictures don't match the words": **14** comments, **252** likes (3 faceless competitors). Faceless videos built around one real woman: median like rate **2.45%** vs **1.03%** for videos with many different women (n=3 vs 13, p=0.025). | Matching: medium. One-woman continuity: low (thin data). |

What the data **cannot** prove:
- Hook visuals: the first 60 s of our best and worst videos look the same. Full-screen share is 51% vs 53%, and every hook feature has |rho| ≤ 0.33, p ≥ 0.08, against age-adjusted views.
- Layout mix vs views: once video age is accounted for, no layout share predicts our views.

---

## 2. What was measured

### 2.1 Data
- **Competitors:** 50 winners in `proof2`. Storyboards came down for 49 (`cDeZJYNSbB8` returned 404 on every sprite). 44 of them have a heatmap, and 16 of those are faceless.
- **Our channel:** 30 long videos, 24 with a heatmap.
- **Storyboards (sb0):** 708 sprites downloaded with curl, 1 s apart. 8 failed. 7 of the failures were rebuilt from `own/sb/*.mhtml`. The last tile of `FA5i_dkTTXQ` is missing.
- **Frames:** cut into **10,273** frames: 7,062 competitor and 3,211 ours. Spacing is one frame every 4.9 s (fps 0.2) or 9.9 s (fps 0.1), and 1.98 s for `L251XRvuJCM`.
- **Timing check:** the white number cards in `My7qteRU9k0` appear at 44.6, 89.2, 133.7 and 242.7 s. The spoken "Number one/two/three/four" falls at 42.9, 85.8, 133.1 and 242.4 s, so storyboard timing is within one frame.

### 2.2 Visual labels (by eye, 100-frame contact sheets: `sheets/<id>_p<n>.jpg`)
- **Competitors** (`labels/<id>.txt`):
  - F full-screen footage
  - V centred clip/photo on a blurred or flat backdrop
  - M several clips side by side
  - T text card
  - H talking head
  - C product/detail close-up
  - B before/after or comparison layout
  - G graphic/diagram
  - P slideshow photo
  - K black/blank
  - Suffix `t` = on-screen text visible (includes burned-in subtitles). Suffix `a` = AI-looking image.
- **Our channel** (`labels_own/<id>.txt`):
  - F full-screen clip (includes a clip over its own blurred copy)
  - S single clip/photo on the caramel (or cream) backdrop
  - R row of 2-4 clips
  - P cut-out/photo panels
  - Q caramel backdrop with a quote, or empty
  - W white card (number, title or end card)
  - C detail close-up
  - G graphic
  - B before/after labels
  - K black
- Limits: one annotator, no second rater, 160x90 thumbnails. "Slideshow photo" vs "footage" can't be told apart from single frames, so P is under-counted.

### 2.3 Continuity (same woman/scene as the previous frame)
- **Method:** ResNet-50 embedding cosine similarity ≥ 0.84 counts as "same".
- **Calibration:** on 195 hand-judged pairs (`sheets/pairs_0..4.jpg`, `pair_labels.txt`), accuracy is **92.3%**, precision 0.93, recall 0.78. Weighted to the real similarity distribution, accuracy is 91.8%.
- **Pacing grid:** pacing numbers use a common grid (10 s for competitors, 5 s for ours), because storyboard spacing differs between videos.

### 2.4 Heatmap ("most replayed")
- **Segments:** 100 segments per video.
- **Peaks:** the top 5 local maxima, at least 3 segments apart, excluding the first 15 s and the last 5%.
- **Dips:** the 5 lowest local minima, chosen the same way.
- **Drop pattern:** mean value per quarter.
- **Sharp changes:** jumps of at least max(0.08, 2.5 SD).
- **Content coding:** all **680** peaks and dips were coded by hand from the transcript words at that moment ±1.5 s (`pd_list.txt`, `content_labels.txt`). Codes: list reveal, demo/how-to, swap/before-after, surprising claim, warning/mistake, concrete item, explanation, humour/story, intro, ad/CTA, recap, quote. `jenfPeWb5Q4` has no transcript.
- **Visual test:** each group's peak frames vs 3,000 draws of 5 random eligible segments per video.
- **Segment test ("lift"):** each segment's value divided by the rolling median of ±5 segments, compared within the same video, across all 6,000+ segments.
- **Caveat:**
  - The heatmap is relative watch intensity, normalised to 1 per video, and it includes seeking.
  - It is **not** audience retention, and it can't be compared across videos.
  - Many peaks at list reveals are viewers jumping to the next item, which makes number cards navigation landmarks.
  - There is no YouTube Studio retention data for our channel in this folder. That data would be the stronger test.

---

## 3. Findings

### 3a. What is on screen and being said at replay peaks

**Visual type at peaks vs chance** (observed / expected frames; p from the permutation test)

| Visual | Competitors, all 44 | Faceless competitors, 16 | Our channel, 24 |
|---|---|---|---|
| Text / white number card | **2.33x** (19 vs 8.1, p=0.0003) | **2.33x** (12 vs 5.2, p=0.005) | **2.67x** (28 vs 10.5, p<0.001) |
| Centred clip on backdrop / single clip on caramel | **1.45x** (p=0.010) | **1.37x** (p=0.030) | 1.06x (p=0.36) |
| Side-by-side clips / row of clips | **0.79x** (p=0.024 low) | **0.78x** (p=0.013 low) | 0.80x (p=0.15); at dips **0.69x** (p=0.037) |
| Full-screen footage / full-screen clip | 0.83x (p=0.11) | 0.94x | **0.62x** (p=0.007); at dips **1.31x** (p=0.023) |
| Close-up of the item | 0.80x (ns) | 0.75x (ns) | 1.31x (ns) |
| Before/after layout | 0.87x (ns) | 0.54x (ns) | 1 frame (thin) |
| Any on-screen text | **1.23x** (p=0.0013) | **1.27x** (p=0.020) | **1.45x** (p<0.001) |
| New picture vs previous frame | **1.12x** (p=0.007) | 1.04x (ns) | 1.03x (ns) |

**Lift by segment type** (difference from the video's own mean of value / local trend)

| Segment | Competitors | Faceless competitors | Our channel |
|---|---|---|---|
| Item reveal said in it ("number five", "rule three") | **+0.399** (n=491, p<0.001) | **+0.567** (n=273, p<0.001) | +0.072 (n=48, ns) |
| Text card / white card | +0.427 (n=137, p=0.006) | +0.472 (n=88, p=0.017) | **+0.133** (n=187, p=0.0001) |
| Text on footage, not a card | +0.047 (p=0.056) | +0.010 (ns) | **-0.018** (p=0.04) |
| Picture unchanged in the segment | **-0.058** (n=1,776, p=0.0001) | **-0.179** (n=128, p=0.004) | **-0.037** (n=198, p=0.010) |
| Full-screen clip | -0.010 (ns) | +0.001 (ns) | **-0.043** (n=564, p<0.001) |
| AI vs real frames (6 mixed videos) | AI -0.007 / real +0.006 (ns) | | |

**Content at peaks vs dips** (hand-coded, 220 / 220 competitor, 80 / 80 faceless, 120 / 120 ours)

| Content | Competitors: peaks / dips | Faceless: peaks / dips | Ours: peaks / dips |
|---|---|---|---|
| List reveal (new numbered item) | **34.1% / 2.7%** (p<0.001) | **43.8% / 3.8%** (p<0.001) | **45.8% / 9.2%** (p<0.001) |
| Demo / how-to / actionable step | **23.2% / 12.3%** (p=0.004) | 20.0% / 11.2% | 22.5% / 13.3% (p=0.09) |
| Swap / before-after ("instead") | 8.2% / 5.0% | 13.8% / 5.0% (p=0.10) | **5.8% / 0%** (p=0.014) |
| Surprising claim | **6.8% / 0%** (p<0.001) | 3.8% / 0% | 2.5% / 0% |
| Concrete item named | 11.4% / 8.6% | 12.5% / 18.8% | 12.5% / 18.3% |
| Humour / personal story | 8.6% / 5.9% | 2.5% / 2.5% | 0% / 0.8% |
| Warning / describing the mistake | **3.6% / 12.7%** (p=0.0007) | **1.2% / 21.2%** (p=0.0001) | 2.5% / 3.3% |
| Abstract explanation | **7.7% / 31.8%** (p<0.001) | **6.2% / 27.5%** (p<0.001) | **5.0% / 24.2%** (p<0.001) |
| Intro / hook talk | 1.4% / 8.2% (p=0.001) | 2.5% / 6.2% | **0% / 11.7%** (p=0.0001) |
| Ad / promo / CTA | **0% / 9.5%** (p<0.001) | 0% / 1.2% | **0.8% / 13.3%** (p=0.0002) |
| Recap / outro | 0.9% / 1.8% | 2.5% / 5.0% | 0.8% / 0.8% |

Where the peaks fall in the video (share of peaks):
- Competitors: 0-20%: 16.8, 20-40%: 23.6, 40-60%: 23.2, 60-80%: 24.5, 80-100%: 11.8.
- Ours: 16.7 / 20.8 / 25.0 / **30.0** / 7.5.

Drop pattern (mean heatmap value per quarter):
- Ours: 0.41 / 0.48 / 0.46 / **0.33**. Median Q4/Q1 = 0.87.
- Competitors: 0.25 / 0.27 / 0.30 / 0.21 (Q4/Q1 = 0.82).

Contact sheets (red = peak, blue = dip): `sheets/peaks_comp_0..3.jpg`, `sheets/peaks_own_0..1.jpg`.
- Rock Your Fashion `TFhmgp8frbA`: all 5 peaks are the white "#5. THE FADED BLACK CLOTHES…" title cards.
- Our `A-JRkjQs2XI`: all 5 peaks are vertical hair-tutorial clips on caramel. Its dips are full-screen portraits of finished hair.
- Our dips repeatedly show the dark "Personal Stylist Guide" promo card and full-screen film/celebrity clips.

### 3b. Faceless competitors: high vs low like rate (19 videos, 8 channels; split at the median like rate of 1.13%)

| Measure | High half (9) | Low half (10) | Test |
|---|---|---|---|
| Before/after layout share | 0.2% | 7.3% | Mann-Whitney p=0.034 (driven by Rock Your Fashion and Chic After 60) |
| Layout-type switches/min (10 s grid) | 2.36 | 3.27 | p=0.079 |
| Close-up share | 6.3% | 10.9% | p=0.14 |
| Side-by-side share | 54.0% | 37.0% | p=0.13 |
| AI-looking frames | 23.2% | 33.0% | p=0.66 |
| On-screen text (includes subtitles) | 16.4% | 26.5% | p=0.97 |
| New picture/min (10 s grid) | 5.40 | 5.49 | p=0.78 |
| Same scene as previous frame (10 s grid) | 10.7% | 9.2% | p=0.87 |

Subject continuity (hand-classified from the contact sheets):
- One real woman through the whole video (Trends Spotted's Sissi and Inès, Elvira's Jennifer Aniston): median like rate **2.45%** (2.71, 2.45, 1.26).
- Many different women: **1.03%** (n=13). p=0.025.
- One consistent AI model: 1.92% and 0.80%.
- Two of the three "one real woman" videos come from one channel, so treat this as a lead, not proof.
- Faceless videos overall have a median like rate of **1.13%**, vs **3.64%** for presenter-led ones (n=19 vs 28, p<0.001). Ours is **2.93%**.

### 3c. Our channel

Layout share across 30 videos:

| Layout | Share of frames |
|---|---|
| Full-screen clip | 29.5% |
| Single clip on caramel | 25.5% |
| Row of clips | 17.8% |
| White card | 9.8% |
| Caramel quote/empty | 6.0% |
| Cut-out panels | 5.2% |
| Detail close-up | 4.7% |

Peaks vs dips by layout: see the tables in 3a.
- **White cards win:** 23 of the 28 peak white cards are number cards at a list reveal.
- **Full-screen clips lose:** -4.3% overall, -7.9% when one shot is held for 5 s or more (n=29).
- **Single clips and rows are neutral.**

Best vs worst videos:
- **Age matters most:** age explains a lot of raw views (log views vs log age r = 0.66), so features were also tested against age-adjusted views. Top 6 by raw views: My7, A-JR, QOEU, q78, oHh4, RiTn. Bottom 6: MNEo, -pOz, 2Y-P, -dfv, eDGH, OSAN.
- **Raw views:**
  - Fewer layout switches/min goes with more views (rho -0.44, p=0.015). Cut-out panels (rho +0.43, p=0.018) and caramel quote frames (rho +0.42, p=0.022) also go with more views.
- **Age-adjusted views:**
  - Those three drop to rho -0.21 (p=0.26), +0.26 (p=0.17) and +0.18 (p=0.33).
  - The only significant feature is graphic/diagram share, rho -0.38 (p=0.039), driven by the body-shape diagrams in `B5jfik9g63o`.
- **So the earlier conclusion in `edit-style-measured.md` does not survive the age adjustment.** That conclusion was "the more watched, the more caramel and the calmer the pace". Older videos simply had that style and more time to collect views. Topic, not layout, separates our best from our worst.

Hooks (first 60 s, `sheets/hook_own_top15.jpg`, `hook_own_bottom15.jpg`):
- The formula is the same in every video: full-screen cinematic clips for 0:00-0:25, the "Episode/title" card at 0:24-0:34, then the first number card.
- Top 6 vs bottom 6:

  | Hook feature | Top 6 | Bottom 6 | Correlation with age-adjusted views |
  |---|---|---|---|
  | Full-screen share | 51.3% | 52.6% | rho +0.17, p=0.38 |
  | Text in hook | 16.7% | 16.7% | rho +0.06 |
  | Rows in hook | 9.0% | 16.7% | rho -0.33, p=0.08 |
  | Cut-out panels in hook | 9.0% | 1.3% | rho +0.31, p=0.10 |
  | First white card | 34.6 s | 37.1 s | |

- **Data too thin:** none of these hook differences is significant.
- **What is solid:** after 0:15 the intro is skipped or under-watched in every video (0.41x the median until item 1). The competitors' equivalent is 0.60x, with their first item at 46 s.

Where our viewers replay:
- **Peaks:** list reveals (46% of peaks), demos (22.5%), concrete items (12.5%).
- **Dips:** abstract explanation (24%), the guide plug (13%), the intro (12%), concrete items (18%), quotes (5.8%).
- **Example:** `oHh4T67jJNM` peaks at 2:57 on the guide plug. The words at 160-200 s confirm this is the plug, so this one is an exception.

### 3d. Comments about visuals
3,382 competitor and 2,685 own comments were scanned with keywords and then read by hand (`comments_visual_curated.json`).

| Theme | Comments | Likes | Of which ours | Top example |
|---|---|---|---|---|
| Models too young/thin for the audience | 39 | 1,119 | 11 (101 likes) | "It would have been nice if your model actually had saggy skin as a woman in her 70's" (272, Chic After 60, AI model). Ours: "Most of these models have a perfect egg shape…" (34); "They keep putting pictures of models women! Like everyone is young and thin" (9); "more than 90% of the images… very slim bodies" (7) |
| On-screen graphics / visual explanation praised | 11 | 4,766 | 0 | "Love the on-screen graphic showing the different styles part of each outfit" (975, Mademoiselle Spends); "visually presented your tips" (407, Asia Jackson) |
| Pictures don't match the words / can't tell good from bad | 14 | 252 | 0 | "Same pictures and narrative did not match the photos" (84); "I can't tell the difference between the good examples and the bad ones" (16) |
| Our visuals praised | 7 | 250 | 7 | "the images were stunning. Also, you spoke slowly enough" (158, My7) |
| Diversity praised or requested | 8 | 143 | 4 (58) | "Can you do a part 2 with some added pictures of darker skin women" (34, ours) |
| AI visuals or "AI feel" criticised | 6 | 45 | 2 (3) | "I WANT TO SEE REAL HUMANS" (aQ3H); ours: "Why do you use AI videos and photos to showcase products?" (L251) |
| Wrong person shown (Meghan Markle) | 3 | 24 | 3 | "Showing Megan Markle as a picture of elegance was certainly a mistake" (16) |
| Soft music praised | 5 | 80 | 4 (73) | "gentle voice with that quiet background music is so peaceful" (34) |
| Text covering the item | 1 | 3 | 0 | "the 2nd set of words at the bottom obscured the visual" (Chic After 60) |

Not about visuals, but frequent on our channel: **27** comments mention "voice" together with "AI" (most-liked 113, praising a real voice; the others have 0-32).

---

## 4. Rules with full evidence

1. **Number card opens every item** (white, script number + item name, 2-3 s).
   - Evidence:
     - White cards are 2.67x over-represented at our peaks and lift their segment +13.3%.
     - Competitors' text cards are 2.33x at peaks and lift +43%.
     - List reveals are 45.8% of our peaks vs 9.2% of dips.
   - Interpretation: viewers navigate by these cards, so make them unmistakable and consistent.
   - In the newer "habits" videos (`oHh4T67jJNM`, `rHI_hcgK39E`), some reveals were spoken over full-screen clips with no card. Those videos still peak at the reveal, but the card is the cheapest landmark.
2. **Item 1 by 0:30.**
   - Hook: 1-2 strong real clips with the promise, then the title card, then "Number one".
   - Evidence: 0.41x replay before item 1 in 18 of 18 videos, and intro talk is 0 of 120 peaks.
   - Hook visual formula: no evidence for any change (see 3c).
3. **One sentence of "why" per item, no more.**
   - Evidence: explanation is 24% of our dips vs 5% of peaks. Competitors show the same pattern (32% vs 8%).
4. **Show the mistake briefly, then the swap.**
   - Order: 1 frame of the mistake, then the swap with the "instead" items each on screen.
   - Evidence:
     - Swaps are 5.8% of our peaks vs 0% of dips.
     - At faceless competitors, describing the mistake is 21% of dips vs 1% of peaks.
     - Faceless videos that lean on before/after split layouts have lower like rates (0.2% vs 7.3% share, p=0.034). Show the swap as footage, not as a split-screen.
5. **Demo footage for every actionable tip** (hands tying, tucking, steaming, applying; a try-on).
   - Evidence:
     - Demos are 22.5% of our peaks vs 13.3% of dips, and 23.2% vs 12.3% for competitors (p=0.004).
     - The hairstyles video (942k) has 4 of 5 peaks on step demos.
6. **Fewer full-screen cinematic clips.**
   - Target: from 29.5% to 15% or less of frames, mainly hook and section transitions. Never hold one for 5 s or more.
   - Evidence: 0.62x at peaks, 1.31x at dips, -4.3% lift, -7.9% when held (n=29).
7. **Main "show" layout: a single centred vertical clip, or a row of 2-4 clips, on the caramel backdrop.**
   - Evidence: competitors 1.45x at peaks; our rows 0.69x at dips; neutral lift.
8. **Pacing.**
   - A new clip or image at least every 5 s. Keep the same layout family for the whole item.
   - Evidence:
     - A segment with an unchanged picture loses -3.7% (ours) and -17.9% (faceless competitors).
     - Calmer layout switching goes with higher like rates (2.4 vs 3.3/min, p=0.08, weak).
9. **Text only as titles or one keyword.**
   - Evidence: cards help (+13%), while text on footage outside cards does not (-1.8%, p=0.04). Never cover the item with text (1 comment).
10. **Guide plug.**
    - 10 s or less, at the end of an item, followed by the next number card. Not in the first 60 s and not mid-item.
    - Evidence: CTA is 13.3% of dips vs 0.8% of peaks, and CTA segments lose -5.5%. 13 peaks are the reveal right after a plug.
11. **Casting.**
    - For each item, pick clips of women 30-70+, several sizes and skin tones, real (no AI people), and no polarising celebrities.
    - Evidence: 39 comments / 1,119 likes on age or body mismatch; 8 / 143 on diversity; 3 / 24 on Meghan Markle; AI visuals criticised in 6 comments.
12. **Word-picture match and continuity.**
    - The clip on screen must show the exact garment, colour or gesture being named, at the moment it is named.
    - Label which look is "avoid" and which is "instead".
    - Where possible, keep the same real woman across the 2-4 clips of one item.
    - Evidence:
      - 14 "pictures don't match" comments with 252 likes.
      - 975 likes for an on-screen graphic that labels the styles.
      - One-real-woman videos: median like rate 2.45% vs 1.03% (n=3 vs 13, p=0.025, thin).

Where the data is too thin:
- Hook visuals: n=30, all non-significant.
- One-woman continuity: 3 videos.
- Layout calm vs like rate: p=0.08.
- AI vs real frames: replay shows no difference across 6 videos, so the evidence against AI comes from comments only.
- Recap/outro: 1 peak and 1 dip.
- Like rate depends heavily on the channel (faceless channels sit at 0.5-2.7%) and on audience age, so 3b is suggestive only.

---

## 5. Files
- `per_video_measurements.json`: for each of the 79 videos:
  - visual-type shares, text %, AI %
  - continuity and pacing on a common grid
  - hook (0-60 s) codes
  - quarter means, sharp changes
  - 5 peaks + 5 dips, each with the words, the hand-coded content and the frames (visual type, text, same-as-previous)
- `aggregate.json`: all tests in this report (permutation, lift, content, like-rate, our views with age adjustment, quarters).
- `aggregate_extra.json`: off-card text, AI vs real, held shots, subject continuity.
- `intro_timing.json`: first-item time and intro replay level.
- `heat.json`: raw heatmaps, peaks, dips, sharp changes, with transcript words.
- `comments_visual_raw.json` (keyword hits), `comments_visual_curated.json` (hand-sorted).
- `labels/`, `labels_own/` (frame labels), `content_labels.txt` + `pd_list.txt` (peak/dip content), `pair_labels.txt` (continuity calibration).
- `sheets/`:
  - `<id>_p<n>.jpg` (all frames, 100 per sheet)
  - `peaks_comp_0..3.jpg`, `peaks_own_0..1.jpg`
  - `hook_own_top15.jpg`, `hook_own_bottom15.jpg`
  - `pairs_0..4.jpg`
- `sb/` (raw sprites), `frames/` (cut frames, npz), `emb/` (embeddings), `scripts/` (all code).
