# gen_docs_charm.py - sources log, credits and chapters for "5 Quiet Habits That Make a Woman Unforgettable" (run after the final build)
import json, os
m = json.load(open('raw/meta.json')); U = json.load(open('used_times.json')); B = json.load(open('beats.json'))
Bd = {d['i']: d for d in B}
CROP = {}; MAXSLOW = {}
exec(open('clips.py').read())
def line_at(t):
    best = B[0]
    for d in B:
        if d['start'] - 0.6 <= t: best = d
    return best
mmss = lambda t: f'{int(t//60)}:{int(t%60):02d}'
# where the picture is true to the idea of the line but not to every word (from eye_notes.txt)
PARTLY = {
 'h2d': 'a couple seen from the back seat at night, no faces (the line: "in the car on the way home")',
 'h4c': 'hands pouring tea: stands for "a little calmer"',
 'h5d': 'a woman painting at an easel: stands for "this can be learned"',
 'a9d': 'a crowd mingling in a hall; no single quick hello in shot',
 'a11c': 'a woman walking away alone down a road (not stepping back from a group)',
 'a12a': 'a family at a garden table (the gathering), nobody walking in',
 'a12c': 'two friends laughing over coffee (the "whole story" is implied)',
 'a14b': 'six friends laughing on a sofa: a group, not "two or three conversations"',
 'b18a': 'close-ups of different women laughing: stands for "then she said something..."',
 'b19a': 'real newsreel of Marilyn talking and laughing; the witty line itself is not heard',
 'b19b': 'real newsreel of Marilyn laughing with an older man; the witty line itself is not heard',
 'b20b': 'Diana bending to children in wheelchairs (1984), not the AIDS or leprosy patients the line means',
 'b20c': 'Diana at a hospital bedside with an elderly woman',
 'b24a': 'two women laughing as they run through a meadow: stands for "say the funny thought"',
 'c28a': 'a woman with roses walking and smiling on her way (not at a door)',
 'c30a': 'two women at a table, one eating, one reading: calm, nobody asking yet',
 'd39a': 'a woman standing at a family table sharing news (not a named Anna)',
 'd40b': 'a woman on a rock, eyes closed, calm: stands for "your shoulders drop"',
 'd40d': 'a woman on a sofa, hand on her chest, breathing: stands for "an ease about you"',
 'e43c': 'a woman scrolling her phone in the dark: stands for "going quiet for three days"',
 'e44b': 'a woman in a blanket with a mug, calm; no screen in shot (the line: a series you love)',
 'e45a': 'a woman playing the piano: stands for "discover them a little at a time"',
 'e47b': 'a mother and daughter laughing on a sofa (the label says "your sister")',
}
ARCHIVE = {'marilynd39', 'marilynd14', 'dianaa12', 'dianaf14', 'dianab4'}
slot_of = {}
for s_, (k, a, b) in C.items(): slot_of.setdefault(k, []).append((s_, a, b))
rows = []
for n, (k, t) in enumerate(sorted(U.items(), key=lambda z: z[1]), 1):
    d = line_at(t); x = m[k]; who = (x.get('creator') or '').replace('|', '/').strip()
    who = f"{who} (@{x['user']})" if x.get('user') else who
    src = x.get('src') or ''; src = src if ('instagram.com' in src or 'tiktok.com' in src) else ''
    txt = d['text'][:60].replace('|', '/') + ('...' if len(d['text']) > 60 else '')
    how = f'Pinterest video pin -> {src}' if src else 'Pinterest video pin (original post not traced)'
    ss = slot_of.get(k, []); win = '; '.join(f'{a:g}-{b:g} s' for _, a, b in ss)
    note = '; '.join(PARTLY[s_] for s_, _, _ in ss if s_ in PARTLY)
    fit = 'PARTLY: ' + note if note else 'matches the line'
    if k in CROP: fit += ' (cropped past a caption or a small watermark)'
    holder = who + (' / ARCHIVE film: the original newsreel or broadcaster owns it' if k in ARCHIVE else '')
    rows.append(f"| {n} | {mmss(t)} | L{d['i']}: {txt} | {k} ({win}) | {holder} | {how} | credited, not licensed | unresolved | {fit} |")
hdr = f"""# SOURCES-LOG - 5 Quiet Habits That Make a Woman Unforgettable (The Classy Elegance, v1, 16 Nov 2026)

One row per clip, in order of appearance: **{len(rows)} video clips**, no photos, no product cut-outs.
- **Where the footage comes from:** Pinterest video pins of Instagram / TikTok creators' reels (the creator's own
  sources), 600 clips downloaded and read from 169 search phrases in two rounds. No free-stock site was used:
  one clip posted by a stock-photo account (rawpixel) was found and thrown out.
- **Each clip appears once.** 108 different clips, each in one window only; the builder refuses any window that
  repeats footage already shown.
- **Duplicate check:** every download hashed at 1 frame per second (`tools/dupall.py`); re-pinned copies of the same
  footage grouped, only one copy of a group may be used; 0 clashes among the used clips.
- **No repeats from earlier videos:** `oldclash.py` (blank and near-black frames ignored, which had chained unrelated
  clips) against the used clips of every earlier video, the French winter video included: 130 downloads repeat earlier
  footage; none is used.
- **AI checks:** the Gemini watermark scan flagged 2 downloads (not used) and 5 pins with a Gemini mark were left out at the
  thumbnail stage; removed by eye: a known AI "persona" account
  (one woman in a white linen shirt across many pins), "podcast girl" clips, a posed snow portrait with added snow.
  Honest limit: a real-looking clip can still be AI. These checks lower the risk; they do not prove a clip is real.
- **Captions, watermarks and stickers:** every candidate was read on time-labelled strips by a first and a second
  screening, every pick again at large size by me (`eye_notes.txt`), every prepared segment at three moments, and the
  finished edit at 121 snapshots. 9 picks were thrown out for burned-in captions or watermarks; {len(CROP)} clips are
  cropped past a caption or a small watermark (the `CROP` list in `clips.py`).
- **Named women:** Marilyn Monroe and Princess Diana are shown only in real archive film (newsreels, 1980s-90s news
  film) found as Pinterest pins; never an actress, never an AI clip. Rejected: The Crown, an "AI clips" pin, animated
  press stills, a clip with a burned-in subtitle.
- **"PARTLY" in the last column is said plainly**: the picture is true to the idea of the line but not to every word.

**Rights status.** Footage: creators' reels found on Pinterest, and archive news film. **None is licensed**: every row
is **unresolved**, and credit is not permission. A copyright claim or YouTube's reused-content rule is a real risk.
The archive film (5 clips) belongs to the original broadcasters. The creator decides before publishing.
Music: "Classical vibes 3" by Grigoriy Nuzhny, Mixkit Stock Music Free License (cleared). No sound effects.

| # | At | Script line | Clip key (seconds used) | Creator / rights holder | How it was found | Licence basis | Decision | Fit to the line |
|---|---|---|---|---|---|---|---|---|
"""
D = '/home/user/AISalesAgent1/classy-academy-test/videos/unforgettable-charm/'
open(D + 'SOURCES-LOG.md', 'w').write(hdr + '\n'.join(rows) + '\n')
handles = []
for k, t in sorted(U.items(), key=lambda z: z[1]):
    h = m[k].get('user')
    if h and '@' + h not in handles: handles.append('@' + h)
open(D + 'CREDITS.txt', 'w').write('VISUAL CREDITS (all footage belongs to its creators, thank you):\n' + ' '.join(handles) +
    '\nArchive film of Marilyn Monroe and Princess Diana: the original newsreels and broadcasters.\n'
    'Music: "Classical vibes 3" by Grigoriy Nuzhny (Mixkit)\n')
secs = [(1, 'Why some women are never forgotten'), (8, '1. Choose where your attention goes'), (16, '2. Let your contrasts show'),
        (26, '3. Make them feel interesting'), (34, 'Your personal stylist guide'), (35, '4. Be calm on the inside'),
        (42, '5. Let them discover you slowly'), (49, 'Charm is a blend, and it is yours')]
out = [(0 if i == 1 else int(Bd[i]['start']), x) for i, x in secs]
total = Bd[len(Bd)]['end'] + 4.2
assert out[0][0] == 0 and min(b[0] - a[0] for a, b in zip(out, out[1:] + [(int(total), '')])) >= 10
open(D + 'CHAPTERS.txt', 'w').write('\n'.join(f'{t//60:02d}:{t%60:02d} {x}' for t, x in out) + '\n')
missing = [s_ for s_ in PARTLY if s_ not in C]
print(len(rows), 'clip rows', len(handles), 'handles; partly notes for missing slots:', missing)
print(sum(1 for r in rows if 'PARTLY' in r), 'rows marked PARTLY'); print(open(D + 'CHAPTERS.txt').read())
