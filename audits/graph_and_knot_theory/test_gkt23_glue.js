// GKT-23-GLUE-01: all paired sides of two triangles, with both endpoint bijections.
function run(){
 const assert=(x,m)=>{if(!x)throw Error(m)};
 const sides=Array.from({length:6},(_,i)=>[3*Math.floor(i/3)+i%3,3*Math.floor(i/3)+(i+1)%3]);
 function dsu(n){let a=Array.from({length:n},(_,i)=>i);function root(i){while(a[i]!==i)i=a[i];return i}return {root,join:(i,j)=>{a[root(i)]=root(j)}}}
 let models=0,sphere=0,torus=0,theta=0,linkChecks=0,disconnected=0;
 function check(P,mask){let v=dsu(6),l=dsu(12),dual=dsu(2),cross=0;
 // Each corner interval has two ends, one for each incident side.
 P.forEach(([a,b],k)=>{dual.join(a/3|0,b/3|0);if((a/3|0)!==(b/3|0))cross++;for(let t=0;t<2;t++){let u=t^((mask>>k)&1);v.join(sides[a][t],sides[b][u]);l.join(2*a+t,2*b+u)}});
 let L=new Map();for(let c=0;c<6;c++){let prev=3*(c/3|0)+(c%3+2)%3,e=[l.root(2*c),l.root(2*prev+1)],r=v.root(c);if(!L.has(r))L.set(r,[]);L.get(r).push(e)}
 for(let E of L.values()){let V=[...new Set(E.flat())];for(let x of V)assert(E.flat().filter(y=>y===x).length===2,"link degree two");let visited=new Set([V[0]]),Q=[V[0]];while(Q.length){let x=Q.pop();for(let e of E)if(e.includes(x))for(let y of e)if(!visited.has(y)){visited.add(y);Q.push(y)}}assert(visited.size===V.length,"corner link connected");linkChecks++}
 let chi=L.size-3+2;models++;if(cross===3){theta++;if(chi===2)sphere++;if(chi===0&&P.every(([a,b],k)=>((mask>>k)&1)===1))torus++}if(dual.root(0)!==dual.root(1))disconnected++;
 }
 function pair(S,P){if(!S.length){for(let mask=0;mask<8;mask++)check(P,mask);return}let a=S[0];for(let i=1;i<S.length;i++)pair(S.filter((_,j)=>j!==0&&j!==i),[...P,[a,S[i]]])}
 pair([0,1,2,3,4,5],[]);assert(models===120&&theta===48&&sphere>0&&torus>0,"coverage");return {models,theta,sphere,torus,linkChecks,disconnected};
}
console.log(JSON.stringify(run()));
