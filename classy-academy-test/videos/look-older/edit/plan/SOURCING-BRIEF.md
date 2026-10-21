# Sourcing brief: "8 Things That Make You Look Older: What to Wear Instead"

You are sourcing footage for one video of an elegant women's style channel. It is a calm, faceless voice-over over real footage of real women.
Work folder: `/tmp/claude-0/-home-user-AISalesAgent1/73fc3aa5-807d-530d-b865-5c7bcc671679/scratchpad/lo`.
Run every command from that folder (`cd` to it first in each Bash call).
The briefs are in `plan/briefs.json`, one per asset ID. Each has:
- `brief` (what the picture must show);
- `text` (the narration it sits under);
- `kind`: V = video clip, P = photo of a woman, C = product photo to be cut out later;
- `slot`: the frame shape;
- `need_s`: the seconds of clean, usable footage needed from the in-point;
- starter `queries`.

## What the channel's footage looks like (studied from its own videos, frame by frame)

**Mostly:**
- creators' vertical Instagram/TikTok reels of elegant women, found as Pinterest video pins;
- outfit try-ons, walking shots, closet scenes, routines, beauty close-ups.

**Also:**
- product photos, cut out and laid on a caramel or cream background (shoes, trousers);
- famous women in film or red-carpet clips (never named on screen).

**Palette and light:**
- cream, ivory, camel, beige, chocolate, black, navy, white;
- soft daylight; calm, unhurried movement;
- city streets, cafés, bright homes and closets.

**People:**
- women only;
- several ages (for THIS video lean to 40s-70s, with some 30s);
- several skin tones.

The picture must show **exactly** what the narration names, at that moment ("a turned-up cuff" = a cuffed trouser hem, visible).

## Hard rules

1. **Real footage only, never AI.** Reject a candidate if any of these hold:
   - the AI scan (`python3 -I /home/user/AISalesAgent1/classy-academy-test/workflow/tools/aiscan.py <ID> ...`, run from the work folder) scores 0.40 or more;
   - the uploader or board name suggests AI ("ai", "gemini", "midjourney", "ai influencer", "aesthetic ai");
   - the pin description says AI-generated, or is a leftover "Pinterest Description:" template;
   - the source link is an affiliate link (amzn.to, shopstyle collective), or the pin is `#sponsored`;
   - the clip is exactly 5.0 / 6.0 / 8.0 / 10.0 / 15.0 s at 24 fps (look extra hard; reject if anything else is odd);
   - by eye: waxy or airbrushed skin, hair or jewellery or bags that change between frames, impossible hands, studio-perfect light with no reason.

   When in doubt, leave it out.
2. **No generic free-stock sites.** Do not use clips from Pexels, Pixabay, Mixkit, Unsplash, Shutterstock previews or any stock site (check `src_link`/`dom`). The owner forbids them.
3. **No large burned-in captions or titles** across the middle of the frame ("10 chic outfits", "HOW TO STYLE"). Also avoid:
   - big TikTok/Reels logos;
   - split-screen collages;
   - heavy filters;
   - men as the subject;
   - children;
   - lingerie or very revealing clothes;
   - logos as the subject.

   A small creator @handle in a corner is acceptable. Note it.
4. **Quality:**
   - video at least 540 px wide (720x1280 preferred), steady or gently moving;
   - photos at least 600 px on the short side;
   - product photos on a plain white or light background, the whole product visible.
5. **Video slot shapes:**
   - PANEL/CENTRE are vertical (608x1080); a vertical reel is ideal.
   - FULL is 16:9. A vertical reel will be cropped to a 16:9 band, so pick clips whose subject survives a tight crop (close-ups, waist-up), or horizontal clips.
   - PAIR is a near-square.
6. **Do not use the same creator for more than 3 assets across your list,** and avoid creators already used (see `picks/*.json` from other workers when you start).
7. **Be respectful** with every "don't" example (chunky shoes, a mid-calf hem, a pale lip): an ordinary, nice-looking woman, never a mocking or unflattering shot of a person.

## How to work

1. **Search:** `./tools/search.sh tag="query words video"`. It writes `pin/<tag>.json` and a contact sheet `pin/sheet_<tag>.jpg`; look at the sheet with the Read tool.
   - Video pins are marked VIDEO.
   - Add `--images` to see photo pins (for P and C assets): `./tools/search.sh --images tag="query"`.
   - Put the word "video" in video queries.
   - Make tags unique: start them with your asset ID, e.g. `S10a`, `S10b`.
   - Try 2-4 different phrasings per brief before giving up. Wait at least 3 s between searches (the script already sleeps). Never hammer Pinterest.
2. **Download the best candidate:** `python3 -I tools/dl.py <ID> <tag> <index>`. Add `--image` for photos.
   - This writes `raw/<ID>.mp4` or `.jpg` and `picks/<ID>.json`.
   - The script deletes an earlier file of the same ID. To compare two candidates, use IDs like `S10_alt1` and rename later, or just re-download the winner.
3. **Look at it:** `python3 -I tools/look.py pin/look_<ID>.jpg <ID> [more IDs]`, then Read the image. Check:
   - the subject;
   - text overlays;
   - AI tells;
   - where the relevant moment is.
4. **Run the AI scan** on every video you keep.
5. **Choose the in-point.** Pull extra frames with ffmpeg if needed. It must leave at least `need_s` seconds of clean footage that shows the brief:
   - no cut to unrelated content;
   - no caption appearing;
   - no end screen.

   If the clip is shorter, note it (a slower speed like 0.8 is allowed; down to 0.7 is fine for walking shots).
6. **Write your decision INTO `picks/<ID>.json`** (keep the fields dl.py wrote and add these):
   - `in` (seconds), `speed` (1.0 unless needed), `focus` ([x, y] 0-1: the point to keep centred when cropping, e.g. [0.5, 0.35] for a face high in a vertical frame);
   - `ai_scan` (score), `ai_eye` ("checked: no tells" or what you saw);
   - `creator_evidence`: how you know who made it, e.g. "native_creator on the pin", "src_link is instagram.com/reel/... of @x", "watermark @x in frames". Read watermarks in the frames.
   - `original_post`: the creator's own post URL when known;
   - `rights`: write exactly "No licence known; creator permission not requested", unless the source states a licence (then quote it and its URL);
   - `note`: one line on what the clip shows and why it matches the brief.
7. **If nothing acceptable exists after real effort,** write `picks/<ID>.json` with `"gap": true` and what you tried, plus the nearest fallback idea. A gap is better than a wrong or AI picture.

## When you finish

Write `picks/REPORT_<your worker name>.md`:
- one line per asset: ID, chosen file, creator, in-point, verdict;
- the gaps;
- anything doubtful.

Then build one review sheet of all your picks (`tools/look.py pin/final_<worker>.jpg <IDs...>`), look at it once more, and fix anything wrong.

Keep your final message short: the IDs done, gaps, doubts.
