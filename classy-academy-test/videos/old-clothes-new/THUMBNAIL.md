# 8 Ways to Make Old Clothes Look New Again: thumbnails

Built with the `yt-package` skill (title and thumbnail as one unit), `workflow/4-THUMBNAIL.md`, and the channel's own
tools: `thumb_make.py` (the measured channel layout) and `thumb_xo.py` (same woman, ✗ → ✓). The image files are not committed. They are in the session scratchpad `thumb/`, and they were sent in chat.

## Title (decided with the thumbnail)

**8 Ways to Make Old Clothes Look New Again**. That is 41 characters, scoring 94/100 in `title.py`. It is the exact phrase the topic's videos rank for: Star News Today 2.37M, 5-Minute Crafts 1.68M, Amber Scholl 0.91M.

The working title "...(Without Buying More)" is 64 characters, scores 76/100, and is cut on desktop.

## The proof: 40 topic videos, scored by how far each beat its own channel

**Method.** Ten YouTube searches a woman types, for example "how to make old clothes look new again", "make your clothes look new", "clothing care tips" and "how to restore faded black clothes". Kids' channels, men's channels and craft-hack channels were dropped. Each video's views were divided by the median of its channel's last 60 videos (yt-dlp, 26 Oct 2026). The top 24 thumbnails were looked at by eye (`thumb/winners.jpg`).

| On the thumbnail | Examples (multiple of own channel, views) |
|---|---|
| **The same garment or woman, before ✗ → after ✓** | Just Marina Here, "How to make your faded clothes black again": **330x**, 0.20M (faded black ✗ → black ✓) |
| **Three elegant women side by side + one line** (our layout) | Classy Woman **341x** 0.34M; dear peachie 19x 0.64M; Kelli Cardenal 14x; Classy Academy's own "Look Expensive" thumbnail, 5.9x 0.71M |
| **An older woman** | AnniePicks, Helen Mirren: **241x**, 1.01M |
| A named royal with circles on the garment | Star News Today, Diana: 58x, 2.37M. **Not used**: our rules forbid a famous face in a thumbnail |
| Text-heavy how-to / product shots | Rit Dye 25x, Melissa Maker 91x (her own channel face) |

## The three (YouTube Studio → Thumbnail → Test & compare)

1. **B: recommended.** `B_dont_toss_it.jpg`, **DON'T / TOSS IT / \*bring it back\***. Scores 98/100 and does not repeat the title's words.
   - **Who:** Christie Moeller (@icanstyleu), a woman over 50, from her own reveal.
   - **Before:** at 4.0 s she holds her faded grey jeans (red ✗).
   - **After:** at 28.3 s the same jeans are black again (green ✓). This is our video's point 5 (faded colour, fabric dye).
   - **Why:**
     - it copies the topic's biggest multiple (faded ✗ → black ✓, 330x);
     - it uses the channel's proven rules format (same woman, mistake → fix);
     - it shows a woman over 50 (the 241x pattern, and our viewers' most repeated request).
   - **Look:** caramel backdrop, Montserrat with the red underline, Cormorant SC, CE logo.
   - **Check:** the cut-out edges were checked at 2x.
   - **Honesty note:** she restored the colour with coffee. The thumbnail shows only her before and after, not the method.
2. **A.** `A_throw_it_out.jpg`, **Before You / THROW IT OUT / \*try these 8 first\***. Scores 98/100.
   - **Layout:** the channel's #1 layout, pixel-measured (`thumb_make.py`).
   - **Women:** three real women from our video's reels: a camel wool coat (airing20), a cream dress in her closet (closetaes22) and a cream knit (sweaterwoman30). The faces sit in the top third.
3. **C.** `C_restore_it.jpg`, **Don't Replace It, / RESTORE IT / \*8 elegant ways\***. Scores 98/100.
   - The same layout as A, with other words and other frames: a white top (closetaes15), a cream knit (sweaterwoman30) and a cream dress (closetaes22).
   - A vs C tests the words ("throw it out" against "restore it").

**Feed test** (`thumb/feed_test.jpg`, 320x180, next to six topic winners):
- All three headlines read in one glance.
- B stands out most: the only caramel tile, faces close up, ✗/✓ readable.
- A and C sit beside Classy Academy's own thumbnail and look like the same family.

## Rejected (and why)

- **Pink coat, pilled ✗ → shaved ✓** (depill33): the clip never shows a fully clean result, so a ✓ would overstate it.
- **Beige sweater before/after** (depill45): the difference is invisible at feed size.
- **Commons "Before/After shaving"** (CC BY-SA, licensed): Wikimedia rate-limited this server (HTTP 429), and the only copy that downloaded (500 px) is too small.
- **Camel coat with circles on the buttons** (clothesbrush5): the buttons are too small at feed size, and the frame carries an "M." watermark.
- **Princess of Wales / Diana photos:** famous faces are not allowed in thumbnails (`SOURCES-LOG-TEMPLATE.md`).
- **The "women over 60" Pinterest photos:** most come from content-farm sites (sewmamasew-type, too uniform), which the channel treats as likely AI.
- **Frames with burned-in brand marks** ("SKALL studio", LILYSILK) or a hidden face (whitecoat32 under her hat, 360p).

## Photo credits (description)

`Thumbnail photos: @icanstyleu (Christie Moeller) · @norwegianwool · @bblynnnn (Brooke Justine) · @OfficialKateHutchins · pinned by @craftinaroundbunches`

| Frame | Creator / pinner | Original | Note |
|---|---|---|---|
| dye14 4.0 s, 28.3 s (B) | Christie Moeller @icanstyleu | Pinterest pin (her own reel "How to dye black jeans with coffee!") | her own before/after |
| airing20 2.0 s (A) | Norwegian Wool @norwegianwool | instagram.com/reel/DDLAL6oxqNI | brand reel: the brand owns it |
| closetaes22 9.8 s, 3.8 s (A, C) | Kate Hutchins @OfficialKateHutchins | instagram.com/reel/DYxLjqToPgi | |
| closetaes15 3.6 s (C) | Brooke Justine @bblynnnn | instagram.com/reel/DRaflu1kQNS | |
| sweaterwoman30 2.3 s, 6.8 s (A, C) | pinned by @craftinaroundbunches | a TikTok watermark in the clip: the original is a TikTok creator not yet traced | trace before publishing |

These are frames of Pinterest video pins. Their rights status is **unresolved**, exactly like the clips in the video (SOURCES-LOG.md). Option B depends on one creator, so the most useful single permission to ask for is @icanstyleu's (template: `workflow/ASSET-RESEARCH-GUIDE.md` section 5).
