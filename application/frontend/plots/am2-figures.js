/* Canonical AM II figure definitions. No code from TeX is executed. */
(function(root){
  "use strict";
  const lin=(a,b,n)=>Array.from({length:n},(_,i)=>a+(b-a)*i/(n-1));
  const grid=(x,y,f)=>y.map(v=>x.map(u=>f(u,v)));
  const surface=(x,y,z,extra={})=>({type:"surface",x,y,z,showscale:false,colorscale:"Viridis",...extra});
  const line=(x,y,z,name,color)=>({type:"scatter3d",mode:"lines",x,y,z,name,line:{color,width:5}});
  const axis=title=>({title,showbackground:true,backgroundcolor:"#f5f6f7",gridcolor:"#d5dbe0",zerolinecolor:"#b0b8bf",showspikes:false});
  const scene=(x="x",y="y",z="z")=>({xaxis:axis(x),yaxis:axis(y),zaxis:axis(z),aspectmode:"auto"});
  const base=(data,title,layout={})=>({data,layout:{title:{text:title,font:{size:16}},autosize:true,margin:{l:0,r:0,b:0,t:55},scene:scene(),...layout}});
  const figures={
    "am2_01_norm_balls.html":()=>{
      const a=lin(0,Math.PI,61),t=lin(0,2*Math.PI,121);
      // Exact planar faces; show only geometric edges, never face diagonals.
      const oct=[[-1,0,0],[1,0,0],[0,-1,0],[0,1,0],[0,0,-1],[0,0,1]],octFaces=[[0,4,2],[0,2,5],[0,3,4],[0,5,3],[1,2,4],[1,5,2],[1,4,3],[1,3,5]],octEdges=[[0,2],[0,3],[0,4],[0,5],[1,2],[1,3],[1,4],[1,5],[2,4],[2,5],[3,4],[3,5]];
      const cube=[[-1,-1,-1],[-1,-1,1],[-1,1,-1],[-1,1,1],[1,-1,-1],[1,-1,1],[1,1,-1],[1,1,1]],cubeFaces=[[0,1,3],[0,3,2],[4,6,7],[4,7,5],[0,4,5],[0,5,1],[2,3,7],[2,7,6],[0,2,6],[0,6,4],[1,5,7],[1,7,3]],cubeEdges=[[0,1],[0,2],[0,4],[1,3],[1,5],[2,3],[2,6],[3,7],[4,5],[4,6],[5,7],[6,7]];
      const poly=(v,f,e,sc,name)=>{
        const coord=k=>v.map(p=>p[k]),idx=k=>f.map(p=>p[k]),edgeCoord=k=>e.flatMap(([a,b])=>[v[a][k],v[b][k],null]);
        return [{type:"mesh3d",scene:sc,name,x:coord(0),y:coord(1),z:coord(2),i:idx(0),j:idx(1),k:idx(2),intensity:coord(2),colorscale:"Viridis",cmin:-1,cmax:1,flatshading:true,showscale:false,showlegend:false},
          {type:"scatter3d",scene:sc,mode:"lines",x:edgeCoord(0),y:edgeCoord(1),z:edgeCoord(2),line:{color:"#222222",width:5},hoverinfo:"skip",showlegend:false}];
      };
      const coord=k=>a.map(v=>t.map(u=>[Math.sin(v)*Math.cos(u),Math.sin(v)*Math.sin(u),Math.cos(v)][k]));
      const data=[...poly(oct,octFaces,octEdges,"scene","l1"),
        surface(coord(0),coord(1),coord(2),{scene:"scene2",name:"l2",cmin:-1,cmax:1,showlegend:false}),
        ...poly(cube,cubeFaces,cubeEdges,"scene3","l∞")];
      const layout={};
      for(let i=0;i<3;i++)layout[i?"scene"+(i+1):"scene"]={domain:{x:[i/3,(i+1)/3],y:[0,1]},aspectmode:"cube",...Object.fromEntries(["x","y","z"].map(k=>[k+"axis",{...axis(k),range:[-1.1,1.1]}]))};
      return base(data,"Brzegi kul jednostkowych",layout);
    },
    "am2_08_peaks.html":()=>{
      const colors=["#440154","#443983","#31688E","#21918C","#35B779","#90D743","#B8DE29"],indices=[1,2,3,5,8,13,20];
      const data=Array.from({length:20},(_,i)=>{
        const n=i+1,x=[...new Set([0,1/n,Math.min(1,2/n),1])].sort((a,b)=>a-b);
        const j=indices.reduce((best,k,j)=>Math.abs(k-n)<Math.abs(indices[best]-n)?j:best,0);
        return line(x,x.map(()=>n),x.map(v=>Math.max(1-n*Math.abs(v-1/n),0)),"n="+n,colors[j]);
      });
      data.push({type:"scatter3d",mode:"markers",x:lin(1,20,20).map(n=>1/n),y:lin(1,20,20),z:Array(20).fill(1),name:"maksima",marker:{size:4,color:"#c87900"}});
      return base(data,"Wędrujące maksima",{scene:scene("x","n","gₙ(x)")});
    },
    "am2_09_sums.html":()=>{
      const x=lin(0,1,501),indices=[1,2,4,8,16,32,64],colors=["#440154","#443983","#31688E","#21918C","#35B779","#90D743","#B8DE29"];
      const axes=scene("x","N (log₂)","Sₙ(x)");
      axes.yaxis={...axes.yaxis,type:"log",tickmode:"array",tickvals:indices,ticktext:indices.map(String)};
      const data=indices.map((n,i)=>line(x,x.map(()=>n),x.map(v=>v-v**(n+1)),"N="+n,colors[i]));
      data.push({type:"scatter3d",mode:"markers",x:indices.map(()=>1),y:indices,z:indices.map(()=>0),marker:{size:3,color:colors},name:"S_N(1)=0",showlegend:false});
      return base(data,"Sumy częściowe",{scene:axes});
    },
    "am2_11_paths.html":()=>{
      const x=lin(-1,1,161),data=[surface(x,x,grid(x,x,(u,v)=>u===0&&v===0?null:u*u*v/(u**4+v*v)),{colorscale:"Viridis",cmin:-.5,cmax:.5,connectgaps:false})];
      for(const t of [lin(-1,-.001,301),lin(.001,1,301)])data.push(line(t,t.map(v=>v*v),t.map(()=>.5),"y=x²","black"));
      data.push({type:"scatter3d",mode:"markers",x:[0],y:[0],z:[0],name:"f(0,0)=0"});
      return base(data,"Granice wzdłuż krzywych");
    },
    "am2_12_direction.html":()=>{
      const x=lin(-1,1,81),t=lin(-1,1,201),u=t.map(v=>v/Math.sqrt(2));
      return base([surface(x,x,grid(x,x,(a,b)=>a*a+2*b*b+a+b),{opacity:.65,colorscale:"Viridis"}),line(u,u,t.map(v=>1.5*v*v+Math.sqrt(2)*v),"przekrój","black"),line(u,u,t.map(v=>Math.sqrt(2)*v),"styczna","red")],"Przekrój kierunkowy");
    },
    "am2_13_frechet.html":()=>{
      const x=lin(-1,1,161),data=[surface(x,x,grid(x,x,(u,v)=>u===0&&v===0?null:Math.abs(u**3*v)/((u**4+v*v)*Math.hypot(u,v))),{connectgaps:false,colorscale:"Viridis"})];
      for(const t of [lin(-1,-.001,301),lin(.001,1,301)])data.push(line(t,t.map(v=>v*v),t.map(v=>1/(2*Math.sqrt(1+v*v))),"y=x²","red"));
      return base(data,"Iloraz błędu Frécheta",{scene:scene("x","y","|f(x,y)|/‖(x,y)‖")});
    },
    "am2_14_remainder.html":()=>{
      const x=lin(-1,1,81);
      return base([surface(x,x,grid(x,x,(u,v)=>u*u+2*v*v),{name:"reszta",showlegend:true,opacity:.65,colorscale:"Viridis",cmin:0,cmax:4}),surface(x,x,grid(x,x,(u,v)=>2*(u*u+v*v)),{name:"ograniczenie",showlegend:true,opacity:.65,colorscale:"Viridis",cmin:0,cmax:4})],"Kwadratowe oszacowanie reszty");
    },
    "am2_15_mixed.html":()=>{
      const x=lin(-1,1,121);
      return base([surface(x,x,grid(x,x,(u,v)=>u===0&&v===0?0:u*v*(u*u-v*v)/(u*u+v*v)),{colorscale:"Viridis",cmid:0})],"Pochodne mieszane");
    },
    "am2_16_taylor.html":()=>{
      const x=lin(-1,1,81);
      return base([surface(x,x,grid(x,x,(u,v)=>u*u+v*v+u**3/2),{name:"f",showlegend:true,opacity:.65,colorscale:"Viridis",cmin:0,cmax:2.5}),surface(x,x,grid(x,x,(u,v)=>u*u+v*v),{name:"T₂",showlegend:true,opacity:.65,colorscale:"Viridis",cmin:0,cmax:2.5})],"Funkcja i wielomian Taylora");
    },
    "am2_17_saddle.html":()=>{
      const x=lin(-1,1,121),y=lin(-.5,2,151),data=[surface(x,y,grid(x,y,(u,v)=>(v-u*u)*(v-2*u*u)),{opacity:.8,colorscale:"Viridis",cmid:0})];
      for(const c of [1,1.5,2])data.push(line(x,x.map(v=>c*v*v),x.map(v=>(c-1)*(c-2)*v**4),"y="+c+"x²","black"));
      return base(data,"Punkt siodłowy");
    },
    "am2_18_inverse.html":()=>{
      const x=lin(-1,1,81);
      return base([surface(x,x,grid(x,x,(u,v)=>v+u*u),{colorscale:"Viridis",cmin:-2,cmax:2,scene:"scene"}),surface(x,x,grid(x,x,(u,v)=>v-u*u),{colorscale:"Viridis",cmin:-2,cmax:2,scene:"scene2"})],"Składowe funkcji i odwrotności",{scene:{...scene("x","y","f₂"),domain:{x:[0,.48],y:[0,1]}},scene2:{...scene("u","v","g₂"),domain:{x:[.52,1],y:[0,1]}}});
    },
    "am2_19_implicit.html":()=>{
      const a=lin(Math.asin(.65),Math.PI,61),t=lin(0,2*Math.PI,121),r=lin(0,.65,41);
      const X=t.map(u=>a.map(v=>Math.sin(v)*Math.cos(u))),Y=t.map(u=>a.map(v=>Math.sin(v)*Math.sin(u))),Z=t.map(()=>a.map(Math.cos));
      const U=t.map(u=>r.map(v=>v*Math.cos(u))),V=t.map(u=>r.map(v=>v*Math.sin(u)));
      return base([surface(X,Y,Z,{opacity:.38,colorscale:[[0,"#a4bacd"],[1,"#e9f1f7"]],name:"sfera",showlegend:true}),surface(U,V,t.map(()=>r.map(v=>Math.sqrt(1-v*v))),{colorscale:"Viridis",cmin:Math.sqrt(1-.65**2),cmax:1,name:"lokalny wykres",showlegend:true}),surface(U,V,t.map(()=>r.map(()=>1)),{opacity:.45,colorscale:[[0,"#cd9123"],[1,"#f5dfac"]],name:"płaszczyzna styczna",showlegend:true}),{type:"scatter3d",mode:"markers",x:[0],y:[0],z:[1],name:"p",marker:{color:"#aa4137",size:5}}],"Sfera i lokalny wykres",{scene:{...scene("x₁","x₂","y"),aspectmode:"data"}});
    },
    "am2_20_rank.html":()=>{
      const x=lin(-1,1,61);
      return base([-1,0,1].map((c,i)=>surface(x,x,grid(x,x,(u,v)=>u*u+v*v+c),{colorscale:"Viridis",cmin:-1,cmax:3,opacity:.8,name:"c="+c,showlegend:true})),"Poziomice submersji");
    },
    "am2_21_tangent.html":()=>{
      const x=lin(-1,1,61);
      return base([surface(x,x,grid(x,x,(u,v)=>u*u+v*v),{colorscale:"Viridis",name:"S",showlegend:true}),surface(x,x,grid(x,x,()=>0),{colorscale:[[0,"#cd9123"],[1,"#f5dfac"]],opacity:.45,name:"T₀S",showlegend:true}),line([0,0],[0,0],[0,1],"n","#aa4137"),{type:"scatter3d",mode:"markers",x:[0],y:[0],z:[0],name:"p",marker:{color:"#aa4137",size:5}}],"Przestrzeń styczna i normalna",{scene:{...scene(),aspectmode:"data"}});
    },
    "am2_22_constrained.html":()=>{
      const x=lin(-1.2,2.2,81),y=lin(-1.2,1.2,61),t=lin(0,2*Math.PI,121),r=lin(0,1,41);
      const U=r.map(v=>t.map(a=>v*Math.cos(a))),V=r.map(v=>t.map(a=>v*Math.sin(a)));
      const f=(u,v)=>(u-2)**2+v*v;
      const data=[surface(x,y,grid(x,y,f),{scene:"scene",colorscale:"Viridis",cmin:0,cmax:12,name:"pełny wykres"}),
        surface(U,V,U.map((row,i)=>row.map((u,j)=>f(u,V[i][j]))),{scene:"scene2",colorscale:"Viridis",cmin:0,cmax:12,name:"część dopuszczalna"})];
      const a=lin(0,2*Math.PI,241);
      for(const sc of ["scene","scene2"]){
        data.push({...line(a.map(Math.cos),a.map(Math.sin),a.map(v=>5-4*Math.cos(v)),"brzeg koła","#222222"),scene:sc,showlegend:false});
        data.push({type:"scatter3d",mode:"markers",x:[1],y:[0],z:[1],scene:sc,name:"minimum związane",marker:{color:"red",size:5},showlegend:false});
      }
      data.push({type:"scatter3d",mode:"markers",x:[2],y:[0],z:[0],scene:"scene",name:"minimum swobodne",marker:{color:"blue",size:5},showlegend:false});
      const panel=(domain)=>({...scene("x","y","f"),domain:{x:domain,y:[0,1]},aspectmode:"manual",aspectratio:{x:1.4,y:1,z:1.2},xaxis:{...axis("x"),range:[-1.2,2.2]},yaxis:{...axis("y"),range:[-1.2,1.2]},zaxis:{...axis("f"),range:[0,12]}});
      return base(data,"Minimum na kole jednostkowym",{scene:panel([0,.48]),scene2:panel([.52,1]),annotations:[{text:"Pełny wykres",xref:"paper",yref:"paper",x:.24,y:1,showarrow:false},{text:"Część dopuszczalna",xref:"paper",yref:"paper",x:.76,y:1,showarrow:false}]});
    },
    "am2_23_gradient.html":()=>{
      const theta=lin(0,Math.PI,61),phi=lin(0,2*Math.PI,121);
      const X=theta.map(t=>phi.map(a=>Math.sin(t)*Math.cos(a))),Y=theta.map(t=>phi.map(a=>Math.sin(t)*Math.sin(a))),Z=theta.map(t=>phi.map(()=>Math.cos(t)));
      const p=[.6,0,.8],e=[0,0,1],w=p.map(v=>.8*v),g=e.map((v,i)=>v-w[i]);
      const data=[surface(X,Y,Z,{cmin:-1,cmax:1}),{type:"scatter3d",mode:"markers",x:[p[0]],y:[p[1]],z:[p[2]],marker:{color:"black",size:5},name:"p"}];
      const arrow=(v,name,color)=>{
        const tip=p.map((a,i)=>a+v[i]),side=[-v[2],0,v[0]];
        const left=tip.map((a,i)=>a-.18*v[i]+.09*side[i]),right=tip.map((a,i)=>a-.18*v[i]-.09*side[i]);
        const points=[p,tip,null,tip,left,null,tip,right],coord=i=>points.map(a=>a===null?null:a[i]);
        return {type:"scatter3d",mode:"lines",x:coord(0),y:coord(1),z:coord(2),name,line:{color,width:6}};
      };
      data.push(arrow(g,"gradient styczny","#b52332"),arrow(w,"składowa normalna","#c87900"),arrow(e,"gradient otoczenia","#234ab5"));
      return base(data,"Gradient styczny na sferze",{scene:{...scene(),aspectmode:"data",camera:{eye:{x:1.6,y:1.6,z:.8}},xaxis:{...axis("x"),range:[-1.2,1.35]},yaxis:{...axis("y"),range:[-1.2,1.2]},zaxis:{...axis("z"),range:[-1.15,1.95]}}});
    },
    "am2_24_darboux.html":()=>{
      const data=[],tri=[[0,2,1],[0,3,2],[4,5,6],[4,6,7],[0,1,5],[0,5,4],[1,2,6],[1,6,5],[2,3,7],[2,7,6],[3,0,4],[3,4,7]];
      const edges=[[0,1],[1,2],[2,3],[3,0],[4,5],[5,6],[6,7],[7,4],[0,4],[1,5],[2,6],[3,7]];
      for(let panel=0;panel<2;panel++)for(let i=0;i<2;i++)for(let j=0;j<2;j++){
        const x=i/2,y=j/2,X=x+.5,Y=y+.5,z=(1+x+y+panel)/3,sc=panel?"scene2":"scene";
        const pts=[[x,y,0],[X,y,0],[X,Y,0],[x,Y,0],[x,y,z],[X,y,z],[X,Y,z],[x,Y,z]];
        data.push({type:"mesh3d",scene:sc,x:pts.map(p=>p[0]),y:pts.map(p=>p[1]),z:pts.map(p=>p[2]),i:tri.map(t=>t[0]),j:tri.map(t=>t[1]),k:tri.map(t=>t[2]),intensity:pts.map(p=>p[2]),colorscale:"Viridis",cmin:0,cmax:1,showscale:false,flatshading:true,showlegend:false});
        const xyz=edges.flatMap(([u,v])=>[pts[u],pts[v],[null,null,null]]);
        data.push({type:"scatter3d",scene:sc,mode:"lines",x:xyz.map(p=>p[0]),y:xyz.map(p=>p[1]),z:xyz.map(p=>p[2]),line:{color:"#333",width:3},showlegend:false});
      }
      const panel=d=>({...scene("x","y","z"),domain:{x:d,y:[0,1]},aspectmode:"data",xaxis:{...axis("x"),range:[0,1]},yaxis:{...axis("y"),range:[0,1]},zaxis:{...axis("z"),range:[0,1.05]}});
      return base(data,"Sumy Darboux",{scene:panel([0,.48]),scene2:panel([.52,1]),annotations:[{text:"Suma dolna",xref:"paper",yref:"paper",x:.24,y:1,showarrow:false},{text:"Suma górna",xref:"paper",yref:"paper",x:.76,y:1,showarrow:false}]});
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
