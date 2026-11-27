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
    # Test the normal chapter route with the server's actual indexed LaTeX,
    # not a synthetic renderer fixture or a manual renderSimplified call.
    page.evaluate("() => openModule('AA-01')")
    box = page.locator('#simplified')
    frames = box.locator('.preview-statement')
    definition = frames.filter(has=page.locator('.preview-block-title').filter(has_text='Definicja — Grupa')).first
    definition.wait_for(state='visible')
    for kind in ('definition', 'result', 'example'):
        # Match the frame itself, not just nested descendants.
        first = box.locator(f'.preview-statement[data-environment-kind="{kind}"]').first
        assert first.is_visible(), kind
        style = first.evaluate("""el => {
            const s=getComputedStyle(el);
            return {top:parseFloat(s.borderTopWidth), left:parseFloat(s.borderInlineStartWidth),
                    radius:parseFloat(s.borderTopLeftRadius), borderStyle:s.borderTopStyle,
                    color:s.borderTopColor, title:getComputedStyle(el.firstElementChild).color};
        }""")
        assert style['top'] >= 2 and style['left'] >= 4 and style['radius'] >= 12, style
        assert style['borderStyle'] == 'solid' and style['color'] == style['title'], style
    assert box.locator('[data-environment-kind="proof"].preview-statement').count() == 0
    count = frames.count()
    assert page.locator('#readerFrameStatus').inner_text() == f'Ramki: {count}'
    page.locator('#themeToggle').click()
    assert page.locator('html').get_attribute('data-theme') == 'dark'
    for frame in frames.all():
        assert frame.evaluate("el => getComputedStyle(el).borderTopStyle === 'solid' && parseFloat(getComputedStyle(el).borderTopWidth) >= 2")
    # Simulate a stylesheet mismatch and require a visible diagnostic.
    page.add_style_tag(content='.preview-statement {border:0!important}')
    page.evaluate("() => updateReaderFrameStatus()")
    assert page.locator('#readerFrameStatus').inner_text() == 'Ramki: błąd stylów'
    page.locator('style').last.evaluate('el => el.remove()')
    page.evaluate("() => updateReaderFrameStatus()")
    assert page.locator('#readerFrameStatus').inner_text() == f'Ramki: {count}'
    page.locator('#themeToggle').click()
    page.locator('#togglePreview').click()
    assert box.is_hidden() and page.locator('#latexSource').is_visible()
    page.locator('#togglePreview').click()
    assert box.is_visible() and frames.count() == count
    definition.scroll_into_view_if_needed()
    page.screenshot(path=str(Path(os.environ.get('TEMP', '/tmp')) / 'atlas-real-chapter-frames.png'))
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
                    requests.push({url,resolve,signal});
                    signal.addEventListener('abort',()=>reject(new Error('aborted')),{once:true});
                });
            };
            URL.createObjectURL=blob=>{const url=originalCreate.call(URL,blob);created.push(url);return url;};
            URL.revokeObjectURL=url=>{revoked.push(url);originalRevoke.call(URL,url);};
            const figures=Array.from({length:6},()=>{
                const figure=document.createElement('figure');host.append(figure);return figure;
            });
            const hashes=await Promise.all(figures.map(async (_,i)=>{
                const digest=await crypto.subtle.digest('SHA-256',new TextEncoder().encode('fixture'+i));
                return Array.from(new Uint8Array(digest),b=>b.toString(16).padStart(2,'0')).join('');
            }));
            const request=i=>requests.find(r=>r.url.endsWith('/'+hashes[i]+'.png'));
            const jobs=figures.map((figure,i)=>loadTikzFigure(figure,'fixture'+i,'ATLAS-TIKZ-QUEUE',true));
            figures[5].remove();
            await wait(()=>requests.length===3);
            if(tikzActive.size!==3)throw Error('concurrency cap');
            count++;
            figures[0].remove();
            await wait(()=>requests.length===4);
            if(!request(0).signal.aborted)throw Error('detached fetch not aborted');
            count++;
            request(1).resolve(good());await wait(()=>requests.length===5);
            if(!figures[1].querySelector('img')?.naturalWidth||revoked.length!==1)
                throw Error('image did not release slot and Blob URL');
            count++;
            request(2).resolve(new Response(JSON.stringify({detail:'fixture failure'}),{status:500}));
            request(3).resolve(new Response(new Blob(['invalid image'],{type:'image/png'})));
            request(4).resolve(good());
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
    # A starred heading is visible once; its ToC metadata is not prose.
    toc_source = (r"\chapter*{Wstęp do grafów}\phantomsection"
                  r"\addcontentsline {toc}{chapter}{Wstęp \textbf{do grafów}}"
                  r"\addtocontents{toc}{\protect\smallskip}"
                  "\n\nDalszy tekst.")
    page.evaluate("latex => renderSimplified(latex, 'GW-01')", toc_source)
    assert box.locator('h2').count() == 1
    assert box.locator('h2').inner_text() == 'Wstęp do grafów'
    assert box.inner_text().count('Wstęp') == 1
    assert 'Dalszy tekst.' in box.inner_text()
    assert not any(token in box.inner_text() for token in ('addcontentsline', 'addtocontents', 'phantomsection', 'tocchapter'))
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
    # Repository-backed Plotly figures are lazy, sandboxed and scoped to their chapter.
    chapter18 = (ROOT.parent / 'chapters/pl/mathematical_analysis_ii/18-twierdzenie-o-funkcji-odwrotnej.tex').read_text(encoding='utf-8')
    page.set_viewport_size({'width': 1520, 'height': 900})
    page.evaluate("latex => renderSimplified(latex, 'AM2-18')", chapter18)
    host = box.locator('.atlas-plot-host')
    assert host.count() == 1
    assert host.locator('iframe').count() == 0
    host.locator('button').click()
    iframe = host.locator('iframe')
    assert iframe.get_attribute('sandbox') == 'allow-scripts'
    frame = host.frame_locator('iframe')
    frame.locator('#plot[data-ready=true]').wait_for(timeout=60000)
    assert frame.locator('#plot .gl-container').count() > 0
    host.locator('button').click()
    assert iframe.count() == 0
    page.evaluate("latex => renderSimplified(latex, 'AM2-17')", chapter18)
    assert box.locator('.atlas-plot-host').count() == 0
    # AM II 01: exact polyhedral faces, 12 true edges each, no diagonals.
    source = (ROOT.parent / 'chapters/pl/mathematical_analysis_ii/01-przestrzenie-unormowane-i-banacha.tex').read_text(encoding='utf-8')
    page.evaluate("latex => renderSimplified(latex, 'AM2-01')", source)
    page.wait_for_function(
        """() => {
            const images = [...document.querySelectorAll('#simplified .atlas-tikz-preview img')];
            return images.length === 2 && images.every(img => img.complete && img.naturalWidth > 0);
        }""", timeout=180000)
    host = box.locator('.atlas-plot-host')
    assert host.count() == 1
    host.locator('button').click()
    frame = host.frame_locator('iframe')
    plot = frame.locator('#plot[data-ready=true]')
    plot.wait_for(timeout=60000)
    geometry = plot.evaluate("""el => {
        const d=el.data;
        return {types:d.map(t=>t.type), edges:[d[1],d[4]].map(t=>t.x.filter(x=>x===null).length),
                triangles:[d[0].i.length,d[3].i.length]};
    }""")
    assert geometry == {'types': ['mesh3d', 'scatter3d', 'surface', 'mesh3d', 'scatter3d'],
                        'edges': [12, 12], 'triangles': [8, 12]}, geometry
    host.locator('button').click()
    assert host.locator('iframe').count() == 0
    # Static TikZ and interactive Plotly coexist in chapters 19–24.
    for module, filename in [
        ('AM2-19', '19-twierdzenie-o-funkcji-uwiklanej.tex'),
        ('AM2-20', '20-twierdzenia-o-rzedzie.tex'),
        ('AM2-21', '21-podrozmaitosci-przestrzeni-euklidesowej.tex'),
        ('AM2-22', '22-ekstrema-zwiazane.tex'),
        ('AM2-23', '23-rachunek-rozniczkowy-na-podrozmaitosciach.tex'),
        ('AM2-24', '24-calka-riemanna.tex'),
    ]:
        source = (ROOT.parent / 'chapters/pl/mathematical_analysis_ii' / filename).read_text(encoding='utf-8')
        page.evaluate("([latex, code]) => renderSimplified(latex, code)", [source, module])
        # Dynamic TikZ first inserts a placeholder and loads the image asynchronously.
        # Wait for the actual decoded image, not just for an immediate DOM snapshot.
        assert box.locator('.atlas-tikz-preview').count() == 1, module
        page.wait_for_function(
            """() => {
                const images = document.querySelectorAll('#simplified .atlas-tikz-preview img');
                return images.length === 1 && images[0].complete && images[0].naturalWidth > 0;
            }""", timeout=90000
        )
        assert box.locator('.atlas-tikz-preview img').count() == 1, module
        host = box.locator('.atlas-plot-host')
        assert host.count() == 1
        assert host.locator('iframe').count() == 0
        host.locator('button').click()
        assert host.locator('iframe').get_attribute('sandbox') == 'allow-scripts'
        frame = host.frame_locator('iframe')
        frame.locator('#plot[data-ready=true]').wait_for(timeout=60000)
        assert frame.locator('#plot .gl-container').count() > 0
        if module == 'AM2-23':
            check = frame.locator('#plot').evaluate("""el => {
                const d=el.data, vec=t=>['x','y','z'].map(k=>t[k][1]-t[k][0]);
                const [g,w,e]=d.slice(2).map(vec);
                let error=0;
                for(let i=0;i<d[0].z.length;i++)for(let j=0;j<d[0].z[i].length;j++)
                    error=Math.max(error,Math.abs(d[0].x[i][j]**2+d[0].y[i][j]**2+d[0].z[i][j]**2-1));
                return {types:d.map(t=>t.type), error, dot:.6*g[0]+.8*g[2],
                    sum:Math.max(...g.map((v,i)=>Math.abs(v+w[i]-e[i])))};
            }""")
            assert check['types'] == ['surface', 'scatter3d', 'scatter3d', 'scatter3d', 'scatter3d']
            assert max(check['error'], abs(check['dot']), check['sum']) < 1e-12
        if module == 'AM2-24':
            check = frame.locator('#plot').evaluate("""el => {
                const meshes=el.data.filter(t=>t.type==='mesh3d');
                const volumes=['scene','scene2'].map(sc=>meshes.filter(t=>t.scene===sc).reduce((a,t)=>a+Math.max(...t.z)/4,0));
                return {meshes:meshes.length, volumes, edges:el.data.filter(t=>t.type==='scatter3d').length};
            }""")
            assert check['meshes'] == 8 and check['edges'] == 8, check
            assert abs(check['volumes'][0]-.5) < 1e-12, check
            assert abs(check['volumes'][1]-5/6) < 1e-12, check
        host.locator('button').click()
        assert host.locator('iframe').count() == 0
    # Real graph chapters: every figure must decode, not merely insert a placeholder.
    for module, filename, expected in (
        ('GW-01', '01-podstawy-teorii-grafow.tex', 7),
        ('GW-02', '02-drzewa-mosty-i-cykle-fundamentalne.tex', 6),
    ):
        source = (ROOT.parent / 'chapters/pl/graph_and_knot_theory' / filename).read_text(encoding='utf-8')
        page.evaluate("([latex, code]) => renderSimplified(latex, code)", [source, module])
        assert box.locator('.atlas-tikz-preview').count() == expected, module
        page.wait_for_function(
            """() => {
                const figures = [...document.querySelectorAll('#simplified .atlas-tikz-preview')];
                return figures.length > 0 && figures.every(f => f.querySelector('button') ||
                    (f.querySelector('img')?.complete && f.querySelector('img').naturalWidth > 0));
            }""", timeout=180000)
        assert box.locator('.atlas-tikz-preview button').count() == 0, (module, box.locator('.atlas-tikz-preview').all_inner_texts())
    assert not errors, errors
    browser.close()
    print('Reader prose, math, references, safe content, responsive layout and persistent themes, rendered TikZ and interactive Plotly figures: OK')
