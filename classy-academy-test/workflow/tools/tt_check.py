# usage: python3 -I tt_check.py urls.txt out.json   (one TikTok video URL per line)
# tt_check.py - who posted each TikTok video, read from TikTok's own public embed page (oEmbed no longer returns the author)
import sys, re, json, subprocess, time
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
out = []
for u in open(sys.argv[1]).read().split():
    vid = re.search(r'/video/(\d+)', u).group(1); url_user = re.search(r'tiktok\.com/@([^/]+)/', u).group(1)
    t = subprocess.run(['curl', '-sS', '-m', '40', '-A', UA, f'https://www.tiktok.com/embed/v2/{vid}'], capture_output=True).stdout.decode('utf-8', 'ignore')
    m = re.search(r'"uniqueId":"([^"]+)","nickName":"([^"]*)"', t)
    out.append(dict(url=u, video_id=vid, url_user=url_user, embed_ok=bool(m) and vid in t, author=m.group(1) if m else None, name=m.group(2) if m else None,
                    match=bool(m) and m.group(1).lower() == url_user.lower()))
    time.sleep(1)
json.dump(out, open(sys.argv[2], 'w'), indent=1)
print(sum(o['match'] for o in out), 'of', len(out), 'authors confirmed;', [o['url'] for o in out if not o['match']])
