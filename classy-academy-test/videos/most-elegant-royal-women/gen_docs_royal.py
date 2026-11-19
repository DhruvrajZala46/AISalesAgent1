# gen_docs_royal.py - SOURCES-LOG, CREDITS and CHAPTERS for "The 7 Most Elegant Royal Women Ever, Ranked"
# Run inside the work folder after the final build:  python3 <this file>
import json, re, os
D = '/home/user/AISalesAgent1/classy-academy-test/videos/most-elegant-royal-women/'
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
FILM = {'rdiana6', 'rdiana8', 'rkate31', 'rqueen3', 'rgrace3', 'rletwalk5', 'rletizia3', 'rqm0'}
PARTLY = {
 'h4a': 'a woman showing a simple cream outfit at home: stands for "small choices any woman can make"',
 'h5a': 'real film: Princess Diana in a red jacket greeting a crowd; under the title, standing for the seven women',
 'm10a': 'a woman holding up one dress and trying it on, not dressing for a birthday',
 'm10b': 'a woman in a long black dress checking it in the mirror: "will it be enough?"',
 'm11a': 'two women in long pale gowns at a sunny celebration; nobody takes a photograph',
 'l17a': 'a woman handling clothes with tags at a rail; no price is read',
 'l18b': 'beige heels walking (the size label cropped away); leather not certain',
 'l18c': 'a long, well-cut coat in blue',
 'l18d': 'one good bag with a tweed jacket, white shirt and jeans; she talks to camera',
 'q24a': 'a woman in a black dress at the mirror, her face hidden by her phone',
 'q25c': 'a white shirt and cream trousers under a camel trench; posing, not walking (cropped past a watermark)',
 'g27b': 'an elegant woman in winter white under the guide line',
 'k31a': 'shoes being put on a rack; no dress is shown',
 'k32b': 'one woman in five outfits of different colours with nude and black court shoes',
 'e37a': 'a woman in a grey coat under an umbrella on a quiet street',
 'e38b': 'an emerald green jacket, walking',
 'e38c': 'a rust-red scarf put on at a mirror',
 'd41a': 'real film: Princess Diana with the short cut; not the 1990 Vogue shoot itself',
 'd43a': 'a client talking in a salon chair (cropped past word captions)',
 'd44a': 'a young woman with a short bob turning to the camera',
 'd45a': 'a young woman with a fresh short cut',
 'c49a': 'a short, tight pink dress; nobody tugs a hem',
 'c50a': 'a high-neck, long-sleeved lace dress in daylight, a brand reel (captions cropped away)',
 'c50b': 'lace sleeves, a brand reel; not an evening event',
 'c50c': 'a high-neck midi dress, a try-on',
 'c51a': 'an elegant older woman smiles',
 'z52a': 'real film: Queen Letizia greeting the public, under the summary of the seven lessons',
 'z53a': 'a woman talking to camera, under the comment ask',
 'z54a': 'real film: Queen Letizia smiles and waves, under the thank-you',
 'z54b': 'an elegant woman in cream, under the guide line',
 'z54c': 'real film: the Queen Mother in later life in her garden (cropped past a news-agency logo), at the goodbye',
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
    holder = who + (' / ARCHIVE film of a royal woman: the original broadcaster or news agency owns it; this pin is a fan re-upload' if k in FILM else '')
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
for ln in list(open('photo_picks.txt')) + list(open('photo_picks2.txt')):
    if ln.startswith('#') or not ln.strip(): continue
    tag, rest = ln.split(None, 1); nums, _, note = rest.partition('#')
    for n_ in nums.split(): TAGNOTE[f'{tag}_{n_}'] = note.strip()
PH = json.load(open('ph_picks.json')) if os.path.exists('ph_picks.json') else {}
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

hdr = f"""# SOURCES-LOG - The 7 Most Elegant Royal Women Ever, Ranked (The Classy Elegance, v1, 19 Nov 2026)

In order of appearance: **{len(rows)} video clips** ({len([k for k in U if k in FILM])} of them real archive or news film of the royal women,
{len([k for k in U if k not in FILM])} everyday scenes) and **{len(prow)} photographs** (press photographs and portraits of the seven women,
the Hartnell sketch of 1938, the Dior gown in the museum, and two product photographs of the L.K. Bennett Sledge). No stock
sites, no AI pictures.

- **Where the footage comes from:** Pinterest video pins of Instagram / TikTok creators' reels and of fan re-uploads of
  news film, as the creator does (`../../VISUAL-EDITING-DNA.md`). 191 clips downloaded from 53 searches in two rounds;
  the photographs from 20 Pinterest photo searches, each read at full size.
- **All new footage.** Picks from accounts used in any earlier video were dropped before download (25 in round two);
  `oldclash.py` compared every download with the clips of the three Diana videos (one repeat, not used). Every photograph
  was compared with the photographs of the earlier videos (no repeats). No clip or photograph is used twice here.
- **Captions, labels, logos and end cards:** every used window was sheeted at three moments and read by eye; the last
  frame of every used clip was read (one brand reel with a price card dropped, four windows trimmed before the subject
  walks out); the finished edit was read at about 150 snapshots plus re-checks. {len(CROP)} clips are cropped past a
  caption, logo or watermark (the `CROP` list in `clips.py`), and the Queen Mother film is cropped past a news logo.
- **The royal women are shown only in real archive film, news film and real photographs.** Never an actress (The Crown,
  Spencer and Grace Kelly's own film roles were all left out), never AI. Photographs that looked AI-smoothed or
  AI-colourised were left out. No real 1950s film of Princess Margaret and no 1930s film of the Queen Mother were found,
  so those two are shown in photographs only.
- **"PARTLY" in the last column is said plainly**: the picture is true to the idea of the line but not to every word.

**Rights status.** **Nothing here is licensed.** The everyday clips are creators' reels found on Pinterest; the archive
film belongs to the original broadcasters and agencies; the photographs belong to press agencies, photographers, museums
and brands. Every row is **unresolved**, and credit is not permission. A copyright claim or YouTube's reused-content rule
is a real risk. The creator decides before publishing.
Music: "Gymnopedie No 3" and "At Rest" by Kevin MacLeod (incompetech.com), Creative Commons Attribution 4.0 - the credit
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
    '\nArchive film and photographs of the royal women: the original broadcasters, news agencies, photographers and museums.\n'
    'Music: "Gymnopedie No 3" and "At Rest" by Kevin MacLeod (incompetech.com)\nLicensed under Creative Commons: By Attribution 4.0 License\nhttp://creativecommons.org/licenses/by/4.0/\n')
secs = [(1, 'The most elegant royal women, ranked'), (7, '7. Princess Margaret'), (14, '6. Queen Letizia of Spain'),
        (20, '5. The Queen Mother'), (27, 'Your personal stylist guide'), (28, '4. Catherine, Princess of Wales'),
        (34, '3. Queen Elizabeth II'), (40, '2. Princess Diana'), (46, '1. Grace Kelly'), (52, 'Seven lessons, no crown needed')]
out = [(0 if i == 1 else int(Bd[i]['start']), x) for i, x in secs]
total = Bd[len(Bd)]['end'] + 3.0
gaps = [b[0] - a[0] for a, b in zip(out, out[1:] + [(int(total), '')])]
assert out[0][0] == 0 and min(gaps) >= 10, gaps
open(D + 'CHAPTERS.txt', 'w').write('\n'.join(f'{t//60:02d}:{t%60:02d} {x}' for t, x in out) + '\n')
print(len(rows), 'clip rows', len(prow), 'photo rows', len(handles), 'handles;', sum(1 for r in rows if 'PARTLY' in r), 'PARTLY')
print('photos without a time:', [f for f, t in P.items() if t is None])
print(open(D + 'CHAPTERS.txt').read())
