# Pinterest profile facts for each pinner (website, verified domain, about) - to judge whether a pin is the creator's own upload
#   python3 -I pin_users.py out.json <username>...
import json, sys, time, urllib.request, urllib.parse
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
def get(u, h={}): return urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": UA, **h}), timeout=40).read()
out = {}
for name in sys.argv[2:]:
    d = {"options": {"username": name, "field_set_key": "profile"}, "context": {}}
    u = "https://www.pinterest.com/resource/UserResource/get/?" + urllib.parse.urlencode({"source_url": f"/{name}/", "data": json.dumps(d)})
    try:
        r = json.loads(get(u, {"X-Pinterest-PWS-Handler": "www/[username].js", "X-Requested-With": "XMLHttpRequest", "Accept": "application/json"}))["resource_response"]["data"]
        keep = {k: r.get(k) for k in ('username', 'full_name', 'about', 'website_url', 'domain_url', 'domain_verified', 'is_verified_merchant', 'follower_count', 'pin_count', 'profile_cover', 'verified_identity', 'country', 'locale', 'instagram_data', 'youtube_data', 'tiktok_data', 'etsy_data', 'native_pin_count', 'impressum_url', 'is_partner') if k in r}
        out[name] = keep
    except Exception as e: out[name] = {'err': str(e)}
    time.sleep(1.5)
json.dump(out, open(sys.argv[1], 'w'), indent=1, ensure_ascii=False)
for k, v in out.items(): print(k, json.dumps(v, ensure_ascii=False)[:500]); print()
