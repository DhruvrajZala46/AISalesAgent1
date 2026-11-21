# 006: the AI closed-mouth edit of the yawning brain shifted the whole drawing, so the closed variant is the mouthless base
# with a small sleepy mouth line drawn on the exact spot of the yawn (run after composite_mouths.py).
import json
from PIL import Image, ImageDraw
P=json.load(open('art/mouth/patches.json'))['brain_yawn']; bx,by=P['box'][:2]; cx,cy=P['patch'][0]-bx,P['patch'][1]-by
im=Image.open('art/brain_yawn.png').convert('RGBA'); d=ImageDraw.Draw(im)
d.arc([cx-38,cy-30,cx+38,cy+18],start=20,end=160,fill=(74,42,36,255),width=10)
im.save('art/brain_yawn_c.png'); print('closed yawn mouth at',cx,cy)
