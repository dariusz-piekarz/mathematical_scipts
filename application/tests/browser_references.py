"""Real-browser regression for captions, multiple targets and ambiguous navigation."""
import os
from pathlib import Path
import sqlite3
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
URL = os.environ.get('MATLIB_TEST_URL','http://127.0.0.1:8765')
with sqlite3.connect(ROOT/'data/biblioteka.db') as db:
    conflict = db.execute('SELECT name FROM label_conflicts ORDER BY name LIMIT 1').fetchone()[0]
    target_module, target_entity = db.execute('SELECT document_id,entity_id FROM label_conflicts WHERE name=? ORDER BY document_id LIMIT 1',(conflict,)).fetchone()

with sync_playwright() as pw:
    browser=pw.chromium.launch(headless=True)
    page=browser.new_page(viewport={'width':1360,'height':900})
    errors=[]
    page.on('pageerror',lambda e: errors.append(str(e)))
    page.goto(URL,wait_until='networkidle')
    page.evaluate("() => openModule('ALG-08')")
    page.locator('#docTitle').filter(has_text='Geometria biwymierna').wait_for()
    link=page.locator('#simplified [data-reference="ch:ga5-rozdmuchania"]').first
    link.filter(has_text='Rozdmuchania i rozwiązywanie').wait_for()
    assert 'ch:ga5' not in link.inner_text()
    link.hover()
    page.locator('#tipBody h3').filter(has_text='Rozdmuchania').wait_for()
    page.locator('#tipOpen').hover()
    # The pointer entered the overlay; it must survive the delayed close
    # scheduled when leaving the source link, even without CSS :hover.
    page.wait_for_timeout(350)
    assert page.locator('#referenceTip').is_visible()
    assert page.evaluate("() => referenceTipHovered")
    page.screenshot(path=str(Path(os.environ['TEMP'])/'atlas-reference-preview.png'))
    page.locator('#tipOpen').click()
    page.wait_for_function("state.currentModule==='ALG-05' && !!state.currentEntity")
    # Explicit captions use the source's macros, while tooltip content uses
    # the destination chapter's macros, even when detached from its header.
    page.evaluate(r"""() => {
        const box=document.getElementById('simplified');
        box.replaceChildren(createReferenceLink('ALG-05::ch:ga5-rozdmuchania','AM1-36',
            {caption:'$\\HK$'}));
    }""")
    page.locator('#simplified .ref-link .katex').wait_for()
    assert page.locator('#simplified .ref-link .katex-html').inner_text() == 'KH'
    page.evaluate(r"() => renderSimplified('Zobacz \\ref{AM1-36::ma1:kh:lem:variation-additivity}.','ALG-08')")
    link=page.locator('#simplified .ref-link')
    link.hover()
    page.locator('#tipBody .tip-code .katex-html').filter(has_text='BV').first.wait_for()
    assert 'Nie złożono' not in page.locator('#tipBody').inner_text()
    page.evaluate("() => closeTip()")
    # Each label in a multi-reference must be separately clickable.
    page.evaluate(r"() => renderSimplified('Zobacz \\cref{ch:ga5-rozdmuchania,ch:ga6-powierzchnie}.', 'ALG-08')")
    assert page.locator('#simplified .ref-link').count()==2
    page.locator('#simplified .ref-link').first.filter(has_text='Rozdmuchania').wait_for()
    # Real FA-15B label: preserve the caption, render its math and open the
    # actual example, not merely the chapter or an unresolved placeholder.
    hyperref = r'Zobacz \hyperref[ex:dunford-not-pettis15b]{\emph{przykład z} $c_0$}.'
    page.evaluate("latex => renderSimplified(latex, 'FA-15B')", hyperref)
    link = page.locator('#simplified [data-reference="ex:dunford-not-pettis15b"]')
    assert link.count() == 1
    assert link.locator('em').inner_text() == 'przykład z'
    assert link.locator('.katex').count() == 1
    assert r'\hyperref' not in page.locator('#simplified').inner_text()
    link.hover()
    page.locator('#tipBody').filter(has_text='Całka Dunforda').wait_for()
    link.click()
    page.wait_for_function("state.currentModule==='FA-15B' && !!state.currentEntity")
    assert 'Całka Dunforda' in page.locator('#docTitle').inner_text()
    page.evaluate("() => closeTip()")
    # Explicit captions remain visible even for a missing target.
    page.evaluate(r"() => renderSimplified('Zobacz \\hyperref[FA-15B::atlas-missing-fixture]{opis celu}.', 'FA-15B')")
    missing = page.locator('#simplified .ref-link.ref-missing')
    missing.wait_for()
    assert missing.inner_text() == 'opis celu'
    # Source view must preserve all characters, including the optional argument.
    source = r'\hyperref [ ex:dunford-not-pettis15b ]{\textbf{przykład} $c_0$}'
    assert page.evaluate("""source => {
        const box=document.createElement('div');showRefs(box,source);
        const link=box.querySelector('button[data-reference]');
        return box.textContent===source &&
            box.querySelectorAll('button[data-reference]').length===1 &&
            link.dataset.reference==='ex:dunford-not-pettis15b';
    }""", source)
    # Original source text, spaces and starred commands must stay byte-for-byte intact.
    sample=r'Tekst \cref* { ch:ga5-rozdmuchania, ch:ga6-powierzchnie }.'
    actual=page.evaluate("source => {const box=document.createElement('div');showRefs(box,source);return box.textContent;}",sample)
    assert actual==sample,(actual,sample)
    # Build a long source outside the live DOM, then replace it atomically.
    # Preserve whitespace and clickable reference context exactly.
    source_batch_cases = page.evaluate(r"""() => {
        const box=document.createElement('div');
        document.body.append(box);
        const observer=new MutationObserver(()=>{});
        observer.observe(box,{childList:true});
        let count=0;
        try{
            const samples=['','plain text','\\ref{a}','\\cref* { a , b }',
                '\\ref{   }','\\atlasref{DG-14::a}{Opis}',
                'A\\eqref{x}\nB\\nameref {y}','\\ref{a,,b}','\\ref{a}\r\nend\n'];
            for(const source of samples){
                showRefs(box,source);
                if(box.textContent!==source||observer.takeRecords().length>1)
                    throw Error('source text or atomic replacement mismatch');
                const expected=source.length?source.split('\n').length-
                    (source.endsWith('\n')?1:0):0;
                if(sourceLineCount(source)!==expected)throw Error('source line count');
                count++;
            }
            const long=Array.from({length:1000},(_,i)=>
                'Wiersz '+i+' \\cref{ a'+i+', b'+i+' }.\n').join('');
            showRefs(box,long);
            if(box.textContent!==long||observer.takeRecords().length!==1||
               box.querySelectorAll('button[data-reference]').length!==2000||
               sourceLineCount(long)!==1000)
                throw Error('long source batch mismatch');
            return count+1;
        }finally{observer.disconnect();box.remove();}
    }""")
    assert source_batch_cases == 10
    # Clicking an ambiguous reference keeps the chapter picker open.
    page.evaluate(r"label => renderSimplified('Zobacz \\ref{'+label+'}.','TEST')",conflict)
    page.locator('#simplified .ref-link').filter(has_text='Wybierz cel').wait_for()
    page.locator('#simplified .ref-link').click()
    page.locator('#tipBody .ref-choice').first.wait_for()
    page.locator('#tipBody .ref-choice').first.click()
    page.wait_for_function('target => state.currentModule===target[0] && state.currentEntity===target[1]',arg=[target_module,target_entity])
    # Missing explicit targets must not quietly redirect to a different chapter.
    page.evaluate(r"() => renderSimplified('Zobacz \\ref{ALG-08::ch:ga5-rozdmuchania}.','ALG-08')")
    page.locator('#simplified .ref-missing').filter(has_text='Brak celu').wait_for()
    # A slow label lookup must not override a more recent chapter selection.
    # A source-specific cached preview must not answer an unqualified lookup.
    cases = page.evaluate("""async () => {
        const originalApi = api;
        let pending, count = 0;
        const toastBox = document.getElementById('toast');
        const resetToast = () => {toastBox.textContent = ''; toastBox.classList.add('hidden');};
        try {
            api = (url, options) => url.startsWith('/api/labels/atlas-race-test')
                ? new Promise((resolve, reject) => {pending = {resolve, reject};})
                : originalApi(url, options);
            for (const result of [{entity_id:'invalid'}, {document_id:'invalid'},
                                  {ambiguous:true}, null]) {
                closeTip(); resetToast(); pending = null;
                const old = openLabel('atlas-race-test','ALG-08');
                await openModule('ALG-08');
                if (!pending) throw Error('lookup not intercepted');
                if (result === null) pending.reject(new Error('obsolete error'));
                else pending.resolve(result);
                await old;
                if (state.currentModule !== 'ALG-08' || state.currentEntity !== null ||
                    toastBox.textContent || !document.getElementById('referenceTip').classList.contains('hidden'))
                    throw Error('obsolete lookup changed current view');
                count++;
            }
            closeTip(); pending = null;
            state.tooltipData = {name:'atlas-race-test', source_document:'ALG-05',
                                 entity_id:'invalid'};
            const current = openLabel('atlas-race-test');
            if (!pending) throw Error('wrong source cache reused');
            pending.resolve({document_id:'ALG-08'});
            await current;
            if (state.currentModule !== 'ALG-08' || state.currentEntity !== null)
                throw Error('uncached target not opened');
            count++;
        } finally {
            api = originalApi; closeTip(); resetToast();
        }
        return count;
    }""")
    assert cases == 5
    # Fallback label responses need not echo source_document. The preview
    # must keep the original lookup context, including a global lookup.
    context_cases = page.evaluate("""async () => {
        const originalApi=api, originalOpenEntity=openEntity;
        const anchor=document.getElementById('togglePreview');
        let calls=[], opened=[], count=0;
        try{
            api=(url,options)=>{
                if(url.startsWith('/api/labels/atlas-context-test')){
                    calls.push(url);
                    return Promise.resolve({name:'canonical-test',document_id:'ALG-05',
                        entity_id:'context-target',title:'Test',latex:''});
                }
                return originalApi(url,options);
            };
            openEntity=async id=>{opened.push(id);};
            for(const source of [null,'ALG-05','AM1-36']){
                calls=[];opened=[];
                await previewLabel('atlas-context-test',anchor,source);
                if(state.tooltipData.name!=='atlas-context-test'||
                   state.tooltipData.source_document!==source)
                    throw Error('lookup context was not retained');
                document.getElementById('tipOpen').click();
                await Promise.resolve();
                if(calls.length!==1||opened.length!==1||opened[0]!=='context-target')
                    throw Error('preview opening re-resolved label in wrong context');
                if(state.tooltipData)throw Error('preview did not close');
                count++;
            }
        }finally{api=originalApi;openEntity=originalOpenEntity;closeTip();}
        return count;
    }""")
    assert context_cases == 3
    # Search responses cannot reopen a dismissed dropdown or replace a
    # more recent query, including repeated submission of the same text.
    search_cases = page.evaluate("""async () => {
        const originalApi = api, input = document.getElementById('searchInput');
        const list = document.getElementById('searchResults');
        const toastBox = document.getElementById('toast');
        const requests = [];
        let count = 0;
        try {
            api = (url, options) => url.startsWith('/api/search?')
                ? new Promise((resolve, reject) => requests.push({resolve, reject}))
                : originalApi(url, options);
            for (const mode of ['escape', 'outside', 'repeat', 'change']) {
                for (const failure of [false, true]) {
                    dismissSearch(); requests.length = 0;
                    toastBox.textContent = ''; input.value = 'alpha';
                    const old = performSearch('alpha');
                    if (mode === 'escape') {
                        input.dispatchEvent(new KeyboardEvent('keydown', {key:'Escape', bubbles:true}));
                    } else if (mode === 'outside') {
                        document.getElementById('docTitle').click();
                    } else {
                        input.value = mode === 'change' ? 'beta' : 'alpha';
                        const current = performSearch(input.value);
                        requests[1].resolve({items:[]}); await current;
                    }
                    const before = list.firstChild;
                    if (failure) requests[0].reject(new Error('stale search'));
                    else requests[0].resolve({items:[]});
                    await old;
                    const dismissed = mode === 'escape' || mode === 'outside';
                    if (list.classList.contains('hidden') !== dismissed ||
                        list.firstChild !== before || toastBox.textContent !== '')
                        throw Error('stale search: ' + mode);
                    count++;
                }
            }
        } finally {
            api = originalApi; input.value = ''; dismissSearch();
            toastBox.textContent = ''; toastBox.classList.add('hidden');
        }
        return count;
    }""")
    assert search_cases == 8
    # Search result buttons are navigable without a mouse. Escape from
    # a focused result dismisses the dropdown and returns focus to input.
    keyboard_cases = page.evaluate("""async () => {
        const originalApi=api, input=document.getElementById('searchInput');
        const list=document.getElementById('searchResults');
        let count=0;
        const press=(key,expected,prevent=true)=>{
            const event=new KeyboardEvent('keydown',{key,bubbles:true,cancelable:true});
            document.activeElement.dispatchEvent(event);
            if(document.activeElement!==expected||event.defaultPrevented!==prevent)
                throw Error('search keyboard: '+key);
            count++;
        };
        try{
            api=(url,options)=>url.startsWith('/api/search?')
                ? Promise.resolve({items:[
                    {id:'a',title:'A',kind:'module',document_id:'ALG-05',start_line:1},
                    {id:'b',title:'B',kind:'module',document_id:'ALG-08',start_line:1}
                ]}) : originalApi(url,options);
            input.value='atlas';input.focus();await performSearch('atlas');
            const buttons=[...list.querySelectorAll('button')];
            if(buttons.length!==3)throw Error('missing search results');
            press('ArrowDown',buttons[0]);press('ArrowDown',buttons[1]);
            press('End',buttons[2]);press('ArrowDown',buttons[2]);
            press('Home',buttons[0]);press('ArrowUp',input);
            press('ArrowUp',buttons[2]);press('ArrowUp',buttons[1]);
            press('Escape',input);
            if(!list.classList.contains('hidden'))throw Error('Escape did not dismiss search');
            press('ArrowDown',input,false);
            return count;
        }finally{api=originalApi;input.value='';dismissSearch();input.blur();}
    }""")
    assert keyboard_cases == 10
    # A pending result must not reopen the dropdown after keyboard focus
    # leaves the header or a programmatic tab/reading-mode transition.
    search_focus_cases = page.evaluate("""async () => {
        const originalApi=api, input=document.getElementById('searchInput');
        const list=document.getElementById('searchResults');
        const toastBox=document.getElementById('toast');
        const oldTab=state.tab;
        let requests=[],count=0;
        try{
            api=(url,options)=>url.startsWith('/api/search?')
                ? new Promise((resolve,reject)=>requests.push({resolve,reject}))
                : originalApi(url,options);
            for(const cancel of [
                ()=>document.getElementById('togglePreview').focus(),
                ()=>activateTab('reader'),
                ()=>setReadingMode(true)
            ]){
                for(const failure of [false,true]){
                    input.value='atlas';input.focus();
                    toastBox.textContent='';
                    const pending=performSearch('atlas');
                    cancel();
                    const req=requests.at(-1);
                    if(failure)req.reject(Error('obsolete search'));
                    else req.resolve({items:[]});
                    await pending;
                    if(!list.classList.contains('hidden')||toastBox.textContent)
                        throw Error('obsolete search response after focus/view change');
                    setReadingMode(false);count++;
                }
            }
            input.focus();const pending=performSearch('atlas');
            requests.at(-1).resolve({items:[]});await pending;
            const button=list.querySelector('button');
            button.focus();
            if(list.classList.contains('hidden'))throw Error('internal focus dismissed search');
            document.getElementById('togglePreview').focus();
            if(!list.classList.contains('hidden'))throw Error('outside focus retained search');
            return count+2;
        }finally{
            api=originalApi;input.value='';dismissSearch();
            setReadingMode(false);activateTab(oldTab);
            toastBox.textContent='';toastBox.classList.add('hidden');
        }
    }""")
    assert search_focus_cases == 8
    # Pending reference requests must not resurrect a detached anchor
    # after the source pane or simplified preview is rebuilt.
    detached_cases = page.evaluate("""async () => {
        await openModule('ALG-08');
        const originalApi=api, box=document.getElementById('simplified');
        const requests=[];
        const tip=document.getElementById('referenceTip');
        const makeAnchor=()=>{const a=document.createElement('button');box.append(a);return a;};
        let count=0;
        try {
            api=(url,options)=>url.startsWith('/api/labels/atlas-detached-')
                ? new Promise((resolve,reject)=>requests.push({resolve,reject}))
                : originalApi(url,options);
            await previewLabel('atlas-detached-0',document.createElement('button'));
            if(requests.length)throw Error('detached anchor requested');
            count++;
            for(const success of [true,false]){
                const a=makeAnchor();
                const pending=previewLabel('atlas-detached-1',a);
                a.remove();
                const request=requests.at(-1);
                if(success)request.resolve({title:'obsolete',document_id:'ALG-08',latex:''});
                else request.reject(new Error('obsolete error'));
                await pending;
                if(!tip.classList.contains('hidden')||state.tooltipData)
                    throw Error('detached tooltip displayed');
                count++;
            }
            const a=makeAnchor();
            const pending=previewLabel('atlas-detached-2',a);
            renderReader();
            requests.at(-1).resolve({title:'obsolete',document_id:'ALG-08',latex:''});
            await pending;
            if(!tip.classList.contains('hidden')||state.tooltipData)
                throw Error('reader rebuild left obsolete tooltip');
            count++;
        }finally{api=originalApi;closeTip();}
        return count;
    }""")
    assert detached_cases == 4
    # A partial or malformed batch must not permanently cache an absent label.
    description_cases = page.evaluate("""async () => {
        const originalApi=api;
        const source='ATLAS-DESCRIPTION-TEST';
        let count=0, calls=0, reply;
        const key=label=>JSON.stringify([source,label]);
        const clear=label=>referenceDescriptions.delete(key(label));
        try {
            api=async (url,options)=>{
                if(url==='/api/references/descriptions'){
                    const body=JSON.parse(options.body);
                    if(body.source_document===source){calls++;return reply;}
                }
                return originalApi(url,options);
            };
            for(const malformed of [{items:{}},{items:{bad:null}},{items:{bad:[]}},
                                    {items:{bad:{}}},{items:[]},null,
                                    {items:{bad:{document_id:42}}}]){
                clear('bad');reply=malformed;const before=calls;
                if(await describeReference('bad',source)!==null)
                    throw Error('invalid description accepted');
                reply={items:{bad:{document_id:'ALG-08'}}};
                if((await describeReference('bad',source)).document_id!=='ALG-08'||
                    calls!==before+2)throw Error('description retry failed');
                count++;
            }
            clear('ok');clear('bad');
            reply={items:{ok:{missing:true}}};const before=calls;
            const good=describeReference('ok',source),bad=describeReference('bad',source);
            if(!(await good).missing||await bad!==null||calls!==before+1)
                throw Error('partial batch did not settle independently');
            if(describeReference('ok',source)!==good)throw Error('valid cache discarded');
            reply={items:{bad:{ambiguous:true}}};
            if(!(await describeReference('bad',source)).ambiguous||calls!==before+2)
                throw Error('partial batch retry failed');
            count++;
            reply={items:{}};
            if(await describeReference('constructor',source)!==null)
                throw Error('inherited property treated as description');
            count++;
        }finally{
            api=originalApi;
            for(const label of ['ok','bad','constructor'])clear(label);
        }
        return count;
    }""")
    assert description_cases == 9
    # Bound settled cache entries without evicting or duplicating in-flight
    # requests. Restore the original cache after the synthetic long session.
    cache_cases = page.evaluate("""async () => {
        const originalApi=api, source='ATLAS-CACHE-TEST';
        const saved=new Map(referenceDescriptions);
        const key=label=>JSON.stringify([source,label]);
        let calls=[],count=0;
        try{
            referenceDescriptions.clear();
            api=(url,options)=>{
                if(url==='/api/references/descriptions'){
                    const body=JSON.parse(options.body);
                    if(body.source_document===source){
                        calls.push(body.labels);
                        return Promise.resolve({items:Object.fromEntries(body.labels.map(
                            label=>[label,{document_id:'ALG-08'}]))});
                    }
                }
                return originalApi(url,options);
            };
            const first=describeReference('first',source);
            if(first!==describeReference('first',source))throw Error('pending duplicate');
            await first;count++;
            if(describeReference('first',source)!==first)throw Error('settled promise lost');
            count++;
            const entries=Array.from({length:REFERENCE_CACHE_LIMIT-1},
                (_,i)=>describeReference('entry'+i,source));
            await Promise.all(entries);
            if(referenceDescriptions.size!==REFERENCE_CACHE_LIMIT)throw Error('cache capacity');
            count++;
            if(describeReference('first',source)!==first)throw Error('cache refresh');
            count++;
            const extra=describeReference('extra',source);
            if(referenceDescriptions.size!==REFERENCE_CACHE_LIMIT||
               extra!==describeReference('extra',source))throw Error('pending eviction');
            count++;
            await extra;
            if(referenceDescriptions.size!==REFERENCE_CACHE_LIMIT||
               referenceDescriptions.has(key('entry0'))||!referenceDescriptions.has(key('first')))
                throw Error('incorrect LRU eviction');
            count++;
            const retry=describeReference('entry0',source);
            if(retry===entries[0]||retry!==describeReference('entry0',source))
                throw Error('evicted entry not refetched exactly once');
            await retry;count++;
            if(referenceDescriptions.size!==REFERENCE_CACHE_LIMIT||
               [...referencePending.keys()].some(k=>k.startsWith('["'+source+'",')))
                throw Error('pending cache not settled');
            count++;
            if(calls.some(batch=>batch.length>200))throw Error('batch limit exceeded');
            return count+1;
        }finally{
            api=originalApi;referenceDescriptions.clear();
            for(const [k,v] of saved)referenceDescriptions.set(k,v);
        }
    }""")
    assert cache_cases == 9
    # Viewport-aware geometry must use the measured overlay size, and
    # scrolling the reader must invalidate even an outstanding lookup.
    position_cases = page.evaluate("""() => {
        let count=0;
        for(const [w,h] of [[320,240],[390,844],[768,500],[1360,900]]){
            const width=Math.min(430,w*.92),height=Math.min(300,h-24);
            for(const anchor of [{left:0,top:0,bottom:15},
                  {left:w-20,top:h-30,bottom:h-10},
                  {left:w/2,top:h/2,bottom:h/2+20}]){
                const p=referenceTipPosition(anchor,width,height,w,h);
                if(p.left<8||p.top<8||p.left+width>w-8+.01||p.top+height>h-8+.01)
                    throw Error('reference overlay outside viewport');
                count++;
            }
        }
        if(referenceTipPosition({left:20,top:500,bottom:520},250,200,600,600).top!==292)
            throw Error('overlay did not prefer space above anchor');
        if(referenceTipPosition({left:20,top:30,bottom:50},250,200,600,600).top!==58)
            throw Error('overlay did not prefer space below anchor');
        if(referenceTipPosition({left:280,top:30,bottom:50},150,100,390,844).left!==232)
            throw Error('overlay did not use measured width');
        return count+3;
    }""")
    assert position_cases == 15
    for width,height in [(320,240),(390,844),(1360,900)]:
        page.set_viewport_size({'width':width,'height':height})
        page.evaluate("""async () => {
            const reader=document.getElementById('view-reader');
            reader.scrollTop=0;
            await new Promise(resolve=>requestAnimationFrame(()=>requestAnimationFrame(resolve)));
            await previewLabel('ch:ga5-rozdmuchania',
                               document.getElementById('togglePreview'),'ALG-08');
        }""")
        bounds=page.locator('#referenceTip').bounding_box()
        assert bounds is not None
        assert bounds['x']>=7 and bounds['y']>=7,bounds
        assert bounds['x']+bounds['width']<=width-7,bounds
        assert bounds['y']+bounds['height']<=height-7,bounds
        page.evaluate("""() => {
            const tip=document.getElementById('referenceTip');
            tip.dispatchEvent(new Event('scroll'));
        }""")
        assert page.locator('#referenceTip').is_visible()
        # An already-delivered scroll geometry must not dismiss a new hover.
        page.evaluate("() => document.getElementById('view-reader').dispatchEvent(new Event('scroll'))")
        assert page.locator('#referenceTip').is_visible()
        page.evaluate("""() => {
            const anchor=state.tooltipAnchor;
            const original=anchor.getBoundingClientRect;
            try{
                anchor.getBoundingClientRect=()=> {
                    const r=original.call(anchor);
                    return {left:r.left, right:r.right, top:r.top+20, bottom:r.bottom+20};
                };
                document.getElementById('view-reader').dispatchEvent(new Event('scroll'));
            }finally{anchor.getBoundingClientRect=original;}
        }""")
        assert page.locator('#referenceTip').is_hidden()
    page.evaluate("""async () => {
        const originalApi=api;
        let resolve;
        try{
            api=()=>new Promise(r=>{resolve=r;});
            const pending=previewLabel('atlas-scroll-test',document.getElementById('togglePreview'));
            const anchor=state.tooltipAnchor, original=anchor.getBoundingClientRect;
            try{
                anchor.getBoundingClientRect=()=>{
                    const r=original.call(anchor);
                    return {left:r.left,right:r.right,top:r.top+20,bottom:r.bottom+20};
                };
                document.getElementById('view-reader').dispatchEvent(new Event('scroll'));
            }finally{anchor.getBoundingClientRect=original;}
            resolve({title:'obsolete',document_id:'ALG-08',latex:''});
            await pending;
            if(state.tooltipData||!document.getElementById('referenceTip').classList.contains('hidden'))
                throw Error('late response reopened scrolled tooltip');
        }finally{api=originalApi;closeTip();}
    }""")
    assert not errors,errors
    browser.close()
    print('Reference titles, hover, exact navigation, multiple targets, conflicts, missing labels and source preservation: OK')
