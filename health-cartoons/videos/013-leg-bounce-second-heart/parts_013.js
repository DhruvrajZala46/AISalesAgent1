// =============== 013 v2: "Why is bouncing your leg good for you?" One set, the leg, from the first frame to the last. ===============
const E=D.ev, ST=D.start, END=D.end, BI=E.B, PI=E.P;
//__VISEME__
const lend=id=>{const L=D.lines.find(l=>l.id===id);return L.t0+L.dur;};
const inL=(id,T,pre=.05,post=.1)=>T>=ST[id]-pre&&T<lend(id)+post;
const ss=(a,b,x)=>{const k=clamp((x-a)/(b-a));return k*k*(3-2*k);};
const win=(y,a,b)=>ss(a-70,a,y)*(1-ss(b,b+70,y));

// ---------- the scene ----------
let S1=`<g id="s1"><g id="cam">${legWorld()}</g>
 ${labelBox('lbValve','ONE-WAY VALVE',170,690,24)}${labelBox('lbCalf','CALF MUSCLE',500,236,25)}${labelBox('lb2nd','SECOND HEART',500,236,26)}${labelBox('lbVein','VEIN',360,150,26)}${heartIcon('hrt')}
 <g id="shout" opacity="0"><path d="${Array.from({length:24},(_,i)=>{const a=i/24*Math.PI*2,r=i%2?62:96;return (i?'L':'M')+(Math.cos(a)*r*1.25).toFixed(1)+','+(Math.sin(a)*r).toFixed(1);}).join(' ')}Z" fill="#fff" stroke="${INK}" stroke-width="4" stroke-linejoin="round"/>
  <text text-anchor="middle" y="24" style="font-family:LG,sans-serif;font-size:74px" fill="#ff7a55" stroke="${INK}" stroke-width="3">!!</text></g>
 <g transform="translate(0,252)">${studyCard()}</g>${docBubble()}</g>`;
const svg=$('S');
svg.innerHTML=`<defs><filter id="soft" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="7"/></filter>${DEFS}</defs>`
 +S1+`<text id="wm" x="360" y="64" text-anchor="middle" style="font-family:ComicNeue,sans-serif;font-weight:700;font-size:24px" fill="#fff" stroke="#0b6e6b" stroke-width=".6" opacity=".55">@GiggleMD</text>`
 +`<g id="capg"><text id="cap" class="cap" x="360" y="1015" text-anchor="middle" style="stroke-width:7px;font-size:48px"></text></g>`;

// ---------- the bounce: the heel taps the floor 4 times a second ----------
const bStart=T=>{for(const [a,b] of BI)if(T>=a&&T<b)return a;return null;};
function bounceB(T){const a=bStart(T);if(a===null)return 0;const ph=((T-a)%.25)/.25,amp=a<0?1:lerp(.55,1,P(T,a,a+1));return Math.pow(Math.sin(Math.PI*ph),.8)*amp;}
const ALLTAPS=[];BI.forEach(([a,b])=>{for(let t=Math.max(a,-6);t<b-.05;t+=.25)ALLTAPS.push(t);});
const pumping=T=>PI.some(([a,b])=>T>=a&&T<b);
const PTAPS=ALLTAPS.filter(pumping);
function dTap(T){let d=9;for(const t of PTAPS){if(t>T)break;d=T-t;}return d;}       // time since the calf's last squeeze
const sqz=T=>{if(!pumping(T))return 0;const d=dTap(T);return d<.17?Math.pow(Math.sin(Math.PI*d/.17),.6):0;};

// ---------- the blood cells: a small simulation, run once (they ride up on every squeeze and slide back when it stops) ----------
const N=30, LANES=[-38,0,38], FLOOR=885, restOff=l=>l===1?66:47;
const STOPS=[[-99,.7,45,170],[E.stop1,.7,45,170],[E.stop2,.1,300,340],[E.getUp,.3,80,170]];
const SIM=(()=>{const y=[],lane=[];for(let i=0;i<N;i++){lane.push(i%3);y.push(-340+((i*1260/N)+(i%3)*17+((i*7)%5)*6)%1260);}
  const fr=[];const dt=1/60;let step=0;
  for(let t=-6;t<END+.2;t+=dt,step++){
    if(pumping(t)){if(dTap(t)<.17)for(let i=0;i<N;i++){y[i]-=365*dt;if(y[i]<-340)y[i]+=1260;}}
    else{let s=STOPS[0];for(const q of STOPS)if(q[0]<=t)s=q;const v=clamp((t-s[0]-s[1])*s[2],0,s[3]);
      if(v>0)for(let l=0;l<3;l++){const idx=[];for(let i=0;i<N;i++)if(lane[i]===l)idx.push(i);idx.sort((a,b)=>y[b]-y[a]);let prev=1e9;
        for(const i of idx){let fl=FLOOR;for(const hv of [V_LO,V_UP])if(y[i]<hv-20)fl=Math.min(fl,hv-restOff(l));fl=Math.min(fl,prev-39);
          y[i]=Math.min(y[i]+v*dt,Math.max(y[i],fl));prev=y[i];}}}
    if(t>=-1e-6&&Math.round((t)*60)%2===0)fr.push(Float32Array.from(y));}
  return {fr,lane};})();
const F=T=>SIM.fr[clamp(Math.round(T*30),0,SIM.fr.length-1)];
// the two speaking cells: the top ones of the pile that the lower valve catches
const [HA,HB]=(()=>{const y=F(E.caught+.3);const mid=i=>y[i]<V_LO-20&&y[i]>V_UP;const top=l=>{let b=-1;for(let i=0;i<N;i++)if(SIM.lane[i]===l&&mid(i)&&(b<0||y[i]<y[b]))b=i;return b;};
  let a=top(1),b=top(2);if(a<0)a=0;if(b<0||b===a)b=top(0);if(b<0||b===a)b=(a+1)%N;return [a,b];})();
const cx=(i,y,T)=>VX(y)+LANES[SIM.lane[i]]+(pumping(T)?Math.sin(T*5+i*1.7)*2.5:0);

function setHero(id,x,y,{talk=0,T=0,dx=0,dy=0,mood=.2,worry=0,happy=0,seed=0,lid=.08,small=false,sx=1,sy=1,rot=0}={}){
  $(id).setAttribute('transform',`translate(${x.toFixed(1)},${y.toFixed(1)}) rotate(${rot.toFixed(1)}) scale(${sx.toFixed(3)},${sy.toFixed(3)})`);
  const bl=blinkK(T,seed*1.3+.2);setOEye(id+'_eL',8.3,{dx,dy,lid,blink:bl,small});setOEye(id+'_eR',8.3,{dx,dy,lid,blink:bl,small});
  setBrow(id+'_bL',-9.4,-16-worry*2,10,-worry*18+happy*6,2+happy*3);setBrow(id+'_bR',9.4,-16-worry*2,10,worry*18-happy*6,2+happy*3);
  setMouthV(id+'_m',talk,7.5,mood,T,seed);}

// ---------- vein, valves ----------
function leafD(hx,hy,tipx,tipy,side){const mx=(hx+tipx)/2;
  return `M${hx.toFixed(1)},${hy} Q${mx.toFixed(1)},${(hy-5).toFixed(1)} ${tipx.toFixed(1)},${tipy.toFixed(1)} Q${(mx-side*6).toFixed(1)},${((hy-34+tipy)/2-12).toFixed(1)} ${hx.toFixed(1)},${hy-36} Z`;}
function drawValve(idL,idR,hy,o,wHalf){const c=VX(hy),lx=c-wHalf,rx=c+wHalf;
  const tl=[lerp(c-1,lx+12,o),lerp(hy-58,hy-68,o)],tr2=[lerp(c+1,rx-12,o),lerp(hy-58,hy-68,o)];
  $(idL).setAttribute('d',leafD(lx,hy,tl[0],tl[1],1));$(idR).setAttribute('d',leafD(rx,hy,tr2[0],tr2[1],-1));}
function drawVein(sq,pk){const wf=y=>VW+10*pk*win(y,V_LO-190,V_LO-10)-8*sq*win(y,140,740);const L=[],R=[];
  for(let y=-460;y<=900;y+=40){const w=wf(y),c=VX(y);L.push([c-w,y]);R.push([c+w,y]);}
  const d=smooth(L)+' L'+smooth(R.slice().reverse()).slice(1)+'Z';['veinO','veinW','veinL','lumClipP'].forEach(id=>$(id).setAttribute('d',d));
  $('veinShine').setAttribute('d',smooth(L.map(([x,y])=>[x+15,y])));return wf;}

// ---------- the camera ----------
const WIDE=[1,360,640], TWO=[1.5,440,400], PILE=[2.0,395,480], CALF=[1.9,545,320];
const CAM=[[0,...WIDE,0],[E.stop1+.35,...TWO,.45],[E.caught,...PILE,.4],[E.twoA,...TWO,.4],[E.calfCam,...CALF,.4],[E.crowd,...PILE,.4],[E.bounce,...WIDE,.4],
  [ST['10_calf']-.1,...CALF,.35],[E.up-.12,1.3,420,480,.3],[E.up+.4,1.3,420,330,1.3],[E.flex,...CALF,.4],[E.ask,...WIDE,.45],[E.rp0,...TWO,.4],[E.stop2,2.0,395,470,.35],[E.bounce3,...WIDE,.4]];
function camAt(T){let s=CAM[0][1],x=CAM[0][2],y=CAM[0][3];for(let i=1;i<CAM.length;i++){const [t,ks,kx,ky,d]=CAM[i];if(T<t)break;const k=eio(P(T,t,t+d));s=lerp(s,ks,k);x=lerp(x,kx,k);y=lerp(y,ky,k);}return [s,x,y];}

const spk=(w,T)=>speak(w,T);
function renderLeg(T){
  const b=bounceB(T),pump=pumping(T),sq=sqz(T),y=F(T),yp=F(T-1/30);
  const still1=T>=E.stop1&&T<E.bounce, wait=T>=E.bounce&&T<E.up, crowd=T>=E.crowd&&T<E.bounce, still2=T>=E.stop2&&T<E.bounce3, gone=T>=E.getUp;
  // the outside: the leg rides up as the heel lifts, the sneaker turns about its toes, the couch shakes
  const wk=Math.max(0,T-E.walk),wx=-(wk*wk*520+wk*260),hop=wk>0?Math.abs(Math.sin(wk*Math.PI/.34))*46:0;
  $('walkG').setAttribute('transform',`translate(${wx.toFixed(1)},${(-hop).toFixed(1)})`);
  $('legG').setAttribute('transform',`translate(0,${(-30*b).toFixed(2)})`);
  $('shoeG').setAttribute('transform',`rotate(${(-6*b).toFixed(3)},110,1112)`);
  $('couch').setAttribute('transform',`translate(${(b*3).toFixed(2)},${(-b*2).toFixed(2)})`);
  $('shadow').setAttribute('opacity',(.16-.06*b).toFixed(3));
  let im='';const ba=bStart(T);if(ba!==null){const ph=(T-ba)%.25,o=ph<.12?(1-ph/.12):0,fl=Math.floor((T-ba)/.125)%2;
    if(o>0)im+=`<path d="M556,1128 q14,10 30,2 M572,1146 q10,7 24,1" fill="none" stroke="${INK}" stroke-width="3.6" stroke-linecap="round" opacity="${o.toFixed(2)}"/>`;
    const zz=(x,y,r)=>`<path transform="translate(${x},${y}) rotate(${r})" d="M0,0 l10,-12 l10,12 l10,-12 l10,12 l10,-12" fill="none" stroke="#ffc928" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><path transform="translate(${x},${y}) rotate(${r})" d="M0,0 l10,-12 l10,12 l10,-12 l10,12 l10,-12" fill="none" stroke="${INK}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" opacity=".5"/>`;
    im+=zz(596,fl?950:940,-62)+zz(624,fl?1012:1022,-74)+zz(206,fl?886:894,-128);}
  $('impact').innerHTML=im;
  // the vein and the calf's squeeze
  const pk=crowd?.5+.5*P(T,E.crowd,E.crowd+.5):((still1||still2)?.5*P(T,(still1?E.stop1:E.stop2)+.8,(still1?E.stop1:E.stop2)+2):0);
  const wf=drawVein(sq,pk);
  $('calfG').setAttribute('transform',`translate(640,300) scale(${(1+.075*sq).toFixed(4)},${(1-.014*sq).toFixed(4)}) translate(-640,-300)`);
  $('sqz').innerHTML=sq>.15?[250,330,430,520].map((yy,j)=>`<path d="M${452-j%2*4},${yy} l-16,-7 M${452-j%2*4},${yy+16} l-17,0 M${452-j%2*4},${yy+32} l-16,7" stroke="#fff" stroke-width="4" stroke-linecap="round" opacity="${(sq*.9).toFixed(2)}"/>`).join(''):'';
  const o=pump?(dTap(T)<.17?1:clamp(1-(dTap(T)-.17)/.06)):0;
  drawValve('gvL','gvR',V_LO,o,wf(V_LO));drawValve('uvL','uvR',V_UP,o,wf(V_UP));
  // the cells
  let h='';const lookA=[VX(480),480];
  for(let i=0;i<N;i++){if(i===HA||i===HB)continue;const yy=y[i],fall=yy-yp[i]>.6,rest=!pump&&!fall;
    const mood=pump?1:(fall?-1:(crowd&&yy<V_LO&&yy>V_UP?-2:(wait?0:(rest&&(still1||still2)?(i%3?0:-2):0))));
    const lx=pump?0:(fall?0:(wait?0:(i%2?.6:-.6))),ly=pump?-1:(fall?1:(wait?1:-.4));
    const jig=wait?Math.sin(T*50+i)*1.5*b:0;
    h+=smallCell(cx(i,yy,T)+jig,yy-(rest?b*4:0),20,(rnd(i)-.5)*14+(pump?Math.sin(T*6+i)*5:0),mood,lx,ly,blinkK(T,i*.53)>.5);}
  $('cellsG').innerHTML=h;
  // the two speaking cells
  const aT=spk('cell',T),bT=spk('cell2',T),ya=y[HA],yb=y[HB],fa=ya-yp[HA]>.6,fb=yb-yp[HB]>.6;
  const sq08=inL('08_cell',T)?1:0;
  setHero('hA',cx(HA,ya,T),ya-(still1&&!fa?b*4:0)-(aT>.3?aT*4:0),{talk:aT,T,seed:1,
    dx:pump?0:(inL('06_cell',T)?24:(inL('03_cell',T)?0:(wait?0:-14))),dy:pump?-24:(fa?26:(inL('06_cell',T)?-24:(wait?26:(crowd?4:-10)))),
    mood:pump?.9:(fa||crowd?-.7:(still1?-.4:.2)),worry:pump?0:(still1||wait?1:.3),happy:pump?1:0,small:fa||(wait&&T<ST['10_calf']),
    sx:crowd?1.1:1,sy:crowd?.9:1,rot:fa?Math.sin(T*24)*8:0});
  setHero('hB',cx(HB,yb,T),yb-(still1&&!fb?b*4:0)-(bT>.3?bT*4:0),{talk:bT,T,seed:2,
    dx:pump?0:(wait?0:(inL('06_cell',T)||inL('07_calf',T)?22:-18)),dy:pump?-24:(fb?26:(wait?28:(inL('07_calf',T)?-22:0))),
    mood:pump?1:(fb?-.7:(crowd?-.6:-.2)),worry:pump?0:(still1||wait?.9:.3),happy:pump?1:0,small:fb,sx:crowd?1.08:1,sy:crowd?.92:1,rot:fb?Math.sin(T*22+1)*8:0});
  let sw='';if(crowd){[[ya-34,-30,0],[yb-30,34,1],[ya+30,-44,2]].forEach(([yy,ox,j])=>{const f=((T*1.6+j*.37)%1),x=VX(yy)+ox,yv=yy+f*26;
      sw+=`<path transform="translate(${x.toFixed(1)},${yv.toFixed(1)}) scale(1.25)" d="M0,-9 C5,-2 7,3 5,7 C3,11 -4,11 -5,7 C-7,3 -4,-2 0,-9Z" fill="#bfe9ff" stroke="${INK}" stroke-width="1.8" opacity="${(1-f).toFixed(2)}"/>`;});}
  $('sweat').innerHTML=sw;
  // the valve guard
  const gT=spk('gate',T),gBusy=T>=E.caught-.2&&T<E.bounce;
  const gdx=gBusy?26:18,gdy=pump?-20:(gBusy?-16:(still2?-18:4));
  setOEye('gd_eL',10.5,{dx:gdx,dy:gdy,lid:pump?.15:.42,blink:blinkK(T,2.2)});setOEye('gd_eR',10.5,{dx:gdx,dy:gdy,lid:pump?.15:.42,blink:blinkK(T,2.2)});
  setBrow('gd_bL',-11,-17,13,gBusy?10:2,1.5);setBrow('gd_bR',11,-17,13,gBusy?-10:-2,1.5);
  setMouthV('gd_m',gT,6,gBusy?-.4:(pump?.5:0),T,3);
  $('gd_cap').setAttribute('transform',`translate(0,${(-sq*3-(gT>.5?2:0)).toFixed(1)}) rotate(${gBusy?-6:0})`);
  // the calf
  const cT=spk('calf',T),smug=T>=E.flex-.05&&T<E.ask,excited=T>=ST['10_calf']-.1&&T<E.up,surprised=wait&&!excited,lazy=still1,calm=still2;
  let cdx=-22,cdy=20,clid=.05,mood=.75,bA=10,bArch=7,small=false;                                   // working: focused and happy
  if(T<E.stop1&&inL('01_partner',T,0,0)){cdx=18;cdy=-26;clid=0;mood=.2;bA=-6;}                    // he hears the shout
  if(lazy){cdx=-26;cdy=18;clid=.46;mood=-.2;bA=3;bArch=3;}
  if(lazy&&inL('06_cell',T)){cdx=-30;cdy=24;clid=.38;}
  if(crowd){cdx=-32;cdy=26;clid=.3;mood=-.35;}
  if(surprised){cdx=Math.sin(T*5)*22;cdy=30;clid=0;mood=-.1;small=true;bA=-8;bArch=9;}
  if(excited){cdx=-14;cdy=16;clid=0;mood=.9;bA=-10;bArch=10;}
  if(smug){cdx=-4;cdy=2;clid=.4;mood=.95;bA=-4;bArch=8;}
  if(calm){cdx=-28;cdy=22;clid=.3;mood=.1;bA=2;bArch=4;}
  if(gone){cdx=-10;cdy=-10;clid=0;mood=.9;bA=-8;bArch=9;}
  const cbl=blinkK(T,.6);
  setOEye('cEyeL',33,{dx:cdx,dy:cdy,lid:clid,blink:cbl,small});setOEye('cEyeR',33,{dx:cdx,dy:cdy,lid:clid,blink:cbl,small});
  const by=246-(clid<.1?8:0);
  setBrow('cBrL',521,by,38,bA,bArch);setBrow('cBrR',593,by-(smug?10:0),38,-bA-(smug?8:0),bArch+(smug?3:0));
  setMouthV('calf_m',cT,20,mood,T,4);
  $('calfFace').setAttribute('transform',`translate(${(-sq*6).toFixed(1)},${(Math.sin(T*1.4)*1.5-cT*2).toFixed(2)})`);
  let sp='';if(smug){[[486,236,0],[634,262,1],[628,372,2],[490,392,3],[556,150,4]].forEach(([x,yy,j])=>{const k=.5+.5*Math.sin(T*7+j*1.9),r=8+10*k;
      sp+=`<path d="M${x},${yy-r} Q${x+2},${yy-2} ${x+r},${yy} Q${x+2},${yy+2} ${x},${yy+r} Q${x-2},${yy+2} ${x-r},${yy} Q${x-2},${yy-2} ${x},${yy-r}Z" fill="#fff" stroke="${INK}" stroke-width="2" opacity="${(.5+.5*k).toFixed(2)}"/>`;});}
  $('sparks').innerHTML=sp;
  // camera
  const [s,ccx,ccy]=camAt(T);$('cam').setAttribute('transform',`translate(360,640) scale(${s.toFixed(4)}) translate(${(-ccx).toFixed(2)},${(-ccy).toFixed(2)})`);
  // labels, the shout, the heart
  popLabel('lbValve',T,E.caught+.55,E.twoA-.05,170,770);if(T>=E.stop2)popLabel('lbValve',T,E.stop2+.45,E.bounce3-.05,170,790);
  popLabel('lbCalf',T,E.calfCam+.55,E.crowd-.05,500,236);popLabel('lb2nd',T,E.second,E.ask-.1,500,236);
  popLabel('lbVein',T,E.stop1+1.0,E.caught-.1,330,120);
  const shOn=T<E.stop1+.1;show('shout',shOn?1:0);
  if(shOn){const k=T<.01?1:1+.06*Math.sin(T*16);$('shout').setAttribute('transform',`translate(${118+Math.sin(T*38)*3},${330+Math.cos(T*31)*3}) rotate(${-8+Math.sin(T*9)*3}) scale(${(k*.8).toFixed(3)})`);}
  const hOn=T>=E.rpHeart&&T<E.stop2;show('hrt',hOn?1:0);
  if(hOn){const kk=eob(P(T,E.rpHeart,E.rpHeart+.25)),beat=1+.13*Math.pow(Math.abs(Math.sin((T-E.rpHeart)*Math.PI/.5)),6);$('hrt').setAttribute('transform',`translate(322,104) scale(${(kk*beat).toFixed(3)})`);}
}
// ---------- Dr. Mira's bubble and the study card ----------
function renderDoc(T){
  const on=T>=E.doc;show('docB',on?1:0);if(!on)return;
  const k=eob(P(T,E.doc,E.doc+.3));$('docB').setAttribute('transform',`translate(122,196) scale(${k.toFixed(3)})`);
  const dT=speak('doctor',T);
  tr('docHead',0,Math.sin(T*1.3)*1.2-(dT>.7?1.5:0),1,1,2+(dT>.15?Math.sin(T*6.5)*1.8*dT:0));
  $('dBrows').setAttribute('transform',`translate(0,${dT>.72?-3.5:0})`);
  setMouthV('doc_m',dT,10,.5,T,5);setHEye('dEyeL',3,blinkK(T,.7));setHEye('dEyeR',3,blinkK(T,.7));
  $('docArmR').setAttribute('transform',`rotate(0,86,226)`);
}
function renderCard(T){
  const cOn=T>=E.card0&&T<E.card1+.16;show('card',cOn?1:0);if(!cOn)return;
  const k=eob(P(T,E.card0,E.card0+.3))*(1-P(T,E.card1,E.card1+.16));$('card').setAttribute('transform',`translate(360,300) scale(${Math.max(.001,k).toFixed(3)}) translate(-360,-300)`);
  const ph=((T-E.card0)%.25)/.25,fb=Math.pow(Math.sin(Math.PI*ph),.8);
  $('mlF_leg').setAttribute('transform',`translate(0,${(-24*fb).toFixed(2)})`);$('mlF_shoe').setAttribute('transform',`rotate(${(-4.8*fb).toFixed(3)},110,1112)`);
  $('mlF_imp').innerHTML=ph<.45?`<path d="M560,1124 q14,10 32,2 M578,1146 q11,8 26,1 M556,1090 q16,-4 30,-16" fill="none" stroke="${INK}" stroke-width="7" stroke-linecap="round" opacity="${(1-ph/.45).toFixed(2)}"/>`:'';
  const a1=T>=E.arrDown,a2=T>=E.arrUp;show('arrD',a1?1:0);show('arrU',a2?1:0);show('tD',a1?1:0);show('tU',a2?1:0);
  if(a1){const k1=eob(P(T,E.arrDown,E.arrDown+.28));$('arrD').setAttribute('transform',`translate(296,${(272+Math.abs(Math.sin((T-E.arrDown)*3.2))*12).toFixed(1)}) scale(${k1.toFixed(3)})`);}
  if(a2){const k2=eob(P(T,E.arrUp,E.arrUp+.28));$('arrU').setAttribute('transform',`translate(584,${(284-Math.abs(Math.sin((T-E.arrUp)*3.2))*12).toFixed(1)}) scale(${k2.toFixed(3)})`);}}
function caption(T){let w='',ws=0;for(const L of D.lines)for(const x of L.words){if(T>=x[0]&&T<Math.max(x[1],x[0]+.12)){w=x[2];ws=x[0];}}
  if(!w){for(const L of D.lines)for(const x of L.words){if(T>=x[1]&&T<x[1]+.1){w=x[2];ws=x[0];}}}
  const c=$('cap');c.textContent=w;const k=eo(P(T,ws,ws+.12));c.setAttribute('transform',`translate(360,998) scale(${lerp(1.4,1,k).toFixed(3)}) translate(-360,-998)`);}
window.render=function(T){renderLeg(T);renderDoc(T);renderCard(T);caption(T);};
window.render(0);
