# fetch_assets_probe.py - Discovers and verifies downloadable 1080p/720p video assets for never-say-v2
import json, urllib.request, urllib.parse, re, os, subprocess

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"

def get(url, headers={}):
    req = urllib.request.Request(url, headers={"User-Agent": UA, **headers})
    return urllib.request.urlopen(req, timeout=30).read()

def head_ok(url):
    try:
        req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": UA})
        resp = urllib.request.urlopen(req, timeout=15)
        return resp.status == 200
    except Exception:
        return False

def pin_search_videos(query, limit=6):
    d = {"options": {"query": query, "scope": "pins", "page_size": 40}, "context": {}}
    url = "https://www.pinterest.com/resource/BaseSearchResource/get/?" + urllib.parse.urlencode({"source_url": f"/search/pins/?q={query}", "data": json.dumps(d)})
    try:
        res = json.loads(get(url, {"X-Pinterest-PWS-Handler": "www/search/[scope].js"}))["resource_response"]["data"]["results"]
    except Exception as e:
        return [{"error": str(e)}]
    out = []
    for p in res:
        vurl = None
        vl = (p.get('videos') or {}).get('video_list') or {}
        for k in ('V_720P', 'V_EXP7', 'V_EXP6', 'V_EXP5', 'V_HLSV4'):
            if k in vl:
                vurl = vl[k]['url']
                break
        if not vurl:
            sp = p.get('story_pin_data') or {}
            for pg in sp.get('pages', []) or []:
                for b in pg.get('blocks', []) or []:
                    v = ((b.get('video') or {}).get('video_list') or {})
                    for k in ('V_EXP7', 'V_720P', 'V_EXP6', 'V_EXP5', 'V_HLSV4'):
                        if k in v:
                            vurl = v[k]['url']
                            break
        if vurl:
            pn = p.get('pinner') or {}
            nc = p.get('native_creator') or {}
            pid = str(p.get('id') or '')
            out.append({
                "id": pid,
                "pin_url": f"https://www.pinterest.com/pin/{pid}/",
                "video_url": vurl,
                "creator": nc.get('full_name') or pn.get('full_name') or '',
                "user": nc.get('username') or pn.get('username') or '',
                "title": (p.get('grid_title') or p.get('title') or '')[:80]
            })
            if len(out) >= limit:
                break
    return out

def pin_by_id(pin_id):
    # Try fetching pin page or resource to extract video_list
    try:
        d = {"options": {"id": str(pin_id), "field_set_key": "unauth_react_main_pin"}, "context": {}}
        url = "https://www.pinterest.com/resource/PinResource/get/?" + urllib.parse.urlencode({"source_url": f"/pin/{pin_id}/", "data": json.dumps(d)})
        p = json.loads(get(url, {"X-Pinterest-PWS-Handler": "www/pin/[id].js"}))["resource_response"]["data"]
        vl = (p.get('videos') or {}).get('video_list') or {}
        for k in ('V_720P', 'V_EXP7', 'V_EXP6', 'V_EXP5', 'V_HLSV4'):
            if k in vl:
                return vl[k]['url']
        sp = p.get('story_pin_data') or {}
        for pg in sp.get('pages', []) or []:
            for b in pg.get('blocks', []) or []:
                v = ((b.get('video') or {}).get('video_list') or {})
                for k in ('V_EXP7', 'V_720P', 'V_EXP6', 'V_EXP5', 'V_HLSV4'):
                    if k in v:
                        return v[k]['url']
    except Exception as e:
        return f"ERR:{e}"
    return None

report = {}

# 1. Test Charade on Internet Archive
try:
    ia_meta = json.loads(get("https://archive.org/metadata/charade-1963-cary-grant-audrey-hepburn-walter-matthau-1080p-reup"))
    mp4s = [f["name"] for f in ia_meta.get("files", []) if f.get("name", "").endswith(".mp4")]
    report["charade_ia"] = mp4s
except Exception as e:
    report["charade_ia"] = str(e)

# 2. Test known Pinterest Pin IDs from CREDITS.txt
pin_ids = {
    "camelwalk14": "677721443976163105",
    "camelwalk15": "273030796155910376",
    "over60chic14": "318911217386789543",
    "over60chic8": "308004062033767775",
    "over60chic19": "411305378493650252",
    "camelwalk4": "892205376185786950",
    "over60chic2": "190769734209320926",
    "over60chic37": "225180050116197734",
    "fabrictest20": "30047522510062821",
    "navyblazer4": "1104437508651305870",
    "navyblazer15": "16888567442040491",
    "curvychic17": "763219468151313794",
    "proportion3": "4855512095760090",
    "over60chic4": "411305378493784282",
    "woolcoat33": "45669383717630595",
    "midivneck9": "371265563053407040",
    "fabriclight16": "8585055536723532",
    "woolcoat46": "363173157456383198",
    "over60chic0": "411305378493703523",
    "over60chic23": "411305378493742433",
    "camelwalk0": "916271486661036908"
}
report["pin_by_id"] = {}
for k, pid in list(pin_ids.items())[:8]:
    report["pin_by_id"][k] = pin_by_id(pid)

# 3. Test Pinterest video search for iconic cinema & public figure interviews
queries = {
    "audrey_tiffany": "Audrey Hepburn Breakfast at Tiffany's speaking video",
    "grace_kelly": "Grace Kelly To Catch a Thief Rear Window video",
    "audrey_sabrina": "Audrey Hepburn Sabrina 1954 video",
    "angelina_jolie_interview": "Angelina Jolie interview speaking softly video",
    "emma_watson_speech": "Emma Watson UN speech video",
    "amal_clooney_interview": "Amal Clooney interview speaking video",
    "princess_diana_interview": "Princess Diana speaking softly interview video",
    "kate_middleton": "Kate Middleton greeting smiling video",
    "michelle_obama": "Michelle Obama stage speaking suit video",
    "hijab_elegant": "elegant modest hijab woman speaking video"
}
report["pin_searches"] = {}
for k, q in queries.items():
    report["pin_searches"][k] = pin_search_videos(q, limit=3)

os.makedirs("classy-academy-test/videos/never-say-v2/render-output", exist_ok=True)
with open("classy-academy-test/videos/never-say-v2/render-output/asset_probe.json", "w") as f:
    json.dump(report, f, indent=2)
print("Asset probe complete")
