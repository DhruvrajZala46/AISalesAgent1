# Verify an original post: python3 -I verify.py <tiktok url | tiktok short link> ...  -> author, title, followers (TikTok oEmbed + profile)
import sys, json, subprocess, re
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
def curl(a): return subprocess.run(["curl", "-sS", "-m", "30", "-A", UA] + a, capture_output=True).stdout.decode('utf-8', 'ignore')
def profile(h):
    t = curl(["-H", "Accept-Language: en-US", f"https://www.tiktok.com/@{h}"])
    m = re.search(r'<script id="__UNIVERSAL_DATA_FOR_REHYDRATION__" type="application/json">(.*?)</script>', t, re.S)
    if not m: return {}
    ui = json.loads(m.group(1)).get('__DEFAULT_SCOPE__', {}).get('webapp.user-detail', {}).get('userInfo', {})
    return {'followers': ui.get('stats', {}).get('followerCount'), 'bio': (ui.get('user', {}).get('signature') or '')[:160]}
for u in sys.argv[1:]:
    if '/t/' in u or 'vm.tiktok' in u:
        u = subprocess.run(["curl", "-sS", "-m", "30", "-o", "/dev/null", "-w", "%{redirect_url}", "-A", UA, u], capture_output=True).stdout.decode().split('?')[0]
    try: d = json.loads(curl([f"https://www.tiktok.com/oembed?url={u}"]))
    except Exception: d = {}
    h = d.get('author_unique_id')
    vid = re.search(r'/video/(\d+)', u)
    canon = f"https://www.tiktok.com/@{h}/video/{vid.group(1)}" if h and vid else u
    print(json.dumps({'url': canon, 'ok': bool(h), 'author': h, 'title': (d.get('title') or '')[:160], **(profile(h) if h else {})}, ensure_ascii=False))
