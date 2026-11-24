// AA-61 exact matrix generators in types A and C and disconnected ideals.
function testAA61(){
 const assert=(p,m)=>{if(!p)throw Error(m)};
 const zero=n=>Array.from({length:n},()=>Array(n).fill(0));
 const unit=(n,i,j)=>{const a=zero(n);a[i][j]=1;return a};
 const sub=(a,b)=>a.map((r,i)=>r.map((x,j)=>x-b[i][j]));
 const mul=(a,b)=>a.map(r=>b[0].map((_,j)=>r.reduce((s,x,k)=>s+x*b[k][j],0)));
 const br=(a,b)=>sub(mul(a,b),mul(b,a));
 const scale=(a,c)=>a.map(r=>r.map(x=>x*c));
 const eq=(a,b)=>a.every((r,i)=>r.every((x,j)=>x===b[i][j]));
 const iszero=a=>a.every(r=>r.every(x=>x===0));
 let models=0,pairs=0,serre=0,exponents={};
 for(const type of ["A","C"])for(let rank=1;rank<=6;rank++){
  const n=type==="A"?rank+1:2*rank, e=[],f=[];
  for(let i=0;i<rank;i++){
   if(type==="A"){e.push(unit(n,i,i+1));f.push(unit(n,i+1,i));}
   else if(i===rank-1){e.push(unit(n,i,rank+i));f.push(unit(n,rank+i,i));}
   else{e.push(sub(unit(n,i,i+1),unit(n,rank+i+1,rank+i)));f.push(sub(unit(n,i+1,i),unit(n,rank+i,rank+i+1)));}
  }
  const h=e.map((x,i)=>br(x,f[i]));
  for(let i=0;i<rank;i++)for(let j=0;j<rank;j++){
   const a=i===j?2:Math.abs(i-j)!==1?0:type==="C"&&i===rank-2&&j===rank-1?-2:-1;
   assert(iszero(br(h[i],h[j])),"h,h");
   assert(eq(br(h[i],e[j]),scale(e[j],a)),"h,e");
   assert(eq(br(h[i],f[j]),scale(f[j],-a)),"h,f");
   assert(eq(br(e[i],f[j]),i===j?h[i]:zero(n)),"e,f");
   pairs++;
   if(i!==j)for(const X of [e,f]){
    let v=X[j];for(let k=0;k<=-a;k++){assert(!iszero(v),"premature zero");v=br(X[i],v);}
    assert(iszero(v),"Serre fails");serre++;exponents[1-a]=(exponents[1-a]||0)+1;
   }
  }
  models++;
 }
 // A disconnected block diagonal example: sl2 + sl3. All cross brackets vanish.
 const e=[unit(5,0,1),unit(5,2,3),unit(5,3,4)],f=[unit(5,1,0),unit(5,3,2),unit(5,4,3)];
 const h=e.map((x,i)=>br(x,f[i]));let cross=0;
 for(const a of [e[0],f[0],h[0]])for(const b of [e[1],e[2],f[1],f[2],h[1],h[2],br(e[1],e[2]),br(f[1],f[2])]){assert(iszero(br(a,b)),"cross ideal");cross++;}
 return {models,pairs,serre,exponents,cross};
}
console.log('AA-61 matrix relations: PASS',testAA61());
