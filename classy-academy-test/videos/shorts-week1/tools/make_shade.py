# make_shade.py -> assets/shade.png: a soft gradient (no box) that build_short.py lays over bright footage
import numpy as np
from PIL import Image
H,W=1920,1080; y=np.arange(H,dtype=np.float32)
top=0.38*np.clip(1-y/300,0,1)**1.6                       # behind the CE monogram
band=0.40*np.exp(-0.5*((y-1240)/150)**2)                  # behind the two text lines (y 1170-1340)
a=np.clip(np.maximum(top,band),0,1)
img=np.zeros((H,W,4),np.uint8); img[...,3]=(a*255).astype(np.uint8)[:,None]
Image.fromarray(img,'RGBA').save('assets/shade.png')
