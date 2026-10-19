# credits_build.py - builds the credit records from the checked evidence in credits-evidence/ (19 Oct 2026):
#   every file the final timeline shows (used.json, from timeline.json), its creator as verified on the platform itself
#   (TikTok embed author, Instagram embed author), and the hand-checked Pinterest, photo and music traces (manual_trace.json).
#   python3 -I credits_build.py   -> ../CREDITS-CHECKLIST.md, ../CREDITS-PINNED-COMMENT.txt, ../credits-evidence/visual_credits_block.txt
import json, os, re
V = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + '/../..'); EV = V + '/credits-evidence'
used = json.load(open(f'{EV}/used.json')); src = {s['file']: s for s in json.load(open(f'{EV}/sources.json'))}
tt = {x['url']: x for x in json.load(open(f'{EV}/tiktok_verify.json'))}
ig = {x['url']: x for x in map(json.loads, open(f'{EV}/instagram_verify.jsonl'))}
man = json.load(open(f'{EV}/manual_trace.json')); pins = json.load(open(f'{EV}/pinterest_pins.json'))
# what a post's own caption says about who made or features the clip (read from the captions in instagram_verify.jsonl)
NOTE = {'samvillahair': 'stylist @bytaylorchere', 'therighthairstyles': 'stylist @tressesbytress',
        'treasuretress': 'video credited to @ramataabah'}


def ts(t): return f'{int(t // 60)}:{int(t % 60):02d}'


rows = []
for path, us in used.items():
    f = os.path.basename(path); s = src[f]; first = min(u['t0'] for u in us)
    scenes = sorted({u['scene'] for u in us}); spans = ', '.join(f"{ts(u['t0'])}-{ts(u['t1'])}" for u in sorted(us, key=lambda u: u['t0']))
    kind = 'photo' if f.endswith('.jpg') else 'video clip'
    if s['kind'] == 'post':
        if 'tiktok.com' in s['url']:
            v = tt[s['url']]; ok = v['match'] and v['embed_ok']
            r = dict(platform='TikTok', handle=v['author'], status='VERIFIED' if ok else 'CHECK', link=s['url'],
                     how=f"TikTok embed of the post shows author @{v['author']} ({v['name']})")
        else:
            v = ig[s['url']]; who = v['user'].split()[0]          # the embed adds 'Verified' after a verified account's name
            r = dict(platform='Instagram', handle=who, status='VERIFIED', link=s['url'],
                     how=f"Instagram embed of the post shows author @{who}")
        r['credit'] = '@' + r['handle'] + (f" ({NOTE[r['handle']]})" if r['handle'] in NOTE else '')
    elif f in man['photos']:
        m = man['photos'][f]
        r = dict(platform='Editorial photo', handle=None, status=m['status'], link=m['source'], credit=m['credit'],
                 how=m['evidence'], short=m['description_credit'])
    else:
        m = man['pinterest'][f]; p = pins[f]
        r = dict(platform='Instagram (via Pinterest)' if 'instagram.com' in (m['credit_link'] or '') else 'Pinterest',
                 handle=None, status=m['status'], link=m['credit_link'], credit=m['credit'], how=m['evidence'],
                 pin=p['pin_url'], uploader=p['uploader'], short=m.get('description_credit'))
    r.update(file=f, kind=kind, first=first, scenes=scenes, spans=spans)
    rows.append(r)
rows.sort(key=lambda r: r['first'])

# 1. the checklist: one row per file shown in the video
md = ["# Credit checklist: Why Her Hair Always Looks Expensive (It's Not the Cut)", '',
      'Every third-party picture in the final export (`Why_Her_Hair_Always_Looks_Expensive_CE_1080p.mp4`, 10:57), one row per file, in order of',
      'first appearance. Built by `project/tools/credits_build.py` from the evidence in `credits-evidence/`. **Permission: none obtained for any row**',
      '(see `CREDITS-ISSUES.md`).', '',
      '- **VERIFIED:** the platform itself names this creator as the author of this post (TikTok or Instagram embed), or the photo credit was read',
      '  from the publisher and the picture matched pixel by pixel.',
      '- **IDENTIFIED:** the uploader is the creator\'s own account (own branding in the clip, own website, own shoot), but the creator\'s original post',
      '  elsewhere was not found.',
      '- **ATTRIBUTED / PUBLISHER IDENTIFIED:** a name is on the clip or the pin, but it could not be confirmed at the source.',
      '- **UNVERIFIED:** the original creator is unknown; the Pinterest re-upload is the only source.', '',
      '| # | First seen | Scenes | On screen | File | Type | Platform | Credit | Original / source link | Status | How it was checked |',
      '|---|---|---|---|---|---|---|---|---|---|---|']
for k, r in enumerate(rows, 1):
    how = r['how'].replace('|', '/')
    if r.get('pin') and r['pin'] != r['link']: how += f" Pinterest pin: {r['pin']} (uploader {r['uploader']})."
    elif r.get('uploader'): how += f" (uploader {r['uploader']})"
    md.append(f"| {k} | {ts(r['first'])} | {', '.join(map(str, r['scenes']))} | {r['spans']} | `{r['file']}` | {r['kind']} | {r['platform']} | "
              f"{r['credit'] or 'UNVERIFIED (uploaded to Pinterest by ' + r['uploader'] + ')'} | {r['link']} | {r['status']} | {how} |")
cnt = {}
for r in rows: cnt[r['status'].split(' (')[0]] = cnt.get(r['status'].split(' (')[0], 0) + 1
md += ['', '## Totals', '', f'- Files shown: **{len(rows)}** ({sum(r["kind"] == "video clip" for r in rows)} video clips, '
       f'{sum(r["kind"] == "photo" for r in rows)} photos).']
md += [f'- {k}: {v}' for k, v in sorted(cnt.items(), key=lambda x: -x[1])]
posts = {r['link'] for r in rows if r['platform'] in ('TikTok', 'Instagram', 'Instagram (via Pinterest)')}
md += [f'- Distinct original posts verified on TikTok / Instagram: {len(posts)}.',
       f'- Distinct creators credited by handle: {len({r["credit"].split(" (")[0] for r in rows if r["credit"] and r["credit"].startswith("@")})}.', '',
       '## Audio', '',
       '| What | Where it is heard | Credit | Licence | Evidence |', '|---|---|---|---|---|']
mu = man['music']
for fn, x in mu['files'].items():
    md.append(f"| Chopin, {x['piece']} | music bed under the voice, 0:00-10:46, and the end-card swell | performed by "
              f"{x['performer_tag'].replace(' (sic, the file tag; read as Olga Gurevich)', '')}; recording: Musopen | CC0 1.0 (public domain dedication) | "
              f"md5 {x['md5']} = the archive.org item's file; Musopen's own upload: {x['musopen_own_upload_match']} |")
md += [f"| Narration | the whole voice track | synthetic voice: {man['narration']['what']} | Kokoro-82M Apache-2.0; kokoro-onnx MIT | "
       f"{man['narration']['note']} |",
       '| Sound from the clips | none | - | - | every clip is muted; `mix.py` mixes only the voice, the music bed and the swell |', '',
       f"Music download: {mu['downloaded_from']} (licence field: {mu['downloaded_item']['licenseurl']}; uploaded {mu['downloaded_item']['publicdate']} by "
       f"{mu['downloaded_item']['uploader']}). Musopen's own item: {mu['musopen_own_item']['url']} (uploaded by Musopen, licence "
       f"{mu['musopen_own_item']['licenseurl']}). File tags: {mu['file_tags']}.", '',
       '## Other', '',
       '- Fonts: Pinyon Script and Playfair Display (Google Fonts, SIL Open Font License; no credit needed).',
       '- Logo: CE / The Classy Elegance, the channel\'s own.',
       '- Thumbnail photos are not in the video; they are listed in `CREDITS-ISSUES.md`.']
open(f'{V}/CREDITS-CHECKLIST.md', 'w').write('\n'.join(md) + '\n')

# 2. the description's VISUAL CREDITS lines: each creator once, in order of first appearance, grouped by where the credit was verified
seen = set(); groups = {'Instagram': [], 'TikTok': []}; idn, attr, unv, photos = [], [], [], []
for r in rows:
    key = r['credit'] or r['link']
    if key in seen: continue
    seen.add(key)
    if r['platform'] in ('Instagram', 'Instagram (via Pinterest)'): groups['Instagram'].append(r['credit'])
    elif r['platform'] == 'TikTok': groups['TikTok'].append(r['credit'])
    elif r['platform'] == 'Editorial photo': photos.append(r)
    elif r['status'].startswith('IDENTIFIED'): idn.append(r['short'])
    elif r['status'].startswith(('ATTRIBUTED', 'PUBLISHER')): attr.append(r['short'])
    else: unv.append(r)
blk = ['Instagram: ' + ', '.join(groups['Instagram']), '', 'TikTok: ' + ', '.join(groups['TikTok']), '',
       'Found on Pinterest: ' + ', '.join(idn + attr), '',
       'Andie MacDowell at Cannes 2021: ' + '; '.join(p['short'] for p in photos), '',
       'Clips found on Pinterest whose original creator we could not confirm: '
       + ', '.join(re.sub(r'https://www\.', '', r['link']).rstrip('/') for r in unv) + '. If one of these is yours, comment below and we will add your name.']
open(f'{EV}/visual_credits_block.txt', 'w').write('\n'.join(blk) + '\n')

# 3. a pinned comment with the link to every original post (the description has no room for 100+ links)
pc = ['Thank you to every creator in this video. The original posts:', '']
seen = set()
for r in rows:
    if r['link'] in seen: continue
    seen.add(r['link'])
    who = r.get('short') or r['credit'] or ('creator not confirmed, uploaded by ' + r['uploader'])
    if r['platform'] == 'Editorial photo': who = 'Andie MacDowell, ' + who
    pc.append(f"{ts(r['first'])} {who}: {re.sub(r'https://(www\.)?', '', r['link']).rstrip('/')}")
open(f'{V}/CREDITS-PINNED-COMMENT.txt', 'w').write('\n'.join(pc) + '\n')
print('rows', len(rows), cnt, '| block chars', len('\n'.join(blk)), '| comment chars', len('\n'.join(pc)))
