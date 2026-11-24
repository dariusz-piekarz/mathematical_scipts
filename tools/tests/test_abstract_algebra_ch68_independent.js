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
