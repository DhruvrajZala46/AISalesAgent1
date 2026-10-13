# AI tells in the metadata (LEARNINGS, redcoat0): pin title "Description:", affiliate links, exact 5/6/8/10/15 s at 24 fps, AI-ish uploader names
import json,subprocess,glob,os,re
M=json.load(open('raw/meta.json')); out=[]
for f in sorted(glob.glob('raw/*.mp4')):
    k=os.path.basename(f)[:-4]; m=M.get(k,{})
    pr=json.loads(subprocess.run(['ffprobe','-v','error','-select_streams','v:0','-show_entries','stream=r_frame_rate:format=duration','-of','json',f],capture_output=True,text=True).stdout or '{}')
    try: d=float(pr['format']['duration']); fr=pr['streams'][0]['r_frame_rate']; a,b=fr.split('/'); fps=float(a)/float(b)
    except Exception: out.append((k,'UNREADABLE')); continue
    flags=[]
    if 'description:' in (m.get('title') or '').lower(): flags.append('title Description:')
    if re.search(r'amzn\.to|amazon\.|bit\.ly|shopltk|liketk|rstyle|go\.magik|temu|shein',(m.get('src') or ''),re.I): flags.append('affiliate '+m.get('src','')[:40])
    if abs(fps-24)<0.1 and any(abs(d-x)<0.25 for x in (5,6,8,10,15)): flags.append(f'AI length {d:.2f}s@24')
    if re.search(r'gemini|veo|sora|kling|runway|midjourney|\bai\b|_ai|ai_',(m.get('user','')+' '+m.get('creator','')),re.I): flags.append('ai name '+m.get('user',''))
    if re.fullmatch(r'\d+',m.get('user','') or 'x'): flags.append('digit-only user')
    if flags: out.append((k,'; '.join(flags)))
for k,f in out: print(k,'|',f)
print(len(glob.glob('raw/*.mp4')),'clips checked')
