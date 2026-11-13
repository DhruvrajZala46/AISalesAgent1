const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  const errs = []; p.on('pageerror', e => errs.push(e.message)); p.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
  await p.goto('file://' + process.argv[2] + '/index.html'); await p.waitForTimeout(1500);
  const r = await p.evaluate((t) => {
    const tl = window.__timelines && window.__timelines.main; if (!tl) return 'no timeline';
    tl.seek(t); const q = id => { const e = document.querySelector(id); if (!e) return id + ' missing'; const cs = getComputedStyle(e); return `${id} vis=${cs.visibility} op=${cs.opacity} tf=${cs.transform}`; };
    return ['#s1', '#s1c', '#k1', '#h1', '#tm'].map(q).join('\n');
  }, parseFloat(process.argv[3]));
  console.log(r); console.log('errors:', errs.slice(0, 5).join(' | '));
  await b.close();
})();
