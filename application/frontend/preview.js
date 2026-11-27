/* Safe, deliberately limited TeX prose reader. Math is passed unchanged to KaTeX. */
function buildProsePreview(container, source, moduleId) {
  const fragment=document.createDocumentFragment();
  // Sticky matching avoids allocating the unconsumed suffix at every token.
  const at=(pattern,text,offset)=>{pattern.lastIndex=offset;return pattern.exec(text);};
  const environmentNames = {definicja:'Definicja',definition:'Definicja',twierdzenie:'Twierdzenie',theorem:'Twierdzenie',lemat:'Lemat',lemma:'Lemat',stwierdzenie:'Stwierdzenie',proposition:'Stwierdzenie',wniosek:'Wniosek',corollary:'Wniosek',uwaga:'Uwaga',remark:'Uwaga',przyklad:'Przykład',example:'Przykład',proof:'Dowód',dowod:'Dowód'};
  function tablePreview(source, root) {
    const wrapper=document.createElement('div'), table=document.createElement('table');
    wrapper.className='preview-table-scroll';table.className='preview-table';wrapper.append(table);root.append(wrapper);
    let cells=[], cell='', depth=0, environmentDepth=0, lastRow=null;
    const finishRow=()=>{
      cells.push(cell);cell='';
      if(cells.some(value=>value.trim())){
        lastRow=table.insertRow();
        for(const value of cells)parse(value,lastRow.insertCell(),true);
      }
      cells=[];
    };
    for(let i=0;i<source.length;){
      if(source[i]==='%'){while(i<source.length&&source[i]!=='\n')i++;continue;}
      const math=at(/(\$\$|\$|\\\[|\\\()/y,source,i);
      if(math){
        const left=math[0], right=left==='\\['?'\\]':left==='\\('?'\\)':left;
        const start=i;i+=left.length;
        while(i<source.length&&!source.startsWith(right,i))i+=source[i]==='\\'?2:1;
        if(i<source.length)i+=right.length;
        cell+=source.slice(start,i);continue;
      }
      const env=at(/\\(begin|end)\{[^}]+\}/y,source,i);
      if(env){environmentDepth+=env[1]==='begin'?1:-1;cell+=env[0];i+=env[0].length;continue;}
      if(depth===0&&environmentDepth===0){
        const rule=at(/\\(?:hline|toprule|midrule|bottomrule)\b/y,source,i);
        if(rule){
          if(cell.trim()||cells.length)finishRow();
          (lastRow||table).classList.add(lastRow?'preview-rule-bottom':'preview-rule-top');
          i+=rule[0].length;continue;
        }
        if(source.startsWith('\\\\',i)){
          finishRow();i+=2;
          const spacing=at(/\s*\[[^\]]*\]/y,source,i);if(spacing)i+=spacing[0].length;
          continue;
        }
        if(source[i]==='&'){cells.push(cell);cell='';i++;continue;}
      }
      if(source[i]==='\\'&&i+1<source.length){cell+=source.slice(i,i+2);i+=2;continue;}
      if(source[i]==='{')depth++;else if(source[i]==='}')depth--;
      cell+=source[i++];
    }
    finishRow();
  }
  function parse(text, root, inline=false) {
    let i=0, paragraph=null;
    const parents=[root];
    const parent=()=>parents[parents.length-1];
    const flush=()=>{paragraph=null;};
    const target=()=>inline?root:(paragraph||(paragraph=document.createElement('p'),parent().append(paragraph),paragraph));
    const append=value=>target().append(typeof value==='string'?document.createTextNode(value):value);
    function whitespace(){
      while(i<text.length){
        if(/\s/.test(text[i])){i++;continue;}
        if(text[i]==='%'){while(i<text.length&&text[i]!=='\n')i++;continue;}
        break;
      }
    }
    function group(open='{',close='}') {
      whitespace(); if(text[i]!==open)return null;
      const start=++i;let depth=1;
      while(i<text.length){
        if(text[i]==='\\'){i+=2;continue;}
        // Braces in TeX comments do not belong to the argument.
        if(text[i]==='%'){while(i<text.length&&text[i]!=='\n')i++;continue;}
        if(text[i]===open)depth++;
        if(text[i]===close && --depth===0){const value=text.slice(start,i);i++;return value;}
        i++;
      }
      return text.slice(start);
    }
    while(i<text.length) {
      if(text[i]==='%'){while(i<text.length && text[i]!=='\n')i++;continue;}
      if(text[i]==='$' || text.startsWith('\\[',i) || text.startsWith('\\(',i) || (text[i]==='\\' && at(/\\begin\{(?:equation\*?|align\*?|alignat\*?|gather\*?|multline\*?|CD)\}/y,text,i))) {
        const start=i;
        let left=text[i]==='$'?(text[i+1]==='$'?'$$':'$'):text.slice(i,i+2), right=left;
        if(left==='\\[')right='\\]';else if(left==='\\(')right='\\)';
        if(text.startsWith('\\begin',i)){left=at(/\\begin\{[^}]+\}/y,text,i)[0];right=left.replace('begin','end');}
        i+=left.length;
        while(i<text.length && !text.startsWith(right,i)){if(text[i]==='\\' && !text.startsWith(right,i))i+=2;else i++;}
        if(i<text.length)i+=right.length;
        append(text.slice(start,i));continue;
      }
      if(text[i]==='\n') {let end=i;while(text[end]==='\n'||text[end]==='\r'||text[end]===' '||text[end]==='\t')end++;if(text.slice(i,end).split('\n').length>2 && !inline)flush();else append(' ');i=end;continue;}
      if(text[i]==='{'){const value=group();parse(value||'',target(),true);continue;}
      if(text[i]==='}'){i++;continue;}
      if(text[i]!=='\\'){const start=i;while(i<text.length && !/[\\$%\n{}]/.test(text[i]))i++;append(text.slice(start,i).replace(/~/g,'\u00a0').replace(/---/g,'—').replace(/--/g,'–'));continue;}
      i++;
      const commandStart=i-1;
      const match=at(/[a-zA-Z]+\*?/y,text,i);
      if(!match){const symbol=text[i++];append(symbol==='\\'?' ':symbol==='%'?'%':symbol==='&'?'&':symbol==='$'?'$':symbol||'');continue;}
      const command=match[0].replace(/\*$/,'');i+=match[0].length;
      if(['newcommand','renewcommand','providecommand','DeclareMathOperator'].includes(command)) {group();while(true){whitespace();if(text[i]!=='[')break;group('[',']');}group();continue;}
      if(['label','index','bibliographystyle','bibliography'].includes(command)){group();continue;}
      if(['setcounter','addtocounter'].includes(command)){group();group();continue;}
      if(['stepcounter','refstepcounter'].includes(command)){group();continue;}
      if(['noindent','indent','smallskip','medskip','bigskip','newpage','clearpage','centering','begingroup','endgroup'].includes(command))continue;
      if(command==='texorpdfstring') {
        const visible=group()||'';group();
        parse(visible,target(),true);continue;
      }
      if(['chapter','section','subsection','subsubsection','paragraph'].includes(command)) {
        whitespace();if(text[i]==='[')group('[',']');const title=group()||'';
        if(inline){parse(title,root,true);continue;}
        flush();const heading=document.createElement(command==='chapter'?'h2':command==='section'?'h3':'h4');parse(title,heading,true);parent().append(heading);continue;
      }
      if(command==='begin'||command==='end') {
        const env=group()||'';whitespace();const title=text[i]==='['?group('[',']'):null;
        if(command==='begin'&&['tabular','tabular*'].includes(env)){
          if(env==='tabular*')group();
          group(); // Column specifications are layout metadata, not cell text.
          const token=/\\(begin|end)\{tabular\*?\}/g;token.lastIndex=i;
          let nesting=1, end=text.length, after=text.length, next;
          while((next=token.exec(text))){
            nesting+=next[1]==='begin'?1:-1;
            if(nesting===0){end=next.index;after=token.lastIndex;break;}
          }
          if(!inline)flush();tablePreview(text.slice(i,end),inline?root:parent());i=after;continue;
        }
        if(inline)continue;
        flush();
        if(command==='end'){if(parents.length>1)parents.pop();continue;}
        if(['tikzpicture','tikzcd','picture'].includes(env)){
          const closing='\\end{'+env+'}', end=text.indexOf(closing,i);
          i=end<0?text.length:end+closing.length;
          const figure=document.createElement('figure');figure.className='preview-figure atlas-tikz-preview';
          parent().append(figure);loadTikzFigure(figure,text.slice(commandStart,i),moduleId);continue;
        }
        if(['lstlisting','verbatim'].includes(env)){
          const end=text.indexOf('\\end{'+env+'}',i);
          const code=document.createElement('pre');code.className='preview-listing';code.textContent=text.slice(i,end<0?text.length:end);
          i=end<0?text.length:end+env.length+6;parent().append(code);continue;
        }
        const block=document.createElement('div');block.className='preview-block';
        if(environmentNames[env]){const label=document.createElement('strong');label.className='preview-block-title';label.textContent=environmentNames[env]+(title?' — ':'');if(title)parse(title,label,true);block.append(label);}
        parent().append(block);parents.push(block);continue;
      }
      if(command==='item'){if(!inline)flush();whitespace();const label=text[i]==='['?group('[',']'):'•';append((label||'•')+' ');continue;}
      if(['small','footnotesize','scriptsize','normalsize','large'].includes(command))continue;
      if(command==='caption'){const caption=document.createElement('p');caption.className='preview-caption';parse(group()||'',caption,true);flush();parent().append(caption);continue;}
      if(['emph','textit','textbf','texttt','textrm','textnormal','underline','footnote'].includes(command)) {
        const value=group()||'', el=document.createElement(command==='textbf'?'strong':command==='emph'||command==='textit'?'em':command==='texttt'?'code':'span');
        if(command==='footnote')el.className='preview-footnote';parse(value,el,true);append(el);continue;
      }
      if(['ref','eqref','pageref','autoref','nameref','cref','Cref','vref','Vref','atlasref'].includes(command)) {
        const label=group()||'', title=command==='atlasref'?group():null;
        const labels=command==='atlasref'?[label]:label.split(',').map(value=>value.trim()).filter(Boolean);
        labels.forEach((value,index)=>{if(index)append(', ');append(createReferenceLink(value,moduleId,{caption:title,command}));});continue;
      }
      if(command==='href'){group();const value=group()||'';parse(value,target(),true);continue;}
      if(command==='url'){append(group()||'');continue;}
      if(['LaTeX','TeX','ldots','dots','quad','qquad','hfill','par'].includes(command)){if(command==='par'&&!inline)flush();else append(command==='LaTeX'?'LaTeX':command==='TeX'?'TeX':command==='dots'||command==='ldots'?'…':' ');continue;}
      // Unsupported commands remain visible, rather than silently dropping content.
      append('\\'+match[0]);
    }
  }
  parse(source.replace(/\r\n/g,'\n'),fragment);
  container.replaceChildren(fragment);
}

async function loadTikzFigure(figure,source,moduleId,skipStatic=false){
  const entry=!skipStatic&&typeof atlasTikzPreviews!=='undefined'?atlasTikzPreviews.get(source.replace(/\r\n/g,'\n')):null;
  if(entry){
    const image=document.createElement('img');image.src='/assets/figures/'+entry.file;image.alt=entry.alt;
    image.onerror=()=>loadTikzFigure(figure,source,moduleId,true);
    figure.replaceChildren(image);return;
  }
  const status=document.createElement('figcaption');status.textContent='Składanie rysunku…';status.setAttribute('role','status');figure.replaceChildren(status);
  try{
    const digest=await crypto.subtle.digest('SHA-256',new TextEncoder().encode(source.replace(/\r\n/g,'\n')));
    const id=Array.from(new Uint8Array(digest),b=>b.toString(16).padStart(2,'0')).join('');
    const url='/api/modules/'+encodeURIComponent(moduleId)+'/figures/'+id+'.png';
    const response=await fetch(url);
    if(!response.ok){const error=await response.json();throw new Error(error.detail||'Nie udało się załadować rysunku.');}
    const objectUrl=URL.createObjectURL(await response.blob());
    const image=document.createElement('img');image.alt='Rysunek matematyczny z rozdziału '+moduleId;
    image.onload=()=>URL.revokeObjectURL(objectUrl);
    image.onerror=()=>{URL.revokeObjectURL(objectUrl);status.textContent='Nie udało się odczytać obrazu rysunku.';figure.replaceChildren(status);};
    image.src=objectUrl;figure.replaceChildren(image);
  }catch(error){
    status.textContent=error.message;
    const details=document.createElement('details'),summary=document.createElement('summary'),code=document.createElement('pre');
    summary.textContent='Pokaż źródło rysunku';code.textContent=source;details.append(summary,code);figure.append(details);
    const retry=document.createElement('button');retry.className='ghost-btn';retry.textContent='Ponów składanie rysunku';retry.onclick=()=>loadTikzFigure(figure,source,moduleId);figure.append(retry);
  }
}
