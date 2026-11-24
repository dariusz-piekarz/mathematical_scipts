// GKT-17-CONTRACT-02. Run: node audits/graph_and_knot_theory/test_gkt17_contraction_descent.js
// All labelled simple graphs with 5 or 6 vertices, plus 20000 deterministic samples on 7 vertices (possible repeats); filters to 3-connected graphs.
// Checks the contraction criterion and strict descent for overlapping separators.
// Finite test, not a general proof or Lean verification.
function run(){
 let graphs=0,edges=0,bad=0,good=0,triples=0,descents=0,overlap=0,inside=0,outside=0;
 const bit=i=>1<<i;
 const assert=(p,msg)=>{if(!p)throw Error(msg)};
 for(let n=5;n<=7;n++){
  let full=(1<<n)-1, all=[];for(let i=0;i<n;i++)for(let j=i+1;j<n;j++)all.push([i,j]);
  function comps(adj,mask){let result=[];while(mask){let reached=mask&-mask,front=reached;while(front){let v=front&-front;front^=v;let newV=adj[31-Math.clz32(v)]&mask&~reached;reached|=newV;front|=newV}result.push(reached);mask&=~reached}return result}
  function connected(adj){let m=(1<<adj.length)-1;for(let a=0;a<adj.length;a++)for(let b=a+1;b<adj.length;b++)if(comps(adj,m&~(bit(a)|bit(b))).length!==1)return false;return true}
  function size(m){let c=0;while(m){m&=m-1;c++}return c}
  let state=1729;
  for(let step=0;step<(n<7?1<<all.length:20000);step++){
   if(n===7)state=(Math.imul(state,1664525)+1013904223)>>>0;
   let mask=n<7?step:state>>>11;
   let adj=Array(n).fill(0),es=[];for(let i=0;i<all.length;i++)if(mask&bit(i)){let [x,y]=all[i];adj[x]|=bit(y);adj[y]|=bit(x);es.push([x,y])}
   if(adj.some(a=>size(a)<3)||!connected(adj))continue;
   graphs++;let found=false;
   for(let [x,y] of es){
    edges++;let contracted=Array(n-1).fill(0),map=Array.from({length:n},(_,v)=>v===y?x:v>y?v-1:v);
    for(let [u,v] of es){let a=map[u],b=map[v];if(a!==b){contracted[a]|=bit(b);contracted[b]|=bit(a)}}
    let ok=connected(contracted), separators=[];
    for(let z=0;z<n;z++)if(z!==x&&z!==y){
      let cs=comps(adj,full&~(bit(x)|bit(y)|bit(z)));
      if(cs.length>1)separators.push([z,cs]);
    }
    assert(ok===(separators.length===0),"criterion");
    if(ok){good++;found=true;continue}bad++;
    for(let [z,cs] of separators)for(let C of cs){
      triples++;
      assert([x,y,z].every(v=>adj[v]&C),"three-cut adjacency");
      for(let w=0;w<n;w++)if(C&bit(w)&&adj[z]&bit(w))for(let t=0;t<n;t++)if(t!==z&&t!==w){
        let ds=comps(adj,full&~(bit(z)|bit(w)|bit(t)));
        if(ds.length<2)continue;
        let candidates=ds.filter(D=>!(D&(bit(x)|bit(y))));
        assert(candidates.length>0,"no D");
        for(let D of candidates){
          assert((adj[w]&D)!==0 && (D&~C)===0 && size(D)<size(C),"descent");
          descents++;if(t===x||t===y)overlap++;else if(C&bit(t))inside++;else outside++;
        }
      }
    }
   }
   assert(found,"no contractible edge");
  }
 }
 assert(overlap>0&&inside>0,"missing overlap or inside cases");
 assert(outside===0,"separator outside C and original cut");
 return {graphs,edges,good,bad,triples,descents,overlap,inside,outside};
}
console.log(JSON.stringify(run()));
