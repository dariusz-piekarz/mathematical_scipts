// GKT-21-EXAMPLES-01: Hessians and level-set equations for explicit Morse examples.
function run(){
 const assert=(x,m)=>{if(!x)throw Error(m)};let tori=0,critical=0,projective=0,points=0;
 for(let R=2;R<=16;R++)for(let r=1;r<R;r++){
 const data=[[-1,1,0],[-1,-1,1],[1,-1,1],[1,1,2]].map(([u,v,i])=>{let h=(R+r*v)*u,A=-h,B=-r*v*u;assert(A!==0&&B!==0&&Number(A<0)+Number(B<0)===i,"torus Hessian index");critical++;return h});
 assert(data.every((h,i)=>i===0||data[i-1]<h),"distinct ordered critical values");tori++}
 for(let i=0;i<3;i++){let d=[0,1,2].filter(j=>j!==i).map(j=>j-i);assert(d.every(x=>x!==0)&&d.filter(x=>x<0).length===i,"RP2 Hessian");projective++}
 for(let d=2;d<=20;d++)for(let n=1;n<d;n++)for(let side of [0,1]){
 let h=side+n/d;
 for(let j=0;j<24;j++){let a=j*Math.PI/12,x,y,z;
 if(side===0){x=1;y=Math.sqrt(h/(1-h))*Math.cos(a);z=Math.sqrt(h/(2-h))*Math.sin(a)}
 else{z=1;x=Math.sqrt((2-h)/h)*Math.cos(a);y=Math.sqrt((2-h)/(h-1))*Math.sin(a)}
 assert(Math.abs((y*y+2*z*z)/(x*x+y*y+z*z)-h)<1e-12,"RP2 ellipse equation");points++}
 }
 return {tori,critical,projective,points};
}
console.log(JSON.stringify(run()));
