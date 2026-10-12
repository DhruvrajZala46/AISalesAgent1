// usage: node ffr_capture.js <dir with node_modules/puppeteer-core> <project dir> <out dir>   (see ffr.py)
// Capture every text / graphic element exactly as Chrome draws it (fonts, shadows), on a transparent background,
// with transforms, masks and opacity reset. Output: sprites/<id>.png + sprites.json (border-box geometry).
const puppeteer = require(process.argv[2] + '/node_modules/puppeteer-core');
const fs = require('fs'), path = require('path');
const P = process.argv[3];            // project dir (index.html)
const OUT = process.argv[4];          // output dir
const OFF = 200;                      // shift the stage so the oversized backdrop can be captured
(async () => {
  let html = fs.readFileSync(path.join(P, 'index.html'), 'utf8');
  html = html.replace(/<script>\s*const tl[\s\S]*?<\/script>/, '');            // no GSAP: static final state
  html = html.replace('<body>', `<body style="background:transparent;margin:0">`);
  fs.writeFileSync(path.join(P, '_capture.html'), html);
  const b = await puppeteer.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args: ['--no-sandbox', '--force-color-profile=srgb', '--font-render-hinting=none'] });
  const pg = await b.newPage();
  await pg.setViewport({ width: 1920 + 2 * OFF, height: 1080 + 2 * OFF, deviceScaleFactor: 1 });
  await pg.goto('file://' + path.join(P, '_capture.html'), { waitUntil: 'networkidle0' });
  await pg.evaluate(async (OFF) => {
    await document.fonts.ready;
    const r = document.getElementById('root');
    r.style.position = 'absolute'; r.style.left = OFF + 'px'; r.style.top = OFF + 'px';
    r.style.width = '1920px'; r.style.height = '1080px'; r.style.overflow = 'visible'; r.style.background = 'transparent';
    document.querySelectorAll('video,audio').forEach(v => v.remove());
  }, OFF);
  const ids = await pg.evaluate(() => {
    const keep = ['card','hint','q1','q2','qr1','qr2','qs1','qs2','gtx1','gtx2','title','cl','hd','chk','logo','endlogo','bg','rcp'];
    return [...document.querySelectorAll('#root > *')].filter(e => e.id && keep.some(k => e.classList.contains(k))).map(e => [e.id, e.className]);
  });
  const meta = {};
  const MASKED = ['card','hint','q1','q2','qr1','qr2','qs1','qs2','gtx1','gtx2','rcp'];
  for (const [id, cls] of ids) {
    const parts = cls.includes('chk') ? ['text', 'mark'] : ['all'];
    for (const part of parts) {
      const box = await pg.evaluate((id, part) => {
        // reset what earlier captures switched on: an svg left visibility:visible shows through its hidden parent
        // and would be baked into every later sprite that overlaps it
        for (const e of document.querySelectorAll('#root svg')) e.style.visibility = '';
        for (const e of document.querySelectorAll('#root > *')) e.style.visibility = 'hidden';
        const e = document.getElementById(id);
        e.style.visibility = 'visible'; e.style.opacity = '1'; e.style.transform = 'none';
        e.style.webkitMaskImage = 'none'; e.style.maskImage = 'none';
        const svg = e.querySelector('svg');
        if (svg) {
          const p = svg.querySelector('path'); p.style.strokeDashoffset = '0';
          if (part === 'text') svg.style.visibility = 'hidden';
          if (part === 'mark') { svg.style.visibility = 'visible'; e.style.color = 'transparent'; e.style.textShadow = 'none'; }
          else svg.style.visibility = part === 'all' ? 'visible' : svg.style.visibility;
        }
        const r = e.getBoundingClientRect();
        return { x: r.left, y: r.top, w: r.width, h: r.height };
      }, id, part);
      const masked = MASKED.some(k => cls.split(' ').includes(k));
      // masked elements: the mask clips to the border box. Others: grab a padded area so shadows are kept.
      const pad = masked ? 0 : (cls.includes('bg') ? 0 : (cls.includes('chk') ? 110 : 40));
      let clip = { x: Math.floor(box.x - pad), y: Math.floor(box.y - pad), width: Math.ceil(box.w + 2 * pad), height: Math.ceil(box.h + 2 * pad) };
      if (cls.includes('bg')) clip = { x: 0, y: 0, width: 1920 + 2 * OFF, height: 1080 + 2 * OFF };
      const f = path.join(OUT, `${id}_${part}.png`);
      await pg.screenshot({ path: f, clip, omitBackground: true });
      meta[`${id}_${part}`] = { id, part, cls, x: clip.x - OFF, y: clip.y - OFF, w: clip.width, h: clip.height,
                                bx: box.x - OFF, by: box.y - OFF, bw: box.w, bh: box.h, masked };
    }
  }
  fs.writeFileSync(path.join(OUT, 'sprites.json'), JSON.stringify(meta, null, 1));
  await b.close();
  console.log('captured', Object.keys(meta).length);
})();
