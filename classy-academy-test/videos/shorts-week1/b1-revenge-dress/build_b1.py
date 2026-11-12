import subprocess, os
W=os.getcwd(); F="fonts/PlayfairDisplay.ttf"; FS="fonts/CormorantSC-Regular.ttf"
def run(c): subprocess.run(c,shell=True,check=True)
# (clip, start, dur, mode, extra-crop)
SEGS=[("sad18",0.2,1.2,"fit","crop=iw:ih*0.86:0:ih*0.14"),
      ("sad21",15.0,1.0,"fit",""),
      ("sad18",6.0,1.0,"fit",""),
      ("sad3",0.5,1.0,"fill",""),
      ("sad14",3.0,1.0,"fit",""),
      ("dress2",0.0,5.0,"fill",""),
      ("dress14",0.0,0.8,"fill",""),
      ("dress2",10.0,4.0,"fill",""),
      ("dress6",2.5,4.0,"fit","")]
lst=open("seg/list.txt","w")
for k,(c,s,d,mode,crop) in enumerate(SEGS):
    pre=(crop+",") if crop else ""
    if mode=="fill":
        vf=f"{pre}scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=30"
        run(f"ffmpeg -nostdin -v error -y -ss {s} -t {d} -i raw/{c}.mp4 -an -vf \"{vf}\" -c:v libx264 -crf 16 -pix_fmt yuv420p seg/s{k}.mp4")
    else:
        fc=(f"[0:v]{pre}split[a][b];[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=30:2,eq=brightness=-0.12[bg];"
            f"[b]scale=1080:-2[fg];[bg][fg]overlay=0:(H-h)/2-60,setsar=1,fps=30")
        run(f"ffmpeg -nostdin -v error -y -ss {s} -t {d} -i raw/{c}.mp4 -an -filter_complex \"{fc}\" -c:v libx264 -crf 16 -pix_fmt yuv420p seg/s{k}.mp4")
    lst.write(f"file 's{k}.mp4'\n")
lst.close()
run("ffmpeg -nostdin -v error -y -f concat -safe 0 -i seg/list.txt -c copy seg/body.mp4")
TOTAL=sum(x[2] for x in SEGS)
# text: (line, start, end, y, size, font)
TXT=[("The night Charles admitted",0.0,2.2,1170,78,F),("his affair on TV,",0.0,2.2,1268,78,F),
     ("she had two choices.",2.2,4.2,1220,78,F),
     ("Hide.",4.2,6.9,1180,86,F),("Or walk in.",4.2,6.9,1285,86,F),
     ("29 June 1994",6.3,9.6,1400,48,FS),
     ("She didn't explain.",14.6,TOTAL,1170,78,F),("She walked in.",14.6,TOTAL,1268,78,F)]
dt=[]
for i,(t,a,b,y,size,font) in enumerate(TXT):
    open(f"seg/t{i}.txt","w").write(t)
    alpha=(f"'if(gt(t,{b}-0.2),({b}-t)/0.2,1)'" if a==0 else f"'if(lt(t,{a}+0.25),(t-{a})/0.25,if(gt(t,{b}-0.2),({b}-t)/0.2,1))'")
    dt.append(f"drawtext=fontfile={font}:textfile=seg/t{i}.txt:fontsize={size}:fontcolor=white:"
              f"shadowcolor=black@0.75:shadowx=0:shadowy=4:borderw=2:bordercolor=black@0.25:"
              f"x=(w-text_w)/2:y={y}:enable='between(t,{a},{b})':alpha={alpha}")
vf=",".join(dt)
fc=(f"[1:v]scale=120:-1,format=rgba,colorchannelmixer=aa=0.85[lg];[0:v]{vf}[v0];[v0][lg]overlay=(W-w)/2:95[v]")
af=f"[2:a]atrim=start=34.5:duration={TOTAL},asetpts=PTS-STARTPTS,afade=t=in:st=0:d=0.4,afade=t=out:st={TOTAL-1.6}:d=1.6,volume=4dB[a]"
run(f"ffmpeg -nostdin -v error -y -i seg/body.mp4 -i assets/logo_ce.png -i assets/m717.mp3 -filter_complex \"{fc};{af}\" "
    f"-map \"[v]\" -map \"[a]\" -c:v libx264 -crf 17 -preset slow -pix_fmt yuv420p -r 30 -c:a aac -b:a 192k -movflags +faststart -t {TOTAL} out/B1_diana_revenge_dress.mp4")
print("done", TOTAL)
