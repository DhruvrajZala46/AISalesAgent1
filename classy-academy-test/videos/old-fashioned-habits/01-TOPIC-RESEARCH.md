# Topic research and evidence (27 Nov 2026)

## How the data was collected
- **Fresh listings:** the public video lists of 60 niche channels (`.claude/skills/content-idea/channels.json`),
  collected today with `yt-dlp --flat-playlist`. That gives 3,432 long videos from 59 channels; one channel
  failed.
- **The multiple:** every video is scored as a multiple of its own channel's median views (`rank.py`,
  `shapes.py`). A big number on a small channel and a big number on a big channel are judged the same way.
- **Exact numbers:** views, publish date and subscriber count for 22 reference videos were fetched one by one
  from YouTube's public video pages. These are in the table below; raw data is in `research-data/meta.jsonl`.
- **Viewer comments:** the top comments of 3 reference videos (`research-data/comments/`).
- **Search demand:**
  - YouTube autocomplete for 12 seed phrases (`research-data/yt_suggest.json`);
  - Google Trends, YouTube search, last 5 years (`research-data/trends_youtube_5y.csv`). It was refused twice
    (HTTP 429) and worked on the third try.
- **What I could not use:**
  - vidIQ: the account has 0 credits, so there are no absolute search volumes;
  - Wikimedia Commons searches: rate-limited (HTTP 429) during this research.
- **Absolute search volumes are not known.** Google Trends gives relative interest (0-100) only.

## Candidate topics (12)

"Multiple" means views ÷ that channel's median views. "Views/subs" uses the subscriber count shown on the
channel today. "12-mo shape" counts videos in the 59 channels over the last 12 months whose titles match the
topic: how many there are (competition), their median multiple, and how many reached 5x or more.

| # | Topic | Reference video / channel | URL | Views | Published | Subscribers | Views/subs | Evidence of repeated interest | Why it has potential | Competition (12-mo shape) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Always look put together / polished | "How to Always Look Put Together \| Why Some Women Look So Polished", Julianna Lee | https://youtu.be/FHr_OxICTcg | 1,151,081 | 2026-09-25 | 92,500 | 12.44 | Same channel's "Look Polished When You Have No Time" (176,627, 2026-10-02); Old Money Femininity "Why Some Women Look Expensive Even in the Grocery Store" (92,035 on 8,970 subs, 10.26); the video's title is now a YouTube autocomplete suggestion. **Counter-evidence:** Winnie's School "10 Small Habits That Instantly Make You Look MORE Put Together" got 22,758 on 593k subs (0.04). | Highest median multiple of any evergreen shape; low competition | 66 videos, median **1.35x**, 4 at 5x+ from 3 channels |
| 2 | Habits / traits of elegant women | "10 Traits of Classy Women", Patricia Berenzon | https://youtu.be/ZmkyJN0C1UY | 249,181 | 2026-04-20 | 38,900 | 6.41 | Old Money Femininity "9 Habits Of An Elegant Woman" (40,218 on 8,970, 4.48); Woman Of Elegance "10 SIGNS That Show YOU are a CLASSY LADY" (1,570,796, 2023); Jillz Guerin "8 Habits of CLASSY & ELEGANT Women" (816,547 in a search check) | **Widest proof**: winners on many channels | 191 videos, median 1.14x, **24 at 5x+ from 14 channels** |
| 3 | Look expensive on any budget | "How to look good everyday *even on a budget*", Simone Nicole | https://youtu.be/847jgrJUaO4 | 1,811,206 | 2025-05-18 | 589,000 | 3.08 | Top comments ask for exactly this ("you are worth the effort", ironing, posture: 4,100 likes); "look expensive" holds a steady ~11/100 in YouTube Trends for 5 years | Steady search demand; strong emotion in comments | 188 videos, median 0.99x, 11 at 5x+ from 9 channels |
| 4 | Things elegant women never wear | "8 Things Elegant Ladies Never Wear", Classy Academy | https://youtu.be/My7qteRU9k0 | 1,279,491 | 2025-05-28 | 136,000 | 9.41 | Elvira Hartwell "10 CASUAL Pieces Elegant Ladies Over 50 NEVER Wear!" (102,792, 2.25) | The reference creator's own #1 format | 80 videos, median 0.99x, 8 at 5x+ from 5 channels |
| 5 | Styling mistakes / what cheapens a look | "How to Make Your Outfits Better (Avoid These Styling Mistakes!)", Asia Jackson | https://youtu.be/klKVm1FALhs | 7,334,139 | 2023-05-20 | 710,000 | 10.33 | Woman Of Elegance "13 Things that Cheapen your Appearance" (979,299, 2023); The Lifestyle Cog "11 Office Outfit Mistakes" (1,507,217, 2025) | Huge all-time ceiling | 136 videos, median 0.99x, 10 at 5x+ from 5 channels |
| 6 | French dressing rules | "French Dressing Rules EVERYONE Should Learn Once And For ALL", Mademoiselle Spends | https://youtu.be/DHpCvqbY2ho | 1,867,170 | 2024-08-18 | 207,000 | 9.02 | Chic After 60 "French Women Get More Beautiful With Age" (320,350, 2026-10-03) | The "rules" format plus a strong theme | 67 videos, median 1.04x, 10 at 5x+ from 6 channels |
| 7 | Elegant shoes for women who hate heels | "10 Elegant Shoes For Women Who HATE Heels!", Mademoiselle Spends | https://youtu.be/zdel9jsxTH8 | 668,855 | 2026-09-19 | 207,000 | 3.23 | Chic After 60, same title, 2 days later (266,943, 2.22) | A concrete product list | 61 videos, median 1.10x, 9 at 5x+ from 6 channels |
| 8 | Jewelry rules | "Jewelry Rules for Women Over 60 That Actually Work", Chic After 60 | https://youtu.be/G4ao9SYVrDw | 177,202 | 2026-10-10 | 120,000 | 1.48 | Only 2 videos at 5x+ | Narrow | 17 videos, median 0.92x |
| 9 | Season trends (fall 2026) | "Fall Fashion 2026 \| 15 Classy Trends", Classy Over 40 | https://youtu.be/Cz68Rx4CJUE | 212,922 | 2026-08-18 | 32,400 | 6.57 | Ciara O Doherty autumn trends 14.3x | **Not evergreen**: dated by next season | 162 videos, median 1.36x, 15 at 5x+ from 9 channels |
| 10 | Dressing over 60 (casual pieces) | "How to Wear LEGGINGS Over 60 Without Looking Sloppy", Chic After 60 | https://youtu.be/h6Y1RZzOlzg | 1,526,005 | 2026-10-20 | 120,000 | 12.72 | One channel only | A single-channel spike | 8 videos, median 0.76x |
| 11 | Capsule / pieces you need | "You Only Need These 45 Pieces in Your Wardrobe", Self Guide | https://youtu.be/uzjYzPmi6Fo | 868,148 | 2026-01-31 | 268,000 | 3.24 | "capsule wardrobe" is the strongest YouTube search term tested (Trends 30/100 in 2026). But Self Guide is a men's channel, so off-lane for us | Search demand | 135 videos, median 1.12x, 9 at 5x+ from 8 channels |
| 12 | Elegant etiquette rules | "10 NEW Modern Etiquette Rules Every Polished Woman Knows", Annie Parker | https://youtu.be/5eMw4zn9mSE | 75,000 (listing, rounded) | ~2026-10 (listing) | n/a | n/a | Julianna Lee etiquette video 11.0x; Intentional Woman "9 Old-Fashioned Dating Rules" 3.6x | The "rules" angle | small sample |

**Search demand (Google Trends, YouTube search, yearly average, relative 0-100 across the 5 terms):**

| Term | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|
| look put together | 1.8 | 1.8 | 1.5 | 1.9 | 2.0 | 2.1 |
| look expensive | 11.2 | 11.6 | 11.0 | 11.4 | 10.8 | 11.3 |
| old money style | 0.8 | 2.2 | 11.5 | 17.5 | 16.3 | 13.3 |
| look elegant | 3.8 | 3.9 | 5.2 | 5.5 | 6.5 | **6.8** (rising every year) |
| capsule wardrobe | 17.8 | 27.3 | 28.8 | 27.3 | 25.4 | 30.2 |

How to read this:
- "look put together" is a small *search* term. That video's breakout came from browse and suggested views,
  not search.
- "look elegant" has grown every year since 2021, so the title should carry "elegant".

## Selected topic

**"7 Old-Fashioned Habits That Still Make a Woman Look Elegant"**

(title.py 94/100 for the 9-habit version. The 7-habit version keeps the same structure and fits 6-7 minutes.)

Why this one, on the evidence:
1. **Format with the widest proof:** a numbered *habits* list. 24 winners at 5x or more on 14 different
   channels in the last 12 months, the broadest of any shape.
2. **Promise with the highest median:** *always looking put together / polished*, the "people who look polished
   do X" promise. Its 12-month median is 1.35x, the highest evergreen median in the lane, with the lowest
   competition (66 videos). The topic's biggest video gained 1,151,081 views in two months on a
   92,500-subscriber channel.
3. **Search word with rising demand:** "elegant" grows every year in YouTube search (Trends 3.8 to 6.8, 2021-2026).
4. **What viewers ask for:** the top comments on the reference videos name the same habits again and again:
   - hair matters more than make-up (593 likes);
   - posture ("GOOD POSTURE!", 4,100 likes);
   - ironing your clothes (592 likes);
   - caring for what you own ("We were taught to always take care of everything we had", on the Old Money
     Femininity video);
   - "This is everything they used to teach at charm school or even a Home Ec class."

   That last comment is the angle: **the habits our grandmothers were taught, which still work.**
5. **Evergreen:** nothing in it dates. It isn't seasonal and isn't a trend list.
6. **Footage that can be used legally:** the angle matches public-domain grooming and etiquette films of the
   1940s-50s (Prelinger Archives) and public-domain classic films. Those are the only legally reusable footage
   of this kind that I can obtain myself (see `SOURCES.csv`).
7. **Not a repeat:** the October video "8 Ways to Always Look Put Together" is a different angle. The new
   script avoids its tips where possible and says where it overlaps (see `03-SCRIPT.md`).

## What the evidence does NOT prove (honest limits)
- **No absolute search volumes.** vidIQ has no credits; Google Trends is relative only.
- **The "old-fashioned / charm school" framing is my hypothesis, not proven.** It is supported by one viewer
  comment and by the "rules" titles that work (Mademoiselle Spends 9.02 views/subs; Intentional Woman
  "Old-Fashioned Dating Rules" 3.6x). No proven outlier uses exactly this angle.
- **Counter-evidence:**
  - a "put together habits" video from Winnie's School of Excellence flopped (0.04 views/subs);
  - on the reference creator's own channel, habits videos have a median of 0.9x (`fit.py`).

  The topic is strong in the niche, not a guaranteed hit.
- **Dates in the listing-based multiples are month-accurate.** The 22 reference rows above use exact dates.
