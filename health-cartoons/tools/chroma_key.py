# chroma-key a flat #00FF00 sprite -> transparent PNG trimmed to content, with green despill and a soft 1px edge
import sys,numpy as np
from PIL import Image, ImageFilter
src,out=sys.argv[1],sys.argv[2]
im=np.asarray(Image.open(src).convert('RGB')).astype(np.float32)
r,g,b=im[...,0],im[...,1],im[...,2]
greenness=g-np.maximum(r,b)            # how much greener than the other channels
a=np.clip(1-(greenness-40)/80,0,1)      # >120 -> fully transparent, <40 -> opaque
# despill: pull green down to max(r,b) on semi-transparent / edge pixels
spill=(g>np.maximum(r,b))&(a<1)|(greenness>15)
g2=np.where(spill,np.minimum(g,np.maximum(r,b)),g)
rgba=np.dstack([r,g2,b,a*255]).astype(np.uint8)
img=Image.fromarray(rgba,'RGBA')
al=img.split()[3].filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(.6)); img.putalpha(al)
bb=img.getbbox(); img=img.crop(bb); img.save(out); print(out,img.size,'bbox',bb)
