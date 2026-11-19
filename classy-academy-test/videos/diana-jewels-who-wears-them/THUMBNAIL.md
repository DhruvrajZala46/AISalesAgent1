# Princess Diana's 7 Jewels: Who Wears Them Now? - thumbnails (19 Nov 2026)

**No thumbnail can guarantee views.** What the research can do is copy what the winners in this exact lane do, and avoid
what the losers do. In this lane, 14 videos have passed 1M views. The biggest documentary-style ones are "The Crown
Jewels" (5.9M), "Her Life Through Jewels" (5.1M), "Queen Elizabeth II's Tiaras" (2.3M) and "The 15 Most Beautiful Royal
Necklaces" (898,000).

## 1. What was read
- **30 YouTube searches** on Diana's and royal jewels: 1,452 videos. After removing The Crown clips, children's channels
  and tutorials, **433 videos** were left in the lane.
- **Each video was scored against its own channel's usual video** (the latest 60 long videos of each of 161
  channels): 415 videos scored. The usual result was 4.2x; 192 videos reached 5x or more, and 60 were under 1x.
- **Thumbnails read by eye:** the 48 with the most views, the 32 biggest winners against their own channel (all with
  50,000+ views) and 24 random losers (under 0.8x). That is **104 thumbnails**. The lists are in
  `thumb/winners_losers.json`; the searches are in `thumb/youtube_queries.txt`.
- Not available: click-through rates (only in YouTube Studio).

## 2. The patterns (my reading of the 32 winners and 24 losers)

| Pattern | Winners (32) | Losers (24) |
|---|---|---|
| **One jewel, huge (50%+ of the height), glowing on a dark rich background, with one or two famous faces at the edges** | **10**: The 15 Most Beautiful Royal Necklaces (898k, 816x); The 10 Most Expensive Royal Jewelry (126x); Diana's Most Legendary Jewels (790k, 259x); Elizabeth Taylor's jewels (919k, 301x) | 5, all with a large title banner or many small items |
| Tabloid drama: a crying royal, "EXCLUSIVE", a quote in a box | 9 (very high multiples) | 2 |
| Faces or a photo collage with no jewel in focus | 10 | 9 |
| Many small jewels, red circles and arrows, a big title | 1 | 6 |

**Why the winners work:**
1. **The jewel is the hero.** It is the biggest, brightest thing on the screen. The eye lands on it first and
   recognises it at phone size. On losers the jewels are small insets that disappear at 168 pixels wide.
2. **One famous face says whose it was, and a second face says who has it now.** That is the whole "where is it now"
   story, told in a single picture. The faces at the edges look toward the jewel, so the eye travels to it.
3. **Dark, rich backgrounds with a glow behind the stone** (navy, black, red velvet): diamonds and sapphires are only
   bright against dark. Loser thumbnails are often flat, grey or busy.
4. **Few or no words.** The biggest jewel winner (816x) has none. Winners that do use words keep to two or three
   ("NEVER WORN!", "PRICELESS JEWELS"). Losers spell out the title ("PRINCESS DIANA JEWELRY", "TOP 10 JEWELS OF...").
5. **Curiosity, not information.** "Who wears it now?" and "Never worn" open a question; a list of names answers it
   and takes the reason to click away.

**Left out on purpose:** the tabloid drama pattern. Its multiples are high, but the stories are invented ("King
Charles finds a note in Diana's jewelry box") and the pictures are AI-made. It goes against the channel's trust, and the
earlier Diana research found this style has the most failures. **Honest limit:** the jewel formula also appears on 5
losers, so it is not a guarantee. Channel size and the title matter too.

## 3. The three thumbnails (1920x1080, real press photos and real jewellery photos only)

| | What it shows | Words | Why |
|---|---|---|---|
| **A, the one I would bet on** | Diana touching her face, the sapphire ring on her hand; the same ring, huge and glowing in the centre; Catherine smiling, the ring on her hand, in William's arms | none | The exact formula of the biggest winner (816x): one giant jewel between "who had it" and "who has it now". It is the most famous jewel in the world, so it is recognised instantly. It answers the title's question visually and leaves the story open. Dark navy with a blue glow; the faces look toward the ring. |
| B | Diana in the Lover's Knot tiara, the tiara in the centre, Catherine in the same tiara | NOW HERS | The same formula, with a second jewel and two words that make the "who wears it now" twist plain. |
| C | Diana smiling in the centre; her ring, the amethyst cross and the pearl drops glowing around her on dark red | WHERE ARE THEY NOW? | The formula of "Diana's Most Legendary Jewels" (790k, 259x): her face with her jewels laid around her. The words carry the promise. |

**My order: A, then B, then C.** Upload all three in YouTube Studio under "Test & compare".
**Title:** "Princess Diana's 7 Jewels: Who Wears Them Now?". It pairs with A (no words, so nothing is said twice) and
with B ("NOW HERS" adds the twist; it does not repeat the title).

## 4. How they were made
`thumb/build_thumbs.py`: the jewel is cut from a plain-background jeweller photo of the same design; a glow is placed
behind it, plus a soft drop shadow, sharpening and two or three small sparkles. The faces are real press photos,
faded into the background toward the centre; a dark vignette sits at the edges. The text is Montserrat ExtraBold in
warm ivory with a dark outline and shadow. All three were checked at feed size (360 px) and phone size (168 px)
beside the winners.

## 5. Before you use them
- **Rights:** press photos and jeweller photos; none is licensed, as with the earlier thumbnails.
- **The ring in the centre is a jeweller's photo of the same Garrard design**, not the actual ring (no clean photo of
  the real one exists on a plain background). The same is true of the cross (the Sotheby's photo) and of the pearl
  drops.
- **The logo is CA**, as on the earlier thumbnails; it can be switched to CE.
