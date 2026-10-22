# Thumbnail photos, v3: "8 Things That Make You Look Older: What to Wear Instead" (22 Oct 2026)

**The brief:** replace the photos you disliked. Keep the three concepts, their text and their layout (`THUMBNAIL-RESEARCH.md`).

**The result:**
- Three finished 1280×720 thumbnails. Every photo is a real photograph from Unsplash or Pexels, free for commercial use.
- I opened each photo's library page and read its licence. Each one was checked at full size by eye.
- There are also two extra versions: an alternative B without an older woman, and a paid-photo preview built from iStock/Getty watermarked comps.
- **Nothing was bought, and nobody was contacted.**

**Files, sent in the chat** (media is not in git; how to rebuild them is in the last section):

| File | What it is |
|---|---|
| `CA_LookOlder_A_details.jpg` | **A**: Details That Make You / **Look Older** / \*wear this instead\* |
| `CA_LookOlder_B_younger.jpg` | **B**: How to Look / **Younger** / \*at any age\* |
| `CA_LookOlder_C_never-dated.jpg` | **C**: Elegant Ladies / **Never Look Dated** / \*what to wear instead\* (red rule under "Never") |
| `CA_LookOlder_B_younger_ALT-no-older-woman.jpg` | B with a woman in her 20s instead of the woman of about 55 (see section 3) |
| `CA_LookOlder_ABC_sheet.jpg` | A, B and C stacked |
| `feed_test_mobile.jpg` | A, B and C at phone-feed size beside your 1.25M, 951k and 698k thumbnails |
| `candidates_free_ranked.jpg` | the 18 free candidates, ranked and labelled |
| `candidates_paid_ranked.jpg` | the 9 paid iStock/Getty candidates, with prices |
| `PREVIEW_paid_sheet.jpg` | A, B and C with the paid photos. **Preview only:** the comps are watermarked and not licensed. |

## 1. What your channel's photos look like (from your 30 thumbnails, 90 photo panels)

Source: every panel of all 30 thumbnails, looked at by eye (`pkg/dna/panels_top8.jpg`, `own_1…5.jpg`), plus pixel measurements.

| | What recurs (strongest in the top 8: 1.25M, 951k, 698k, 637k, 498k…) |
|---|---|
| **Who** | Women in their 20s–40s, polished and groomed. A woman of colour in most thumbnails. **No grey-haired or older woman in any of the 30**; Kate Middleton is the oldest. |
| **Hair** | Sleek buns and sleek ponytails (about 40% of the top-6 panels), or glossy blow-outs. |
| **Make-up** | Soft glam: defined brows, glowing skin, lip colour. |
| **Jewellery** | Gold that shows: sculptural earrings, hoops, rings, watches, bracelets. |
| **Clothes** | Black, ivory, cream and camel. Tailoring, knits, white shirts, halter tops. No loud colour or prints. |
| **Pose and expression** | Calm: a hand at the face or in the hair, eyes closed, a profile, looking away, a soft smile. Some direct, warm gazes. Never mid-speech, never a selfie. |
| **Angle and crop** | Eye level. Head-to-waist in most panels; full length for outfit topics. The woman fills her panel. |
| **Face position** (measured) | Face centre at y≈163 of 720 (middle half 138–192); the face is about 21% of the panel height. In the centre panel the eyes sit above the top line (y≈193). |
| **Light and colour** (measured over all 30) | Brightness median 111 (middle half 95–123); warm (R–B +22); saturation 74 (64–88). Warm golden or soft daylight; luminous. |
| **Setting** | Paris or European street, café, candlelit room, car, stone wall, neutral wall. Clean, softly blurred. |
| **Subject** | The photos show the video's topic (hair for hair videos, outfits for outfit videos). The women are always the elegant "after", never a "before". |

**What the rejected sets got wrong:**
- v1 was moody and dark: profiles, rain, harsh light.
- v2 used video frames, home selfies and mostly older women, all darkened in the middle.

## 2. The three finished thumbnails, panel by panel

The layout and text are unchanged from v2: the same `thumb_ce.py` template, logo, fonts, sizes and red rule. Each panel's crop was set so the eyes clear the text lines (checked on every panel).

Measured, against your 30 (brightness 95–123, warmth +19 to +32, saturation 64–88):

| | Brightness | Warmth | Saturation |
|---|---:|---:|---:|
| A | 100 | +31 | 97 (the glasses panel's golden light) |
| B | 120 | +30 | 83 |
| C | 117 | +28 | 72 |

### A. "Details That Make You / Look Older / \*wear this instead\*"

The three details the hook names: where a hem stops, the colour closest to your face, and your frames.

| Panel | Photo | Why it matches your channel | Topic fit |
|---|---|---|---|
| Left | The AW Creative, Unsplash (#5) | European columns, ivory top, a calm lean against the stone; full length like your outfit panels | **The hem:** a cognac midi that ends just below the knee, worn with a light sandal |
| Centre | Elist Nguyen, Unsplash (#1) | Sleek low bun, flower-pearl earring, red lip, a smile over the shoulder, classic facade | **Colour at the face:** ivory at the neckline, lighting her face |
| Right | yan kolesnyk, Unsplash (#3) | Both hands in her hair tying a sleek bun, pearl drop earring, golden lamp light (your 1.25M's hands-in-hair pose) | **The frames:** thin metal frames whose top line follows the brows |

### B. "How to Look / Younger / \*at any age\*"

Three women glowing in light colours, at three different ages.

| Panel | Photo | Why it matches | Topic fit |
|---|---|---|---|
| Left | Tamara Bellis, Unsplash (#7) | Ivory knit, pearl hair clips and drop earrings, a soft smile over the shoulder | Light colour at the face; late 20s |
| Centre | Eko Agalarov, Pexels (#8) | Eyes closed, hand in her curls, gold earrings and chains, camel and rust (your eyes-closed / hand-in-hair pose) | Woman of colour; glowing |
| Right | Darina Belonogova, Pexels (#9) | Polished and joyful: platinum crop, thin round gold frames, beige suit over ivory, hand to chin | "At any age": about 50–55 |

**Choose between B and B-ALT.** Your 30 thumbnails show no older woman, and the older-women-only "at any age" thumbnail on Put Together got 3.0% CTR (LEARNINGS).
- **B (one woman of about 55):** keeps the "at any age" promise honest.
- **B-ALT:** replaces her with Maria Orlova's ivory-blouse portrait (#10). It matches your DNA exactly, but all three women are under 30.

### C. "Elegant Ladies / Never Look Dated / \*what to wear instead\*"

Three modern outfits from the script.

| Panel | Photo | Why it matches | Topic fit |
|---|---|---|---|
| Left | Leeloo The First, Pexels (#6) | Sleek dark hair, red lip, gold earring, a stone street | Black blazer over a white shirt |
| Centre | Lokman Sevim, Pexels (#4) | Black fedora (your 1.25M has a hat woman), glossy waves, a classic facade | Camel coat over black |
| Right | Masoud Razeghi, Unsplash (#2) | Sleek high ponytail, hand to chin, gold earring and bangle, warm glow | The crisp white shirt |

**Women of colour:** one in B. In A and C, two of the women look East or South-East Asian or of mixed heritage. Pexels McFollis (#12), a Black woman in gold earrings and a black blazer, was the closest look to your channel, but her 4:5 close-up puts the headline across her mouth in a tall panel. I tried her in C and in B and left her out.

## 3. All candidates, ranked

Full records (page, image file, photographer, licence, size, crop) are in `edit/thumbnails/photos_v3.json`.

### Free to use (cleared): 18 candidates

**How they were checked:**
- **Licence:** I opened every library page with the web reader and read its licence there. Every Unsplash page says "Free to use under the Unsplash License", not Unsplash+.
- **Files:**
  - Unsplash photos came from images.unsplash.com at 3000 px wide.
  - Pexels photos came from images.pexels.com at 2400 px wide. Originals are larger where the page lists them.
  - The six Unsplash photos found through Pinterest were re-downloaded from Unsplash. They match the pin copies pixel for pixel (mean difference about 1 level in 255).

| # | Used | Photographer, library | Photo page | Size | Crop in a 9:16 panel | Look |
|---|---|---|---|---|---|---|
| 1 | A-centre | Elist Nguyen (@hieuanhcauam), Unsplash | https://unsplash.com/photos/gPc7zFdSADA | 3000×4500 | face high; head to waist | sleek bun, pearl earring, ivory coat, smile, facade |
| 2 | C-right | Masoud Razeghi (@masud_razeghi), Unsplash | https://unsplash.com/photos/AfWz2PVA3z8 | 3000×3925 | close portrait, hair-top trimmed | ponytail, hand to chin, gold, white shirt |
| 3 | A-right | yan kolesnyk (@kolesnykyan), Unsplash | https://unsplash.com/photos/oG3IJtQgtmk | 3000×4500 | close crop so the eyes clear the text; colour toned down | thin frames, hands in hair, golden light |
| 4 | C-centre | Lokman Sevim, Pexels | https://www.pexels.com/photo/woman-in-camel-coat-and-fedora-hat-16144965/ | 3966×5949 | three-quarter length | camel coat, black fedora, stone street |
| 5 | A-left | The AW Creative Digital Marketing, Unsplash | https://unsplash.com/photos/yy2BPHT8U94 | 3000×4499 | full length, hem and shoes in frame | cognac midi, ivory top, columns |
| 6 | C-left | Leeloo The First, Pexels | https://www.pexels.com/photo/a-woman-in-black-blazer-while-leaning-5900573/ | 4016×6016 | head to waist | black blazer, white shirt, red lip |
| 7 | B-left | Tamara Bellis, Unsplash | https://unsplash.com/photos/FKk__o6c-tw | 3000×4512 | head to waist | ivory knit, pearls, smile |
| 8 | B-centre | Eko Agalarov, Pexels | https://www.pexels.com/photo/stylish-woman-relaxing-outdoors-in-autumn-fashion-29946756/ | 2400×3593 | face at the top | eyes closed, hand in curls, gold |
| 9 | B-right | Darina Belonogova, Pexels | https://www.pexels.com/photo/photo-of-a-business-woman-smiling-while-posing-with-her-hand-on-her-chin-7959665/ | 2333×3500 | face in the top third | about 55, gold frames, beige suit, smile |
| 10 | B-ALT | Maria Orlova, Pexels | https://www.pexels.com/photo/sensitive-contemplative-elegant-woman-on-beige-background-4906281/ | 2400×3194 | close portrait | ivory blouse, freckles, looking away |
| 11 | spare | Vitaly Gorbachev, Pexels | https://www.pexels.com/photo/elegant-woman-wearing-beret-and-eyeglasses-14436117/ | 2400×3600 | face mid-frame, so "You" crosses the lenses | gold round frames, beret, gold chain, trench |
| 12 | spare | McFollis, Pexels | https://www.pexels.com/photo/elegant-black-woman-in-fashionable-earrings-38581716/ | 4480×5600 | 4:5: headline crosses her mouth | gold earrings, black blazer, hand to ear |
| 13 | spare | Marcin Sajur (@m_sajur), Unsplash | https://unsplash.com/photos/-0lduz3NTQI | 3000×4500 | good | sleek top bun, cat-eye sunglasses, black coat; cool grey background |
| 14 | spare | Adetola Salako (@adetolas), Unsplash | https://unsplash.com/photos/pbA11BeCJ9g | 3000×4494 | crop at the waist (bare legs) | black blazer, hand to chin |
| 15 | spare | Olga Zhuravleva (@zabegina), Unsplash | https://unsplash.com/photos/A3MleA0jtoE | 3000×4000 | full length, studio | black tuxedo suit |
| 16 | spare | Raamin ka, Unsplash | https://unsplash.com/photos/uR51HXLO7G0 | 3000×3750 | dark studio | white off-shoulder ruffle |
| 17 | spare | Jonaorle, Pexels | https://www.pexels.com/photo/woman-in-black-turtleneck-sweater-with-blonde-hair-3828245/ | 2400×3600 | good | hands in hair, black knit; no jewellery |
| 18 | spare (borderline) | Brock Wegner (@isthatbrock), Unsplash | https://unsplash.com/photos/zWOPIzzzltk | 3000×4498 | good | golden light, stone; strapless, no jewellery |

**Ranking:** by how closely the photo matches your channel's photos (section 1), then topic fit, then how well it crops into a panel under your text.

**Licence restrictions for all 18:**
- **Unsplash Licence** (https://unsplash.com/license): free commercial use; attribution optional. The images cannot be sold without significant modification, or compiled into a competing service.
- **Pexels Licence** (https://www.pexels.com/license/): free; attribution optional. "Identifiable people may not appear in a bad light or in a way that is offensive". Do not imply endorsement. Do not resell unaltered copies.

### Paid, royalty-free and model-released: 9 ranked candidates (from 17 found)

**Nothing bought.** These are iStock Standard Licence images: commercial use is allowed, including social media and advertising. Each carries iStock's "Non-AI" label.

| Rank | Panel | iStock / Getty ID | Credit | Price shown | Look |
|---|---|---|---|---|---|
| P1 | A-left | istock-1073221492 | janiecbros | $33 (Premium) | ivory pleated midi, white fedora, stone arcade, golden light |
| P2 | A-centre | istock-1492372153 | Liudmila Chernetska | $12 | sleek bun, sculptural gold earring, camel knit, hand to face |
| P3 | A-right | istock-943104058 | puhhha | $12 | thin half-rim frames on the brow line, camel blazer |
| P4 | B-left | istock-1309569610 | alexandr_1958 | $12 | cream turtleneck, golden backlight |
| P5 | B-centre | istock-2187102448 | LightFieldStudios | $12 | sleek bun with a gold pin, ivory halter, profile |
| P6 | B-right | istock-2172634020 | Szepy | $12 | about 40, ivory turtleneck, smiling by a window |
| P7 | C-left | getty-1386257547 | Victor Dyomin | not shown (Getty page showed a bot check, not bypassed) | black belted suit, cobbled street |
| P8 | C-centre | istock-1362713839 | A_Columbo | $12 | camel coat over ivory, stone steps, Black woman |
| P9 | C-right | istock-2263859063 | LightFieldStudios | $12 | about 50, ivory cardigan, pearls, camel trousers |

- **Price:** P1–P9 (without the Getty photo) cost about $117 on credit packs. iStock also lists "any 10 images for $70/month", a subscription; I could not see whether it covers Premium files like P1.
- **Other paid candidates found:** 8 more, in `ph/cand/STOCK/records.json`:
  - istock-2173866514, 928208974, 2160117478, 908005082, 2290148076, 2172634012, 1220749672;
  - getty-1386239606.
- **Pages:** all are in `photos_v3.json` ("paid").

### Reference only: not usable (no licence)

Found through Pinterest; kept only as a guide to the look.
- **REF-01:** tortoiseshell frames, camel blazer, eyes closed. Uploaded by @albeephoto. The ideal A-right look.
- **REF-02:** oval frames, black blazer, sleek bun. Uploaded by @pusovskaua.
- **REF-03:** Paris café, ivory polka-dot midi. The pin's Unsplash link describes a different photo, so its source is unverified.
- **REF-04:** an Instagram reel by @byandykopecky.
- **REF-05:** an unidentified brand's lookbook.
- **REF-06:** Instagram @auror_avogue; AI not ruled out.

Giving credit would not make any of them usable.

## 4. Source and licence manifest (the 9 photos in A, B and C)

| Thumb | Photo page | File used (CDN) | Photographer | Licence | Model release | AI check |
|---|---|---|---|---|---|---|
| A-left | https://unsplash.com/photos/yy2BPHT8U94 | images.unsplash.com/photo-1618244942912-7351be026e8b | The AW Creative Digital Marketing | Unsplash Licence | not provided by Unsplash | full-size face crop: natural skin, real pearl earrings |
| A-centre | https://unsplash.com/photos/gPc7zFdSADA | images.unsplash.com/photo-1775794181051-1f2afd17fcfb | Elist Nguyen | Unsplash Licence | not provided | page lists the camera (Canon EOS R6); skin texture, consistent earring |
| A-right | https://unsplash.com/photos/oG3IJtQgtmk | images.unsplash.com/photo-1770533979411-c43f6ba1d383 | yan kolesnyk | Unsplash Licence | not provided | page lists the camera (Fujifilm X-T5); four more frames of the same shoot are on Unsplash (feZNn4N7y-o, ACFgp7YA4Ck, -kG4UiU2JEs, TjG5pFRW-10) |
| B-left | https://unsplash.com/photos/FKk__o6c-tw | images.unsplash.com/photo-1578220438799-c0ba9b9d78a4 | Tamara Bellis | Unsplash Licence | not provided | uploaded Jan 2020 (from its file ID); real hair flyaways, pearl clips consistent |
| B-centre | https://www.pexels.com/photo/stylish-woman-relaxing-outdoors-in-autumn-fashion-29946756/ | images.pexels.com/photos/29946756/pexels-photo-29946756.jpeg | Eko Agalarov | Pexels Licence | not provided by Pexels | hands, chains and earrings consistent at full size |
| B-right | https://www.pexels.com/photo/photo-of-a-business-woman-smiling-while-posing-with-her-hand-on-her-chin-7959665/ | images.pexels.com/photos/7959665/pexels-photo-7959665.jpeg | Darina Belonogova | Pexels Licence | not provided | natural teeth, skin and hands at full size |
| C-left | https://www.pexels.com/photo/a-woman-in-black-blazer-while-leaning-5900573/ | images.pexels.com/photos/5900573/pexels-photo-5900573.jpeg | Leeloo The First | Pexels Licence | not provided | natural skin and hair at full size |
| C-centre | https://www.pexels.com/photo/woman-in-camel-coat-and-fedora-hat-16144965/ | images.pexels.com/photos/16144965/pexels-photo-16144965.jpeg | Lokman Sevim | Pexels Licence | not provided | film-grain texture, freckles, consistent hat |
| C-right | https://unsplash.com/photos/AfWz2PVA3z8 | images.unsplash.com/photo-1789496950339-77a201c65774 | Masoud Razeghi | Unsplash Licence | not provided | page lists the camera (Canon EOS 5D Mark III); hand, nails and earring consistent |

**What the licences cover, and what they don't:**
- Both licences cover the photographer's copyright for commercial use in a thumbnail, cropped and colour-graded.
- **Neither library supplies model releases.** The women are identifiable.
  - Every photo shows the woman as the elegant "after", never a "before", as your thumbnails always do.
  - Thumbnail A, whose headline reads "Look Older", uses only Unsplash photos.
  - B and C use Pexels photos only under positive headlines. That respects Pexels' "not in a bad light" rule.
- **If you want model-released photos:** the paid set is released. iStock asks for the line "Stock photo. Posed by model." only for uses that could be unflattering.

**Optional credit lines for the description** (not required by either licence; one line per thumbnail):
- A: "Thumbnail photos: The AW Creative, Elist Nguyen and yan kolesnyk on Unsplash."
- B: "Thumbnail photos: Tamara Bellis on Unsplash; Eko Agalarov and Darina Belonogova on Pexels."
- C: "Thumbnail photos: Leeloo The First and Lokman Sevim on Pexels; Masoud Razeghi on Unsplash."

## 5. Recommendation and test plan

**Upload with A.** Then run YouTube's Test & compare with A, B and C, as in `THUMBNAIL-RESEARCH.md` section 7.
- **Why A:**
  - Each photo shows one of the three details the title and hook promise: the hem, the light colour at the face, the thin frames.
  - Its headline is the niche's proven "Look Older".
  - Its photos are all Unsplash.
- **C:** the closest visual twin of your 1.25M "Never Wear" thumbnail (black / camel / white, a hat, European stone, the red rule). It is the one to watch in the test.
- **B (or B-ALT):** the third arm.

YouTube picks the winner by watch-time share, usually within about two weeks. This is a judgement, not a CTR prediction.

**If you prefer the paid look** (`PREVIEW_paid_sheet.jpg`):
- Say which panels to buy. I will not buy anything myself.
- Once you have the licensed files, I rebuild with them in a few minutes, with the same specs.

## 6. How the search was done, and what was blocked

1. **Pinterest** (about 100 searches; a discovery tool only):
   - Most "elegant woman", glasses, blazer and coat pins were AI (Midjourney/Gemini sizes such as 768×1344, 941×1672, 1024×1536).
   - Only pins credited to Unsplash or Pexels led to licensed photos (#5, #7, #8, #10, #11, #14–18).
2. **Unsplash and Pexels, searched directly:** 13 searches through the web reader:
   - Unsplash: camel coat, sleek bun with gold earrings, elegant glasses, black blazer on the street, white shirt, cream sweater, women in their 40s.
   - Pexels: beige, sleek bun with gold earrings, camel coat on the street, eyeglasses, black blazer with a white shirt, mature women.
   - That gave about 120 results on contact sheets, then 24 opened at full size, then #1–4, #6, #9, #12, #13.
   - These sites' bot check blocks direct downloads from this machine. The web reader opened their pages normally, and the image servers serve the files. No bot check was bypassed.
3. **iStock and Getty:** 46 previews were looked at and 17 kept. Prices were read from the iStock pages. The Getty page showed a bot check, which was not bypassed.
4. **Flickr Creative Commons:**
   - Flickr's image server rate-limited this machine (HTTP 429) after the first thumbnails, so no Flickr photo could be viewed.
   - There are 8 unviewed CC0 / CC BY leads (freestocks.org shoots; Garry Knight's London Fashion Week street style, real people with no releases) in `ph/cand/FLICKR/leads_not_viewed.json`. None is used.

## 7. Rebuild

**Specs:** `edit/thumbnails/specs_v3.json`:
- `final`: A, B, C;
- `b_alt`;
- `paid_preview`.

**Command:** `python3 workflow/tools/thumb_ce.py <spec>`

**New renderer options:** `thumb_ce.py` gained `sat` and per-panel `bright`/`sat`.

**Placement and grading:**
- Face boxes were found with `edit/thumbnails/tools/faces.py`, then hand-checked with `facecheck.py`.
- `mkspec.py` builds the specs.
- `measure.py` gives brightness, warmth, centre/edge and saturation.

**Image paths:** they point to the session scratchpad. To rebuild elsewhere, download each photo from the CDN address in section 4 (or `photos_v3.json`) and change the `img` paths.
