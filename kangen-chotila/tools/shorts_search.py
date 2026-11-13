import json, subprocess, time, sys
Q = ["health tips hindi shorts", "पानी पीने का सही तरीका shorts", "doctor health tips shorts hindi", "kidney stone shorts hindi",
     "alkaline water shorts hindi", "kangen water shorts", "पानी की कमी के लक्षण shorts", "RO water shorts hindi", "subah khali pet pani shorts",
     "body detox shorts hindi", "dehydration shorts hindi", "health facts hindi shorts viral", "copper water shorts", "garam pani peene ke fayde shorts",
     "pathri ka ilaj shorts", "kabj ka ilaj shorts", "sir dard ka karan shorts", "pani kab peena chahiye shorts", "dr health shorts water", "hydration shorts hindi doctor"]
out = {}
for q in Q:
    try: d = json.loads(subprocess.run(["yt-dlp", "--flat-playlist", "-J", f"ytsearch50:{q}"], capture_output=True, text=True, timeout=120).stdout)
    except Exception: print('FAIL', q); continue
    for e in d.get('entries') or []:
        if e.get('view_count') and (e.get('duration') or 999) <= 75:
            out.setdefault(e['id'], dict(id=e['id'], title=e.get('title'), views=e['view_count'], dur=e.get('duration'), ch=e.get('channel'), chid=e.get('channel_id'), q=q))
    print('ok', q, flush=True); time.sleep(1.5)
json.dump(out, open('shorts.json', 'w'), ensure_ascii=False, indent=0)
for x in sorted(out.values(), key=lambda x: -x['views'])[:70]:
    print(f"{x['views']:>11,} {x['dur']:>4}s {str(x['ch'])[:22]:22} | {x['title'][:85]} | {x['id']}")
