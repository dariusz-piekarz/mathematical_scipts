// AA-65: independent tensor powers of natural and contragredient sl3 modules.
function tensor65(){
 const assert=(v,m)=>{if(!v)throw Error(m)};
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b)[a,b]=[b,a%b];return a;};
 function rank(cols){let rows=[];for(let v of cols){v=v.slice();for(const [p,w] of rows){if(!v[p])continue;const a=w[p],b=v[p];v=v.map((x,i)=>a*x-b*w[i]);const d=v.reduce(gcd,0n);if(d)v=v.map(x=>x/d);}const p=v.findIndex(x=>x!==0n);if(p>=0)rows.push([p,v]);}return rows.length;}
 const wt=[[1,0],[-1,1],[0,-1]];
 let models=0,dimensions=0,reflections=0,highestSpaces=0,dominant=0,relations=0;
 for(let a=0;a<=2;a++)for(let b=0;b<=2;b++){
  const n=a+b,dim=3**n,bs=Array.from({length:dim},(_,k)=>Array.from({length:n},(_,j)=>Math.floor(k/3**j)%3));
  const groups=new Map();const weight=word=>word.reduce((w,x,j)=>w.map((y,i)=>y+(j<a?1:-1)*wt[x][i]),[0,0]);
  for(let k=0;k<dim;k++){const w=weight(bs[k]).join(",");if(!groups.has(w))groups.set(w,[]);groups.get(w).push(k);}
  const E=(k,i,raise)=>{const w=bs[k],out=new Map();for(let j=0;j<n;j++){let dual=j>=a,from=(raise!==dual)?i+1:i,to=(raise!==dual)?i:i+1;if(w[j]===from){let l=k+(to-from)*3**j;out.set(l,(out.get(l)||0n)+(dual?-1n:1n));}}return out;};
  const comp=(k,i,x,j,y)=>{let v=new Map();for(const [l,c] of E(k,j,y))for(const [t,d] of E(l,i,x))v.set(t,(v.get(t)||0n)+c*d);return v;};
  for(let k=0;k<dim;k++)for(let i=0;i<2;i++)for(let j=0;j<2;j++){const X=comp(k,i,true,j,false),Y=comp(k,j,false,i,true);for(const l of new Set([...X.keys(),...Y.keys(),k]))assert((X.get(l)||0n)-(Y.get(l)||0n)===(i===j&&l===k?BigInt(weight(bs[k])[i]):0n),"commutator");relations++;}
  for(const [key,ks] of groups){const w=key.split(",").map(Number);
   for(let i=0;i<2;i++){const r=w.map((v,j)=>v-w[i]*(i===j?2:-1));assert(groups.get(r.join(","))?.length===ks.length,"weight multiplicity");reflections++;}
   const cols=ks.map(k=>{let v=Array(2*dim).fill(0n);for(let i=0;i<2;i++)for(const [l,c] of E(k,i,true))v[i*dim+l]=c;return v;});
   const d=ks.length-rank(cols);if(d){assert(w.every(v=>v>=0),"dominance");dominant+=d;highestSpaces++;}
   if(key===`${a},${b}`)assert(d===1&&ks.length===1,"top multiplicity");
  }
  models++;dimensions+=dim;
 }
 // Independently check exact highest multiplicities for V tensor V*:
 // the scalar and adjoint highest weights are (0,0), (1,1).
 const expected=2; // one trivial and one highest vector in the adjoint summand
 const W=Array.from({length:9},(_,k)=>[k%3,Math.floor(k/3)]);
 let cols=W.map(([x,y])=>{let v=Array(18).fill(0n);for(let i=0;i<2;i++){if(x===i+1)v[i*9+i+3*y]+=1n;if(y===i)v[i*9+x+3*(i+1)]-=1n;}return v;});
 assert(9-rank(cols)===expected,"V times dual highest dimension");
 return {models,dimensions,reflections,highestSpaces,dominant,relations,adjointAndTrivial:expected};
}
console.log('AA-65 tensor modules: PASS',tensor65());

// Independent non-simply-laced check: tensor square of the standard C_n representation.
function symplectic65(){
 const assert=(v,m)=>{if(!v)throw Error(m)};
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b)[a,b]=[b,a%b];return a;};
 function rank(cols){let rows=[];for(let v of cols){v=v.slice();for(const [p,w] of rows){if(!v[p])continue;const a=w[p],b=v[p];v=v.map((x,i)=>a*x-b*w[i]);const d=v.reduce(gcd,0n);if(d)v=v.map(x=>x/d);}const p=v.findIndex(x=>x!==0n);if(p>=0)rows.push([p,v]);}return rows.length;}
 let models=0,reflections=0,relations=0,cartan=0,highest=0,weightSpaces=0;
 for(let n=2;n<=5;n++){
  const d=2*n,dim=d*d;
  // Standard sp(2n) basis x_1,...,x_n,y_1,...,y_n.
  const es=Array.from({length:n},(_,i)=>i===n-1?[[i,n+i,1n]]:[[i,i+1,1n],[n+i+1,n+i,-1n]]);
  const fs=es.map(entries=>entries.map(([a,b,c])=>[b,a,c]));
  const wt=Array.from({length:d},(_,k)=>Array.from({length:n},(_,i)=>(k<n?1:-1)*((k%n===i?1:0)-(i<n-1&&k%n===i+1?1:0))));
  const A=Array.from({length:n},(_,i)=>Array.from({length:n},(_,j)=>i===j?2:i===n-2&&j===n-1?-2:Math.abs(i-j)===1?-1:0));
  for(let j=0;j<n;j++)for(const [a,b,c] of es[j])for(let i=0;i<n;i++){assert(wt[a][i]-wt[b][i]===A[i][j],"Cartan entry");cartan++;}
  function weight(k){return wt[k%d].map((x,i)=>x+wt[Math.floor(k/d)][i]);}
  function act(k,i,raise){const out=new Map();for(const [a,b,c] of (raise?es:fs)[i]){if(k%d===b){const l=k+a-b;out.set(l,(out.get(l)||0n)+c);}if(Math.floor(k/d)===b){const l=k+d*(a-b);out.set(l,(out.get(l)||0n)+c);}}return out;}
  function comp(k,i,x,j,y){const v=new Map();for(const [l,c] of act(k,j,y))for(const [t,e] of act(l,i,x))v.set(t,(v.get(t)||0n)+c*e);return v;}
  const groups=new Map();
  for(let k=0;k<dim;k++){
   const w=weight(k),key=w.join(",");if(!groups.has(key))groups.set(key,[]);groups.get(key).push(k);
   for(let i=0;i<n;i++)for(let j=0;j<n;j++){const X=comp(k,i,true,j,false),Y=comp(k,j,false,i,true);for(const l of new Set([...X.keys(),...Y.keys(),k]))assert((X.get(l)||0n)-(Y.get(l)||0n)===(i===j&&l===k?BigInt(w[i]):0n),"tensor commutator");relations++;}
  }
  const expected=new Set([Array.from({length:n},(_,i)=>i===0?2:0).join(","),Array.from({length:n},(_,i)=>i===1?1:0).join(","),Array(n).fill(0).join(",")]);
  for(const [key,ks] of groups){
   const w=key.split(",").map(Number);weightSpaces++;
   for(let i=0;i<n;i++){const reflected=w.map((x,j)=>x-w[i]*A[j][i]);assert(groups.get(reflected.join(","))?.length===ks.length,"C_n Weyl reflection");reflections++;}
   const cols=ks.map(k=>{const v=Array(n*dim).fill(0n);for(let i=0;i<n;i++)for(const [l,c] of act(k,i,true))v[i*dim+l]=c;return v;});
   const nullity=ks.length-rank(cols);assert(nullity===(expected.has(key)?1:0),"C_n highest multiplicity");if(nullity)highest+=nullity;
  }
  assert([...expected].every(key=>groups.has(key)),"expected highest weights occur");models++;
 }
 return {models,weightSpaces,cartan,reflections,relations,highest};
}
console.log('AA-65 symplectic tensor squares: PASS',symplectic65());
