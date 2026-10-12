import cv2,numpy as np,re,json,os,sys
# AI-watermark scan: finds the Google Gemini/Veo sparkle (✦) that AI video tools stamp in the bottom-right corner.
# usage (inside the work folder): python3 aiscan.py [clip keys...]   (default: every raw/*.mp4)
# score >= 0.60 = look at the corner yourself; 1.00 = the AI clip found in the French video. NEVER use a flagged clip.
F=os.getcwd()
def hp(a): return a-cv2.GaussianBlur(a,(0,0),6)
def med_corner(path,n=12,keep=None):
    cap=cv2.VideoCapture(path); N=int(cap.get(cv2.CAP_PROP_FRAME_COUNT)); fr=[]
    for k in range(n):
        cap.set(cv2.CAP_PROP_POS_FRAMES,int(N*(k+0.5)/n)); ok,im=cap.read()
        if ok: fr.append(cv2.cvtColor(cv2.resize(im,(720,1280)),cv2.COLOR_BGR2GRAY).astype(np.float32))
    cap.release()
    if len(fr)<3: return None
    return np.median(np.stack(fr),0)[-320:,-320:]
T=np.load(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','assets','gemini_star.npy'))
keys=sys.argv[1:] or sorted(set(f[:-4] for f in os.listdir(F+'/raw') if f.endswith('.mp4')))
res={}
for k in keys:
    m=med_corner(f'{F}/raw/{k}.mp4')
    if m is None: continue
    best=0
    for s in (0.8,0.9,1.0,1.1,1.25):
        t=cv2.resize(T,None,fx=s,fy=s)
        r=cv2.matchTemplate(hp(m),t,cv2.TM_CCOEFF_NORMED); best=max(best,float(r.max()))
    res[k]=best
json.dump(res,open('aiscan.json','w'))
flag=[k for k,v in res.items() if v>=0.60]
print('CHECK BY EYE / DO NOT USE:', flag if flag else 'none')
for k,v in sorted(res.items(),key=lambda z:-z[1])[:30]: print(f'{k:18} {v:.3f}')
