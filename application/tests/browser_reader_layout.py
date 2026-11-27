"""Check TeX headings and viewport-bound reader scrolling in real Chromium."""
import os
from pathlib import Path

from playwright.sync_api import sync_playwright


URL = os.environ.get('MATLIB_TEST_URL', 'http://127.0.0.1:8765')


def assert_viewport_layout(page):
    metrics = page.evaluate("""() => {
        const root=document.scrollingElement, view=document.getElementById('view-reader');
        const box=view.getBoundingClientRect();
        return {height:innerHeight,width:innerWidth,rootHeight:root.scrollHeight,
                rootWidth:root.scrollWidth,scrollY,readerBottom:box.bottom,
                readerHeight:view.clientHeight,readerScroll:view.scrollHeight};
    }""")
    assert metrics['rootHeight'] <= metrics['height'] + 1, metrics
    assert metrics['rootWidth'] <= metrics['width'] + 1, metrics
    assert abs(metrics['readerBottom'] - metrics['height']) <= 1, metrics
    assert metrics['readerHeight'] > 0, metrics
    assert metrics['scrollY'] == 0, metrics
    return metrics


with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=True)
    page = browser.new_page(viewport={'width': 1934, 'height': 877})
    errors = []
    page.on('pageerror', lambda error: errors.append(str(error)))
    page.goto(URL, wait_until='networkidle')
    page.evaluate("() => openModule('AM1-14')")
    page.locator('#simplified .katex').first.wait_for(state='attached')

    # Previously KaTeX's absolute MathML spans enlarged the document to over
    # 6000 px while the reader remained one viewport tall. Scrolling the outer
    # document exposed a large blank region below the application.
    for width, height in ((1934, 877), (1547, 702), (967, 439), (390, 844), (390, 350), (320, 240)):
        page.set_viewport_size({'width': width, 'height': height})
        metrics = assert_viewport_layout(page)
        assert metrics['readerScroll'] > metrics['readerHeight'], metrics
        page.locator('#view-reader').evaluate('el => {el.scrollTop=el.scrollHeight}')
        page.mouse.move(width - 35, height - 35)
        page.mouse.wheel(0, 10000)
        page.wait_for_function('window.scrollY === 0')
        assert_viewport_layout(page)
        assert page.locator('#view-reader').evaluate('el => el.scrollTop > 0')
        # The toolbar stays at the reader scrollport, not at document top.
        pinned = page.evaluate("""() => {
            const view = document.querySelector('#view-reader');
            const toolbar = view.querySelector('.reader-toolbar');
            const v = view.getBoundingClientRect(), t = toolbar.getBoundingClientRect();
            return {top: t.top, bottom: t.bottom, viewTop: v.top,
                    viewBottom: v.bottom, position: getComputedStyle(toolbar).position};
        }""")
        assert pinned['position'] == 'sticky', pinned
        assert abs(pinned['top'] - pinned['viewTop']) <= 2, pinned
        assert pinned['viewBottom'] - pinned['bottom'] >= 40, pinned
        if width == 1934:
            page.screenshot(path=str(Path(os.environ.get('TEMP', '/tmp')) / 'atlas-reader-am1-14-fixed.png'))

    page.set_viewport_size({'width': 1360, 'height': 900})
    page.locator('#view-reader').evaluate('el => {el.scrollTop=0}')
    for _ in range(8):
        page.locator('#textSizeUp').click()
    assert page.locator('#textSizeUp').is_disabled()
    assert_viewport_layout(page)
    page.locator('#showExplorer').click()
    assert page.locator('#explorer').is_visible()
    assert page.locator('#tree').evaluate('el => el.scrollHeight > el.clientHeight')

    # Clicking the chapter caret in the default chapter-only mode must
    # actually reveal sections and accurately announce expansion.
    caret_cases = page.evaluate("""async () => {
        const id='DG-14', module=state.modules.find(m=>m.id===id);
        const oldMode=state.granularity, oldOutline=state.outlines.get(id);
        const oldDomain=state.expandedDomains.has(module.domain);
        const oldExpanded=state.expandedModules.has(id);
        const select=document.getElementById('granularity');
        const caret=()=>[...document.querySelectorAll('.module-line .chev')]
            .find(el=>el.getAttribute('aria-label')==='Rozwiń '+id ||
                      el.getAttribute('aria-label')==='Zwiń '+id);
        try {
            state.expandedDomains.add(module.domain);
            state.expandedModules.delete(id);
            state.outlines.set(id,[{id:'caret-fixture',kind:'section',title:'Sekcja testowa'}]);
            state.granularity='module'; select.value='module'; renderTree();
            if(caret().getAttribute('aria-expanded')!=='false')throw Error('initial expansion');
            caret().click();
            if(state.granularity!=='section'||select.value!=='section'||
               caret().getAttribute('aria-expanded')!=='true'||
               ![...document.querySelectorAll('.outline-name')].some(el=>el.textContent==='Sekcja testowa'))
                throw Error('caret did not reveal sections');
            caret().click();
            if(caret().getAttribute('aria-expanded')!=='false')throw Error('collapse');
            state.expandedModules.add(id); state.granularity='module';
            select.value='module'; renderTree();
            caret().click();
            if(caret().getAttribute('aria-expanded')!=='true'||select.value!=='section')
                throw Error('previously expanded hidden branch collapsed');
            state.granularity='object'; select.value='object'; renderTree();
            caret().click(); caret().click();
            if(select.value!=='object'||caret().getAttribute('aria-expanded')!=='true')
                throw Error('object mode lost');
            return 4;
        } finally {
            state.granularity=oldMode; select.value=oldMode;
            if(oldOutline===undefined)state.outlines.delete(id);else state.outlines.set(id,oldOutline);
            if(!oldDomain)state.expandedDomains.delete(module.domain);
            if(oldExpanded)state.expandedModules.add(id);else state.expandedModules.delete(id);
            renderTree();
        }
    }""")
    assert caret_cases == 4

    # A long outline must expose every object without creating an unbounded
    # DOM list. Pagination is independent for sections and all objects.
    pagination = page.evaluate("""() => {
        const id='DG-14', module=state.modules.find(m=>m.id===id);
        const oldMode=state.granularity, oldOutline=state.outlines.get(id);
        const oldDomain=state.expandedDomains.has(module.domain);
        const oldExpanded=state.expandedModules.has(id);
        const rows=Array.from({length:1201}, (_,i)=>({
            id:'pagination-fixture-'+i, kind:i%2?'section':'theorem', title:'Fixture '+i
        }));
        const key=mode=>JSON.stringify([id,mode]);
        const oldPages=['section','object'].map(mode=>[key(mode),outlinePages.get(key(mode))]);
        try {
            state.expandedDomains.add(module.domain); state.expandedModules.add(id);
            state.outlines.set(id,rows);
            let count=0;
            for (const mode of ['object','section']) {
                state.granularity=mode; outlinePages.delete(key(mode)); renderTree();
                const expected=rows.filter(e=>mode==='object'||e.kind==='section').map(e=>e.title);
                const getPager=()=>[...document.querySelectorAll('.outline-pagination')]
                    .find(el=>el.dataset.pageKey===key(mode));
                const seen=[];
                while(true) {
                    const pager=getPager(), branch=pager.parentElement;
                    const pagers=branch.querySelectorAll('.outline-pagination');
                    if(pagers.length!==2 || pagers[0].dataset.position!=='top' ||
                       pagers[1].dataset.position!=='bottom' ||
                       branch.firstElementChild!==pagers[0] || branch.lastElementChild!==pagers[1])
                        throw Error('missing top or bottom pagination controls');
                    const actual=[...branch.querySelectorAll('.outline-name')].map(e=>e.textContent);
                    if(actual.length>300)throw Error('unbounded outline page');
                    seen.push(...actual);
                    const next=pager.querySelector('[data-direction="next"]');
                    if(next.disabled)break;
                    // Advance from the bottom controls as a reader would.
                    pagers[1].querySelector('[data-direction="next"]').click();
                    const top=getPager();
                    if(!top.contains(document.activeElement))
                        throw Error('focus not returned to start of new page');
                    const viewport=document.getElementById('tree').getBoundingClientRect();
                    const bounds=top.getBoundingClientRect();
                    if(bounds.top < viewport.top-2 || bounds.bottom > viewport.bottom+2)
                        throw Error('new page start not visible');
                }
                if(JSON.stringify(seen)!==JSON.stringify(expected))
                    throw Error('missing or duplicated outline objects');
                if(!getPager().querySelector('[data-direction="prev"]').disabled) {
                    getPager().querySelector('[data-direction="prev"]').click();
                    if(!getPager().contains(document.activeElement))
                        throw Error('pagination keyboard focus lost');
                }
                count++;
            }
            return count;
        } finally {
            state.granularity=oldMode;
            if(oldOutline===undefined)state.outlines.delete(id);else state.outlines.set(id,oldOutline);
            if(!oldDomain)state.expandedDomains.delete(module.domain);
            if(!oldExpanded)state.expandedModules.delete(id);
            for(const [k,v] of oldPages)if(v===undefined)outlinePages.delete(k);else outlinePages.set(k,v);
            renderTree();
        }
    }""")
    assert pagination == 2

    # Collapsing/reopening a pending outline shares one request, and a
    # failed outline is immediately retryable without an extra collapse.
    outline_cases = page.evaluate("""async () => {
        const originalApi = api, id = 'DG-14';
        const data = await api('/api/modules/DG-14/outline');
        const requests = [];
        const toastBox = document.getElementById('toast');
        const clearToast = () => {toastBox.textContent = ''; toastBox.classList.add('hidden');};
        let count = 0;
        try {
            state.expandedModules.delete(id); state.outlines.delete(id); clearToast();
            api = (url, options) => url === '/api/modules/DG-14/outline'
                ? new Promise((resolve, reject) => requests.push({resolve, reject}))
                : originalApi(url, options);
            const first = toggleModule(id);
            await toggleModule(id);
            const second = toggleModule(id);
            if (requests.length !== 1) throw Error('duplicate outline request');
            requests[0].resolve(data); await Promise.all([first, second]);
            if (!state.expandedModules.has(id) || state.outlines.get(id) !== data.entities)
                throw Error('outline not populated');
            count++;
            await toggleModule(id); await toggleModule(id);
            if (requests.length !== 1) throw Error('cached outline refetched');
            count++;
            await toggleModule(id); state.outlines.delete(id);
            const failed = toggleModule(id);
            requests[1].reject(new Error('outline failure')); await failed;
            if (state.expandedModules.has(id) || toastBox.textContent !== 'outline failure')
                throw Error('failed outline not retryable');
            const retry = toggleModule(id);
            requests[2].resolve(data); await retry;
            if (!state.expandedModules.has(id)) throw Error('retry failed');
            count++;
            await toggleModule(id); state.outlines.delete(id); clearToast();
            const closed = toggleModule(id); await toggleModule(id);
            requests[3].reject(new Error('closed outline')); await closed;
            if (state.expandedModules.has(id) || toastBox.textContent)
                throw Error('closed outline reported error');
            count++;
            const malformed = toggleModule(id);
            requests[4].resolve({entities:null}); await malformed;
            if (state.expandedModules.has(id) || state.outlines.has(id))
                throw Error('malformed outline cached');
            count++;
        } finally {
            api = originalApi; state.expandedModules.delete(id);
            state.outlines.delete(id); clearToast(); renderTree();
        }
        return count;
    }""")
    assert outline_cases == 5
    # Retain expanded branches and only a bounded LRU of collapsed ones.
    outline_cache_cases = page.evaluate("""async () => {
        const originalApi=api, prefix='ATLAS-OUTLINE-CACHE-';
        const saved={outlines:new Map(state.outlines),expanded:new Set(state.expandedModules),
                     pages:new Map(outlinePages)};
        const pinned=prefix+'pinned', ids=Array.from({length:COLLAPSED_OUTLINE_LIMIT},
            (_,i)=>prefix+i), fresh=prefix+'new', late=prefix+'late';
        const requests=[];
        const key=id=>JSON.stringify([id,'object']);
        let count=0;
        try{
            state.outlines.clear();state.expandedModules.clear();outlinePages.clear();
            state.expandedModules.add(pinned);state.outlines.set(pinned,[]);
            for(const id of ids){state.outlines.set(id,[]);outlinePages.set(key(id),3);}
            api=(url,options)=>url.includes(prefix)
                ? new Promise((resolve,reject)=>requests.push({resolve,reject}))
                : originalApi(url,options);
            await toggleModule(ids[0]);await toggleModule(ids[0]);
            if(requests.length)throw Error('warm outline refetched');
            count++;
            let p=toggleModule(fresh);requests.at(-1).resolve({entities:[]});await p;
            if(state.outlines.size!==COLLAPSED_OUTLINE_LIMIT+2)
                throw Error('expanded branch counted toward collapsed cap');
            count++;
            await toggleModule(fresh);
            if(state.outlines.size!==COLLAPSED_OUTLINE_LIMIT+1)throw Error('collapsed cap');
            count++;
            if(!state.outlines.has(pinned)||!state.outlines.has(ids[0])||state.outlines.has(ids[1]))
                throw Error('incorrect outline LRU eviction');
            count++;
            if(outlinePages.has(key(ids[1])))throw Error('orphan pagination state');
            count++;
            p=toggleModule(ids[1]);const req=requests.at(-1);
            await toggleModule(ids[1]);const q=toggleModule(ids[1]);
            if(requests.at(-1)!==req)throw Error('pending outline duplicated');
            count++;
            req.resolve({entities:[{id:'fixture'}]});await Promise.all([p,q]);
            if(!state.expandedModules.has(ids[1])||state.outlines.get(ids[1]).length!==1)
                throw Error('evicted outline not restored');
            count++;
            p=toggleModule(late);await toggleModule(late);
            requests.at(-1).resolve({entities:[]});await p;
            if(!state.outlines.has(late)||[...state.outlines.keys()].filter(
                id=>!state.expandedModules.has(id)).length!==COLLAPSED_OUTLINE_LIMIT)
                throw Error('late collapsed response exceeded cache cap');
            count++;
            return count;
        }finally{
            api=originalApi;
            state.outlines.clear();for(const [k,v] of saved.outlines)state.outlines.set(k,v);
            state.expandedModules.clear();for(const id of saved.expanded)state.expandedModules.add(id);
            outlinePages.clear();for(const [k,v] of saved.pages)outlinePages.set(k,v);
            renderTree();
        }
    }""")
    assert outline_cache_cases == 8
    # Selecting another object in an expanded domain must preserve existing
    # DOM nodes and keyboard focus rather than rebuild the entire tree.
    tree_reuse_cases = page.evaluate("""async () => {
        const originalApi=api, id='DG-14';
        const module=state.modules.find(m=>m.id===id);
        const saved={domains:new Set(state.expandedDomains),expanded:new Set(state.expandedModules),
            outlines:new Map(state.outlines),pages:new Map(outlinePages),
            module:state.currentModule,entity:state.currentEntity,mode:state.granularity};
        const tree=document.getElementById('tree');
        let count=0,pending;
        try{
            state.expandedDomains.add(module.domain);state.expandedModules.add(id);
            state.granularity='object';
            state.outlines.set(id,[{id:'reuse-a',kind:'section',title:'A'},
                                  {id:'reuse-b',kind:'section',title:'B'}]);
            state.currentModule=id;state.currentEntity='reuse-a';renderTree();
            const row=tree.querySelector('[data-tree-entity="reuse-a"]');
            const next=tree.querySelector('[data-tree-entity="reuse-b"]');
            const chapter=tree.querySelector('[data-tree-module="DG-14"]');
            const focus=chapter.querySelector('.module-name');
            focus.focus();
            state.currentEntity='reuse-b';refreshTreeSelection(module.domain);
            if(tree.querySelector('[data-tree-entity="reuse-a"]')!==row||
               tree.querySelector('[data-tree-entity="reuse-b"]')!==next||
               document.activeElement!==focus||row.classList.contains('active')||
               !next.classList.contains('active')||!chapter.classList.contains('active'))
                throw Error('selection rebuilt tree or lost focus');
            count++;
            state.currentEntity=null;refreshTreeSelection(module.domain);
            if(next.classList.contains('active')||document.activeElement!==focus)
                throw Error('module selection retained entity or lost focus');
            count++;
            api=(url,options)=>url==='/api/modules/DG-14/outline'
                ?new Promise((resolve,reject)=>pending={resolve,reject}):originalApi(url,options);
            await toggleModule(id);state.outlines.delete(id);
            const first=toggleModule(id);await toggleModule(id);
            const before=tree.firstElementChild;
            pending.resolve({entities:[]});await first;
            if(tree.firstElementChild!==before)throw Error('collapsed response rebuilt tree');
            count++;
            state.outlines.delete(id);
            const second=toggleModule(id);
            toggleDomain(module.domain);
            const hidden=tree.firstElementChild;
            pending.resolve({entities:[]});await second;
            if(tree.firstElementChild!==hidden)throw Error('hidden domain response rebuilt tree');
            count++;
            refreshTreeSelection(module.domain);
            if(!state.expandedDomains.has(module.domain)||
               !tree.querySelector('[data-tree-module="DG-14"]'))
                throw Error('selection did not reveal new domain');
            count++;
            return count;
        }finally{
            api=originalApi;
            state.expandedDomains=saved.domains;state.expandedModules=saved.expanded;
            state.outlines=saved.outlines;
            outlinePages.clear();for(const [k,v] of saved.pages)outlinePages.set(k,v);
            state.currentModule=saved.module;state.currentEntity=saved.entity;
            state.granularity=saved.mode;renderTree();
        }
    }""")
    assert tree_reuse_cases == 5

    # A new target must start at its beginning, even if the previous
    # chapter had been scrolled far down. Test both chapter and entity routes.
    page.evaluate("() => openModule('AM1-14', true)")
    reader = page.locator('#view-reader')
    reader.evaluate('el => {el.scrollTop=el.scrollHeight}')
    assert reader.evaluate('el => el.scrollTop > 0')
    page.evaluate("() => openModule('DG-14')")
    assert page.evaluate("state.currentModule === 'DG-14'")
    assert reader.evaluate('el => el.scrollTop === 0')
    outline = page.evaluate("() => api('/api/modules/DG-14/outline')")
    entity = next(item['id'] for item in outline['entities'] if item['kind'] == 'section')
    reader.evaluate('el => {el.scrollTop=el.scrollHeight}')
    assert reader.evaluate('el => el.scrollTop > 0')
    page.evaluate('id => openEntity(id)', entity)
    assert page.evaluate('id => state.currentEntity === id', entity)
    assert reader.evaluate('el => el.scrollTop === 0')

    # A rejected superseded API request must not display an error for the
    # currently open chapter. Test both routes and both completion orders.
    races = page.evaluate("""async () => {
        const originalApi = api;
        const requests = [];
        const moduleData = await api('/api/modules/DG-14');
        const outline = await api('/api/modules/DG-14/outline');
        const entityId = outline.entities.find(item => item.kind === 'section').id;
        const entityData = await api('/api/entities/' + encodeURIComponent(entityId));
        const open = kind => kind === 'module' ? openModule('DG-14') : openEntity(entityId);
        const data = kind => kind === 'module' ? moduleData : entityData;
        const isCurrent = kind => state.currentModule === 'DG-14' &&
            state.currentEntity === (kind === 'module' ? null : entityId);
        const intercept = (url, options) => {
            if (url === '/api/modules/DG-14' ||
                url === '/api/entities/' + encodeURIComponent(entityId)) {
                return new Promise((resolve, reject) => requests.push({resolve, reject}));
            }
            return originalApi(url, options);
        };
        // toast is a const; observe its real DOM output instead of replacing it.
        const toastBox = document.getElementById('toast');
        const resetToast = () => {toastBox.textContent = ''; toastBox.classList.add('hidden');};
        let count = 0;
        try {
            api = intercept;
            for (const oldKind of ['module', 'entity']) {
                for (const newKind of ['module', 'entity']) {
                    requests.length = 0; resetToast();
                    const old = open(oldKind), current = open(newKind);
                    requests[1].resolve(data(newKind)); await current;
                    requests[0].reject(new Error('superseded navigation error')); await old;
                    if (!isCurrent(newKind) || toastBox.textContent !== '') throw Error('obsolete error');
                    count++;
                    requests.length = 0; resetToast();
                    const stale = open(oldKind), failing = open(newKind);
                    requests[1].reject(new Error('current navigation error')); await failing;
                    requests[0].resolve(data(oldKind)); await stale;
                    if (!isCurrent(newKind) || toastBox.textContent !== 'current navigation error')
                        throw Error('current error or stale success mishandled');
                    count++;
                }
            }
        } finally {
            api = originalApi; resetToast();
        }
        return count;
    }""")
    assert races == 8
    # A slow chapter, entity or reference lookup must not override an
    # explicitly selected tab, including a return to the existing reader.
    tab_races = page.evaluate("""async () => {
        const originalApi=api;
        const moduleData=await api('/api/modules/DG-14');
        const outline=await api('/api/modules/DG-14/outline');
        const id=outline.entities.find(item=>item.kind==='section').id;
        const entityData=await api('/api/entities/'+encodeURIComponent(id));
        const routes=[
            [()=>openModule('DG-14'),moduleData],
            [()=>openEntity(id),entityData],
            [()=>openLabel('atlas-tab-race','DG-14'),{document_id:'DG-14'}]
        ];
        const toastBox=document.getElementById('toast');
        const resetToast=()=>{toastBox.textContent='';toastBox.classList.add('hidden');};
        let pending,count=0;
        await openModule('AM1-14');
        try {
            api=(url,options)=>{
                if(url==='/api/modules/DG-14'||
                   url==='/api/entities/'+encodeURIComponent(id)||
                   url.startsWith('/api/labels/atlas-tab-race'))
                    return new Promise((resolve,reject)=>pending={resolve,reject});
                return originalApi(url,options);
            };
            for(const [open,data] of routes){
                for(const tab of ['selection','reader']){
                    for(const failure of [false,true]){
                        activateTab('selection');resetToast();
                        const old=open();
                        activateTab(tab);
                        if(failure)pending.reject(Error('obsolete navigation'));
                        else pending.resolve(data);
                        await old;
                        if(state.tab!==tab||state.currentModule!=='AM1-14'||
                           state.currentEntity!==null||toastBox.textContent)
                            throw Error('stale navigation changed selected tab or reader');
                        count++;
                    }
                }
            }
            const current=openModule('DG-14');
            pending.resolve(moduleData);await current;
            if(state.tab!=='reader'||state.currentModule!=='DG-14')
                throw Error('current navigation did not open reader');
            return count+1;
        }finally{api=originalApi;resetToast();activateTab('reader');}
    }""")
    assert tab_races == 13
    # Changes to the generated collection update only the membership
    # indicator, not the source/KaTeX DOM or the user's selected line range.
    page.evaluate("() => openModule('AM1-14', true)")
    selection_reuse = page.evaluate("""() => {
        const saved=new Map(state.selected);
        const source=document.getElementById('latexSource');
        const preview=document.getElementById('simplified');
        const start=document.getElementById('rangeStart');
        const end=document.getElementById('rangeEnd');
        const button=document.getElementById('addCurrent');
        const reader=document.getElementById('view-reader');
        const oldRange=[start.value,end.value],oldScroll=reader.scrollTop;
        let count=0;
        try{
            state.selected.clear();renderSelection();updateCurrentSelectionButton();
            const first=source.firstChild,math=preview.firstChild;
            if(!first||!math)throw Error('missing reader fixture');
            start.value='2';end.value='4';
            const check=selected=>{
                if(source.firstChild!==first||preview.firstChild!==math||
                   start.value!=='2'||end.value!=='4'||
                   button.textContent!==(selected?'✓ W zestawie':'+ Do zestawu'))
                    throw Error('selection change rebuilt reader or reset range');
                count++;
            };
            button.click();check(true);
            button.click();check(false);
            button.click();
            document.querySelector('#selectionList .selection-controls button:last-child').click();
            check(false);
            button.click();document.getElementById('clearSelection').click();check(false);
            return count;
        }finally{
            state.selected=saved;renderSelection();updateCurrentSelectionButton();
            start.value=oldRange[0];end.value=oldRange[1];reader.scrollTop=oldScroll;
        }
    }""")
    assert selection_reuse == 4
    # Switching source/preview retains both DOM trees and the chosen range.
    mode_reuse = page.evaluate("""() => {
        const source=document.getElementById('latexSource');
        const preview=document.getElementById('simplified');
        const button=document.getElementById('togglePreview');
        const start=document.getElementById('rangeStart');
        const end=document.getElementById('rangeEnd');
        const oldMode=state.simplified,oldRange=[start.value,end.value];
        let count=0;
        try{
            if(!state.simplified)button.click();
            const first=source.firstChild,math=preview.firstChild;
            if(!first||!math)throw Error('missing current reader content');
            start.value='2';end.value='4';
            for(let i=0;i<6;i++){
                button.click();
                if(source.firstChild!==first||preview.firstChild!==math||
                   start.value!=='2'||end.value!=='4'||
                   source.classList.contains('hidden')!==state.simplified||
                   preview.classList.contains('hidden')===state.simplified||
                   button.getAttribute('aria-pressed')!==String(!state.simplified))
                    throw Error('mode toggle rebuilt panes or reset range');
                count++;
            }
            return count;
        }finally{
            if(state.simplified!==oldMode)button.click();
            start.value=oldRange[0];end.value=oldRange[1];
        }
    }""")
    assert mode_reuse == 6

    # Source mode and keyboard interaction must also work at 180% text.
    page.evaluate("() => openModule('AM1-14', true)")
    page.set_viewport_size({'width': 390, 'height': 350})
    reader.evaluate('el => {el.scrollTop=el.scrollHeight / 2}')
    toggle = page.locator('#togglePreview')
    toggle.focus()
    toggle.press('Enter')
    assert page.locator('#latexSource').is_visible()
    assert toggle.get_attribute('aria-pressed') == 'true'
    reader.evaluate('el => {el.scrollTop=el.scrollHeight / 2}')
    assert_viewport_layout(page)
    toggle.focus()
    toggle.press('Enter')
    assert page.locator('#simplified').is_visible()
    assert toggle.get_attribute('aria-pressed') == 'false'
    page.set_viewport_size({'width': 1360, 'height': 900})
    reader.evaluate('el => {el.scrollTop=0}')

    # Fullscreen retains the same single reader scroll owner with large text.
    page.locator('#readingMode').click()
    page.wait_for_function('document.fullscreenElement !== null')
    assert_viewport_layout(page)
    reader.evaluate('el => {el.scrollTop=el.scrollHeight}')
    fullscreen_pinned = page.evaluate("""() => {
        const view = document.getElementById('view-reader');
        const toolbar = view.querySelector('.reader-toolbar');
        return {offset:toolbar.getBoundingClientRect().top-view.getBoundingClientRect().top,
                remaining:view.getBoundingClientRect().bottom-toolbar.getBoundingClientRect().bottom};
    }""")
    assert abs(fullscreen_pinned['offset']) <= 2, fullscreen_pinned
    assert fullscreen_pinned['remaining'] >= 40, fullscreen_pinned
    # A fixed-position overlay outside the fullscreen element can have a
    # nonempty bounding box yet be absent from the painted/hit-tested UI.
    reader.evaluate('el => {el.scrollTop=0}')
    page.evaluate("""async () => {
        await previewLabel('ch:ga5-rozdmuchania',
                           document.getElementById('togglePreview'), 'ALG-08');
        toast('Kontrola powiadomienia w pełnym ekranie');
    }""")
    page.locator('#tipBody h3').filter(has_text='Rozdmuchania').wait_for()
    overlay_check = """() => {
        const ids=['tipOpen','toast'];
        return ids.map(id=>{
            const el=document.getElementById(id), r=el.getBoundingClientRect();
            const hit=document.elementFromPoint(r.left+r.width/2,r.top+r.height/2);
            return {id,inside:document.querySelector('.app-shell').contains(el),
                    fullscreen:!document.fullscreenElement||document.fullscreenElement.contains(el),
                    hit:el.contains(hit)};
        });
    }"""
    overlays=page.evaluate(overlay_check)
    assert all(x['inside'] and x['fullscreen'] and x['hit'] for x in overlays), overlays
    page.evaluate("() => {closeTip();document.getElementById('toast').classList.add('hidden');}")
    page.keyboard.press('Escape')
    page.wait_for_function("!document.documentElement.classList.contains('reading-mode')")
    assert_viewport_layout(page)
    page.locator('#textSizeReset').click()

    # Real browser DOM with controlled Fullscreen API promises, so delayed
    # native transitions and refusals are deterministic rather than timed.
    page.wait_for_function('document.fullscreenElement === null')
    fullscreen_races = page.evaluate("""async () => {
        const shell=document.querySelector('.app-shell');
        const saved=[ [document,'fullscreenElement'],[document,'exitFullscreen'],
                      [shell,'requestFullscreen'] ].map(([obj,key])=>
                      [obj,key,Object.getOwnPropertyDescriptor(obj,key)]);
        let active=null, entry, exit, entries=0, exits=0, count=0;
        const change=()=>document.dispatchEvent(new Event('fullscreenchange'));
        const completeEntry=()=>{active=shell;change();entry.resolve();};
        const completeExit=()=>{active=null;change();exit.resolve();};
        const tick=async()=>{await Promise.resolve();await Promise.resolve();};
        try {
            Object.defineProperty(document,'fullscreenElement',{configurable:true,get:()=>active});
            Object.defineProperty(shell,'requestFullscreen',{configurable:true,value:()=>{
                entries++;return new Promise((resolve,reject)=>{entry={resolve,reject};});
            }});
            Object.defineProperty(document,'exitFullscreen',{configurable:true,value:()=>{
                exits++;return new Promise((resolve,reject)=>{exit={resolve,reject};});
            }});
            let pending=enterReadingMode();
            document.dispatchEvent(new KeyboardEvent('keydown',{key:'Escape',cancelable:true}));
            if(readingMode)throw Error('Escape did not leave pending entry');
            completeEntry();await tick();
            if(exits!==1)throw Error('late entry was not exited');
            completeExit();await pending;
            if(readingMode||ownedFullscreen||active)throw Error('late entry leaked');
            count++;
            pending=enterReadingMode();await leaveReadingMode();await enterReadingMode();
            if(entries!==2)throw Error('duplicated native entry');
            completeEntry();await pending;
            if(!readingMode||!ownedFullscreen)throw Error('latest entry intent lost');
            active=null;change();
            if(readingMode||ownedFullscreen)throw Error('native exit not reconciled');
            count++;
            pending=enterReadingMode();entry.reject(Error('denied'));await pending;
            if(!readingMode||ownedFullscreen)throw Error('layout fallback lost');
            await leaveReadingMode();
            if(exits!==1)throw Error('fallback attempted native exit');
            count++;
            active=document.createElement('div');
            await enterReadingMode();await leaveReadingMode();
            if(entries!==3||exits!==1||!active)throw Error('foreign fullscreen disturbed');
            active=null;count++;
            pending=enterReadingMode();completeEntry();await pending;
            let leaving=leaveReadingMode();exit.reject(Error('denied'));await leaving;
            if(!readingMode||!ownedFullscreen)throw Error('exit refusal stranded user');
            leaving=leaveReadingMode();completeExit();await leaving;
            if(readingMode||ownedFullscreen)throw Error('exit retry failed');
            count++;
            pending=enterReadingMode();completeEntry();await pending;
            leaving=leaveReadingMode();await enterReadingMode();
            completeExit();await leaving;
            if(!readingMode||ownedFullscreen||entries!==5)
                throw Error('reentry during exit did not retain layout fallback');
            await leaveReadingMode();count++;
            return count;
        } finally {
            for(const [obj,key,descriptor] of saved){
                if(descriptor)Object.defineProperty(obj,key,descriptor);
                else delete obj[key];
            }
            ownedFullscreen=false;fullscreenEntryPending=false;fullscreenExitPending=false;
            setReadingMode(false);
        }
    }""")
    assert fullscreen_races == 6

    # Switching between short previews, full chapters and other tabs must not
    # leave an independently scrollable document underneath the app shell.
    for module in ('DG-14', 'ALG-10', 'AM1-14'):
        for full in (False, True):
            page.evaluate('([module,full]) => openModule(module,full)', [module, full])
            assert_viewport_layout(page)
            page.evaluate('window.scrollTo(0,100000)')
            assert_viewport_layout(page)

    page.evaluate("() => openModule('ALG-10', true)")
    tables = page.locator('#simplified .preview-table')
    assert tables.count() > 0
    assert tables.first.locator('tr').count() >= 2
    assert tables.first.locator('.katex').count() > 0
    assert r'\hline' not in tables.first.inner_text()
    assert tables.first.locator('.preview-rule-bottom').count() > 0

    table_source = (r'\begin{tabular}{cc}\hline '
                    r'\textbf{A\&B}&$\begin{aligned}x&=1\\y&=2\end{aligned}$\\\hline '
                    r'\textit{C}&D\\\hline\end{tabular}')
    page.evaluate("source => renderSimplified(source, 'DG-14')", table_source)
    table = page.locator('#simplified .preview-table')
    assert table.locator('tr').count() == 2
    assert table.locator('td').count() == 4
    assert table.locator('strong').inner_text() == 'A&B'
    assert table.locator('.katex').count() == 1
    assert table.locator('.preview-rule-bottom').count() == 2
    assert page.locator('#mathPreviewStatus').is_hidden()
    assert_viewport_layout(page)

    source = (r'\chapter{Test \texorpdfstring{\emph{Visible $x^2$}}{PDF-ONLY}}'
              r'\section{\texorpdfstring{Second \texorpdfstring{$\alpha$}{INNER-PDF}}{OUTER-PDF}}'
              r'\texorpdfstring{Body \textbf{bold}}{BODY-PDF}')
    page.evaluate("source => renderSimplified(source, 'DG-14')", source)
    box = page.locator('#simplified')
    assert box.locator('h2 em .katex').count() == 1
    assert box.locator('h3 .katex').count() == 1
    assert box.locator('strong').inner_text() == 'bold'
    assert 'texorpdfstring' not in box.inner_text()
    assert 'PDF' not in box.inner_text()
    assert page.locator('#mathPreviewStatus').is_hidden()

    # Real chapter-local macros must also work in detached theorem fragments.
    page.evaluate("() => openModule('AM1-36')")
    # Reproduce the report using the canonical chapter, not only a fixture.
    assert page.evaluate(r"() => state.currentData.latex.includes('\\begingroup')")
    # Verify a real prose anchor from the currently fetched chapter instead
    # of tying renderer correctness to a historical editorial introduction.
    prose = page.evaluate(r"""() => {
        const source = state.currentData.latex;
        const line = source.split('\n').find(line =>
            line.trim() && !line.trim().startsWith('\\') &&
            /^[A-ZĄĆĘŁŃÓŚŹŻ][^\\$%{}]{20,}/.test(line));
        return line?.match(/^[^\\$%{}]{20,}/)?.[0].trim().slice(0, 60) || '';
    }""")
    assert len(prose) >= 20, prose
    assert prose in box.inner_text(), prose
    assert r'\begingroup' not in box.inner_text()
    assert r'\providecommand' not in box.inner_text()
    # The source pane must remain lossless.
    assert r'\begingroup' in page.locator('#latexSource').text_content()
    assert page.evaluate(r"() => previewMacros('AM1-36')['\\HK']") == r"\mathrm{KH}"
    fragment = r"$\R,\C,\K,\HK,\Var_I F,\osc_I F,\BV,\ind{A}$"
    page.evaluate("source => renderSimplified(source, 'AM1-36')", fragment)
    assert box.locator('.katex').count() == 1
    assert box.locator('.katex-error').count() == 0
    assert page.locator('#mathPreviewStatus').is_hidden()
    assert page.evaluate(r"() => previewMacros('AM1-14')['\\HK'] === undefined")
    assert page.evaluate(r"() => previewMacros('MOD')['\\Q']") == r"\mathrm Q"

    # A closing brace inside a comment must not end a declaration early.
    # Grouping commands delimit scope but are not reader-visible prose.
    commented = (r'\begingroup\providecommand% comment between arguments' + '\n'
                 + r'{\testmacro}% comment before replacement' + '\n'
                 + r'{\frac{1}{% }' + '\n'
                 + r'2}}' + '\n' + r'Widoczny tekst: $\R$.\endgroup')
    page.evaluate("source => renderSimplified(source, 'AM1-36')", commented)
    assert 'Widoczny tekst:' in box.inner_text()
    assert '2}' not in box.inner_text()
    assert r'\begingroup' not in box.inner_text()
    assert r'\endgroup' not in box.inner_text()
    assert box.locator('.katex').count() == 1
    assert page.locator('#mathPreviewStatus').is_hidden()

    # Counter controls used by FA-15A/15B are source metadata, not prose.
    counters = (r'\setcounter{section}{15}\begingroup'
                r'\renewcommand{\thesection}{15A}'
                r'\renewcommand{\theHsection}{15A}'
                r'\section{Całkowanie}\addtocounter{section}{1}'
                r'\stepcounter{equation}\refstepcounter{equation}'
                r'Widoczny tekst: $x$.\endgroup')
    page.evaluate("source => renderSimplified(source, 'FA-15A')", counters)
    assert 'Widoczny tekst:' in box.inner_text()
    assert box.locator('h3').inner_text() == 'Całkowanie'
    for metadata in ('setcounter', 'addtocounter', 'stepcounter', 'refstepcounter',
                     'thesection', 'theHsection', '15A', 'begingroup', 'endgroup'):
        assert metadata not in box.inner_text(), metadata
    assert box.locator('.katex').count() == 1

    # Keep wide equations and code independently scrollable, rather than
    # hiding document overflow and accidentally clipping their contents.
    wide = r'\[' + '+'.join(f'x_{{{i}}}' for i in range(100)) + r'\]'
    listing = r'\begin{lstlisting}' + '\n' + 'long_code = ' + 'value + ' * 100 + '\n' + r'\end{lstlisting}'
    page.evaluate("source => renderSimplified(source, 'DG-14')", wide + listing)
    for selector in ('.katex-display', '.preview-listing'):
        assert box.locator(selector).evaluate('el => el.scrollWidth > el.clientWidth'), selector
    assert_viewport_layout(page)
    page.screenshot(path=str(Path(os.environ.get('TEMP', '/tmp')) / 'atlas-reader-layout-fixed.png'))
    assert not errors, errors
    browser.close()
    print('TeX/PDF headings, viewport fill, one reader scroll owner, small viewport, large text, fullscreen and local wide content: OK')
