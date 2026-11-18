# gen_docs_loved.py - SOURCES-LOG, CREDITS and CHAPTERS for "7 Things Princess Diana Loved That You Can Still Buy Today"
# Run inside the work folder after the final build:  python3 <this file>
import json, re, os
D = '/home/user/AISalesAgent1/classy-academy-test/videos/diana-things-she-loved/'
m = json.load(open('raw/meta.json')); B = json.load(open('beats.json')); Bd = {d['i']: d for d in B}
H = open('index.html').read()
CROP = {}; MAXSLOW = {}
exec(open('clips.py').read())
mmss = lambda t: f'{int(t//60)}:{int(t%60):02d}'
def line_at(t):
    best = B[0]
    for d in B:
        if d['start'] - 0.6 <= t: best = d
    return best

# ---- where each clip first appears (from the built page) ----
U = {}
for src, st in re.findall(r'<video[^>]*src="assets/(?:[KF]_)?([a-z0-9]+)_[0-9.m]+_[0-9.m]+_[0-9.]+[^"]*\.mp4"[^>]*data-start="([0-9.]+)"', H):
    U.setdefault(src, float(st)); U[src] = min(U[src], float(st))
FILM = {'dlaugh18', 'dsmile20c', 'dbalmoral3', 'deyes9', 'dwed32', 'dwedb10', 'dwed35', 'dlaugh36'}
# where the picture is true to the idea of the line but not to every word (read by eye on frames and snapshots)
PARTLY = {
 'h4a': 'a woman tying a silk scarf: stands for "how she chose"',
 'h6a': 'a woman walking with her handbag: stands for "some are small"',
 'h6b': 'a woman at a flower stall with a tote: stands for "one or two may surprise you"',
 's18a': 'a lilac and cream top folded away, not a patterned jumper; no drawer in shot',
 'e26a2': 'a brown (umber) pencil along the lashes, then a brush starts to smudge',
 'l32b': 'loafers worn with a skirt; a jacket on a chair fills part of the clip',
 't38e': 'a structured black top-handle bag on its own: stands for "jeans in the morning, a dress in the evening"',
 't39a': 'a woman smiling at ease: stands for "free to think about everything else"',
 'b43a': 'a silk scarf laid away in its gift box, not a bag in its dust bag (the box label is cropped out)',
 'b44e': 'silk scarves taken out of a drawer, not a handbag out of the wardrobe',
 'p50a': 'a woman holding a pink perfume bottle to her nose: stands for "the most personal thing a woman wears"',
 'p51a': 'testing perfume at a counter; an Armani Prive sign is visible behind (every perfume-shop clip found shows a brand name)',
 'c54a': 'a woman smiling, close; no phone or comments in shot',
 'c55b': 'a perfume tray in sunlight under the guide line',
 'w10a': 'green wellies and a dog walk; the reel is a country-clothing shop\'s (Bishops & Haig), cut before its logo appears',
 'h5a': 'real film: Diana in a red jacket; the pin gives no date or place (the title is shown over it)',
 'h6c': 'real film: Diana smiling, close, 1990s; the pin gives no date or place (cut out of its black letterbox)',
 'w12a': 'real film: Lady Diana Spencer with Prince Charles, 1981, heather behind (the engagement-period interview)',
 'e27a': 'real film: Diana\'s eyes, then her smile; the pin gives no date or place',
 'p52a': 'real film: Diana in a light blue suit shaking hands with soldiers; the pin gives no date or place',
 'p48a': 'real film of the wedding, 29 July 1981: the Glass Coach at St Paul\'s',
 'p48b': 'real film of the wedding, 29 July 1981: the dress and the train',
 'p48c': 'real film of the wedding, 29 July 1981: up the cathedral steps',
}
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
    fit = ('NOTE: ' if k in FILM else 'PARTLY: ') + note if note else 'matches the line'
    if k in CROP: fit += ' (cropped past a caption, label or small watermark)'
    holder = who + (' / ARCHIVE film of Princess Diana: the original broadcaster owns it; this pin is a fan re-upload' if k in FILM else '')
    rows.append(f"| {n} | {mmss(t)} | L{d['i']}: {txt} | {k} ({win}) | {holder} | {how} | credited, not licensed | unresolved | {fit} |")
assert len(U) == len({v[0] for v in C.values() if v[0] in U}) and len(U) == len(set(U))

# ---- photographs and product cut-outs ----
def first_time(i):
    ts = [float(x) for x in re.findall(r'tl\.[a-zA-Z]+\("#' + re.escape(i) + r'"[^;]*?,([0-9.]+)\);', H)]
    return min(ts) if ts else None
P = {}
for i, f in re.findall(r'<img id="([^"]+)" src="assets/((?:p|ph_)[a-z0-9_]+\.(?:jpg|png))"', H):
    t = first_time(i)
    if t is not None and (f not in P or t < P[f]): P[f] = t
for i, f in re.findall(r'<div id="([^"]+)"[^>]*>\s*<img[^>]*src="assets/((?:p|ph_)[a-z0-9_]+\.(?:jpg|png))"', H):
    t = first_time(i)
    if t is not None and (f not in P or t < P[f]): P[f] = t
for f in set(re.findall(r'assets/((?:p[a-z]+_[0-9]+|ph_[a-z]+)\.(?:jpg|png))', H)):
    P.setdefault(f, None)   # on the page but its start time was not found: listed without a time
TAGNOTE = {}
for ln in open('photo_picks.txt'):
    if ln.startswith('#') or not ln.strip(): continue
    tag, rest = ln.split(None, 1); nums, _, note = rest.partition('#')
    for n_ in nums.split(): TAGNOTE[f'{tag}_{n_}'] = note.strip()
PH = json.load(open('ph_picks.json'))
prow = []; n = 0
for f, t in sorted(P.items(), key=lambda z: (z[1] is None, z[1] or 0)):
    n += 1; k = f.rsplit('.', 1)[0]
    if k.startswith('ph_'):
        x = PH.get(k[3:], {}); tag, idx = x.get('tag', '?'), x.get('k', '?')
        kind = 'product cut-out (the brand or retailer owns the photograph)'
    else:
        tag, idx = k.rsplit('_', 1); kind = 'press photograph of Princess Diana (the photographer or agency owns it)'
    try: x = json.load(open(f'photos/{tag}.json'))[int(idx)]
    except Exception: x = {}
    pinned = f"pinned by @{x.get('creator_user', '?')}" + (f", links {x['src_link'][:70]}" if x.get('src_link') else '')
    title = (x.get('title') or '').replace('|', '/').replace('\n', ' ')[:90]
    chk = TAGNOTE.get(f'{tag}_{idx}', '') + (f' / pin title: "{title}"' if title else '')
    d = line_at(t) if t is not None else {'i': '?'}
    prow.append(f"| P{n} | {mmss(t) if t is not None else '-'} | L{d['i']} | {f} | {kind}; {pinned} | not licensed | unresolved | {chk} |")

hdr = f"""# SOURCES-LOG - 7 Things Princess Diana Loved That You Can Still Buy Today (The Classy Elegance, v1, 18 Nov 2026)

In order of appearance: **{len(rows)} video clips** ({len([k for k in U if k in FILM])} of them real archive film of Princess Diana, {len([k for k in U if k not in FILM])}
everyday scenes) and **{len(prow)} photographs** (press photographs of Princess Diana and product cut-outs from brand or
retailer photographs). No stock sites, no AI pictures.

- **Where the footage comes from:** Pinterest video pins of Instagram / TikTok creators' reels and of fan re-uploads of
  news film, as the creator does (`../../VISUAL-EDITING-DNA.md`). 233 clips downloaded from 50 searches in two rounds,
  plus a few later searches for single lines; the photographs from Pinterest photo pins, each read at full size.
- **All new footage.** 40 picks were dropped before download because their accounts appear in earlier videos' logs;
  `oldclash.py` compared every download with the 96 clips of the last Diana video and dropped 6 more. No clip is used
  twice in this video.
- **Captions, labels, logos and end cards:** every used window was sheeted at three moments and read by eye, the last
  frame of every used clip was read (a brand or AI end card puts the whole reel out: two reels were dropped for this,
  a scarf brand's tutorial and a stock-style ad), and the finished edit was read at 161 snapshots plus 24 re-checks.
  {len(CROP)} clips are cropped past a caption, a box label or a small watermark (the `CROP` list in `clips.py`).
- **Princess Diana is shown only in real archive film and real press photographs.** Never an actress, never AI.
- **"PARTLY" in the last column is said plainly**: the picture is true to the idea of the line but not to every word.

**Rights status.** **Nothing here is licensed.** The everyday clips are creators' reels found on Pinterest; the archive
film belongs to the original broadcasters; the photographs belong to press agencies, photographers and brands. Every
row is **unresolved**, and credit is not permission. A copyright claim or YouTube's reused-content rule is a real risk.
The creator decides before publishing.
Music: "Gymnopedie No 1" by Kevin MacLeod (incompetech.com), Creative Commons Attribution 4.0 - the credit line must be
in the description. No sound effects.

## Video clips

| # | At | Script line | Clip key (seconds used) | Creator / rights holder | How it was found | Licence basis | Decision | Fit to the line |
|---|---|---|---|---|---|---|---|---|
"""
open(D + 'SOURCES-LOG.md', 'w').write(hdr + '\n'.join(rows) + '\n\n## Photographs and product cut-outs\n\n| # | At | Line | File | Rights holder | Licence basis | Decision | What it shows / how it was checked |\n|---|---|---|---|---|---|---|---|\n' + '\n'.join(prow) + '\n')
handles = []
for k, t in sorted(U.items(), key=lambda z: z[1]):
    h = m[k].get('user')
    if h and '@' + h not in handles: handles.append('@' + h)
open(D + 'CREDITS.txt', 'w').write('VISUAL CREDITS (all footage belongs to its creators, thank you):\n' + ' '.join(handles) +
    '\nArchive film and photographs of Diana, Princess of Wales: the original broadcasters, news agencies and photographers.\n'
    'Music: "Gymnopedie No 1" by Kevin MacLeod (incompetech.com)\nLicensed under Creative Commons: By Attribution 4.0 License\nhttp://creativecommons.org/licenses/by/4.0/\n')
secs = [(1, 'Things she loved that you can still buy'), (7, '1. Her green wellies'), (13, '2. The black sheep jumper'),
        (21, '3. Soft brown, not blue'), (28, 'Your personal stylist guide'), (29, '4. One shoe, three colours'),
        (35, '5. The everyday tote'), (40, "6. The bag she didn't save"), (46, '7. Her perfume'), (53, 'All seven, and what they cost')]
out = [(0 if i == 1 else int(Bd[i]['start']), x) for i, x in secs]
total = Bd[len(Bd)]['end'] + 3.0
gaps = [b[0] - a[0] for a, b in zip(out, out[1:] + [(int(total), '')])]
assert out[0][0] == 0 and min(gaps) >= 10, gaps
open(D + 'CHAPTERS.txt', 'w').write('\n'.join(f'{t//60:02d}:{t%60:02d} {x}' for t, x in out) + '\n')
print(len(rows), 'clip rows', len(prow), 'photo rows', len(handles), 'handles;', sum(1 for r in rows if 'PARTLY' in r), 'PARTLY')
print('photos without a time:', [f for f, t in P.items() if t is None])
print(open(D + 'CHAPTERS.txt').read())
