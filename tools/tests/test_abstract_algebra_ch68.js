// AA-68-CH-01: aa:prz:lie-character-sl2; exact Laurent coefficients.
const assert=(x,m)=>{if(!x)throw Error(m)};
const add=(a,b,c=1n)=>{let r=new Map(a);for(const [k,v] of b){let z=(r.get(k)||0n)+c*v;if(z)r.set(k,z);else r.delete(k)}return r};
const mul=(a,b)=>{let r=new Map();for(const [k,v] of a)for(const [l,w] of b)r=add(r,new Map([[k+l,v*w]]));return r};
const eq=(a,b)=>a.size===b.size&&[...a].every(([k,v])=>b.get(k)===v);
const C=m=>new Map(Array.from({length:m+1},(_,i)=>[m-2*i,1n]));
let products=0,coefficients=0,virtual=0;
for(let a=0;a<=20;a++)for(let b=0;b<=20;b++){
 const p=mul(C(a),C(b));let q=new Map();
 for(let j=0;j<=Math.min(a,b);j++)q=add(q,C(a+b-2*j));
 assert(eq(p,q),"tensor decomposition");
 assert([...p.values()].reduce((s,x)=>s+x,0n)===BigInt((a+1)*(b+1)),"augmentation");
 for(const [k,v] of p){assert(p.get(-k)===v,"reflection");coefficients++}
 products++;
}
for(let n=0;n<=30;n++){
 let f=new Map();for(let k=0;k<=n;k++){let c=BigInt((k%5)-2);if(c)f=add(f,C(k),c)}
 let g=new Map(f),out=new Map();while(g.size){
  let h=Math.max(...g.keys());assert(h>=0,"dominance");
  let c=g.get(h);out=add(out,new Map([[h,c]]));g=add(g,C(h),-c);
 }
 let expected=new Map();for(let k=0;k<=n;k++)if(k%5!==2)expected.set(k,BigInt(k%5-2));
 assert(eq(out,expected),"virtual triangular recovery");virtual++;
}
console.log("AA-68-CH-01: PASS",{products,coefficients,virtual});
