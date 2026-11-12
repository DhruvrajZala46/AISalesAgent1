# build_short.py spec.json -> silent Short in the Classy Elegance look (serif text, CE monogram, piano bed)
import json, subprocess, sys, os, numpy as np
S=json.load(open(sys.argv[1])); name=S["name"]; F="fonts/PlayfairDisplay.ttf"; FS="fonts/CormorantSC-Regular.ttf"
def run(c): subprocess.run(c,shell=True,check=True)
os.makedirs(f"seg/{name}",exist_ok=True); D=f"seg/{name}"
lst=open(f"{D}/list.txt","w")
for k,g in enumerate(S["segs"]):
    c,s,d,mode=g["clip"],g["start"],g["dur"],g.get("mode","fill"); pre=(g["crop"]+",") if g.get("crop") else ""
    if mode=="fill":
        fc=f"[0:v]{pre}scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=30"
    else:
        fc=(f"[0:v]{pre}split[a][b];[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=30:2,eq=brightness=-0.12[bg];"
            f"[b]scale=1080:-2[fg];[bg][fg]overlay=0:(H-h)/2-60,setsar=1,fps=30")
    run(f"ffmpeg -nostdin -v error -y -ss {s} -t {d} -i raw/{c}.mp4 -an -filter_complex \"{fc}\" -c:v libx264 -crf 16 -pix_fmt yuv420p {D}/s{k}.mp4")
    lst.write(f"file 's{k}.mp4'\n")
lst.close()
run(f"ffmpeg -nostdin -v error -y -f concat -safe 0 -i {D}/list.txt -c copy {D}/body.mp4")
TOTAL=round(sum(g["dur"] for g in S["segs"]),3)
dt=[]
for i,t in enumerate(S["texts"]):
    a,b=t["a"],min(t["b"],TOTAL); y=t["y"]; size=t.get("size",78); font=FS if t.get("small") else F
    open(f"{D}/t{i}.txt","w").write(t["text"])
    alpha=(f"'if(gt(t,{b}-0.2),({b}-t)/0.2,1)'" if a==0 else f"'if(lt(t,{a}+0.25),(t-{a})/0.25,if(gt(t,{b}-0.2),({b}-t)/0.2,1))'")
    dt.append(f"drawtext=fontfile={font}:textfile={D}/t{i}.txt:fontsize={size}:fontcolor=white:shadowcolor=black@0.75:shadowx=0:shadowy=4:"
              f"borderw=2:bordercolor=black@0.25:x=(w-text_w)/2:y={y}:enable='between(t,{a},{b})':alpha={alpha}")
m=S["music"]
fc=f"[1:v]scale=120:-1,format=rgba,colorchannelmixer=aa=0.85[lg];[0:v]{','.join(dt)}[v0];[v0][lg]overlay=(W-w)/2:95[v]"
af=f"[2:a]atrim=start={m['start']}:duration={TOTAL},asetpts=PTS-STARTPTS,afade=t=in:st=0:d=0.4,afade=t=out:st={TOTAL-1.6}:d=1.6,volume={m.get('gain',4)}dB[a]"
os.makedirs("out",exist_ok=True)
run(f"ffmpeg -nostdin -v error -y -i {D}/body.mp4 -i assets/logo_ce.png -i assets/{m['file']}.mp3 -filter_complex \"{fc};{af}\" -map \"[v]\" -map \"[a]\" "
    f"-c:v libx264 -crf 17 -preset slow -pix_fmt yuv420p -r 30 -c:a aac -b:a 192k -movflags +faststart -t {TOTAL} out/{name}.mp4")
for ts in S.get("check",[]):
    run(f"ffmpeg -nostdin -v error -y -ss {ts} -i out/{name}.mp4 -frames:v 1 -vf scale=360:-2 chk/{name}_{ts}.jpg")
from PIL import Image, ImageDraw
ims=[Image.open(f"chk/{name}_{ts}.jpg") for ts in S.get("check",[])]
if ims:
    sh=Image.new('RGB',(sum(i.width+4 for i in ims),ims[0].height+20),'white'); x=0
    for ts,i in zip(S["check"],ims): sh.paste(i,(x,20)); ImageDraw.Draw(sh).text((x+3,3),f"{ts}s",fill='black'); x+=i.width+4
    sh.save(f"chk/{name}_sheet.jpg",quality=85)
print("built", name, TOTAL)
