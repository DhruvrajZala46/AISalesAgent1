import torch, numpy as np, subprocess, glob, sys
from transformers import ASTFeatureExtractor, ASTForAudioClassification
def load(p,ss=0,t=10): return np.frombuffer(subprocess.run(['ffmpeg','-v','error','-ss',str(ss),'-t',str(t),'-i',p,'-f','s16le','-ac','1','-ar','16000','-'],capture_output=True).stdout,np.int16).astype(np.float32)/32768
name='MIT/ast-finetuned-audioset-10-10-0.4593'
fe=ASTFeatureExtractor.from_pretrained(name); m=ASTForAudioClassification.from_pretrained(name).eval()
def emb(x):
  with torch.no_grad(): o=m(**fe(x,sampling_rate=16000,return_tensors='pt'),output_hidden_states=True)
  return torch.nn.functional.normalize(o.hidden_states[-1][0].mean(0),dim=-1)
R='../ref2/sep/htdemucs/'
# use music-only regions: no_vocals stems, several windows
refs=[emb(load(R+f'v{i}/no_vocals.wav',ss,8)) for i in [1,3,4,5] for ss in (10,30)]
ref=torch.nn.functional.normalize(torch.stack(refs).mean(0),dim=-1)
print('ref self', np.mean([float(r@ref) for r in refs]))
names=dict(l.rstrip('\n').split('\t') for l in open('map.tsv'))
res=[]
for p in glob.glob('*.mp3'):
  e=[emb(load(p,ss,8)) for ss in (5,25)]
  e=torch.nn.functional.normalize(torch.stack(e).mean(0),dim=-1)
  res.append((float(e@ref),p,names.get(p[:-4],'?')))
for s,p,n in sorted(res,reverse=True)[:12]: print(f'{s:.3f} {p:10s} {n}')
