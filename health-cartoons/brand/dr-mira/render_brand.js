const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();
for(const [fn,w,h,out] of [['drawAvatar',800,800,'avatar.png'],['drawBanner',2560,1440,'banner.png']]){
 const p=await b.newPage({viewport:{width:w,height:h}});p.on('pageerror',e=>console.log('ERR',e.message));
 await p.goto('file://'+process.cwd()+'/mira.html');await p.evaluate(()=>document.fonts.ready);await p.evaluate(f=>window[f](),fn);await p.waitForTimeout(200);
 await p.screenshot({path:out,clip:{x:0,y:0,width:w,height:h}});await p.close();}
await b.close();console.log('done');})();
