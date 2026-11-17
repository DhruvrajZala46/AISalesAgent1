# phbig.py tag:k ...  -> ph/big_<tag>_<k>.jpg (the original image) and prints its pin, domain, creator, size
import sys, json, urllib.request
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
for it in sys.argv[1:]:
    tag, k = it.split(':'); p = json.load(open(f'ph/{tag}.json'))[int(k)]
    try:
        b = urllib.request.urlopen(urllib.request.Request(p['orig'], headers={"User-Agent": UA}), timeout=40).read()
        open(f'ph/big_{tag}_{k}.jpg', 'wb').write(b)
    except Exception as e: print(it, 'ERR', e); continue
    print(it, p['w'], p['h'], '|', p['domain'], '|', p['creator'], '|', p['user'], '|', p['link'][:70], '|', p['text'][:90].replace('\n', ' '))
