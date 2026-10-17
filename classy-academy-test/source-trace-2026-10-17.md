# Where the creator's footage comes from - reverse-image trace (17 Oct 2026)

## Method

1. **Frames.**
   - YouTube storyboard frames (160x90, one every ~5 s) of the creator's videos.
   - For the #1 video, 17 HD frames (1280x720) kept from an earlier session.
   - The clip area was cropped where the frame shows a clip on the backdrop.
2. **Search.** Each frame went to Yandex "search by image", which lists the web pages holding the same or a
   near-identical image. Tool: `workflow/tools/revsearch.py`. The scratchpad version also batch-processes storyboards.
3. **Verification.** A similarity score was computed against each hit's preview. **Then every match was checked by
   eye on review sheets.** The score alone gave false matches on tiny frames: unrelated pages, including adult sites,
   scored 0.9+. Those were discarded and never opened.
4. **Labels** (`workflow/ASSET-RESEARCH-GUIDE.md` section 3):
   - **Confirmed:** the same frame, plus a second source naming the work (a film database, a Blu-ray review, the
     broadcaster's page).
   - **Likely:** the same frame, found only on re-uploads, aggregators or pins.
   - **Similar:** a look-alike only.
   - **Unresolved:** nothing found.

**Coverage.**
- Reference: all footage frames (about 75).
- "10 Microhabits", "7 Habits", "Feminine Energy", "Look Elegant at Home", "Never Share": 14 frames each.
- #1 video: 17 HD frames.

**Limits.**
- 160x90 frames are small, so a famous film still is found easily, while a creator's reel often is not.
- "Unresolved" means "not found by this method", not "original".
- Licence pages were not opened where the site blocks this machine (Pexels shows a Cloudflare check).
- Pinterest's terms restrict automated collection: pin pages were read only through search results, not scraped.

## 1. Reference: "6 Ways to INSTANTLY Sound More Elegant"

| Time | On screen | Source found | Label | Rights status |
|---|---|---|---|---|
| 0:04 | Audrey Hepburn in an orange coat and hat with George Peppard at a shop counter | "Breakfast at Tiffany's" (1961, Paramount), the Tiffany's scene: identical frames on pages naming the film and its trailer | Confirmed (film) | unresolved |
| 0:05-0:10 | woman in a black halter dress at a restaurant table | "Scent of a Woman" (1992, Universal): identical frames on several pages titled with the film | Confirmed (film) | unlicensed studio film: unresolved |
| 0:10-0:15, 0:39-0:49 | Audrey Hepburn, black and white, white headscarf, smiling (title "How to Speak Elegantly" over it) | "Sabrina" (1954, Paramount): the same frame on a "Sabrina Blu-ray" review page and on pins titled "Sabrina 1954" | Confirmed (film) | unresolved |
| 0:15-0:22 | Margot Robbie at a dinner (title over it) | "The Wolf of Wall Street" (2013, Paramount): identical frame on GIF/TikTok pages naming the film | Likely | unresolved |
| 0:30 | three Audrey Hepburn photos | one is a widely pinned black-and-white publicity portrait | Likely | unresolved (some 1950s publicity stills may be public domain in the US; not checked) |
| 0:34-0:39 | Audrey in a large black hat with George Peppard on brownstone steps; her line heard ("I never could do that." "It's easy.") | "Breakfast at Tiffany's" (1961, Paramount), the taxi-whistle scene: identical frame on articles about the film; the dialogue and the whistle (captioned "[screaming]") fit | Confirmed (film) | unresolved |
| 1:04 | woman speaking into a podcast mic, framed | look-alikes only | Similar | unresolved |
| 1:09 | Emma Watson at the UN podium in a white suit, plus a seated woman in white | Emma Watson's HeForShe speech (UN, 2014): the same frame on many quote-image pins | Likely | unresolved (UN footage; terms not checked) |
| 1:14 | restaurant dining room | "Scent of a Woman" (1992): the restaurant/tango room on GIF pages naming the film | Likely | unresolved |
| 1:19 | two women laughing at a restaurant table | **Pexels video 8922355**: identical thumbnail on Pexels search pages | Confirmed (stock) | Pexels License - cleared type (licence page not saved: blocked here) |
| 1:29 | two women at a restaurant table; the woman in black is Monica Bellucci | a Monica Bellucci film scene, identical GIF frames (film not named on the pages) | Likely | unresolved |
| 1:34 | Beyoncé smiling | "The Pink Panther" (2006): identical frames on pins titled "Beyoncé Pink Panther" | Likely | unresolved |
| 1:44-1:54 | Princess Diana at a table, framed, speaking softly, her voice heard ("...we did a group session, and you asked all the ladies...") | the clip circulating as "Princess Diana at a therapy session" (YouTube fan upload F13RyhDd2fw, channel iLovePrincessDiana, 150k views); identical frame pinned as "Princess Diana at Group Therapy session - YouTube" | Likely | unresolved (original broadcaster unknown) |
| 1:44 | Diana laughing in a cream jacket | an event photo, widely pinned | Likely | unresolved |
| 2:03 | an actress speaking softly | The Hollywood Reporter roundtable/cover footage (same face on THR pins) | Likely | unresolved |
| 2:23 | Angelina Jolie in a grey satin top | The Hollywood Reporter Actress Roundtable (2024): identical frame with the THR logo, on re-uploads titled "Actress Roundtable Angelina Jolie, Demi Moore, Zendaya, Zoe Saldaña..." | Likely | unresolved |
| 2:33 | Grace Kelly in the ice-blue chiffon gown, framed | "To Catch a Thief" (1955, Paramount): identical frames on pins naming the film and the Edith Head dress | Confirmed (film) | unresolved |
| 2:38 | collage of four women in conversation | one panel: an event talk featuring Jasmine Tookes (identical pins) | Likely (one panel) | unresolved |
| 2:48 | woman in a cream outfit in a white room | a fashion photo re-pinned many times | Likely | unresolved |
| 3:03 | a man and a woman talking in a garden | a film scene (identical frames pinned; title not identified) | Likely (film) | unresolved |
| 3:08-3:13 | framed: two women seated facing each other in a white studio; "Uh, I'm not sure" -> "Let me think for a second" written beside | a stock-style studio series (Pexels 9065003 is a similar shot from the same kind of set; exact clip not found) | Similar | unresolved |
| 3:18 | framed: three women talking in a hall; "Wait, what?" -> "Say that again" | the same image on a Turkish elegance article (accessland.live, "Sofistike Kadın Olmanın Sessiz İşaretleri") | Likely (copy found; origin unknown) | unresolved |
| 3:23 | framed: two women on a white sofa, interview; "I see what you mean, here's how I see it" | interview set pinned as Rosie Huntington-Whiteley | Likely | unresolved |
| 3:28 | framed: a woman in a burgundy hijab speaking | Sefamerve (Turkish modest-fashion brand) product imagery, same model and set | Likely | unresolved (brand content) |
| 3:38 | Tracee Ellis Ross at a podcast mic | a widely shared podcast clip ("When fear shows up, @TraceeEllisRoss doesn't run from it...") | Likely | unresolved |
| 3:52 | triptych of women on phones, one grey-haired | one panel: pin titled "Sherien Boni on Instagram" (original creator named) | Likely | unresolved |
| 4:07-4:12 | woman in a camel coat texting in a car (principle written over it) | **Pexels video 9520296** | Confirmed (stock) | Pexels License - cleared type |
| 4:17 | hands, phone and white mug; bubble "I'm not sure, let me check" | a stock photo used by many blogs (Pexels candidates 8512141/8512972 not checked by eye) | Likely (stock) | probably cleared type; unverified |
| 4:27 | woman in a sheet face mask texting on a sofa; bubbles "??????" / "HUH" | **Pexels video 6000621** | Confirmed (stock) | Pexels License - cleared type |
| 4:37 | woman at a laptop with coffee, framed | a stock photo series (Pexels 10040704-10040738 candidates, not checked by eye) | Likely (stock) | unverified |
| 4:52 | Angelina Jolie close-up on a train (the 3.13x replay peak) | a film scene; identical frame on pages using Movieclips excerpts; probably "The Tourist" (2010) - the pages do not name it | Likely (film; title not confirmed) | unresolved |
| 5:02 | woman with her head in her hands | - | Similar only | unresolved |
| 5:17 | woman at a desk with a large book | possibly Carine Roitfeld at Vogue Paris (look-alike) | Similar | unresolved |
| 5:22 | framed: curly-haired woman in a beige blazer at a mic; the long nervous reply written beside her (2.2x replay) | a "boundary coach" creator's clip, re-pinned as quote images | Likely | unresolved (creator clip) |
| 5:27 | collage: two women dining with wine | a stock-style photo used by many restaurant sites | Likely (stock) | unverified |
| 5:51 | Gwyneth Paltrow seated in a garden, "Elegant Women ... they don't say yes out of pressure" written over it | Vogue video of Gwyneth Paltrow's kitchen garden in the Hamptons (same frame on Vogue UK / Dailymotion) | Likely | unresolved |
| 6:31 | framed: Amal Clooney seated on stage; "What?" -> "Say that again" | an event photo of Amal Clooney (Cultivate conference), pinned many times | Likely | unresolved |
| 6:26 | framed: two women at a bar | a creator/brand photo, pinned many times | Likely | unresolved |
| 6:36 | Sofía Vergara smiling | TV footage (the judges' desk) | Likely | unresolved |
| 6:41-6:46 | two women with wine on a sofa; "Oh no, it's nothing" -> "Thank you, that's kind of you" | a vertical video pin (blazer/brand video) | Likely | unresolved |
| 7:00 | woman in a cream tweed set reading at a café (guide plug) | a brand's product video pinned as "Two Piece Tweed Set ... Video" | Likely | unresolved |
| other frames (about 15) | interviews, framed women, rows, blurred transitions | not found | Unresolved | unresolved |

**What it adds up to (reference).**
- **Famous film scenes** of iconic actresses carry the hook and the named-woman demonstrations: "Breakfast at
  Tiffany's", "Sabrina", "Scent of a Woman", "The Wolf of Wall Street", "To Catch a Thief", "The Pink Panther", a
  Monica Bellucci film, and an Angelina Jolie film scene (the 3.13x peak).
- **Celebrity interview, speech and event footage** carries "a real woman doing it": Diana, Emma Watson, Angelina
  Jolie (Hollywood Reporter roundtable), Tracee Ellis Ross, Gwyneth Paltrow, Amal Clooney, Sofía Vergara.
- **Pexels stock** carries the everyday actions. It is made specific by written phrases and chat bubbles.
- **Creators' and brands' clips** found as Pinterest pins carry conversations and outfits.

## 2. Other uploads (sampled)

| Video | Time | Source found | Label |
|---|---|---|---|
| "10 Microhabits" | 0:39 | Amal Clooney (title card over her) | Likely |
| | 2:03 | Jessica Alba, seated interview | Likely |
| | 2:57 | Beyoncé, CNN "Anderson Cooper 360" interview, Aug 2012 (identical frame on the CNN page) | Confirmed (programme) |
| | 3:26 | Amal Clooney close-up | Likely |
| | 4:25 | **under the guide plug:** Lindsay Lohan in Esurance's 2015 Super Bowl ad | Likely |
| | 4:55 | "old money couple" creator reel | Likely |
| | 5:34 | woman in a white suit in a doorway (brand image on a marketplace) | Likely |
| "7 Habits That Make You Instantly Classy" | 0:10 | a creator's "Audrey look" reel (big black hat, phone) | Likely |
| | 1:19 | a creator's mirror/make-up reel | Likely |
| | 1:53 | woman in a beige suit by a wardrobe, a TV-series frame | Likely (series not identified) |
| | 2:57 | two women on a sofa with drinks, a TV-series frame | Likely (series not identified) |
| | 3:26 | an older woman at a restaurant: an **Instagram story** (Instagram's interface visible in the pin) | Likely |
| | 4:40 | woman in a tweed jacket in a car: pin titled "**Sherien Boni** on Instagram" (original creator named) | Likely (original named) |
| | 6:13 | Leonardo DiCaprio, "The Wolf of Wall Street" (identical frame on a Blu-ray review) | Confirmed (film) |
| "10 Micro Habits... Feminine Energy" | 0:10 | Marilyn Monroe and Jane Russell, "Gentlemen Prefer Blondes" (1953, 20th Century Fox) | Confirmed (film) |
| | 2:04 | Bella Hadid street photo | Likely |
| | 3:23 | women in polka-dot dresses in a pastel room (creator reel) | Likely |
| "How to Look Elegant & Expensive at Home" | 0:10 | Audrey Hepburn in the sleep mask, "Breakfast at Tiffany's" (1961) | Confirmed (film) |
| | 0:40, 2:28, 2:58 | women in loungewear, knit sets: images found on marketplaces (Wildberries) and pins | Likely (brand/product photos) |
| "7 Things Elegant Ladies Never Share" | 0:39 | woman with a laptop and yellow roses: a business-portrait image used by many sites | Likely |
| | 2:37 | a birthday cake moment: an Instagram video by @therealkarismakapoor | Likely |
| | 3:16 | two women at a café, one drinking from a mug: **Pexels** (identical frame on Pexels search pages) | Confirmed (stock) |
| | 4:15 | two women talking at a table: a stock photo used by many blogs | Likely (stock) |
| | 4:45 | a couple at a candlelit table: a film scene (pages disagree on the title) | Likely (film; title unresolved) |
| | 5:14 | Michelle Obama on stage: a Getty Images editorial photo | Likely |
| | 5:43 | a creator's outfit photo (blue blouse, white trousers) | Likely |
| "8 Things Elegant Ladies Never Wear" (#1) | 0:05 | the opening woman (white shirt, sunglasses): a **Pinterest video pin**, saved on boards named "Footage" and "Gangar References" | Likely |
| | 0:38 | row: a creator's video "Amina ~ vestido asimétrico", a marketplace product photo | Likely |
| | 0:49-0:55 | GUCCI outfits: a 2017 street-style photo (NYFW blog) and pins | Likely |
| | 1:12 | woman in cream: a marketplace product photo (Trendyol listing) | Likely |
| | 1:45 | the seated mirror-selfie series: pin titled "By **@gavanndi**" (original creator named) | Likely (original named) |
| | 2:23 | navy satin gown: a Pinterest video pin | Likely |

## 3. What this proves, and what it does not

**Proved (by identical frames):**
- The channel uses **unlicensed studio film scenes** in at least 5 of the 7 videos checked:
  - "Breakfast at Tiffany's" in 2 of them (twice in the reference);
  - "The Wolf of Wall Street" in 2;
  - also "Sabrina", "Scent of a Woman", "To Catch a Thief", "The Pink Panther", "Gentlemen Prefer Blondes".
- It uses **TV/interview/news footage**: CNN, The Hollywood Reporter, a Super Bowl ad, Vogue, the UN, Diana
  archive.
- It uses **creators' and brands' clips** that circulate as Pinterest pins: two pins name the original Instagram
  creators.
- It uses **Pexels** stock: in the speech video's texting and restaurant moments, and in "Never Share".

**Not proved:**
- **Where she searched.** Every traced clip exists on Pinterest, and Pinterest is consistent with her process, but the
  same clips are also on YouTube, GIF sites and marketplaces. Pinterest as her main source is **[H]**.
- **Whether any of the film/TV clips are licensed** somewhere outside this repository.

**Content ID.**
- Studio films and CNN footage are the kind of material YouTube's Content ID matches.
- Claims on these videos would show in the creator's YouTube Studio ("Copyright" column). We cannot see that from
  here.
