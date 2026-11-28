// GKT-18-ROT-01: exact printed torus walks and all cyclic orders of K5 and K3,3.
// Finite combinatorial checks, not a topological proof. Run with Node.js.
function run(){
  const cases=[
    {name:"K5",r:[[2,3,4,5],[1,3,4,5],[1,2,5,4],[1,3,2,5],[1,4,2,3]],walks:[[1,2,3,5],[2,1,3,2,4,5],[3,1,4],[4,1,5],[4,2,5,3]]},
    {name:"K33",r:[[4,5,6],[4,5,6],[4,5,6],[1,2,3],[1,2,3],[1,2,3]],walks:[[1,4,2,5,3,6],[4,1,5,2,6,3],[5,1,6,2,4,3]]}
  ];
  function assert(b,m){if(!b)throw Error(m)}
  function faces(r){
    const next=new Map();
    for(let i=1;i<=r.length;i++)for(let j of r[i-1]){
      const order=r[j-1],p=order.indexOf(i);
      assert(p>=0,"nonreciprocal adjacency");
      next.set(`${i},${j}`,`${j},${order[(p+1)%order.length]}`);
    }
    const seen=new Set(),f=[];
    for(let d of next.keys()){
      if(seen.has(d))continue;
      const cycle=[];let x=d;
      do{assert(!seen.has(x)&&next.has(x),"not permutation");seen.add(x);cycle.push(x);x=next.get(x)}while(x!==d);
      f.push(cycle);
    }
    return f;
  }
  function perms(a){return a.length===0?[[]]:a.flatMap((x,i)=>perms(a.filter((_,j)=>j!==i)).map(p=>[x,...p]))}
  function canonical(w){return w.map((_,i)=>w.slice(i).concat(w.slice(0,i)).join(";")).sort()[0]}
  const out=[];
  for(const {name,r,walks} of cases){
    let f=faces(r),m=r.flat().length/2;
    assert(JSON.stringify(f.map(canonical).sort())===JSON.stringify(walks.map(w=>canonical(w.map((x,i)=>`${x},${w[(i+1)%w.length]}`))).sort()),"printed walks");
    assert(r.length-m+f.length===0,"torus");
    let rotations=0,minGenus=Infinity,torus=0;
    const opts=r.map(a=>perms(a.slice(1)).map(p=>[a[0],...p]));
    function scan(v,rs){
      if(v<opts.length){for(let a of opts[v])scan(v+1,[...rs,a]);return}
      const ff=faces(rs),g=(2-r.length+m-ff.length)/2;
      assert(Number.isInteger(g)&&g>=1,"genus lower bound");
      assert(ff.every(c=>c.length>=(name==="K33"?4:3)),"face length");
      if(name==="K33")assert(ff.every(c=>c.length%2===0),"bipartite parity");
      rotations++;minGenus=Math.min(minGenus,g);torus+=g===1;
    }
    scan(0,[]);
    out.push({name,printedFaces:f.length,darts:2*m,rotations,minGenus,torus});
  }
  return out;
}
console.log(JSON.stringify(run()));
