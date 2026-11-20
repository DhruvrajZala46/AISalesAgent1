// =============== timing / animation (003) ===============
const E=D.ev, ST=D.start, END=D.end;
const T_CLINIC=E.clinic, T_STING=E.stinger;
const KEY=/^(NOSE|DOWN|DOOR|SHUT|PUBLIC|JOKE|NOODLES|LAUGHING|DROP|HAIRY|DAYLIGHT|NASAL|REGURGITATION|PALATE|SEALS|BREATHE|HARMLESS|CHECKED|LAUGH|THEN|FOLLOW|BRAIN|UP)$/;
//__VISEME__
// ---------- geometry helpers ----------
function crSample(P,n=10){const out=[];for(let i=0;i<P.length-1;i++){const p0=P[Math.max(0,i-1)],p1=P[i],p2=P[i+1],p3=P[Math.min(P.length-1,i+2)];
  for(let k=0;k<n;k++){const t=k/n,t2=t*t,t3=t2*t;out.push([0,1].map(j=>.5*((2*p1[j])+(-p0[j]+p2[j])*t+(2*p0[j]-5*p1[j]+4*p2[j]-p3[j])*t2+(-p0[j]+3*p1[j]-3*p2[j]+p3[j])*t3)));}}
  out.push(P[P.length-1]);return out;}
function arcTab(pts){const s=[0];for(let i=1;i<pts.length;i++)s.push(s[i-1]+Math.hypot(pts[i][0]-pts[i-1][0],pts[i][1]-pts[i-1][1]));return s;}
function atS(pts,S,s){s=clamp(s,0,S[S.length-1]);let lo=0,hi=S.length-1;while(hi-lo>1){const m=(lo+hi)>>1;if(S[m]<=s)lo=m;else hi=m;}
  const k=(s-S[lo])/((S[hi]-S[lo])||1);return [lerp(pts[lo][0],pts[hi][0],k),lerp(pts[lo][1],pts[hi][1],k)];}
const BODY_R=[[-900,606],[-300,604],[-60,603],[40,602],[82,601],[160,592],[260,588],[360,594],[440,616],[500,606],[540,580],[556,540]];
const LAUNCH_R=[[570,480],[578,430],[566,384],[530,352],[450,344],[340,350],[240,362],[160,386],[112,414],[84,446],[62,474],[46,500],[34,530],[28,570],[30,612]];
const TR=crSample(BODY_R.concat(LAUNCH_R),14), TS=arcTab(TR);
function sNear(x,y){let b=0,bd=1e9;TR.forEach((p,i)=>{const d=Math.hypot(p[0]-x,p[1]-y);if(d<bd){bd=d;b=i;}});return TS[b];}
const S_LIPS=sNear(70,601), S_IDLE=sNear(556,540), S_HAIR=sNear(112,414), S_VEST=sNear(80,450), S_OUT=sNear(34,530), S_HANG=sNear(29,590);
const NL=1500;
function rot(x,y,a){const c=Math.cos(a),s=Math.sin(a);return [x*c-y*s,x*s+y*c];}
function hose(a,b,bend){const mx=(a[0]+b[0])/2,my=(a[1]+b[1])/2,dx=b[0]-a[0],dy=b[1]-a[1],L=Math.hypot(dx,dy)||1;
  return `M${a[0].toFixed(1)},${a[1].toFixed(1)} Q${(mx-dy/L*bend).toFixed(1)},${(my+dx/L*bend).toFixed(1)} ${b[0].toFixed(1)},${b[1].toFixed(1)}`;}
function mitt(x,y,r=10,ang=0){return `<g transform="translate(${x.toFixed(1)},${y.toFixed(1)}) rotate(${ang.toFixed(1)})"><circle r="${r}" fill="#fff" ${LN2}/><circle cx="${-r*.8}" cy="${-r*.5}" r="${r*.45}" fill="#fff" ${LN2}/></g>`;}
function key(T,ks){if(T<=ks[0][0])return ks[0][1];for(let i=1;i<ks.length;i++){if(T<ks[i][0]){const k=eio(P(T,ks[i-1][0],ks[i][0]));const a=ks[i-1][1],b=ks[i][1];return Array.isArray(a)?a.map((v,j)=>lerp(v,b[j],k)):lerp(a,b,k);}}return ks[ks.length-1][1];}
const w03=ST['03_noodle'], wUp2=wordT('02_palate','UP'), L09=ST['09_palate'], L13=ST['13_noodle'];
// ---------- world state at time T (also used for the clinic thought-bubble replays) ----------
function worldState(T){
  const s={};
  // soft palate angle (deg): closed (sealing the nose) = -14, dropped (breathing) = +52
  let th=-14+Math.sin(T*1.7)*.8;
  const dip=P(T,E.noway,E.noway+.45); if(dip>0&&dip<1) th+=Math.sin(dip*Math.PI)*9;
  const sq=P(T,E.shut-.1,E.shut+1.0); if(sq>0&&sq<1) th-=Math.sin(sq*Math.PI)*3;
  if(T>=L09&&T<E.drop) th+=Math.sin(T*31)*(T>=E.laugh?2.8:1.2);
  const dr=P(T,E.drop,E.drop+.35), dr2=P(T,E.cant,E.cant+.4);
  th=lerp(th,34,eob(dr)); th=lerp(th,52,eio(dr2));
  if(T>=E.drop) th+=Math.sin(T*9)*2*(1-P(T,E.innose,E.innose+2));
  th=lerp(th,40,eio(P(T,E.blame-.2,E.blame+.3)));
  s.th=th;
  // noodle head arc position + head offset
  let sh;
  if(T<E.launch){sh=lerp(S_LIPS-30,S_IDLE,eo(P(T,.12,.95)));}
  else if(T<E.popout){const a=P(T,E.launch,E.innose+.2);sh=lerp(S_IDLE,S_HAIR,eio(a));sh=lerp(sh,S_VEST,eio(P(T,E.innose+.3,E.popout-.1)));}
  else {sh=lerp(S_VEST,S_OUT,eo(P(T,E.popout,E.popout+.18)));sh=lerp(sh,S_HANG,eob(P(T,E.popout+.18,E.popout+.6)));}
  s.sh=sh;
  let off=[0,Math.sin(T*2.3)*4];
  if(T<E.launch){
    const pk=key(T,[[w03,[0,0]],[w03+.5,[4,-30]],[E.peek+.2,[10,-60]],[E.noway,[10,-60]],[E.noway+.15,[-4,30]],[E.noway+.7,[0,8]],[E.noway+1.3,[0,0]]]);
    off=[off[0]+pk[0],off[1]+pk[1]];
    const up=key(T,[[E.up-.6,0],[E.up,1],[E.public,1],[E.public+.4,0]]); off[1]-=up*18;
    const dp=key(T,[[E.boring-.5,0],[E.boring,1],[E.ring,1],[E.ring+.3,0]]); off=[off[0]-dp*8,off[1]+dp*24];
    if(T>=E.laugh) {off[0]+=Math.sin(T*37)*4;off[1]+=Math.cos(T*29)*4;}
  }
  s.off=off;
  return s;
}
function noodlePts(st){const pts=[];const tail=st.sh-NL;for(let s=Math.max(0,tail);s<=st.sh;s+=12)pts.push([s,atS(TR,TS,s)]);pts.push([st.sh,atS(TR,TS,st.sh)]);
  return pts.map(([s,p])=>{const w=clamp(1-(st.sh-s)/170);const k=w*w*(3-2*w);return [p[0]+st.off[0]*k,p[1]+st.off[1]*k];});}
function renderWorld(T){
  const st=worldState(T), th=st.th*Math.PI/180;
  // ---- noodle body
  let pts=noodlePts(st);
  const wv=pts.map((p,i)=>{const n=pts.length;if(i===0||i===n-1)return p;const dx=pts[i+1][0]-pts[i-1][0],dy=pts[i+1][1]-pts[i-1][1],L=Math.hypot(dx,dy)||1;
    const a=Math.sin(i*.55-T*6)*2.2*clamp((n-i)/8);return [p[0]-dy/L*a,p[1]+dx/L*a];});
  const d=smooth(wv); ['ndO','ndF'].forEach(id=>$(id).setAttribute('d',d));
  $('ndS').setAttribute('d',smooth(wv.map(p=>[p[0]+2,p[1]+5])));$('ndH').setAttribute('d',smooth(wv.slice(-Math.min(wv.length,60)).map(p=>[p[0]-2,p[1]-5])));
  const hd=pts[pts.length-1], pv=pts[Math.max(0,pts.length-4)], dirx=hd[0]-pv[0], diry=hd[1]-pv[1];
  // ---- noodle face (upright), looks at the palate before launch, forward while flying, around when outside
  const launched=T>=E.launch, out=T>=E.popout;
  tr('ndFace',hd[0],hd[1]-6,1,1,0);
  let lx=launched?dirx*6:(T>=E.ring&&T<E.laugh?-20:16), ly=launched?diry*6:(T>=E.ring&&T<E.laugh?-40:-34);
  if(out){lx=Math.sin(T*1.7)*20;ly=-6;}
  const nb=blinkK(T,1.3), nlid=(T>=E.boring-.3&&T<E.ring)?.55:(T>=E.noway&&T<E.noway+.9?.35:.12);
  const panic=(T>=E.launch&&T<E.innose+.5)||(T>=E.wait&&T<E.popout+.6);
  setOEye('nEyeL',19,{dx:lx,dy:ly,lid:panic?0:nlid,blink:nb,small:panic});setOEye('nEyeR',19,{dx:lx,dy:ly,lid:panic?0:nlid,blink:nb,small:panic});
  const nbr=T>=E.boring-.3&&T<E.ring?-6:(panic?10:(T>=E.peek-.8&&T<E.noway?8:2));
  setBrow('nBrowL',-17,-40-Math.max(0,nbr)*.4,18,-nbr*.8,3);setBrow('nBrowR',17,-40-Math.max(0,nbr)*.4,18,nbr*.8,3);
  setMouthV('noodle_m',speak('noodle',T),11,(T>=E.boring-.3&&T<E.ring)||out?-.6:.8,T,1);
  $('ndEyes').setAttribute('transform',`translate(0,${launched&&!out?-2:0})`);
  // speed lines while flying up the nose
  const fly=T>=E.launch&&T<E.innose+.3;
  if(fly){const L=Math.hypot(dirx,diry)||1,ux=dirx/L,uy=diry/L;$('speed').innerHTML=[-16,0,16].map((o,i)=>{const bx=hd[0]-ux*(40+i*8)-uy*o,by=hd[1]-uy*(40+i*8)+ux*o;return `<path d="M${bx.toFixed(1)},${by.toFixed(1)} l${(-ux*(46+i*10)).toFixed(1)},${(-uy*(46+i*10)).toFixed(1)}" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".85"/>`;}).join('');}
  show('speed',fly?1:0);
  // ---- soft palate body + face + arms
  const O=[400,490];
  $('palBody').setAttribute('transform',`translate(${O[0]},${O[1]}) rotate(${st.th.toFixed(2)})`);
  const fc=rot(104,-2,th), fx=O[0]+fc[0], fy=O[1]+fc[1];
  const pT=speak('palate',T); const breathe=1+Math.sin(T*3)*.012+(pT>.4?.03:0);
  $('palFace').setAttribute('transform',`translate(${fx.toFixed(1)},${fy.toFixed(1)}) scale(${breathe.toFixed(3)})`);
  const pnk=(T>=L09&&T<E.innose)||(T>=E.laugh&&T<E.innose);
  let ex=-10,ey=34; // looks at the noodle below-right
  if(T>=E.brain-.4&&T<L09+.6) {ex=-26;ey=-40;}
  if(T>=E.launch){const h=hd;ex=clamp((h[0]-fx)/4,-30,30);ey=clamp((h[1]-fy)/4,-30,30);}
  if(T>=E.blame-.2&&T<T_CLINIC){ex=-28;ey=-40;}
  const stern=(T>=ST['02_palate']&&T<E.down+.6)||(T>=E.noway&&T<ST['05_noodle'])||(T>=E.blame&&T<T_CLINIC);
  const plid=pnk?0:(stern?.34:.14), pbl=blinkK(T,.4);
  setOEye('pEyeL2',32,{dx:ex,dy:ey,lid:plid,blink:pbl,small:pnk});setOEye('pEyeR2',32,{dx:ex,dy:ey,lid:plid,blink:pbl,small:pnk});
  const dram=T>=E.bubble-.3&&T<E.bubbleEnd;
  const bang=stern?16:(pnk||dram?-14:4), by=pnk||dram?-36:-30;
  setBrow('paBrowL',-28,by-8,32,bang,dram?6:2);setBrow('paBrowR',30,by-11,32,-bang,dram?6:2);
  setMouthV('palate_m',pT,16,pnk?-.8:(stern?-.4:.3),T,3);
  // arms: acting poses (relative to the face), flailing once he drops
  const sh1=rot(70,34,th), sh2=rot(146,30,th), S1p=[O[0]+sh1[0],O[1]+sh1[1]], S2p=[O[0]+sh2[0],O[1]+sh2[1]];
  const dropK=clamp((st.th+14)/50);
  const hdN=hd, F=(dx,dy)=>[fx+dx,fy+dy];
  const POSE={rest:[F(-80,96),F(70,100)],down:[F(-80,96),F(52,160)],shove:[[hdN[0]-8,hdN[1]-30],F(70,100)],cross:[F(30,92),F(-26,96)],
    jazz:[F(-96,-26),F(96,-40)],cheeks:[F(-80,34),F(82,30)],fist:[F(-96,-60),F(70,100)]};
  const TL=[[0,'rest'],[E.down-.3,'rest'],[E.down,'down'],[E.down+1.1,'down'],[E.down+1.5,'rest'],[E.noway-.2,'rest'],[E.noway,'shove'],[E.noway+.7,'shove'],
    [E.shut-.4,'cross'],[E.shut+1.2,'cross'],[E.bubble-.3,'rest'],[E.bubble,'jazz'],[E.bubbleEnd-.2,'jazz'],[E.bubbleEnd+.2,'rest'],[L09-.2,'rest'],[L09,'cheeks'],
    [E.toolate+.5,'cheeks'],[E.laugh,'cheeks'],[E.drop,'cheeks'],[E.blame-.3,'cheeks'],[E.blame,'fist'],[T_CLINIC,'fist']];
  let i0=0;for(let i=0;i<TL.length;i++)if(T>=TL[i][0])i0=i;const i1=Math.min(TL.length-1,i0+1);
  const kk=i1===i0?1:eio(P(T,TL[i0][0],TL[i1][0])), A0=POSE[TL[i0][1]], A1=POSE[TL[i1][1]];
  let h1=[lerp(A0[0][0],A1[0][0],kk),lerp(A0[0][1],A1[0][1],kk)], h2=[lerp(A0[1][0],A1[1][0],kk),lerp(A0[1][1],A1[1][1],kk)];
  if(TL[i0][1]==='fist'||TL[i1][1]==='fist'){h1[0]+=Math.sin(T*22)*6;h1[1]+=Math.cos(T*22)*5;}
  if(TL[i0][1]==='cheeks'&&T<E.drop){h1[0]+=Math.sin(T*30)*2;h2[0]+=Math.sin(T*30+1)*2;}
  const flail=clamp(dropK*1.4)*(T<E.blame-.3?1:0);
  const fl1=[S1p[0]-40+Math.sin(T*13)*30,S1p[1]+30+Math.cos(T*11)*30], fl2=[S2p[0]+30+Math.cos(T*12)*28,S2p[1]+40+Math.sin(T*14)*28];
  h1=[lerp(h1[0],fl1[0],flail),lerp(h1[1],fl1[1],flail)];h2=[lerp(h2[0],fl2[0],flail),lerp(h2[1],fl2[1],flail)];
  const ad=hose(S1p,h1,16)+' '+hose(S2p,h2,-16);$('paAO').setAttribute('d',ad);$('paAI').setAttribute('d',ad);
  $('paHands').innerHTML=mitt(h1[0],h1[1],13,-20)+mitt(h2[0],h2[1],13,200);
  // sweat + tension ticks
  show('sweat',pnk?1:0); if(pnk) tr('sweat',fx,fy+Math.sin(T*20)*2);
  show('ticks',T>=E.shut-.05&&T<E.shut+1.1&&Math.floor(T*10)%2===0?1:0);
  // ---- brain on the phone
  const ringOn=T>=E.ring&&T<E.brain-.05, onPhone=T>=E.brain-.35;
  show('ring',ringOn&&Math.floor(T*8)%2===0?1:0);
  const pz=key(T,[[E.brain-.35,[590,262]],[E.brain-.05,[566,186]]]), shk=ringOn?Math.sin(T*60)*4:0;
  tr('phone',pz[0]+shk,pz[1],1,1,ringOn?Math.sin(T*50)*8:(onPhone?-20:0));
  const bsh=[530,232], bh=[pz[0]-6+shk,pz[1]+14], bd=hose(bsh,bh,-20);$('bArmO').setAttribute('d',bd);$('bArmI').setAttribute('d',bd);$('bHand').innerHTML=mitt(bh[0],bh[1],11,-30);
  const bT=speak('brain',T), sleepy=T<E.ring, flinch=T>=E.blame&&T<ST['16_brain'], smug=T>=ST['16_brain']-.1;
  const blid=sleepy?.55:(flinch?0:(smug?.42:(T>=E.toolate&&T<E.laugh?.25:.1)));
  const bx=T>=E.launch&&T<E.blame?-14:(onPhone&&T<E.laugh?-30:-16), byy=T>=E.launch&&T<E.blame?24:30;
  setOEye('bEyeL',36,{dx:bx,dy:byy,lid:blid,blink:blinkK(T,2.6),small:flinch});setOEye('bEyeR',36,{dx:bx,dy:byy,lid:blid,blink:blinkK(T,2.6),small:flinch});
  const bb=flinch?-16:(smug?-10:(T>=E.toolate&&T<E.laugh?-12:0));
  setBrow('bBrowL',386,130-(flinch||smug?8:0),34,-bb,4);setBrow('bBrowR',462,124-(flinch||smug?8:0),34,bb,4);
  setMouthV('brain_m',bT,17,smug?1:(T>=E.toolate&&T<E.laugh?-.7:.4),T,7);
  $('brainFace').setAttribute('transform',smug&&T<T_CLINIC?`rotate(${Math.sin(P(T,ST['16_brain'],ST['16_brain']+.6)*Math.PI*2)*4},430,200)`:'');
  // ---- nose: hairs tickle, daylight glow
  const tick=T>=E.innose&&T<E.popout+.4;
  for(let i=0;i<10;i++){const e=$('hair'+i);e.setAttribute('transform',tick?`rotate(${(Math.sin(T*16+i*1.3)*14).toFixed(1)},${[60,70,84,98,112,74,90,106,120,136][i]},${[470,452,436,420,404,486,478,470,462,456][i]})`:'');}
  show('glow',T>=E.daylight-.1?clamp(P(T,E.daylight-.1,E.daylight+.3)*.9-(T>E.popout+.6?.3:0)):0);
  // ---- teaching arrows
  const ad1=T>=E.down&&T<E.down+1.3, ad2=T>=wUp2&&T<wUp2+1.1;
  show('arDown',ad1?1:0); if(ad1) $('arDown').setAttribute('transform',`translate(560,620) scale(${eob(P(T,E.down,E.down+.25))}) translate(-560,-620) translate(0,${Math.sin(T*9)*5})`);
  show('arUpX',ad2?1:0); if(ad2) $('arUpX').setAttribute('transform',`translate(530,300) scale(${eob(P(T,wUp2,wUp2+.25))}) translate(-530,-300)`);
  // ---- the laugh: air bursts up from the lungs, HA! letters
  const lg=T>=E.laugh-.05&&T<E.innose;
  if(lg){const open=T>=E.drop+.1;const R=open?[[556,1250],[556,900],[560,620],[576,450],[540,356],[400,344],[240,362],[120,412],[46,494],[10,540]]:[[556,1250],[556,900],[560,640],[566,500]];
    const rp=crSample(R,8), rs=arcTab(rp), Lr=rs[rs.length-1];let h='';
    for(let k=0;k<6;k++){const u=((T-E.laugh)*(open?1.1:1.6)+k/6)%1, s0=u*Lr;const a=atS(rp,rs,s0), b=atS(rp,rs,s0+60), c=atS(rp,rs,s0+120);
      h+=`<path d="M${a[0].toFixed(1)},${a[1].toFixed(1)} Q${b[0].toFixed(1)},${b[1].toFixed(1)} ${c[0].toFixed(1)},${c[1].toFixed(1)}" fill="none" stroke="#fff" stroke-width="${k%2?5:8}" stroke-linecap="round" opacity="${(.85*Math.sin(u*Math.PI)).toFixed(2)}"/>`;}
    $('air').innerHTML=h;} else $('air').innerHTML='';
  let hh='';[0,.5,1.0,1.5,2.0].forEach((o,i)=>{const t0=E.laugh+o,k=P(T,t0,t0+1.1);if(k>0&&k<1){const x=420+[0,-60,50,-30,40][i],y=1000-k*260;
    hh+=`<text class="cap" x="${x}" y="${y.toFixed(1)}" text-anchor="middle" style="font-size:${46+i*4}px" opacity="${(1-k*k).toFixed(2)}" transform="rotate(${[-10,8,-6,12,-4][i]},${x},${y.toFixed(1)}) translate(${x},${y.toFixed(1)}) scale(${eob(clamp(k*4)).toFixed(3)}) translate(${-x},${(-y).toFixed(1)})">HA!</text>`;}});
  $('has').innerHTML=hh;
  // ---- thought bubble "in public"
  const bo=T>=E.bubble&&T<E.bubbleEnd; show('pubBub',bo?1:0);
  if(bo){const k=eob(P(T,E.bubble,E.bubble+.3));$('pubBub').setAttribute('transform',`translate(450,440) scale(${k}) translate(-450,-440)`);
    show('ha1',T>=E.public?1:0);show('ha2',T>=E.public+.25?1:0);}
  return st;
}
// ---------- inside camera: locked; shakes on impacts, gentle push toward the nostril while the noodle is in the nose
function renderInside(T){
  renderWorld(T);
  let sx=0,sy=0;
  if(T>=E.laugh&&T<E.launch+.6){const a=T<E.drop?4:8;sx+=Math.sin(T*47)*a;sy+=Math.cos(T*41)*a;}
  const imp=(t0,a)=>{const k=P(T,t0,t0+.3);if(k>0&&k<1){sx+=Math.sin(k*40)*a*(1-k);sy+=Math.cos(k*33)*a*(1-k);}};
  imp(E.noway,6);imp(E.drop,12);imp(E.popout,10);
  const pz=eio(P(T,E.innose,E.innose+1.2))*(1-eio(P(T,E.popout+.5,E.popout+1.1)));
  const z=1.15+.17*pz, cx=lerp(330,220,pz), cy=lerp(560,470,pz);
  $('cam').setAttribute('transform',`translate(${360+sx},${640+sy}) scale(${z}) translate(${-cx},${-cy})`);
  popLabel('lbPal',T,1.0,5.2,300,548);
  popLabel('lbNose',T,E.nose-.05,E.peek-.2,300,402);
  popLabel('lbBrain',T,E.brain,E.notnow-.2,250,96);
  const fin=P(T,T_CLINIC-.25,T_CLINIC); show('indark',fin*.9);
}
//__CLINIC__
//__STING__
function caption(T){let w='',ws=0;for(const L of D.lines)for(const x of L.words){if(T>=x[0]&&T<Math.max(x[1],x[0]+.12)){w=x[2];ws=x[0];}}
  if(!w){for(const L of D.lines)for(const x of L.words){if(T>=x[1]&&T<x[1]+.12){w=x[2];ws=x[0];}}}
  const c=$('cap'),big=KEY.test(w.replace(/[^A-Z']/g,'')); c.textContent=w; c.style.fontSize=big?'56px':'44px'; c.style.fill=big?'#ffd21f':'#fff';
  const k=eo(P(T,ws,ws+.09)); c.setAttribute('transform',`translate(360,1110) scale(${lerp(1.2,1,k)}) translate(-360,-1110)`);}
window.render=function(T){
  const ins=T<T_CLINIC, cli=T>=T_CLINIC&&T<T_STING, stg=T>=T_STING;
  $('s1').setAttribute('display',ins?'inline':'none'); $('s2').setAttribute('display',cli?'inline':'none'); $('sg').setAttribute('display',stg?'inline':'none');
  show('indark',0);
  if(ins) renderInside(T);
  if(cli) renderS2(T);
  if(stg) renderSting(T);
  caption(T);
};
window.render(0);
