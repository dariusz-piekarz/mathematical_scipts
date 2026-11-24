// AA-69-DEN-01: aa:tw:weyl-denominator, aa:lem:weyl-regular-orbits.
// Exact weight-coordinate calculations, independent group enumeration by matrices.
const assert=(b,m)=>{if(!b)throw Error(m)};
const key=v=>v.join(","),parse=s=>s.split(",").map(Number);
const add=(f,v,c)=>{const k=key(v),x=(f.get(k)||0n)+c;if(x)f.set(k,x);else f.delete(k)};
const equal=(a,b)=>a.size===b.size&&[...a].every(([k,v])=>b.get(k)===v);
const types=[
 ["A1",[[2]],2,1],["A2",[[2,-1],[-1,2]],6,3],
 ["B2",[[2,-2],[-1,2]],8,4],["G2",[[2,-3],[-1,2]],12,6],
 ["A1xA1",[[2,0],[0,2]],4,2],
 ["A3",[[2,-1,0],[-1,2,-1],[0,-1,2]],24,6],
 ["B3",[[2,-1,0],[-1,2,-2],[0,-1,2]],48,9],
 ["C3",[[2,-1,0],[-1,2,-1],[0,-2,2]],48,9],
 ["D4",[[2,-1,0,0],[-1,2,-1,-1],[0,-1,2,0],[0,-1,0,2]],192,12]
];
let groups=0,groupElements=0,positiveRoots=0,coefficients=0,regularOrbits=0,singularOrbits=0,reflections=0;
for(const [name,C,size,pos] of types){
 const r=C.length,unit=i=>Array.from({length:r},(_,j)=>+(i===j));
 const col=j=>C.map(row=>row[j]);
 const refl=(v,i)=>v.map((x,j)=>x-v[i]*C[j][i]);
 const rootRefl=(v,i)=>{const w=[...v];w[i]-=C[i].reduce((s,c,j)=>s+c*v[j],0);return w};
 const roots=new Map(),queue=[];
 function put(v){if(!roots.has(key(v))){roots.set(key(v),v);queue.push(v)}}
 for(let i=0;i<r;i++)put(unit(i));
 for(let j=0;j<queue.length;j++)for(let i=0;i<r;i++)put(rootRefl(queue[j],i));
 const positive=queue.filter(v=>v.every(x=>x>=0));
 assert(queue.length===2*pos&&positive.length===pos,name+" root count");
 for(let i=0;i<r;i++)for(const v of positive){const w=rootRefl(v,i);assert(key(v)===key(unit(i))?w.every(x=>x<=0):w.every(x=>x>=0),name+" sign permutation");reflections++}
 const weight=v=>C.map(row=>row.reduce((s,c,j)=>s+c*v[j],0));
 const rho=Array(r).fill(1),sum=Array(r).fill(0);
 for(const v of positive)weight(v).forEach((x,j)=>sum[j]+=x);
 assert(sum.every(x=>x===2),name+" rho");
 const I=Array.from({length:r},(_,i)=>unit(i));
 const ms=[{m:I,s:1}],seen=new Map([[I.map(key).join(";"),1]]);
 for(let j=0;j<ms.length;j++)for(let i=0;i<r;i++){
  const m=ms[j].m.map(v=>refl(v,i)),s=-ms[j].s,k=m.map(key).join(";");
  if(seen.has(k))assert(seen.get(k)===s,name+" determinant sign");
  else{seen.set(k,s);ms.push({m,s})}
 }
 assert(ms.length===size,name+" group size");
 const apply=(m,v)=>Array.from({length:r},(_,i)=>m.reduce((s,col,j)=>s+col[i]*v[j],0));
 const alt=v=>{const f=new Map();for(const {m,s} of ms)add(f,apply(m,v),BigInt(s));return f};
 let D=new Map([[key(rho),1n]]);
 for(const root of positive){const a=weight(root),old=D;D=new Map(old);for(const [k,c] of old)add(D,parse(k).map((x,j)=>x-a[j]),-c)}
 assert(equal(D,alt(rho)),name+" denominator");
 assert(D.size===size&&D.get(key(rho))===1n,name+" rho regular");
 for(let i=0;i<r;i++)for(const [k,v] of D){assert(D.get(key(refl(parse(k),i)))===-v,name+" alternating");reflections++}
 for(let mask=0;mask<2**r;mask++){
  const v=Array.from({length:r},(_,i)=>1+((mask>>i)&1));
  const a=alt(v);
  assert(a.size===size&&a.get(key(v))===1n,name+" free regular orbit");
  assert([...a.keys()].filter(k=>parse(k).every(x=>x>0)).length===1,name+" unique strict dominant");
  regularOrbits++;
 }
 for(let i=0;i<r;i++){const v=[...rho];v[i]=0;assert(alt(v).size===0,name+" singular cancellation");singularOrbits++}
 groups++;groupElements+=size;positiveRoots+=pos;coefficients+=D.size;
}
console.log("AA-69-DEN-01: PASS",{groups,groupElements,positiveRoots,coefficients,regularOrbits,singularOrbits,reflections});

// AA-69-DEN-02: aa:lem:weyl-positive-permutation, aa:lem:weyl-regular-orbits.
// BFS shortest words in root coordinates; test the deletion lemma directly.
function checkExchange69(){
 let elements=0,extensions=0,deletions=0,nonDominantRegular=0,positiveStabilizers=0;
 for(const [name,C,size,pos] of types){
  const r=C.length,unit=i=>Array.from({length:r},(_,j)=>+(i===j));
  const I=Array.from({length:r},(_,i)=>unit(i));
  const rootRefl=(v,i)=>{const w=[...v];w[i]-=C[i].reduce((s,c,j)=>s+c*v[j],0);return w};
  const weightRefl=(v,i)=>v.map((x,j)=>x-v[i]*C[j][i]);
  const apply=(m,v)=>Array.from({length:r},(_,i)=>m.reduce((s,col,j)=>s+col[i]*v[j],0));
  const matrixKey=m=>m.map(key).join(";");
  const wordMatrix=word=>{let m=I;for(let k=word.length-1;k>=0;k--)m=m.map(v=>rootRefl(v,word[k]));return m};
  const queue=[{m:I,word:[]}],seen=new Map([[matrixKey(I),queue[0]]]);
  for(let k=0;k<queue.length;k++)for(let i=0;i<r;i++){
   const m=queue[k].m.map(v=>rootRefl(v,i)),s=matrixKey(m);
   if(!seen.has(s)){const z={m,word:[i,...queue[k].word]};seen.set(s,z);queue.push(z)}
  }
  assert(queue.length===size,name+" order");
  for(const {m,word} of queue){
   assert(matrixKey(wordMatrix(word))===matrixKey(m),name+" word product");
   if(m.every(v=>v.every(x=>x>=0))){assert(word.length===0,name+" chamber stabilizer");positiveStabilizers++}
   let rho=Array(r).fill(1);for(let k=word.length-1;k>=0;k--)rho=weightRefl(rho,word[k]);
   if(word.length){assert(rho.some(x=>x<0),name+" regular need not be dominant");nonDominantRegular++}
   for(let j=0;j<r;j++){
    const target=m.map((v,i)=>i===j?v.map(x=>-x):v.map((x,k)=>x-C[j][i]*m[j][k]));
    // The j-th column above uses C[j][j]=2, so the special case agrees.
    const z=seen.get(matrixKey(target));assert(z,name+" extension in group");
    const negative=m[j].every(x=>x<=0);
    assert(z.word.length===word.length+(negative?-1:1),name+" length change");
    if(negative){
     let v=unit(j),at=-1;
     for(let k=word.length-1;k>=0;k--){const w=rootRefl(v,word[k]);if(v.every(x=>x>=0)&&w.every(x=>x<=0)){assert(key(v)===key(unit(word[k])),name+" sign crossing");at=k;break}v=w}
     assert(at>=0,name+" missing crossing");
     assert(matrixKey(wordMatrix(word.filter((_,k)=>k!==at)))===matrixKey(target),name+" deleted word");
     deletions++;
    }
    extensions++;
   }
   elements++;
  }
 }
 return {elements,extensions,deletions,nonDominantRegular,positiveStabilizers};
}
console.log("AA-69-DEN-02: PASS",checkExchange69());
