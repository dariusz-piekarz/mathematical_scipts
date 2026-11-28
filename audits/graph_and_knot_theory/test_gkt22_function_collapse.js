// GKT-22-FUNCTION-COLLAPSE-01: finite Morse function/matching and barycentric collapse checks.
function run(){
 const assert=(x,m)=>{if(!x)throw Error(m)},S=[1,2,3,4,5,6,7],pop=x=>[1,2,4].filter(k=>k&x).length;
 const I=S.flatMap(a=>S.filter(b=>(a&b)===a&&pop(b)===pop(a)+1).map(b=>[a,b]));
 function topo(P){let A=S.map(()=>[]),N=S.map(()=>0);for(let [a,b] of I){if(P.some(([x,y])=>x===a&&y===b))[a,b]=[b,a];A[a-1].push(b);N[b-1]++}let Q=S.filter(x=>N[x-1]===0),L=[];while(Q.length){let a=Q.pop();L.push(a);for(let b of A[a-1])if(--N[b-1]===0)Q.push(b)}return L}
 function pathCycle(P){function visit(a,seen){let pair=P.find(([x])=>x===a);if(!pair)return false;for(let [x,b] of I)if(b===pair[1]&&x!==a){if(seen.has(x)||visit(x,new Set([...seen,x])))return true}return false}return S.some(a=>visit(a,new Set([a])))}
 function fromF(F){return I.filter(([a,b])=>F[b-1]<=F[a-1])}
 function valid(F){return S.every(a=>I.filter(([x,y])=>x===a&&F[y-1]<=F[a-1]).length<=1&&I.filter(([x,y])=>y===a&&F[x-1]>=F[a-1]).length<=1)}
 let assignments=0,functions=0,withTies=0,matchings=0,acyclic=0,cyclic=0,collapsePoints=0,homotopies=0;
 for(let n=0;n<4**7;n++){let z=n,F=S.map(()=>{let x=z%4;z=Math.floor(z/4);return x});assignments++;if(!valid(F))continue;functions++;let P=fromF(F);assert(new Set(P.flat()).size===P.length*2,"no cell paired twice");assert(topo(P).length===7&&!pathCycle(P),"function acyclic");if(P.some(([a,b])=>F[a-1]===F[b-1]))withTies++}
 for(let n=0;n<2**I.length;n++){let P=I.filter((_,i)=>n&(1<<i));if(new Set(P.flat()).size!==P.length*2)continue;matchings++;let L=topo(P),cyc=pathCycle(P);assert(cyc===(L.length!==7),"cycle equivalence");if(cyc){cyclic++;continue}acyclic++;let F=S.map(a=>L.indexOf(a));assert(valid(F)&&JSON.stringify(fromF(F))===JSON.stringify(P),"matching round trip")}
 function compositions(n,k,prefix,fn){if(k===1){fn([...prefix,n]);return}for(let i=0;i<=n;i++)compositions(n-i,k-1,[...prefix,i],fn)}
 for(let p=0;p<=5;p++)compositions(6,p+2,[],T=>{let m=Math.min(...T.slice(0,-1));collapsePoints++;for(let j=0;j<=6;j++){let W=T.map((x,i)=>i<=p?6*x-j*m:6*x+(p+1)*j*m);assert(W.every(x=>x>=0)&&W.reduce((a,b)=>a+b,0)===36,"barycentric simplex");if(m===0||j===0)assert(W.every((x,i)=>x===6*T[i]),"fixed");if(j===6)assert(W.slice(0,-1).some(x=>x===0),"retraction target");homotopies++}});
 assert(cyclic>0&&withTies>0,"coverage");return {assignments,functions,withTies,matchings,acyclic,cyclic,collapsePoints,homotopies};
}
console.log(JSON.stringify(run()));
