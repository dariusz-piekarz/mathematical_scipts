// Independent exact finite-field cross-audit of AA-25--AA-27.
// Run: node tools/tests/test_abstract_algebra_cross_aa25_27.js
// No dependencies beyond Node.js.
function runAudit(){
  const C={field:0,addH90:0,multH90:0,witness:0,AS:0,Kummer:0,cross:0};
  function ok(cond,cat,note){C[cat]++;if(!cond)throw Error(cat+" FAILED "+note)}
  class Field{
    constructor(p,P,name){this.p=p;this.P=P;this.m=P.length-1;this.q=p**this.m;this.name=name}
    dig(a){let r=[];for(let j=0;j<this.m;j++){r.push(a%this.p);a=Math.floor(a/this.p)}return r}
    enc(a){return a.reduce((s,d,i)=>s+d*this.p**i,0)}
    mod(a){return (a%this.p+this.p)%this.p}
    add(a,b){let x=this.dig(a),y=this.dig(b);return this.enc(x.map((d,i)=>this.mod(d+y[i])))}
    sub(a,b){let x=this.dig(a),y=this.dig(b);return this.enc(x.map((d,i)=>this.mod(d-y[i])))}
    mul(a,b){let x=this.dig(a),y=this.dig(b),v=Array(2*this.m-1).fill(0);for(let i=0;i<this.m;i++)for(let j=0;j<this.m;j++)v[i+j]+=x[i]*y[j];for(let k=v.length-1;k>=this.m;k--){let c=this.mod(v[k]);for(let j=0;j<this.m;j++)v[k-this.m+j]-=c*this.P[j];v[k]=0}return this.enc(v.slice(0,this.m).map(d=>this.mod(d)))}
    pow(a,n){let v=1;while(n){if(n%2)v=this.mul(v,a);a=this.mul(a,a);n=Math.floor(n/2)}return v}
    inv(a){if(!a)throw Error("division by zero");return this.pow(a,this.q-2)}
    sigma(a){return this.pow(a,this.p)}
    trace(a){let x=a,s=0;for(let j=0;j<this.m;j++){s=this.add(s,x);x=this.sigma(x)}return s}
    norm(a){let x=a,s=1;for(let j=0;j<this.m;j++){s=this.mul(s,x);x=this.sigma(x)}return s}
    wp(a){return this.sub(this.pow(a,this.p),a)}
    roots(n,a){let v=[];for(let x=0;x<this.q;x++)if(this.pow(x,n)===a)v.push(x);return v}
  }
  const fs=[
    new Field(2,[0,1],"F2"),new Field(2,[1,1,1],"F4"),new Field(2,[1,1,0,1],"F8"),
    new Field(3,[0,1],"F3"),new Field(3,[1,0,1],"F9"),new Field(3,[2,2,0,1],"F27"),
    new Field(5,[0,1],"F5"),new Field(5,[2,0,1],"F25"),
    new Field(7,[0,1],"F7"),new Field(7,[5,0,0,1],"F343")
  ];
  for(const f of fs){
    const add=new Map(),mult=new Map();
    for(let x=0;x<f.q;x++){
      ok(f.pow(x,f.q)===x,"field",f.name+" x^q="+x);
      ok(f.trace(x)<f.p&&f.norm(x)<f.p,"field",f.name+" base-valued trace norm x="+x);
      if(x)ok(f.mul(x,f.inv(x))===1,"field",f.name+" inverse x="+x);
      const d=f.sub(x,f.sigma(x));if(!add.has(d))add.set(d,x);
      if(x){let y=f.mul(x,f.inv(f.sigma(x)));if(!mult.has(y))mult.set(y,x)}
    }
    for(let a=0;a<f.q;a++){
      ok(add.has(a)===(f.trace(a)===0),"addH90",f.name+" a="+a);
      if(a)ok(mult.has(a)===(f.norm(a)===1),"multH90",f.name+" a="+a);
      if(f.trace(a)===0)ok(f.sub(add.get(a),f.sigma(add.get(a)))===a,"witness",f.name+" additive a="+a);
      if(a&&f.norm(a)===1){
        let p=[1],cur=1,z=a;
        for(let j=0;j<f.m;j++){cur=f.mul(cur,z);p.push(cur);z=f.sigma(z)}
        ok(p[f.m]===1,"witness",f.name+" norm product a="+a);
        let found=false;
        for(let x=0;x<f.q;x++){
          let b=0,t=x;for(let j=0;j<f.m;j++){b=f.add(b,f.mul(p[j],t));t=f.sigma(t)}
          if(b!==0){found=f.mul(a,f.sigma(b))===b;break}
        }
        ok(found,"witness",f.name+" Dedekind witness a="+a);
      }
    }
  }
  for(const name of ["F4","F27"]){
    let f=fs.find(x=>x.name===name),alpha=f.p;
    ok(f.wp(alpha)===1,"AS",name+" alpha^p-alpha");
    ok(f.sigma(alpha)===f.add(alpha,1),"AS",name+" Frobenius shift");
    let b=f.sub(0,alpha);
    ok(f.trace(1)===0&&f.sub(b,f.sigma(b))===1,"cross",name+" additive H90 from AS");
    for(let a=0;a<f.p;a++){
      const roots=[];for(let x=0;x<f.q;x++)if(f.wp(x)===a)roots.push(x);
      ok(roots.length===f.p,"AS",name+" root count "+a);
      ok(roots.every(x=>a===0?x<f.p:x>=f.p),"AS",name+" root field "+a);
      for(const x of roots){const orb=new Set();let v=x;for(let j=0;j<f.m;j++){orb.add(v);v=f.sigma(v)}ok(orb.size===(a===0?1:f.p),"AS",name+" Frobenius orbit "+x)}
    }
    for(let c=1;c<f.p;c++)for(let d=0;d<f.p;d++){
      const beta=f.add(f.mul(c,alpha),d);
      ok(f.wp(beta)===c,"AS",name+" class c="+c+" d="+d);
      ok(f.sigma(beta)===f.add(beta,c),"AS",name+" shift c="+c+" d="+d);
    }
  }
  const f7=fs.find(x=>x.name==="F343"),alpha=7,beta=f7.mul(alpha,alpha);
  ok(f7.pow(alpha,3)===2,"Kummer","F343 alpha³=2");
  ok(f7.pow(beta,3)===4,"Kummer","F343 beta³=4");
  ok(f7.mul(beta,beta)===f7.mul(2,alpha),"Kummer","F343 beta²=2alpha");
  let z=f7.mul(f7.sigma(alpha),f7.inv(alpha));
  ok([2,4].includes(z)&&f7.pow(z,3)===1,"Kummer","F343 sigma(alpha)/alpha");
  for(let a=1;a<7;a++){
    const roots=f7.roots(3,a),cube=[1,6].includes(a);
    ok(roots.length===3,"Kummer","F343 roots "+a);
    ok(roots.every(x=>cube?x<7:x>=7),"Kummer","F343 root base "+a);
    for(const x of roots){const orb=new Set();let v=x;for(let j=0;j<3;j++){orb.add(v);v=f7.sigma(v)}ok(orb.size===(cube?1:3),"Kummer","F343 orbit "+a+" "+x)}
  }
  for(const a of [2,3,4,5])for(const b of [2,3,4,5]){
    let matches=[1,2].filter(j=>[1,6].includes(f7.mul(b,f7.inv(f7.pow(a,j)))));
    ok(matches.length===1,"Kummer","F7 Kummer class a="+a+" b="+b);
  }
  let f5=fs.find(x=>x.name==="F25"),t=5;
  ok(f5.pow(t,2)===3,"Kummer","F25 alpha²=3");
  ok(f5.pow(f5.mul(2,t),2)===2,"Kummer","F25 (2alpha)²=2");
  for(let a=1;a<5;a++){let roots=f5.roots(2,a);ok(roots.length===2,"Kummer","F25 roots "+a);ok(roots.every(x=>[1,4].includes(a)?x<5:x>=5),"Kummer","F25 root field "+a)}
  const total=Object.values(C).reduce((a,b)=>a+b,0);
  return {counts:C,total,fields:fs.map(x=>x.name)};
}
const result = runAudit();
if (result.total !== 2514) throw new Error("Unexpected number of checks: " + result.total);
console.log(JSON.stringify(result, null, 2));
