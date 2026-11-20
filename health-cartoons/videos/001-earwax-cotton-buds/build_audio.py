import numpy as np, subprocess, json
SR=44100; FPS=30
def load(p): return np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',p,'-f','s16le','-ac','1','-ar',str(SR),'-'],capture_output=True).stdout,np.int16).astype(np.float32)/32768
SCRIPT={'a01_wax':"Huh?! What's that fluffy thing doing in here?",'a02_swab':"Cleaning crew! This ear's getting scrubbed!",
 'a03_wax':"Wait, wait! I was already leaving on my own!",'a04_swab':"Sure you were. In you go!",
 'a05_wax':"Ow! Not deeper! The eardrum's back there!",'a06_swab':"There! Spotless!",
 'a07_drum':"Hey! Who's leaning on me?! I can't vibrate!",'a08_wax':"Don't look at me! Fluffy did this!",
 'a09_swab':"Huh? Why'd it get so quiet in here?",
 'a10_patient':"Doc, my ear feels blocked and everything sounds muffled. But I clean it with cotton buds every single day!",
 'a11_doctor':"That's the problem. Your ears clean themselves. Earwax slowly moves out on its own. Cotton buds push it back in, and it gets packed deep, right next to your eardrum. That's called earwax impaction. Only clean the outer ear, and let a doctor remove a blockage.",
 'a12_swab':"Fine... I'll just stay outside."}
GAP={'a01_wax':0.45,'a02_swab':.2,'a03_wax':.22,'a04_swab':.2,'a05_wax':.5,'a06_swab':.18,'a07_drum':.55,'a08_wax':.2,'a09_swab':.25,'a10_patient':.75,'a11_doctor':.3,'a12_swab':1.0}
W=json.load(open('words.json')); A={k:load(f'proc/{k}.wav') for k in SCRIPT}
t=0; lines=[]; START={}
for k in SCRIPT:
    t+=GAP[k]; START[k]=round(t,3); t+=len(A[k])/SR
END=round(t+1.9,3)
N=int(END*SR); voice=np.zeros(N,np.float32)
def wt(k,word,n=0):
    sw=SCRIPT[k].replace('...',' ').split(); idx=[i for i,w in enumerate(sw) if w.strip('.,!?').upper()==word][n]
    return START[k]+W[k][min(idx,len(W[k])-1)][0]
for k,t0 in START.items():
    a=A[k]; i=int(t0*SR); voice[i:i+len(a)]+=a
    hop=SR//FPS; env=[float(np.sqrt((a[j:j+hop]**2).mean())) for j in range(0,len(a),hop)]
    mx=max(env) or 1; env=[round(min(1,e/mx*1.35),3) for e in env]
    sw=SCRIPT[k].replace('...',' ').split(); ww=W[k]; words=[]
    for idx,w in enumerate(sw):
        s,e=(ww[idx][0],ww[idx][1]) if idx<len(ww) else (ww[-1][1],ww[-1][1]+.3)
        words.append([round(t0+s,3),round(t0+e,3),w.strip('.,!?').upper()])
    lines.append({'id':k,'who':k.split('_')[1],'t0':t0,'dur':round(len(a)/SR,3),'env':env,'words':words})
EV={'go':wt('a04_swab','GO'),'eardrumWord':wt('a05_wax',"EARDRUM'S"),'there':wt('a06_swab','THERE'),'leaving':wt('a03_wax','LEAVING'),
    'quiet':wt('a09_swab','QUIET'),'clinic':START['a10_patient']-0.5,'themselves':wt('a11_doctor','THEMSELVES'),'outOwn':wt('a11_doctor','OUT'),
    'push':wt('a11_doctor','PUSH'),'impaction':wt('a11_doctor','IMPACTION'),'only':wt('a11_doctor','ONLY'),'blockage':wt('a11_doctor','BLOCKAGE'),
    'stinger':START['a12_swab']-0.75,'scrub':START['a02_swab'],'drum':START['a07_drum']}
EV['cta']=START['a12_swab']+len(A['a12_swab'])/SR+0.1
sfx=np.zeros(N,np.float32)
def place(f,t,g):
    a=load('../../assets/sfx/'+f)*g; i=int(t*SR); n=min(len(a),N-i); sfx[i:i+n]+=a[:n]
S=place
S('1492.mp3',0.0,.5); S('1714.mp3',0.55,.35); S('2882.mp3',1.15,.35); S('2882.mp3',1.6,.25)
S('2886.mp3',EV['scrub']+.2,.35); S('2151.mp3',EV['leaving'],.5)
S('2209.mp3',EV['go']+.05,.95); S('92.mp3',EV['go']+.15,.5); S('324.mp3',EV['go']+.3,.55)
S('2882.mp3',EV['eardrumWord'],.3); S('1886.mp3',START['a05_wax']+.8,.45)
S('2209.mp3',EV['there']+.1,.9); S('473.mp3',EV['there']+.25,.6); S('391.mp3',EV['there']+.4,.35)
S('2894.mp3',START['a09_swab']+2.95,.55); S('1714.mp3',EV['clinic']-.25,.45)
S('1486.mp3',EV['themselves']+.6,.3); S('2882.mp3',EV['impaction']-.1,.4); S('2151.mp3',EV['impaction']+.15,.45)
S('2882.mp3',EV['only'],.35); S('1492.mp3',EV['stinger']-.1,.45); S('2873.mp3',EV['cta'],.45)
mus=np.tile(load('../../assets/music/mixkit-9.mp3'),2)[:N]
from math import exp
q0,q1=EV['quiet']-0.9, START['a10_patient']-0.5
lp=mus.copy(); y=0; al=1-exp(-2*np.pi*350/SR)
for i in range(int((q0-.3)*SR),int((q1+.3)*SR)): y+=al*(mus[i]-y); lp[i]=y
m=np.zeros(N,np.float32); a0,a1,b0,b1=[int(x*SR) for x in (q0,q0+.4,q1-.25,q1)]
m[a0:a1]=np.linspace(0,1,a1-a0); m[a1:b0]=1; m[b0:b1]=np.linspace(1,0,b1-b0)
mus=mus*(1-m)+lp*m*1.6; fl=int(1.2*SR); mus[-fl:]*=np.linspace(1,0,fl)
for name,b in [('voice',voice),('sfx',sfx),('music',mus)]:
    subprocess.run(['ffmpeg','-v','error','-y','-f','f32le','-ar',str(SR),'-ac','1','-i','-',f'{name}.wav'],input=np.clip(b,-1,1).tobytes())
json.dump({'end':END,'lines':lines,'ev':EV,'start':START},open('data.json','w'))
open('data.js','w').write('window.DATA='+json.dumps({'end':END,'lines':lines,'ev':EV,'start':START})+';')
print('END',END); print({k:round(v,2) for k,v in EV.items()}); print(START)
