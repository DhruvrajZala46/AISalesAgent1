# yt_medians.py research_dir - relevance-filter videos.json, fetch channel medians (videos + shorts tabs), rank by views / median
import json, subprocess, time, statistics, re, sys, os
D = sys.argv[1]
vids = json.load(open(f'{D}/videos.json'))
REL = re.compile(r'(पानी|पाणी|paani|pani\b|water|\bRO\b|TDS|hydrat|पेशाब|प्यास|પાણી|આરો|kidney|किडनी|alkaline|kangen|fluoride|purifier|filter|फिल्टर|आरओ|thirst)', re.I)
BAD = re.compile(r'(song|lyric|official video|official music|full video|cover|dance|trailer|nohay|remix|punjabi|haryanvi|bhojpuri|pani ?puri|golgappa|fails|experiment|miniature|गाना)', re.I)
rel = {k: v for k, v in vids.items() if REL.search(v['title'] or '') and not BAD.search(v['title'] or '') and (v['dur'] or 0) <= 1500 and v['chid']}
print(len(rel), 'relevant videos', flush=True)
chs = {}
for v in rel.values(): chs.setdefault(v['chid'], []).append(v['views'])
order = sorted(chs, key=lambda c: -max(chs[c]))[:120]
med = json.load(open(f'{D}/medians.json')) if os.path.exists(f'{D}/medians.json') else {}
def run(a, t=90):
    try: return subprocess.run(a, capture_output=True, text=True, timeout=t).stdout
    except Exception: return ''
for c in order:
    if c in med: continue
    allv = []
    for tab in ('videos', 'shorts'):
        o = run(["yt-dlp", "--flat-playlist", "-J", "--playlist-end", "60", f"https://www.youtube.com/channel/{c}/{tab}"])
        try: allv += [(tab, e.get('view_count')) for e in json.loads(o).get('entries') or [] if e.get('view_count')]
        except Exception: pass
        time.sleep(1)
    lv = [x for t, x in allv if t == 'videos']; sv = [x for t, x in allv if t == 'shorts']
    med[c] = dict(videos=statistics.median(lv) if lv else None, shorts=statistics.median(sv) if sv else None, n=len(allv))
    print('ch', c, med[c], flush=True); json.dump(med, open(f'{D}/medians.json', 'w'), indent=0)
rows = []
for v in rel.values():
    m = med.get(v['chid'])
    if not m: continue
    short = (v['dur'] or 999) <= 180
    base = (m['shorts'] if short else m['videos']) or m['videos'] or m['shorts']
    if not base: continue
    v.update(short=short, median=base, score=round(v['views'] / max(base, 1), 2)); rows.append(v)
rows.sort(key=lambda r: -r['score'])
json.dump(rows, open(f'{D}/ranked.json', 'w'), ensure_ascii=False, indent=0)
with open(f'{D}/ranked.md', 'w') as f:
    f.write('| score | views | channel median | sec | channel | title | id |\n|---|---|---|---|---|---|---|\n')
    for r in rows[:150]: f.write(f"| {r['score']}x | {r['views']:,} | {int(r['median']):,} | {r['dur']} | {r['ch']} | {r['title']} | {r['id']} |\n")
print('DONE', len(rows))
