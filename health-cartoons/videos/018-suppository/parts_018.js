// =============== 018: "How does a suppository fix constipation?" One locked body scene, then the hospital room. ===============
const E=D.ev, ST=D.start, END=D.end;
//__VISEME__
const lend=id=>{const L=D.lines.find(l=>l.id===id);return L.t0+L.dur;};
const inL=(id,T,pre=.05,post=.1)=>T>=ST[id]-pre&&T<lend(id)+post;
const svg=$('S');
const S1=`<g id="s1">${bodyWorld()}${labelBox('lbR','RECTUM',590,470,28)}${labelBox('lbS','HARD STOOL',548,372,26)}${labelBox('lbP','SUPPOSITORY',560,1010,26)}</g>`, S3=`<g id="s3"><rect x="-40" y="-40" width="800" height="400" fill="#cfe0e6"/><g transform="translate(0,150)">${ward()}</g><g transform="translate(360,24) scale(.82) translate(-360,-30)">${board()}</g></g>`;
svg.innerHTML=`<defs><filter id="soft" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="7"/></filter>${DEFS}</defs>`
 +S1+S3+`<text id="wm" x="120" y="700" text-anchor="middle" style="font-family:ComicNeue,sans-serif;font-weight:700;font-size:24px" fill="#fff" stroke="#0b6e6b" stroke-width=".6" opacity=".7">@GiggleMD</text>`
 +`<g id="capg"><text id="cap" class="cap" x="360" y="1015" text-anchor="middle" style="stroke-width:7px;font-size:48px"></text></g>`;
function face(id,r,{dx=0,dy=0,lid=.1,blink=0,small=false,bx=27,by=48,bw=26,bA=0,arch=3,talk=0,mw=12,mood=0,T=0,seed=0}){
  setOEye(id+'_eL',r,{dx,dy,lid,blink,small});setOEye(id+'_eR',r,{dx,dy,lid,blink,small});
  setBrow(id+'_bL',-bx,by,bw,bA,arch);setBrow(id+'_bR',bx,by,bw,-bA,arch);setMouthV(id+'_m',talk,mw,mood,T,seed);}
const mv=(id,x,y,r=0,s=1)=>$(id).setAttribute('transform',`translate(${x.toFixed(1)},${y.toFixed(1)}) rotate(${r.toFixed(1)}) scale(${s})`);
// the stool lumps: where they sit, and the order they leave in
const LP=[[352,268,-8],[690,196,6],[566,204,-4],[436,172,10],[330,160,-12]];
function pathPos(u){   // u: 0 at the lump's seat ... 1 far below the exit
  const pts=[[365,330],[365,620],[360,800],[360,905],[352,1060],[330,1420]];const n=pts.length-1,f=clamp(u)*n,i=Math.min(n-1,Math.floor(f)),k=f-i;return [lerp(pts[i][0],pts[i+1][0],k),lerp(pts[i][1],pts[i+1][1],k)];}
function renderBody(T){
  const soft=eio(P(T,E.melt+.5,E.soft+.4)),ins=eio(P(T,E.ins-.35,E.ins+.35)),melted=T>=E.melt,out=T>=E.out,clear=T>=E.clear;
  // ---- the glove and the suppository ----
  const gT=speak('glove',T),rise=eo(P(T,-.5,.5)),push=Math.sin(clamp(P(T,E.ins-.35,E.ins+.2))*Math.PI),side=eio(P(T,E.out-.3,E.out+.2))*(1-eio(P(T,E.clear,E.clear+.5)));
  const gx=372-side*210,gy=lerp(1190,1016,rise)-push*60+Math.sin(T*2.2)*5-gT*4;mv('glove',gx,gy,side*-10,1.22);
  face('gv',26,{dx:side?24:0,dy:out&&!clear?10:-26,lid:.05,blink:blinkK(T,1.7),bx:27,by:-40,bw:26,bA:inL('04_glove',T)||inL('08_glove',T)?-6:-2,arch:7,talk:gT,mw:13,mood:.7,T,seed:2});
  const sy=lerp(gy-156,676,ins),sOn=T<E.melt+.5;show('supp',sOn?1-P(T,E.melt,E.melt+.5):0);mv('supp',lerp(gx-16,362,ins),sy,0,lerp(1,1.15,ins)*(1-.5*P(T,E.melt,E.melt+.5)));
  const mk=P(T,E.melt,E.melt+.7),mOut=P(T,E.soft+.5,E.soft+1.6);show('melt',melted?(1-mOut)*.9:0);if(melted)mv('melt',362,lerp(676,690,mk),T*20,.5+mk*1.1);
  // water drawn toward the stool
  let dr='';if(T>=E.melt+.3&&T<E.out){for(let j=0;j<8;j++){const p=((T-E.melt)*.8+j/8)%1,sx=j%2?280:450,sy0=640+(j%4)*30,x=lerp(sx,352+((j%3)-1)*30,p*p),y=lerp(sy0,300,p);
    dr+=`<path transform="translate(${x.toFixed(1)},${y.toFixed(1)}) scale(1.5)" d="M0,-9 C5,-2 7,3 5,7 C3,11 -4,11 -5,7 C-7,3 -4,-2 0,-9Z" fill="#8fd0fb" stroke="${INK}" stroke-width="1.6" opacity="${(Math.sin(p*Math.PI)).toFixed(2)}"/>`;}}
  $('drops').innerHTML=dr;
  // ---- the stool ----
  const sT=speak('stool',T);
  LP.forEach(([x0,y0,r0],i)=>{const id='L'+i;let x=x0,y=y0,r=r0,sq=1;
    const t0=E.out+i*.27,u=eio(P(T,t0,t0+1.25));
    if(u>0){const a=clamp(u*5),p=pathPos(u);x=lerp(x0,p[0],a);y=lerp(y0,p[1],a);r=r0+u*200;sq=1-.25*Math.sin(clamp((p[1]-760)/200)*Math.PI);}
    else{const w=(.5+soft)*Math.sin(T*3.3+i*1.7)*2.5;x+=w;y+=(.5+soft)*Math.cos(T*2.7+i)*2.5;r+=Math.sin(T*2.1+i)*2.5;if(i===0&&inL('07_stool',T))y-=Math.abs(Math.sin((T-ST['07_stool'])*8))*10*sT;}
    mv(id,x,y,r);$(id+'_s').setAttribute('transform',`scale(${sq.toFixed(3)},${(2-sq).toFixed(3)})`);
    const c=Math.round(lerp(0x6b,0xa8,soft)),g=Math.round(lerp(0x3a,0x66,soft)),b2=Math.round(lerp(0x1c,0x34,soft));$(id+'_p').setAttribute('fill',`rgb(${c},${g},${b2})`);show(id+'_cr',1-soft);show(id+'_gl',soft);});
  face('L0',20.5,{dx:soft>.5?0:-6,dy:soft>.5?(out?30:-10):24,lid:soft>.5?.02:.3,blink:blinkK(T,2.6),small:false,bx:23,by:-30,bw:20,bA:soft>.5?-6:8,arch:soft>.5?8:2,talk:sT,mw:10,mood:soft>.5?.9:-.4,T,seed:6});
  // ---- the rectum ----
  const rT=speak('rect',T);
  let rf={dx:0,dy:30,lid:.05,bA:-12,arch:7,mood:-.5,small:T<1.2};                                   // alarmed, looking down at the glove
  if(inL('03_rect',T))rf={dx:0,dy:28,lid:.3,bA:12,arch:2,mood:-.6,small:false};
  if(T>=E.ins-.4&&!melted)rf={dx:Math.sin(T*10)*6,dy:16,lid:0,bA:-18,arch:6,mood:-.8,small:true};
  if(melted&&!out)rf={dx:0,dy:-24,lid:.05,bA:-8,arch:8,mood:-.1,small:false};
  if(out&&!clear)rf={dx:0,dy:30,lid:0,bA:-12,arch:9,mood:.2,small:false};
  if(clear)rf={dx:4,dy:24,lid:.12,bA:-4,arch:8,mood:.95,small:false};
  face('rc',32,{...rf,blink:blinkK(T,.8),bx:34,by:-48,bw:32,talk:rT,mw:16,T,seed:3});
  $('rface').setAttribute('transform',`translate(${(365+Math.sin(T*1.3)*3).toFixed(1)},${(505+Math.sin(T*2.6)*5-(T>=E.ins-.3&&!melted?push*10:0)).toFixed(1)}) scale(${(1.22+Math.sin(T*2.6)*.02).toFixed(3)},${(1.22-Math.sin(T*2.6)*.02).toFixed(3)})`);
  let fx='';if(push>.3)fx+=`<path d="M290,900 l-26,14 M430,900 l26,14 M300,930 l-20,22 M420,930 l20,22" stroke="${INK}" stroke-width="5" stroke-linecap="round" opacity="${push.toFixed(2)}"/>`;
  if(clear){[[300,200,0],[440,170,1],[620,190,2],[360,360,3],[400,640,4]].forEach(([x,y,j])=>{const k=.5+.5*Math.sin(T*7+j*1.9),r=9+11*k;fx+=`<path d="M${x},${y-r} Q${x+2},${y-2} ${x+r},${y} Q${x+2},${y+2} ${x},${y+r} Q${x-2},${y+2} ${x-r},${y} Q${x-2},${y-2} ${x},${y-r}Z" fill="#fff" stroke="${INK}" stroke-width="2" opacity="${(.5+.5*k).toFixed(2)}"/>`;});}
  $('fx').innerHTML=fx;
  [['lbR',600,500,0,4.4],['lbS',548,372,0,4.4],['lbP',gx+200,gy-150,4.6,8]].forEach(([id,x,y,a,b])=>{const on=T>=a&&T<b;show(id,on?1:0);if(on)$(id).setAttribute('transform',`translate(${x},${y}) scale(${(T<.02?1:Math.max(.01,eob(P(T,a-.01,a+.28)))).toFixed(3)})`);});
}
function renderWard(T){
  const dT=speak('doctor',T),pT=speak('patient',T),d0=ST['10_doctor'],hope=T>=lend('10_doctor')-5.2;
  tr('docHead',0,Math.sin(T*1.3)*1.2-(dT>.7?1.5:0),1,1,4+(dT>.15?Math.sin(T*6.5)*1.8*dT:0));
  $('dBrows').setAttribute('transform',`translate(0,${dT>.72?-3.5:0})`);
  setMouthV('doc_m',dT,10,hope?.6:.1,T,5);setHEye('dEyeL',4,blinkK(T,.7));setHEye('dEyeR',4,blinkK(T,.7));
  $('docArmR').setAttribute('transform',`rotate(${(dT>.2?-6+Math.sin(T*4.2)*7*dT:0).toFixed(2)},86,226)`);
  let pr=-6+Math.sin(T*.8)*1;if(pT>.2)pr+=Math.sin(T*7)*2;
  tr('patHead',0,Math.sin(T*1.5+1)*1.2+(T>=d0&&!hope?3:0),1,1,pr);
  $('pBrows').setAttribute('d','M-36,66 Q-24,64 -10,60 M8,60 Q22,64 34,66');
  setMouthV('pat_m',pT,10,hope?-.1:-.6,T,6);setHEye('pEyeL',-4,blinkK(T,2.1));setHEye('pEyeR',-4,blinkK(T,2.1));
  show('patBlush',.2);show('pSweat',0);
  const sh=[-84,234],el=[-108,356],wr=[-100,470];const d=limbD([sh,el,wr],[44,38,32]);$('patArmLD').setAttribute('d',d);$('patArmLO').setAttribute('d',d);
  $('patHandL').innerHTML=hand(wr[0],wr[1]+8,10,1.2,PSK);
}

function renderBoard(T){$('patWrap').setAttribute('transform',`translate(${(Math.sin(T*1.1)*2).toFixed(1)},${(Math.sin(T*2.2)*3).toFixed(1)})`);$('brd').setAttribute('transform',`translate(360,265) scale(${(1+Math.sin(T*2.4)*.006).toFixed(4)}) translate(-360,-265)`);[['b0',E.i0],['b1',E.i1],['b2',E.i2],['b3',E.i3]].forEach(([id,t0],i)=>{const on=T>=t0;show(id,on?1:0);if(on){const k=eob(P(T,t0,t0+.3)),y=169+i*86;$(id).setAttribute('transform',`translate(360,${y}) scale(${k.toFixed(3)}) translate(-360,${-y})`);}});}
function caption(T){let w='',ws=0;for(const L of D.lines)for(const x of L.words){if(T>=x[0]&&T<Math.max(x[1],x[0]+.12)){w=x[2];ws=x[0];}}
  if(!w){for(const L of D.lines)for(const x of L.words){if(T>=x[1]&&T<x[1]+.1){w=x[2];ws=x[0];}}}
  const c=$('cap');c.textContent=w;const sc=T<E.clinic,y0=sc?972:1150;c.setAttribute('y',y0+17);const k=eo(P(T,ws,ws+.12));c.setAttribute('transform',`translate(360,${y0}) scale(${lerp(1.4,1,k).toFixed(3)}) translate(-360,${-y0})`);}
window.render=function(T){
  const sc=T<E.clinic?1:3;$('s1').setAttribute('display',sc===1?'inline':'none');$('s3').setAttribute('display',sc===3?'inline':'none');
  if(sc===1)renderBody(T);else{renderWard(T);renderBoard(T);}caption(T);};
window.render(0);
