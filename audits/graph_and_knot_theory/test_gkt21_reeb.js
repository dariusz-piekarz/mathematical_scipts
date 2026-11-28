// GKT-21-REEB-01: finite combinatorial models of orientable Morse bands.
// Tests degree counts and Euler characteristic, not the topological quotient proof.
function run(){
 const assert=(x,m)=>{if(!x)throw Error(m)};
 let cases=0,connected=0,cycles=0,parallel=0,steps=0,subdivisions=0;
 function check(seq){
 let V=[],E=[],live=[],chi=0;
 for(let type of seq){let id=V.length;V.push(type);if(type==="birth"){live.push(id);chi++}else if(type==="split"){E.push([live.shift(),id]);live.push(id,id);chi--}else if(type==="merge"){E.push([live.shift(),id],[live.shift(),id]);live.push(id);chi--}else{E.push([live.shift(),id]);chi++}}
 assert(live.length===0,"closed band sequence");let deg=V.map(()=>0),adj=V.map(()=>[]);for(let [a,b] of E){assert(a<b,"height increases");deg[a]++;deg[b]++;adj[a].push(b);adj[b].push(a)}
 assert(deg.every((d,i)=>d===(V[i]==="birth"||V[i]==="death"?1:3)),"local degrees");
 let seen=new Set(),k=0;for(let i=0;i<V.length;i++)if(!seen.has(i)){k++;let S=[i];seen.add(i);while(S.length)for(let j of adj[S.pop()])if(!seen.has(j)){seen.add(j);S.push(j)}}
 let beta=E.length-V.length+k;assert(beta===k-chi/2&&beta>=0,"Euler and cycle rank");
 let P=V.map((_,i)=>i);function root(i){while(P[i]!==i)i=P[i];return i}let r=0;for(let [a,b] of E){let u=root(a),v=root(b);if(u===v)r++;else P[u]=v}assert(r===beta,"forest cycle rank");
 let W=[...E].flatMap(([a,b],i)=>[[a,V.length+i],[V.length+i,b]]);assert(W.length-(V.length+E.length)+k===beta,"subdivision");subdivisions+=E.length;
 cases++;steps+=V.length;if(k===1){connected++;cycles+=beta;assert(beta===(2-chi)/2,"connected genus formula")}if(new Set(E.map(e=>e.join(","))).size<E.length)parallel++;
 }
 function go(seq,n){if(seq.length&&n===0)check(seq);if(seq.length===8)return;go([...seq,"birth"],n+1);if(n>0){go([...seq,"split"],n+1);go([...seq,"death"],n-1)}if(n>=2)go([...seq,"merge"],n-1)}
 go([],0);assert(connected>0&&parallel>0&&cycles>0,"coverage");return {cases,connected,cycles,parallel,steps,subdivisions};
}
console.log(JSON.stringify(run()));
