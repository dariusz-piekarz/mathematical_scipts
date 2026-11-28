// GKT-20-CHAIN-01: signed boundaries and triangle homology over Z and finite fields.
function run(){
 const assert=(x,m)=>{if(!x)throw Error(m)},key=t=>[...t].sort((a,b)=>a-b).join(",");
 function sign(t){let p=0;for(let i=0;i<t.length;i++)for(let j=i+1;j<t.length;j++)p+=t[i]>t[j];return p%2?-1:1}
 function add(m,k,a){m.set(k,(m.get(k)||0)+a);if(m.get(k)===0)m.delete(k)}
 function bd(t){let m=new Map();if(t.length>1)for(let i=0;i<t.length;i++){let f=t.filter((_,j)=>i!==j);add(m,key(f),(-1)**i*sign(f))}return m}
 let orientations=0,squares=0,transpositions=0;
 function perm(t,k){if(k<t.length){for(let j=k;j<t.length;j++){[t[j],t[k]]=[t[k],t[j]];perm(t,k+1);[t[j],t[k]]=[t[k],t[j]]}return}
 let a=bd(t),b=bd([...t].sort((a,b)=>a-b));assert(a.size===b.size&&[...a].every(([k,v])=>v===sign(t)*b.get(k)),"orientation relation");orientations++;
 let m=new Map();for(let [k,v] of a)for(let [l,w] of bd(k.split(",").map(Number)))add(m,l,v*w);assert(m.size===0,"boundary squared");squares++;
 for(let i=0;i+1<t.length;i++){let u=[...t];[u[i],u[i+1]]=[u[i+1],u[i]];let c=bd(u);assert(a.size===c.size&&[...a].every(([k,v])=>v===-c.get(k)),"adjacent transposition");transpositions++}
 }
 for(let n=1;n<=6;n++)perm(Array.from({length:n},(_,i)=>i),0);
 let integerTriples=0,cycles=0,degreeZero=0;
 for(let a=-6;a<=6;a++)for(let b=-6;b<=6;b++)for(let c=-6;c<=6;c++){integerTriples++;let z=[-a-c,a-b,b+c];let is=z.every(x=>x===0);assert(is===(a===b&&b===-c),"triangle kernel");cycles+=is;
 // Any zero-sum vertex chain is a combination of [1]-[0] and [2]-[0].
 if(a+b+c===0){assert(a===-b-c,"augmentation kernel");degreeZero++}}
 let fields=0,fieldTriples=0;
 for(let p of [2,3,5,7]){let mod=x=>(x%p+p)%p,count=0,im=new Set();for(let a=0;a<p;a++)for(let b=0;b<p;b++)for(let c=0;c<p;c++){fieldTriples++;let z=[mod(-a-c),mod(a-b),mod(b+c)];im.add(z.join(","));if(z.every(x=>x===0)){count++;assert(a===b&&mod(b+c)===0,"mod kernel")}}assert(count===p&&im.size===p*p,"Betti counts");fields++}
 return {orientations,squares,transpositions,integerTriples,cycles,degreeZero,fields,fieldTriples};
}
console.log(JSON.stringify(run()));
