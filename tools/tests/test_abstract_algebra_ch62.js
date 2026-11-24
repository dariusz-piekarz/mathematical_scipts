// AA-62: exact Weyl orbits and positive support descent.
function rootAudit62(){
 const assert=(v,m)=>{if(!v)throw Error(m)};
 const models=[
 ["A1",[[2]],2],["A2",[[2,-1],[-1,2]],6],
 ["B2",[[2,-2],[-1,2]],8],["G2",[[2,-3],[-1,2]],12],
 ["A3",[[2,-1,0],[-1,2,-1],[0,-1,2]],12],
 ["C3",[[2,-1,0],[-1,2,-2],[0,-1,2]],18],
 ["D4",[[2,-1,0,0],[-1,2,-1,-1],[0,-1,2,0],[0,-1,0,2]],24],
 ["F4",[[2,-1,0,0],[-1,2,-2,0],[0,-1,2,-1],[0,0,-1,2]],48],
 ["A1+A2",[[2,0,0],[0,2,-1],[0,-1,2]],8]
 ];
 let roots=0,descents=0,reflections=0,nonroots=0;
 for(const [name,A,count] of models){
 const r=A.length, key=v=>v.join(","), dot=(i,v)=>A[i].reduce((s,a,j)=>s+a*v[j],0), reflect=(i,v)=>v.map((x,j)=>j===i?x-dot(i,v):x);
 const simple=Array.from({length:r},(_,i)=>Array.from({length:r},(_,j)=>Number(i===j)));
 const list=[...simple],set=new Set(list.map(key));
 for(let j=0;j<list.length;j++)for(let i=0;i<r;i++){const w=reflect(i,list[j]);if(!set.has(key(w))){set.add(key(w));list.push(w);assert(list.length<=count,name+" infinite or too many");}}
 assert(list.length===count,name+" root count");roots+=count;
 for(const v of list){assert(v.every(x=>x>=0)||v.every(x=>x<=0),name+" mixed root");
 for(let i=0;i<r;i++){assert(key(reflect(i,reflect(i,v)))===key(v),"involution");assert(set.has(key(reflect(i,v))),"closure");reflections++;}
 if(v.every(x=>x>=0)&&v.filter(Boolean).length>1){const i=v.findIndex((x,j)=>x>0&&dot(j,v)>0);assert(i>=0,"descent exists");const w=reflect(i,v);assert(w.every(x=>x>=0)&&w.reduce((a,b)=>a+b,0)<v.reduce((a,b)=>a+b,0),"height");descents++;}
 }
 // Nonroots cannot pass the positive-support descent criterion.
 function check(v){if(!v.some(Boolean)||set.has(key(v)))return;nonroots++;let w=v.slice();for(let k=0;k<=v.reduce((a,b)=>a+b,0);k++){if(w.some(x=>x<0)){assert(w.some(x=>x>0),"negative instead of mixed");return;}const support=w.filter(Boolean);if(support.length===1){assert(support[0]>1,"nonroot became simple");return;}const i=w.findIndex((x,j)=>x>0&&dot(j,w)>0);assert(i>=0,"positive definite descent");w=reflect(i,w);}throw Error("did not terminate");}
 function enumerate(v){if(v.length===r){check(v);return;}for(let i=0;i<=5;i++)enumerate([...v,i]);}enumerate([]);
 }
 return {models:models.length,roots,reflections,descents,nonroots};
}
console.log('AA-62 root descent: PASS',rootAudit62());
