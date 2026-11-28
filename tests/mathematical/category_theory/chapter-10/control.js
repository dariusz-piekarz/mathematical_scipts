"use strict";
function control(){
 const maps=(n,m)=>{let out=[[]];for(let i=0;i<n;i++)out=out.flatMap(a=>Array.from({length:m},(_,j)=>[...a,j]));return out};
 const eq=(a,b)=>JSON.stringify(a)===JSON.stringify(b),comp=(g,f)=>f.map(i=>g[i]),assert=x=>{if(!x)throw Error("control failure")};
 let parallel=0,actions=0,candidates=0,embedding=0;
 // Category with two parallel arrows 0 -> 1, not a poset.
 // Enumerate all functors on it and all candidate transformations
 // from the two representables, in each orientation.
 for(let n=0;n<=3;n++)for(let m=0;m<=3;m++)for(const u of maps(n,m))for(const v of maps(n,m)){
   for(const A of [0,1]){
     const sizes=A===0?[1,2]:[0,1], h=A===0?[[0],[1]]:[[],[]];
     let got=[];
     for(const a of maps(sizes[0],n))for(const b of maps(sizes[1],m)){
       if(eq(comp(u,a),comp(b,h[0]))&&eq(comp(v,a),comp(b,h[1])))got.push([a,b]);
     }
     const expected=A===0?Array.from({length:n},(_,i)=>[[i],[u[i],v[i]]]):Array.from({length:m},(_,i)=>[[],[i]]);
     assert(eq(got,expected));parallel++;
   }
 }
 // Full transformation monoid of a two-element set is noncommutative.
 const M=maps(2,2),id=M.findIndex(x=>eq(x,[0,1]));
 const mul=(g,f)=>M.findIndex(x=>eq(x,comp(M[g],M[f])));
 for(const opposite of [false,true]){
   const prod=(g,f)=>opposite?mul(f,g):mul(g,f);
   for(let n=0;n<=2;n++){
     const funcs=maps(n,n),I=Array.from({length:n},(_,i)=>i);
     for(const indices of maps(M.length,funcs.length)){
       const T=indices.map(i=>funcs[i]);
       if(!eq(T[id],I))continue;
       let valid=true;
       for(let g=0;g<M.length;g++)for(let f=0;f<M.length;f++)if(!eq(T[prod(g,f)],comp(T[g],T[f])))valid=false;
       if(!valid)continue;
       actions++;
       const regular=M.map((_,g)=>M.map((_,f)=>prod(g,f)));
       let actual=[];
       for(const a of maps(M.length,n)){
         candidates++;
         if(T.every((t,g)=>eq(comp(t,a),comp(a,regular[g]))))actual.push(a);
       }
       const expected=Array.from({length:n},(_,x)=>T.map(t=>t[x]));
       assert(eq(actual.map(a=>JSON.stringify(a)).sort(),expected.map(a=>JSON.stringify(a)).sort()));
       for(const a of actual)assert(eq(a,T.map(t=>t[a[id]])));
     }
   }
   // Natural endomorphisms of regular action: all right multiplications.
   const regular=M.map((_,g)=>M.map((_,f)=>prod(g,f)));
   const got=maps(M.length,M.length).filter(a=>regular.every(r=>eq(comp(r,a),comp(a,r))));
   assert(got.length===M.length);
   for(const a of got){assert(eq(a,M.map((_,f)=>prod(f,a[id]))));embedding++}
 }
 return {parallel,actions,candidates,embedding};
}
console.log(JSON.stringify(control()));
