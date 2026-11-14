# textfit.py spec.json [...] -> width of every on-screen line as a share of 1080 px; flags lines wider than 78%
import json,sys
from PIL import ImageFont
for p in sys.argv[1:]:
    for t in json.load(open(p))["texts"]:
        f=ImageFont.truetype("fonts/CormorantSC-Regular.ttf" if t.get("small") else "fonts/PlayfairDisplay.ttf", t.get("size",78))
        w=f.getlength(t["text"])/1080
        print(f"{p:10s} {w:5.0%} {'TOO WIDE' if w>0.78 else '':8s} {t['text']}")
