// AA-61 independent G2 model on seven weights; exact BigInt elimination.
function independent61(){
 const assert=(p,m)=>{if(!p)throw Error(m)};
 // G2 seven-dimensional weight chain; alpha short, beta long.
 const W=[[2,1],[1,1],[1,0],[0,0],[-1,0],[-1,-1],[-2,-1]],n=W.length;
 const z=()=>Array.from({length:n},()=>Array(n).fill(0n));
 const sub=(a,b)=>a.map((r,i)=>r.map((x,j)=>x-b[i][j]));
 const mul=(a,b)=>a.map(r=>b[0].map((_,j)=>r.reduce((s,x,k)=>s+x*b[k][j],0n)));
 const br=(a,b)=>sub(mul(a,b),mul(b,a));
 const scale=(a,c)=>a.map(r=>r.map(x=>x*BigInt(c)));
 const eq=(a,b)=>a.every((r,i)=>r.every((x,j)=>x===b[i][j]));
 const nonzero=a=>a.some(r=>r.some(x=>x!==0n));
 const E=[z(),z()],F=[z(),z()],H=[z(),z()], A=[[2,-3],[-1,2]];
 for(let j=0;j<n;j++)for(let i=0;i<2;i++)H[i][j][j]=BigInt(A[i][0]*W[j][0]+A[i][1]*W[j][1]);
 for(let i=0;i<2;i++)for(let j=0;j<n;j++){
   const below=W.findIndex(w=>w.every((v,k)=>v===W[j][k]-Number(k===i)));
   if(below<0)continue;
   F[i][below][j]=1n;
   let m=0,up=j;
   while(true){const t=W.findIndex(w=>w.every((v,k)=>v===W[up][k]+Number(k===i)));if(t<0)break;up=t;m++;}
   let down=below,length=m+1;
   while(true){const t=W.findIndex(w=>w.every((v,k)=>v===W[down][k]-Number(k===i)));if(t<0)break;down=t;length++;}
   E[i][j][below]=BigInt((m+1)*(length-m));
 }
 let rel=0,serre=[];
 for(let i=0;i<2;i++)for(let j=0;j<2;j++){
   assert(eq(br(H[i],H[j]),z()),"HH");assert(eq(br(H[i],E[j]),scale(E[j],A[i][j])),"HE");
   assert(eq(br(H[i],F[j]),scale(F[j],-A[i][j])),"HF");assert(eq(br(E[i],F[j]),i===j?H[i]:z()),"EF");rel+=4;
   if(i!==j)for(const X of [E,F]){
    let v=X[j];for(let k=0;k<=-A[i][j];k++){assert(nonzero(v),"premature vanishing");v=br(X[i],v);}
    assert(!nonzero(v),"Serre");serre.push(1-A[i][j]);
   }
 }
 // Incremental exact row elimination over Q using integer arithmetic.
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b)[a,b]=[b,a%b];return a};
 function space(){
  const rows=[],matrices=[];
  return {matrices,add(m){let v=m.flat();for(const [p,w] of rows){if(!v[p])continue;const a=w[p],b=v[p];v=v.map((x,i)=>a*x-b*w[i]);const d=v.reduce(gcd,0n);if(d)v=v.map(x=>x/d);}
   const p=v.findIndex(x=>x!==0n);if(p<0)return false;rows.push([p,v]);matrices.push(m);return true;}};
 }
 function generated(xs){const s=space();xs.forEach(x=>s.add(x));for(let i=0;i<s.matrices.length;i++)for(let j=0;j<i;j++)s.add(br(s.matrices[i],s.matrices[j]));return s.matrices;}
 const all=generated([...E,...F]),positive=generated(E),negative=generated(F);
 assert(all.length===14&&positive.length===6&&negative.length===6,"G2 dimensions");
 const joined=space();[...positive,...H,...negative].forEach(x=>joined.add(x));assert(joined.matrices.length===14,"triangle");
 let central=positive,classes=[central.length];
 while(central.length){const s=space();for(const a of positive)for(const b of central)s.add(br(a,b));central=s.matrices;classes.push(central.length);assert(classes.length<=7,"not nilpotent");}
 assert(classes.join(",")==="6,4,3,2,1,0","G2 lower central");
 // Ideal generation: each root vector from either nilpotent subalgebra generates all G2.
 let ideals=0;
 for(const seed of [...positive,...negative]){const s=space();s.add(seed);for(let i=0;i<s.matrices.length;i++)for(const a of all)s.add(br(a,s.matrices[i]));assert(s.matrices.length===14,"proper ideal");ideals++;}
 return {relations:rel,serre,dimensions:[negative.length,H.length,positive.length],lowerCentral:classes,ideals};
}
console.log('AA-61 G2 independent: PASS',independent61());
