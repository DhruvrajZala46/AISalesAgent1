import sys,os,subprocess,urllib.request,urllib.parse,re,tempfile,shutil
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/130.0 Safari/537.36"
def get(u): return urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":UA,"Referer":"https://www.pinterest.com/"}),timeout=60).read()
def dl(url,out):
    if url.endswith('.mp4'): open(out,'wb').write(get(url)); return
    alt=url.replace('/hls/','/720p/').replace('.m3u8','.mp4')
    try: open(out,'wb').write(get(alt)); return
    except Exception: pass
    pl=get(url).decode(); base=url.rsplit('/',1)[0]+'/'
    if '#EXT-X-STREAM-INF' in pl:   # master: pick highest bandwidth variant
        vs=re.findall(r'BANDWIDTH=(\d+)[^\n]*\n([^\n]+)',pl); bw,v=max(vs,key=lambda x:int(x[0]))
        url=urllib.parse.urljoin(base,v.strip()); pl=get(url).decode(); base=url.rsplit('/',1)[0]+'/'
    d=tempfile.mkdtemp(); parts=[]
    m=re.search(r'#EXT-X-MAP:URI="([^"]+)"',pl)
    if m: init=os.path.join(d,'init.mp4'); open(init,'wb').write(get(urllib.parse.urljoin(base,m.group(1)))); parts.append(init)
    segs=[l for l in pl.splitlines() if l and not l.startswith('#')][:12]
    for k,seg in enumerate(segs):
        p=os.path.join(d,f'{k:04d}.seg'); open(p,'wb').write(get(urllib.parse.urljoin(base,seg))); parts.append(p)
    cat=os.path.join(d,'all.bin')
    with open(cat,'wb') as f:
        for p in parts: f.write(open(p,'rb').read())
    try: subprocess.run(f"ffmpeg -nostdin -v error -y -i {cat} -t 40 -c copy {out}",shell=True,check=True)
    finally: shutil.rmtree(d,ignore_errors=True)
if __name__=='__main__': dl(sys.argv[1],sys.argv[2])
