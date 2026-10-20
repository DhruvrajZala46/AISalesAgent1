# Public like counts via the Return YouTube Dislike API (it mirrors YouTube's public like count). One request per second.
import json, sys, time, urllib.request
ids = json.load(open(sys.argv[1])); out = {}
for v in ids:
    try: out[v] = json.loads(urllib.request.urlopen(urllib.request.Request(f'https://returnyoutubedislikeapi.com/votes?videoId={v}', headers={'User-Agent': 'curl/8.5.0'}), timeout=20).read())
    except Exception as e: out[v] = dict(err=str(e)[:80])
    time.sleep(1)
json.dump(out, open(sys.argv[2], 'w'), indent=0); print(len(out), 'done', sum('likes' in x for x in out.values()), 'with likes')
