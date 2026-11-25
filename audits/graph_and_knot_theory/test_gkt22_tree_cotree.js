// GKT-22-TREE-COTREE-01: surface matching and exact integral reduced boundaries.
function run(){
 const assert=(v,m)=>{if(!v)throw Error(m)};let seed=206;
 const rnd=n=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed%n};
 function sh(a){a=[...a];for(let i=a.length-1;i>0;i--){let j=rnd(i+1);[a[i],a[j]]=[a[j],a[i]]}return a}
 const key=a=>[...a].sort((x,y)=>x-y).join(","),faces=t=>t.map((_,i)=>t.filter((_,j)=>i!==j));
 function periodic(n){let v=(i,j)=>(i%n)*n+j%n,F=[];for(let i=0;i<n;i++)for(let j=0;j<n;j++)F.push([v(i,j),v(i+1,j),v(i+1,j+1)],[v(i,j),v(i,j+1),v(i+1,j+1)]);return F}
 const cases=[["sphere",[[0,1,2],[0,1,3],[0,2,3],[1,2,3]],0],["RP2",["012","013","024","035","045","125","134","145","234","235"].map(s=>[...s].map(Number)),1],...([3,4,5].map(n=>["torus"+n,periodic(n),2]))];
 let models=0,pairs=0,torsion=0,zero=0,linkChecks=0;
 for(let [name,F,k] of cases){
 F=F.map(t=>t.sort((a,b)=>a-b));assert(new Set(F.map(key)).size===F.length,"distinct triangles");
 let V=[...new Set(F.flat())].sort((a,b)=>a-b),E=[...new Set(F.flatMap(t=>faces(t).map(key)))].sort(),ev=E.map(s=>s.split(",").map(Number)),fi=F.map(t=>faces(t).map(key)),ef=E.map(e=>fi.flatMap((a,i)=>a.includes(e)?[i]:[]));assert(ef.every(a=>a.length===2),"two incident triangles");
 for(let v of V){let ls=F.filter(t=>t.includes(v)).map(t=>t.filter(w=>w!==v)),lv=[...new Set(ls.flat())];assert(lv.every(w=>ls.filter(e=>e.includes(w)).length===2),"link degree");let seen=new Set([lv[0]]),Q=[lv[0]];while(Q.length){let x=Q.pop();for(let e of ls)if(e.includes(x))for(let y of e)if(!seen.has(y)){seen.add(y);Q.push(y)}}assert(seen.size===lv.length,"link connected");linkChecks++}
 function tree(vertices,edges,root){let visited=new Set([root]),Q=[root],P=[];while(Q.length){let a=Q.shift();for(let e of sh(edges.filter(e=>e.a===a||e.b===a))){let b=e.a===a?e.b:e.a;if(!visited.has(b)){visited.add(b);Q.push(b);P.push([b,e.id])}}}assert(visited.size===vertices.length,"spanning");return P}
 for(let trial=0;trial<24;trial++){
 let pv=tree(V,ev.map(([a,b],id)=>({a,b,id})),V[rnd(V.length)]),used=new Set(pv.map(e=>e[1]));
 let pt=tree(F.map((_,i)=>i),ef.map(([a,b],id)=>({a,b,id})).filter(e=>!used.has(e.id)),rnd(F.length));
 let C=[V.map(v=>String(v)),E.slice(),F.map(key)],D=[[],V.map(v=>ev.map(([a,b])=>v===a?-1:v===b?1:0)),E.map(e=>F.map(t=>{let i=faces(t).findIndex(f=>key(f)===e);return i<0?0:(-1)**i}))];
 let P=[pv.map(([v,e])=>[String(v),E[e]]),pt.map(([t,e])=>[E[e],key(F[t])])];assert(new Set(P.flat().flat()).size===2*(pv.length+pt.length),"matching");
 for(let d of (trial%2?[1,0]:[0,1])){
 let G=P[d].slice();while(G.length){let j=G.findIndex(([a,b])=>G.every(([x,y])=>x===a||D[d+1][C[d].indexOf(a)][C[d+1].indexOf(y)]===0));assert(j>=0,"acyclic triangular block");
 let [a,b]=G.splice(j,1)[0],i=C[d].indexOf(a),h=C[d+1].indexOf(b),A=D[d+1],l=A[i][h];assert(Math.abs(l)===1,"unit");
 D[d+1]=A.filter((_,z)=>z!==i).map(row=>row.flatMap((x,z)=>z===h?[]:[x-row[h]*A[i][z]/l]));
 if(d)D[d]=D[d].map(row=>row.filter((_,z)=>z!==i));if(d===0)D[2]=D[2].filter((_,z)=>z!==h);C[d].splice(i,1);C[d+1].splice(h,1);pairs++;
 for(let u=0;u<C[0].length;u++)for(let v=0;v<C[2].length;v++)assert(D[1][u].reduce((s,x,w)=>s+x*D[2][w][v],0)===0,"boundary square");
 }}
 assert(C.map(c=>c.length).join(",")===[1,k,1].join(","),"critical counts");assert(D[1].flat().every(x=>x===0),"zero d1");
 if(name==="RP2"){assert(Math.abs(D[2][0][0])===2,"torsion coefficient");torsion++}else{assert(D[2].flat().every(x=>x===0),"orientable d2 zero");zero++}models++;
 }}
 return {models,pairs,torsion,zero,linkChecks};
}
console.log(JSON.stringify(run()));
