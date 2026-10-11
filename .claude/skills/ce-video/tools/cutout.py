# Product photo on a light plain background -> transparent PNG (flood fill from the border, soft edge)
import sys,numpy as np
from PIL import Image,ImageFilter
from scipy import ndimage
src,out=sys.argv[1],sys.argv[2]
im=Image.open(src).convert('RGB'); a=np.asarray(im).astype(float)
bg=np.median(np.concatenate([a[0],a[-1],a[:,0],a[:,-1]]),axis=0)
dist=np.sqrt(((a-bg)**2).sum(-1))
cand=dist<28
lab,_=ndimage.label(cand)
edge=set(np.unique(np.concatenate([lab[0],lab[-1],lab[:,0],lab[:,-1]])))-{0}
bgmask=np.isin(lab,list(edge))
# enclosed background pockets (between arm and body): large, very close to the bg colour
sizes=ndimage.sum(np.ones_like(lab),lab,index=np.arange(1,lab.max()+1))
for k,sz in enumerate(sizes,1):
    if k not in edge and sz>a.shape[0]*a.shape[1]*0.0015 and dist[lab==k].mean()<14: bgmask|=(lab==k)
alpha=(~bgmask).astype(np.uint8)*255
alpha=ndimage.binary_opening(alpha>0,iterations=2)
A=Image.fromarray((alpha*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.2))
rgba=im.copy(); rgba.putalpha(A); bb=A.getbbox(); rgba=rgba.crop(bb)
rgba.thumbnail((900,900)); rgba.save(out); print(out,rgba.size)
