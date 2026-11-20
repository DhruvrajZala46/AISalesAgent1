# Mouth-only layers: the pixels where each mouth variant differs from its mouthless base, same crop box as the variant,
# so the scene can draw the stomach's mouth OVER the burger standing inside the stomach.
import json,numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage
P=json.load(open('art/mouth/patches.json'))
for n in ['stomach_base','stomach_panic','stomach_point','stomach_drowsy']:
    box=tuple(P[n]['box']); cx,cy,rx,ry=P[n]['patch']
    base=np.asarray(Image.open(f'art/src/{n}.png').convert('RGB').crop(box)).astype(int)
    for v in P[n]['variants']:
        var=Image.open(f'art/{n}_{v}.png').convert('RGBA'); a=np.asarray(var).astype(int)
        d=np.abs(a[...,:3]-base).max(2)>55
        yy,xx=np.mgrid[0:d.shape[0],0:d.shape[1]]; ell=((xx-(cx-box[0]))/rx)**2+((yy-(cy-box[1]))/ry)**2<1
        d=ndimage.binary_opening(d&ell,iterations=1); lab,k=ndimage.label(d)
        if k: sz=ndimage.sum(d,lab,range(1,k+1)); d=lab==np.argmax(sz)+1
        d=ndimage.binary_fill_holes(ndimage.binary_dilation(d,iterations=4))
        al=Image.fromarray((d*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.5))
        o=var.copy(); o.putalpha(Image.fromarray(np.minimum(np.asarray(al),a[...,3]).astype(np.uint8)))
        o.save(f'art/{n}_{v}_m.png'); ys,xs=np.nonzero(d); print(n,v,'mouth src y',ys.min(),ys.max(),'of',d.shape[0])
