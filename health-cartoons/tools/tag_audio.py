import torch, numpy as np, subprocess, collections, sys
from transformers import ASTFeatureExtractor, ASTForAudioClassification
def load(p,sr=16000):
  return np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',p,'-f','s16le','-ac','1','-ar',str(sr),'-'],capture_output=True).stdout,np.int16).astype(np.float32)/32768
name='MIT/ast-finetuned-audioset-10-10-0.4593'
fe=ASTFeatureExtractor.from_pretrained(name); m=ASTForAudioClassification.from_pretrained(name).eval()
a=load(sys.argv[1]); sr=16000
tot=collections.Counter(); W=1.0
for i in range(0,len(a)-int(W*sr),int(W*sr)):
  x=a[i:i+int(W*sr)]
  with torch.no_grad(): lo=m(**fe(x,sampling_rate=sr,return_tensors='pt')).logits[0].sigmoid()
  top=lo.topk(6); labs=[(m.config.id2label[int(k)],float(v)) for v,k in zip(top.values,top.indices)]
  for l,v in labs:
    if v>.15: tot[l]+=1
  print(f'{i/sr:5.1f}', ' | '.join(f'{l} {v:.2f}' for l,v in labs[:5]))
print('\nTOTAL windows:',len(a)//int(W*sr)); print(tot.most_common(25))
