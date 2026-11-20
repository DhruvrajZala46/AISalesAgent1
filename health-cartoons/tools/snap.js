const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:720,height:1280}});
p.on('pageerror',e=>console.log('ERR',e.message));p.on('console',m=>console.log('LOG',m.text()));
await p.goto('file://'+process.cwd()+'/scene.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
const ts=process.argv.slice(2).map(Number);
for(const t of ts){await p.evaluate(t=>render(t),t);await p.screenshot({path:`snap_${t}.png`});}
await b.close();})();
