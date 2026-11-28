"use strict";
function control(){
 const maps=(n,m)=>{let a=[[]];for(let i=0;i<n;i++)a=a.flatMap(x=>Array.from({length:m},(_,j)=>[...x,j]));return a};
 const comp=(g,f)=>f.map(i=>g[i]);const eq=(a,b)=>JSON.stringify(a)===JSON.stringify(b);const check=x=>{if(!x)throw Error("control failed")};
 let cov=0,contra=0,local=0,der=0;
 for(let b=0;b<=3;b++)for(let a=0;a<=3;a++){
   for(const u of maps(b,a)){
     let initial=true;
     for(let x=0;x<=3;x++)for(const v of maps(b,x)){
       const mediators=maps(a,x).filter(f=>eq(comp(f,u),v));
       if(mediators.length!==1)initial=false;cov++;
     }
     check(initial===(a===b&&new Set(u).size===a));
   }
   for(const u of maps(a,b)){
     let terminal=true;
     for(let x=0;x<=3;x++)for(const v of maps(x,b)){
       const mediators=maps(x,a).filter(f=>eq(comp(u,f),v));
       if(mediators.length!==1)terminal=false;contra++;
     }
     check(terminal===(a===b&&new Set(u).size===b));
   }
 }
 for(let m=1;m<=12;m++){
   const inv=x=>Array.from({length:m},(_,i)=>i).find(i=>x*i%m===1%m);
   const ringmap=(n,f)=>f[1%n]===1%m&&Array.from({length:n},(_,i)=>i).every(a=>Array.from({length:n},(_,i)=>i).every(b=>f[(a+b)%n]===(f[a]+f[b])%m&&f[a*b%n]===f[a]*f[b]%m));
   const f=Array.from({length:6},(_,i)=>i%m);
   const admissible=ringmap(6,f)&&inv(f[2])!==undefined;
   const extensions=maps(3,m).filter(g=>ringmap(3,g)&&eq(Array.from({length:6},(_,i)=>g[i%3]),f));
   check(extensions.length===(admissible?1:0));local++;
 }
 for(const p of [2,3]){
   const n=p*p,add=(a,b)=>(a%p+b%p)%p+p*((Math.floor(a/p)+Math.floor(b/p))%p),
   mul=(a,b)=>(a%p*(b%p))%p+p*((a%p*Math.floor(b/p)+b%p*Math.floor(a/p))%p);
   for(let u=0;u<n;u++)for(let v=0;v<n;v++){
     const d=a=>add(mul(a%p,u),mul(Math.floor(a/p),v));
     let valid=true;
     for(let a=0;a<n;a++)for(let b=0;b<n;b++){
       if(d(add(a,b))!==add(d(a),d(b))||d(mul(a,b))!==add(mul(a,d(b)),mul(b,d(a))))valid=false;
     }
     for(let c=0;c<p;c++)if(d(c)!==0)valid=false;
     check(valid===(u===0&&mul(2%p,mul(p,v))===0));der++;
   }
 }
 return {cov,contra,local,der,total:cov+contra+local+der};
}
console.log(JSON.stringify(control()));
