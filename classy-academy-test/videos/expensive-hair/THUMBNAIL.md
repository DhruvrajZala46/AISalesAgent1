# Why Her Hair Always Looks Expensive: thumbnails

Built with the `yt-package` skill and `workflow/4-THUMBNAIL.md`. The title is unchanged: **Why Her Hair Always Looks Expensive (It's Not the Cut)**.

## The proof: 102 hair winners, each scored against its own channel

- **Sources, 19 Oct 2026:**
  - the niche's 60 channels (`content-idea/channels.json`, 12,804 long videos);
  - YouTube's own results for 20 searches a woman types ("how to make your hair look expensive", "old money hair",
    "glossy hair tips", "hair mistakes that make you look older", "elegant hair over 50", ...).
- **Scoring:** every hair video is scored as a multiple of its channel's median. Men's, wigs, kids and off-topic videos were dropped.
- **Kept:** the 102 that beat their channel. Each thumbnail was looked at and tagged by eye.

| On the thumbnail | Niche channels: n / median views / median x | Search: n / median views / median x |
|---|---|---|
| **Glossy-hair close-ups** | 2 / 1.10M / **22.8x** | 4 / 0.90M / **120x** |
| **Same hair, frizzy/dull -> glossy (before -> after, x / tick)** | 6 / 0.20M / 8.2x | 8 / **0.56M** / 17.4x |
| One woman + a few words | 12 / 0.06M / 8.8x | 17 / 0.53M / 27.5x |
| Same woman, several styles | 7 / 0.13M / 4.7x | 7 / 1.79M / 31.1x |
| Line-up of different women | 3 / 0.04M / 6.0x | 10 / 0.34M / 88.9x (mostly AI faces on tiny channels) |
| Big text over a blurred face | 10 / 0.07M / 8.9x (one channel only) | 1 |

**Winners of the format:**
- Beauty Theory "how ANYONE can tame frizzy dry hair": 1.7M, 35x, "BEFORE / AFTER" on the same hair.
- Hang "Why your wavy hair is FRIZZY": 3.47M, 30x, the same woman with x / tick.
- kayli boyle: 2.3M, 13x.
- Glam Girl Gabi: 1.2M, 12x.
- Elena Spati "How I Get My Hair THIS Shiny": 452k, 188x, glossy hair from behind.

**What the lane's winning words say:**
- Lucrative Elegance "YOU'LL NEVER LOOK RICH WITH THIS HAIR": 25x.
- Lucrative Elegance "YOUR HAIR REVEALS YOUR CLASS": 15x.
- Julianna Lee "look clean & expensive": 14x.

**Not copied:** the many AI-face line-ups. We use real women only.

## The three (YouTube Studio -> Thumbnail -> Test & compare)

1. **A (recommended)** `thumb_A_same_haircut.jpg`.
   - **Picture:** one woman's hair from behind, frizzy (cross) -> glossy (tick). It is the same haircut in the same room, so the picture shows
     the title's promise: it's the finish, not the cut.
   - **Words:** "ONE WOMAN, / SAME HAIRCUT / *it's the finish*". `title.py`: 80/100, no repeated title words.
   - **Build:** `tools/thumb_xo.py`, the channel's look (caramel, Montserrat + Cormorant SC, red underline, CE logo).
2. **B** `thumb_B_the_finish.jpg`: the same picture with the answer as the words, "THE SECRET IS / THE FINISH / *same haircut*" (80/100).
   A vs B tests the question ("same haircut?") against the answer.
3. **C** `thumb_C_pure_shine.jpg`: the channel's #1 three-photo format (`tools/thumb_make.py`).
   - **Photos:** three women of different ages and hair types: glossy brunette, silver-haired woman of 76, golden curls.
   - **Words:** "AT ANY AGE, / PURE SHINE / *the haircut can wait*" (80/100).

**Feed test** (`feed_test.jpg`): at 320x180, next to six winners:
- A and B read in one glance;
- the frizzy/glossy contrast is the strongest picture on the sheet;
- the caramel stands apart from the white and grey winners.

C's faces stay clear.

## Photos (real, from the video's own footage, checked)

- **A, B:** @haircarebyleila (Instagram reel DKHyAlZATCo).
  - Her own client before/after: frizzy, matte lengths, then sleek and glossy, in the same room and light.
  - Frames 4.4 s and 9.5 s. The stylist's arm in the second frame is cut away.
  - AI watermark scan: none (all clips scanned for the video).
- **C:**
  - @xmondohair (TikTok 7607880947727355150), frame at 43 s. Their TikTok mark was removed from a plain white area.
  - @lynnezekis (Instagram reel Db6X9GOqR0u, "Here at 76"), 120 s.
  - @wtheeduarda (Instagram reel Db_kc_KOD0Z), 10 s.
- **Permission:** as with the video, no creator has been asked yet. Credit them in the description (`CREDITS.txt`).

## Tools

- The research data and scripts are in the session scratchpad (`thumb/`): `hair_scored.json`, `winners.json`, `tags.json`, `make_c.py`.
- The cut-out uses rembg (isnet-general-use).

**Ship it, or change it?**
