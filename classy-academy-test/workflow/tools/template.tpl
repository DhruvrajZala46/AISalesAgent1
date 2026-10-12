<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=1920, height=1080" />
<title>%TITLE%</title>
<script src="gsap.min.js"></script>
<style>
@font-face { font-family: "Pinyon"; src: url("fonts/PinyonScript-Regular.ttf"); }
@font-face { font-family: "Playfair"; src: url("fonts/PlayfairDisplay.ttf"); }
body { margin: 0; background: #000; }
#root { position: relative; width: 100%; height: 100%; overflow: hidden; background: #c38d62; }
.bg { position: absolute; inset: -180px; filter: blur(90px);
  background:
   radial-gradient(40% 45% at 22% 30%, #dba778 0%, transparent 70%),
   radial-gradient(35% 40% at 70% 18%, #e2b07f 0%, transparent 70%),
   radial-gradient(45% 50% at 30% 80%, #b06e42 0%, transparent 70%),
   radial-gradient(40% 45% at 85% 75%, #a8673e 0%, transparent 70%),
   radial-gradient(30% 35% at 55% 50%, #c99a76 0%, transparent 70%),
   #c38d62; }
.w { position: absolute; overflow: hidden; }
.canvas { position: absolute; inset: -60px; overflow: hidden; }
.canvas video { width: 100%; height: 100%; object-fit: cover; filter: blur(38px) brightness(.82) saturate(.9); }
.med { width: 100%; height: 100%; object-fit: cover; display: block; }
.snow { position: absolute; inset: 0; mix-blend-mode: screen; pointer-events: none; z-index: 40; }
.snow video { width: 100%; height: 100%; object-fit: cover; }
.white { position: absolute; inset: 0; background: #fff; z-index: 48; }
.card, .q1, .q2, .qr1, .qr2, .qs1, .qs2, .hint, .rcp, .gtx1, .gtx2 { position: absolute; left: 0; right: 0; text-align: center; z-index: 45;
  --p: 100;
  -webkit-mask-image: linear-gradient(90deg, #000 45%, transparent 55%); mask-image: linear-gradient(90deg, #000 45%, transparent 55%);
  -webkit-mask-size: 220% 100%; mask-size: 220% 100%;
  -webkit-mask-position: calc(var(--p) * 1%) 0; mask-position: calc(var(--p) * 1%) 0; }
.card { z-index: 49 !important; top: 0; bottom: 0; display: flex; align-items: center; justify-content: center; font-family: "Pinyon"; font-size: 120px; color: #111; }
.q1, .q2, .qr1, .qr2 { color: #fff; font-family: "Playfair"; text-shadow: 0 2px 18px rgba(60,40,25,.25); }
.q1 { top: 430px; font-size: 84px; }
.q2 { top: 548px; font-size: 76px; }
.qr1 { left: 680px; right: 30px; top: 440px; font-size: 66px; }
.qr2 { left: 680px; right: 30px; top: 540px; font-size: 66px; }
.q1 i, .q2 i, .qr1 i, .qr2 i { font-family: "Pinyon"; font-style: normal; font-size: 1.25em; line-height: 0.8; }
.title { position: absolute; left: 0; right: 0; top: 400px; text-align: center; color: #fff; z-index: 45; text-shadow: 0 2px 22px rgba(0,0,0,.25); }
.title .ep { font-family: "Playfair"; font-size: 58px; }
.title .big { font-family: "Pinyon"; font-size: 104px; margin-top: 0px; white-space: nowrap; }
.logo { position: absolute; left: 42px; top: 38px; width: 150px; height: 151px; z-index: 47; opacity: .92; }
.black { position: absolute; inset: 0; background: #000; z-index: 60; }

/* ---- motion-graphic layer ---- */
.tag { position: absolute; z-index: 46; color: #fff; font-family: "Playfair"; font-size: 34px; letter-spacing: 3px; text-transform: lowercase; text-align: center; text-shadow: 0 2px 14px rgba(0,0,0,.45); }
.tag .ln { display: block; height: 2px; background: rgba(255,255,255,.85); margin: 10px auto 0; width: 0; }
.tag .mk { font-family: "Pinyon"; font-size: 50px; text-transform: none; letter-spacing: 0; margin-right: 8px; }
.lay { position: absolute; left: 760px; z-index: 46; color: #fff; font-family: "Playfair"; font-size: 46px; text-shadow: 0 2px 16px rgba(60,40,25,.3); white-space: nowrap; }
.lay b { font-family: "Pinyon"; font-weight: normal; font-size: 64px; margin-right: 22px; }
.lay .ln { position: absolute; left: -90px; top: 38px; height: 2px; width: 70px; background: rgba(255,255,255,.9); transform-origin: 100% 50%; }
.sw { position: absolute; z-index: 46; width: 230px; text-align: center; }
.sw .dot { width: 190px; height: 190px; border-radius: 50%; margin: 0 auto; box-shadow: 0 10px 30px rgba(60,30,15,.35), inset 0 0 0 6px rgba(255,255,255,.18); }
.sw .nm { margin-top: 18px; font-family: "Pinyon"; font-size: 64px; color: #fff; text-shadow: 0 2px 14px rgba(60,40,25,.3); }
.guide { position: absolute; z-index: 46; left: 1080px; top: 250px; width: 620px; height: 580px; background: #fbf7f2; border-radius: 6px; box-shadow: 0 30px 70px rgba(60,30,15,.35); text-align: center; color: #3b2a20; }
.guide .k { font-family: "Playfair"; font-size: 30px; letter-spacing: 6px; margin-top: 80px; }
.guide .t { font-family: "Pinyon"; font-size: 96px; margin-top: 20px; line-height: 1.05; }
.guide .s { font-family: "Playfair"; font-size: 30px; margin-top: 40px; color: #8a6a55; }
.chk { position: absolute; left: 1010px; z-index: 46; color: #fff; font-family: "Playfair"; font-size: 46px; white-space: nowrap; text-shadow: 0 2px 16px rgba(60,40,25,.3); }
.chk svg { position: absolute; left: -78px; top: 6px; width: 54px; height: 54px; }
.chk svg path { fill: none; stroke: #fff; stroke-width: 5; stroke-linecap: round; stroke-linejoin: round; stroke-dasharray: 80; stroke-dashoffset: 80; }
.endc { position: absolute; z-index: 46; left: 1010px; top: 300px; width: 760px; height: 428px; border: 2px solid rgba(255,255,255,.85); border-radius: 4px; overflow: hidden; }
.endt { position: absolute; z-index: 46; left: 1010px; top: 210px; width: 760px; text-align: center; font-family: "Pinyon"; font-size: 72px; color: #fff; }

.hint { top: 455px; font-family: "Pinyon"; font-size: 92px; color: #fff; text-shadow: 0 2px 16px rgba(60,40,25,.3); }
.rcp { left: 716px !important; right: auto !important; width: 488px; font-family: "Playfair"; font-size: 40px; color: #fff; text-shadow: 0 2px 14px rgba(60,40,25,.35); }
.hd { position: absolute; z-index: 46; width: 516px; text-align: center; font-family: "Pinyon"; font-size: 66px; color: #fff; text-shadow: 0 2px 14px rgba(60,40,25,.35); }
.haze { position: absolute; inset: 0; background: rgba(248,238,228,.42); z-index: 44; }
.gtx1 { top: 455px; font-family: "Playfair"; font-size: 40px; color: #fff; text-shadow: 0 2px 18px rgba(80,55,35,.45); }
.gtx2 { top: 500px; font-family: "Pinyon"; font-size: 104px; color: #fff; text-shadow: 0 2px 18px rgba(80,55,35,.45); }
.endlogo { position: absolute; left: 760px; top: 340px; width: 400px; height: 402px; z-index: 62; }
.endwhite { position: absolute; inset: 0; background: #fff; z-index: 61; }
.cut { position: absolute; z-index: 46; display: flex; flex-direction: column; align-items: center; }
.cut img { max-width: 100%; max-height: 100%; object-fit: contain; filter: drop-shadow(0 22px 26px rgba(70,35,15,.38)); }
.cut .lb { margin-top: 10px; font-family: "Pinyon"; font-size: 46px; color: #fff; white-space: nowrap; text-shadow: 0 2px 14px rgba(60,40,25,.35); }
.cl { position: absolute; z-index: 46; text-align: center; font-family: "Pinyon"; font-size: 64px; color: #fff; text-shadow: 0 2px 16px rgba(0,0,0,.45); }
.photo { width: 100%; height: 100%; object-fit: cover; display: block; filter: contrast(1.03) saturate(.95) sepia(.05); }
.title .ep { font-size: 46px; letter-spacing: 2px; }
.qs1, .qs2 { left: 820px !important; right: 40px !important; color: #fff; font-family: "Playfair"; font-size: 64px; text-shadow: 0 2px 18px rgba(60,40,25,.25); }
.qs1 { top: 430px; } .qs2 { top: 528px; }
.qs1 i, .qs2 i { font-family: "Pinyon"; font-style: normal; font-size: 1.3em; line-height: 0.8; }
</style>
</head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-width="1920" data-height="1080" data-duration="%DUR%">
  <div id="bg" class="bg"></div>
%ELS%
  <img id="logo" class="logo" src="assets/logo_ce.png">
  <div id="black" class="black"></div>
  <audio id="mix" src="assets/mix.wav" data-start="0" data-duration="%DUR%" data-track-index="0"></audio>
</div>
<script>
const tl = gsap.timeline({ paused: true });
tl.fromTo("#black", { opacity: 1 }, { opacity: 0, duration: 1.0, ease: "none" }, 0);
tl.fromTo("#bg", { x: -60, y: -30, rotation: 0 }, { x: 60, y: 40, rotation: 6, duration: %DUR%, ease: "sine.inOut" }, 0);
%TW%
window.__timelines["main"] = tl;
</script>
</body>
</html>
