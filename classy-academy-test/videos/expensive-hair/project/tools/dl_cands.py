# Download the verified creator clips listed in CLIP-CANDIDATES.md (first row per asset = best; second = alternate).
#   python3 dl_cands.py --list     (dry run: prints what would be downloaded)
#   python3 dl_cands.py            -> raw/<asset>_<k>.mp4 + raw/meta.json
import re, json, os, subprocess, sys, time
MD = '/home/user/AISalesAgent1/classy-academy-test/videos/expensive-hair/CLIP-CANDIDATES.md'
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/130.0 Safari/537.36"
TT = re.compile(r'^https://www\.tiktok\.com/@[\w.]+/video/(\d+)$')
IG = re.compile(r'^https://www\.instagram\.com/(reel|p)/[\w-]+/$')
rows = {}
for line in open(MD):
    if not (line.startswith('| A') or line.startswith('| (A')) or 'GAP' in line: continue
    c = [x.strip() for x in line.strip().strip('|').split('|')]
    ids = re.findall(r'A\d+[a-z]?', c[0])
    urls = re.findall(r'https://www\.(?:tiktok\.com/@[\w.]+/video/\d+|instagram\.com/(?:reel|p)/[\w-]+/)', line)
    for a in ids:
        for u in urls:
            if TT.match(u) or IG.match(u):
                rows.setdefault(a, []).append(dict(url=u, partial=('PARTIAL' in line or 'WEAK' in line), desc=c[2][:120], creator=c[4][:60] if len(c) > 4 else ''))
order = sorted(rows, key=lambda a: (int(re.search(r'\d+', a).group()), a))
if '--list' in sys.argv:
    for a in order: print(a, [r['url'] for r in rows[a][:2]])
    print(len(order), 'assets'); sys.exit()
os.makedirs('raw', exist_ok=True)
meta = json.load(open('raw/meta.json')) if os.path.exists('raw/meta.json') else {}


def tiktok(url, out):
    vid = TT.match(url).group(1)
    t = subprocess.run(['curl', '-sS', '-m', '40', '-A', UA, f'https://www.tiktok.com/embed/v2/{vid}'], capture_output=True).stdout.decode('utf-8', 'ignore')
    m = re.search(r'<script id="__FRONTITY_CONNECT_STATE__"[^>]*>(.*?)</script>', t, re.S)
    u = re.search(r'"urls":\["(https://[^"]+)"', m.group(1)) if m else None
    if not u: return False
    v = json.loads('"' + u.group(1) + '"')
    subprocess.run(['curl', '-sSL', '-m', '180', '-A', UA, '-H', 'Referer: https://www.tiktok.com/', '-o', out, v], capture_output=True)
    return os.path.exists(out) and os.path.getsize(out) > 50000


def insta(url, out):
    subprocess.run(['yt-dlp', '-q', '--no-warnings', '-f', 'bv*+ba/b', '--merge-output-format', 'mp4', '-o', out, url], capture_output=True, timeout=240)
    return os.path.exists(out) and os.path.getsize(out) > 50000


for a in order:
    for k, r in enumerate(rows[a][:2]):
        key = f'{a}_{k}'; out = f'raw/{key}.mp4'
        if meta.get(key, {}).get('ok'): continue
        ok = False
        try: ok = tiktok(r['url'], out) if TT.match(r['url']) else insta(r['url'], out)
        except Exception as e: print('ERR', key, e)
        meta[key] = dict(r, ok=ok, file=out if ok else None)
        print(key, 'ok' if ok else 'FAIL', r['url'], flush=True)
        json.dump(meta, open('raw/meta.json', 'w'), indent=1)
        time.sleep(3)
print('DLDONE', sum(1 for v in meta.values() if v['ok']), 'of', len(meta))
