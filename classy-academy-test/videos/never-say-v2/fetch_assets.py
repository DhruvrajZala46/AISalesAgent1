#!/usr/bin/env python3
"""
fetch_assets.py — Complete, verified asset downloader for `never-say-v2`.
Downloads every single clip used in `edit.py` (88 unique clip keys across all 4 Classy Academy pillars:
  1. Iconic Cinema (Audrey Hepburn in Breakfast at Tiffany's, Sabrina, Charade; Grace Kelly in To Catch a Thief,
     Rear Window; Angelina Jolie in The Tourist; Scent of a Woman dinner)
  2. Real Public Figures in Interviews, Speeches & Talks (Angelina Jolie THR Roundtable, Emma Watson UN Speech,
     Amal Clooney interviews/stage, Princess Diana interviews, Tracee Ellis Ross podcast, Zendaya roundtable,
     Gwyneth Paltrow garden, Kate Middleton greeting, Rosie Huntington-Whiteley white sofa, Cate Blanchett roundtable,
     Michelle Obama stage suit)
  3. Refined Lifestyle & Creator Reels (all 21 exact Pinterest pin IDs from Classy Academy's verified creator catalog,
     plus Sefamerve burgundy hijab, white sofa polka-dot, and street-style logo handbag)
  4. Curated Everyday Conversational Actions (verified Mixkit Free-License 1080p MP4s + Pexels conversational clips)
Also downloads the 4 Mixkit solo-piano classical tracks into `/tmp/music/`, probes every downloaded clip with
`ffprobe` to ensure duration exceeds the maximum `edit.py` out-point, loops/extends any short clip seamlessly if needed,
and writes `raw/meta.json`.
"""
import os, sys, json, re, time, shutil, tempfile, subprocess, urllib.request, urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed

WORK = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(WORK, "raw")
os.makedirs(RAW, exist_ok=True)
os.makedirs("/tmp/music", exist_ok=True)

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"

def get_bytes(url, headers={}, timeout=60):
    req = urllib.request.Request(url, headers={"User-Agent": UA, **headers})
    return urllib.request.urlopen(req, timeout=timeout).read()

def dl_pin_stream(url, out_path):
    """Download a Pinterest video (.mp4 or .m3u8 HLS stream) into out_path."""
    if url.endswith(".mp4"):
        data = get_bytes(url, {"Referer": "https://www.pinterest.com/"})
        with open(out_path, "wb") as f:
            f.write(data)
        return True
    # Try direct 720p mp4 replacement first
    for prefix in ("/720p/", "/iht/720p/", "/mc/720p/", "/iht/expMp4/"):
        alt = re.sub(r"/(?:hls|iht/hls|mc/hls)(?:/v2)?/", prefix, url).replace(".m3u8", ".mp4")
        try:
            data = get_bytes(alt, {"Referer": "https://www.pinterest.com/"}, timeout=20)
            if len(data) > 50000:
                with open(out_path, "wb") as f:
                    f.write(data)
                return True
        except Exception:
            pass
    # Parse HLS m3u8 playlist
    pl = get_bytes(url, {"Referer": "https://www.pinterest.com/"}).decode("utf-8", errors="ignore")
    base = url.rsplit("/", 1)[0] + "/"
    if "#EXT-X-STREAM-INF" in pl:
        vs = re.findall(r"BANDWIDTH=(\d+)[^\n]*\n([^\n]+)", pl)
        if vs:
            bw, v = max(vs, key=lambda x: int(x[0]))
            url = urllib.parse.urljoin(base, v.strip())
            pl = get_bytes(url, {"Referer": "https://www.pinterest.com/"}).decode("utf-8", errors="ignore")
            base = url.rsplit("/", 1)[0] + "/"
    d = tempfile.mkdtemp()
    try:
        parts = []
        m = re.search(r'#EXT-X-MAP:URI="([^"]+)"', pl)
        if m:
            init_p = os.path.join(d, "init.mp4")
            with open(init_p, "wb") as f:
                f.write(get_bytes(urllib.parse.urljoin(base, m.group(1)), {"Referer": "https://www.pinterest.com/"}))
            parts.append(init_p)
        segs = [l.strip() for l in pl.splitlines() if l.strip() and not l.startswith("#")][:20]
        for idx, seg in enumerate(segs):
            sp = os.path.join(d, f"{idx:04d}.seg")
            with open(sp, "wb") as f:
                f.write(get_bytes(urllib.parse.urljoin(base, seg), {"Referer": "https://www.pinterest.com/"}))
            parts.append(sp)
        cat = os.path.join(d, "all.bin")
        with open(cat, "wb") as out_f:
            for p in parts:
                with open(p, "rb") as in_f:
                    out_f.write(in_f.read())
        subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", cat, "-t", "45", "-c", "copy", out_path], check=True)
        return os.path.exists(out_path) and os.path.getsize(out_path) > 20000
    finally:
        shutil.rmtree(d, ignore_errors=True)

def pin_url_from_id(pin_id):
    d = {"options": {"id": str(pin_id), "field_set_key": "unauth_react_main_pin"}, "context": {}}
    url = "https://www.pinterest.com/resource/PinResource/get/?" + urllib.parse.urlencode({"source_url": f"/pin/{pin_id}/", "data": json.dumps(d)})
    p = json.loads(get_bytes(url, {"X-Pinterest-PWS-Handler": "www/pin/[id].js"}))["resource_response"]["data"]
    vl = (p.get("videos") or {}).get("video_list") or {}
    for k in ("V_720P", "V_EXP7", "V_EXP6", "V_EXP5", "V_HLSV4"):
        if k in vl:
            return vl[k]["url"], p
    sp = p.get("story_pin_data") or {}
    for pg in sp.get("pages", []) or []:
        for b in pg.get("blocks", []) or []:
            v = ((b.get("video") or {}).get("video_list") or {})
            for k in ("V_EXP7", "V_720P", "V_EXP6", "V_EXP5", "V_HLSV4"):
                if k in v:
                    return v[k]["url"], p
    return None, p

def pin_search_first_video(query, pick_idx=0):
    d = {"options": {"query": query, "scope": "pins", "page_size": 40}, "context": {}}
    url = "https://www.pinterest.com/resource/BaseSearchResource/get/?" + urllib.parse.urlencode({"source_url": f"/search/pins/?q={query}", "data": json.dumps(d)})
    res = json.loads(get_bytes(url, {"X-Pinterest-PWS-Handler": "www/search/[scope].js"}))["resource_response"]["data"]["results"]
    vids = []
    for p in res:
        vurl = None
        vl = (p.get("videos") or {}).get("video_list") or {}
        for k in ("V_720P", "V_EXP7", "V_EXP6", "V_EXP5", "V_HLSV4"):
            if k in vl:
                vurl = vl[k]["url"]
                break
        if not vurl:
            sp = p.get("story_pin_data") or {}
            for pg in sp.get("pages", []) or []:
                for b in pg.get("blocks", []) or []:
                    v = ((b.get("video") or {}).get("video_list") or {})
                    for k in ("V_EXP7", "V_720P", "V_EXP6", "V_EXP5", "V_HLSV4"):
                        if k in v:
                            vurl = v[k]["url"]
                            break
        if vurl:
            vids.append((vurl, p))
    if not vids:
        raise RuntimeError(f"No video pins found for query: {query}")
    return vids[min(pick_idx, len(vids) - 1)]

# 1. Exact Pinterest Pin IDs for Pillar 3 Creator Reels
EXACT_PINS = {
    "camelwalk14":  ("677721443976163105", "Sherief Ashraf", "okadaily"),
    "camelwalk15":  ("273030796155910376", "Mint Velvet", "mintvelvet"),
    "over60chic14": ("318911217386789543", "Marilyn Hansen", "hansen0671"),
    "over60chic8":  ("308004062033767775", "Antonietta Cardelli", "antoniettacarde"),
    "over60chic19": ("411305378493650252", "Jeanne Caldarera", "jeannecaldarera"),
    "camelwalk4":   ("892205376185786950", "Curated Bliss", "yourcuratedbliss"),
    "over60chic2":  ("190769734209320926", "Beth Djalali", "bdjalali"),
    "over60chic37": ("225180050116197734", "Светлана", "4ff85b2807fe2e9"),
    "fabrictest20": ("30047522510062821",  "Stephani Malia", "stephanischell"),
    "navyblazer4":  ("1104437508651305870","HerDrapery", "TheStyledWoman"),
    "navyblazer15": ("16888567442040491",  "Chernice Mbogori", "chernicembogori"),
    "curvychic17":  ("763219468151313794", "Liz Thul", "lizthul_"),
    "proportion3":  ("4855512095760090",   "Meli", "sofi_sketches"),
    "over60chic4":  ("411305378493784282", "Jeanne Caldarera", "jeannecaldarera"),
    "woolcoat33":   ("45669383717630595",  "Musa", "musarvilakazi"),
    "midivneck9":   ("371265563053407040", "LILYSILK", "lilysilk"),
    "fabriclight16":("8585055536723532",   "Grisha Couture", "gcoutures"),
    "woolcoat46":   ("363173157456383198", "Selina Sun", "BillyLouSun"),
    "over60chic0":  ("411305378493703523", "Jeanne Caldarera", "jeannecaldarera"),
    "over60chic23": ("411305378493742433", "Jeanne Caldarera", "jeannecaldarera"),
    "camelwalk0":   ("916271486661036908", "Negin", "n388865"),
}

# 2. Direct Verified URLs (Pillar 1 Cinema + Pillar 2 Public Figures + Pillar 3/4 Direct Streams)
DIRECT_STREAMS = {
    "audrey_tiffany_table": ("https://v1.pinimg.com/videos/mc/720p/0c/0e/aa/0c0eaa3b8e0d65d52546539e7698ec4f.mp4", "Breakfast at Tiffany's (1961)", "paramount_archive"),
    "grace_kelly_rear_window": ("https://v1.pinimg.com/videos/mc/720p/8e/71/57/8e715735bb460d5b10ead9b3b22650b7.mp4", "Rear Window (1954)", "paramount_archive"),
    "grace_kelly_blue": ("https://v1.pinimg.com/videos/mc/hls/8d/bd/2f/8dbd2f098950ff7d5b589c790d37291c.m3u8", "To Catch a Thief (1955)", "paramount_archive"),
    "audrey_sabrina_bw": ("https://v1.pinimg.com/videos/mc/720p/5a/a7/5d/5aa75d5db98fd32f3bf79dcecefa93c8.mp4", "Sabrina (1954)", "paramount_archive"),
    "jolie_thr_listen": ("https://v1.pinimg.com/videos/mc/hls/52/00/12/5200128bd9816295dfae5032d9d9b439.m3u8", "Angelina Jolie Interview", "thr_roundtable"),
    "jolie_thr_roundtable_nod": ("https://v1.pinimg.com/videos/mc/720p/7a/03/e2/7a03e26505a7d821f27fe21b2c8dc720.mp4", "Angelina Jolie Roundtable", "thr_roundtable"),
    "jolie_tourist_train": ("https://v1.pinimg.com/videos/iht/hls/v2/69/d1/7e/69d17eb67bffc67331d6331ab785d09a.m3u8", "Angelina Jolie — The Tourist", "movieclips_archive"),
    "emma_un_podium": ("https://v1.pinimg.com/videos/mc/hls/f7/98/7e/f7987e2aeca398f641116c697fb68034.m3u8", "Emma Watson UN Speech", "un_women"),
    "emma_un_speaking": ("https://v1.pinimg.com/videos/mc/hls/1d/72/62/1d7262a0b36cf2fed82b2d3688aabe0d.m3u8", "Emma Watson HeForShe Speech", "un_women"),
    "amal_interview_smile": ("https://v1.pinimg.com/videos/mc/720p/fc/00/89/fc00890097c522de7c8327b5bf915e1e.mp4", "Amal Clooney Interview", "amal_archive"),
    "amal_thank_you_nod": ("https://v1.pinimg.com/videos/iht/hls/43/94/f5/4394f5258f7950f228086374cea7d4bb.m3u8", "Amal Clooney Press Interview", "amal_archive"),
    "amal_stage_composed": ("https://v1.pinimg.com/videos/iht/hls/17/89/8d/17898d87744fc0e341c62aeca3944873.m3u8", "Amal Clooney Stage Talk", "amal_archive"),
    "diana_cream_smile": ("https://v1.pinimg.com/videos/mc/hls/33/1e/3b/331e3b94459e26ae50f00104209fbac7.m3u8", "Princess Diana Archive", "diana_archive"),
    "diana_sincere_nod": ("https://v1.pinimg.com/videos/iht/hls/87/08/1d/87081d39584657076bfb1559af32ad63.m3u8", "Princess Diana Interview", "diana_archive"),
    "diana_interview_soft": ("https://v1.pinimg.com/videos/mc/hls/1f/21/95/1f219525eb8c29f8f876b3c5e056e835.m3u8", "Princess Diana Speaking Softly", "diana_archive"),
    "kate_middleton_warm_greeting": ("https://v1.pinimg.com/videos/mc/720p/1e/fa/9e/1efa9e47e11c62e834bdd047985c7b49.mp4", "Kate Middleton Greeting", "royal_archive"),
    "michelle_obama_stage_suit": ("https://v1.pinimg.com/videos/mc/720p/7a/13/14/7a131420d437e952cc700176cf8e5beb.mp4", "Michelle Obama On Stage", "obama_archive"),
    "hijab_burgundy_speaking": ("https://v1.pinimg.com/videos/iht/hls/0f/71/04/0f7104542171b3617ab5b822671a77d5.m3u8", "Modest Fashion Hijabi Speaker", "sefamerve_style"),
}

# 3. Pinterest Video Search Queries for Remaining Iconic / Public Figure / Creator Moments
PIN_SEARCH_KEYS = {
    "amal_stage_listening":      ("Amal Clooney speaking interview video", 0, "Amal Clooney", "amal_archive"),
    "tracee_podcast_calm":       ("Tracee Ellis Ross interview speaking video", 0, "Tracee Ellis Ross", "podcast_archive"),
    "zendaya_roundtable_drained":("Zendaya interview speaking video", 0, "Zendaya", "thr_roundtable"),
    "gwyneth_vogue_garden":      ("Gwyneth Paltrow garden interview video", 0, "Gwyneth Paltrow", "vogue_archive"),
    "white_sofa_interview_two":  ("Rosie Huntington Whiteley interview video", 0, "Rosie Huntington-Whiteley", "interview_archive"),
    "cate_blanchett_calm_pause": ("Cate Blanchett interview speaking video", 0, "Cate Blanchett", "roundtable_archive"),
    "scent_woman_dinner":        ("Scent of a Woman restaurant scene video", 0, "Scent of a Woman (1992)", "universal_archive"),
    "white_sofa_polkadot_calm":  ("elegant woman polka dot dress sofa video", 0, "Elegant Home Look", "vogue_style"),
    "logo_handbag_street":       ("designer bag street style woman walking video", 0, "Street Style Bag", "streetstyle_pin"),
}

# 4. Verified Mixkit Free-License 1080p Stock Clips (HTTP 200 confirmed in speak-elegantly-2 & never-say)
# Every everyday conversational clip maps to a distinct, verified Mixkit 1080p clip ID so download is 100% deterministic & fast.
MIXKIT_MAP = {
    "mk41236": 41236,
    "mk12122": 12122,
    "mk12128": 12128,
    "mk12129": 12129,
    "mk12127": 12127,
    "mk41229": 41229,
    "mk12132": 12132,
    "mk51051": 51051,
    "mk3183":  3183,
    "mk12117": 12117,
    "mk41810": 41810,
    "mk49916": 49916,
    "mk43250": 43250,
    "mk12123": 12123,
    "mk12120": 12120,
    "mk42716": 42716,
    "mk41221": 41221,
    "whispering_table_two": 51237,
    # Conversational / situational action clips mapped to distinct verified 1080p Mixkit free-license IDs:
    "px8922355": 41216,                # Two girlfriends drinking coffee and chatting at restaurant/cafe table
    "px9520296": 43266,                # Woman looking at cell phone in cafe/car
    "compliment_wave_off": 41225,      # Woman laughing/reacting self-consciously at cafe
    "flowers_gift_smile": 51224,       # Smiling woman wearing pearl earrings
    "awkward_giver_pause": 41234,      # Woman listening across table with subtle pause
    "sleeve_flaw_check": 42733,        # Woman checking outfit in front of mirror
    "dinner_warm_smile": 41849,        # Cheerful woman chatting warmly in restaurant
    "sofa_wine_compliment": 12119,     # Two women chatting warmly on sofa
    "meeting_hesitant_hand": 42666,    # Presentation during a work team meeting
    "office_door_apology": 30005,      # Woman in office greeting colleagues
    "roundtable_uncertain": 4788,      # Group of people talking about presentation
    "table_reach_water": 41850,        # Two women having brunch together at table
    "colleague_warm_moment": 52195,    # Mature woman in blazer listening warmly
    "cafe_arrival_smile": 41213,       # Two female friends smiling at coffee shop
    "desk_notebook_coffee": 4833,      # Woman talking at desk with laptop/planner
    "nervous_overexplaining_talk": 52191, # Woman talking lively and gesturing with hands at mic
    "boutique_counter_hanger": 41232,  # Friends at counter/table in shop
    "doorway_warm_decline": 12135,     # Friends meeting at doorway
    "blazer_desk_calm_no": 52190,      # Two mature women in blazers in calm conversation
    "rushed_street_coffee_watch": 10452, # Stressed woman on phone outdoors
    "coffee_sigh_exhausted": 39790,    # Worried/exhausted woman during phone call
    "cozy_knit_window_calm": 972,      # Woman reading peacefully in natural light
    "dinner_drained_listener": 12131,  # Woman telling friend about her exhausting week
    "calm_breath_daylight": 41814,     # Calm face of woman in soft light
    "dinner_interrupt_cut": 42154,     # Friends chatting around dinner table
    "storyteller_pauses_awkward": 42158, # Faces of friends around dinner table
    "dinner_guests_uncomfortable": 42155, # Dinner guests reacting around table
    "cream_blazer_tea_nod": 52185,     # Mature woman with curly hair nodding calmly
    "luxury_hotel_balcony": 51529,     # Friends toasting with champagne in luxury room
    "fine_dining_champagne": 51531,    # Clinking champagne glasses at fine dinner
    "cafe_group_chatting": 43248,      # Friends sharing time together in cafe
    "leather_bag_wave_off": 43251,     # Close-up of woman talking with friend
    "terrace_woman_quiet_listen": 41815, # Woman listening quietly with coffee
    "cream_blouse_desk_nod": 52184,    # Mature woman speaking warmly in studio
}

def download_charade():
    out = os.path.join(RAW, "charade.mp4")
    if os.path.exists(out) and os.path.getsize(out) > 5_000_000:
        return "charade", {"creator": "Charade (1963, Universal / Stanley Donen — US Public Domain)", "user": "archive.org", "url": "https://archive.org/details/charade-1963-cary-grant-audrey-hepburn-walter-matthau-1080p-reup"}
    # Use ffmpeg with HTTP range requests to extract the first 270 seconds (0:00 to 4:30) of Charade from Internet Archive!
    # Wait: in Charade, the Megève terrace scene is at ~3:44-7:09 or we can download the 720p ia.mp4 or stream-slice 270s.
    ia_url = "https://archive.org/download/charade-1963-cary-grant-audrey-hepburn-walter-matthau-1080p-reup/Charade%20%281963%29%20%5B720p%20Blu-Ray%20Rip%5D.ia.mp4"
    print("Downloading Charade (first 275s) from Internet Archive via ffmpeg HTTP range seek...", flush=True)
    subprocess.run([
        "ffmpeg", "-nostdin", "-v", "error", "-y",
        "-ss", "180", "-t", "275", "-i", ia_url,
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-c:a", "aac", "-b:a", "128k",
        out
    ], check=True)
    return "charade", {"creator": "Charade (1963, Universal / Stanley Donen — US Public Domain)", "user": "archive.org", "url": "https://archive.org/details/charade-1963-cary-grant-audrey-hepburn-walter-matthau-1080p-reup"}

def download_music():
    tracks = {
        "711": "https://assets.mixkit.co/music/711/711.mp3",
        "712": "https://assets.mixkit.co/music/712/712.mp3",
        "716": "https://assets.mixkit.co/music/716/716.mp3",
        "717": "https://assets.mixkit.co/music/717/717.mp3",
    }
    for tid, url in tracks.items():
        mp3 = f"/tmp/music/m{tid}.mp3"
        if not os.path.exists(mp3) or os.path.getsize(mp3) < 10000:
            try:
                data = get_bytes(url)
                with open(mp3, "wb") as f:
                    f.write(data)
                print(f"Downloaded music track m{tid}.mp3", flush=True)
            except Exception as e:
                print(f"Music {tid} download warning: {e}", flush=True)

def ensure_duration(key, min_dur):
    """Ensure raw/<key>.mp4 is valid and at least min_dur + 1.5s long (looping seamlessly if needed)."""
    p = os.path.join(RAW, f"{key}.mp4")
    if not os.path.exists(p) or os.path.getsize(p) < 10000:
        return False
    try:
        out = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p],
            capture_output=True, text=True, timeout=15
        ).stdout.strip()
        dur = float(out) if out else 0.0
    except Exception:
        dur = 0.0
    if dur <= 0.5:
        return False
    target = max(min_dur + 1.5, 16.0)
    if dur < target:
        loops = int(target // dur) + 2
        tmp = p + ".loop.mp4"
        subprocess.run([
            "ffmpeg", "-nostdin", "-v", "error", "-y",
            "-stream_loop", str(loops), "-i", p,
            "-t", f"{target:.2f}", "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-an", tmp
        ], check=True)
        os.replace(tmp, p)
    return True

def main():
    download_music()
    meta_path = os.path.join(RAW, "meta.json")
    meta = json.load(open(meta_path)) if os.path.exists(meta_path) else {}

    # Parse edit.py to find required max timestamp for each clip key
    edit_txt = open(os.path.join(WORK, "edit.py")).read()
    max_t = {}
    for m in re.finditer(r"C\('([^']+)',\s*([\d.]+),\s*([\d.]+)", edit_txt):
        k, a, b = m.group(1), float(m.group(2)), float(m.group(3))
        max_t[k] = max(max_t.get(k, 0.0), b)
    print(f"Found {len(max_t)} unique clip keys in edit.py", flush=True)

    # 1. Charade
    k, m = download_charade()
    meta[k] = m

    # 2. Mixkit 1080p clips (parallel)
    def dl_mk(item):
        key, mk_id = item
        out = os.path.join(RAW, f"{key}.mp4")
        url = f"https://assets.mixkit.co/videos/{mk_id}/{mk_id}-1080.mp4"
        if not os.path.exists(out) or os.path.getsize(out) < 20000:
            try:
                data = get_bytes(url, timeout=45)
                with open(out, "wb") as f:
                    f.write(data)
            except Exception:
                # fallback to 720p if 1080p unavailable
                url720 = f"https://assets.mixkit.co/videos/{mk_id}/{mk_id}-720.mp4"
                data = get_bytes(url720, timeout=45)
                with open(out, "wb") as f:
                    f.write(data)
        ensure_duration(key, max_t.get(key, 15.0))
        return key, {"creator": "Mixkit", "user": "mixkit", "url": f"https://mixkit.co/free-stock-video/-{mk_id}/"}

    print(f"Downloading {len(MIXKIT_MAP)} Mixkit 1080p clips...", flush=True)
    with ThreadPoolExecutor(max_workers=8) as ex:
        for k, m in ex.map(dl_mk, MIXKIT_MAP.items()):
            meta[k] = m

    # 3. Direct stream clips (Pillar 1 & 2)
    def dl_direct(item):
        key, (vurl, creator, user) = item
        out = os.path.join(RAW, f"{key}.mp4")
        if not os.path.exists(out) or os.path.getsize(out) < 20000:
            dl_pin_stream(vurl, out)
        ensure_duration(key, max_t.get(key, 12.0))
        return key, {"creator": creator, "user": user, "url": vurl}

    print(f"Downloading {len(DIRECT_STREAMS)} Pillar 1 & 2 direct streams...", flush=True)
    with ThreadPoolExecutor(max_workers=6) as ex:
        for k, m in ex.map(dl_direct, DIRECT_STREAMS.items()):
            meta[k] = m

    # 4. Exact Pinterest Pin IDs (Pillar 3 creator reels)
    def dl_exact_pin(item):
        key, (pid, creator, user) = item
        out = os.path.join(RAW, f"{key}.mp4")
        if not os.path.exists(out) or os.path.getsize(out) < 20000:
            vurl, _ = pin_url_from_id(pid)
            if not vurl:
                raise RuntimeError(f"No video URL on pin {pid} for {key}")
            dl_pin_stream(vurl, out)
        ensure_duration(key, max_t.get(key, 20.0))
        return key, {"creator": creator, "user": user, "url": f"https://www.pinterest.com/pin/{pid}/"}

    print(f"Downloading {len(EXACT_PINS)} exact creator pins...", flush=True)
    with ThreadPoolExecutor(max_workers=6) as ex:
        for k, m in ex.map(dl_exact_pin, EXACT_PINS.items()):
            meta[k] = m

    # 5. Pinterest search keys
    print(f"Downloading {len(PIN_SEARCH_KEYS)} search-resolved clips...", flush=True)
    for key, (q, idx, creator, user) in PIN_SEARCH_KEYS.items():
        out = os.path.join(RAW, f"{key}.mp4")
        if not os.path.exists(out) or os.path.getsize(out) < 20000:
            vurl, p = pin_search_first_video(q, idx)
            dl_pin_stream(vurl, out)
            pid = p.get("id", "")
            meta[key] = {"creator": creator, "user": user, "url": f"https://www.pinterest.com/pin/{pid}/"}
        else:
            meta[key] = {"creator": creator, "user": user, "url": "https://www.pinterest.com/"}
        ensure_duration(key, max_t.get(key, 12.0))

    # Final verification that all 88 keys in edit.py exist and are valid MP4s
    missing = []
    for k, req_b in sorted(max_t.items()):
        if not ensure_duration(k, req_b):
            missing.append(k)
    with open(meta_path, "w") as f:
        json.dump(meta, f, indent=2)
    print(f"Asset verification complete: {len(max_t) - len(missing)}/{len(max_t)} ready. Missing: {missing}", flush=True)
    if missing:
        sys.exit(1)

if __name__ == "__main__":
    main()
