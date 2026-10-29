# sources_log_from_edit.py - writes SOURCES-LOG.md for the built edit (one row per clip or cut-out on screen), plus music,
# fonts and logo.  usage (inside the work folder): python3 sources_log_from_edit.py [SOURCES-LOG.md] [ok5.txt]
import json, sys, re
B = json.load(open('beats.json')); SB = json.load(open('storyboard.json')); META = json.load(open('raw/meta.json'))
AI = json.load(open('aiscan.json'))
OKF = sys.argv[2] if len(sys.argv) > 2 else 'ok5.txt'
NOTE = {}
for l in open(OKF):
    p = l.split(None, 1)
    if len(p) == 2 and not l.startswith('#') and not p[1].startswith('SKIP'): NOTE.setdefault(p[0], p[1].strip())
def mmss(t): return f'{int(t // 60)}:{t % 60:04.1f}'
def lines_at(a, z): return [b['i'] for b in B if b['start'] < z and b['end'] > a]
first, lines, segs = {}, {}, {}
for s in SB:
    for c in s['clips']:
        k = 'p_' + c[0][4:-4] if c[0].endswith('.png') else c[0]
        first.setdefault(k, (s['t0'], s['t1'])); lines.setdefault(k, set()).update(lines_at(s['t0'], s['t1']))
        if not c[0].endswith('.png'): segs.setdefault(k, []).append(f'{c[1]:g}-{c[2]:g}')
nfilm = sum(k.startswith('film_') for k in first); ncut = sum(k.startswith('p_') for k in first)
out = ['# SOURCES-LOG / asset ledger v5 - 8 Things Elegant Ladies Never Wear in Winter (Episode 15)', '',
       f'Every asset in the render: {len(first) - nfilm - ncut} Pinterest video pins, {nfilm} scenes from *Charade* (1963) and {ncut} product',
       'cut-outs made from Pinterest product photos, plus music, fonts and logo. Generated from `raw/meta.json` (the search',
       'record of each pin) and the built edit (`storyboard.json`).', '',
       '**How the footage was found.** Pinterest\'s real Videos tab, several pages deep (`tools/pinsearch2.py`), one search per',
       'garment combination the script names (`picks.md`); every result sheet was looked at by eye, every pick was downloaded and',
       'checked frame by frame (`ok5.txt`: what each clip shows and which seconds are clean). The key is the search tag plus the',
       'result number, e.g. `a_fineturtle5` = the "fine turtleneck under a long coat" search, result 5.', '',
       '**Rights status (read this).**',
       '- Under `workflow/SOURCES-LOG-TEMPLATE.md`, a clip that is only found on Pinterest and credited is **unresolved**.',
       '  None of the Pinterest clips or product photos has a licence or the creator\'s written permission.',
       '- The *Charade* rows come from the Internet Archive item `charade-1963-cary-grant-audrey-hepburn-comedy-mystery-romance-',
       '  thriller-full-movie`, marked **Public Domain Mark 1.0** there. *Charade* is widely reported to have entered the US',
       '  public domain because it was published without a valid copyright notice; that is the archive\'s and the reports\'',
       '  claim, not a legal opinion. They play silent, under the voice.',
       '- The name given is the Pinterest pinner, which is often not the original creator. A TikTok mark or an Instagram',
       '  outbound link means the clip started there.', '',
       '**AI check.** `tools/aiscan.py` ran on every clip used; none scored 0.40 or more (the build stops if one does).', '',
       '| # | First on screen | Lines | What it shows (key, seconds used) | Where we got it | Creator / pinner (handle) | Outbound link | Licence or permission basis | Commercial use on monetised YouTube? | Edit/crop/speed allowed? | AI scan | Decision |',
       '|---|---|---|---|---|---|---|---|---|---|---|---|']
for n, k in enumerate(sorted(first, key=lambda k: first[k][0]), 1):
    m = META.get(k, {}); a, z = first[k]
    what = re.sub(r'^[\d.,\- ]+', '', NOTE.get(k, m.get('title', ''))).replace('|', '/')
    src = (m.get('src') or '-').replace('|', '/')
    if k.startswith('film_'):
        where, basis, com, ed, dec = 'Internet Archive', 'Public Domain Mark 1.0 (archive item)', 'yes if public domain', 'yes', 'public-domain mark'
    elif k.startswith('p_'):
        where, basis, com, ed, dec = f'Pinterest image pin {m.get("pin_id", "?")} (product photo, background removed)', 'none: found on Pinterest, credited only', 'unknown', 'unknown', 'unresolved'
    else:
        where, basis, com, ed, dec = f'Pinterest video pin {m.get("pin_id", "?")}', 'none: found on Pinterest, credited only', 'unknown', 'unknown', 'unresolved'
    used = f', {", ".join(segs[k])} s' if k in segs else ''
    out.append(f'| {n} | {mmss(a)}-{mmss(z)} | {",".join(map(str, sorted(lines[k])))} | {what} (`{k}`{used}) | {where} | '
               f'{m.get("creator", "?").replace("|", "/")} (@{m.get("user", "")}) | {src} | {basis} | {com} | {ed} | '
               f'{AI.get(k, 0):.2f} | {dec} |')
out += ['', '## Not footage', '',
        '| Asset | Source | Licence | Decision |', '|---|---|---|---|',
        '| Music: "Classical 4", "Classical 9", "Classical 5", "Classical 10" by Jonny S. | Mixkit | Mixkit Free Licence (music) | cleared (same tracks as the channel\'s earlier edits) |',
        '| Voice-over | Kokoro TTS, voice af_heart, speed 0.80, generated here | Apache-2.0 model | cleared |',
        '| Fonts: Pinyon Script, Playfair Display | Google Fonts | SIL Open Font License | cleared |',
        '| Logo: CE monogram (`workflow/assets/logo_ce.png`, `logo_ce_dark.png`) | the channel\'s own | own | cleared |']
open(sys.argv[1] if len(sys.argv) > 1 else 'SOURCES-LOG.md', 'w').write('\n'.join(out) + '\n')
print('rows', len(first))
