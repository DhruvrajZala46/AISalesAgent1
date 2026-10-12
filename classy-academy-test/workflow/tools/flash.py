import subprocess,re,os,sys,statistics
used=sorted(set(re.findall(r'assets/([^"]+\.mp4)',open('index.html').read())))
for f in used:
    o=subprocess.run(['ffprobe','-v','error','-f','lavfi','-i',f'movie=assets/{f},scale=160:-2,signalstats','-show_entries','frame=pts_time:frame_tags=lavfi.signalstats.YAVG','-of','csv=p=0'],capture_output=True,text=True).stdout
    v=[(float(a),float(b)) for a,b in (l.split(',')[:2] for l in o.split() if l.count(',')>=1 and l.split(',')[1])]
    if not v: continue
    med=statistics.median(y for _,y in v)
    bad=[t for t,y in v if y<med*0.45]
    if bad: print(f, 'median',round(med), 'dark frames',len(bad),'at',[round(x,1) for x in bad[:6]])
print('SCANNED',len(used))
