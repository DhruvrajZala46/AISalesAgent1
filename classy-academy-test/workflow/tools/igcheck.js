// PW=$(npm root -g)/playwright node igcheck.js <reel-or-post-url>... : render Instagram's public embed and read the author + caption
const { chromium } = require(process.env.PW);
(async () => {
  const browser = await chromium.launch({ args: ['--no-sandbox'], proxy: process.env.HTTPS_PROXY ? { server: process.env.HTTPS_PROXY } : undefined });
  const ctx = await browser.newContext({ locale: 'en-US', ignoreHTTPSErrors: true, userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0 Safari/537.36' });
  for (const u of process.argv.slice(2)) {
    const page = await ctx.newPage();
    const e = u.replace(/\?.*$/, '').replace(/\/$/, '') + '/embed/captioned/';
    try {
      await page.goto(e, { waitUntil: 'networkidle', timeout: 45000 });
      const user = await page.$eval('.UsernameText, .Username', n => n.innerText).catch(() => null);
      const cap = await page.$eval('.Caption', n => n.innerText).catch(() => null);
      const body = (await page.innerText('body').catch(() => '')).replace(/\s+/g, ' ').slice(0, 200);
      console.log(JSON.stringify({ url: u, user, caption: cap && cap.slice(0, 200), body: user ? undefined : body }));
    } catch (err) { console.log(JSON.stringify({ url: u, error: err.message.slice(0, 80) })); }
    await page.close();
  }
  await browser.close();
})();
