# find Hindi health Shorts channels, rank by MEDIAN views of their recent Shorts
import json, subprocess, time, statistics
Q = ["health facts hindi #shorts", "body facts in hindi shorts", "health tips in hindi #shorts viral", "sehat tips shorts hindi",
     "ayurvedic tips shorts hindi", "doctor advice hindi shorts", "pani health shorts hindi", "kidney health shorts hindi",
     "gut health hindi shorts", "liver health hindi shorts", "हेल्थ टिप्स #shorts", "स्वास्थ्य जानकारी shorts", "body ke raaz shorts", "health knowledge hindi shorts"]
def run(a, t=120):
    try: return subprocess.run(a, capture_output=True, text=True, timeout=t).stdout
    except Exception: return ''
chs = {}; mx = {}
for q in Q:
    try: d = json.loads(run(["yt-dlp", "--flat-playlist", "-J", f"ytsearch60:{q}"])) or {}
    except Exception: continue
    for e in d.get('entries') or []:
        if e and e.get('channel_id') and (e.get('duration') or 999) <= 90:
            chs.setdefault(e['channel_id'], e.get('channel')); mx[e['channel_id']] = max(mx.get(e['channel_id'], 0), e.get('view_count') or 0)
    time.sleep(1.2)
keep = sorted(chs, key=lambda c: -mx[c])[:60]
chs = {c: chs[c] for c in keep}
print(len(chs), 'channels', flush=True)
res = []
for cid, name in chs.items():
    try: d = json.loads(run(["yt-dlp", "--flat-playlist", "-J", "--playlist-end", "80", f"https://www.youtube.com/channel/{cid}/shorts"], 90)) or {}
    except Exception: continue
    vs = [(e.get('view_count') or 0, e.get('id'), e.get('title')) for e in d.get('entries') or [] if e and e.get('view_count')]
    if len(vs) < 15: continue
    med = statistics.median(v for v, _, _ in vs)
    res.append(dict(cid=cid, name=name, n=len(vs), median=med, top=sorted(vs, reverse=True)[:8]))
    print(f'{int(med):>10,} {name}', flush=True); time.sleep(1)
    json.dump(sorted(res, key=lambda r: -r['median']), open('shorts_channels.json', 'w'), ensure_ascii=False, indent=0)
print('DONE')
