# slog.py - writes SOURCES-LOG.md for the built edit (one row per clip on screen), plus music, fonts and logo.
import json, sys, re
B = json.load(open('beats.json')); SB = json.load(open('storyboard.json')); META = json.load(open('raw/meta.json'))
AI = json.load(open('aiscan.json'))
NOTE = {}
for l in open('ok.txt'):
    if l.strip() and not l.startswith('#'):
        k, rest = l.split(None, 1); NOTE[k] = rest.strip()
FILM = {'fymail10': ("You've Got Mail (1998, Warner Bros.)", 'film footage inside a creator\'s comparison reel ("Meg Ryan fall"); the creator\'s own recreations are cut out'),
        'flw5': ('Little Women (1994, Columbia Pictures)', 'fan montage of the film; the burned-in "Little Women (1994)" caption is cropped out')}
def mmss(t): return f'{int(t // 60)}:{t % 60:04.1f}'
def lines_at(a, z): return [b['i'] for b in B if b['start'] < z and b['end'] > a]
first, lines, segs = {}, {}, {}
for s in SB:
    for c in s['clips']:
        k = c[0]; first.setdefault(k, (s['t0'], s['t1'])); lines.setdefault(k, set()).update(lines_at(s['t0'], s['t1']))
        segs.setdefault(k, []).append(f'{c[1]:g}-{c[2]:g}')
out = ['# SOURCES-LOG / asset ledger - 8 Things Elegant Ladies Never Wear in Winter (Episode 32)', '',
       f'Every clip in the render: {len(first)} Pinterest video pins, plus music, fonts and logo. Generated from `raw/meta.json`',
       '(the Pinterest search record of each pin) and the built edit (`storyboard.json`).', '',
       '**How the footage was found.** Pinterest video search with `tools/pin_search.py`, the way the channel sources its',
       'reels (VISUAL-EDITING-DNA.md). The key is the search tag plus the result number, e.g. `windycoat41` = search',
       '"windy day long wool coat woman video", result 41. Pinterest returns ad-style pin IDs (`e1_...`), so there is no',
       'public pin URL; the pin ID and the outbound link (if the pin has one) are recorded instead.', '',
       '**Rights status (read this).**',
       '- Under `workflow/SOURCES-LOG-TEMPLATE.md`, a clip that is only found on Pinterest and credited is **unresolved**.',
       '  None of these clips has a licence or the creator\'s written permission.',
       '- Two rows are **1980s-90s film scenes**. The owner chose to use them ("Use film scenes, my risk"), so they are',
       '  marked **unlicensed, owner\'s decision**. Film scenes can trigger Content ID claims; they play silent, under the voice.',
       '- The name given is the Pinterest pinner, which is often not the original creator. A TikTok mark or an Instagram',
       '  outbound link means the clip started there.', '',
       '**AI check.** `tools/aiscan.py` ran on every download. Clips scoring 0.40 or more are never used (the build stops).',
       'label9 (1.00), scarfwrap26 (0.63) and scarfwrap34 (0.44) were flagged and are not used. washknit0 (0.38) is borderline and is not used. heels42, knitquality23,',
       'woolcare43 and the cosy-fireplace search results were also left out because they look computer-made to the eye, even',
       'where the score was low.', '',
       '| # | First on screen | Lines | What it shows (key, seconds used) | Where we got it | Creator / pinner (handle) | Outbound link | Licence or permission basis | Commercial use on monetised YouTube? | Edit/crop/speed allowed? | AI scan | Decision | Notes |',
       '|---|---|---|---|---|---|---|---|---|---|---|---|---|']
for n, k in enumerate(sorted(first, key=lambda k: first[k][0]), 1):
    m = META.get(k, {}); a, z = first[k]
    what = re.sub(r'^[\d.,\- ]+', '', NOTE.get(k, m.get('title', ''))).replace('|', '/')
    src = (m.get('src') or '-').replace('|', '/')
    if k in FILM:
        basis, dec, note = 'none (film studio copyright)', "**unlicensed, owner's decision**", f'{FILM[k][0]}; {FILM[k][1]}'
    else:
        basis, dec, note = 'none: found on Pinterest, credited only', 'unresolved', ('TikTok/Instagram origin' if 'instagram' in src or 'tiktok' in src else '')
    out.append(f'| {n} | {mmss(a)}-{mmss(z)} | {",".join(map(str, sorted(lines[k])))} | {what} (`{k}`, {", ".join(segs[k])} s) | '
               f'Pinterest, pin id {m.get("pin_id", "?")} | {m.get("creator", "?").replace("|", "/")} (@{m.get("user", "?")}) | {src} | {basis} | unknown | unknown | '
               f'{AI.get(k, 0):.2f} | {dec} | {note} |')
out += ['', '## Not footage', '',
        '| Asset | Source | Licence | Decision |', '|---|---|---|---|',
        '| Music: "Classical 4", "Classical 9", "Classical 5", "Classical 10" by Jonny S. | Mixkit | Mixkit Free Licence (music) | cleared (same tracks as the channel\'s earlier edits) |',
        '| Voice-over | Kokoro TTS, voice af_heart, speed 0.80, generated here | Apache-2.0 model | cleared |',
        '| Fonts: Pinyon Script, Playfair Display | Google Fonts | SIL Open Font License | cleared |',
        '| Logo: CE monogram (`workflow/assets/logo_ce.png`, `logo_ce_dark.png`) | the channel\'s own | own | cleared |']
open(sys.argv[1] if len(sys.argv) > 1 else 'SOURCES-LOG.md', 'w').write('\n'.join(out) + '\n')
print('rows', len(first))
