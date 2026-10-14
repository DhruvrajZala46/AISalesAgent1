# 8 Ways to Dress for Your Body Shape: thumbnails

Built with the `yt-package` skill (title + thumbnail as one unit), `workflow/4-THUMBNAIL.md` and the new
`tools/thumb_shape.py`. Title assumed: **8 Ways to Dress for Your Body Shape** (decided at the package stage).

## The proof: 42 body-shape winners, scored by how far each beat its own channel

Sources: the niche's 14,127 videos (`alltime.json`, 60 channels) + YouTube's own results for five searches a woman
types ("how to dress for your body shape", "dress for your body type women", "body shape styling tips over 50",
"how to find your body shape", "dressing for your body type mistakes"). Men's and off-topic videos dropped, the top 42
by views kept, each channel's median of its last 80 videos used for the multiple. Every thumbnail was looked at and
tagged by eye.

| On the thumbnail | n | median views | median multiple |
|---|---|---|---|
| **Same woman, mistake -> fix** (x/tick or before -> after arrow) | 7 | 1.34M | **67.5x** |
| Same woman, 2+ outfits | 14 | 1.41M | 55.4x (others 16.0x) |
| **Same woman + lines/arrows drawn on her body** | 6 | **1.84M** | 56.8x |
| Lines/arrows drawn on the body (any) | 13 | 1.31M | 38.1x (others 19.6x) |
| Shape icons / diagrams / illustration | 12 | 0.88M | **14.0x** (others 25.6x) |
| Line-up of different women | 8 | 0.66M | 18.0x |
| One woman + text only | 7 | 0.46M | 19.6x |
| All 42 | 42 | 0.66M | 22.6x |

Winners of the format: Kaiti Yoo 6.07M (88x, same woman twice, arrows and labels drawn on her), SuppleChicTV 2.23M
(154x, same woman before -> after), Style with Cathy 1.70M (241x), Libby 1.63M (15x, same woman, the shape drawn on her
in dashed lines), Asia Jackson 1.34M (43x), Anna Rova 0.84M (101x), Giedre 0.52M (22x), Annie Parker 0.42M (67x).
Shape icons and fruit diagrams win views on big channels but the lowest multiples; our own channel's data agrees
(static diagram slides were the one layout feature linked to fewer views, rho -0.38).

Words: "it's not you, it's the outfit" is the angle of three winners (Kaiti Yoo "I look bad in everything." dude, no.
you're just not dressing for YOU 6.07M / 88x; dear peachie "Why I Look Bad in Everything I Wear?" 2.10M / 61x; Desi
Rich's thumbnail "IT'S NOT YOU... IT'S THE OUTFIT") and our own hook ("Before you blame your body for one more outfit,
stop... Only clothes that are cut for it, or not"). Told kindly: the fault is the cut, never her body.
Topic words on the thumbnail: the 88x winner ("HOW TO DRESS YOUR BODY TYPE"), Glamrs 90x, Anna Bey, Justine Leconte.

Our audience: "models too young / too thin" 39 comments, 1,119 likes -> the main thumbnail shows a woman over 50.

## The three (YouTube Studio -> Thumbnail -> Test & compare)

1. **A (recommended)** `thumb_A_its_not_you.jpg`: ALEX @mylifeafter_50 (over 50), her own before -> after: the tight
   tee over slim jeans she calls "dated, frumpy and unflattering" (cross) -> layered with an open blazer and a belt
   (tick). Lines drawn only where she explains them herself: the tee ending at "the widest part of hips" (dashed line,
   "widest point") and "open blazer creates vertical lines... the belt emphasizes the waist" (two long dashed lines,
   "waist"). Words "IT'S NOT / YOU / *it's the cut*" (`title.py` 100/100).
2. **B** `thumb_B_dress_for_your_shape.jpg`: the same image, the topic words "DRESS FOR / YOUR SHAPE / *at any age*"
   (94/100: repeats "shape" from the title on purpose, like the 88x winner). A vs B tests feeling against topic.
3. **C** `thumb_C_its_not_you_dress.jpg`: Jaymehallyall (our video's hook woman, point 3), her own "easy hack for
   oversized dress": the dress hanging straight from its fullest point (cross, two straight dashed lines) -> tied at
   the waist (tick, a waist curve). Same words as A. A vs C tests the woman (over 50 vs 30s-40s, our clip).

Feed test (`feed_test.jpg`, 320x180 next to six winners): "IT'S NOT YOU" reads in one glance, the faces stay clear,
the caramel stands apart from the white and grey winners. B's words are smaller (10 letters on the bold line) but read.

## Photos (real, checked)

- A, B: ALEX, @mylifeafter_50 (Instagram reel DPwgSIjDnRJ, 13 Oct 2025, 4,345 likes, 135 comments; found through a
  repin by @gearjunkie77, https://www.pinterest.com/pin/60094976274814979/). Frames 0.05 s and 9.6 s, framed head to
  upper thigh, so her own caption (across her hips) is not in the picture. Watermark scan: none; metadata: plain
  phone re-encode (Lavf); eyes: real room, real skin, real hands, she talks in her own reel.
- C: Jaymehallyall, @jaymehallyall (https://www.pinterest.com/pin/320811173468624784/, clip `loosedress11`), frames
  0.1 s and 7.4 s; her "Easy hack for oversized dress" caption box (on the curtain) painted out before the cut-out.

Description credit line: `Thumbnail photos: @mylifeafter_50 @jaymehallyall`

## The winners (tags: s same woman 2+ outfits, f mistake -> fix, d drawn on her body, i icons/illustration,
## l line-up, t one woman + text, a no real photo)

| # | channel | title | views | multiple | tags |
|---|---|---|---|---|---|
| 1 | Kaiti Yoo | "I look bad in everything." dude, no. you're just not dressi | 6.07M | 88.0x | sd |
| 2 | The Lifestyle Cog | The Ultimate Guide to Finding Jeans for YOUR Body Type / Sty | 5.31M | 83.5x | si |
| 3 | TheThings Celebrity | 10 Best Ways To Dress For YOUR BODY SHAPE | 2.78M | 1544.3x | ia |
| 4 | SuppleChicTV | WORST FASHION MISTAKES 4 TUMMY / BELLY FAT 🛑 5 THINGS YOU SH | 2.23M | 153.9x | sfd |
| 5 | dear peachie | Why I Look Bad in Everything I Wear? How to Dress for Your B | 2.10M | 60.9x | idfa |
| 6 | Dearly Bethany | 5 Things To AVOID if you have Curvy Hips (Like Me) | 2.05M | 25.6x | sd |
| 7 | Style with Cathy  | Summer Style Tips for Plus Size Apple Shape Women: How to Tr | 1.70M | 241.0x | sf |
| 8 | Justine Leconte officiel | How to determine your body type / How to take your measureme | 1.66M | 10.2x | i |
| 9 | Anna Bey | How To Dress For Your Body Shape | 1.64M | 3.1x | i |
| 10 | Libby | How to dress for your body shape in under 12 mins | 1.63M | 15.1x | sfd |
| 11 | Glamrs | How to Take Measurements & Determine Your Body Type / Differ | 1.48M | 89.9x | sd |
| 12 | Asia Jackson | How to Understand Your Body for Better Outfits | 1.34M | 43.3x | sf |
| 13 | The Style Theorists and The Food Theorists | What's Your Body Shape... and How to Dress for It / Style Th | 1.31M | 0.0x | d |
| 14 | Morah Style Lab | Dress To Impress: Chic Outfits For Large Tummy! | 1.26M | 147.7x | l |
| 15 | Busbee Style | How To Determine Your Body Shape Using Measurements | 1.26M | 16.0x | ia |
| 16 | The Lifestyle Cog | 6 Easy Outfit Ideas Using Wide Leg Jeans / Petite Girl Guide | 1.00M | 15.7x | s |
| 17 | MM Personal Styling  | Body Shape Masterclass 20 / How to Dress for Your Body Shape | 0.90M | 13.3x | l |
| 18 | Elegance At 60 | Pants to Avoid with a Large Tummy & Lower Belly Pooch - Appl | 0.89M | 55.3x | lfd |
| 19 | Anna Rova | Dressing Rules EVERY Woman Should Learn Once and For All | 0.84M | 101.1x | sf |
| 20 | jasmine le | “Why do I look bad in everything I wear?” how to dress for y | 0.78M | 2.8x | sd |
| 21 | Audrey Coyne | I LET 4 BODY TYPE EXPERTS DRESS ME *life changing* | 0.69M | 6.2x | l |
| 22 | Ally Purugganan | NEVER HAVE A BORING OUTFIT! dressing for your body type, acc | 0.63M | 1.9x | l |
| 23 | Ethereal Elegance | 25 Styling Secrets High Class Elegant Women Over 50 NEVER Sh | 0.61M | 144.3x | f |
| 24 | Audrey Coyne | PETITE STYLE TIPS: Styling Hacks 5'4" & Under + How To Dress | 0.58M | 5.2x | t |
| 25 | Marie-Anne Lecoeur - The French Chic Expert | How To Look Slimmer: The MOST EFFECTIVE Style Tips For Women | 0.55M | 16.0x | t |
| 26 | Giedre Kavaliunaite | Avoid These 7 Plus Size Fashion Mistakes / Fixing | 0.52M | 22.5x | sf |
| 27 | The Essence Of Elegance | How to Look Thinner : Fashion Tricks for Plus Size Women | 0.49M | 19.6x | t |
| 28 | Elegance Feed | Make ANY outfit work for your body shape | 0.49M | 12.0x | i |
| 29 | Elegance At 60 | How to Dress a Short Plus-Size Body - Petite & Plus Size Wom | 0.47M | 29.5x | lf |
| 30 | Desi Rich | How To Dress For Your BODY TYPE (Real Examples That Actually | 0.46M | 8.0x | i |
| 31 | Chic After 60 | 7 Style Tips for Petite Women 60 and Over | 0.46M | 64.4x | t |
| 32 | Jules Beth | You DON'T Know Your FULL Body Type: Improve Your Style with  | 0.45M | 50.5x | di |
| 33 | Annie Parker Confidential by Shelli Pelly | 10 Petite Style Secrets That’ll Change Everything | 0.42M | 67.5x | sf |
| 34 | Beauty Theory | How to ACTUALLY get an hourglass figure at ANY SHAPE | 0.41M | 8.3x | d |
| 35 | Glamrs | How To Pick The Right Dress For Your Body Type | 0.41M | 24.6x | s |
| 36 | The Lifestyle Cog | The Ultimate Guide to Finding Office Pants for YOUR Body Typ | 0.38M | 5.9x | li |
| 37 | Lucrative Elegance | AGING COLORS: How to Avoid and Choose Flattering Shades Afte | 0.37M | 65.7x | t |
| 38 | Elegance At 60 | 15 Summer Style Mistakes for Women with a Large Tummy, Apple | 0.36M | 22.6x | lfd |
| 39 | Ishita Saluja Image Consultancy | Find Your Perfect Fit // Body Shape Guide // Ishita Saluja | 0.34M | 18.1x | di |
| 40 | Fashion & Elegance 50 | 7 GENIUS Styling Hacks to Look 10x More EXPENSIVE Over 50 –  | 0.34M | 39.3x | t |
| 41 | The Essence Of Elegance | 7 PETITE STYLE SECRETS That’ll Change Your Life / How to Dre | 0.31M | 12.4x | t |
| 42 | Busbee Style | How To Dress If You Are A Hourglass Body Shape | 0.30M | 3.8x | ia |