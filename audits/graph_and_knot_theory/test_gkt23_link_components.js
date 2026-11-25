// GKT-23-LINK-COMPONENTS-01: arbitrary full side pairings, corner classes and dual components.
function run(){
 const assert=(v,m)=>{if(!v)throw Error(m)};let seed=212;
 const rnd=n=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;return (seed>>>8)%n};
 function dsu(n){let a=Array.from({length:n},(_,i)=>i);function root(i){while(a[i]!==i){a[i]=a[a[i]];i=a[i]}return i}return {root,join:(i,j)=>{a[root(i)]=root(j)}}}
 let models=0,links=0,loops=0,disconnected=0,extraIdentifications=0;
 function check(n,P){
  let N=3*n,v=dsu(N),l=dsu(2*N),dual=dsu(n),corner=(a,t)=>3*Math.floor(a/3)+(a%3+t)%3;
  for(let [a,b,f] of P){let A=Math.floor(a/3),B=Math.floor(b/3);if(A===B)loops++;dual.join(A,B);for(let t=0;t<2;t++){v.join(corner(a,t),corner(b,t^f));l.join(2*a+t,2*b+(t^f))}}
  let G=new Map();for(let c=0;c<N;c++){let prev=3*Math.floor(c/3)+(c%3+2)%3,r=v.root(c),e=[l.root(2*c),l.root(2*prev+1)];if(!G.has(r))G.set(r,[]);G.get(r).push(e)}
  function components(E){let A=new Map();for(let [a,b] of E){if(!A.has(a))A.set(a,[]);if(!A.has(b))A.set(b,[]);A.get(a).push(b);A.get(b).push(a)}assert([...A.values()].every(x=>x.length===2),"degree two");let seen=new Set(),k=0;for(let a of A.keys())if(!seen.has(a)){k++;let Q=[a];seen.add(a);while(Q.length)for(let b of A.get(Q.pop()))if(!seen.has(b)){seen.add(b);Q.push(b)}}return k}
  for(let E of G.values()){assert(components(E)===1,"connected vertex link");links++}
  let owner=new Map();for(let c=0;c<N;c++){let a=v.root(c),b=dual.root(Math.floor(c/3));if(owner.has(a))assert(owner.get(a)===b,"vertex classes do not cross dual components");owner.set(a,b)}
  if(new Set(Array.from({length:n},(_,i)=>dual.root(i))).size>1)disconnected++;
  let values=[...G.values()];if(values.length>1){assert(components([...values[0],...values[1]])===2,"extra vertex identification gives two-circle link");extraIdentifications++}
  models++;
 }
 for(let n of [2,4,6,8,12,20])for(let trial=0;trial<80;trial++){
  let P=[];let groups=trial%4===0?Array.from({length:n/2},(_,i)=>Array.from({length:6},(_,j)=>6*i+j)):[Array.from({length:3*n},(_,i)=>i)];
  for(let S of groups){for(let i=S.length-1;i>0;i--){let j=rnd(i+1);[S[i],S[j]]=[S[j],S[i]]}for(let i=0;i<S.length;i+=2)P.push([S[i],S[i+1],rnd(2)])}
  check(n,P);
 }
 assert(disconnected>0&&loops>0&&extraIdentifications>0,"coverage");return {models,links,loops,disconnected,extraIdentifications};
}
console.log(JSON.stringify(run()));
