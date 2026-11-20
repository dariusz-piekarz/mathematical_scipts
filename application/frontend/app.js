"use strict";
/* HTML/CSS/JS client for read-only mathematical library.
   No untrusted TeX or API text is inserted via innerHTML. */
const $ = id => document.getElementById(id);
const state = {
  domains:[], modules:[], outlines:new Map(), expandedDomains:new Set(), expandedModules:new Set(),
  currentModule:null, currentEntity:null, currentData:null, selected:new Map(),
  tab:"reader", granularity:"module", simplified:false, tooltipData:null,
  tooltipKey:0, graph:null, renderEpoch:0, draftSession:null,
};
const titleOr = item => item.title || item.subtype || item.kind || item.id;
const tr = s => String(s ?? "");
const crop = (s,n=90) => tr(s).length > n ? tr(s).slice(0,n-1)+"…" : tr(s);
const toast = message => { $("toast").textContent=message;$("toast").classList.remove("hidden");clearTimeout(toast.timer);toast.timer=setTimeout(()=>$("toast").classList.add("hidden"),3400); };
function node(tag,attrs={},text){const el=document.createElement(tag);for(const [key,value] of Object.entries(attrs)){if(key==="className")el.className=value;else if(key==="title")el.title=value;else el.setAttribute(key,value);}if(text!==undefined)el.textContent=tr(text);return el;}
async function api(path, options={}) {
  let response;
  try { response=await fetch(path,{headers:{"Accept":"application/json",...(options.body?{"Content-Type":"application/json"}:{})},...options}); }
  catch(e){throw new Error("Nie można połączyć się z serwerem. Sprawdź, czy działa uvicorn.");}
  if(!response.ok){let desc="HTTP "+response.status;try{desc=(await response.json()).detail || desc;}catch(_){}throw new Error(desc);}
  return response.json();
}
function activateTab(name){
  state.tab=name;
  document.querySelectorAll(".tab").forEach(b=>b.classList.toggle("active",b.dataset.tab===name));
  for(const k of ["reader","graph","selection"])$("view-"+k).classList.toggle("hidden",k!==name);
  if(name==="selection")renderSelection();
  if(name==="graph" && !state.graph)loadGraph();
  closeTip();
}
function toggleDomain(domain){state.expandedDomains.has(domain)?state.expandedDomains.delete(domain):state.expandedDomains.add(domain);renderTree();}
async function toggleModule(id){
  if(state.expandedModules.has(id)){state.expandedModules.delete(id);renderTree();return;}
  state.expandedModules.add(id);
  if(!state.outlines.has(id)){
    try{const data=await api(`/api/modules/${encodeURIComponent(id)}/outline`);state.outlines.set(id,data.entities);}catch(e){toast(e.message);}
  }
  renderTree();
}
function typeIcon(kind){return ({chapter:"C",section:"§",subsection:"§",subsubsection:"§",theorem:"T",definition:"D",proof:"P",example:"E",exercise:"Z",remark:"U",equation:"∑",figure:"▧"})[kind] || "·";}
function renderTree(){
  const tree=$("tree");tree.replaceChildren();
  for(const domain of state.domains){
    const expanded=state.expandedDomains.has(domain.name);
    const group=node("div",{className:"domain-group"});
    const head=node("button",{className:"domain-header",role:"treeitem","aria-expanded":String(expanded)});
    head.append(node("span",{className:"chev"},expanded?"▾":"▸"),node("span",{className:"domain-icon"},"∑"),node("span",{className:"domain-title"},domain.name),node("span",{className:"count"},domain.modules));
    head.addEventListener("click",()=>toggleDomain(domain.name));group.append(head);
    if(expanded){
      for(const m of state.modules.filter(x=>x.domain===domain.name)){
        const line=node("div",{className:"module-line"+(state.currentModule===m.id?" active":"")});
        const caret=node("button",{className:"chev",title:"Rozwiń strukturę rozdziału","aria-label":"Rozwiń "+m.id},state.expandedModules.has(m.id)?"▾":"▸");
        caret.style.border="0";caret.style.background="transparent";caret.style.padding="0";
        caret.addEventListener("click",e=>{e.stopPropagation();toggleModule(m.id);});
        const trigger=node("button",{className:"module-name",title:m.title},crop(m.title,72));
        trigger.style.cssText="border:0;background:none;text-align:left;padding:0;color:inherit;cursor:pointer";
        trigger.addEventListener("click",()=>{openModule(m.id);if(state.granularity!=="module"&&!state.expandedModules.has(m.id))toggleModule(m.id);});
        line.append(caret,node("span",{className:"module-id"},m.id),trigger);group.append(line);
        if(state.expandedModules.has(m.id)&&state.granularity!=="module"){
          const branch=node("div",{className:"outline-list"});
          const rows=state.outlines.get(m.id)||[];
          let shown=0;
          for(const e of rows){
            const heading=["part","chapter","section","subsection","subsubsection","paragraph","subparagraph"].includes(e.kind);
            if(state.granularity==="section"&&!heading)continue;
            if(shown++>300){branch.append(node("div",{className:"explorer-description"},"Dalsze obiekty: użyj wyszukiwarki."));break;}
            const line=node("button",{className:"outline-row"+(state.currentEntity===e.id?" active":""),role:"treeitem",title:e.title||e.excerpt});
            line.append(node("span",{className:"outline-type"},typeIcon(e.kind)),node("span",{className:"outline-name"},crop(e.title || e.excerpt || e.kind,73)));
            line.addEventListener("click",()=>openEntity(e.id));branch.append(line);
          }
          group.append(branch);
        }
      }
    }
    tree.append(group);
  }
}
async function openModule(id,full=false){
  try{
    const epoch=++state.renderEpoch;const data=await api(`/api/modules/${encodeURIComponent(id)}${full?'?full=true':''}`);
    if(epoch!==state.renderEpoch)return;
    state.currentModule=id;state.currentEntity=null;state.currentData=data;
    state.expandedDomains.add(data.module.domain);renderTree();renderReader();activateTab("reader");
    $("explorer").classList.remove("visible");
  }catch(e){toast(e.message);}
}
async function openEntity(id,full=false){
  try{
    const epoch=++state.renderEpoch;const data=await api(`/api/entities/${encodeURIComponent(id)}${full?'?full=true':''}`);
    if(epoch!==state.renderEpoch)return;
    state.currentModule=data.entity.document_id;state.currentEntity=id;state.currentData=data;
    state.expandedDomains.add(data.domain);renderTree();renderReader();activateTab("reader");
    $("explorer").classList.remove("visible");
  }catch(e){toast(e.message);}
}
function showRefs(container,latex){
  container.replaceChildren();const regex=/\\(ref|eqref|pageref|autoref|nameref|cref|Cref|vref|Vref)\s*\{([^{}]+)\}/g;
  let last=0, match;
  while((match=regex.exec(latex))){
    if(match.index>last)container.append(document.createTextNode(latex.slice(last,match.index)));
    container.append(document.createTextNode("\\"+match[1]+"{"));
    const refs=match[2].split(",");
    refs.forEach((raw,i)=>{
      if(i)container.append(document.createTextNode(","));
      const lab=raw.trim();if(!lab){container.append(document.createTextNode(raw));return;}
      const b=node("button",{className:"ref-link",title:"Podgląd etykiety: "+lab},lab);
      b.addEventListener("mouseenter",()=>previewLabel(lab,b));
      b.addEventListener("focus",()=>previewLabel(lab,b));
      b.addEventListener("mouseleave",()=>{const key=state.tooltipKey;setTimeout(()=>{if(key===state.tooltipKey && !$("referenceTip").matches(":hover"))closeTip();},240);});
      b.addEventListener("click",()=>openLabel(lab));container.append(b);
    });
    container.append(document.createTextNode("}"));last=regex.lastIndex;
  }
  if(last<latex.length)container.append(document.createTextNode(latex.slice(last)));
}
function renderReader(){
  const data=state.currentData;if(!data)return;
  $("readerEmpty").classList.add("hidden");$("readerContent").classList.remove("hidden");
  const entity=Boolean(data.entity);const mod=state.modules.find(m=>m.id===state.currentModule);
  $("docBreadcrumb").textContent=(mod?.domain||data.domain||"")+" / "+state.currentModule+(entity?" / "+data.entity.kind:"");
  $("docTitle").textContent=entity?(data.entity.title||data.module_title||data.entity.kind):(data.module.title);
  $("docMeta").textContent=entity?`Wiersze ${data.entity.start_line}–${data.entity.end_line} · ${data.module_title}`:"Pełny moduł · "+data.module.path;
  $("readerKind").textContent=entity?"Fragment · "+data.entity.kind:"Źródło LaTeX — rozdział";
  $("readSize").textContent=(data.full_length||0).toLocaleString("pl-PL")+" znaków";
  $("showFull").classList.toggle("hidden",!data.truncated);
  $("addCurrent").textContent=state.selected.has((entity?"entity:":"module:")+(entity?data.entity.id:state.currentModule))?"✓ W zestawie":"+ Do zestawu";
  showRefs($("latexSource"),data.latex);
  renderSimplified(data.latex);
  $("latexSource").classList.toggle("hidden",state.simplified);
  $("simplified").classList.toggle("hidden",!state.simplified);
  $("togglePreview").textContent=state.simplified?"Pokaż LaTeX":"Podgląd uproszczony";
}
function renderSimplified(latex){
  // Deliberately not a full TeX renderer: strip document structure, retain math delimiters.
  const stripped=latex.replace(/\\label\s*\{[^}]*\}/g,"")
    .replace(/\\(?:begin|end)\s*\{[^}]*\}(?:\[[^\]]*\])?/g,"\n")
    .replace(/\\(?:chapter|section|subsection|subsubsection|paragraph)\*?(?:\[[^\]]*\])?\s*\{([^{}]*)\}/g,"\n\n$1\n")
    .replace(/\\(?:emph|textbf|textit)\s*\{([^{}]*)\}/g,"$1")
    .replace(/\n{4,}/g,"\n\n");
  const box=$("simplified");box.textContent=stripped;
  if(window.renderMathInElement){try{window.renderMathInElement(box,{delimiters:[{left:"$$",right:"$$",display:true},{left:"\\[",right:"\\]",display:true},{left:"$",right:"$",display:false},{left:"\\(",right:"\\)",display:false}],throwOnError:false});}catch(_){}}
}
function addCurrent(){
  const d=state.currentData;if(!d)return;
  const isEntity=!!d.entity;const id=isEntity?d.entity.id:state.currentModule;
  const key=(isEntity?"entity:":"module:")+id;
  if(state.selected.has(key)){state.selected.delete(key);toast("Usunięto z zestawu.");}
  else{state.selected.set(key,{id,kind:isEntity?"entity":"module",title:isEntity?(d.entity.title||d.entity.kind):d.module.title,module:state.currentModule});toast("Dodano do zestawu.");}
  renderReader();renderSelection();
}
function positionReferenceTip(anchor){
  const r=anchor.getBoundingClientRect(), tip=$("referenceTip");
  tip.classList.remove("hidden");
  tip.style.left=Math.max(8,Math.min(window.innerWidth-448,r.left))+"px";
  tip.style.top=Math.max(8,Math.min(window.innerHeight-tip.offsetHeight-12,r.bottom+8))+"px";
}
async function previewLabel(label,anchor){
  const request=++state.tooltipKey;
  state.tooltipData=null;
  // Do not leave a stale result on screen while the next request is pending.
  const body=$("tipBody");body.replaceChildren();
  body.append(node("p",{className:"tip-meta"},"Ładowanie etykiety: "+label));
  $("tipOpen").disabled=true;
  positionReferenceTip(anchor);
  try{
    const result=await api(`/api/labels/${encodeURIComponent(label)}`);
    if(request!==state.tooltipKey)return;
    state.tooltipData=result;
    $("tipOpen").disabled=Boolean(result.ambiguous);
    body.replaceChildren();
    if(result.ambiguous){
      body.append(node("h3",{},"Etykieta występuje w kilku rozdziałach"));
      body.append(node("p",{className:"tip-meta"},`${label} · wybierz właściwy rozdział`));
      for(const choice of result.candidates){
        const target=node("button",{className:"ref-choice"},`${choice.document_id}: ${choice.title} (wiersz ${choice.line})`);
        target.addEventListener("click",()=>{closeTip();openModule(choice.document_id);});
        body.append(target);
      }
    }else{
      body.append(node("h3",{},result.entity_title || result.title || label));
      body.append(node("p",{className:"tip-meta"},`${label} · ${result.document_id} · wiersz ${result.line}`));
      body.append(node("div",{className:"tip-code"},crop(result.latex,1100)));
    }
    positionReferenceTip(anchor);
  }catch(e){
    if(request!==state.tooltipKey)return;
    state.tooltipData=null;
    $("tipOpen").disabled=true;
    body.replaceChildren();
    body.append(node("h3",{},"Nie znaleziono cytowanej etykiety"));
    body.append(node("p",{className:"tip-meta"},label));
    body.append(node("p",{},"Cel odsyłacza nie jest dostępny w indeksie. Wymaga audytu źródła LaTeX."));
    positionReferenceTip(anchor);
  }
}
function closeTip(){state.tooltipKey++;state.tooltipData=null;$("referenceTip").classList.add("hidden");}
async function openLabel(label){
  try{
    const result=state.tooltipData?.name===label?state.tooltipData:await api(`/api/labels/${encodeURIComponent(label)}`);
    closeTip();if(result.ambiguous){toast("Etykieta jest niejednoznaczna. Wybierz rozdział w podglądzie odsyłacza.");return;}
    if(result.entity_id)await openEntity(result.entity_id);else await openModule(result.document_id);
  }catch(e){toast(e.message);}
}
function setupSearch(){
  const input=$("searchInput");let task;
  input.addEventListener("input",()=>{clearTimeout(task);const q=input.value.trim();if(q.length<2){$("searchResults").classList.add("hidden");return;}task=setTimeout(()=>performSearch(q),240);});
  input.addEventListener("keydown",e=>{if(e.key==="Enter"){e.preventDefault();clearTimeout(task);performSearch(input.value.trim());}if(e.key==="Escape")$("searchResults").classList.add("hidden");});
  document.addEventListener("click",e=>{if(!e.target.closest(".header-search"))$("searchResults").classList.add("hidden");});
}
async function performSearch(q){
  if(!q)return;
  try{
    const result=await api(`/api/search?q=${encodeURIComponent(q)}&limit=25`);
    if($("searchInput").value.trim()!==q)return;
    const list=$("searchResults");list.replaceChildren();
    if(!result.items.length)list.append(node("p",{className:"empty-sub"},"Nie znaleziono dopasowań."));
    for(const e of result.items){
      const b=node("button",{className:"search-hit"});b.append(node("strong",{},crop(e.title||e.excerpt,95)),node("small",{},`${e.document_id} · ${e.kind} · wiersz ${e.start_line}`));
      b.addEventListener("click",()=>{if(e.kind==="module")openModule(e.id);else openEntity(e.id);list.classList.add("hidden");});list.append(b);
    }
    list.classList.remove("hidden");
  }catch(e){toast(e.message);}
}
function renderSelection(){
  const list=$("selectionList");list.replaceChildren();
  $("selectedCount").textContent=state.selected.size+" elementów";
  if(!state.selected.size){list.append(node("div",{className:"empty-sub"},"Zestaw jest pusty. Wybierz moduły lub fragmenty z Czytnika."));return;}
  for(const [key,x] of state.selected){
    const line=node("div",{className:"selection-item"});const info=node("div");
    info.append(node("strong",{},x.title),node("small",{},`${x.kind==="module"?"Rozdział":"Fragment"} · ${x.module} · ${x.id}`));
    const del=node("button",{title:"Usuń z zestawu"},"×");del.addEventListener("click",()=>{state.selected.delete(key);renderSelection();if(state.currentData)renderReader();});
    line.append(info,del);list.append(line);
  }
}
function selectedManifest(){return {format:"matlib-selection-v1",modules:[...state.selected.values()].filter(x=>x.kind==="module").map(x=>x.id),entities:[...state.selected.values()].filter(x=>x.kind==="entity").map(x=>x.id)};}
function downloadManifest(){
  const blob=new Blob([JSON.stringify(selectedManifest(),null,2)],{type:"application/json"});const url=URL.createObjectURL(blob);
  const a=node("a",{download:"biblioteka_zestaw.json",href:url});document.body.append(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(url),1000);
}
function generationPayload(){
  return {...selectedManifest(),title:$('generatorTitle').value.trim() || 'Mój skrypt matematyczny',closure_depth:Number($('generatorClosure').value)};
}
async function checkSelection(){
  const payload=generationPayload();
  if(!payload.modules.length&&!payload.entities.length){toast('Wybierz rozdział lub obiekt.');return;}
  try{
    const result=await api('/api/generate/manifest',{method:'POST',body:JSON.stringify(payload)});
    const root=$('planResult');root.replaceChildren();const card=node('div',{className:'plan-card'});
    card.append(node('h3',{},'Weryfikacja generatora'));
    card.append(node('p',{},`${result.modules.length} modułów · ${result.references_internal} odsyłaczy wewnętrznych · ${result.references_external} odsyłaczy przez xr-hyper · ${Object.keys(result.external_targets).length} plików referencyjnych.`));
    if(result.preamble_warning)card.append(node('p',{},result.preamble_warning));
    if(Object.keys(result.fragments).length)card.append(node('p',{},'Fragmenty: sprawdzono odsyłacze tylko w wybranych obiektach. Semantyczna samowystarczalność wymaga audytu.'));
    if(Object.keys(result.external_targets).length){
      const ul=node('ul');for(const [mod,labels] of Object.entries(result.external_targets))ul.append(node('li',{},`${mod}: ${labels.join(', ')}`));
      card.append(node('strong',{},'Dokumenty referencyjne:'),ul);
    }
    card.append(node('p',{},'Pliki aux/*.aux powstaną po uruchomieniu build.ps1 lub build.sh. PDF nie jest kompilowany przez serwer.'));
    root.append(card);
  }catch(e){toast(e.message);}
}
async function generateZip(){
  const payload=generationPayload();
  if(!payload.modules.length&&!payload.entities.length){toast('Wybierz rozdział lub obiekt.');return;}
  const button=$('generateZip');button.disabled=true;button.textContent='Generowanie…';
  try{
    const response=await fetch('/api/generate',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(payload)});
    if(!response.ok){let error='HTTP '+response.status;try{error=(await response.json()).detail||error;}catch(_){}throw new Error(error);}
    const blob=await response.blob();const url=URL.createObjectURL(blob);
    const a=node('a',{href:url,download:'skrypt_matematyczny.zip'});document.body.append(a);a.click();a.remove();
    setTimeout(()=>URL.revokeObjectURL(url),1500);toast('Projekt LaTeX został wygenerowany.');
  }catch(e){toast(e.message);}finally{button.disabled=false;button.textContent='Pobierz ZIP';}
}

async function createDraft(){
  const payload=generationPayload();
  if(!payload.modules.length&&!payload.entities.length){toast('Wybierz rozdział lub obiekt.');return;}
  const button=$('createDraft');button.disabled=true;button.textContent='Tworzenie szkicu…';
  try{
    const url='/api/drafts'+(state.draftSession?'?session_id='+encodeURIComponent(state.draftSession):'');
    const draft=await api(url,{method:'POST',body:JSON.stringify(payload)});
    state.draftSession=draft.session_id;
    const host=$('draftResult');host.replaceChildren();
    host.append(node('strong',{},'Szkic tymczasowy · '+Math.ceil(draft.size_bytes/1024)+' KB'));
    const link=node('a',{href:draft.download_url,download:'mathematical_draft.zip'},'Pobierz szkic');
    const saveButton=node('button',{className:'secondary-btn'},'Zapisz na stałe');
    saveButton.addEventListener('click',saveDraft);
    const discardButton=node('button',{className:'ghost-btn'},'Usuń szkic');
    discardButton.addEventListener('click',discardDraft);
    const actions=node('div',{className:'draft-actions'});actions.append(link,saveButton,discardButton);host.append(actions);
    host.append(node('small',{},'Niezapisany szkic zostanie usunięty przy zamknięciu karty (X). Zapisane projekty pozostają na dysku serwera.'));
  }catch(e){toast(e.message);}finally{button.disabled=false;button.textContent='Utwórz szkic';}
}
async function saveDraft(){
  if(!state.draftSession)return;
  try{
    await api('/api/drafts/'+state.draftSession+'/save',{method:'POST'});
    toast('Zapisano projekt na stałe. Zamknięcie karty go nie usunie.');
    await showSavedProjects();
  }catch(e){toast(e.message);}
}
async function discardDraft(){
  if(!state.draftSession)return;
  const id=state.draftSession;state.draftSession=null;
  try{await api('/api/drafts/'+id+'/close',{method:'POST'});}catch(e){toast(e.message);}
  $('draftResult').replaceChildren();
}
async function showSavedProjects(){
  const host=$('savedProjects');host.replaceChildren();
  try{
    const {items}=await api('/api/projects');if(!items.length)return;
    host.append(node('h3',{},'Zapisane projekty'));
    for(const item of items.slice(0,40)){
      const line=node('div',{className:'saved-project-item'});
      line.append(node('span',{},item.title || 'Projekt'));
      line.append(node('a',{href:item.download_url,download:'saved_mathematical_project.zip'},'Pobierz'));
      host.append(line);
    }
  }catch(e){toast(e.message);}
}
function closeUnsavedDraft(){
  if(!state.draftSession)return;
  const session=state.draftSession;state.draftSession=null;
  const url='/api/drafts/'+encodeURIComponent(session)+'/close';
  // sendBeacon is best-effort. The server also deletes orphaned drafts by TTL.
  if(!navigator.sendBeacon || !navigator.sendBeacon(url,new Blob([]))){
    fetch(url,{method:'POST',keepalive:true}).catch(()=>{});
  }
}
function setSelect(select, items){select.replaceChildren();for(const item of items){const opt=node("option",{value:item.name},item.name);select.append(opt);}}
async function loadGraph(){
  if(!state.domains.length)return;
  const left=$("graphLeft").value,right=$("graphRight").value;
  const level=$("graphLevel").value;
  try{
    const data=await api(`/api/graph?left=${encodeURIComponent(left)}&right=${encodeURIComponent(right)}&granularity=${level}&min_weight=${Number($("graphMin").value)||1}&max_edges=65`);
    state.graph=data;$("graphSummary").textContent=`${data.nodes.length} węzłów · ${data.edges.length} par powiązanych odsyłaczami${data.truncated?" · widok ograniczony do 65 par":""} · źródło: jawne odsyłacze LaTeX`;
    renderGraph(data);
  }catch(e){toast(e.message);}
}
function openGraphNode(n){if(n.entity_id && n.entity_id!==n.module)openEntity(n.entity_id);else openModule(n.module);}
function renderGraph(data){
  const host=$("graphCanvas");host.replaceChildren();
  if(!data.edges.length){host.append(node("div",{className:"empty-sub"},"Brak bezpośrednich odsyłaczy między tymi dziedzinami. Nie oznacza to braku powiązań matematycznych."));return;}
  const left=data.nodes.filter(n=>n.side==="left"),right=data.nodes.filter(n=>n.side==="right");
  const nRows=Math.max(left.length,right.length,5);
  const height=Math.max(410,85+nRows*48);
  // Prefer Cytoscape when online; offline fallback stays fully functional.
  if(typeof window.cytoscape==="function"){
    host.style.height=Math.min(700,height)+"px";
    const elements=[...data.nodes.map(n=>({data:{id:n.id,label:crop(n.label,30),side:n.side,original:n}})),
                    ...data.edges.map((e,i)=>({data:{id:"e"+i,source:e.source,target:e.target,weight:e.weight}}))];
    const positions={};left.forEach((n,i)=>positions[n.id]={x:110,y:60+i*48});right.forEach((n,i)=>positions[n.id]={x:690,y:60+i*48});
    try{
      const cy=window.cytoscape({container:host,elements,layout:{name:"preset",positions,fit:true,padding:50},
        style:[{selector:"node",style:{"shape":"round-rectangle","width":"label","height":36,"padding":"12px","background-color":"#d4edf0","border-color":"#66a4af","border-width":1,"label":"data(label)","color":"#17465a","font-size":12}},{selector:'node[side="right"]',style:{"background-color":"#e8ecf9","border-color":"#aaaed4"}},{selector:"edge",style:{"width":"mapData(weight,1,20,1,5)","line-color":"#a4bdc8","opacity":.64,"curve-style":"bezier","target-arrow-shape":"triangle","target-arrow-color":"#91aabb"}}],userZoomingEnabled:true,boxSelectionEnabled:false});
      cy.on("tap","node",event=>openGraphNode(event.target.data("original")));
      state.cy=cy;return;
    }catch(e){host.replaceChildren();}
  }
  host.style.height="";
  const NS="http://www.w3.org/2000/svg",svg=document.createElementNS(NS,"svg");svg.setAttribute("viewBox",`0 0 920 ${height}`);svg.setAttribute("height",String(height));
  const pos={};const distribute=(arr,x)=>arr.forEach((n,i)=>pos[n.id]={x,y:65+i*(Math.max(46,(height-100)/Math.max(1,arr.length-1)))});
  distribute(left,25);distribute(right,530);
  for(const e of data.edges){
    const a=pos[e.source],b=pos[e.target];if(!a||!b)continue;
    const path=document.createElementNS(NS,"path");path.setAttribute("d",`M ${a.x+320} ${a.y} C 415 ${a.y}, 455 ${b.y}, ${b.x} ${b.y}`);
    path.setAttribute("fill","none");path.setAttribute("stroke","#9ebbc5");path.setAttribute("stroke-width",String(1+Math.min(4,e.weight/2)));path.setAttribute("opacity",".72");svg.append(path);
  }
  for(const n of data.nodes){
    const {x,y}=pos[n.id];const g=document.createElementNS(NS,"g");g.setAttribute("class","fallback-node");
    const rect=document.createElementNS(NS,"rect");rect.setAttribute("x",String(x));rect.setAttribute("y",String(y-19));rect.setAttribute("rx","8");rect.setAttribute("width","320");rect.setAttribute("height","38");rect.setAttribute("stroke",n.side==="left"?"#84b2b9":"#b0b9d1");rect.setAttribute("fill",n.side==="left"?"#e7f5f6":"#edf0fa");
    const label=document.createElementNS(NS,"text");label.setAttribute("x",String(x+10));label.setAttribute("y",String(y+4));label.setAttribute("fill","#34566b");label.setAttribute("font-size","12");label.textContent=`${n.module} · ${crop(n.label,41)}`;
    const title=document.createElementNS(NS,"title");title.textContent=n.label;
    g.append(rect,label,title);g.addEventListener("click",()=>openGraphNode(n));svg.append(g);
  }
  host.append(svg);
}
async function findPath(){
  const source=$("pathFrom").value.trim(),target=$("pathTo").value.trim();
  if(!source||!target){toast("Wpisz dwa identyfikatory modułów.");return;}
  try{
    const data=await api(`/api/graph/path?source=${encodeURIComponent(source)}&target=${encodeURIComponent(target)}`);
    const box=$("pathResult");box.replaceChildren();
    if(!data.found){box.textContent="Nie istnieje ścieżka złożona z jawnych odsyłaczy między tymi modułami.";return;}
    box.append(document.createTextNode("Ścieżka o długości "+data.steps.length+": "));
    data.modules.forEach((m,i)=>{if(i)box.append(document.createTextNode(" → "));const btn=node("button",{title:m.title},m.id);btn.addEventListener("click",()=>openModule(m.id));box.append(btn);});
  }catch(e){toast(e.message);}
}
async function init(){
  try{
    const [domains,mods,stats]=await Promise.all([api("/api/domains"),api("/api/modules?limit=500"),api("/api/stats")]);
    state.domains=domains;state.modules=mods.items;
    $("dbStatus").textContent="Baza połączona";$("dbStatus").classList.add("connected");
    $("statPill").textContent=stats.documents+" rozdziałów";
    for(const n of ["graphLeft","graphRight"])setSelect($(n),domains);
    const a=domains.find(d=>d.name==="geometria algebraiczna"),b=domains.find(d=>d.name==="geometria algebraiczna / topologia");
    $("graphLeft").value=(a||domains[0]).name;$("graphRight").value=(b||domains.at(-1)).name;
    state.expandedDomains.add($("graphLeft").value);
    renderTree();renderSelection();await showSavedProjects();
  }catch(e){$("dbStatus").textContent="Brak indeksu";toast(e.message);}
}
function listeners(){
  document.querySelectorAll(".tab").forEach(b=>b.addEventListener("click",()=>activateTab(b.dataset.tab)));
  $("granularity").addEventListener("change",e=>{state.granularity=e.target.value;renderTree();});
  $("addCurrent").addEventListener("click",addCurrent);
  $("openFirst").addEventListener("click",()=>{if(state.modules.length)openModule(state.modules[0].id);});
  $("openGraphQuick").addEventListener("click",()=>activateTab("graph"));
  $("togglePreview").addEventListener("click",()=>{state.simplified=!state.simplified;renderReader();});
  $("showFull").addEventListener("click",()=>{if(state.currentEntity)openEntity(state.currentEntity,true);else if(state.currentModule)openModule(state.currentModule,true);});
  $("closeTip").addEventListener("click",closeTip);
  $("tipOpen").addEventListener("click",()=>{const x=state.tooltipData;if(x)openLabel(x.name);});
  $("referenceTip").addEventListener("mouseleave",closeTip);
  document.addEventListener("keydown",e=>{if(e.key==="Escape")closeTip();});
  $("drawGraph").addEventListener("click",loadGraph);$("findPath").addEventListener("click",findPath);
  $("checkSelection").addEventListener("click",checkSelection);$("generateZip").addEventListener("click",generateZip);$("createDraft").addEventListener("click",createDraft);$("saveManifest").addEventListener("click",downloadManifest);
  window.addEventListener("pagehide",event=>{if(!event.persisted)closeUnsavedDraft();});
  // Some browsers do not dispatch pagehide when a tab is closed; keep an idempotent fallback.
  window.addEventListener("beforeunload",closeUnsavedDraft);
  setInterval(()=>{if(state.draftSession)fetch("/api/drafts/"+encodeURIComponent(state.draftSession)+"/heartbeat",{method:"POST"}).catch(()=>{});},15*60*1000);
  $("clearSelection").addEventListener("click",()=>{state.selected.clear();renderSelection();if(state.currentData)renderReader();$("planResult").replaceChildren();});
  $("showExplorer").addEventListener("click",()=>$("explorer").classList.add("visible"));
  $("closeExplorer").addEventListener("click",()=>$("explorer").classList.remove("visible"));
  setupSearch();
}
listeners();init();
