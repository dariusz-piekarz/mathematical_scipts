// AA-65: symmetric powers of natural sl_n modules, exact integer monomial action.
function highest65(){
 const assert=(v,m)=>{if(!v)throw Error(m)},key=v=>v.join(","),sum=(a,b)=>a.map((x,i)=>x+b[i]);
 function comps(n,k){if(n===1)return [[k]];let r=[];for(let j=0;j<=k;j++)for(let w of comps(n-1,k-j))r.push([j,...w]);return r;}
 let models=0,weights=0,reflections=0,relations=0,highest=0;
 for(let n=2;n<=5;n++)for(let m=0;m<=7;m++){
  const basis=comps(n,m),r=n-1,w=a=>a.slice(0,-1).map((x,i)=>x-a[i+1]),map=new Map(basis.map(a=>[key(a),a]));
  function op(a,i,e){const from=e?i+1:i,to=e?i:i+1;if(!a[from])return null;const b=a.slice();b[from]--;b[to]++;return [b,a[from]];}
  function act2(a,i,e,j,f){const x=op(a,j,f);if(!x)return new Map();const y=op(x[0],i,e);return y?new Map([[key(y[0]),x[1]*y[1]]]):new Map();}
  let top=0;
  for(const a of basis){const wa=w(a);weights++;
   if(Array.from({length:r},(_,i)=>op(a,i,true)).every(x=>!x)){assert(wa[0]===m&&wa.slice(1).every(x=>x===0),"highest");top++;}
   for(let i=0;i<r;i++){
    const b=a.slice();[b[i],b[i+1]]=[b[i+1],b[i]];
    const alpha=Array.from({length:r},(_,j)=>j===i?2:Math.abs(j-i)===1?-1:0);
    assert(map.has(key(b))&&key(w(b))===key(sum(wa,alpha.map(x=>-wa[i]*x))),"reflection");reflections++;
    for(let j=0;j<r;j++){
     const X=act2(a,i,true,j,false),Y=act2(a,j,false,i,true);
     for(const k of new Set([...X.keys(),...Y.keys(),key(a)]))assert((X.get(k)||0)-(Y.get(k)||0)===(i===j&&k===key(a)?wa[i]:0),"commutator");relations++;
    }
   }
  }
  assert(top===1,"one highest monomial");highest++;models++;
 }
 return {models,weights,reflections,relations,highest};
}
console.log('AA-65 symmetric powers: PASS',highest65());
