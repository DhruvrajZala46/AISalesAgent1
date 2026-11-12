import subprocess, numpy as np, sys
rise=float(sys.argv[1]); dur=float(sys.argv[2]); exclude=sys.argv[3:] 
best=None
import os
for m in os.environ.get("TRACKS","m711 m712 m716 m717").split():
    raw=subprocess.run(f"ffmpeg -nostdin -v error -i assets/{m}.mp3 -ac 1 -ar 8000 -f s16le -",shell=True,capture_output=True).stdout
    a=np.frombuffer(raw,dtype=np.int16).astype(np.float32)/32768; sec=4000; n=len(a)//sec
    db=20*np.log10(np.array([np.sqrt(np.mean(a[i*sec:(i+1)*sec]**2))+1e-6 for i in range(n)]))
    r=int(rise*2); L=int(dur*2)
    for s in range(0,n-L):
        if any(e==f"{m}@{s/2}" for e in exclude): continue
        pre=db[s:s+r].mean(); post=db[s+r:s+L].mean(); mn=db[s+r:s+L].min()
        sc=(post-pre)-0.2*max(0,-35-mn)
        if pre>-42 and (best is None or sc>best[0]): best=(sc,m,s/2)
print(best[1], best[2], round(float(best[0]),1))
