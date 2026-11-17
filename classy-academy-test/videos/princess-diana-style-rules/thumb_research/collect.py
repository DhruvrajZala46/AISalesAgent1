import json, os, sys, subprocess, re, glob
from concurrent.futures import ThreadPoolExecutor
W = sys.argv[1]
def search(q):
    import hashlib
    slug = re.sub(r'[^a-z0-9]+', '_', q.lower())
    if len(slug.strip('_')) < 6 or any(ord(c) > 127 for c in q): slug = 'q' + hashlib.md5(q.encode()).hexdigest()[:10]
    f = f"{W}/s/{slug}.json"
    if os.path.exists(f) and os.path.getsize(f) > 500: return q, True
    import time
    for k in range(4):
        r = subprocess.run(['yt-dlp', '--flat-playlist', '-J', f'ytsearch80:{q}'], capture_output=True, text=True)
        ok = False
        try: ok = len(json.loads(r.stdout).get('entries') or []) >= 10
        except Exception: pass
        if ok: open(f, 'w').write(r.stdout); return q, True
        time.sleep(15 * (k + 1))
    open(f + '.err', 'w').write(r.stderr[-2000:]); return q, False
qs = [l.strip() for l in open(W + '/q.txt') if l.strip()]
with ThreadPoolExecutor(2) as ex:
    a = list(ex.map(search, qs)); print('searches', sum(ok for _, ok in a), 'of', len(a), 'failed', [q for q, ok in a if not ok], flush=True)
print('SEARCH_DONE', flush=True)
