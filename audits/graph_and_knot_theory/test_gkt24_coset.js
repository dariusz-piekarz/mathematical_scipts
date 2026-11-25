// GKT-24-COSET-01: exact affine coset incidence in BS(1,2).
function run(){
 const assert=(x,m)=>{if(!x)throw Error(m)};
 // Represent x -> 2^k*x+b/256 by [k,b], for bounded exponents.
 // Use rational integer scaling sufficient for all chosen elements and compositions.
 const scale=256n, pow=k=>2n**BigInt(k), mod=(x,m)=>(x%m+m)%m;
 function shift(b,k){if(k>=0)return b*pow(k);let d=pow(-k);assert(b%d===0n,"exact dyadic scaling");return b/d}
 function mul([k,b],[j,c]){return [k+j,b+shift(c,k)]}
 function inv([k,b]){return [-k,-shift(b,-k)]}
 const t=[1,0n],a=[0,scale], ti=inv(t);
 const same=(u,v)=>u[0]===v[0]&&u[1]===v[1];
 assert(same(mul(mul(t,a),ti),mul(a,a)),"HNN relation");
 assert(!same(mul(t,a),mul(a,t)),"noncommuting");
 const period=(k,h)=>pow(k+8)*BigInt(h);
 const key=([k,b],h=1)=>k+":"+mod(b,period(k,h));
 function edge(g,rev){return {id:(rev?"-":"+")+key(g,rev?2:1),o:key(g),v:key(mul(g,rev?t:ti)),rep:mul(g,rev?t:ti),rev:!rev}}
 let vertices=0,incidences=0,independence=0,reversals=0,translations=0;
 for(let k=-4;k<=4;k++)for(let b=-96;b<=96;b+=3){
  let g=[k,BigInt(b)],b1=period(k,1);
  const E=[edge(g,false),edge(g,true),edge([k,g[1]+b1],true)];
  assert(E.every(e=>e.o===key(g))&&new Set(E.map(e=>e.id)).size===3,"degree 3");
  assert(new Set(E.map(e=>e.v)).size===3,"distinct neighbors");
  assert(E[0].rep[0]===k-1&&E.slice(1).every(e=>e.rep[0]===k+1),"unique lower neighbor");
  for(let [h,rev] of [[g,false],[g,true],[[k,g[1]+b1],true]]){
   let e=edge(h,rev),back=edge(e.rep,!rev),again=edge(back.rep,rev);
   assert(back.o===e.v&&back.v===e.o&&again.id===e.id,"reverse involution");reversals++;
   for(let j=-4;j<=4;j++){let hp=[h[0],h[1]+BigInt(j)*period(h[0],rev?2:1)],f=edge(hp,rev);assert(e.id===f.id&&e.o===f.o&&e.v===f.v,"representative independence");independence++}
   // left translation by integer powers of a and t, scaled b chosen even for k=-1.
   for(let z of [[0,scale],[1,0n],[0,-2n*scale]]){
    let f=edge(mul(z,h),rev);assert(f.o===key(mul(z,h))&&f.v===key(mul(z,e.rep)),"left equivariance");translations++;
   }
   incidences++;
  }vertices++;
 }
 // Finite dyadic residue model: each vertex has two children and one parent
 // outside boundary levels. Each pair of vertices merges by descending levels.
 let levels=0,children=0;
 for(let k=-8;k<=2;k++){
  const p=period(k,1);for(let b=0n;b<p;b++){
   let v=[k,b];if(k>-8){let parent=edge(v,false);assert(parent.v===key([k-1,b]),"parent residue")}
   for(let e of [edge(v,true),edge([k,b+p],true)]){assert(edge(e.rep,false).v===key(v),"child returns to parent");children++}
   levels++;
  }
 }
 return {vertices,incidences,independence,reversals,translations,levels,children};
}
console.log(JSON.stringify(run()));
