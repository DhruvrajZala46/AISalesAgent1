// =============== 016: "This habit left him with one lung". One locked chest scene, then the hospital room. ===============
const E=D.ev, ST=D.start, END=D.end;
//__VISEME__
const lend=id=>{const L=D.lines.find(l=>l.id===id);return L.t0+L.dur;};
const inL=(id,T,pre=.05,post=.1)=>T>=ST[id]-pre&&T<lend(id)+post;
const svg=$('S');
const S1=`<g id="s1">${chestWorld()}${labelBox('lbH','HEALTHY LUNG',170,206,26)}${labelBox('lbS',"SMOKER'S LUNG",548,206,26)}</g>`, S3=`<g id="s3">${ward()}</g>`;
svg.innerHTML=`<defs><filter id="soft" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="7"/></filter>${DEFS}</defs>`
 +S1+S3+`<text id="wm" x="360" y="50" text-anchor="middle" style="font-family:ComicNeue,sans-serif;font-weight:700;font-size:24px" fill="#fff" stroke="#0b6e6b" stroke-width=".6" opacity=".6">@GiggleMD</text>`
 +`<g id="capg"><text id="cap" class="cap" x="360" y="1085" text-anchor="middle" style="stroke-width:7px;font-size:48px"></text></g>`;
function face(id,r,{dx=0,dy=0,lid=.1,blink=0,small=false,bx=27,by=48,bw=26,bA=0,arch=3,talk=0,mw=12,mood=0,T=0,seed=0}){
  setOEye(id+'_eL',r,{dx,dy,lid,blink,small});setOEye(id+'_eR',r,{dx,dy,lid,blink,small});
  setBrow(id+'_bL',-bx,by,bw,bA,arch);setBrow(id+'_bR',bx,by,bw,-bA,arch);setMouthV(id+'_m',talk,mw,mood,T,seed);}
const drop=(x,y,o)=>`<path transform="translate(${x.toFixed(1)},${y.toFixed(1)}) scale(1.6)" d="M0,-9 C5,-2 7,3 5,7 C3,11 -4,11 -5,7 C-7,3 -4,-2 0,-9Z" fill="#bfe9ff" stroke="${INK}" stroke-width="1.8" opacity="${o.toFixed(2)}"/>`;
const mv=(id,x,y,r=0,s=1)=>$(id).setAttribute('transform',`translate(${x.toFixed(1)},${y.toFixed(1)}) rotate(${r.toFixed(1)}) scale(${s})`);
// where each cut piece of the dark lung goes: [lift start, centre of the piece, its spot on the tray, turn]
const PIECES=[['dp1m',E.cut+3.2,[530,370],[280,988],78],['dp2m',E.cut+4.4,[545,560],[360,980],-84],['dp3m',E.cut+5.6,[545,740],[440,992],100]];
function renderChest(T){
  const breath=Math.sin(T*1.9),asleep=T>=E.inj+.45,cutting=T>=E.cut,gone=T>=E.done;
  // ---- the dark (smoker's) lung ----
  const dT=speak('dark',T),hasPack=T<E.give+.5;
  $('darkG').setAttribute('transform',cutting?'':`translate(540,540) scale(${(1+breath*.008).toFixed(4)},${(1+breath*.012).toFixed(4)}) translate(-540,-540)`);
  show('darkFace',(cutting||asleep)?0:1);show('dSleep',asleep?1:0);
  let df={dx:-26,dy:4,lid:.25,bA:-6,arch:8,mood:.8,small:false};                                        // smug
  if(T>=E.scope)df={dx:20,dy:26,lid:.05,bA:-12,arch:6,mood:-.3,small:false};
  if(T>=E.scal)df={dx:24,dy:20,lid:0,bA:-16,arch:5,mood:-.6,small:true};
  if(T>=E.syr)df={dx:30,dy:14,lid:0,bA:-18,arch:6,mood:-.9,small:true};
  const dz=P(T,E.inj,E.inj+.45);
  face('dk',38,{...df,lid:asleep?1:lerp(df.lid,.95,dz),blink:asleep?1:blinkK(T,1.3),bx:40,by:-56,bw:36,talk:dT,mw:18,T,seed:4});
  // its hand: the cigarette, and handing over the pack
  const puffK=T<E.give?.5+.5*Math.sin(T*2.2):0,g=eio(P(T,E.give,E.give+.5)),gb=eio(P(T,E.give+.7,E.give+1.1));
  const hx=lerp(lerp(450,430,puffK),388,g*(1-gb)),hy=lerp(lerp(560,528,puffK),600,g*(1-gb));
  $('dkArm').setAttribute('d',`M430,590 Q${(hx-22).toFixed(1)},${(hy+34).toFixed(1)} ${hx.toFixed(1)},${hy.toFixed(1)}`);
  mv('dkCig',lerp(hx-22,hx-8,g),lerp(hy-6,hy+30,g),lerp(170,120,g),1.3);show('dkHand',T<E.scal+.2&&!cutting?1:0);show('dkCig',T<E.scope+.3?1:0);
  const px=lerp(452,300,g),py=lerp(640,610,g)-Math.sin(g*Math.PI)*40;mv('dkPack',px,py,lerp(-8,6,g),1.35);show('dkPack',T<E.give+.5&&T>=E.give-1.2?1:0);
  // smoke from the cigarette
  let sm='';if(T<E.scope+.3){for(let j=0;j<4;j++){const p=((T*.6+j/4)%1),x=lerp(hx-46,hx-70,g)+Math.sin(p*6+j)*14,y=lerp(hy-10,hy+22,g)-p*150;sm+=`<circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="${(10+p*20).toFixed(1)}" fill="#e9e3e0" opacity="${((1-p)*.6).toFixed(2)}"/>`;}}
  // ---- the pink (healthy) lung ----
  const pT=speak('pink',T),hide=eio(P(T,E.sus+.45,E.sus+.8)),shock=T>=E.cut-.2&&T<E.sus,nerv=T>=E.sus;
  $('pinkB').setAttribute('transform',`translate(170,560) scale(${(1+breath*.01).toFixed(4)},${(1+breath*.014+(pT>.4?.004:0)).toFixed(4)}) translate(-170,-560) translate(${(shock?Math.sin(T*40)*2.2:0).toFixed(1)},0)`);
  let pf={dx:26,dy:2,lid:.08,bA:-6,arch:7,mood:.3,small:false};
  if(inL('02_pink',T))pf={dx:26,dy:0,lid:.05,bA:-8,arch:9,mood:.8,small:false};
  if(T>=E.give)pf={dx:18,dy:26,lid:.1,bA:-4,arch:8,mood:.7,small:false};
  if(T>=E.scope)pf={dx:30,dy:20,lid:.05,bA:-10,arch:6,mood:-.1,small:false};
  if(T>=E.syr)pf={dx:30,dy:8,lid:0,bA:-14,arch:6,mood:-.5,small:true};
  if(shock)pf={dx:28,dy:cutting&&T>E.cut+2.6?30:10,lid:0,bA:-18,arch:6,mood:-.9,small:true};
  if(nerv)pf={dx:inL('09_pink',T)?Math.sin(T*7)*18:22,dy:6,lid:.05,bA:-12,arch:8,mood:inL('09_pink',T)?.4:-.4,small:!inL('09_pink',T)};
  face('pk',40,{...pf,blink:blinkK(T,.5),bx:42,by:-58,bw:38,talk:pT,mw:19,T,seed:1});
  const got=T>=E.give+.5,tk=eio(P(T,E.take,E.take+.5));
  show('pkHand',got&&hide<1?1-hide:0);
  if(got){const hx2=lerp(300,246,hide),hy2=612+Math.sin(T*2.2)*2;$('pkArm').setAttribute('d',`M318,650 Q${(hx2+26).toFixed(1)},${(hy2+40).toFixed(1)} ${hx2.toFixed(1)},${hy2.toFixed(1)}`);mv('pkPack',hx2,hy2,6,1.35);
    show('pkCig',tk>0?1:0);mv('pkCig',hx2+lerp(0,40,tk),hy2-lerp(46,96,tk),lerp(90,150,tk),1.3);}
  let sw='';if(shock||nerv){[[70,360,0],[300,330,1]].forEach(([x,y,j])=>{const p=((T*1.4+j*.5)%1);sw+=drop(x,y+p*50,1-p);});}$('pkSweat').innerHTML=sw;
  $('smoke').innerHTML=sm;
  // ---- the camera tool ----
  const sIn=eo(P(T,E.scope,E.scope+.9)),sOut=eio(P(T,E.scal-.1,E.scal+.5)),scOn=T>=E.scope&&sOut<1;show('scope',scOn?1:0);
  const sx=lerp(900,470,sIn)+sOut*420,sy=lerp(1250,700,sIn)+sOut*520+Math.sin(T*3)*4;mv('scope',sx,sy,0,1.3);
  const scan=T>=E.scope+1.0&&T<E.scope+2.25;show('cone',scan?.9:0);if(scan)mv('cone',sx-20,sy-28,Math.sin((T-E.scope)*5)*7);
  const scT=speak('scope',T);show('scFace',T>=E.scope+2.2?1:0);
  setOEye('sc_eL',16,{dx:22,dy:-18,lid:0,blink:blinkK(T,.3),small:true});setOEye('sc_eR',16,{dx:22,dy:-18,lid:0,blink:blinkK(T,.3),small:true});setMouthV('sc_m',scT,9,-.6,T,8);
  // ---- the scalpel: arrives, cuts three times, later turns on the pink lung ----
  const cutK=j=>eio(P(T,E.cut+j*.85,E.cut+.55+j*.85));
  let kx=1000,ky=300,kr=0,kOn=false;const slT=speak('scalpel',T);
  if(T>=E.scal&&T<E.cut){const k=eo(P(T,E.scal,E.scal+.6));const o=eio(P(T,E.syr-.1,E.syr+.35));kx=lerp(900,470,k)+o*520;ky=lerp(1100,900,k)-slT*8+o*200;kr=-10;kOn=o<1;}
  if(cutting&&T<E.cut+2.7){const j=Math.min(2,Math.floor((T-E.cut)/.85)),k=cutK(j),yy=[470,640,770][j];kx=lerp(740,392,k);ky=lerp(yy-22,yy+14,k);kr=14;kOn=true;}
  if(T>=E.cut+2.7&&T<E.sus){const k=eio(P(T,E.cut+2.7,E.cut+3.1));kx=lerp(392,940,k);ky=lerp(780,700,k);kr=14;kOn=k<1;}
  if(T>=E.sus){const k=eo(P(T,E.sus,E.sus+.5));kx=lerp(900,400,k);ky=lerp(1100,860,k)-slT*8;kr=-4;kOn=true;}
  show('scalpel',kOn?1:0);mv('scalpel',kx,ky,kr,1.35);
  const look=T>=E.sus?[-28,-16]:[10,-26];setOEye('sl_eL',14,{dx:look[0],dy:look[1],lid:T>=E.sus?.3:.05,blink:blinkK(T,2.7)});setOEye('sl_eR',14,{dx:look[0],dy:look[1],lid:T>=E.sus?.3:.05,blink:blinkK(T,2.7)});
  let cu='';[[398,486,640,460],[400,650,684,632],[452,786,660,764]].forEach(([x1,y1,x2,y2],j)=>{const k=cutK(j);if(k>0&&T<PIECES[Math.min(j,2)][1]+ (j===2?0:0)+9)cu+=`<path d="M${x2},${y2} L${lerp(x2,x1,k).toFixed(1)},${lerp(y2,y1,k).toFixed(1)}" stroke="#ff8f86" stroke-width="5" stroke-linecap="round"/>`;});
  $('cuts').innerHTML=T<E.cut+3.2?cu:'';
  // ---- the syringe ----
  const yIn=eo(P(T,E.syr,E.syr+.5)),jab=eio(P(T,E.inj-.15,E.inj)),yOut=eio(P(T,E.inj+.45,E.inj+.9));show('syringe',T>=E.syr&&yOut<1?1:0);
  mv('syringe',lerp(900,lerp(548,520,jab),yIn)+yOut*320,lerp(420,lerp(700,726,jab),yIn)-yOut*380,0,1.2);
  $('plunger').setAttribute('transform',`translate(0,${(P(T,E.inj,E.inj+.4)*60).toFixed(1)})`);
  // ---- the tray, and the three pieces lifted onto it ----
  const tIn=eo(P(T,E.cut+2.6,E.cut+3.1)),tOut=eio(P(T,E.done-.45,E.done));show('tray',T>=E.cut+2.6&&tOut<1?1:0);
  const ty=lerp(1420,1010,tIn)+tOut*420;mv('tray',360,ty,0,1.22);
  let fOn=false,fxp=0,fyp=0;
  PIECES.forEach(([id,t0,c,to,rot],i)=>{const k=eio(P(T,t0,t0+.95)),x=lerp(0,to[0]-c[0],k),y=lerp(0,to[1]-c[1],k)-Math.sin(k*Math.PI)*70+(k>=1?ty-1010:0);
    $(id).setAttribute('transform',`translate(${x.toFixed(1)},${y.toFixed(1)}) rotate(${(rot*k).toFixed(1)},${c[0]},${c[1]}) translate(${c[0]},${c[1]}) scale(${lerp(1,.78,k).toFixed(3)}) translate(${-c[0]},${-c[1]})`);
    $(id.slice(0,3)).setAttribute('clip-path',k>0?'':`url(#pc${i+1})`);
    if(k>0)$(id).setAttribute('clip-path',`url(#pc${i+1})`);
    if(T>=t0-.35&&T<t0+1.2){fOn=true;const a=eo(P(T,t0-.35,t0)),b=eio(P(T,t0+.95,t0+1.2));fxp=c[0]+x+40+(1-a)*260+b*260;fyp=c[1]+y-30-(1-a)*300-b*300;}
    show(id,gone?0:1);});
  show('forceps',fOn?1:0);mv('forceps',fxp,fyp,0,1.25);
  ['lbH','lbS'].forEach((id,i)=>{const on=T<4.2;show(id,on?1:0);if(on)$(id).setAttribute('transform',`translate(${i?548:170},206) scale(${(T<.02?1:Math.max(1,eob(P(T,-.3,.02)))).toFixed(3)})`);});
}
function renderWard(T){
  const dT=speak('doctor',T),pT=speak('patient',T),d0=ST['11_doctor'],hope=T>=lend('11_doctor')-5.2;
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
function caption(T){let w='',ws=0;for(const L of D.lines)for(const x of L.words){if(T>=x[0]&&T<Math.max(x[1],x[0]+.12)){w=x[2];ws=x[0];}}
  if(!w){for(const L of D.lines)for(const x of L.words){if(T>=x[1]&&T<x[1]+.1){w=x[2];ws=x[0];}}}
  const c=$('cap');c.textContent=w;const k=eo(P(T,ws,ws+.12));c.setAttribute('transform',`translate(360,1068) scale(${lerp(1.4,1,k).toFixed(3)}) translate(-360,-1068)`);}
window.render=function(T){
  const sc=T<E.clinic?1:3;$('s1').setAttribute('display',sc===1?'inline':'none');$('s3').setAttribute('display',sc===3?'inline':'none');
  if(sc===1)renderChest(T);else renderWard(T);caption(T);};
window.render(0);
