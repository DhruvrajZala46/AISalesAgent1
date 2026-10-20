# Deep metrics per video (public): exact upload date, views, likes, comment count, duration, subs, tags, chapters, description head.
# yt-dlp first (no login), the public watch page as fallback; spaced to respect YouTube's rate limit. Resumable.
import json, subprocess, sys, time, re, os, urllib.request
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
OUT = sys.argv[1]; ids = sys.argv[2:] if len(sys.argv) > 2 else []
if len(ids) == 1 and ids[0].endswith('.json'): ids = json.load(open(ids[0]))
out = json.load(open(OUT)) if os.path.exists(OUT) else {}
for vid in ids:
    if vid in out and not out[vid].get('err'): continue
    m = None
    r = subprocess.run(['timeout', '90', 'yt-dlp', '-J', '--skip-download', '--no-warnings', f'https://www.youtube.com/watch?v={vid}'], capture_output=True, text=True)
    try: m = json.loads(r.stdout)
    except Exception: pass
    if m:
        out[vid] = dict(title=m.get('title'), channel=m.get('channel'), channel_id=m.get('channel_id'), subs=m.get('channel_follower_count'), date=m.get('upload_date'),
                        views=m.get('view_count'), likes=m.get('like_count'), comments=m.get('comment_count'), duration=m.get('duration'),
                        tags=(m.get('tags') or [])[:20], chapters=[c.get('title') for c in (m.get('chapters') or [])], desc=(m.get('description') or '')[:600], src='yt-dlp')
    else:
        try:
            h = urllib.request.urlopen(urllib.request.Request(f'https://www.youtube.com/watch?v={vid}', headers={'User-Agent': UA, 'Accept-Language': 'en'}), timeout=30).read().decode('utf-8', 'ignore')
            g = lambda rx: (re.search(rx, h) or [None, None])[1]
            lk = g(r'like this video along with ([\d,]+) other') 
            out[vid] = dict(title=g(r'<meta name="title" content="([^"]+)'), channel=g(r'"ownerChannelName":"([^"]+)'), channel_id=g(r'"externalChannelId":"([^"]+)'),
                            date=(g(r'"uploadDate":"([^"]+)') or '')[:10].replace('-', ''), views=int(g(r'"viewCount":"(\d+)"') or 0),
                            likes=int(lk.replace(',', '')) + 1 if lk else None, comments=None, duration=int(g(r'"lengthSeconds":"(\d+)"') or 0), src='watch page',
                            err=None if g(r'"uploadDate":"([^"]+)') else 'no data: ' + r.stderr[-80:])
        except Exception as e: out[vid] = dict(err=str(e)[:100] + ' | ' + r.stderr[-80:])
    if 'err' in out[vid] and out[vid]['err'] and '429' in str(out[vid]['err']):
        print(vid, '429 - backing off 300s', flush=True); time.sleep(300)
    print(vid, out[vid].get('src'), out[vid].get('date'), out[vid].get('views'), out[vid].get('likes'), out[vid].get('comments'), out[vid].get('err') or '', flush=True)
    json.dump(out, open(OUT, 'w'), indent=1, ensure_ascii=False)
    time.sleep(int(os.environ.get('GAP', '12')))
print('DONE')
