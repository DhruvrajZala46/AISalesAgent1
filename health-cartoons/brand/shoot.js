const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();
 for(const [m,w,h,out] of [['dp',800,800,'dp.png'],['banner',2560,1440,'banner.png']]){const p=await b.newPage({viewport:{width:w,height:h}});
  p.on('pageerror',e=>console.log('ERR',e.message));await p.goto('file://'+process.cwd()+'/brand.html#'+m);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(400);
  await p.screenshot({path:out});await p.close();}
 await b.close();})();
