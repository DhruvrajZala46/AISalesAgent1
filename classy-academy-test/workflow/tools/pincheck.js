// open each Pinterest pin URL in a real browser and report the page title and whether the pin's own text shows
// PW=$(npm root -g)/playwright node pincheck.js jobs.json out.json   jobs = {name: {url, probe, pinner}}
const { chromium } = require(process.env.PW);
(async () => {
  const jobs = JSON.parse(require('fs').readFileSync(process.argv[2], 'utf8'));
  const b = await chromium.launch(); const ctx = await b.newContext({ userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36', locale: 'en-US' });
  const out = {};
  for (const [f, j] of Object.entries(jobs)) {
    const p = await ctx.newPage();
    try {
      const r = await p.goto(j.url, { waitUntil: 'domcontentloaded', timeout: 45000 }); await p.waitForTimeout(6000);
      const title = await p.title(); const body = (await p.innerText('body')).slice(0, 4000);
      out[f] = { status: r.status(), final: p.url(), title, found: j.probe ? body.includes(j.probe) || title.includes(j.probe) : null, pinner_seen: j.pinner ? body.toLowerCase().includes(j.pinner.toLowerCase()) : null };
    } catch (e) { out[f] = { err: String(e).slice(0, 200) }; }
    console.log(f, JSON.stringify(out[f])); await p.close();
  }
  require('fs').writeFileSync(process.argv[3], JSON.stringify(out, null, 1)); await b.close();
})();
