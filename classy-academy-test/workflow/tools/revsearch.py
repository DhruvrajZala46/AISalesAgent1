"""Reverse image search for provenance (ASSET-RESEARCH-GUIDE.md, section 3).

    python3 -I revsearch.py <out_dir> <frame.png> [<frame2.png> ...]

For each frame: Yandex "search by image" -> the pages that contain the same or a near-identical image
(title, page URL, domain, image URL) -> downloads the small previews -> scores each against the frame
(best normalised cross-correlation over scales, crops allowed) -> writes <out_dir>/<name>.json and a
review sheet <out_dir>/<name>_sheet.jpg (frame on the left, best candidates to the right).
Scores are a hint only: confirm every match by eye before writing "Confirmed"/"Likely" in SOURCES-LOG.
Adult sites are dropped from the sheet. Be polite: one search every ~8 s.
"""
import html, json, os, re, subprocess, sys, time, urllib.request
import cv2
import numpy as np
from PIL import Image, ImageDraw

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
BAD = re.compile(r"porn|xham|nude|xxx|sex|redlight|spank|fuck|fap|hentai|erot|onlyfans", re.I)


def curl(args):
    return subprocess.run(["curl", "-g", "-sS", "-m", "90", "-A", UA] + args, capture_output=True).stdout


def yandex(img):
    up = curl(["-F", f"upfile=@{img}", 'https://yandex.com/images/search?rpt=imageview&format=json&request='
               '{"blocks":[{"block":"b-page_type_search-by-image__link"}]}'])
    cb = json.loads(up)["blocks"][0]["params"]["cbirId"]
    t = html.unescape(curl([f"https://yandex.com/images/search?cbir_id={cb}&rpt=imageview&cbir_page=sites"]).decode("utf-8", "ignore"))
    sites = []
    i = t.find('"sites":[')
    if i >= 0:
        arr, _ = json.JSONDecoder().raw_decode(t[i + 8:])
        for s in arr:
            o = s.get("originalImage") or {}
            sites.append({"title": s.get("title"), "url": s.get("url"), "domain": s.get("domain"),
                          "image": o.get("url"), "w": o.get("width"), "h": o.get("height"),
                          "thumb": (s.get("thumb") or {}).get("url")})
    return {"cbir_id": cb, "captcha": "showcaptcha" in t, "sites": sites}


def score(q, c):
    qg = cv2.cvtColor(np.asarray(q), cv2.COLOR_RGB2GRAY)
    cg = cv2.cvtColor(np.asarray(c), cv2.COLOR_RGB2GRAY)
    best = -1.0
    for a, b in ((qg, cg), (cg, qg)):
        for s in np.linspace(0.25, 1.0, 13):
            tw = int(b.shape[1] * s); th = int(a.shape[0] * tw / a.shape[1])
            if tw < 24 or th < 24 or th > b.shape[0] or tw > b.shape[1]:
                continue
            best = max(best, float(cv2.matchTemplate(b, cv2.resize(a, (tw, th), interpolation=cv2.INTER_AREA),
                                                     cv2.TM_CCOEFF_NORMED).max()))
    return round(best, 3)


def fetch(url, dst):
    if url.startswith("//"):
        url = "https:" + url
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        open(dst, "wb").write(urllib.request.urlopen(req, timeout=25).read())
        return True
    except Exception:
        return False


def main():
    out, frames = sys.argv[1], sys.argv[2:]
    os.makedirs(out, exist_ok=True)
    for f in frames:
        name = os.path.splitext(os.path.basename(f))[0]
        q = Image.open(f).convert("RGB")
        res = yandex(f)
        for i, s in enumerate(res["sites"][:25]):
            p = f"{out}/{name}_c{i:02d}.jpg"
            u = s.get("thumb") or s.get("image")
            if u and fetch(u, p):
                try:
                    s["score"] = score(q, Image.open(p).convert("RGB"))
                except Exception:
                    s["score"] = None
        json.dump(res, open(f"{out}/{name}.json", "w"), indent=1, ensure_ascii=False)
        good = [(i, s) for i, s in enumerate(res["sites"][:25])
                if s.get("score") is not None and not BAD.search(f"{s.get('domain')}{s.get('url')}{s.get('title')}")]
        # Yandex lists exact/near-exact copies first: keep its first 3, then the best-scoring others
        first = good[:3]
        rest = sorted(good[3:], key=lambda x: -x[1]["score"])
        good = first + rest
        W, H = 260, 220
        sh = Image.new("RGB", (W * 7, H + 50), "white"); d = ImageDraw.Draw(sh)
        qq = q.copy(); qq.thumbnail((W, H)); sh.paste(qq, (0, 46)); d.text((2, 2), name, fill="red")
        for k, (i, s) in enumerate(good[:6]):
            c = Image.open(f"{out}/{name}_c{i:02d}.jpg").convert("RGB"); c.thumbnail((W - 6, H))
            x = (k + 1) * W; sh.paste(c, (x + 3, 46))
            d.text((x + 3, 2), f"#{i} {s['score']} {(s['domain'] or '')[:24]}", fill="blue")
            d.text((x + 3, 16), (s["title"] or "")[:40], fill="black")
            d.text((x + 3, 30), (s["title"] or "")[40:80], fill="black")
        sh.save(f"{out}/{name}_sheet.jpg", quality=85)
        top = max((s for _, s in good), key=lambda s: s["score"], default={})
        print(f"{name}: {len(res['sites'])} pages; best {top.get('score')} {top.get('domain')} {(top.get('title') or '')[:60]}"
              + ("  [CAPTCHA]" if res["captcha"] else ""), flush=True)
        time.sleep(8)


if __name__ == "__main__":
    main()
