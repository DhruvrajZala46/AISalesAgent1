#!/bin/bash
# subs.sh OUTDIR id... : auto-captions (en-orig/en) via yt-dlp android_vr player JSON + direct caption URL
OUT=$1; shift; mkdir -p $OUT
for id in "$@"; do
  [ -s $OUT/$id.txt ] && continue
  for try in 1 2 3; do
    timeout 120 yt-dlp --js-runtimes node -J --skip-download --extractor-args "youtube:player_client=android_vr" "https://www.youtube.com/watch?v=$id" 2>/dev/null > $OUT/$id.info.json
    [ -s $OUT/$id.info.json ] && break; sleep 5
  done
  python3 - "$OUT" "$id" <<'PY'
import json,sys,urllib.request
out,i=sys.argv[1],sys.argv[2]
try: d=json.load(open(f'{out}/{i}.info.json')); assert d
except Exception: print(i,'no info'); sys.exit()
ac=d.get('automatic_captions') or {}; sc=d.get('subtitles') or {}; d['language']=d.get('language') or ''
lang=d.get('language') or ''
url=None
for src in (sc,ac):
  for k in ['en-orig']+[x for x in src if x.endswith('-orig')]+['en',lang]:
    for f in src.get(k,[]) or []:
      if f.get('ext')=='json3': url=f['url']; break
    if url: break
  if url: break
if not url: print(i,'no captions'); sys.exit()
j=json.load(urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=30))
lines=[]
for e in j.get('events',[]):
  t=''.join(s.get('utf8','') for s in e.get('segs',[]) or []).strip()
  if t: lines.append(f"[{e['tStartMs']//1000}s] {t}")
open(f'{out}/{i}.txt','w').write('\n'.join(lines)); print(i,lang,len(lines),'lines')
PY
  sleep 8
done
