# host.py - the hand-drawn host character (inline SVG, no AI tools): a friendly young Gujarati man in a checked shirt
# holding a steel glass. Rig ids: #hd (head), #brL/#brR (brows), #eyL/#eyR (eyes, scaleY to blink), #m0..#m3 (mouth shapes),
# #arm (forearm + glass). host_svg() returns the <svg> markup; mock.html shows the opening frame.
SKIN, SKIN_D, SKIN_L = '#c98d62', '#ad7149', '#d9a077'
HAIR = '#1e1916'

def host_svg(w=620, h=700):
    return f'''<svg id="host" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 620 700" width="{w}" height="{h}" style="overflow:visible">
<defs>
  <pattern id="chk" width="46" height="46" patternUnits="userSpaceOnUse" patternTransform="rotate(3)">
    <rect width="46" height="46" fill="#f4f6f9"/>
    <rect x="0" y="0" width="12" height="46" fill="#8fb0d1" opacity=".55"/><rect x="0" y="0" width="46" height="12" fill="#8fb0d1" opacity=".55"/>
    <rect x="26" y="0" width="3" height="46" fill="#3f5f85" opacity=".55"/><rect x="0" y="26" width="46" height="3" fill="#3f5f85" opacity=".55"/>
  </pattern>
  <linearGradient id="steel" x1="0" x2="1"><stop offset="0" stop-color="#8f9aa5"/><stop offset=".22" stop-color="#eef2f5"/><stop offset=".5" stop-color="#b4bec8"/><stop offset=".8" stop-color="#f4f7f9"/><stop offset="1" stop-color="#97a2ad"/></linearGradient>
  <filter id="stk" x="-12%" y="-12%" width="124%" height="124%">
    <feMorphology in="SourceAlpha" operator="dilate" radius="8" result="d"/><feFlood flood-color="#fff"/><feComposite in2="d" operator="in" result="o"/>
    <feGaussianBlur in="d" stdDeviation="10" result="b"/><feOffset in="b" dy="10" result="s"/><feFlood flood-color="#000" flood-opacity=".35"/><feComposite in2="s" operator="in" result="sh"/>
    <feMerge><feMergeNode in="sh"/><feMergeNode in="o"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
</defs>
<g filter="url(#stk)">
  <!-- torso -->
  <path d="M30 700 C30 590 84 528 176 502 L262 474 L358 474 L444 502 C536 528 590 590 590 700 Z" fill="url(#chk)"/>
  <path d="M30 700 C30 590 84 528 176 502 L262 474 L358 474 L444 502 C536 528 590 590 590 700 Z" fill="#20324a" opacity=".06"/>
  <!-- neck -->
  <path d="M262 392 L262 486 C284 522 336 522 358 486 L358 392 Z" fill="{SKIN_D}"/>
  <path d="M262 430 C290 456 330 456 358 430 L358 400 L262 400 Z" fill="#000" opacity=".16"/>
  <!-- collar -->
  <path d="M258 468 L310 528 L268 560 L226 492 Z" fill="#fbfcfe"/><path d="M362 468 L310 528 L352 560 L394 492 Z" fill="#fbfcfe"/>
  <path d="M310 528 L310 700" stroke="#b9c7d8" stroke-width="4"/>
  <circle cx="310" cy="580" r="6" fill="#dfe6ee"/><circle cx="310" cy="640" r="6" fill="#dfe6ee"/>
  <!-- head -->
  <g id="hd">
    <ellipse cx="190" cy="282" rx="19" ry="32" fill="{SKIN_D}"/><ellipse cx="430" cy="282" rx="19" ry="32" fill="{SKIN_D}"/>
    <path d="M192 246 C192 150 246 104 310 104 C374 104 428 150 428 246 L428 300 C428 372 374 420 310 420 C246 420 192 372 192 300 Z" fill="{SKIN}"/>
    <path d="M310 104 C374 104 428 150 428 246 L428 300 C428 372 374 420 310 420 C352 400 392 350 392 280 C392 190 368 130 310 104 Z" fill="{SKIN_D}" opacity=".28"/>
    <!-- beard: short, close to the jaw -->
    <path d="M192 268 C194 300 198 326 206 344 C222 392 264 424 310 424 C356 424 398 392 414 344 C422 326 426 300 428 268 C420 284 416 304 410 322 C400 350 376 368 352 366 C344 352 328 344 310 344 C292 344 276 352 268 366 C244 368 220 350 210 322 C204 304 200 284 192 268 Z" fill="{HAIR}" opacity=".93"/>
    <path d="M270 380 C284 392 336 392 350 380 C350 404 334 414 310 414 C286 414 270 404 270 380 Z" fill="{HAIR}" opacity=".93"/>
    <!-- cheeks -->
    <ellipse cx="232" cy="312" rx="24" ry="14" fill="#e59a7a" opacity=".35"/><ellipse cx="388" cy="312" rx="24" ry="14" fill="#e59a7a" opacity=".35"/>
    <!-- hair -->
    <path d="M186 262 C170 168 224 84 314 82 C400 80 452 160 434 262 C430 222 418 190 396 172 C352 196 280 194 236 164 C208 186 192 220 186 262 Z" fill="{HAIR}"/>
    <path d="M236 164 C262 120 330 100 384 126" stroke="#3a322d" stroke-width="5" fill="none" opacity=".6"/>
    <!-- brows -->
    <path id="brL" d="M230 230 C246 219 268 219 282 228" stroke="{HAIR}" stroke-width="9" stroke-linecap="round" fill="none"/>
    <path id="brR" d="M338 228 C352 219 374 219 390 230" stroke="{HAIR}" stroke-width="9" stroke-linecap="round" fill="none"/>
    <!-- eyes -->
    <g id="eyL" style="transform-origin:258px 268px"><ellipse cx="258" cy="268" rx="21" ry="15" fill="#fff"/><circle cx="260" cy="269" r="11.5" fill="#3b2415"/><circle cx="260" cy="269" r="5.5" fill="#0c0806"/><circle cx="255.5" cy="264.5" r="3.6" fill="#fff"/>
      <path d="M236 266 C246 253 270 253 280 266" stroke="{HAIR}" stroke-width="5.5" fill="none" stroke-linecap="round"/></g>
    <g id="eyR" style="transform-origin:362px 268px"><ellipse cx="362" cy="268" rx="21" ry="15" fill="#fff"/><circle cx="364" cy="269" r="11.5" fill="#3b2415"/><circle cx="364" cy="269" r="5.5" fill="#0c0806"/><circle cx="359.5" cy="264.5" r="3.6" fill="#fff"/>
      <path d="M340 266 C350 253 374 253 384 266" stroke="{HAIR}" stroke-width="5.5" fill="none" stroke-linecap="round"/></g>
    <!-- nose -->
    <path d="M310 268 C306 292 296 308 300 316 C305 324 318 324 324 314" stroke="{SKIN_D}" stroke-width="6" fill="none" stroke-linecap="round"/>
    <!-- moustache -->
    <path d="M266 342 C280 328 298 330 310 336 C322 330 340 328 354 342 C340 339 324 344 310 344 C296 344 280 339 266 342 Z" fill="{HAIR}"/>
    <!-- mouths: m0 smile, m1 small open, m2 wide open, m3 "o" -->
    <g id="m0"><path d="M282 353 C294 366 326 366 338 353" stroke="#4a1c17" stroke-width="6.5" fill="none" stroke-linecap="round"/></g>
    <g id="m1" style="visibility:hidden"><path d="M286 354 C298 350 322 350 334 354 C330 368 290 368 286 354 Z" fill="#4a1c17"/><path d="M290 354 C300 352 320 352 330 354 L328 358 C318 356 302 356 292 358 Z" fill="#fff"/></g>
    <g id="m2" style="visibility:hidden"><path d="M283 351 C296 346 324 346 337 351 C335 381 285 381 283 351 Z" fill="#4a1c17"/><path d="M288 351 C300 348 320 348 332 351 L330 358 C318 356 302 356 290 358 Z" fill="#fff"/><ellipse cx="310" cy="373" rx="15" ry="6" fill="#c8605a"/></g>
    <g id="m3" style="visibility:hidden"><ellipse cx="310" cy="361" rx="15" ry="13" fill="#4a1c17"/><ellipse cx="310" cy="369" rx="9" ry="5" fill="#c8605a"/></g>
  </g>
  <!-- right forearm + steel glass -->
  <g id="arm" style="transform-origin:560px 700px">
    <path d="M470 700 C474 640 486 600 500 572 L566 590 C572 630 580 664 600 700 Z" fill="url(#chk)"/>
    <path d="M444 438 L548 438 L536 592 L456 592 Z" fill="url(#steel)"/>
    <ellipse cx="496" cy="438" rx="52" ry="11" fill="#cfd7de"/><ellipse cx="496" cy="440" rx="44" ry="8" fill="#9fd4ee"/>
    <path d="M452 470 L540 470" stroke="#fff" stroke-width="3" opacity=".5"/>
    <!-- fingers -->
    <rect x="490" y="486" width="74" height="24" rx="12" fill="{SKIN}"/><rect x="494" y="512" width="74" height="24" rx="12" fill="{SKIN}"/>
    <rect x="494" y="538" width="72" height="24" rx="12" fill="{SKIN}"/><rect x="490" y="564" width="68" height="22" rx="11" fill="{SKIN}"/>
    <path d="M540 486 C580 486 592 520 588 560 C586 584 572 596 552 594 L548 500 Z" fill="{SKIN}"/>
    <path d="M496 511 L548 511 M498 537 L548 537 M496 563 L546 563" stroke="{SKIN_D}" stroke-width="3" stroke-linecap="round" opacity=".8"/>
    <path d="M440 520 C430 500 440 484 456 486 C466 488 470 500 466 516 Z" fill="{SKIN}"/>
  </g>
</g>
</svg>'''

if __name__ == '__main__':
    css = open('fonts.css').read() if __import__('os').path.exists('fonts.css') else ''
    html = f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face {{ font-family: "Anek"; src: url("fonts/anek-gujarati-gujarati-wdth-normal.woff2") format("woff2"); font-stretch: 75% 125%; font-weight: 100 900; unicode-range: U+0A80-0AFF, U+200C-200D, U+25CC; }}
@font-face {{ font-family: "Anek"; src: url("fonts/anek-devanagari-latin-wdth-normal.woff2") format("woff2"); font-stretch: 75% 125%; font-weight: 100 900; unicode-range: U+0000-00FF, U+2010-2212; }}
body {{ margin: 0; background: #000; }} #root {{ position: relative; width: 1080px; height: 1920px; overflow: hidden; font-family: "Anek", sans-serif; font-stretch: 85%; }}
.top {{ position: absolute; left: 0; top: 0; width: 1080px; height: 720px; overflow: hidden; background: linear-gradient(#aee0fb 0%, #dff3fd 62%, #cfe9c4 62%, #b9dca0 100%); }}
.sun {{ position: absolute; left: 90px; top: 70px; width: 150px; height: 150px; border-radius: 50%; background: #fff6c9; box-shadow: 0 0 80px 40px rgba(255,246,201,.8); }}
.tree {{ position: absolute; border-radius: 50%; background: #5c9a4e; filter: blur(3px); }}
.field {{ position: absolute; left: 0; right: 0; top: 446px; bottom: 0; background: repeating-linear-gradient(100deg, #b9dca0 0 60px, #a9d18f 60px 120px); filter: blur(2px); }}
.bot {{ position: absolute; left: 0; top: 720px; width: 1080px; height: 1200px; overflow: hidden; background: #123; }}
.bot img {{ width: 1080px; height: 1200px; object-fit: cover; }}
.pill {{ position: absolute; left: 0; right: 0; margin: 0 auto; width: fit-content; top: 664px; z-index: 9; background: #fff; color: #e8590c; font-weight: 900; font-size: 84px; padding: 10px 46px 20px; border-radius: 70px; box-shadow: 0 12px 30px rgba(0,0,0,.35); }}
.cap {{ position: absolute; left: 40px; right: 40px; top: 1500px; text-align: center; z-index: 9; font-weight: 900; font-size: 110px; color: #fff; text-shadow: 4px 4px 0 #000, -4px 4px 0 #000, 4px -4px 0 #000, -4px -4px 0 #000, 0 10px 26px rgba(0,0,0,.75); }}
</style></head><body><div id="root">
<div class="top"><div class="sun"></div><div class="field"></div>
<div class="tree" style="left:-60px;top:300px;width:330px;height:240px"></div><div class="tree" style="left:820px;top:250px;width:380px;height:290px;background:#4f8a44"></div><div class="tree" style="left:640px;top:360px;width:220px;height:150px;background:#6aa85a"></div>
<div style="position:absolute;left:170px;top:-6px">{host_svg(740, 836)}</div></div>
<div class="bot"><img src="chk/bot.jpg"></div>
<div class="pill">સવારે કયું પાણી પીવું? 🤔</div>
<div class="cap">કોઈને સમજાતું જ નથી</div>
</div></body></html>'''
    open('mock.html', 'w').write(html); print('mock.html written')
