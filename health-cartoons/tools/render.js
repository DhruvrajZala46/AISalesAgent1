// Frame-accurate render of a video folder's scene.html -> video.mp4 (30 fps, 720x1280).
// Usage (from the video folder): node ../../tools/render.js [seconds] [out.mp4]   (default: whole video from data.json -> video.mp4)
const {chromium}=require('playwright');const {spawn}=require('child_process');const fs=require('fs');
(async()=>{const FPS=30,DUR=process.argv[2]?parseFloat(process.argv[2]):JSON.parse(fs.readFileSync('data.json')).end,OUT=process.argv[3]||'video.mp4';
const b=await chromium.launch();const p=await b.newPage({viewport:{width:720,height:1280}});
p.on('pageerror',e=>console.log('ERR',e.message));
await p.goto('file://'+process.cwd()+'/scene.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
const ff=spawn('ffmpeg',['-v','error','-y','-f','image2pipe','-framerate',String(FPS),'-c:v','mjpeg','-i','-','-c:v','libx264','-pix_fmt','yuv420p','-crf','17','-preset','medium',OUT]);
const N=Math.ceil(DUR*FPS);
for(let i=0;i<N;i++){await p.evaluate(t=>render(t),i/FPS);const buf=await p.screenshot({type:'jpeg',quality:95});
 if(!ff.stdin.write(buf)) await new Promise(r=>ff.stdin.once('drain',r)); if(i%300==0)console.log('frame',i,'/',N);}
ff.stdin.end();await new Promise(r=>ff.on('close',r));await b.close();console.log('done');})();
