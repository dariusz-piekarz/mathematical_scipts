// AA-62: independent suffix-weight formula on free words, BigInt.
function moduleAudit62(){
 const assert=(v,m)=>{if(!v)throw Error(m)};
 const models=[[[2,-1],[-1,2]],[[2,-2],[-1,2]],[[2,-3],[-1,2]],[[2,0],[0,2]],[[2,-1,0],[-1,2,-1],[0,-1,2]]];
 let words=0,basic=0,serre=0,preservation=0;
 const add=(u,v,c=1n)=>{const out=new Map(u);for(const [w,a] of v){const b=(out.get(w)||0n)+c*a;if(b)out.set(w,b);else out.delete(w);}return out};
 const scale=(u,c)=>add(new Map(),u,c), basis=w=>new Map([[w,1n]]);
 const eq=(u,v)=>u.size===v.size&&[...u].every(([w,a])=>v.get(w)===a);
 const bracket=(P,Q)=>v=>add(P(Q(v)),Q(P(v)),-1n);
 for(const A of models)for(const l of [0,1,3]){
  const r=A.length,lambda=Array.from({length:r},(_,i)=>BigInt(l-i));
  const H=Array.from({length:r},(_,i)=>v=>{const out=new Map();for(const [w,a] of v){let b=lambda[i];for(const c of w)b-=BigInt(A[i][Number(c)]);if(a*b)out.set(w,a*b);}return out;});
  const F=Array.from({length:r},(_,i)=>v=>new Map([...v].map(([w,a])=>[String(i)+w,a])));
  // Independent closed formula: remove each occurrence of i; coefficient is the H_i weight of its suffix.
  const E=Array.from({length:r},(_,i)=>v=>{let out=new Map();for(const [w,a] of v)for(let k=0;k<w.length;k++)if(Number(w[k])===i){let b=lambda[i];for(let q=k+1;q<w.length;q++)b-=BigInt(A[i][Number(w[q])]);out=add(out,basis(w.slice(0,k)+w.slice(k+1)),a*b);}return out;});
  const cases=[""];for(let j=0;j<cases.length;j++)if(cases[j].length<4)for(let i=0;i<r;i++)cases.push(cases[j]+i);
  const pos=[],neg=[];
  for(let i=0;i<r;i++)for(let j=0;j<r;j++)if(i!==j){let P=E[j],N=F[j];for(let k=0;k<1-A[i][j];k++){P=bracket(E[i],P);N=bracket(F[i],N);}pos.push(P);neg.push(N);}
  for(const w of cases){const v=basis(w);words++;
   for(let i=0;i<r;i++)for(let j=0;j<r;j++){
    assert(!bracket(H[i],H[j])(v).size,"HH");
    assert(eq(bracket(H[i],F[j])(v),scale(F[j](v),BigInt(-A[i][j]))),"HF");
    assert(eq(bracket(H[i],E[j])(v),scale(E[j](v),BigInt(A[i][j]))),"HE");
    assert(eq(bracket(E[i],F[j])(v),i===j?H[i](v):new Map()),"EF");basic+=4;
   }
   for(const P of pos){assert(!P(v).size,"positive Serre on T");serre++;}
   for(const N of neg)for(const e of E){assert(!bracket(e,N)(v).size,"negative relation stability");preservation++;}
  }
 }
 return {models:models.length,weights:3,words,basic,serre,preservation};
}
console.log('AA-62 highest weight module: PASS',moduleAudit62());
