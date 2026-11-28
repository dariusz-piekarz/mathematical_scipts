// GKT-20-LOCAL-01: relative cone chains over finite fields, independently of the link criterion.
// Tests combinatorial local models, not a formal proof of excision.
function run(){
 const assert=(x,m)=>{if(!x)throw Error(m)}, key=s=>s.join(",");
 function rank(A,p){if(!A.length)return 0;let M=A.map(r=>r.map(x=>(x%p+p)%p)),r=0;for(let j=0;j<M[0].length&&r<M.length;j++){let i=M.findIndex((a,i)=>i>=r&&a[j]!==0);if(i<0)continue;[M[i],M[r]]=[M[r],M[i]];let inv=1;while(M[r][j]*inv%p!==1)inv++;M[r]=M[r].map(x=>x*inv%p);for(let i=r+1;i<M.length;i++){let a=M[i][j];M[i]=M[i].map((x,k)=>(x-a*M[r][k]%p+p)%p)}r++}return r}
 function check(n,E,expected){let seen=new Set(),c=0;for(let v=0;v<n;v++)if(!seen.has(v)){c++;let S=[v];seen.add(v);while(S.length){let u=S.pop();for(let [a,b] of E){let w=a===u?b:b===u?a:-1;if(w>=0&&!seen.has(w)){seen.add(w);S.push(w)}}}}
 // Cone apex has label n, with base removed in relative chain groups.
 let C=[[[n]],Array.from({length:n},(_,i)=>[i,n]),E.map(e=>[...e,n])];
 function boundary(d){let rows=new Map(C[d-1].map((s,i)=>[key(s),i])),A=C[d-1].map(()=>C[d].map(()=>0));C[d].forEach((s,j)=>s.forEach((_,i)=>{let f=s.filter((_,h)=>h!==i),r=rows.get(key(f));if(r!==undefined)A[r][j]+=(-1)**i}));return A}
 let B=boundary(1),D=boundary(2);for(let i=0;i<B.length;i++)for(let j=0;j<C[2].length;j++)assert(B[i].reduce((s,x,k)=>s+x*D[k][j],0)===0,"relative boundary squared");
 for(let p of [2,3,5,7]){let r1=rank(B,p),r2=rank(D,p),b=[1-r1,n-r1-r2,E.length-r2];assert(b[0]===Number(n===0)&&b[1]===Math.max(c-1,0)&&b[2]===E.length-n+c,"cone relative homology");if(expected)assert(b.join(",")===expected.join(","),"local model");}
 }
 let graphs=0,disconnected=0,edgeModels=0;
 for(let n=0;n<=5;n++){let es=[];for(let a=0;a<n;a++)for(let b=a+1;b<n;b++)es.push([a,b]);for(let mask=0;mask<2**es.length;mask++){let E=es.filter((_,i)=>mask>>i&1);check(n,E);graphs++;}}
 // Suspension of k discrete points is K_{2,k}, the subdivided graph of k parallel arcs.
 for(let k=1;k<=16;k++){let E=[];for(let i=2;i<k+2;i++)E.push([0,i],[1,i]);check(k+2,E,[0,0,k-1]);edgeModels++}
 // Link consisting of r disjoint triangular circles: local H1 has rank r-1, H2 rank r.
 for(let r=1;r<=8;r++){let E=[];for(let i=0;i<r;i++)E.push([3*i,3*i+1],[3*i+1,3*i+2],[3*i,3*i+2]);check(3*r,E,[0,r-1,r]);disconnected++}
 return {graphs,edgeModels,cycleUnions:disconnected,fieldChecks:4*(graphs+edgeModels+disconnected)};
}
console.log(JSON.stringify(run()));
