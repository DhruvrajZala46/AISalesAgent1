# gen_docs_jewels.py - SOURCES-LOG, CREDITS and CHAPTERS for "Princess Diana's 7 Jewels: Who Wears Them Now?"
# Run inside the work folder after the final build:  python3 <this file>
import json, re, os
D = '/home/user/AISalesAgent1/classy-academy-test/videos/diana-jewels-who-wears-them/'
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
FILM = {'jdsmile7', 'jdaus22', 'jdwed39', 'jdtiara13', 'jdgala20'}
PARTLY = {
 'h2a': 'hands with rings: stands for "nearly every one of those pieces is still out in the world"',
 'h2c': 'a tiara in a museum case: stands for "some went home to her family" (not the Spencer tiara)',
 'h2d': 'a woman\'s hand with rings: stands for "a woman you would never guess"',
 'h6b': 'a tiara, close: stands for "a few may surprise you"',
 'h5a': 'real film: Diana dancing in a pale blue gown; the caption names the Australia tour dance (the title is shown over it)',
 'h1a': 'real film: Diana smiling, close; the pin gives no date or place',
 'r51a': 'real film: Diana dancing in a white and blue print gown; the uploader dates it Australia 1988',
 's11b': 'a mother helping a bride on her wedding morning: stands for "the days that matter"',
 's12a': 'a woman walking in a cream coat: stands for the payoff line',
 'k18a': 'a woman putting on earrings at home, not checking comfort',
 'k18c': 'fastening an earring with a tool (a tutorial caption cropped away), not soft backs',
 'e24a': 'a wooden jewellery box opened: stands for "the way it came out of the box"',
 'e26a': 'a woman putting on her bracelets: stands for "one piece, two ways"',
 'g27b': 'a woman getting ready with earrings: stands for "gold or silver"',
 'g27c': 'putting on earrings at a mirror: stands for "whether gold or silver flatters"',
 'c31a': 'pearl earrings in a box held open, not put away',
 'c32b': 'a woman in a black dress and gloves, evening; pearl earrings not visible',
 'c32c': 'a woman in a pearl necklace, not pearl earrings',
 'm37a': 'an old ring box opened, rings inside (a small label on the lid)',
 'm38a': 'hands taking pieces from a jewellery tray: stands for "don\'t leave those pieces in the dark"',
 'b44b': 'a brooch pinned at the neck of a cardigan: stands for "a sister\'s brooch"',
 'b44c': 'a hand writing a letter: stands for "a little thank-you note"',
 'r47a': 'trying rings at a counter: stands for "anyone could order the same design"',
 'r50b': 'an old locket held in her hands: stands for "keep it close"',
 'z52b': 'Buckingham Palace: under "each one is still telling her story"',
 'z53a': 'a woman of about 65 talking with a friend, under the comment ask',
 'z54b': 'putting in an earring, close, under the thank-you',
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
        tag, idx = k.rsplit('_', 1); kind = 'press photograph (the photographer or agency owns it)'
    try: x = json.load(open(f'photos/{tag}.json'))[int(idx)]
    except Exception: x = {}
    pinned = f"pinned by @{x.get('creator_user', '?')}" + (f", links {x['src_link'][:70]}" if x.get('src_link') else '')
    title = (x.get('title') or '').replace('|', '/').replace('\n', ' ')[:90]
    chk = TAGNOTE.get(f'{tag}_{idx}', '') + (f' / pin title: "{title}"' if title else '')
    d = line_at(t) if t is not None else {'i': '?'}
    prow.append(f"| P{n} | {mmss(t) if t is not None else '-'} | L{d['i']} | {f} | {kind}; {pinned} | not licensed | unresolved | {chk} |")

hdr = f"""# SOURCES-LOG - Princess Diana's 7 Jewels: Who Wears Them Now? (The Classy Elegance, v1, 19 Nov 2026)

In order of appearance: **{len(rows)} video clips** ({len([k for k in U if k in FILM])} of them real archive film of Princess Diana, {len([k for k in U if k not in FILM])}
everyday scenes) and **{len(prow)} photographs** (press photographs of Princess Diana and of Catherine, Princess of
Wales and Celia McCorquodale wearing the same jewels, and two auction photographs of the cross). No stock sites, no AI pictures.

- **Where the footage comes from:** Pinterest video pins of Instagram / TikTok creators' reels and of fan re-uploads of
  news film, as the creator does (`../../VISUAL-EDITING-DNA.md`). 192 clips downloaded from 41 searches in two rounds;
  the photographs from 17 Pinterest photo searches, each read at full size.
- **All new footage.** Picks from accounts used in any earlier video were dropped before download (19 in round one);
  `oldclash.py` compared every download with the clips of the last two Diana videos (4 repeats, none used). No clip is
  used twice in this video.
- **Captions, labels, logos and end cards:** every used window was sheeted at three moments and read by eye; the last
  frame of every used clip was read (5 reels that end on a company card were dropped); the finished edit was read at
  153 snapshots plus re-checks. {len(CROP)} clips are cropped past a caption or a label (the `CROP` list in `clips.py`).
- **Princess Diana is shown only in real archive film and real press photographs.** Never an actress, never AI.
  Photographs that looked AI-smoothed were left out.
- **"PARTLY" in the last column is said plainly**: the picture is true to the idea of the line but not to every word.

**Rights status.** **Nothing here is licensed.** The everyday clips are creators' reels found on Pinterest; the archive
film belongs to the original broadcasters; the photographs belong to press agencies, photographers and brands. Every
row is **unresolved**, and credit is not permission. A copyright claim or YouTube's reused-content rule is a real risk.
The creator decides before publishing.
Music: "Healing" and "Gymnopedie No 2" by Kevin MacLeod (incompetech.com), Creative Commons Attribution 4.0 - the credit
line must be in the description. No sound effects.

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
    'Music: "Healing" and "Gymnopedie No 2" by Kevin MacLeod (incompetech.com)\nLicensed under Creative Commons: By Attribution 4.0 License\nhttp://creativecommons.org/licenses/by/4.0/\n')
secs = [(1, 'Where is every piece today?'), (7, '1. The Spencer tiara'), (13, "2. The Lover's Knot"), (20, '3. The emerald headband'),
        (27, 'Your personal stylist guide'), (28, '4. The Collingwood pearls'), (34, '5. The sapphires made new'),
        (40, '6. The cross she borrowed'), (46, '7. The sapphire ring'), (52, 'Seven jewels, and what they teach')]
out = [(0 if i == 1 else int(Bd[i]['start']), x) for i, x in secs]
total = Bd[len(Bd)]['end'] + 3.0
gaps = [b[0] - a[0] for a, b in zip(out, out[1:] + [(int(total), '')])]
assert out[0][0] == 0 and min(gaps) >= 10, gaps
open(D + 'CHAPTERS.txt', 'w').write('\n'.join(f'{t//60:02d}:{t%60:02d} {x}' for t, x in out) + '\n')
print(len(rows), 'clip rows', len(prow), 'photo rows', len(handles), 'handles;', sum(1 for r in rows if 'PARTLY' in r), 'PARTLY')
print('photos without a time:', [f for f, t in P.items() if t is None])
print(open(D + 'CHAPTERS.txt').read())
