// GKT-17-MINOR-01: finite path-branch-set models of K5 and K3,3.
// Run: node audits/graph_and_knot_theory/test_gkt17_minor_subdivision.js
// Checks witness edges, distinct paths, intersections and degrees; not a general proof.
function run(){
  const K5=Array.from({length:5},(_,i)=>Array.from({length:5},(_,j)=>j).filter(j=>j!==i));
  const K33=Array.from({length:6},(_,i)=>i<3?[3,4,5]:[0,1,2]);
  let totals={models:0,k5:0,k33:0,split:0,zero:0,coincident:0};
  const key=(a,b)=>a<b?`${a}:${b}`:`${b}:${a}`;
  const check=(H,patterns)=>{
    let next=0,edges=new Set(),groups=[],term=new Map();
    const add=(a,b)=>{if(a===b)throw Error("loop");edges.add(key(a,b))};
    for(let h=0;h<H.length;h++){
      let [size,labels]=patterns[h],g=Array.from({length:size},()=>next++);
      groups.push(g);
      for(let i=1;i<size;i++)add(g[i-1],g[i]);
      H[h].forEach((j,i)=>term.set(`${h}:${j}`,g[labels[i]]));
      if(new Set(labels).size<labels.length)totals.coincident++;
    }
    for(let h=0;h<H.length;h++)for(let j of H[h])if(h<j)add(term.get(`${h}:${j}`),term.get(`${j}:${h}`));
    function construct(M){
      let selected=new Set(),paths=[],centers=[];
      function treePath(g,a,b){let i=g.indexOf(a),j=g.indexOf(b);if(i<0||j<0)throw Error("endpoint");return i<=j?g.slice(i,j+1):g.slice(j,i+1).reverse()}
      for(let h=0;h<M.length;h++){
        let g=M[h].nodes,ts=M[h].adj.map(x=>x[1]);
        let z=g.find(z=>{let seen=new Set();for(let a of ts)for(let p of treePath(g,z,a).slice(1)){if(seen.has(p))return false;seen.add(p)}return true});
        if(z===undefined)return {split:h};
        centers.push(z);
      }
      for(let h=0;h<M.length;h++)for(let [j,a,b] of M[h].adj)if(h<j){
        let p=treePath(M[h].nodes,centers[h],a),q=treePath(M[j].nodes,b,centers[j]);
        if(p.length===1||q.length===1)totals.zero++;
        let path=p.concat(q);
        if(new Set(path).size!==path.length||path.length<2)throw Error("not simple");
        for(let k=1;k<path.length;k++){let e=key(path[k-1],path[k]);if(!edges.has(e)||selected.has(e))throw Error("invalid or shared edge");selected.add(e)}
        paths.push([h,j,path]);
      }
      for(let i=0;i<paths.length;i++)for(let j=0;j<i;j++){
        let [a,b,p]=paths[i],[c,d,q]=paths[j],common=p.filter(x=>q.includes(x)),expected=[a,b].filter(x=>x===c||x===d).map(x=>centers[x]);
        if(common.length!==expected.length||common.some(x=>!expected.includes(x)))throw Error("wrong intersection");
      }
      let deg=new Map();for(let e of selected)for(let v of e.split(":").map(Number))deg.set(v,(deg.get(v)||0)+1);
      for(let [v,d] of deg){let i=centers.indexOf(v);if(d!==(i<0?2:M[i].adj.length))throw Error("degree")}
      if(centers.length===5&&paths.length===10)totals.k5++;else if(centers.length===6&&paths.length===9)totals.k33++;else throw Error("wrong graph");
      return {};
    }
    let M=groups.map((nodes,h)=>({nodes,adj:H[h].map(j=>[j,term.get(`${h}:${j}`),term.get(`${j}:${h}`)])}));
    let result=construct(M);
    if(result.split!==undefined){
      if(H.length!==5)throw Error("cubic split");
      totals.split++;
      let h=result.split,g=groups[h],cut=-1;
      for(let i=1;i<g.length;i++)if(H[h].filter(j=>g.slice(0,i).includes(term.get(`${h}:${j}`))).length===2){cut=i;break}
      if(cut<0)throw Error("missing cut");
      let U=g.slice(0,cut),W=g.slice(cut),left=H[h].filter(j=>U.includes(term.get(`${h}:${j}`))),right=H[h].filter(j=>W.includes(term.get(`${h}:${j}`)));
      let A=[U,...right.map(j=>groups[j])],B=[W,...left.map(j=>groups[j])],G=A.concat(B);
      let N=G.map(nodes=>({nodes,adj:[]}));
      for(let i=0;i<3;i++)for(let j=3;j<6;j++){
        let witness;
        for(let a of G[i])for(let b of G[j])if(edges.has(key(a,b)))witness=[a,b];
        if(!witness)throw Error("missing K33 witness");
        let [a,b]=witness;N[i].adj.push([j,a,b]);N[j].adj.push([i,b,a]);
      }
      if(construct(N).split!==undefined)throw Error("split after K33");
    }
    totals.models++;
  };
  for(let H of [K5,K33]){
    let base=H.map(ns=>[1,ns.map(()=>0)]);
    check(H,base);
    for(let h=0;h<H.length;h++)for(let size=1;size<=4;size++){
      function enumerate(t){if(t.length===H[h].length){let ps=base.slice();ps[h]=[size,t];check(H,ps);return}for(let i=0;i<size;i++)enumerate(t.concat(i))}
      enumerate([]);
    }
    let state=17;function rnd(n){state=(Math.imul(state,1664525)+1013904223)>>>0;return state%n}
    for(let i=0;i<500;i++)check(H,H.map(ns=>{let size=1+rnd(4);return [size,ns.map(()=>rnd(size))]}));
  }
  if(!totals.k5||!totals.k33||!totals.split||!totals.zero||!totals.coincident)throw Error("coverage");
  return totals;
}
console.log(JSON.stringify(run()));
