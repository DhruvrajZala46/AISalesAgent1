// click through an Instagram embed carousel and screenshot every slide: node slides.js out_prefix url
// PW=$(npm root -g)/playwright node igslides.js <out_prefix> https://www.instagram.com/p/<id>/embed/
const { chromium } = require(process.env.PW);
(async () => {
  const [pre, u] = process.argv.slice(2);
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 540, height: 900 } });
  await p.goto(u, { waitUntil: 'networkidle', timeout: 45000 }); await p.waitForTimeout(2500);
  for (let i = 0; i < 12; i++) {
    await p.screenshot({ path: `${pre}_${i}.png` });
    const nxt = await p.$('button[aria-label="Next"], .coreSpriteRightChevron, [aria-label="Next"]');
    if (!nxt) { console.log('slides', i + 1); break; }
    await nxt.click(); await p.waitForTimeout(1200);
  }
  await b.close();
})();
