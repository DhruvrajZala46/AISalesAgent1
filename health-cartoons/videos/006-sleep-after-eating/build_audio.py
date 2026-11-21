# 006: voice/sfx/music + data.js from proc/*.wav + words.json. The timeline follows the 26M reference shot list (script.md):
# stomach eats -> more food drops -> the brain yawns and puts on a sleep mask -> the "plan" -> masks on -> black card -> gas -> the man burps.
import numpy as np, subprocess, json, re
SR=44100; FPS=30
def load(p): return np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',p,'-f','s16le','-ac','1','-ar',str(SR),'-'],capture_output=True).stdout,np.int16).astype(np.float32)/32768
W=json.load(open('words.json'))
ORDER=['01_stomach','02_stomach','03_stomach','04_stomach','05_stomach','06_brain','07_stomach','08_stomach','09_brain','10_buddy','11_buddy',
       '12_stomach','13_stomach','14_stomach','15_buddy','16_stomach','17_stomach','18_buddy','19_stomach','20_buddy','21_stomach','22_stomach','23_man','24_man']
GAP={'01_stomach':.5,'02_stomach':.85,'03_stomach':.18,'04_stomach':.15,'05_stomach':.35,
     '06_brain':.8,            # cut to the brain
     '07_stomach':.2,'08_stomach':.15,'09_brain':.35,
     '10_buddy':1.15,            # the brain's mask goes on, cut back to the stomach
     '11_buddy':.15,'12_stomach':.2,'13_stomach':.15,'14_stomach':.2,'15_buddy':.3,'16_stomach':.2,'17_stomach':.15,'18_buddy':.25,'19_stomach':.2,
     '20_buddy':4.4,            # SILENT: masks on (1.0 s), black card "A FEW HOURS LATER" (1.7 s), green gas fills the stomach (1.9 s)
     '21_stomach':.2,'22_stomach':.2,
     '23_man':1.0,              # cut to the bedroom
     '24_man':.2}
FIX={'MMM':'MMM','POSITIVE':'POSITIVE'}
A={k:load(f'proc/{k}.wav') for k in ORDER}
for k in ORDER:   # even out line loudness (004 lesson)
    act=A[k][np.abs(A[k])>0.01]; db=20*np.log10(np.sqrt((act**2).mean())+1e-9); g=float(np.clip((-19-db)*.8,-6,10)); A[k]=A[k]*10**(g/20)
t=0; START={}
for k in ORDER: t+=GAP[k]; START[k]=round(t,3); t+=len(A[k])/SR
END=round(t+3.3,3); N=int(END*SR); voice=np.zeros(N,np.float32); lines=[]
for k in ORDER:
    a=A[k]; t0=START[k]; i=int(t0*SR); voice[i:i+len(a)]+=a
    hop=SR//FPS; env=[float(np.sqrt((a[j:j+hop]**2).mean())) for j in range(0,len(a),hop)]
    mx=max(env) or 1; env=[round(min(1,e/mx*1.35),3) for e in env]
    words=[]
    for s,e,w in W[k]:
        u=re.sub(r"[^A-Za-z'\-]","",w).upper(); u=FIX.get(u,u)
        if u: words.append([round(t0+s,3),round(t0+e,3),u])
    if k=='06_brain':   # whisper hears the long yawn as words: show it as one caption word
        i=next((j for j,w in enumerate(words) if w[2]=='LONG'),0); words=([[words[0][0],words[i-1][1],'YAAAWN']] if i else [])+words[i:]
    if k=='23_man': words=[[w[0],w[1],'*BURP*'] if w[2]=='UGH' else w for w in words]
    lines.append({'id':k,'who':k.split('_')[1],'t0':t0,'dur':round(len(a)/SR,3),'env':env,'words':words})
def wt(k,word,n=0):
    L=[l for l in lines if l['id']==k][0]; m=[w for w in L['words'] if w[2]==word]; return m[n][0] if m else L['t0']
def lend(k): return START[k]+len(A[k])/SR
EV={'drop':START['02_stomach']-.75,'brain':START['06_brain']-.45,'shout':START['07_stomach']-.1,'mask':START['09_brain']+.2,'back':START['10_buddy']-.6,
    'habit':wt('13_stomach','HABIT'),'easy':START['16_stomach'],'masks':lend('19_stomach')+.25,'card':lend('19_stomach')+1.25,'gas':lend('19_stomach')+2.95,
    'wake':START['20_buddy']-.35,'hydrogen':wt('21_stomach','HYDROGEN'),'bed':START['23_man']-.6,'burp':START['23_man']+.05,
    'tip':lend('24_man')+.15,'cta':lend('24_man')+1.6}
sfx=np.zeros(N,np.float32)
def S(f,t,g,dur=None):
    a=load('../../assets/sfx/'+f)*g
    if dur: a=a[:int(dur*SR)].copy(); fl=min(len(a),int(.25*SR)); a[-fl:]*=np.linspace(1,0,fl)
    i=max(0,int(t*SR)); n=min(len(a),N-i); sfx[i:i+n]+=a[:n]
# SFX (Mixkit ids checked, PLAYBOOK section 3): chewing squish, the food drop, the yawn, sound waves, masks, clock, crickets, gas, burp
S('1886.mp3',.3,.3); S('1884.mp3',1.4,.25)
S('1464.mp3',EV['drop'],.45); S('2890.mp3',EV['drop']+.55,.4); S('2364.mp3',EV['drop']+.6,.35); S('2364.mp3',EV['drop']+.75,.3)
S('1492.mp3',EV['brain']-.1,.35); S('1464.mp3',EV['shout'],.35); S('1464.mp3',START['08_stomach'],.3)
S('2358.mp3',EV['mask'],.4); S('1492.mp3',EV['back']-.1,.35); S('2357.mp3',EV['habit'],.35); S('2149.mp3',EV['easy']+.3,.3)
S('2358.mp3',EV['masks'],.4); S('2358.mp3',EV['masks']+.25,.35); S('1060.mp3',EV['card'],.4,1.7); S('1789.mp3',EV['card'],.25,1.7)
S('1321.mp3',EV['gas'],.35,1.8); S('732.mp3',EV['gas']+.4,.3); S('473.mp3',EV['hydrogen']-.2,.25)
S('1492.mp3',EV['bed']-.1,.35); S('1789.mp3',EV['bed'],.2,7.0); S('2357.mp3',EV['tip'],.45); S('2359.mp3',EV['cta'],.45)
mus=np.tile(load('../../assets/music/mixkit-9.mp3'),3)[:N]; fl=int(1.4*SR); mus[-fl:]*=np.linspace(1,0,fl)
cs,ce=int(EV['card']*SR),int((EV['card']+1.7)*SR); mus[cs:ce]*=.25           # the music dips under the black card
for name,b in [('voice',voice),('sfx',sfx),('music',mus)]:
    subprocess.run(['ffmpeg','-v','error','-y','-f','f32le','-ar',str(SR),'-ac','1','-i','-',f'{name}.wav'],input=np.clip(b,-1,1).tobytes())
data={'end':END,'lines':lines,'ev':EV,'start':START}
json.dump(data,open('data.json','w')); open('data.js','w').write('window.DATA='+json.dumps(data)+';')
print('END',END); print({k:round(v,2) for k,v in EV.items()})
