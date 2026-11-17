python3 - <<'PY'
import json, subprocess, glob, os
D={}
for f in sorted(glob.glob('raw/*.mp4')):
    k=os.path.basename(f)[:-4]
    pr=json.loads(subprocess.run(['ffprobe','-v','error','-select_streams','v:0','-show_entries','stream=width,height:format=duration','-of','json',f],capture_output=True,text=True).stdout or '{}')
    try: D[k]=[float(pr['format']['duration']), pr['streams'][0]['width'], pr['streams'][0]['height']]
    except Exception: pass
json.dump(D,open('dur.json','w')); print('dur',len(D))
PY
