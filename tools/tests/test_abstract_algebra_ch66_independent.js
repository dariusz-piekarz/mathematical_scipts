// AA-66: exact block representations and equivariant splitting, independent of cocycle rank test.
function split66(){
 const assert=(v,m)=>{if(!v)throw Error(m)};
 const zero=(r,c)=>Array.from({length:r},()=>Array(c).fill(0n)),mul=(A,B)=>A.map(row=>B[0].map((_,j)=>row.reduce((s,x,k)=>s+x*B[k][j],0n))),sub=(A,B)=>A.map((row,i)=>row.map((x,j)=>x-B[i][j])),eq=(A,B)=>A.every((row,i)=>row.every((x,j)=>x===B[i][j])),tr=A=>A.reduce((s,row,i)=>s+row[i],0n);
 const ident=n=>{let a=zero(n,n);for(let i=0;i<n;i++)a[i][i]=1n;return a;};
 const neg=A=>A.map(r=>r.map(x=>-x)),add=(A,B)=>sub(A,neg(B));
 let models=0,relations=0,cocycles=0,sections=0,projectionChecks=0,nonzero=0,trace=0;
 for(let n=2;n<=4;n++){
  let generators=[];
  for(let i=0;i<n;i++)for(let j=0;j<n;j++)if(i!==j){let M=zero(n,n);M[i][j]=1n;generators.push(M);}
  for(let i=0;i<n-1;i++){let M=zero(n,n);M[i][i]=1n;M[i+1][i+1]=-1n;generators.push(M);}
  const dual=X=>X[0].map((_,j)=>X.map(row=>-row[j]));
  for(let type=0;type<3;type++)for(let seed=1;seed<=3;seed++){
   const u=n,w=type===2?1:n;
   const S=Array.from({length:u},(_,i)=>Array.from({length:w},(_,j)=>BigInt((i*7+j*3+seed*5)%11-5)));
   const W=X=>type===0?X:type===1?dual(X):zero(1,1);
   const delta=X=>sub(mul(X,S),mul(S,W(X)));
   const block=X=>{let R=zero(u+w,u+w),D=delta(X),Y=W(X);for(let i=0;i<u;i++){for(let j=0;j<u;j++)R[i][j]=X[i][j];for(let j=0;j<w;j++)R[i][u+j]=D[i][j];}for(let i=0;i<w;i++)for(let j=0;j<w;j++)R[u+i][u+j]=Y[i][j];return R;};
   // Actual splitting section is (-S,I), projection is (I,S).
   const J=[...neg(S),...ident(w)],P=ident(u).map((row,i)=>[...row,...S[i]]);
   assert(eq(mul(P,J),zero(u,w)),"section in kernel");projectionChecks++;
   for(const X of generators){const R=block(X);assert(eq(mul(R,J),mul(J,W(X))),"section equivariance");sections++;assert(eq(mul(P,R),mul(X,P)),"projection equivariance");projectionChecks++;
    if(delta(X).some(r=>r.some(x=>x)))nonzero++;
    for(const Y of generators){let Z=sub(mul(X,Y),mul(Y,X));assert(eq(sub(mul(R,block(Y)),mul(block(Y),R)),block(Z)),"bracket");relations++;
     let lhs=sub(mul(X,delta(Y)),mul(delta(Y),W(X))),rhs=sub(mul(Y,delta(X)),mul(delta(X),W(Y)));assert(eq(sub(lhs,rhs),delta(Z)),"cocycle");cocycles++;
    }
   }models++;
  }
  for(const X of generators)for(const Y of generators){assert(tr(sub(mul(X,Y),mul(Y,X)))===0n,"trace commutator");trace++;}
 }
 // Nonsemisimple Jordan block: every section (a,1) has image (1,0) under x.
 for(let a=-12;a<=12;a++){const X=[[0n,1n],[0n,0n]],J=[[BigInt(a)],[1n]];assert(!eq(mul(X,J),zero(2,1)),"nonsplit counterexample");}
 return {models,relations,cocycles,sections,projectionChecks,nonzero,trace,nonsplit:25};
}
console.log('AA-66 splitting extensions: PASS',split66());
