// Exact independent AA-59 regression, no SymPy dependency.
function checkAA59(){
 const assert=(v)=>{if(!v)throw Error("AA-59 regression failed")};
 const zero=n=>Array.from({length:n},()=>Array(n).fill(0n));
 const E=(n,i,j)=>{const A=zero(n);A[i][j]=1n;return A};
 const add=(A,B)=>A.map((r,i)=>r.map((x,j)=>x+B[i][j]));
 const scale=(A,k)=>A.map(r=>r.map(x=>x*k));
 const mul=(A,B)=>A.map(r=>B[0].map((_,j)=>r.reduce((s,x,k)=>s+x*B[k][j],0n)));
 const bracket=(A,B)=>add(mul(A,B),scale(mul(B,A),-1n));
 const eq=(A,B)=>A.every((r,i)=>r.every((x,j)=>x===B[i][j]));
 const tr=A=>A.reduce((s,r,i)=>s+r[i],0n);
 let models=0,triples=0,pairs=0,jordan=0;
 for(let n=2;n<=5;n++){
  const I=zero(n);for(let i=0;i<n;i++)I[i][i]=1n;
  const H=zero(n);for(let i=0;i<n;i++)H[i][i]=BigInt(2*i-n+1);
  const units=[];for(let i=0;i<n;i++)for(let j=0;j<n;j++)units.push([i,j,E(n,i,j)]);
  for(const a of [-2n,1n,3n]){
   const A=scale(E(n,0,n-1),a), B=E(n,n-1,0);
   const P=mul(add(I,A),add(I,B)),Q=mul(add(I,scale(B,-1n)),add(I,scale(A,-1n)));
   assert(eq(mul(P,Q),I));assert(eq(mul(Q,P),I));
   const C=X=>mul(mul(P,X),Q), HC=C(H);
   const es=units.filter(([i,j])=>i!==j).map(([i,j,X])=>[i,j,C(X)]);
   const hs=Array.from({length:n-1},(_,i)=>C(add(E(n,i,i),scale(E(n,i+1,i+1),-1n))));
   const basis=[...hs,...es.map(r=>r[2])];
   // Distinct eigenvalues of H ensure the zero weight space is precisely diagonal.
   assert(new Set(H.map((r,i)=>r[i])).size===n);
   assert(hs.every(X=>eq(bracket(HC,X),zero(n))));
   const killing=(X,Y)=>units.reduce((v,[i,j,U])=>v+bracket(X,bracket(Y,U))[i][j],0n);
   for(const [i,j,X] of es){
    assert(eq(bracket(HC,X),scale(X,BigInt(2*(i-j)))));
    const Y=es.find(([k,l])=>k===j&&l===i)[2];
    const T=C(add(E(n,i,i),scale(E(n,j,j),-1n)));
    assert(eq(bracket(X,Y),T));assert(eq(bracket(T,X),scale(X,2n)));assert(eq(bracket(T,Y),scale(Y,-2n)));triples++;
    for(const [k,l,Z] of es){
     const W=bracket(X,Z);
     assert(eq(bracket(HC,W),scale(W,BigInt(2*(i-j+k-l)))));
     const K=killing(X,Z);assert(K===BigInt(2*n)*tr(mul(X,Z)));
     assert(K===BigInt(i===l&&j===k?2*n:0));pairs++;
    }
   }
   if(n>=3){
    const S=zero(n);S[0][0]=S[1][1]=1n;S[2][2]=-2n;
    const SC=C(S),NC=C(E(n,0,1));assert(eq(bracket(SC,NC),zero(n)));
    for(const X of basis){
     assert(eq(bracket(NC,bracket(NC,bracket(NC,X))),zero(n)));
     assert(eq(bracket(SC,bracket(NC,X)),bracket(NC,bracket(SC,X))));jordan++;
    }
   }
   models++;
  }
 }
 return {models,triples,pairs,jordan};
}
console.log('AA-59 exact conjugated models: PASS',checkAA59());
