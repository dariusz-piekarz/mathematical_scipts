/* Canonical AM II figure definitions. No code from TeX is executed. */
(function(root){
  "use strict";
  const lin=(a,b,n)=>Array.from({length:n},(_,i)=>a+(b-a)*i/(n-1));
  const grid=(x,y,f)=>y.map(v=>x.map(u=>f(u,v)));
  const surface=(x,y,z,extra={})=>({type:"surface",x,y,z,showscale:false,...extra});
  const line=(x,y,z,name,color)=>({type:"scatter3d",mode:"lines",x,y,z,name,line:{color,width:5}});
  const scene=(x="x",y="y",z="z")=>({xaxis:{title:x},yaxis:{title:y},zaxis:{title:z},aspectmode:"auto"});
  const base=(data,title,layout={})=>({data,layout:{title:{text:title,font:{size:16}},autosize:true,margin:{l:0,r:0,b:0,t:55},scene:scene(),...layout}});
  const figures={
    "am2_01_norm_balls.html":()=>{
      const a=lin(0,Math.PI,61),t=lin(0,2*Math.PI,121);
      const data=[1,2,Infinity].map((p,i)=>{
        const coord=k=>a.map(v=>t.map(u=>{
          const d=[Math.sin(v)*Math.cos(u),Math.sin(v)*Math.sin(u),Math.cos(v)];
          const n=p===Infinity?Math.max(...d.map(Math.abs)):Math.pow(d.reduce((s,x)=>s+Math.abs(x)**p,0),1/p);
          return d[k]/n;
        }));
        return surface(coord(0),coord(1),coord(2),{scene:i?"scene"+(i+1):"scene",name:["l1","l2","l∞"][i],showlegend:true});
      });
      const layout={};
      for(let i=0;i<3;i++)layout[i?"scene"+(i+1):"scene"]={domain:{x:[i/3,(i+1)/3],y:[0,1]},aspectmode:"cube",...Object.fromEntries(["x","y","z"].map(k=>[k+"axis",{title:k,range:[-1.1,1.1]}]))};
      return base(data,"Brzegi kul jednostkowych",layout);
    },
    "am2_08_peaks.html":()=>{
      const data=Array.from({length:20},(_,i)=>{const n=i+1,x=[...new Set([...lin(0,1,301),1/n])].sort((a,b)=>a-b);return line(x,x.map(()=>n),x.map(v=>Math.max(1-n*Math.abs(v-1/n),0)),"n="+n,"#2469a0");});
      return base(data,"Wędrujące maksima",{scene:scene("x","n","gₙ(x)")});
    },
    "am2_09_sums.html":()=>{
      const x=lin(0,1,501);
      return base([1,2,4,8,16,32,64].map(n=>line(x,x.map(()=>n),x.map(v=>v-v**(n+1)),"N="+n,"#2469a0")),"Sumy częściowe",{scene:scene("x","N","Sₙ(x)")});
    },
    "am2_11_paths.html":()=>{
      const x=lin(-1,1,161),data=[surface(x,x,grid(x,x,(u,v)=>u===0&&v===0?null:u*u*v/(u**4+v*v)),{colorscale:"RdBu",cmin:-.5,cmax:.5,connectgaps:false})];
      for(const t of [lin(-1,-.001,301),lin(.001,1,301)])data.push(line(t,t.map(v=>v*v),t.map(()=>.5),"y=x²","black"));
      data.push({type:"scatter3d",mode:"markers",x:[0],y:[0],z:[0],name:"f(0,0)=0"});
      return base(data,"Granice wzdłuż krzywych");
    },
    "am2_12_direction.html":()=>{
      const x=lin(-1,1,81),t=lin(-1,1,201),u=t.map(v=>v/Math.sqrt(2));
      return base([surface(x,x,grid(x,x,(a,b)=>a*a+2*b*b+a+b),{opacity:.65,colorscale:"Blues"}),line(u,u,t.map(v=>1.5*v*v+Math.sqrt(2)*v),"przekrój","black"),line(u,u,t.map(v=>Math.sqrt(2)*v),"styczna","red")],"Przekrój kierunkowy");
    },
    "am2_13_frechet.html":()=>{
      const x=lin(-1,1,161),data=[surface(x,x,grid(x,x,(u,v)=>u===0&&v===0?null:Math.abs(u**3*v)/((u**4+v*v)*Math.hypot(u,v))),{connectgaps:false,colorscale:"Viridis"})];
      for(const t of [lin(-1,-.001,301),lin(.001,1,301)])data.push(line(t,t.map(v=>v*v),t.map(v=>1/(2*Math.sqrt(1+v*v))),"y=x²","red"));
      return base(data,"Iloraz błędu Frécheta",{scene:scene("x","y","|f(x,y)|/‖(x,y)‖")});
    },
    "am2_14_remainder.html":()=>{
      const x=lin(-1,1,81);
      return base([surface(x,x,grid(x,x,(u,v)=>u*u+2*v*v),{name:"reszta",showlegend:true,opacity:.65,colorscale:"Blues"}),surface(x,x,grid(x,x,(u,v)=>2*(u*u+v*v)),{name:"ograniczenie",showlegend:true,opacity:.65,colorscale:"Oranges"})],"Kwadratowe oszacowanie reszty");
    },
    "am2_15_mixed.html":()=>{
      const x=lin(-1,1,121);
      return base([surface(x,x,grid(x,x,(u,v)=>u===0&&v===0?0:u*v*(u*u-v*v)/(u*u+v*v)),{colorscale:"RdBu",cmid:0})],"Pochodne mieszane");
    },
    "am2_16_taylor.html":()=>{
      const x=lin(-1,1,81);
      return base([surface(x,x,grid(x,x,(u,v)=>u*u+v*v+u**3/2),{name:"f",showlegend:true,opacity:.65,colorscale:"Blues"}),surface(x,x,grid(x,x,(u,v)=>u*u+v*v),{name:"T₂",showlegend:true,opacity:.65,colorscale:"Oranges"})],"Funkcja i wielomian Taylora");
    },
    "am2_17_saddle.html":()=>{
      const x=lin(-1,1,121),y=lin(-.5,2,151),data=[surface(x,y,grid(x,y,(u,v)=>(v-u*u)*(v-2*u*u)),{opacity:.8,colorscale:"RdBu",cmid:0})];
      for(const c of [1,1.5,2])data.push(line(x,x.map(v=>c*v*v),x.map(v=>(c-1)*(c-2)*v**4),"y="+c+"x²","black"));
      return base(data,"Punkt siodłowy");
    },
    "am2_18_inverse.html":()=>{
      const x=lin(-1,1,81);
      return base([surface(x,x,grid(x,x,(u,v)=>v+u*u),{colorscale:"Blues",scene:"scene"}),surface(x,x,grid(x,x,(u,v)=>v-u*u),{colorscale:"Oranges",scene:"scene2"})],"Składowe funkcji i odwrotności",{scene:{...scene("x","y","f₂"),domain:{x:[0,.48],y:[0,1]}},scene2:{...scene("u","v","g₂"),domain:{x:[.52,1],y:[0,1]}}});
    },
    "am2_19_implicit.html":()=>{
      const a=lin(0,Math.PI,61),t=lin(0,2*Math.PI,121),r=lin(0,.65,41);
      const X=t.map(u=>a.map(v=>Math.sin(v)*Math.cos(u))),Y=t.map(u=>a.map(v=>Math.sin(v)*Math.sin(u))),Z=t.map(()=>a.map(Math.cos));
      const U=t.map(u=>r.map(v=>v*Math.cos(u))),V=t.map(u=>r.map(v=>v*Math.sin(u)));
      return base([surface(X,Y,Z,{opacity:.25,colorscale:"Greys",name:"sfera",showlegend:true}),surface(U,V,t.map(()=>r.map(v=>Math.sqrt(1-v*v))),{colorscale:"Blues",name:"lokalny wykres",showlegend:true}),surface(U,V,t.map(()=>r.map(()=>1)),{opacity:.45,colorscale:"Oranges",name:"płaszczyzna styczna",showlegend:true})],"Sfera i lokalny wykres",{scene:{...scene("x₁","x₂","y"),aspectmode:"data"}});
    },
    "am2_36_geometric.html":()=>{
      const r=lin(0,.97,61),t=lin(0,2*Math.PI,121),X=t.map(a=>r.map(v=>v*Math.cos(a))),Y=t.map(a=>r.map(v=>v*Math.sin(a)));
      const norm=(a,v,n)=>n===null?1/Math.hypot(1-v*Math.cos(a),v*Math.sin(a)):Math.hypot(1-v**(n+1)*Math.cos((n+1)*a),v**(n+1)*Math.sin((n+1)*a))/Math.hypot(1-v*Math.cos(a),v*Math.sin(a));
      const data=[null,4,16,64].map(n=>surface(X,Y,t.map(a=>r.map(v=>norm(a,v,n))),{name:n===null?"suma":"N="+n,showlegend:true,visible:n===null?true:"legendonly",colorscale:"Viridis"}));
      return base(data,"Moduł sumy szeregu geometrycznego",{scene:scene("Re z","Im z","moduł")});
    }
  };
  root.atlasAM2Figures=Object.freeze(figures);
})(typeof module==="object"&&module.exports?module.exports:globalThis);
