// =============== 012: why we snore (Dr. Mira Explains, video 1). The reference's beats, our characters and words. ===============
const E=D.ev, ST=D.start, END=D.end;
//__VISEME__
function along(pts,s){s=clamp(s)*(pts.length-1);const i=Math.min(pts.length-2,Math.floor(s)),f=s-i;return [lerp(pts[i][0],pts[i+1][0],f),lerp(pts[i][1],pts[i+1][1],f)];}
const lend=id=>{const L=D.lines.find(l=>l.id===id);return L.t0+L.dur;};
const inL=(id,T,pre=.05,post=.1)=>T>=ST[id]-pre&&T<lend(id)+post;

// ---------- scenes ----------
const BEDPAT=patientSVG().replace(/id="([^"]+)"/g,'id="b$1"');          // a second copy of the 001 patient for the bedroom
let S1=`<g id="s1"><g id="cam">${throatWorld()}</g>${labelBox('lbAir','AIR',190,470,24)}${labelBox('lbTongue','TONGUE',200,930,26)}${labelBox('lbPal','SOFT PALATE',300,368,22)}</g>`;
let S2=`<g id="s2"><g id="bcam">${bedroomWorld(BEDPAT)}</g></g>`;
let S3=`<g id="s3">${clinicRoom12()}<g transform="translate(190,580) scale(1.5)">${doctorSVG()}</g><g transform="translate(565,720) scale(1.6)">${patientSVG()}</g></g>`;
const svg=$('S');
svg.innerHTML=`<defs><filter id="soft" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="7"/></filter>${DEFS}</defs>`
 +S1+S2+S3+`<text x="60" y="168" style="font-family:ComicNeue,sans-serif;font-weight:700;font-size:24px" fill="#fff" opacity=".42">@DrMiraExplains</text>`
 +`<g id="capg"><text id="cap" class="cap" x="360" y="1015" text-anchor="middle" style="stroke-width:7px;font-size:48px"></text></g>`;

// ---------- SET A: the throat ----------
function setPuff(id,x,y,s,{talk=0,T=0,look=0,lookY=0,mood=.3,angry=0,sx=1,sy=1,rot=0,seed=0,lid=.08}={}){
  $(id).setAttribute('transform',`translate(${x.toFixed(1)},${y.toFixed(1)}) rotate(${rot.toFixed(1)}) scale(${(s*sx).toFixed(3)},${(s*sy).toFixed(3)})`);
  const bl=blinkK(T,seed); setOEye(id+'_eL',10,{dx:look*40,dy:lookY*40,lid,blink:bl}); setOEye(id+'_eR',10,{dx:look*40,dy:lookY*40,lid,blink:bl});
  setBrow(id+'_bL',-10,-16+angry*2,12,angry*20,2); setBrow(id+'_bR',12,-16+angry*2,12,-angry*20,2);
  setMouthV(id+'_m',talk,7,mood,T,seed);
  $(id+'_b').setAttribute('transform',`scale(${(1+Math.sin(T*3+seed)*.03).toFixed(3)},${(1-Math.sin(T*3+seed)*.03).toFixed(3)})`);}
function renderThroat(T){
  const vib=T>=E.vib, vk=vib?P(T,E.vib,E.vib+.4):0, ff=vib?Math.sin(T*46)*(.11+.04*Math.sin(T*7))*vk:0;
  const sleepT=T<ST['01_puff']-.15;
  // the soft palate: droops (relaxed), flutters while the air squeezes past = the snore
  const droop=.6+.4*Math.sin(T*1.1)*.3;
  const pts=palPts(droop,-.05+ff); $('palBody').setAttribute('d',bandD(pts,66,30)); $('palHi').setAttribute('d',smooth(pts.slice(0,4).map(([x,y])=>[x,y-12])));
  const palAwake=T>=E.palWake, pT=speak('palate',T);
  const pLid=!palAwake?1:(vib?.0:.42), pw=palAwake?eob(P(T,E.palWake,E.palWake+.3)):1;
  setOEye('paEyeL',13,{dx:vib?Math.sin(T*30)*30:-14,dy:vib?Math.cos(T*27)*30:10,lid:pLid,blink:palAwake?blinkK(T,.9):0,small:vib});
  setOEye('paEyeR',13,{dx:vib?Math.sin(T*30+1)*30:-14,dy:vib?Math.cos(T*27+1)*30:10,lid:pLid,blink:palAwake?blinkK(T,.9):0,small:vib});
  setBrow('paBrL',272,428,18,vib?-14:16,2); setBrow('paBrR',310,436,18,vib?14:-16,2); show('paOpen',palAwake?1:0); show('paShut',palAwake?0:1); show('palate_m',palAwake?1:0);
  setMouthV('palate_m',pT,9,vib?-.8:-.5,T,2);
  $('palFace').setAttribute('transform',`translate(0,${(droop*6+ff*30).toFixed(1)}) scale(1)`); $('palFace').setAttribute('opacity',pw.toFixed(2));
  // the tongue: asleep, then groggy and grumpy; relaxed and smiling once the vibration starts
  const tT=speak('tongue',T);
  const relaxed=T>=ST['12_tongue']-.1, angry=inL('04_tongue',T)||inL('07_tongue',T), groggy=T<ST['04_tongue']-.1;
  const tLid=sleepT?1:(relaxed?(tT>.05?.55:(T>lend('12_tongue')?1:.85)):(angry?.32:(groggy?.55:.45)));
  const tLook=sleepT?0:(T<ST['05_puff2']-.2?-.9:(T<ST['08_palate']-.1?-.4:(T<E.squeeze?-.2:0)));
  show('tOpen',tLid>.97?0:1); show('tShut',tLid>.97?1:0);
  setOEye('tEyeL',34,{dx:tLook*40,dy:-6,lid:tLid,tilt:angry?14:0,blink:sleepT?0:blinkK(T,.4)}); setOEye('tEyeR',34,{dx:tLook*40,dy:-6,lid:tLid,tilt:angry?-14:0,blink:sleepT?0:blinkK(T,.4)});
  setBrow('tBrL',312,662-(angry?0:4),40,angry?18:(relaxed?-6:8),angry?2:6); setBrow('tBrR',402,662-(angry?0:4),40,angry?-18:(relaxed?6:-8),angry?2:6);
  setMouthV('tongue_m',tT,18,relaxed?.9:(angry?-.6:-.3),T,1);
  const br=Math.sin(T*(sleepT?1.6:1.2)); const wob=vib?Math.sin(T*38)*2.2*vk:0;
  $('tongueG').setAttribute('transform',`translate(0,${(br*3+wob).toFixed(2)}) rotate(${(wob*.3).toFixed(2)},300,820)`);
  let zz='';if(sleepT||relaxed&&T>ST['12_tongue']+1.2){for(let i=0;i<3;i++){const u=((T*.55)+i/3)%1;zz+=`<text x="${(430+u*70).toFixed(0)}" y="${(660-u*130).toFixed(0)}" style="font-family:LG,sans-serif;font-size:${(30+u*24).toFixed(0)}px" fill="#ffffff" stroke="${INK}" stroke-width="2.4" opacity="${Math.sin(u*Math.PI).toFixed(2)}">Z</text>`;}}
  $('zzz').innerHTML=zz;
  // the two air puffs
  const p1T=speak('puff',T), p2T=speak('puff2',T);
  const inK=eo(P(T,E.puffIn,E.puffIn+.85)), sq=P(T,E.squeeze,E.squeeze+1.3);
  let p1=[lerp(-90,300,inK),536+Math.sin(T*2.2)*4], p1s=[1,1], p1r=0;
  if(T>=ST['06_puff']-.1&&T<E.squeeze){p1[0]+=Math.sin(clamp(P(T,ST['06_puff'],ST['06_puff']+.35))*Math.PI)*18;}
  if(sq>0){const path=[[300,536],[420,560],[490,620],[530,760],[528,980],[520,1260]];p1=along(path,eio(sq));p1s=[lerp(1,.45,P(sq,.2,.5)),lerp(1,1.7,P(sq,.2,.5))];p1r=sq>.4?90:lerp(0,90,P(sq,.15,.4));}
  setPuff('pf1',p1[0],p1[1],1.05,{talk:p1T,T,look:sq>0?0:(T<ST['05_puff2']-.3?1:(T<ST['08_palate']?.6:.2)),lookY:T>=E.palWake&&T<E.squeeze?-.8:0,mood:p1T>.05?-.1:.3,angry:T>=ST['06_puff']-.2?.8:.2,sx:p1s[0],sy:p1s[1],rot:p1r,seed:1});
  show('pf1',T>=E.puffIn&&sq<1?1:0);
  const in2=eo(P(T,E.puff2In,E.puff2In+.75)), sq2=P(T,E.squeeze+.15,E.squeeze+1.45);
  let p2=[lerp(-90,430,in2),370+Math.sin(T*2.6+1)*4], p2s=[1,1], p2r=0;
  if(sq2>0){const path=[[430,370],[506,392],[544,470],[548,640],[540,900],[530,1260]];p2=along(path,eio(sq2));p2s=[lerp(1,.45,P(sq2,.15,.45)),lerp(1,1.7,P(sq2,.15,.45))];p2r=sq2>.3?90:lerp(0,90,P(sq2,.05,.3));}
  setPuff('pf2',p2[0],p2[1],1.15,{talk:p2T,T,look:sq2>0?0:(T<ST['06_puff']?.4:(T<ST['09_puff2']?.2:.6)),lookY:sq2>0?0:.5,mood:-.2,angry:.7,sx:p2s[0],sy:p2s[1],rot:p2r,seed:2});
  show('pf2',T>=E.puff2In&&sq2<1?1:0);
  // while snoring: a stream of air squeezing down the throat tube, and the vibration marks
  let fl='';if(T>=E.squeeze+.6){for(let i=0;i<7;i++){const u=((T*1.1)+i/7)%1, y=lerp(430,1250,u), x=548-6*Math.sin(u*9+i), w=lerp(16,9,u);
      fl+=`<ellipse cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" rx="${(w*.6).toFixed(1)}" ry="${(w*1.8).toFixed(1)}" fill="#f4fbff" opacity="${(.85*Math.sin(u*Math.PI)).toFixed(2)}" stroke="#9fc9e6" stroke-width="2"/>`;}}
  $('flow').innerHTML=fl;
  let vb='';if(vib){const k=(T*6)%1;[[452,540,0],[590,700,1],[452,450,2]].forEach(([x,y,j])=>{for(let q=0;q<3;q++){const r=26+q*16+k*14;
      vb+=`<path d="M${(x+r*Math.cos(-.9+j)).toFixed(1)},${(y+r*Math.sin(-.9+j)).toFixed(1)} A${r},${r} 0 0 1 ${(x+r*Math.cos(.2+j)).toFixed(1)},${(y+r*Math.sin(.2+j)).toFixed(1)}" fill="none" stroke="#ffd21f" stroke-width="6" stroke-linecap="round" opacity="${(.9-q*.25).toFixed(2)}"/>`;}});}
  $('vibes').innerHTML=vb;
  // camera: the reference opens close on the sleeping tongue and pulls back at about 1.5 s; a small shake while it snores
  const zk=eio(P(T,E.zoomOut,E.zoomOut+.8)), z=lerp(1.38,1,zk), cx=lerp(355,360,zk), cy=lerp(745,640,zk);
  const sh=vib?Math.sin(T*55)*2.4:0;
  $('cam').setAttribute('transform',`translate(${(360+sh).toFixed(1)},640) scale(${z.toFixed(4)}) translate(${(-cx).toFixed(1)},${(-cy).toFixed(1)})`);
  popLabel('lbAir',T,E.puffIn+.7,E.puffIn+3.2,190,470); popLabel('lbTongue',T,ST['02_tongue']+.1,ST['02_tongue']+2.6,200,930);
  popLabel('lbPal',T,E.palWake+.15,E.palWake+2.8,300,368);
}
// ---------- SET B: the bedroom ----------
function renderBed(T){
  const t=T-E.bed, slap=T>=E.slap, sk=P(T,E.slap-.28,E.slap);
  const snoreA=slap?0:(.55+.45*Math.sin(t*2.2*Math.PI/2.8*2));
  // his head: asleep with the mouth open, jerks on the slap, then wide awake
  const jerk=slap?Math.exp(-(T-E.slap)*6)*Math.sin((T-E.slap)*30)*6:0;
  tr('bpatHead',0,Math.sin(t*1.3)*1.2,1,1,(slap?8:-2)+jerk);
  setHEye('bpEyeL',slap?-4:0,slap?0:1); setHEye('bpEyeR',slap?-4:0,slap?0:1);
  $('bpBrows').setAttribute('d',slap?'M-36,62 Q-24,52 -10,58 M8,58 Q22,52 34,62':'M-36,72 Q-24,68 -10,70 M8,70 Q22,68 34,72');
  if(!slap) setMouthV('bpat_m',.35+snoreA*.5,10,0,T,6); else setMouthV('bpat_m',speak('partner',T)>.05?0:0,10,-.9,T,6);
  show('bpHandprint',slap?Math.min(1,(T-E.slap)*6):0); show('bpatBlush',slap?.7:0); show('bpSweat',slap&&T>E.slap+.3?1:0);
  $('bpSweat').setAttribute('transform',`translate(46,${(70+(((T-E.slap)*14)%24)).toFixed(1)})`);
  // snore waves out of his mouth and big Z's while he sleeps
  let sw='';if(!slap){for(let i=0;i<3;i++){const u=((t*.9)+i/3)%1;sw+=`<path d="M${(400+u*150).toFixed(1)},${(650-u*40).toFixed(1)} q20,-24 40,0 t40,0" fill="none" stroke="#7fb5d9" stroke-width="${(9-u*4).toFixed(1)}" stroke-linecap="round" opacity="${(1-u).toFixed(2)}"/>`;
      sw+=`<text x="${(520+u*90).toFixed(0)}" y="${(520-u*200).toFixed(0)}" style="font-family:LG,sans-serif;font-size:${(46+u*40).toFixed(0)}px" fill="#fff" stroke="${INK}" stroke-width="3" opacity="${Math.sin(u*Math.PI).toFixed(2)}">Z</text>`;}}
  $('snoreW').innerHTML=sw;
  // the partner's arm swings in from the left and slaps his cheek
  const out=P(T,E.slap+.45,E.slap+.9), k=slap?1-out:eio(sk);
  show('slapArm',T>=E.slap-.3&&out<1?1:0);
  const sh=[900,1040], el=[lerp(840,560,k),lerp(980,860,k)], hd=[lerp(760,300,k),lerp(900,600,k)];
  const d=`M${sh[0]},${sh[1]} Q${el[0]},${el[1]} ${hd[0]+36},${hd[1]+24}`; $('saO').setAttribute('d',d); $('saS').setAttribute('d',`M${sh[0]},${sh[1]} Q${el[0]},${el[1]} ${lerp(sh[0],hd[0],.55)},${lerp(sh[1],hd[1],.55)}`);
  $('saK').setAttribute('d',`M${lerp(sh[0],hd[0],.5)},${lerp(sh[1],hd[1],.5)} L${hd[0]+30},${hd[1]+20}`); $('saKi').setAttribute('d',`M${lerp(sh[0],hd[0],.5)},${lerp(sh[1],hd[1],.5)} L${hd[0]+30},${hd[1]+20}`);
  $('saH').innerHTML=slapHand(hd[0],hd[1],-70,1.6);
  let im='';if(slap&&T<E.slap+1.6){const q=P(T,E.slap,E.slap+.5);for(let i=0;i<4;i++){const a=-1.2+i*.5,r=lerp(40,90,q);im+=`<path d="M${(250+Math.cos(a)*r).toFixed(1)},${(600+Math.sin(a)*r).toFixed(1)} l${(Math.cos(a)*30).toFixed(1)},${(Math.sin(a)*30).toFixed(1)}" stroke="#ffd21f" stroke-width="8" stroke-linecap="round" opacity="${(1-q*.6).toFixed(2)}"/>`;}}
  $('impact').innerHTML=im;
  const shake=slap&&T<E.slap+.25?Math.sin(T*90)*8:0;
  $('bcam').setAttribute('transform',`translate(${shake.toFixed(1)},0)`);
}
// ---------- SET C: the clinic ----------
function renderClinic(T){
  const dT=speak('doctor',T), pT=speak('patient',T);
  tr('docHead',0,Math.sin(T*1.3)*1.2-(dT>.7?1.5:0),1,1,2+(dT>.15?Math.sin(T*6.5)*1.8*dT:0));
  $('dBrows').setAttribute('transform',`translate(0,${dT>.72?-3.5:0})`);
  let pr=-3+Math.sin(T*.8)*1; if(pT>.2) pr+=Math.sin(T*7)*2;
  tr('patHead',0,Math.sin(T*1.5+1)*1.2,1,1,pr);
  $('pBrows').setAttribute('d',T<ST['15_doctor']?'M-36,66 Q-24,64 -10,60 M8,60 Q22,64 34,66':'M-36,70 Q-24,64 -10,66 M8,66 Q22,64 34,70');
  setMouthV('doc_m',dT,10,.5,T,5); setMouthV('pat_m',pT,10,-.3,T,6);
  setHEye('dEyeL',3,blinkK(T,.7)); setHEye('dEyeR',3,blinkK(T,.7)); setHEye('pEyeL',-3,blinkK(T,2.1)); setHEye('pEyeR',-3,blinkK(T,2.1));
  show('pHandprint',.75); show('patBlush',.5); show('pSweat',0);
  // he holds his slapped cheek
  const sh=[-84,234], el=[-128,316], wr=[-58,186+Math.sin(T*1.4)*2];
  const d=limbD([sh,el,wr],[44,38,32]); $('patArmLD').setAttribute('d',d); $('patArmLO').setAttribute('d',d);
  $('patHandL').innerHTML=hand(wr[0]+6,wr[1]-30,-178,1.2,PSK);
  $('docArmR').setAttribute('transform',`rotate(${(dT>.2?-6+Math.sin(T*4.2)*7*dT:0).toFixed(2)},86,226)`);
}
function caption(T){let w='',ws=0;for(const L of D.lines)for(const x of L.words){if(T>=x[0]&&T<Math.max(x[1],x[0]+.12)){w=x[2];ws=x[0];}}
  if(!w){for(const L of D.lines)for(const x of L.words){if(T>=x[1]&&T<x[1]+.1){w=x[2];ws=x[0];}}}
  const c=$('cap'); c.textContent=w; const k=eo(P(T,ws,ws+.12)); c.setAttribute('transform',`translate(360,998) scale(${lerp(1.4,1,k).toFixed(3)}) translate(-360,-998)`);}
window.render=function(T){
  const sc=T<E.bed?1:T<E.clinic?2:3;
  ['s1','s2','s3'].forEach((id,i)=>$(id).setAttribute('display',sc===i+1?'inline':'none'));
  if(sc===1) renderThroat(T); if(sc===2) renderBed(T); if(sc===3) renderClinic(T);
  caption(T);
};
window.render(0);
