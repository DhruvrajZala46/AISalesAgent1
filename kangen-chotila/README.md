# Kangen Chotila - Instagram/YouTube Shorts (Gujarati)

Health and wellness Shorts in Gujarati for a Chotila (Surendranagar, Gujarat) Enagic Kangen distributor page.
This folder lives here only until the project gets its own repository. Text only: media stays in the scratchpad.

## Rules (from the user)
- Business only: no temple or religious content.
- Value first, no selling. Body and health over "water" talk; under 50 seconds.
- Copy proven formats: Hindi/English/Gujarati winners measured against their own channel.
- Male, trustworthy Gujarati voice. Indian/Gujarati faces where footage is used.
- Every claim true and sourced. No disease-cure claims for Kangen (Enagic policy; India's Drugs and Magic
  Remedies Act, enforced since the Supreme Court order of March 2025).

## Research (Nov 2026)
- `research/youtube-ranked-water-health.md`: about 1,500 YouTube videos from 46 Hindi/English/Gujarati searches,
  each scored by views divided by its channel's median. Top relevant winners: Zee News "RO को लेकर WHO की बड़ी
  चेतावनी" (6.0M, ~7,500x), Khan Sir "Celebrity ये पानी क्यों पीते हैं" (4.7M, ~2,600x), "21 दिन इस तरह पानी पियो"
  (6.6M, ~2,200x; 58M on Pro Fit), Khan Sir "RO फिल्टर का पानी पीते हो तो ये जान लो" (~250x).
- `research/youtube-shorts-health-hindi.md`: Shorts under 75 s. Organic health winners: PACE Hospitals
  "क्या किडनी स्टोन के कारण पीठ दर्द होता है?" (1.2M, 36 s), Acharya Balkrishna constipation (820K, 32 s).
- Blocked here: YouTube refuses caption/transcript downloads from this machine ("confirm you're not a bot"), so
  the winners' exact spoken scripts could not be read. Fix: paste transcripts (YouTube "Show transcript"), or
  vidIQ credits (transcript tool; credits refill 12 Dec).

## Scripts
- `scripts/v6-alkaline-explainer-60s.txt`: current, 60 s, for WhatsApp. Modelled on Khan Sir's "सभी Celebrity लोग ये
  पानी क्यों पीते हैं?" (4.7M views, about 2,600x his channel median) and his "RO फिल्टर का पानी पीते हो तो ये जान लो" (he
  explains electrolysis). Copied moves: celebrity hook + "કેમ?", a "સમજો." teaching beat, question-then-answer
  ("લોહીનું pH? સાત પોઇન્ટ ચાર."), simple chemistry with plus/minus plates, then the twist ("ઘરે, વીજળીથી"). It ends on
  a free home pH demo and "call Hardevsinh" (the WhatsApp sender). Facts: blood pH about 7.4; electrolysis gives alkaline
  water at the cathode and acidic water at the anode; Japan's health ministry classes alkaline ionized-water machines as
  household medical devices (Enagic certified 2006); no disease claims. Credits: `scripts/v6-CREDITS.txt`.
- Transcripts: with the user's cookies, `tools/get_scripts.py` (yt-dlp + node JS runtime + `yt-dlp-ejs`) pulls Hindi
  captions slowly. The cookies file stays in the scratchpad and is never committed.
- `scripts/v5-kidney-stone-55s.txt`: kidney-stone version (no urine mention).
- `scripts/v4-kidney-stone-short-50s.txt`: about 50 s. Sources: NIH/NIDDK (fluids are the most important way
  to prevent kidney stones), Foods (MDPI) 2019 review (Gujarat in India's stone belt), NHS urine colour chart,
  Phillips et al. 1984 (thirst falls with age).
- `scripts/v3-health-signals-86s.txt`: earlier, 86 s (four body signals; also Armstrong 2012 UConn 1.5%
  dehydration, Kenefick/UNH cold cuts thirst up to 40%, Parretti 2015 Birmingham water before meals -1.3 kg).

## Tools (`tools/`)
- `yt_research.py`, `yt_medians.py`, `shorts_search.py`: search + channel-median outlier scoring (yt-dlp, flat listings only).
- `mixkit_search.py`: Mixkit free-licence footage search (keeps clips whose -1080.mp4 exists) + contact sheet.
- `tts_gu.py`: Gujarati voice (Microsoft Edge neural `gu-IN-NiranjanNeural`, male) with word timings.
  Needs `SSL_CERT_FILE=/root/.ccr/ca-bundle.crt` here. Spell English initialisms in Gujarati in `beats_tts.txt`.
- `assemble_voice.py`: trims each line, joins with set gaps, writes `beats.json` with per-word times.
- `build_reel_wip.py`: HyperFrames 1080x1920 reel builder (scenes, motion graphics, word-by-word captions).
  Work in progress, written for the v3 script.

## Footage notes
- Mixkit (free licence): water textures only; its "Indian" clips are staged studio shoots.
- Pexels/Pixabay block this machine (Cloudflare); they need an API key.
- Pinterest has real Indian village clips (an elder at a well, an ionizer pouring water) but they are other
  creators' reels: no licence, credit is not permission. Most Pinterest "health" clips (headache, stomach pain)
  are AI-generated and are not used.
- Best long term: film locally in Chotila with consent.
