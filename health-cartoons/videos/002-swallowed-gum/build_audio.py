import numpy as np, subprocess, json, os
SR=44100; FPS=30
def load(p): return np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',p,'-f','s16le','-ac','1','-ar',str(SR),'-'],capture_output=True).stdout,np.int16).astype(np.float32)/32768
SCRIPT={'01_gum':"Wheee! Wait... where am I?!",'02_stomach':"Oh great. He swallowed his gum. Again.",
 '03_gum':"Relax, big guy. I'm moving in. Seven years, baby!",'04_stomach':"Seven years? Says who?",
 '05_gum':"Everybody, bro! It's a classic!",'06_stomach':"Okay. Acid, melt him.",'07_gum':"Ha! Your acid can't even touch me!",
 '08_stomach':"Yeah, I can't digest you. But I can still kick you out.",'09_gum':"No, no, no! I signed a seven year lease!",
 '10_intestine':"Last stop: the toilet!",'11_gum':"Seven years, they said...",
 '12_stomach':"Uh-oh. He's swallowing the whole pack!",'13_gum':"We're one big blob now! Nobody gets through!",
 '14_patient':"Doc, my stomach hurts. Does swallowed gum really stay in there for seven years?",
 '15_doctor':"No, that's a myth. Your body can't digest gum, but it just passes through and comes out in a few days. The real danger is swallowing a lot at once, especially for kids. It can clump into a ball called a bezoar and block the gut.",
 '16_gum':"Next time... just spit me out."}
# placeholder lengths (s) for lines not generated yet
EST={'12_stomach':2.3,'13_gum':2.8,'14_patient':4.6,'15_doctor':14.5,'16_gum':2.3}
GAP={'01_gum':.75,'02_stomach':.18,'03_gum':.18,'04_stomach':.18,'05_gum':.15,'06_stomach':.18,'07_gum':.55,'08_stomach':.2,'09_gum':.25,
     '10_intestine':1.75,'11_gum':.15,'12_stomach':1.0,'13_gum':.45,'14_patient':.8,'15_doctor':.3,'16_gum':1.0}
W=json.load(open('words.json')); A={}; REAL={}
for k in SCRIPT:
    p=f'proc/{k}.wav'
    if os.path.exists(p): A[k]=load(p); REAL[k]=True
    else: A[k]=np.zeros(int(EST[k]*SR),np.float32); REAL[k]=False
t=0; START={}
for k in SCRIPT: t+=GAP[k]; START[k]=round(t,3); t+=len(A[k])/SR
END=round(t+2.0,3); N=int(END*SR); voice=np.zeros(N,np.float32); lines=[]
for k,t0 in START.items():
    a=A[k]; i=int(t0*SR); voice[i:i+len(a)]+=a
    hop=SR//FPS; env=[float(np.sqrt((a[j:j+hop]**2).mean())) for j in range(0,len(a),hop)]
    mx=max(env) or 1; env=[round(min(1,e/mx*1.35),3) if REAL[k] else 0 for e in env]
    sw=SCRIPT[k].replace('...',' ').split(); words=[]
    if REAL[k]:
        ww=W[k]
        for idx,w in enumerate(sw):
            s,e=(ww[idx][0],ww[idx][1]) if idx<len(ww) else (ww[-1][1],ww[-1][1]+.3)
            words.append([round(t0+s,3),round(t0+e,3),w.strip('.,!?:').upper()])
    else:
        d=len(a)/SR/len(sw)
        words=[[round(t0+i*d,3),round(t0+(i+1)*d,3),w.strip('.,!?:').upper()] for i,w in enumerate(sw)]
    lines.append({'id':k,'who':k.split('_')[1],'t0':t0,'dur':round(len(a)/SR,3),'env':env,'words':words})
def wt(k,word,n=0):
    L=[l for l in lines if l['id']==k][0]; m=[w for w in L['words'] if w[2]==word]; return m[n][0] if m else L['t0']
EV={'splash':START['01_gum']+.9,'stomachLbl':START['02_stomach'],'acid':wt('06_stomach','ACID'),'melt':wt('06_stomach','MELT'),
    'kick':wt('08_stomach','KICK'),'later':START['09_gum']+len(A['09_gum'])/SR+.15,'toilet':wt('10_intestine','TOILET'),
    'packStart':START['12_stomach']-0.8,'pack':wt('12_stomach','PACK'),'blob':START['13_gum'],'clinic':START['14_patient']-.55,
    'myth':wt('15_doctor','MYTH'),'passes':wt('15_doctor','PASSES'),'danger':wt('15_doctor','DANGER'),'clump':wt('15_doctor','CLUMP'),
    'bezoar':wt('15_doctor','BEZOAR'),'gut':wt('15_doctor','GUT'),'stinger':START['16_gum']-.7}
EV['flush']=START['11_gum']+len(A['11_gum'])/SR-.6
EV['cta']=START['16_gum']+len(A['16_gum'])/SR+.1
EV['intestine']=EV['later']+1.15
sfx=np.zeros(N,np.float32)
def S(f,t,g):
    a=load('../../assets/sfx/'+f)*g; i=max(0,int(t*SR)); n=min(len(a),N-i); sfx[i:i+n]+=a[:n]
S('2480.mp3',0.0,.35); S('2886.mp3',0.12,.22); S('2882.mp3',0.5,.55); S('2837.mp3',0.72,.7); S('1714.mp3',0.85,.35)
S('2457.mp3',EV['splash'],.55); S('2882.mp3',EV['stomachLbl']+.05,.3)
S('2457.mp3',EV['acid'],.4); S('123.mp3',EV['melt'],.30); S('2925.mp3',EV['melt']+.2,.4)
S('2151.mp3',START['07_gum']+.1,.4); S('1886.mp3',EV['kick'],.5); S('324.mp3',EV['kick']+.6,.45)
S('2886.mp3',START['09_gum']+.4,.35); S('2999.mp3',START['09_gum']+2.2,.45); S('1492.mp3',EV['later']-.1,.45)
S('1714.mp3',EV['intestine']-.2,.35); S('2886.mp3',START['10_intestine'],.3); S('1889.mp3',EV['flush'],.45); S('2894.mp3',EV['flush']+.9,.45)
for i in range(5): S('2457.mp3',EV['packStart']+.15+i*.32,.3)
S('1886.mp3',EV['blob']-.3,.5); S('473.mp3',EV['blob']+.2,.5)
S('1714.mp3',EV['clinic']-.2,.45); S('2882.mp3',EV['myth'],.4); S('1486.mp3',EV['passes']-.3,.3)
S('2882.mp3',EV['bezoar']-.1,.4); S('2151.mp3',EV['bezoar']+.15,.45); S('1492.mp3',EV['stinger']-.1,.45); S('2873.mp3',EV['cta'],.45)
mus=np.tile(load('../../assets/music/mixkit-9.mp3'),3)[:N]; fl=int(1.2*SR); mus[-fl:]*=np.linspace(1,0,fl)
for name,b in [('voice',voice),('sfx',sfx),('music',mus)]:
    subprocess.run(['ffmpeg','-v','error','-y','-f','f32le','-ar',str(SR),'-ac','1','-i','-',f'{name}.wav'],input=np.clip(b,-1,1).tobytes())
data={'end':END,'lines':lines,'ev':EV,'start':START,'real':REAL}
json.dump(data,open('data.json','w')); open('data.js','w').write('window.DATA='+json.dumps(data)+';')
print('END',END); print({k:round(v,2) for k,v in EV.items()})
