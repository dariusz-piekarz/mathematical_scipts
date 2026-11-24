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

// Additional exact quotient dimensions, independent of operator recursion.
function quotient62(){
 const assert=(v,m)=>{if(!v)throw Error(m)};
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b)[a,b]=[b,a%b];return a};
 const words=n=>Array.from({length:2**n},(_,i)=>n?i.toString(2).padStart(n,"0"):"");
 const choose=(n,k)=>{let c=1n;for(let j=1;j<=k;j++)c=c*BigInt(n-j+1)/BigInt(j);return c};
 const models=[["A1+A1",0,0,[1,1]],["A2",-1,-1,[1,1,2]],["B2",-2,-1,[1,1,2,3]],["G2",-3,-1,[1,1,2,3,4,5]]];
 const out=[];let rows=0;
 for(const [name,a,b,heights] of models){
  const rels=[[0,1,1-a],[1,0,1-b]].map(([i,j,m])=>Array.from({length:m+1},(_,k)=>[String(i).repeat(m-k)+j+String(i).repeat(k),choose(m,k)*(k%2?-1n:1n)]));
  const max=7,expected=Array(max+1).fill(0n);expected[0]=1n;
  for(const h of heights)for(let k=h;k<=max;k++)expected[k]+=expected[k-h];
  const dimensions=[];
  for(let n=0;n<=max;n++){
   const W=words(n),idx=new Map(W.map((w,i)=>[w,i])),basis=[];
   function insert(v){for(const [p,w] of basis){if(!v[p])continue;const a=w[p],b=v[p];v=v.map((x,i)=>a*x-b*w[i]);const d=v.reduce(gcd,0n);if(d)v=v.map(x=>x/d);}const p=v.findIndex(x=>x!==0n);if(p>=0)basis.push([p,v]);}
   for(const R of rels){const len=R[0][0].length;for(let l=0;l<=n-len;l++)for(const u of words(l))for(const w of words(n-len-l)){let v=Array(W.length).fill(0n);for(const [s,c] of R)v[idx.get(u+s+w)]+=c;insert(v);rows++;}}
   const dim=W.length-basis.length;assert(BigInt(dim)===expected[n],`${name}, degree ${n}: ${dim} != ${expected[n]}`);dimensions.push(dim);
  }out.push({name,dimensions});
 }
 return {rows,models:out};
}
console.log('AA-62 associative quotient dimensions: PASS',quotient62());
