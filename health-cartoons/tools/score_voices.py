import torch, numpy as np, subprocess, glob, sys, json
from transformers import AutoFeatureExtractor, WavLMForXVector
torch.set_num_threads(4)
def load(p,filt=None,t=20):
  cmd=['ffmpeg','-v','error','-t',str(t),'-i',p]+(['-af',filt] if filt else [])+['-f','s16le','-ac','1','-ar','16000','-']
  return np.frombuffer(subprocess.run(cmd,capture_output=True).stdout,np.int16).astype(np.float32)/32768
fe=AutoFeatureExtractor.from_pretrained('microsoft/wavlm-base-plus-sv'); m=WavLMForXVector.from_pretrained('microsoft/wavlm-base-plus-sv').eval()
def emb(x):
  with torch.no_grad(): e=m(**fe(x,sampling_rate=16000,return_tensors='pt')).embeddings[0]
  return torch.nn.functional.normalize(e,dim=-1)
E=torch.load(sys.argv[1])
C={'doctorM':['doc_v1','doc_v4'],'doctorF':['docF_v2','doc_v5'],'patientM':['pat_v1','pat_v3','pat_v4'],
   'cartoonA':['c_v1_scalpel','c_v2_her','c_v4_burger','c_v5_a','c_v3_b'],'cartoonB':['c_v1_appendix','c_v4_b','c_v3_a'],'patientF':['patF_v2']}
names=dict(l.rstrip('\n').split('\t',1) for l in open('names.tsv'))
shifts={'0':None,'+4':'asetrate=48000*1.26,aresample=48000,atempo=0.794','+7':'asetrate=48000*1.498,aresample=48000,atempo=0.6675'}
res={k:[] for k in C}
for p in sorted(glob.glob(sys.argv[2]+'/*.mp3')):
  vid=p.split('/')[-1][:-4]
  for sk,f in shifts.items():
    a=load(p,f)
    if len(a)<16000: continue
    e=emb(a)
    for k,ids in C.items():
      if sk!='0' and not k.startswith('cartoon'): continue
      res[k].append((float(np.mean([float(e@E[i]) for i in ids])),names.get(vid,vid),vid,sk))
out={}
for k,v in res.items():
  v.sort(reverse=True); out[k]=v[:6]
  print('==',k); [print(f'  {s:.3f} {sh:>3} {n[:45]:45s} {vid}') for s,n,vid,sh in v[:6]]
json.dump(out,open(sys.argv[2]+'_scores.json','w'))
