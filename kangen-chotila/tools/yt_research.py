# yt_research.py - search YouTube (Hindi/English/Gujarati water & health), score each video vs its channel median
import json, subprocess, sys, time, statistics, os
OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
Q = [
 # Hindi / Hinglish
 "RO ka paani peena chahiye ya nahi", "paani peene ka sahi tarika", "paani peete samay ye galti", "pani kaise piye",
 "TDS kitna hona chahiye peene ka pani", "RO water nuksan", "alkaline water fayde sach", "kangen water hindi",
 "RO purifier paani barbaad", "fluoride wala pani", "kitna paani peena chahiye din me", "subah khali pet paani",
 "pani kam peene ke nuksan", "dehydration ke lakshan", "garmi me pani", "sardi me pani kam peena",
 "RO water vs normal water hindi", "matka vs RO pani", "bottle ka pani plastic", "kidney ke liye pani",
 "पानी पीने का सही तरीका", "आरओ का पानी", "पानी की कमी के लक्षण", "alkaline water kya hai",
 "pani shorts", "paani health shorts", "RO water shorts", "TDS meter test shorts",
 # English (India)
 "are you drinking water wrong", "alkaline water myth", "RO water side effects", "how much water should you drink",
 "water purifier wastage", "dehydration signs you ignore", "kangen water truth", "hydrogen water",
 "tds meter test tap water", "water mistakes shorts",
 # Gujarati
 "પાણી કેવી રીતે પીવું", "પાણી પીવાની સાચી રીત", "RO નું પાણી", "પાણી ગુજરાતી હેલ્થ", "gujarati health tips pani",
 "pani pivani sachi rit", "kangen water gujarati", "gujarati arogya tips",
]
def run(args, t=120):
    try: return subprocess.run(args, capture_output=True, text=True, timeout=t).stdout
    except Exception as e: return ''
vids = {}
for q in Q:
    o = run(["yt-dlp", "--flat-playlist", "-J", f"ytsearch40:{q}"])
    try: d = json.loads(o)
    except Exception: print('FAIL', q, flush=True); time.sleep(5); continue
    for e in d.get('entries') or []:
        if not e.get('id') or not e.get('view_count'): continue
        v = vids.setdefault(e['id'], dict(id=e['id'], title=e.get('title'), views=e['view_count'], dur=e.get('duration'),
            ch=e.get('channel'), chid=e.get('channel_id'), url=e.get('url'), queries=[]))
        v['queries'].append(q)
    print('ok', q, len(d.get('entries') or []), flush=True); time.sleep(1.5)
json.dump(vids, open(f'{OUT}/videos.json', 'w'), ensure_ascii=False, indent=0)
# channel medians: videos + shorts tabs, 60 most recent each
chs = {}
for v in vids.values():
    if v['chid']: chs.setdefault(v['chid'], []).append(v['views'])
order = sorted(chs, key=lambda c: -max(chs[c]))[:140]
med = {}
for c in order:
    allv = []
    for tab in ('videos', 'shorts'):
        o = run(["yt-dlp", "--flat-playlist", "-J", "--playlist-end", "60", f"https://www.youtube.com/channel/{c}/{tab}"], 90)
        try:
            d = json.loads(o); allv += [(tab, e.get('view_count')) for e in d.get('entries') or [] if e.get('view_count')]
        except Exception: pass
        time.sleep(1)
    lv = [x for t, x in allv if t == 'videos']; sv = [x for t, x in allv if t == 'shorts']
    med[c] = dict(videos=statistics.median(lv) if lv else None, shorts=statistics.median(sv) if sv else None, n=len(allv))
    print('ch', c, med[c], flush=True)
    json.dump(med, open(f'{OUT}/medians.json', 'w'), indent=0)
rows = []
for v in vids.values():
    m = med.get(v['chid'])
    if not m: continue
    short = (v['dur'] or 999) <= 180
    base = (m['shorts'] if short else m['videos']) or m['videos'] or m['shorts']
    if not base: continue
    v['short'] = short; v['median'] = base; v['score'] = round(v['views'] / max(base, 1), 2); rows.append(v)
rows.sort(key=lambda r: -r['score'])
json.dump(rows, open(f'{OUT}/ranked.json', 'w'), ensure_ascii=False, indent=0)
with open(f'{OUT}/ranked.md', 'w') as f:
    f.write('| score | views | channel median | dur | channel | title | id |\n|---|---|---|---|---|---|---|\n')
    for r in rows[:120]:
        f.write(f"| {r['score']}x | {r['views']:,} | {int(r['median']):,} | {r['dur']} | {r['ch']} | {r['title']} | {r['id']} |\n")
print('DONE', len(rows))
