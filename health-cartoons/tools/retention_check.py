import numpy as np, subprocess, sys
def frames(p,fps=10):
    raw=subprocess.run(['ffmpeg','-v','error','-i',p,'-vf',f'fps={fps},scale=72:128,format=gray','-f','rawvideo','-'],capture_output=True).stdout
    return np.frombuffer(raw,np.uint8).reshape(-1,128,72).astype(np.float32)
for name,p in [(a.split('=')[0],a.split('=')[1]) for a in sys.argv[1:]]:
    f=frames(p); d=np.abs(np.diff(f,axis=0)).mean(axis=(1,2))   # mean pixel change per 0.1s
    still=(d<0.15).mean()*100
    per_s=[d[i:i+10].mean() for i in range(0,len(d),10)]
    events=(d>4).sum()
    # longest stretch with almost nothing moving
    run=best=0
    for x in d:
        run=run+1 if x<0.3 else 0; best=max(best,run)
    print(f'{name:12s} dur={len(f)/10:5.1f}s  mean_motion={d.mean():.2f}  frozen%={still:4.1f}  big_changes={events:3d}  longest_nearly_static={best/10:.1f}s')
    print('   motion/sec:',' '.join(f'{x:.1f}' for x in per_s))
