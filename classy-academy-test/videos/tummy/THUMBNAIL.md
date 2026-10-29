# 7 Elegant Ways to Dress a Tummy (Without Hiding It): thumbnails

Built 29 Oct 2026 with `workflow/4-THUMBNAIL.md`, the `yt-package` skill and the new `tools/thumb_spec.py`.

## 1. The channel's thumbnail DNA (all 31 long uploads looked at full size)

| Part | What every Classy Academy thumbnail does |
|---|---|
| Layout | three real women, edge to edge, in three tall panels with thin light dividers |
| Women | polished and styled, faces in the top third, mostly waist-up; sunglasses, gold jewellery, sleek hair |
| Palette | black, ivory, camel, chocolate; slightly warm, slightly dark grade |
| Places | European streets, bright homes, cafes; never busy or neon |
| Text | top line in Cormorant SC (white), 1-3 big words in Montserrat Bold (white, soft shadow), small Cormorant SC line in `*asterisks*` |
| Underline | a red line under the first big word, **only in the "Elegant Ladies Never..." series** (Never Wear 1.2M, Never Do in Public 505k, Never Wear in Fall, Never Share). The "Look Expensive", "Put Together", "Dress Elegant" and "Color Combos" thumbnails have none. |
| Logo | the CA monogram, top-left |
| Never | arrows, circles, crosses, emoji or bright backgrounds |

Her biggest thumbnails, with their exact words:
- "Elegant Ladies / Never Wear / *avoid these*" (1.2M)
- "How to Look / Expensive / *instantly*" (707k)
- "How To / Dress Elegant" (641k)
- "Always Look / Put Together" (71k)

## 2. The niche (YouTube search, four queries a woman types)

Top results are SuppleChicTV 2.23M, MM Personal Styling 1.86M, Stylish Curves 1.72M, Style with Cathy 1.70M, Petite Dressing 0.87M and 3.13M, and Morah Style Lab 1.28M.
- **The loud ones.** Almost all use red crosses and green ticks, bright backgrounds and capital-letter text ("DONT DO THIS!", "STOP DRESSING FRUMPY").
- **The kind one.** Petite Dressing's "You Don't Need to Hide Your Belly" (874k) is the same promise as our title. Its thumbnail adds a different thought: "Your Tummy is NOT the Problem". That pattern (title = the how, thumbnail = the permission) is the one copied here.
- **Our gap.** In that feed, a calm, elegant three-panel thumbnail with curvy women styled beautifully is the one that looks different (`Preview_feed_test.jpg`).

## 3. The three thumbnails

All three are the channel's own layout, fonts, grade and logo. Each tests a different hook, palette and set of women.

| | 1 (recommended) | 2 | 3 |
|---|---|---|---|
| File | `Thumbnail_1_Stop_Covering_Up.jpg` | `Thumbnail_2_How_to_Look_Expensive.jpg` | `Thumbnail_3_Always_Look_Put_Together.jpg` |
| Words | Stop / **Covering Up** / *style it instead* | How to Look / **Expensive** / *at every size* | Always Look / **Put Together** / *at any age* |
| Hook | permission: the viewer covers up; the thumbnail says stop, the title says how | the benefit, in her 707k format | the any-age version our viewers ask for ("models too young / too thin": 39 comments, 1,119 likes, body-shape research) |
| Women | Ashley Graham, Hunter McGrady, Precious Lee | Katie Sturino, three camel looks | Oprah Winfrey, Queen Latifah, Melissa McCarthy |
| Palette | black and ivory, like "Never Wear" | camel and cream, like "Look Expensive This Fall" | beige, black and ivory |
| The styling shown | an open long coat over black, a V-neck with a soft waist, a belted waist | an open camel coat, a wrap coat, a bias slip dress with a knit over the shoulders | three tailored jackets: double-breasted, tuxedo, longline |
| Underline | yes ("Never" series style) | no | no |

`title.py`: 98/100 for all three. The thumbnail and title carry different words. The only warning is the shared mobile cut of the title.

**Why the framing changed.** At her usual crop the big words sit across the women's waists. Each panel is framed a little closer, so the face sits in the top third and the waist and styling show below the text. Every crop was set by hand in `thumb-specs/*.json`.

## 4. Photos (real, checked by eye; no AI)

| Thumb | Woman | Where it was found | Original source |
|---|---|---|---|
| 1 | Ashley Graham | Pinterest repin by @stylemikado ("Ashley Graham street style") | street-style press photo, photographer not named |
| 1 | Hunter McGrady | Pinterest pin from fashionista.com | https://fashionista.com/2020/04/hunter-mcgrady-all-worthy-plus-size-qvc-clothing-line |
| 1 | Precious Lee | Pinterest pin from lofficielusa.com (Christian Siriano NYFW SS22) | https://www.lofficielusa.com/fashion/precious-lee-plus-size-model-nyfw-spring-summer-2022 |
| 2 | Katie Sturino | Pinterest pin from theeverygirl.com | http://theeverygirl.com/my-week-of-outfits-katie-sturino-of-the-12ish/ |
| 2 | Katie Sturino | Pinterest pin from popsugar.com (Stitch Fix collection portrait) | https://www.popsugar.com/node/46889329 |
| 2 | Katie Sturino | Pinterest repin by @ajohnson1179 ("@katiesturino") | her own Instagram, post not traced |
| 3 | Oprah Winfrey | Pinterest pin from @Oprahdaily on Instagram | https://www.instagram.com/p/DWRS-UgAUC1/ |
| 3 | Queen Latifah | Pinterest repin by @Goldenlite99 | Vanity Fair Oscar party red carpet, press photo |
| 3 | Melissa McCarthy | Pinterest repin by @shly76 | event press photo, photographer not named |

**Rights.** These are press and blog photos found on Pinterest, the same way the channel's existing thumbnails were made. None has a licence; the copyright belongs to the photographers and outlets. The women are shown as style examples. Nothing says they appear in the video.

## 5. Files

- **Delivered in chat:** the three 1280x720 JPGs (under 300 KB each), side-by-side previews, and `Thumbnail_source_files.zip`.
- **The zip holds:**
  - each thumbnail as a PNG;
  - an editable SVG with live text (open it in Figma, Illustrator or Inkscape with the two fonts installed);
  - each graded photo panel as a PNG;
  - the darkening layer;
  - the logo;
  - the spec;
  - the fonts.
- **Rebuilding:** `python3 workflow/tools/thumb_spec.py thumb-specs/T1.json`, with the photos in `real/`.
