// GKT-19-REC-01: exhaustive multigraphs with up to 4 vertices and 5 edges.
// Compare subset coefficients with deletion/contraction and direct coloring/forest counts.
// Coefficients are in u=x-1,v=y-1. Run from repo root with Node.
function run(){
 const assert=(x,m)=>{if(!x)throw Error(m)};
 const add=(p,a,b,c=1)=>{let k=a+","+b;p.set(k,(p.get(k)||0)+c)};
 function rank(n,E,mask){let p=Array.from({length:n},(_,i)=>i),k=n,forest=true,size=0;function root(x){while(p[x]!==x)x=p[x];return x}E.forEach(([u,v],i)=>{if(mask>>i&1){size++;let a=root(u),b=root(v);if(a===b)forest=false;else{p[a]=b;k--}}});return {k,forest,size}}
 function poly(n,E){let p=new Map(),all=(1<<E.length)-1,c=rank(n,E,all).k;for(let mask=0;mask<=all;mask++){let r=rank(n,E,mask);add(p,r.k-c,r.size-n+r.k)}return p}
 function shift(p,a,b){let z=new Map(p);for(let [k,c] of p){let [i,j]=k.split(",").map(Number);add(z,i+a,j+b,c)}return z}
 function sum(p,q){let z=new Map(p);for(let [k,c] of q){let [i,j]=k.split(",").map(Number);add(z,i,j,c)}return z}
 function equal(p,q){return p.size===q.size&&[...p].every(([k,c])=>q.get(k)===c)}
 function value(p,x,y){let z=0;for(let [k,c] of p){let [i,j]=k.split(",").map(Number);z+=c*(x-1)**i*(y-1)**j}return z}
 let graphs=0,subsets=0,rec=0,loop=0,bridge=0,ordinary=0,colorChecks=0,disconnected=0,forests=0;
 function inspect(n,E){graphs++;let p=poly(n,E),all=(1<<E.length)-1,c=rank(n,E,all).k;disconnected+=c>1;let f=0,t=0;
 for(let m=0;m<=all;m++){let r=rank(n,E,m);if(r.forest){f++;if(r.k===c)t++}subsets++}
 assert(value(p,2,2)===all+1&&value(p,2,1)===f&&value(p,1,1)===t,"specializations");forests+=f;
 for(let i=0;i<E.length;i++){let [u,v]=E[i],D=E.filter((_,j)=>i!==j),pd=poly(n,D),rhs;
 if(u===v){loop++;rhs=shift(pd,0,1)}else{let map=x=>{if(x===v)x=u;return x>v?x-1:x};let C=D.map(([a,b])=>[map(a),map(b)]),pc=poly(n-1,C);if(rank(n,D,(1<<D.length)-1).k>c){bridge++;rhs=shift(pc,1,0)}else{ordinary++;rhs=sum(pd,pc)}}assert(equal(p,rhs),"recursion");rec++}
 for(let q of [1,2,3,4]){let a=Array(n).fill(0),cnt=0;function go(i){if(i===n){if(E.every(([u,v])=>a[u]!==a[v]))cnt++;return}for(let j=0;j<q;j++){a[i]=j;go(i+1)}}go(0);assert(cnt===(-1)**(n-c)*q**c*value(p,1-q,0),"chromatic");colorChecks++}
 }
 for(let n=0;n<=4;n++){let edges=[];for(let u=0;u<n;u++)for(let v=u;v<n;v++)edges.push([u,v]);function enumerate(E,start){inspect(n,E);if(E.length===5)return;for(let i=start;i<edges.length;i++)enumerate([...E,edges[i]],i)}enumerate([],0)}
 assert(loop&&bridge&&ordinary&&disconnected,"coverage");return {graphs,subsets,rec,loop,bridge,ordinary,colorChecks,disconnected,forests};
}
console.log(JSON.stringify(run()));
