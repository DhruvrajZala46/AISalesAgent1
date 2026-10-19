// screenshot Instagram's public embed page of a post or profile: node embshot.js outdir url...
const { chromium } = require(process.env.PW);
(async () => {
  const [out, ...urls] = process.argv.slice(2);
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 540, height: 1100 } });
  for (const u of urls) {
    const name = u.replace(/https:\/\/www\.instagram\.com\//, '').replace(/\//g, '_');
    try { await p.goto(u, { waitUntil: 'networkidle', timeout: 45000 }); await p.waitForTimeout(3000);
          await p.screenshot({ path: `${out}/${name}.png`, fullPage: true }); console.log('ok', name); }
    catch (e) { console.log('err', name, String(e).slice(0, 120)); }
  }
  await b.close();
})();
