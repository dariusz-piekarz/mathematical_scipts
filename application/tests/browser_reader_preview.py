"""Reader regression check against a running local Atlas (MATLIB_TEST_URL)."""
import os
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
URL = os.environ.get('MATLIB_TEST_URL', 'http://127.0.0.1:8765')

with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=True)
    page = browser.new_page(viewport={'width': 1520, 'height': 900}, color_scheme='light')
    errors = []
    page.on('pageerror', lambda error: errors.append(str(error)))
    page.goto(URL, wait_until='networkidle')
    page.evaluate("() => openModule('ALG-08')")
    page.locator('#docTitle').filter(has_text='Geometria biwymierna').wait_for()
    chapter = (ROOT.parent / 'chapters/pl/algebraic_geometry/08-geometria-biwymierna-i-modele-minimalne-powierzchni.tex').read_text(encoding='utf-8')
    page.evaluate("latex => renderSimplified(latex, 'ALG-08')", chapter)
    box = page.locator('#simplified')
    page.wait_for_function("document.querySelectorAll('#simplified .preview-figure').length === 4 && [...document.querySelectorAll('#simplified .preview-figure')].every(box => box.querySelector('button') || (box.querySelector('img')?.complete && box.querySelector('img').naturalWidth > 0))", timeout=90000)
    assert box.locator('.preview-figure').count() == 4
    assert box.locator('.preview-figure button').count() == 0, box.locator('.preview-figure').all_inner_texts()
    page.wait_for_function("tikzActive.size === 0 && tikzQueue.length === 0")
    # Exercise queue lifecycle with real DOM/AbortController and controlled
    # responses, independently of the speed of the TeX compiler.
    queue_cases = page.evaluate("""async () => {
        const originalFetch=window.fetch, originalCreate=URL.createObjectURL,
              originalRevoke=URL.revokeObjectURL;
        const host=document.createElement('div');document.body.append(host);
        const requests=[],created=[],revoked=[];
        const wait=async condition=>{
            for(let i=0;i<500;i++){
                if(condition())return;
                await new Promise(resolve=>setTimeout(resolve,10));
            }
            throw Error('TikZ lifecycle timeout');
        };
        const good=()=>new Response(new Blob([
            '<svg xmlns="http://www.w3.org/2000/svg" width="10" height="10"><rect width="10" height="10"/></svg>'
        ],{type:'image/svg+xml'}));
        let count=0;
        try{
            window.fetch=(url,options)=>{
                if(!url.includes('/ATLAS-TIKZ-QUEUE/'))return originalFetch(url,options);
                return new Promise((resolve,reject)=>{
                    const signal=options.signal;
                    requests.push({resolve,signal});
                    signal.addEventListener('abort',()=>reject(new Error('aborted')),{once:true});
                });
            };
            URL.createObjectURL=blob=>{const url=originalCreate.call(URL,blob);created.push(url);return url;};
            URL.revokeObjectURL=url=>{revoked.push(url);originalRevoke.call(URL,url);};
            const figures=Array.from({length:6},()=>{
                const figure=document.createElement('figure');host.append(figure);return figure;
            });
            const jobs=figures.map((figure,i)=>loadTikzFigure(figure,'fixture'+i,'ATLAS-TIKZ-QUEUE',true));
            figures[5].remove();
            await wait(()=>requests.length===3);
            if(tikzActive.size!==3)throw Error('concurrency cap');
            count++;
            figures[0].remove();
            await wait(()=>requests.length===4);
            if(!requests[0].signal.aborted)throw Error('detached fetch not aborted');
            count++;
            requests[1].resolve(good());await wait(()=>requests.length===5);
            if(!figures[1].querySelector('img')?.naturalWidth||revoked.length!==1)
                throw Error('image did not release slot and Blob URL');
            count++;
            requests[2].resolve(new Response(JSON.stringify({detail:'fixture failure'}),{status:500}));
            requests[3].resolve(new Response(new Blob(['invalid image'],{type:'image/png'})));
            requests[4].resolve(good());
            await Promise.all(jobs);
            if(requests.length!==5||tikzActive.size||tikzQueue.length)
                throw Error('queue retained detached work');
            count++;
            if(!figures[2].querySelector('button')||!figures[3].querySelector('button')||
               !figures[2].textContent.includes('fixture failure'))
                throw Error('retry UI missing');
            count++;
            if(created.length!==3||revoked.length!==3||
                created.some(url=>revoked.filter(v=>v===url).length!==1))
                throw Error('Blob release mismatch');
            count++;
            figures[2].querySelector('button').click();
            await wait(()=>requests.length===6);
            requests[5].resolve(good());
            await wait(()=>tikzActive.size===0&&tikzQueue.length===0);
            if(!figures[2].querySelector('img')?.naturalWidth||revoked.length!==4)
                throw Error('retry did not complete');
            count++;
            const controller=new AbortController(),figure=document.createElement('figure');
            host.append(figure);
            const loading=displayTikzBlob(figure,new Blob(['pending']), 'fixture',controller.signal);
            controller.abort();await loading;
            if(created.length!==5||revoked.length!==5)throw Error('abort leaked Blob URL');
            return count+1;
        }finally{
            host.remove();
            for(const active of tikzActive)
                if(!active.figure.isConnected)active.controller.abort();
            await wait(()=>!tikzActive.size&&!tikzQueue.length);
            window.fetch=originalFetch;URL.createObjectURL=originalCreate;URL.revokeObjectURL=originalRevoke;
        }
    }""")
    assert queue_cases == 8
    text = box.inner_text()
    assert r'\providecommand' not in text and r'\noindent' not in text and r'\atlasref' not in text
    assert 'Dlaczego izomorfizm' in box.locator('h3').first.inner_text()
    assert box.locator('.ref-link').filter(has_text='AA-37:').count() == 1
    assert box.locator('.katex').count() > 20
    assert page.locator('#mathPreviewStatus').is_hidden(), page.locator('#mathPreviewStatus').inner_text()
    assert box.locator('.preview-block-title').filter(has_text='Definicja').count() > 0
    layout = box.locator('p').filter(has_text='Przy badaniu').evaluate('el => ({whiteSpace:getComputedStyle(el).whiteSpace,width:el.clientWidth,parent:el.parentElement.clientWidth})')
    assert layout['whiteSpace'] == 'normal' and layout['width'] > layout['parent'] * .9, layout
    # Balanced arguments, comments, math preservation and HTML safety.
    page.evaluate(r'''() => renderSimplified('Tekst pierwszej linii\nciąg dalszy.\n\n\\textbf{Ważne \\emph{zagnieżdżenie}} % komentarz\n $x<y$ <img src=x onerror=alert(1)> \\[a+b\\]', 'ALG-08')''')
    assert box.locator('strong em').inner_text() == 'zagnieżdżenie'
    assert box.locator('img').count() == 0
    assert 'komentarz' not in box.inner_text()
    assert box.locator('.katex').count() == 2
    page.locator('#themeToggle').click()
    assert page.locator('html').get_attribute('data-theme') == 'dark'
    dark = box.evaluate('el => ({background:getComputedStyle(el).backgroundColor,color:getComputedStyle(el).color})')
    assert dark['background'] != 'rgb(255, 255, 255)', dark
    page.reload(wait_until='networkidle')
    assert page.locator('html').get_attribute('data-theme') == 'dark'
    page.evaluate("() => openModule('ALG-08')")
    page.locator('#docTitle').filter(has_text='Geometria biwymierna').wait_for()
    page.evaluate("latex => renderSimplified(latex, 'ALG-08')", chapter)
    page.wait_for_function("[...document.querySelectorAll('#simplified .preview-figure img')].filter(img => img.complete && img.naturalWidth > 0).length === 4", timeout=90000)
    box.locator('.preview-figure').first.scroll_into_view_if_needed()
    page.screenshot(path=os.environ.get('MATLIB_SCREENSHOT', str(Path(os.environ['TEMP']) / 'atlas-reader-dark.png')))
    page.set_viewport_size({'width': 390, 'height': 844})
    assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
    page.locator('#themeToggle').click()
    assert page.locator('html').get_attribute('data-theme') == 'light'
    assert not errors, errors
    browser.close()
    print('Reader prose, math, references, safe content, responsive layout and persistent themes and four rendered TikZ figures: OK')
