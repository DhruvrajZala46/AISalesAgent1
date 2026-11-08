# 7 Elegant Ways to Dress a Tummy (Without Hiding It) - thumbnails (Classy Academy, 8 Nov 2026)

Built with the `yt-package` skill (title and thumbnail as one unit), `workflow/4-THUMBNAIL.md` (the channel's measured
thumbnail DNA) and the new `tools/thumb_ca_real.py`. Title as given by the user.

## 1. What was studied first (fetched fresh, 8 Nov 2026, maxres, read by eye)

**All 31 Classy Academy thumbnails** (`@ClassyAcademy`, 136k subscribers), at full size. The four closest to this video
(outfit topics) were read at 960x540: "8 Things Elegant Ladies Never Wear" (1.2M), "How to Dress Elegant" (647k), "How to
Dress Casual yet Elegant" (148k), "How to Make Jeans Look Instantly Elegant" (99k).

**The channel's thumbnail DNA, as measured** (and in `4-THUMBNAIL.md`):

| Part | What every CA thumbnail does |
|---|---|
| Photos | 3 real women edge to edge, thin light dividers; full or three-quarter length for outfit topics, faces in the top third |
| Women | polished, attractive, fashion-photo quality; street style and editorial; one hero colour per panel on neutrals |
| Grade | slightly warm, slightly darker, gentle contrast; a soft darkening behind the words; no colour wash |
| Words | Cormorant SC top line ("Elegant Ladies", "How To", "The Most"), Montserrat Bold headline of 2-3 words, a small Cormorant SC line ("\*avoid these\*", "Full Guide", "All Hair Types"); white, soft drop shadow; centred |
| Highlight | a thin red underline under the first headline word, on the 1.2M "Never Wear" |
| Logo | the CA "Classy Academy" logo top-left, at the same place on all 31 |
| Never | arrows, circles, emoji, big ✗/✓, colour boxes, cut-outs, before/after, more than one line of big words |

**The logo:** the old builder (`thumb_ca.py`) drew an approximation of the CA logo. The real one is now extracted from the
31 thumbnails themselves (`tools/ca_logo.py`: the strokes that stay white over 31 different photos) and saved as
`assets/logo_ca.png`; it sits at (33, 26) on a 1280x720 canvas, exactly as on the channel.

**The topic on YouTube** (10 searches, e.g. "how to dress a tummy", "how to dress with a belly", "outfits that flatter a
tummy", "how to dress if you have a belly over 50"; workout and men's videos dropped):

| Views | Channel | Thumbnail |
|---|---|---|
| 3.14M | Petite Dressing, "9 Life Changing Clothing Hacks if you have a Tummy (like me)" | same woman ✗ / ✓ |
| 2.23M | SuppleChicTV, "Worst fashion mistakes 4 tummy" | "DONT DO THIS!", arrows |
| 1.86M | MM Personal Styling, "How to Hide a Larger Stomach" | three outfits on one woman, a label box |
| 1.72M | Stylish Curves, "Do's & Don'ts To Hide A Large Tummy" | ✗ circle, "STOP DRESSING FRUMPY" |
| 1.29M | Morah Style Lab, "Chic Outfits For Large Tummy" | cut-out women, "20 Outfits that Flatter" |
| **879k** | Petite Dressing, "You Don't Need to Hide Your Belly - You Just Need These 7 Styling Hacks" | **"Your Tummy is NOT the Problem"**, ✗ / ✓ |
| 364k | Glow After 60, "7 Dresses That Hide a Tummy After 60" | "ONLY THESE 7 DRESSES HIDES THE BELLY" |
| 353k | Marie-Anne Lecoeur, "How To Hide A Tummy Instantly Over 50" | "how to HIDE YOUR TUMMY", pink, arrow |

What they show: the topic is crowded with loud, cluttered thumbnails (✗ marks, arrows, pink and yellow boxes, "hide",
"look thinner"), and plain grey try-on shots. Only one winner uses the kind angle of this title, the 879k
"Your Tummy is NOT the Problem". So the calm, elegant CA look is the difference in that feed, and the kind angle is
proven once. A before/after with ✗ / ✓ was left out: the channel never uses it, and it would say the "before" body
was wrong, the opposite of this title.

## 2. The three (all 1280x720, the channel's layout, real photos, the real CA logo)

Each is a different visual idea and a different proven word pattern of the channel itself:

| | Words | Women and idea | Copies |
|---|---|---|---|
| **1. Never Hide (recommended)** | Elegant Ladies / **Never Hide** / \*they style it\* | **three different women, three ways of styling a tummy**: Mindy Kaling in a pink check dress gathered at the waist, Precious Lee in a fit-and-flare black dress with a thin belt, Christina Hendricks in a vest, pussy-bow blouse and wide trousers. Three skin tones, three body types, one message | the channel's #1 thumbnail, word for word: "Elegant Ladies / **Never** Wear / \*avoid these\*" (1.2M), with its red underline |
| 2. Flattering Outfits | The Most / **Flattering Outfits** / \*one woman, three looks\* | **one woman, three outfits**: Ashley Graham in a cream wrap coat over cream trousers, a red column dress, a navy suit. Same body each time, so the outfit is the story | the channel's "The Most / Elegant Hairstyles" (965k); "same woman, several outfits" won 55x its channel's median in our body-shape research (`../body-shape/THUMBNAIL.md`) |
| 3. Not the Problem | Your Tummy Is / **Not the Problem** / \*it's how you style it\* | **closer and warmer, faces first**: Precious Lee in a red ribbed dress crossed at the waist (Balmain, Paris), Mindy Kaling in black with embroidered side panels, Christina Hendricks in a black coat over a mustard turtleneck | the topic's only kind winner, "Your Tummy is NOT the Problem" (Petite Dressing, 879k), in the channel's layout instead of ✗ / ✓ |

- **Title and thumbnail together** (`yt-package/title.py`, all three 98/100, "thumbnail and title carry different
  words"): the title gives the number and the topic ("7 Elegant Ways to Dress a Tummy"); the thumbnails add what it
  does not say: *who* does it (1), *what it looks like* (2), or *a kind reframe* (3). None uses "tummy" twice; 1 and 3
  carry the title's spirit ("without hiding it") in other words.
- **Kind to the body:** every woman is shown dressed well and confident, none is marked as a mistake, no "hide",
  "slim", "thinner" or "flat" anywhere; the words promise styling, which the video teaches, not a body change.
- **Side by side with the channel** (`preview_vs_channel.jpg`, next to six CA thumbnails at feed size, and
  `preview_phone_size.jpg` at 168x94): same panels, grade, fonts, sizes and logo; the headline reads in one glance at
  phone size on all three; the faces stay clear. 1 has the biggest headline (2 words, cap 108, the 1.2M's exact size);
  2 and 3 scale down to 82-84 to fit, like the channel's "Casual & Classy" and "Elegant Hairstyles".
- **Sharpness:** 1.10 to 3.78 source pixels per output pixel; nothing is enlarged.

**Which one:** there is no click data for this video, so this is a design call, not a CTR fact. **1** is the closest
to the channel (its #1 thumbnail's exact words, layout and underline) and the clearest at phone size (2 short words,
the biggest type); three different women also tell every viewer "this is for me". **3** is the most curious
(it contradicts what the viewer expects) and complements the title best. **2** is the calmest and most fashion-led.
Upload all three to YouTube Studio → Thumbnail → **Test & compare** and let the watch-time result decide.

## 3. Photos (all real, Pinterest originals; checked by eye at full size and scanned for the AI sparkle)

| Thumb | Woman | Source (as found on Pinterest) |
|---|---|---|
| 1 | Mindy Kaling (Lela Rose pink check dress) | whowhatwear.co.uk, pin by @fabuloushabits https://www.pinterest.com/pin/e1_AfqPShyKr9_tccF3fX9GxKudt4I4iEKjjQWqPWwBW21jsT97oUEb/ |
| 1 | Precious Lee (Christian Siriano, NYFW SS22) | lofficielusa.com, pin by @jaygeeoh https://www.pinterest.com/pin/e1_AfqPShyPG1RScRR6eRX1qOgQ2CDuUijRyRN3xkABymHfGOtf3HZS/ |
| 1 | Christina Hendricks (street style) | pin by @martabrunibf https://www.pinterest.com/pin/e1_AfqPShzVO4Y1zwfAl0DVbI4nA9SPxmVBrfeVNTCfAdCMplWRQ7pC/ |
| 2 | Ashley Graham (cream coat, studio) | pin by @jaygeeoh https://www.pinterest.com/pin/e1_AfqPShz53ZBtSbIAS4cy7B9D4S44FM8Ts5ydVyFmo7A0EOdnCRDP/ |
| 2 | Ashley Graham (red dress, Paris) | instyle.com, pin by @fredhaag34 https://www.pinterest.com/pin/e1_AfqPShyTi3wOKC5qI7V5X07ntKWjiD7vzcIGCuskIDMUTLM3kyk5/ |
| 2 | Ashley Graham (navy suit, New York) | pin by @Maholicious1 https://www.pinterest.com/pin/e1_AfqPShxVGDgKTMSsTyBi34nSdoQnbxXPdPh1Cwax2t5xTBiRzZQa/ |
| 3 | Precious Lee (Balmain, Paris) | Balmain's own pin, @balmain https://www.pinterest.com/pin/e1_AfqPShzWIrT30Kpeks9OspfVFjyRrpHp7LWJP3PMioSjWsTmBkO3/ |
| 3 | Mindy Kaling (black embroidered dress) | purewow.com, pin by @helenannskeffington https://www.pinterest.com/pin/e1_AfqPShxOC7j9zx7ZsXVQn5lHqlBVQbaVKYzK595gR2GlIYC0HF2v/ |
| 3 | Christina Hendricks (black coat, mustard knit) | pin by @waitbyttemoonriver https://www.pinterest.com/pin/e1_AfqPShyPyPXnm7wikImQhlJh5Kfipq1gP9iCdSpDYVl3Fy5HUouG/ |

**Left out:** the "midsize / curvy / old money plus size" pins: many look AI-made (the same glossy faces and marble
lobbies again and again) and carry a `sewmamasew.com` watermark; before/after pins with burned-in text and ✗ / ✓; a
Christina Hendricks photo with a photo-agency watermark; red-carpet shots with sponsor walls (tiff, NYDJ, FOX).

**Rights:** press, street-style and editorial photos belong to their photographers and agencies; none is licensed.
This is the same as the channel's own thumbnails; the creator decides before publishing.

## 4. Files

- Finished: `Thumbnail1_Never-Hide`, `Thumbnail2_Flattering-Outfits`, `Thumbnail3_Not-the-Problem` (.jpg and .png,
  1280x720), sent in the chat with `preview_vs_channel.jpg`, `preview_phone_size.jpg` and `preview_side_by_side.jpg`.
- Editable: `Tummy-thumbnails_editable-source.zip`, with six layers per thumbnail (photos, darkening, text shadow, text,
  logo shadow, logo; 1280x720 transparent PNGs), the spec, the builder and the source photos.
- Rebuild: `python3 workflow/tools/thumb_ca_real.py thumb_spec.json` in a folder holding the photos; it reproduces the
  finished files pixel for pixel (checked).
