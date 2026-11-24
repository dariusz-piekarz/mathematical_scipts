// AA-68-CH-02: aa:tw:lie-character-operations; A2 polynomial and dual models.
const assert=(x,m)=>{if(!x)throw Error(m)};
const wt=[[1,0],[-1,1],[0,-1]],key=(a,b)=>a+","+b;
function sym(n,sign=1){const c=new Map();for(let i=0;i<=n;i++)for(let j=0;j<=n-i;j++){let k=n-i-j;const x=sign*(i-j),y=sign*(j-k);const s=key(x,y);c.set(s,(c.get(s)||0n)+1n)}return c}
function mul(a,b){let c=new Map();for(const [s,v] of a)for(const [t,w] of b){const [x,y]=s.split(",").map(Number),[u,z]=t.split(",").map(Number),k=key(x+u,y+z);c.set(k,(c.get(k)||0n)+v*w)}return c}
let models=0,products=0,reflections=0,weights=0;
function check(c){for(const [s,v] of c){const [x,y]=s.split(",").map(Number);assert(c.get(key(-x,y+x))===v,"s1");assert(c.get(key(x+y,-y))===v,"s2");reflections+=2;weights++}}
for(let n=0;n<=10;n++){const a=sym(n),b=sym(n,-1);check(a);check(b);for(const [s,v] of a){const [x,y]=s.split(",").map(Number);assert(b.get(key(-x,-y))===v,"dual")};models+=2;
 for(let m=0;m<=10;m++){const c=mul(a,sym(m,-1));check(c);
 const dim=BigInt((n+1)*(n+2)*(m+1)*(m+2)/4);
 assert([...c.values()].reduce((s,x)=>s+x,0n)===dim,"augmentation");
 assert(c.get(key(n,m))===1n,"highest multiplicity");
 for(const s of c.keys()){const [x,y]=s.split(",").map(Number),p=n-x,q=m-y;assert((2*p+q)%3===0&&(p+2*q)%3===0&&2*p+q>=0&&p+2*q>=0,"root cone")}
 products++;
 }
}
console.log("AA-68-CH-02: PASS",{models,products,reflections,weights});

// AA-68-CH-03: aa:tw:lie-character-basis, reducible A1 x A1.
// Twice the height is p+q; odd heights and tied maxima must be handled.
// Independent invariant inputs are signed combinations of orbit sums.
function triangularProduct68(){
 const key=(p,q)=>p+","+q;
 const coord=s=>s.split(",").map(Number);
 const height=s=>coord(s).reduce((a,b)=>a+b,0);
 const add=(f,s,c)=>{const v=(f.get(s)||0n)+c;if(v)f.set(s,v);else f.delete(s)};
 const C=(a,b)=>{const f=new Map();for(let i=0;i<=a;i++)for(let j=0;j<=b;j++)f.set(key(a-2*i,b-2*j),1n);return f};
 const orbit=(a,b)=>new Set([key(a,b),key(-a,b),key(a,-b),key(-a,-b)]);
 const same=(a,b)=>a.size===b.size&&[...a].every(([s,c])=>b.get(s)===c);
 let cases=0,steps=0,ties=0,oddHeights=0,negative=0,zero=0;
 function recover(input){
  const f=new Map(input),out=new Map();
  let previousHeight=Infinity,previousCount=Infinity;
  while(f.size){
   const h=Math.max(...[...f.keys()].map(height));
   const maxima=[...f.keys()].filter(s=>height(s)===h);
   assert(h>=0&&maxima.every(s=>coord(s).every(x=>x>=0)),"maxima dominant");
   assert(h<previousHeight||(h===previousHeight&&maxima.length<previousCount),"termination measure");
   previousHeight=h;previousCount=maxima.length;
   if(maxima.length>1)ties++;
   if(h%2)oddHeights++;
   const s=maxima[0],c=f.get(s),[a,b]=coord(s);
   if(c<0n)negative++;
   add(out,s,c);
   for(const [t,v] of C(a,b))add(f,t,-c*v);
   assert(!f.has(s),"highest coefficient not cancelled");
   for(const [t,v] of f){const [p,q]=coord(t);assert(f.get(key(-p,q))===v&&f.get(key(p,-q))===v,"invariance lost");}
   steps++;
  }
  const rebuilt=new Map();
  for(const [s,c] of out){const [a,b]=coord(s);for(const [t,v] of C(a,b))add(rebuilt,t,c*v)}
  assert(same(rebuilt,input),"reconstruction");
  return out;
 }
 for(let n=0;n<=8;n++)for(let seed=0;seed<12;seed++){
  const f=new Map();
  for(let a=0;a<=n;a++)for(let b=0;b<=n-a;b++){
   const c=BigInt(((a*7+b*3+seed*5)%9)-4);
   for(const s of orbit(a,b))add(f,s,c);
  }
  const out=recover(f);
  // Independent finite-difference inverse of the rectangular weight sums.
  const expected=new Map();
  const at=(a,b)=>f.get(key(a,b))||0n;
  for(let a=0;a<=n;a++)for(let b=0;b<=n;b++)
   add(expected,key(a,b),at(a,b)-at(a+2,b)-at(a,b+2)+at(a+2,b+2));
  assert(same(out,expected),"unique coefficients via finite differences");
  if(!f.size)zero++;
  cases++;
 }
 assert(ties>0&&oddHeights>0&&negative>0&&zero>0,"missing edge cases");
 return {cases,steps,ties,oddHeights,negative,zero};
}
console.log("AA-68-CH-03: PASS",triangularProduct68());
