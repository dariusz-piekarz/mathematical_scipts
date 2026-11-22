"use strict";
/* HTML/CSS/JS client for read-only mathematical library.
   No untrusted TeX or API text is inserted via innerHTML. */
const $ = id => document.getElementById(id);
const state = {
  domains:[], modules:[], outlines:new Map(), expandedDomains:new Set(), expandedModules:new Set(),
  currentModule:null, currentEntity:null, currentData:null, selected:new Map(),
  tab:"reader", granularity:"module", simplified:false, tooltipData:null, leanEpoch:0, leanFragment:null, leanRunner:null,
  tooltipKey:0, graph:null, conceptGraph:null, conceptEpoch:0, renderEpoch:0, draftSession:null,
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
  for(const k of ["reader","lean","graph","concepts","selection"])$("view-"+k).classList.toggle("hidden",k!==name);
  if(name==="selection")renderSelection();
  if(name==="graph" && !state.graph)loadGraph();
  if(name==="concepts" && !state.conceptGraph)loadConceptGraph();
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
      const lab=raw.trim(), sourceDocument=state.currentModule;if(!lab){container.append(document.createTextNode(raw));return;}
      const b=node("button",{className:"ref-link",title:"Podgląd etykiety: "+lab},lab);
      b.addEventListener("mouseenter",()=>previewLabel(lab,b,sourceDocument));
      b.addEventListener("focus",()=>previewLabel(lab,b));
      b.addEventListener("mouseleave",()=>{const key=state.tooltipKey;setTimeout(()=>{if(key===state.tooltipKey && state.tooltipAnchor===b && !$("referenceTip").matches(":hover"))closeTip();},240);});
      b.addEventListener("click",()=>openLabel(lab,sourceDocument));container.append(b);
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
  const firstLine=entity?data.entity.start_line:1;
  $("rangeStart").value=firstLine;
  // A terminal newline ends the last source line; it is not an extra line.
  const lineCount=data.latex.length
    ? data.latex.split("\n").length-(data.latex.endsWith("\n")?1:0) : 0;
  $("rangeEnd").value=firstLine+Math.max(0,lineCount-1);
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
function addLineRange(startLine,endLine){
  const module=state.currentModule;
  if(!module||!Number.isSafeInteger(startLine)||!Number.isSafeInteger(endLine)||
     startLine<1||endLine<startLine){toast("Podaj poprawny zakres wierszy.");return;}
  const key="lines:"+module+":"+startLine+"-"+endLine;
  if(state.selected.has(key)){toast("Ten wycinek jest już w zestawie.");return;}
  state.selected.set(key,{
    id:key,kind:"lines",module,start_line:startLine,end_line:endLine,
    title:"Wiersze "+startLine+"–"+endLine+" · "+module
  });
  renderSelection();toast("Dodano wycinek do zestawu.");
}
function addExcerpt(){
  const data=state.currentData,source=$("latexSource"),sel=window.getSelection();
  if(!data||state.simplified||!sel||sel.isCollapsed||!sel.rangeCount){
    toast("Zaznacz fragment tekstu w widoku źródła LaTeX.");return;
  }
  const range=sel.getRangeAt(0);
  if(!source.contains(range.startContainer)||!source.contains(range.endContainer)){
    toast("Zaznaczenie musi mieścić się w źródle LaTeX.");return;
  }
  const prefix=range.cloneRange();
  prefix.selectNodeContents(source);
  prefix.setEnd(range.startContainer,range.startOffset);
  const start=prefix.toString().length,end=start+range.toString().length;
  if(end<=start||end>data.latex.length){
    toast("Nie można wyznaczyć wierszy zaznaczenia.");return;
  }
  const first=data.entity?data.entity.start_line:1;
  const countNewlines=text=>(text.match(/\n/g)||[]).length;
  const startLine=first+countNewlines(data.latex.slice(0,start));
  const endLine=first+countNewlines(data.latex.slice(0,end-1));
  addLineRange(startLine,endLine);
  sel.removeAllRanges();
}
function addRange(){
  addLineRange(Number($("rangeStart").value),Number($("rangeEnd").value));
}
function positionReferenceTip(anchor){
  const r=anchor.getBoundingClientRect(), tip=$("referenceTip");
  tip.classList.remove("hidden");
  tip.style.left=Math.max(8,Math.min(window.innerWidth-448,r.left))+"px";
  tip.style.top=Math.max(8,Math.min(window.innerHeight-tip.offsetHeight-12,r.bottom+8))+"px";
}
async function previewLabel(label,anchor,sourceDocument=null){
  const request=++state.tooltipKey;
  state.tooltipAnchor=anchor;
  state.tooltipData=null;
  // Do not leave a stale result on screen while the next request is pending.
  const body=$("tipBody");body.replaceChildren();
  body.append(node("p",{className:"tip-meta"},"Ładowanie etykiety: "+label));
  $("tipOpen").disabled=true;
  positionReferenceTip(anchor);
  try{
    const result=await api(`/api/labels/${encodeURIComponent(label)}`+(sourceDocument?`?source_document=${encodeURIComponent(sourceDocument)}`:""));
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
function closeTip(){state.tooltipKey++;state.tooltipData=null;state.tooltipAnchor=null;$("referenceTip").classList.add("hidden");}
async function openLabel(label,sourceDocument=null){
  try{
    const result=state.tooltipData?.name===label && (!sourceDocument || state.tooltipData.source_document===sourceDocument)?state.tooltipData:await api(`/api/labels/${encodeURIComponent(label)}`+(sourceDocument?`?source_document=${encodeURIComponent(sourceDocument)}`:""));
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
    const graphButton=node("button",{className:"search-hit search-concept-action"},"Zbuduj graf pojęcia: "+q);
    graphButton.addEventListener("click",()=>{list.classList.add("hidden");openConceptSearch(q);});
    list.append(graphButton);
    if(!result.items.length)list.append(node("p",{className:"empty-sub"},"Nie znaleziono dopasowań."));
    for(const e of result.items){
      const b=node("button",{className:"search-hit"});b.append(node("strong",{},crop(e.title||e.excerpt,95)),node("small",{},`${e.document_id} · ${e.kind} · wiersz ${e.start_line}`));
      b.addEventListener("click",()=>{if(e.kind==="module")openModule(e.id);else openEntity(e.id);list.classList.add("hidden");});list.append(b);
    }
    list.classList.remove("hidden");
  }catch(e){toast(e.message);}
}
function moveSelected(key,step){
  const entries=[...state.selected.entries()];
  const index=entries.findIndex(([k])=>k===key),next=index+step;
  if(index<0||next<0||next>=entries.length)return;
  [entries[index],entries[next]]=[entries[next],entries[index]];
  state.selected=new Map(entries);renderSelection();
}
function renderSelection(){
  const list=$("selectionList");list.replaceChildren();
  $("selectedCount").textContent=state.selected.size+" elementów";
  if(!state.selected.size){
    list.append(node("div",{className:"empty-sub"},"Zestaw jest pusty. Wybierz rozdział, obiekt lub zaznacz wiersze LaTeX w Czytniku."));
    return;
  }
  const keys=[...state.selected.keys()];
  for(const [index,key] of keys.entries()){
    const x=state.selected.get(key);
    const line=node("div",{className:"selection-item"});const info=node("div");
    const kind=x.kind==="module"?"Rozdział":x.kind==="lines"?"Wycinek wierszy":"Obiekt";
    const ref=x.kind==="lines"?("wiersze "+x.start_line+"–"+x.end_line):x.id;
    info.append(node("strong",{},x.title),node("small",{},kind+" · "+x.module+" · "+ref));
    const controls=node("div",{className:"selection-controls"});
    const up=node("button",{title:"Przesuń wyżej","aria-label":"Przesuń wyżej"},"↑");
    up.disabled=index===0;up.addEventListener("click",()=>moveSelected(key,-1));
    const down=node("button",{title:"Przesuń niżej","aria-label":"Przesuń niżej"},"↓");
    down.disabled=index===keys.length-1;down.addEventListener("click",()=>moveSelected(key,1));
    const del=node("button",{title:"Usuń z zestawu","aria-label":"Usuń z zestawu"},"×");
    del.addEventListener("click",()=>{state.selected.delete(key);renderSelection();if(state.currentData)renderReader();});
    controls.append(up,down,del);line.append(info,controls);list.append(line);
  }
}
function selectedManifest(){
  const selected=[...state.selected.values()];
  return {
    format:"matlib-selection-v2",
    items:selected.map(x=>x.kind==="lines"?
      {kind:"lines",module:x.module,start_line:x.start_line,end_line:x.end_line}:
      {kind:x.kind,id:x.id}),
    modules:selected.filter(x=>x.kind==="module").map(x=>x.id),
    entities:selected.filter(x=>x.kind==="entity").map(x=>x.id)
  };
}
function downloadManifest(){
  const manifest={...selectedManifest(),title:$("generatorTitle").value.trim(),
                  closure_depth:Number($("generatorClosure").value)};
  const blob=new Blob([JSON.stringify(manifest,null,2)],{type:"application/json"});
  const url=URL.createObjectURL(blob);
  const a=node("a",{download:"biblioteka_zestaw.json",href:url});
  document.body.append(a);a.click();a.remove();
  setTimeout(()=>URL.revokeObjectURL(url),1000);
}
function generationPayload(){
  const {modules,entities,...selection}=selectedManifest();
  return {...selection,title:$("generatorTitle").value.trim()||"Mój skrypt matematyczny",
          closure_depth:Number($("generatorClosure").value)};
}
async function checkSelection(){
  const payload=generationPayload();
  if(!payload.items.length){toast('Wybierz rozdział lub obiekt.');return;}
  try{
    const result=await api('/api/generate/manifest',{method:'POST',body:JSON.stringify(payload)});
    const root=$('planResult');root.replaceChildren();const card=node('div',{className:'plan-card'});
    card.append(node('h3',{},'Weryfikacja generatora'));
    card.append(node('p',{},`${result.modules.length} modułów · ${result.references_internal} odsyłaczy wewnętrznych · ${result.references_external} odsyłaczy przez xr-hyper · ${Object.keys(result.external_targets).length} plików referencyjnych.`));
    if(result.preamble_warning)card.append(node('p',{},result.preamble_warning));
    if(Object.keys(result.fragments).length)card.append(node('p',{},'Fragmenty: sprawdzono odsyłacze wewnątrz wybranych zakresów. Kontekst matematyczny i kompletność środowisk LaTeX wymagają weryfikacji.'));
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
  if(!payload.items.length){toast('Wybierz rozdział lub obiekt.');return;}
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
  if(!payload.items.length){toast('Wybierz rozdział lub obiekt.');return;}
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

function openConceptSearch(term){
  $("conceptSearch").value=term;
  activateTab("concepts");
  loadConceptGraph();
}
async function loadConceptGraph(){
  const q=$("conceptSearch").value.trim();
  if(q.length<2){toast("Wpisz co najmniej dwa znaki.");return;}
  const epoch=++state.conceptEpoch;
  $("conceptSummary").textContent="Wyszukiwanie wystąpień pojęcia: "+q+"…";
  try{
    const count=Number($("conceptLimit").value);
    const data=await api("/api/concepts/graph?q="+encodeURIComponent(q)+"&max_occurrences="+count);
    if(epoch!==state.conceptEpoch || $("conceptSearch").value.trim()!==q)return;
    state.conceptGraph=data;
    $("conceptSummary").textContent=data.matches_total+" dopasowań tekstowych · "+
      data.occurrences_shown+" widocznych wystąpień · "+
      data.relationships+" zweryfikowanych relacji katalogowych"+
      (data.truncated?" · ograniczono liczbę wyników":"");
    renderConceptGraph(data);
    renderConceptEvidence(data);
  }catch(e){
    if(epoch!==state.conceptEpoch)return;
    $("conceptSummary").textContent="Nie można zbudować grafu.";
    toast(e.message);
  }
}
function openConceptNode(n){
  if(n.type==="concept"){
    $("conceptSearch").value=n.term;
    loadConceptGraph();
  }else if(n.entity_id){
    openEntity(n.entity_id);
  }else if(n.module){
    openModule(n.module);
  }
}
function renderConceptGraph(data){
  const host=$("conceptCanvas");host.replaceChildren();
  const concepts=data.nodes.filter(n=>n.type==="concept");
  const occurrences=data.nodes.filter(n=>n.type==="occurrence");
  const root=concepts.find(c=>c.id===data.root);
  if(!root)return;
  const ordered=[root,...concepts.filter(c=>c.id!==data.root)];
  const positions={};positions[root.id]={x:35,y:70};
  let y=70;
  const groups=[];
  for(const concept of ordered){
    const entries=occurrences.filter(o=>o.concept===concept.id);
    const height=Math.max(75,entries.length*54);
    const center=y+(height-54)/2;
    if(concept.id!==root.id)positions[concept.id]={x:330,y:center};
    entries.forEach((o,i)=>positions[o.id]={x:690,y:y+i*54});
    groups.push({concept,entries,start:y,height});
    y+=height+35;
  }
  const totalHeight=Math.max(410,y+20),W=1120,NS="http://www.w3.org/2000/svg";
  const svgEl=(tag,attrs={},content)=>{
    const el=document.createElementNS(NS,tag);
    for(const [key,value] of Object.entries(attrs))el.setAttribute(key,String(value));
    if(content!==undefined)el.textContent=String(content);
    return el;
  };
  const svg=svgEl("svg",{viewBox:"0 0 "+W+" "+totalHeight,
    height:totalHeight,role:"group","aria-label":"Graf pojęć: "+data.query});
  const defs=svgEl("defs");
  const marker=svgEl("marker",{id:"concept-arrow",viewBox:"0 0 10 10",refX:"9",refY:"5",
    markerWidth:"6",markerHeight:"6",orient:"auto-start-reverse"});
  marker.append(svgEl("path",{d:"M 0 0 L 10 5 L 0 10 z",fill:"#278397"}));
  defs.append(marker);svg.append(defs);
  for(const group of groups){
    if(group.concept.id===data.root)continue;
    const separator=svgEl("line",{x1:298,y1:group.start-18,x2:1090,
      y2:group.start-18,stroke:"#e8edf2","stroke-width":1});
    svg.append(separator);
  }
  for(const edge of data.edges){
    const a=positions[edge.source],b=positions[edge.target];
    if(!a||!b)continue;
    const isOccurrence=edge.type==="occurrence";
    const aWidth=a.x===690?392:244;
    const bWidth=b.x===690?392:244;
    const x1=a.x+aWidth,x2=b.x,y1=a.y,y2=b.y;
    const mid=(x1+x2)/2;
    const path=svgEl("path",{d:"M "+x1+" "+y1+" C "+mid+" "+y1+", "+mid+" "+y2+", "+x2+" "+y2,
      fill:"none",stroke:isOccurrence?"#a6b4c7":"#278397",
      "stroke-width":isOccurrence?1.5:2.2,"stroke-dasharray":isOccurrence?"5 5":"none",
      opacity:isOccurrence?".65":".85"});
    if(!isOccurrence)path.setAttribute("marker-end","url(#concept-arrow)");
    path.append(svgEl("title",{},edge.label+(edge.explanation?": "+edge.explanation:"")));
    svg.append(path);
  }
  for(const n of data.nodes){
    const pos=positions[n.id];if(!pos)continue;
    const concept=n.type==="concept",isRoot=n.id===data.root,w=concept?244:392;
    const group=svgEl("g",{class:"concept-svg-node",tabindex:"0",role:"button",
      "aria-label":concept?n.label+" — pokaż powiązania":n.module+", "+n.label+", wiersz "+n.line});
    group.append(svgEl("rect",{x:pos.x,y:pos.y-21,width:w,height:42,rx:9,
      fill:isRoot?"#d5edf0":concept?"#e7eafb":"#ffffff",
      stroke:isRoot?"#157b8b":concept?"#a9b3dc":"#b7cad7","stroke-width":isRoot?2:1.2}));
    group.append(svgEl("text",{x:pos.x+11,y:pos.y+(concept?4:-3),fill:"#29475d",
      "font-size":concept?13:12,"font-weight":concept?"700":"600"},
      crop(concept?n.label:(n.module+" · "+n.label),concept?32:48)));
    if(!concept)group.append(svgEl("text",{x:pos.x+11,y:pos.y+13,
      fill:"#8192a3","font-size":10},
      "Wiersz "+n.line+" · "+crop(n.matched,31)));
    if(concept)group.append(svgEl("title",{},n.label+" · "+n.modules_total+" rozdziałów"));
    else group.append(svgEl("title",{},n.snippet));
    group.addEventListener("click",()=>openConceptNode(n));
    group.addEventListener("keydown",e=>{
      if(e.key==="Enter"||e.key===" "){e.preventDefault();openConceptNode(n);}
    });
    svg.append(group);
  }
  host.append(svg);
  if(!occurrences.length)host.append(node("p",{className:"empty-sub"},
    "Nie znaleziono tekstowych wystąpień w zaindeksowanych rozdziałach. Relacje katalogowe nie oznaczają obecności w tekście."));
}
function renderConceptEvidence(data){
  const relations=$("conceptRelations");relations.replaceChildren();
  const evidence=$("conceptEvidence");evidence.replaceChildren();
  const all=new Map(data.nodes.filter(n=>n.type==="concept").map(n=>[n.id,n]));
  const relationEdges=data.edges.filter(e=>e.type!=="occurrence");
  if(relationEdges.length){
    const heading=node("h2",{className:"small-heading"},"Relacje matematyczne");
    relations.append(heading);
    for(const edge of relationEdges){
      const a=all.get(edge.source),b=all.get(edge.target);
      const line=node("div",{className:"concept-relation"});
      line.append(node("strong",{},(a?a.label:edge.source)+" "+
        (edge.type==="equivalent"?"⇔":"⇒")+" "+(b?b.label:edge.target)));
      line.append(node("small",{},edge.label+" · "+edge.explanation));
      relations.append(line);
    }
  }
  for(const concept of data.nodes.filter(n=>n.type==="concept")){
    const entries=data.nodes.filter(n=>n.type==="occurrence"&&n.concept===concept.id);
    const section=node("section",{className:"concept-group"});
    section.append(node("h3",{},concept.label+" · "+concept.modules_total+
      " rozdziałów · "+concept.matches_total+" dopasowań"));
    if(!entries.length)section.append(node("p",{className:"concept-empty"},"Brak poświadczonych wystąpień w aktualnym indeksie."));
    for(const item of entries){
      const button=node("button",{className:"concept-occurrence"});
      button.append(node("strong",{},item.module+" · "+(item.label||item.module_title)));
      button.append(node("small",{},item.domain+" · wiersz "+item.line+" · „"+item.matched+"”"));
      button.append(node("span",{},item.snippet));
      button.addEventListener("click",()=>openConceptNode(item));
      section.append(button);
    }
    evidence.append(section);
  }
}


/* Lean 4: exact indexed source -> registered formalization. No client code execution. */
const leanStatementLabels={
  unreviewed:"Nieprzejrzana",needs_review:"Wymaga przeglądu",approved:"Zatwierdzona"
};
const leanFormalizationLabels={
  missing:"Brak formalizacji",draft:"Szkic (bez SHA źródła)",
  ready:"Źródło przypięte",stale:"Źródło zmienione"
};
const leanProofLabels={
  not_run:"Nie uruchomiono",compiled:"Lean skompilował kod",
  failed:"Błąd Lean",timeout:"Przekroczony czas",
  toolchain_unavailable:"Brak Lean/lake",blocked:"Uruchomienie zablokowane"
};
async function loadLeanFragment(query){
  const epoch=++state.leanEpoch;activateTab("lean");
  $("leanResult").classList.add("hidden");$("leanEmpty").classList.remove("hidden");
  $("leanEmpty").textContent="Odczytywanie źródła i formalizacji…";
  try {
    const result=await api("/api/lean/fragment?"+new URLSearchParams(query));
    if(epoch!==state.leanEpoch)return;
    state.leanFragment=result;state.leanRunner=null;
    renderLeanFragment(result);
    try{
      const available=await api("/api/lean/status");
      if(epoch!==state.leanEpoch)return;
      state.leanRunner=available;
      const message=!available.runner_enabled?
        "Uruchamianie wyłączone. W lokalnym serwerze ustaw MATLIB_LEAN_RUN=1.":
        !available.lake_available?
        "Brak lake/Lean 4 w PATH. Zainstaluj elan i przygotuj Mathlib.":
        "Dostępny lokalny runner Lean 4 · "+(available.toolchain||"wersja nieznana");
      $("leanRunnerInfo").textContent=message;
      $("leanRun").disabled=!available.ready||!result.formalization_id||result.formalization_status==="stale";
    }catch(err){$("leanRunnerInfo").textContent=err.message;$("leanRun").disabled=true;}
  }catch(err){
    if(epoch!==state.leanEpoch)return;
    $("leanEmpty").textContent="Nie można otworzyć fragmentu: "+err.message;toast(err.message);
  }
}
function renderLeanFragment(result){
  $("leanEmpty").classList.add("hidden");$("leanResult").classList.remove("hidden");
  const scopeNote=result.source_linkage==="proof_of_adjacent_theorem"?
    " · Kod dotyczy twierdzenia poprzedzającego ten dowód, nie automatycznej transkrypcji rozumowania.":
    result.source_linkage==="contains_theorem"?
    " · Kod dotyczy twierdzenia zawartego w zaznaczeniu.":"";
  $("leanSourceInfo").textContent=result.source_module+" · wiersze "+result.start_line+
    "–"+result.end_line+(result.source_labels.length?" · "+result.source_labels.join(", "):"")+scopeNote;
  $("leanLatex").textContent=result.source_latex;
  $("leanCode").textContent=result.lean_code||"Brak powiązanej formalizacji Lean dla tego fragmentu.";
  const statuses=$("leanStatuses");statuses.replaceChildren();
  for(const [name,label] of [
    ["statement_status","Zgodność stwierdzenia"],
    ["formalization_status","Formalizacja"],
    ["proof_status","Sprawdzenie Lean"]
  ]){
    const card=node("div",{className:"lean-status"});
    const val=result[name],mapped=name==="statement_status"?leanStatementLabels:
      name==="formalization_status"?leanFormalizationLabels:leanProofLabels;
    card.append(node("small",{},label),node("strong",{},mapped[val]||val));
    statuses.append(card);
  }
  const note=result.formalization_id?
    "Identyfikator: "+result.formalization_id+" · "+(result.lean_theorem||""):
    "Brak kodu. Nie wygenerowano ani nie uruchomiono żadnego dowodu.";
  $("leanRunnerInfo").textContent=note;
  if(result.run_cached){
    $("leanLog").textContent="Ostatnie uruchomienie: "+(result.last_run_at||"czas nieznany")+
      "\n"+(result.last_run_detail||"")+
      (result.last_run_log?"\n"+result.last_run_log:"")+
      "\nUwaga: kompilacja nie jest certyfikatem zgodności z LaTeX-em.";
  }else if(result.previous_run_outdated){
    $("leanLog").textContent="Poprzedni wynik Lean unieważniono: zmienił się LaTeX, kod Lean lub konfiguracja narzędzi. Uruchom Lean ponownie.";
  }else if(result.run_record_invalid){
    $("leanLog").textContent="Zapis ostatniego uruchomienia jest nieczytelny. Wymagane ponowne sprawdzenie.";
  }else{
    $("leanLog").textContent="Nie uruchomiono. Kompilacja Lean i zgodność tłumaczenia są oceniane oddzielnie.";
  }
  $("leanRun").disabled=true;
}
function openLeanCurrent(){
  if(!state.currentData){toast("Najpierw wybierz obiekt w Czytniku.");return;}
  if(state.currentEntity){loadLeanFragment({entity_id:state.currentEntity});return;}
  const a=Number($("rangeStart").value),b=Number($("rangeEnd").value);
  if(!Number.isSafeInteger(a)||!Number.isSafeInteger(b)||b<a||b-a>300){
    toast("Dla całego rozdziału wybierz najwyżej 301 wierszy lub otwórz twierdzenie z Explorera.");return;
  }
  loadLeanFragment({module_id:state.currentModule,start_line:a,end_line:b});
}
function openLeanSelection(){
  const data=state.currentData,source=$("latexSource"),sel=window.getSelection();
  if(!data||state.simplified||!sel||sel.isCollapsed||!sel.rangeCount){
    toast("Zaznacz dokładny fragment w źródle LaTeX.");return;
  }
  const range=sel.getRangeAt(0);
  if(!source.contains(range.startContainer)||!source.contains(range.endContainer)){
    toast("Zaznaczenie musi być w źródle LaTeX.");return;
  }
  const prefix=range.cloneRange();prefix.selectNodeContents(source);
  prefix.setEnd(range.startContainer,range.startOffset);
  const start=prefix.toString().length,end=start+range.toString().length;
  if(end<=start||end>data.latex.length){toast("Nie udało się ustalić wierszy.");return;}
  const first=data.entity?data.entity.start_line:1;
  const n=s=>(s.match(/\n/g)||[]).length;
  const startLine=first+n(data.latex.slice(0,start));
  const endLine=first+n(data.latex.slice(0,end-1));
  sel.removeAllRanges();
  loadLeanFragment({module_id:state.currentModule,start_line:startLine,end_line:endLine});
}
// Guard asynchronous Lean results by both selection epoch and exact fragment.
function isCurrentLeanRun(epoch,item){
  return epoch===state.leanEpoch && state.leanFragment===item;
}
async function runLeanFormalization(){
  const item=state.leanFragment;
  const epoch=state.leanEpoch;
  if(!item?.formalization_id||!state.leanRunner?.ready)return;
  const button=$("leanRun");
  button.disabled=true;button.textContent="Sprawdzanie…";
  $("leanLog").textContent="Uruchamianie lokalnego Lean 4…";
  try{
    const r=await api("/api/lean/run",{
      method:"POST",body:JSON.stringify({formalization_id:item.formalization_id})});
    if(!isCurrentLeanRun(epoch,item))return;
    item.proof_status=r.proof_status;
    item.run_cached=Boolean(r.run_record_saved);
    item.last_run_at=r.last_run_at||null;
    item.last_run_detail=r.detail||"";
    item.last_run_log=r.log||"";
    renderLeanFragment(item);
    $("leanLog").textContent=(r.detail||"")+"\n"+(r.log||"")+
      (r.run_record_warning?"\n"+r.run_record_warning:"");
    $("leanRunnerInfo").textContent="Zakończono sprawdzanie kodu Lean. Zgodność z oryginalnym twierdzeniem wymaga osobnego przeglądu.";
    if(r.proof_status==="compiled"&&!r.certificate){
      $("leanRunnerInfo").textContent+=" Brak certyfikatu matematycznej zgodności.";
    }
  }catch(e){
    if(isCurrentLeanRun(epoch,item))$("leanLog").textContent="Błąd sprawdzania: "+e.message;
  }finally{
    if(isCurrentLeanRun(epoch,item)){
      button.textContent="Uruchom Lean";
      button.disabled=!state.leanRunner?.ready||item.formalization_status==="stale";
    }
  }
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
  $("openLeanCurrent").addEventListener("click",openLeanCurrent);
  $("openLeanSelection").addEventListener("click",openLeanSelection);
  $("leanRun").addEventListener("click",runLeanFormalization);
  $("addExcerpt").addEventListener("click",addExcerpt);
  $("addRange").addEventListener("click",addRange);
  $("openFirst").addEventListener("click",()=>{if(state.modules.length)openModule(state.modules[0].id);});
  $("openGraphQuick").addEventListener("click",()=>activateTab("graph"));
  $("togglePreview").addEventListener("click",()=>{state.simplified=!state.simplified;renderReader();});
  $("showFull").addEventListener("click",()=>{if(state.currentEntity)openEntity(state.currentEntity,true);else if(state.currentModule)openModule(state.currentModule,true);});
  $("closeTip").addEventListener("click",closeTip);
  $("tipOpen").addEventListener("click",()=>{const x=state.tooltipData;if(x)openLabel(x.name,x.source_document||state.currentModule);});
  $("referenceTip").addEventListener("mouseleave",closeTip);
  document.addEventListener("keydown",e=>{if(e.key==="Escape")closeTip();});
  $("drawGraph").addEventListener("click",loadGraph);$("findPath").addEventListener("click",findPath);
  $("drawConceptGraph").addEventListener("click",loadConceptGraph);
  $("conceptSearch").addEventListener("keydown",e=>{if(e.key==="Enter"){e.preventDefault();loadConceptGraph();}});
  $("conceptLimit").addEventListener("change",()=>{if(state.tab==="concepts")loadConceptGraph();});
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
