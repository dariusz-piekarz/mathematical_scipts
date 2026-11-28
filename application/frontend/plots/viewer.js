"use strict";
(async function(){
  const status=document.getElementById("status");
  try{
    const id=new URLSearchParams(location.search).get("id");
    const figures=globalThis.atlasAM2Figures;
    if(!figures||!Object.hasOwn(figures,id))throw Error("Nieznany identyfikator wykresu.");
    if(!globalThis.Plotly)throw Error("Brak lokalnego Plotly. Zainstaluj zależności aplikacji.");
    const {data,layout}=figures[id]();
    status.hidden=true;
    await Plotly.newPlot(document.getElementById("plot"),data,layout,{responsive:true,displaylogo:false});
    document.getElementById("plot").dataset.ready="true";
  }catch(error){status.hidden=false;status.textContent=error.message;}
})();
