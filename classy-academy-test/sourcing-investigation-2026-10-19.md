# How Classy Academy sources its visuals: investigation (19 Oct 2026)

**The question:** where do the channel's clips and photos come from, how are they found and chosen, and how do we apply
that to "Why Her Hair Always Looks Expensive"? This file answers from evidence, not from guesses.

**Labels:**
- **[C] Confirmed:** seen directly, or an identical copy was found and checked by eye.
- **[H] Hypothesis:** consistent with the evidence, but not proven.
- **[?] Unknown:** not established.

## 1. Evidence base and method

**Frames:**
- **All 30 long uploads:** YouTube's three public preview frames per video (`sd1`–`sd3`, 640×480). That is 90 frames, split into
  147 picture panels with `tools/panels.py`.
- **The three hair/beauty videos:** also their `hq1`–`hq3` frames and the thumbnails.
- **Earlier evidence:** the trace of about 170 frames from 7 videos (`source-trace-2026-10-17.md`).
- **Not used:** the storyboard files you declined. No video file was downloaded.

**Trace:**
- Every panel went to Yandex "search by image" (`workflow/tools/revsearch.py`).
- A match was counted only when its similarity score was 0.85 or higher **and** I checked it by eye on the review sheets.

**Other evidence:**
- **Captions:** of Hairstyles, Haircuts and Grooming (read to tie each frame to the line being spoken).
- **Descriptions:** of the three hair videos.
- **Your public accounts:** TikTok @classyacademy, its creator embed, and classyladyacademy.com.
- **TikTok profile checks:** of every credited handle.
- **Pinterest searches:** run to reproduce your likely searches.

**Limits:**
- 90 frames is a sample: about 3 per video, at positions YouTube chooses.
- Small frames find famous images easily and creators' clips less often.
- "Not found" means "not found by this method".

## 2. What the channel's visuals are made of [C]

**Result: 63 of the 147 panels have an identical copy online.** Each was checked by eye; 2 high scores that were false matches were dropped. **For 52 of those 63 (83%), the copies include Pinterest pins**, usually dozens of repins. The other 11 are on film/clip sites, news sites, Pexels and marketplaces. The 84 panels with no match are mostly creators' clips: the method finds famous images more easily.

| Source type | Examples found (video → what) | Where the copies live |
|---|---|---|
| **Creators' outfit and lifestyle photos and reels** (Instagram, TikTok, LTK) | Feminine Energy: three creators at dinner and in the street. Make Jeans Elegant: mirror selfies (one creator posts on LTK as Kelseyngross). Color Combos and Summer Color Combos: outfit photos. Old Money Fall: three creators in fall outfits (one clip has the creator's own "good morning" text). Pose Like a Classy Lady. 10 Signs. | Pinterest (dozens of repins each), LTK, Pinterest-fed blogs |
| **Creators' hair tutorials and hair photos** | Hairstyles: half-up clip tutorial, **credited "@allchloerose on TikTok"**. Haircuts: salon bob video; TikTok curtain-bangs video (TikTok logo visible on the pinned copies). Grooming: creator portrait at Christmas. | Pinterest; TikTok |
| **Celebrities: press, TV and event footage** | Kate Middleton in 7 of 30 videos, all confirmed by the trace (royal tour of Ireland 2020, a green-hat event, a video message in a purple blouse, Nottingham Trent visit, National Portrait Gallery reopening, a navy suit, a gingham-collar blazer). Meghan Markle (Netflix, "With Love, Meghan"). Angelina Jolie. Günay Uslu (event photo). Amal Clooney (AFI tribute to George Clooney, TNT 2018). Anne Hathaway interview. Jessica Alba. Jasmine Tookes. Ryan Destiny. Paulina Porizkova. Natasha Poly. | Pinterest, news sites, YouTube |
| **Film scenes** | "The Wolf of Wall Street" (Margot Robbie) in 5 videos. "Gentlemen Prefer Blondes" (Marilyn Monroe) in 2. "Scent of a Woman" (Gabrielle Anwar, restaurant scene) in 2, confirmed by pins naming her and the film. "Breakfast at Tiffany's" and "Sabrina" (Audrey Hepburn). | GIF/clip pages, Pinterest, Russian video sites; some copies carry film-page watermarks (KINOFUN), your copy does not |
| **Retailer product photos** | Make Jeans Elegant: a Mango/Riani tank top on a plain background. Color Combos: trousers and a jumper. Never Wear: a Trendyol product. | Marketplaces (Ozon, Trendyol, Riani), Pinterest |
| **Free stock (Pexels)** | **Old Money Fall (Sep 2026): woman in a car's back seat.** Identical clip on Pexels ("Mercedes Maybach" / "Everyday Luxury" pages). Also Sound Elegant (3 clips) and Never Share (1), from the earlier trace. | Pexels |
| **Possibly AI images [H]** | 8 Easy Ways: a silver-bob woman (60+) in a grey turtleneck on a studio-grey background. Summer Color Combos: two outfit images. Body Language Habits: an older woman in a straw hat (pins "Best Summer Hats for Older Ladies"). Sound Elegant: the dining scene; its largest copy is 1536×2688, exactly double a common AI generator size (768×1344). They appear only on Pinterest and on auto-generated listicle pages ("Hairstyles for women over 60", "What colors to wear with pastel yellow"). Never Wear: an animated colour Audrey Hepburn portrait. | Pinterest, listicle farms |

**Recurring material:**
- **Wolf of Wall Street (Margot Robbie):** 5 videos.
- **Kate Middleton:** 7 videos.
- **Audrey Hepburn:** at least 4 videos.
- **Gentlemen Prefer Blondes:** 2 videos.
- **Scent of a Woman:** 2 videos.
- **Creators named on screen:** two, Chloe Rose (@allchloerose) and Kate Hutchins (@kateehutchins).
- **The same photo is reused across videos:** Jasmine Tookes at dinner appears in both Feminine Energy and Never Share. That points to a kept personal library, not a fresh search each time.
- **No single creator** dominates the outfit footage. Each video draws on many different creators' photos.

## 3. Creator credits: a convention you already use [C]

| Video | Where | Credit on screen | Creator (checked 19 Oct 2026) |
|---|---|---|---|
| The Most Elegant & Easy Hairstyles (Jan 2025) | Half-up clip tutorial, centred on caramel (~2:04) | "@allchloerose on TikTok" (white script, bottom right) | TikTok @allchloerose, Chloe Rose, 297.8k followers, "Fashion, beauty, hair, home" |
| How to Dress Elegant: A Beginner's Guide | Vertical outfit clip, centred on caramel | "@kateehutchins via tiktok" (white serif italic, bottom right) | TikTok @kateehutchins, Kate Hutchins, 936.4k followers; she pins her own reels on Pinterest |
| 6 Elegant Summer Shoes | Row panel | No credit; TikTok's own watermark "♪ @eder…" (cut off) | not identified |

**What the credits show:**
- The credit is typed by hand: the wording and font differ between videos.
- It sits under single-creator vertical clips.
- I found none on rows of photos, and none in the 2026 frames sampled.
- **[H]** Credits are used for TikTok clips of one creator, not for every picture.

## 4. Search route (how the clips are found)

| Hypothesis | Evidence for | Evidence against or missing | Verdict |
|---|---|---|---|
| **H1. Pinterest is the main discovery layer** (search, save, download pins) | 52 of the 63 identified panels (83%) have copies on Pinterest, usually dozens of repins. Pinned copies of TikTok exports keep TikTok's watermark, like the "@eder…" clip. Clips you used also exist as files named "Pinterest-84bf0.mp4" on other sites, so Pinterest downloads of them circulate. Earlier: the #1 video's opening clip is a pin saved on boards named "Footage". | No board or account of yours found. Re-running narration keywords ("hollywood waves", "old money bob") on Pinterest today does not return your exact images in the top 100, but results change over 9 months. | **Most likely [H].** Not provable from outside your account. |
| **H2. TikTok searched directly for tutorials** | Credits name TikTok handles ("on TikTok", "via tiktok"). | @classyacademy follows 0 accounts and has liked 0 videos, and its favourites are private. The handle could equally come from the watermark or the pin text. | **Possible [H]** for tutorials. |
| **H3. Instagram/LTK browsed directly** | Many outfit photos are LTK posts and creators' Instagram posts. | No credit or link to Instagram in any frame or description. | Unproven [?]. |
| **H4. Free stock for everyday actions** | Pexels clips confirmed in Old Money Fall, Sound Elegant and Never Share. | — | **[C]** part of the past workflow. **Excluded for this video by your instruction.** |
| **H5. Film/TV from clip pages and YouTube** | Famous scenes, clean copies without the watermarks that the GIF/Instagram copies carry. | Exact source not traceable. | [?] |

## 5. How visuals are chosen (selection rules seen in the frames) [C]

1. **Named woman, shown when named.** Audrey Hepburn appears at "Audrey Hepburn's look" (Grooming 0:54), and Kate Middleton
   in grooming and posture moments.
2. **Tutorial lines get a vertical tutorial clip of exactly that step, centred on caramel.** For example the half-up clip
   tutorial at Hairstyles 2:04 ("gathering the top section … securing it with a clip").
3. **A style or result line gets a row of 3 finished looks.** The row deliberately mixes skin tones and ages: Haircuts
   "Hollywood waves" uses a blonde model, a Black woman and Paulina Porizkova at 60.
4. **Warm, soft light; cream, camel and black clothes; faces visible and smiling.** Pictures are chosen to match the
   caramel palette.
5. **Newest layout (Grooming, Aug 2026):** photos framed with caramel margins, one centred or two side by side with a
   gap, plus full-screen video for celebrities. Haircuts (Jan 2026) also uses a light quote screen ("It's a style that
   doesn't ask for attention…").
6. **Episode label.** "Episode 7/8/10" sits above the script title in several videos. Some 2025 videos also have white
   serif subtitle lines at the bottom (7 Habits, Casual yet Elegant, 8 Color Combos); none was seen in the 2026 frames.

## 6. Rights: what the evidence says [C]

- **No traced clip shows a licence.** The descriptions carry no credits.
- **An on-screen credit is attribution, not permission.**
- **Studio film and TV footage is what Content ID matches.** Claims would show only in your YouTube Studio, which I
  cannot see.
- **For the hair video**, each candidate is therefore listed with a verified original post and "permission: not granted -
  request needed". A credit in your existing style is planned, and so is a permission request (template in
  `videos/expensive-hair/CLIP-CANDIDATES.md`).

## 7. What remains uncertain [?]
- **Your actual search route:** Pinterest-first is the most likely, but it is not provable without your account history.
- **Whether you hold permissions or licences** for any past clip.
- **The music source.**
- **Fonts:** the exact font files are unknown, as before.
- **Whether the possibly-AI images were knowingly chosen.**
