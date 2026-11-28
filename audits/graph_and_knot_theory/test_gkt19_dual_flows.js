// GKT-19-DUAL-01: finite exhaustive sphere rotation systems (up to 3 edges)
// and exact modular flow/color counts, including q=4,6, loops and bridges.
// node audits/graph_and_knot_theory/test_gkt19_dual_flows.js
function run(){
 const assert=(x,m)=>{if(!x)throw Error(m)};
 function cycles(p){let idx=Array(p.length).fill(-1),n=0;for(let i=0;i<p.length;i++)if(idx[i]<0){let d=i;do{idx[d]=n;d=p[d]}while(d!==i);n++}return {idx,n}}
 function components(n,E,mask){let p=Array.from({length:n},(_,i)=>i);function root(x){while(p[x]!==x)x=p[x];return x}let k=n;E.forEach(([u,v],i)=>{if(mask>>i&1){let a=root(u),b=root(v);if(a!==b){p[a]=b;k--}}});return k}
 let total=0,planar=0,subsets=0,flowChecks=0,composite=0,loops=0,bridges=0,parallel=0;
 function inspect(n,E,f,F){
 const m=E.length,all=(1<<m)-1;total++;
 if(components(n,E,all)!==1||n-m+f!==2)return;
 planar++;assert(components(f,F,all)===1,"dual connectivity");
 loops+=E.some(([u,v])=>u===v);
 bridges+=E.some((_,i)=>components(n,E,all^(1<<i))>1);
 parallel+=new Set(E.map(([u,v])=>[Math.min(u,v),Math.max(u,v)].join(","))).size<m;
 let pc=new Map(),dc=new Map();function add(map,a,b){let k=a+","+b;map.set(k,(map.get(k)||0)+1)}
 for(let mask=0;mask<=all;mask++){
 let a=0;for(let x=mask;x;x>>=1)a+=x&1;
 let k=components(n,E,mask),kd=components(f,F,all^mask);
 let nu=a-n+k,nud=m-a-f+kd;
 assert(kd===1+nu&&nud===k-1,"complement subset rank-nullity");
 add(pc,k-1,nu);add(dc,nud,kd-1);subsets++;
 }
 assert(pc.size===dc.size&&[...pc].every(([k,v])=>dc.get(k)===v),"shifted Tutte coefficient duality");
 for(let q of [2,3,4,6]){
 let colors=0,flows=0;const c=Array(f).fill(0),j=Array(m).fill(0);
 function color(i){if(i===f){if(F.every(([u,v])=>c[u]!==c[v]))colors++;return}for(let a=0;a<q;a++){c[i]=a;color(i+1)}}
 function flow(i){if(i===m){let d=Array(n).fill(0);E.forEach(([u,v],e)=>{d[u]-=j[e];d[v]+=j[e]});if(d.every(x=>x%q===0))flows++;return}for(let a=1;a<q;a++){j[i]=a;flow(i+1)}}
 color(0);flow(0);assert(colors===q*flows,"flow-color count q="+q);flowChecks++;composite+=q===4||q===6;
 }
 }
 inspect(1,[],1,[]);
 function perm(s,k){if(k===s.length){let v=cycles(s),f=cycles(s.map((_,d)=>s[d^1]));let E=[],F=[];for(let i=0;i<s.length;i+=2){E.push([v.idx[i],v.idx[i+1]]);F.push([f.idx[i],f.idx[i+1]])}inspect(v.n,E,f.n,F);return}for(let i=k;i<s.length;i++){[s[k],s[i]]=[s[i],s[k]];perm(s,k+1);[s[k],s[i]]=[s[i],s[k]]}}
 for(let m=1;m<=3;m++)perm(Array.from({length:2*m},(_,i)=>i),0);
 assert(loops&&bridges&&parallel&&composite,"coverage");
 return {total,planar,subsets,flowChecks,composite,loops,bridges,parallel};
}
console.log(JSON.stringify(run()));
