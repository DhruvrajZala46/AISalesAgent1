import sys,re,json,subprocess
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
for h in sys.argv[1:]:
    t=subprocess.run(["curl","-sS","-m","30","-A",UA,"-H","Accept-Language: en-US",f"https://www.tiktok.com/@{h}"],capture_output=True).stdout.decode('utf-8','ignore')
    m=re.search(r'<script id="__UNIVERSAL_DATA_FOR_REHYDRATION__" type="application/json">(.*?)</script>',t,re.S)
    if not m: print(h,'no data',len(t)); continue
    d=json.loads(m.group(1)).get('__DEFAULT_SCOPE__',{}).get('webapp.user-detail',{})
    ui=d.get('userInfo',{}); u=ui.get('user',{}); s=ui.get('stats',{})
    print(h,'status',d.get('statusCode'),'|',u.get('uniqueId'),'|',u.get('nickname'),'|',(u.get('signature') or '').replace('\n',' / ')[:150],'| followers',s.get('followerCount'),'videos',s.get('videoCount'))
