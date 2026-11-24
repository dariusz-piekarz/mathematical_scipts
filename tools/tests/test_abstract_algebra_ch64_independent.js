// AA-64: exact adjoint Jordan/Fitting tests in sl_n, and Heisenberg counterexample.
function cartan64(){
 const assert=(x,m)=>{if(!x)throw Error(m)};
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b)[a,b]=[b,a%b];return a;};
 const rank=vs=>{let rows=[];for(let v of vs){v=v.slice();for(const [p,w] of rows){if(!v[p])continue;let a=w[p],b=v[p];v=v.map((x,i)=>a*x-b*w[i]);let d=v.reduce(gcd,0n);if(d)v=v.map(x=>x/d);}let p=v.findIndex(x=>x!==0n);if(p>=0)rows.push([p,v]);}return rows.length;};
 const Z=n=>Array.from({length:n},()=>Array(n).fill(0n));
 const E=(n,i,j)=>{let a=Z(n);a[i][j]=1n;return a};
 const add=(a,b)=>a.map((r,i)=>r.map((v,j)=>v+b[i][j]));
 const sc=(a,c)=>a.map(r=>r.map(v=>v*c));
 const mul=(a,b)=>a.map(r=>b[0].map((_,j)=>r.reduce((s,v,k)=>s+v*b[k][j],0n)));
 const br=(a,b)=>add(mul(a,b),sc(mul(b,a),-1n));
 const I=n=>Z(n).map((r,i)=>r.map((_,j)=>i===j?1n:0n));
 let models=0,fitting=0,normalizers=0,jordan=0;
 for(let n=2;n<=5;n++){
  const H=Array.from({length:n-1},(_,i)=>add(E(n,i,i),sc(E(n,n-1,n-1),-1n)));
  const B=[...H];for(let i=0;i<n;i++)for(let j=0;j<n;j++)if(i!==j)B.push(E(n,i,j));
  const d=B.length;
  for(let k=1;k<=n;k++){
   // Repeated eigenvalues on the first k coordinates, single Jordan chain.
   let vs=Array.from({length:n},(_,i)=>BigInt(i<k?0:i-k+1));
   let sum=vs.reduce((a,b)=>a+b,0n);vs=vs.map(x=>BigInt(n)*x-sum);
   let S=Z(n),N=Z(n);vs.forEach((x,i)=>S[i][i]=x);for(let i=0;i<k-1;i++)N[i][i+1]=1n;
   let U=I(n),V=I(n);for(let i=0;i<n-1;i++){let A=E(n,i+1,i);U=mul(add(I(n),sc(A,2n)),U);V=mul(V,add(I(n),sc(A,-2n)));}
   let conj=A=>mul(mul(U,A),V);S=conj(S);N=conj(N);const X=add(S,N),basis=B.map(conj);
   const step=(T,vecs)=>vecs.map(Y=>br(T,Y));
   let images=basis;for(let i=0;i<d;i++)images=step(X,images);
   assert(d-rank(images.map(a=>a.flat()))===k*k+n-k-1,"Fitting dimension");
   assert(rank(step(S,basis).map(a=>a.flat()))===rank(images.map(a=>a.flat())),"centralizer dimension");
   let C=[];for(const Y of basis){if(br(S,Y).flat().every(a=>a===0n))C.push(Y);}
   assert(C.length===k*k+n-k-1,"centralizer basis");
   assert(C.every(Y=>{for(let i=0;i<d;i++)Y=br(X,Y);return Y.flat().every(a=>a===0n);}),"centralizer included in fitting");fitting++;
   assert(br(S,N).flat().every(a=>a===0n),"commuting parts");let ns=basis;for(let i=0;i<d;i++)ns=step(N,ns);assert(ns.every(A=>A.flat().every(a=>a===0n)),"nilpotent part");jordan++;
   let hs=H.map(conj);const normalizerRank=rank(basis.map(Y=>hs.flatMap(T=>br(Y,T).flat())));
   assert(d-normalizerRank===n-1,"centralizer of diagonal");
   // For any root basis vector at least one bracket is nonzero modulo H; hence no extra normalizer.
   const off=A=>A.flatMap((row,i)=>row.filter((_,j)=>i!==j));
   const quotientRank=rank(basis.map(Y=>hs.flatMap(T=>off(mul(mul(V,br(Y,T)),U)))));
   assert(d-quotientRank===n-1,"normalizer dimension in quotient");normalizers++;
   models++;
  }
 }
 // Heisenberg: whole algebra is Cartan, but the center is the only maximal toral algebra.
 const p=E(3,0,1),q=E(3,1,2),z=E(3,0,2),h=[p,q,z];
 assert(br(p,q).flat().every((v,i)=>v===z.flat()[i]),"Heisenberg bracket");
 assert(h.every(A=>h.every(B=>br(A,br(A,B)).flat().every(v=>v===0n))),"Heisenberg class two");
 assert(rank(h.map(A=>h.flatMap(B=>br(A,B).flat())))===2,"center dimension");
 return {models,fitting,normalizers,jordan,heisenberg:3};
}
console.log('AA-64 Cartan equivalence models: PASS',cartan64());
