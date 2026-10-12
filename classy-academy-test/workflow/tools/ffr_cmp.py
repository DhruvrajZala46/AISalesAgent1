# ffr_cmp.py - checks the fast renderer against the browser before a full render.
# first: npx hyperframes snapshot --at 5,40,100,200,350,450,530,560 --no-end -o snapcmp   (pick moments with every layout)
# then (inside the work folder): python3 ffr_cmp.py  -> mean pixel difference per moment (< 10 = same) + ffr_cmp_N.jpg sheets
import sys,glob,re,os,cv2,numpy as np
sys.argv=['ffr.py','.','0','1','x.mp4','1']
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ffr.py')).read().split("if __name__ == '__main__':")[0])
rows=[]
for f in sorted(glob.glob('snapcmp/frame-*.png')):
    t=float(re.search(r'at-([\d.]+)s',f).group(1))
    ref=cv2.imread(f)[..., :3]
    if ref.shape[1]!=1920: ref=cv2.resize(ref,(1920,1080))
    CLIPS.clear()
    me=cv2.convertScaleAbs(render(t))
    for c in CLIPS.values(): c.close()
    d=np.abs(ref.astype(int)-me.astype(int)).mean()
    print(f'{t:7.2f}s  mean abs diff {d:5.2f}', flush=True)
    a=cv2.resize(ref,(640,360)); b=cv2.resize(me,(640,360))
    cv2.putText(a,f'browser {t}',(8,24),0,0.7,(0,0,255),2); cv2.putText(b,'fast',(8,24),0,0.7,(0,0,255),2)
    rows.append(np.hstack([a,b]))
for i in range(0, len(rows), 8): cv2.imwrite(f'ffr_cmp_{i // 8}.jpg', np.vstack(rows[i:i + 8]))
