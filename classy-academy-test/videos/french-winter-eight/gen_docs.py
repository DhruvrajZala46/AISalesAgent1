# gen_docs.py - sources log, credits and chapters for "8 French-Inspired Winter Essentials" (run after the final build)
import json, re, os
m = json.load(open('raw/meta.json')); U = json.load(open('used_times.json')); B = json.load(open('beats.json'))
P = json.load(open('ph_picks.json')); Bd = {d['i']: d for d in B}
exec("CROP={};MAXSLOW={}\n" + open('clips.py').read())
def line_at(t):
    best = B[0]
    for d in B:
        if d['start'] - 0.6 <= t: best = d
    return best
mmss = lambda t: f'{int(t//60)}:{int(t%60):02d}'
# what each clip shows, as seen by eye (eye_notes.txt), and where the match is only partial
PARTLY = {
 'i5e': 'a knit on a rail; stands for "worn often"',
 'i6a': 'title beat: a navy V-neck with jeans (one of the eight)', 'i6b': 'title beat: a blazer over a satin skirt',
 'i7b': 'one woman in complete outfits changing every 2-3 s (turtleneck, blazer, jeans, coat)',
 'c10b': 'a cream-beige coat tried at a shop mirror (phone in hand)',
 'c11a': 'a rack of wool coats with price tags', 'c11l': 'a wool label inside a jacket (Harris Tweed), slowed',
 'c14b': 'belted coat by day, not in the evening: the label says only "Or belted"',
 'c14d': 'camel coat over a black top and jeans; she is talking',
 't15': 'a woman opens a camel coat to show what is underneath (black top, not a knit)',
 't16d': 'a navy turtleneck knit DRESS under a coat, not a jumper',
 't17a': 'a dusk street seen from behind a woman in a dark coat (dark picture)',
 't17c': "two women over coffee, top halves; a third person's wrist is in the foreground",
 't18z': 'black turtleneck with white trousers', 't20': 'a cream knit set in a fitting room, coat hanging behind',
 'v22a': 'a plain crew-neck sweater, nothing showing at the neck (quick cuts of the same sweater)',
 'v23b': 'an oversized knit over a satin skirt with trainers',
 'v24a': 'knits held up on hangers (no label in shot: the labels are the two photos)',
 'b28z': 'a blazer outfit in front of a wardrobe', 'b30a': 'a hip-length grey blazer with wide jeans; she is talking',
 'b31': 'a woman of about 45 in a plain navy blazer; she is talking',
 'g33': 'a hand sliding hangers on a rail (the guide screen)',
 'j36b': 'the hem of WIDE jeans resting on a pointed boot', 'j36c': 'flared raw-hem jeans on a tan boot (not straight, not dark)',
 'j37b': 'dark flared jeans with black heels, not boots', 'j38c': 'cuffed jeans with ankle boots under a leather coat',
 'j39': 'wide dark jeans with a blazer, walking',
 's40': 'skirts being hung in a wardrobe (bright colours; a hanger demo)', 's41a': 'a pink check skirt hung on a rail (a hanger demo)',
 's41c': 'an ankle-length wool A-line skirt in a mirror selfie', 's42a': 'a brown tweed wool skirt, close (bare legs)',
 's42m': 'a teal mid-calf skirt with heeled boots (not wool)', 's42b': 'a brown suede-look A-line midi with tall boots',
 's43b': 'a cream sweater over a cream satin midi (not a V-neck)',
 's44a': 'opaque tights with a tweed skirt that ends ABOVE the knee', 's44b': 'a long cream pleated skirt moving (not wool)',
 'o45': 'a woman pulls on flat tall boots in her closet (leggings)',
 'o46b': 'a knee-length skirt with tall boots: a strip of leg shows', 'o46c': 'a long black skirt over black boots, no gap',
 'o47': 'black knee-high boots with a block heel (cropped below the knee)',
 'o48a': 'tall boots under grey TROUSERS, not jeans', 'o48b': 'light jeans over black boots',
 'o49b': 'boot tips in a rain puddle (dark)', 'o49c': 'a boot at a cobbler\'s brushing machine (a shoe-maker\'s film)',
 'o49d': 'brushing a brown ankle boot (cropped past a text box)',
 'g50': 'black leather gloves, close (a product film)', 'g52a': 'black gloves going on over a trench coat (a glove-maker\'s film)',
 'g52b': 'brown fabric gloves with knit cuffs at a coat sleeve: not leather',
 'g54b': 'burgundy leather gloves with an all-black outfit; she is talking',
 'x55': 'a hand lays a tee, belt and watch on a camel coat (a spring flat lay)',
 'x56a': 'two women walking through a French outdoor market', 'x56b': 'a woman in a navy coat choosing vegetables',
 'x57a': 'two friends at a cafe terrace, coats on', 'x58': 'a belted blazer over a pleated midi with heels: no boots, coat or gloves in shot',
 'r61a': 'a woman choosing a knit in a boutique', 'r61b': 'striped knit, black midi skirt and boots on a city street',
 'r62': 'a young woman walks and smiles (black coat, jeans, trainers)', 'r63': 'a hand along a rail of coats and shirts',
 'r64': 'an older woman walks past lit shop windows (three shots of one film)',
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
    fit = 'PARTLY: ' + note if note else 'matches the line'
    if k in CROP: fit += ' (cropped past a caption, handle or bare skin)'
    rows.append(f"| {n} | {mmss(t)} | L{d['i']}: {txt} | {k} ({win}) | {who} | {how} | credited, not licensed | unresolved | {fit} |")
# photos and product cut-outs, in order of appearance
PH = [(11, 'lbsyn', 'label: 100% polyester shell', 'photo'), (11, 'lbcoat', 'label: 60% wool', 'photo'),
      (16, 'tt', 'black turtleneck (cut-out)', 'cut-out'), (18, 'ttdress', 'turtleneck under a short-sleeved dress', 'photo'),
      (19, 'ttc', 'cream turtleneck (cut-out)', 'cut-out'), (19, 'ttn', 'navy turtleneck (cut-out)', 'cut-out'),
      (22, 'vnt1', 'V-neck over a turtleneck, close', 'photo'), (24, 'lbwool', 'label: 100% wool', 'photo'), (24, 'ph_lbacr2', 'label: 100% acrylic', 'photo'),
      (25, 'vnt2', 'V-neck over a turtleneck with jeans', 'photo'), (25, 'vskirt', 'V-neck tucked into a skirt, fine chain (mirror photo, cropped)', 'photo'),
      (42, 'ph_lining', 'a lined wool skirt, inside', 'photo'), (42, 'slit', 'straight wool skirt with a back slit', 'photo'),
      (49, 'boots2', 'black tall boots (cut-out)', 'cut-out'), (49, 'bootsbr', 'dark brown tall boots (cut-out)', 'cut-out'),
      (51, 'glvcoat', 'brown leather gloves on a herringbone coat', 'photo'), (52, 'ph_glvlin', 'leather gloves with a wool-cashmere lining', 'photo'),
      (53, 'glvbag', 'brown gloves matched to a brown bag', 'photo'), (53, 'glvburg', 'burgundy gloves with a charcoal coat', 'photo'),
      (55, 'coat', 'navy long coat (cut-out)', 'cut-out'), (55, 'vn', 'navy V-neck (cut-out)', 'cut-out'), (55, 'blz', 'grey wool blazer (cut-out)', 'cut-out'),
      (55, 'jeans', 'dark straight jeans (cut-out)', 'cut-out'), (55, 'skirt', 'grey wool midi skirt (cut-out)', 'cut-out'), (55, 'glove', 'black leather gloves (cut-out)', 'cut-out')]
prow = []
for n, (li, name, what, kind) in enumerate(PH, 1):
    p = P[name]; who = (p.get('creator') or '').replace('|', '/'); who = f"{who} (@{p['user']})" if p.get('user') else who
    dom = p.get('domain') or ''
    prow.append(f"| P{n} | {mmss(Bd[li]['start'])} | L{li} | {what} | {who} | Pinterest photo pin {p['url']} ({dom}{', ' + p['link'][:60] if p.get('link') else ''}) | {kind}; credited, not licensed | unresolved |")
nphoto = sum(1 for x in PH if x[3] == 'photo'); ncut = len(PH) - nphoto
hdr = f"""# SOURCES-LOG - 8 French-Inspired Winter Essentials (The Classy Elegance, v1, 15 Nov 2026)

One row per clip, in order of first appearance: **{len(rows)} video clips**, then **{nphoto} real photos and {ncut} product
cut-outs**.
- **Where the footage comes from:** Pinterest video pins of Instagram / TikTok creators' reels: 207 search phrases in
  six rounds, 584 clips downloaded and read. Photos: Pinterest photo pins (54 searches). No free-stock site was used.
- **Each clip appears once.** One exception, on purpose: `market1` gives two different shots of the same market film,
  one after the other (the builder refuses any window that overlaps footage already shown).
- **Duplicate check:** every download hashed at 1 frame per second (`tools/dupall.py`): 80 groups of re-pinned footage;
  only one copy of a group may be used; 0 clashes among the used clips.
- **No repeats from earlier videos:** `oldclash.py` against the used clips of all eleven earlier videos flagged 83
  downloads; none is used.
- **AI checks:**
  - the Gemini watermark scan flagged 2 downloads (not used);
  - removed by eye: three near-still "videos" from one account with the same synthetic-looking face in three outfits
    (motion measured at 0.1-0.2 on a 0-255 scale), a clip from an account whose name ends in "ai", a clip with a
    computer-made closet behind the woman, a product clip with a machine-smooth zoom;
  - honest limit: a real-looking clip can still be AI. These checks lower the risk; they do not prove a clip is real.
- **Captions, watermarks and stickers:** every candidate was read on time-labelled strips by a first and a second
  screening, every pick again at large size by me (`vs/*.jpg`, notes in `eye_notes.txt`), every prepared segment at
  three moments, and the finished edit at 161 snapshots. {len(CROP)} clips are cropped past a caption, an account
  handle or bare skin (the `CROP` list in `clips.py`).
- **Where no true clip exists, the line shows a real photo or the piece itself** (listed below): a V-neck over a
  turtleneck, a turtleneck under a dress, a V-neck tucked into a skirt, a back slit, gloves matched to a bag, burgundy
  gloves on a coat, the labels and linings, and the two boot colours.
- **"PARTLY" in the last column is said plainly**: the picture is true to the idea of the line but not to every word.

**Rights status.** Footage and photos: creators' reels, shop product pictures and personal photos found on Pinterest.
**None is licensed**: every row is **unresolved**, and credit is not permission. A copyright claim or YouTube's
reused-content rule is a real risk. The creator decides before publishing.
Music: "Classical 4" by Jonny S., Mixkit Stock Music Free License (cleared).

## Video clips

| # | At | Script line | Clip key (seconds used) | Creator / rights holder | How it was found | Licence basis | Decision | Fit to the line |
|---|---|---|---|---|---|---|---|---|
"""
ph_hdr = """
## Photos and product cut-outs

| # | At | Line | What it shows | Pinner / rights holder | Source | Kind and licence basis | Decision |
|---|---|---|---|---|---|---|---|
"""
D = '/home/user/AISalesAgent1/classy-academy-test/videos/french-winter-eight/'
open(D + 'SOURCES-LOG.md', 'w').write(hdr + '\n'.join(rows) + '\n' + ph_hdr + '\n'.join(prow) + '\n')
handles = []
for k, t in sorted(U.items(), key=lambda z: z[1]):
    h = m[k].get('user')
    if h and '@' + h not in handles: handles.append('@' + h)
ph_names = []
for li, name, what, kind in PH:
    p = P[name]; h = p.get('user') or ''
    if h and not h.startswith('preview_') and '@' + h not in handles and '@' + h not in ph_names: ph_names.append('@' + h)
open(D + 'CREDITS.txt', 'w').write('VISUAL CREDITS (all footage and photos belong to their creators, thank you):\n' + ' '.join(handles) +
    '\nPhotos: ' + ' '.join(ph_names) + '\nMusic: "Classical 4" by Jonny S. (Mixkit)\n')
secs = [(1, 'Eight pieces for the whole winter', 's'), (9, '1. A long wool coat', 's'), (15, '2. A fine turtleneck', 's'), (21, '3. A V-neck sweater', 's'),
        (26, '4. A wool blazer', 's'), (32, 'Your personal stylist guide', 's'), (34, '5. Dark straight-leg jeans', 's'), (40, '6. A wool midi skirt', 's'),
        (45, '7. Tall leather boots', 's'), (50, '8. Leather gloves', 's'), (55, 'Four outfits from the eight', 's'), (60, 'The eight, and which one first?', 's')]
out = [(0 if i == 1 else int(Bd[i]['start']), x) for i, x, kind in secs]
total = Bd[len(Bd)]['end'] + 4.2
assert out[0][0] == 0 and min(b[0] - a[0] for a, b in zip(out, out[1:] + [(total, '')])) >= 10
open(D + 'CHAPTERS.txt', 'w').write('\n'.join(f'{t//60:02d}:{t%60:02d} {x}' for t, x in out) + '\n')
missing = [s_ for s_ in PARTLY if s_ not in C]
print(len(rows), 'clip rows', len(prow), 'photo rows', len(handles), 'handles; partly notes for missing slots:', missing)
print(sum(1 for r in rows if 'PARTLY' in r), 'rows marked PARTLY'); print(open(D + 'CHAPTERS.txt').read())
