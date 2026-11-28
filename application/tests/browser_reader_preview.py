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
        expected = 3 if module == 'AM2-24' else 1
        assert box.locator('.atlas-tikz-preview').count() == expected, module
        page.wait_for_function(
            """expected => {
                const images = [...document.querySelectorAll('#simplified .atlas-tikz-preview img')];
                return images.length === expected && images.every(img => img.complete && img.naturalWidth > 0);
            }""", arg=expected, timeout=180000
        )
        assert box.locator('.atlas-tikz-preview img').count() == expected, module
        hosts = box.locator('.atlas-plot-host')
        assert hosts.count() == expected
        if module == 'AM2-24':
            for i, identifier in enumerate(('am2_24_local_volume.html', 'am2_24_signed_volume.html')):
                host = hosts.nth(i)
                assert host.locator('iframe').count() == 0
                host.locator('button').click()
                iframe = host.locator('iframe')
                assert iframe.get_attribute('sandbox') == 'allow-scripts'
                assert iframe.get_attribute('src').endswith(identifier)
                frame = host.frame_locator('iframe')
                plot = frame.locator('#plot[data-ready=true]')
                plot.wait_for(timeout=60000)
                assert frame.locator('#plot .gl-container').count() > 0
                check = plot.evaluate("""el => {
                    const m=el.data.filter(t=>t.type==='mesh3d');
                    return {meshes:m.length, edges:el.data.filter(t=>t.type==='scatter3d').length,
                        vertices:m.map(t=>t.x.length), triangles:m.map(t=>t.i.length),
                        bounds:m.map(t=>['x','y','z'].map(k=>[Math.min(...t[k]),Math.max(...t[k])])),
                        planeError:Math.max(...m[0].x.slice(4).map((x,j)=>Math.abs(m[0].z[j+4]-(.3+.4*x+.3*m[0].y[j+4]))))};
                }""")
                assert check['meshes'] == 2 and check['edges'] == 2, check
                if i == 0:
                    assert check['vertices'] == [8, 8] and check['triangles'] == [12, 12], check
                    assert check['planeError'] < 1e-12, check
                    assert check['bounds'][1][:2] == [[.75, 1], [.75, 1]], check
                    assert abs(check['bounds'][1][2][1]-.825) < 1e-12, check
                else:
                    assert check['vertices'] == [6, 6] and check['triangles'] == [8, 8], check
                    assert check['bounds'] == [[[-1,0],[0,1],[-1,0]],[[0,1],[0,1],[0,1]]], check
                host.locator('button').click()
                assert iframe.count() == 0
        host = hosts.nth(expected-1)
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
    # AM II 26: slider cross-sections and the Gram area multiplier.
    source = (ROOT.parent / 'chapters/pl/mathematical_analysis_ii/26-calka-lebesguea-w-rn.tex').read_text(encoding='utf-8')
    page.evaluate("latex => renderSimplified(latex, 'AM2-26')", source)
    hosts = box.locator('.atlas-plot-host')
    assert hosts.count() == 2
    for i, identifier in enumerate(('am2_26_layers.html', 'am2_26_gram.html')):
        host = hosts.nth(i)
        assert host.locator('iframe').count() == 0
        host.locator('button').click()
        iframe = host.locator('iframe')
        assert iframe.get_attribute('sandbox') == 'allow-scripts'
        assert iframe.get_attribute('src').endswith(identifier)
        plot = host.frame_locator('iframe').locator('#plot[data-ready=true]')
        plot.wait_for(timeout=60000)
        if i == 0:
            check = plot.evaluate("""el => {
                const cuts=el.data.slice(2), slider=el.layout.sliders[0];
                return {count:cuts.length, steps:slider.steps.length,
                    visible:cuts.filter(t=>t.visible===true).length,
                    error:Math.max(...cuts.map(t=>Math.abs(Math.max(...t.x)-(1-t.z[0])))),
                    activeHeight:cuts[slider.active].z[0],
                    activeArea:Math.max(...cuts[slider.active].x)**2,
                    stepVisibility:slider.steps.every((s,i)=>s.args[0].visible.slice(2).every((v,j)=>v===(i===j)))};
            }""")
            assert check['count'] == check['steps'] == 20 and check['visible'] == 1, check
            assert check['error'] < 1e-12 and check['stepVisibility'], check
            assert abs(check['activeHeight']-.4) < 1e-12 and abs(check['activeArea']-.36) < 1e-12, check
        else:
            check = plot.evaluate("""el => {
                const s=el.data[2], a=[s.x[1]-s.x[0],0,s.z[0][1]-s.z[0][0]],
                    b=[0,s.y[1]-s.y[0],s.z[1][0]-s.z[0][0]];
                const cross=[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]];
                return {area:Math.hypot(...cross), projected:a[0]*b[1]};
            }""")
            assert abs(check['area']-3**.5/16) < 1e-12, check
            assert abs(check['projected']-1/16) < 1e-12, check
        host.locator('button').click()
        assert iframe.count() == 0
    # AM II 27: transverse tube volumes for all slider positions.
    source = (ROOT.parent / 'chapters/pl/mathematical_analysis_ii/27-calki-na-zbiorach-nieograniczonych-i-z-osobliwosciami.tex').read_text(encoding='utf-8')
    page.evaluate("latex => renderSimplified(latex, 'AM2-27')", source)
    host = box.locator('.atlas-plot-host')
    assert host.count() == 1
    host.locator('button').click()
    iframe = host.locator('iframe')
    assert iframe.get_attribute('sandbox') == 'allow-scripts'
    assert iframe.get_attribute('src').endswith('am2_27_tubes.html')
    plot = host.frame_locator('iframe').locator('#plot[data-ready=true]')
    plot.wait_for(timeout=60000)
    check = plot.evaluate("""el => {
        const s=el.layout.sliders[0], d=el.data;
        let error=0;
        for(let h=0;h<8;h++){
            const r=(h+1)/10;
            for(let k=0;k<3;k++){
                const m=d[3+6*h+2*k];
                const volume=['x','y','z'].reduce((v,a)=>v*(Math.max(...m[a])-Math.min(...m[a])),1);
                error=Math.max(error,Math.abs(volume-8*r**(3-k)));
            }
        }
        return {error, steps:s.steps.length, active:s.active,
            visible:d.slice(3).filter(t=>t.visible===true).length};
    }""")
    assert check['error'] < 1e-12 and check['steps'] == 8, check
    assert check['active'] == 3 and check['visible'] == 6, check
    host.locator('button').click()
    assert iframe.count() == 0
    # AM II 28: density and domain contributions, plus moving sphere geometry.
    source = (ROOT.parent / 'chapters/pl/mathematical_analysis_ii/28-calki-zalezne-od-parametrow.tex').read_text(encoding='utf-8')
    page.evaluate("latex => renderSimplified(latex, 'AM2-28')", source)
    hosts = box.locator('.atlas-plot-host')
    assert hosts.count() == 2
    for i, identifier in enumerate(('am2_28_leibniz.html', 'am2_28_moving_ball.html')):
        host = hosts.nth(i)
        host.locator('button').click()
        iframe = host.locator('iframe')
        assert iframe.get_attribute('sandbox') == 'allow-scripts'
        assert iframe.get_attribute('src').endswith(identifier)
        plot = host.frame_locator('iframe').locator('#plot[data-ready=true]')
        plot.wait_for(timeout=60000)
        if i == 0:
            check = plot.evaluate("""el => {
                const d=el.data, s=el.layout.sliders[0];
                const volume=m=>(m.x[1]-m.x[0])*((m.z[4]-m.z[0])+(m.z[5]-m.z[1]))/2;
                let error=0;
                for(let j=0;j<8;j++){
                    const h=(j+1)/20, v=volume(d[2+4*j])+volume(d[4+4*j]);
                    error=Math.max(error,Math.abs(v/h-(2.5+1.5*h+.5*h*h)));
                }
                return {error, steps:s.steps.length, active:s.active, old:volume(d[0])};
            }""")
            assert check['error'] < 1e-12 and abs(check['old']-1.5) < 1e-12, check
        else:
            check = plot.evaluate("""el => {
                const d=el.data, s=el.layout.sliders[0];
                let error=0;
                for(let j=0;j<8;j++){
                    const h=(j+1)/20,r=1+h/2,m=d[1+2*j];
                    for(let a=0;a<m.x.length;a++)for(let b=0;b<m.x[a].length;b++)
                        error=Math.max(error,Math.abs((m.x[a][b]-h)**2+m.y[a][b]**2+m.z[a][b]**2-r*r));
                }
                return {error,steps:s.steps.length,active:s.active};
            }""")
            assert check['error'] < 1e-12, check
        assert check['steps'] == 8 and check['active'] == 4, check
        host.locator('button').click()
        assert iframe.count() == 0
    # AM II 29: two parametrizations of the same helix.
    source = (ROOT.parent / 'chapters/pl/mathematical_analysis_ii/29-krzywe-dlugosc-i-prostowalnosc.tex').read_text(encoding='utf-8')
    page.evaluate("latex => renderSimplified(latex, 'AM2-29')", source)
    hosts = box.locator('.atlas-plot-host')
    assert hosts.count() == 3
    host = hosts.nth(0)
    host.locator('button').click()
    iframe = host.locator('iframe')
    assert iframe.get_attribute('sandbox') == 'allow-scripts'
    assert iframe.get_attribute('src').endswith('am2_29_arclength.html')
    plot = host.frame_locator('iframe').locator('#plot[data-ready=true]')
    plot.wait_for(timeout=60000)
    check = plot.evaluate("""el => {
        let error=0;
        const d=el.data,s=el.layout.sliders[0];
        for(let i=0;i<21;i++){
            const t=i/20;
            for(let k=0;k<2;k++){
                const q=k?t*t:t, m=d[3+4*i+2*k];
                error=Math.max(error,Math.abs(m.x[0]-Math.cos(2*Math.PI*q)),
                    Math.abs(m.y[0]-Math.sin(2*Math.PI*q)),Math.abs(m.z[0]-2*q));
            }
        }
        return {error,steps:s.steps.length,active:s.active};
    }""")
    assert check['error'] < 1e-12 and check['steps'] == 21 and check['active'] == 10, check
    host.locator('button').click()
    assert iframe.count() == 0
    for i, identifier in enumerate(('am2_29_oscillations.html', 'am2_29_cantor.html'),1):
        host = hosts.nth(i)
        host.locator('button').click()
        iframe = host.locator('iframe')
        assert iframe.get_attribute('sandbox') == 'allow-scripts'
        assert iframe.get_attribute('src').endswith(identifier)
        plot = host.frame_locator('iframe').locator('#plot[data-ready=true]')
        plot.wait_for(timeout=60000)
        if i == 1:
            check = plot.evaluate("""el => {
                let error=0;
                for(let j=0;j<12;j++){
                    const d=el.data[3*j], a=(j+1)/4;
                    d.x.forEach((x,k)=>error=Math.max(error,Math.abs(d.y[k]-x**a*Math.sin(1/x))));
                }
                return {error,steps:el.layout.sliders[0].steps.length};
            }""")
            assert check['error'] < 1e-12 and check['steps'] == 12, check
        else:
            check = plot.evaluate("""el => {
                let error=0;
                for(let n=0;n<9;n++){
                    const d=el.data[2*n+1];
                    let mass=0,support=0;
                    for(let k=0;k<d.x.length;k+=3){
                        const w=d.x[k+1]-d.x[k];
                        mass+=w*d.y[k];
                        if(d.y[k]>0)support+=w;
                    }
                    error=Math.max(error,Math.abs(mass-1),Math.abs(support-(2/3)**n));
                }
                return {error,steps:el.layout.sliders[0].steps.length};
            }""")
            assert check['error'] < 1e-12 and check['steps'] == 9, check
        host.locator('button').click()
        assert iframe.count() == 0
    # AM II 30: exact section areas and local nonlinear area ratios.
    source = (ROOT.parent / 'chapters/pl/mathematical_analysis_ii/30-calki-wielokrotne-i-zamiana-zmiennych.tex').read_text(encoding='utf-8')
    page.evaluate("latex => renderSimplified(latex, 'AM2-30')", source)
    hosts = box.locator('.atlas-plot-host')
    assert hosts.count() == 2
    for i, identifier in enumerate(('am2_30_sections.html', 'am2_30_jacobian.html')):
        host = hosts.nth(i)
        host.locator('button').click()
        iframe = host.locator('iframe')
        assert iframe.get_attribute('sandbox') == 'allow-scripts'
        assert iframe.get_attribute('src').endswith(identifier)
        plot = host.frame_locator('iframe').locator('#plot[data-ready=true]')
        plot.wait_for(timeout=60000)
        if i == 0:
            check = plot.evaluate("""el => {
                let error=0;
                for(let j=0;j<42;j++){
                    const d=el.data[j+2],t=(j%21)/20;
                    const area=(d.z[2]+d.z[3])/2;
                    error=Math.max(error,Math.abs(area-(j<21?1+t:.5+2*t)));
                }
                return {error,steps:el.layout.sliders[0].steps.length};
            }""")
            assert check['error'] < 1e-12 and check['steps'] == 42, check
        else:
            check = plot.evaluate("""el => {
                let error=0;
                const area=d=>Math.abs(d.x.slice(0,-1).reduce((s,x,k)=>s+x*d.y[k+1]-d.x[k+1]*d.y[k],0))/2;
                for(let j=0;j<21;j++){
                    const a=el.data[38+2*j],b=el.data[39+2*j];
                    const u=(a.x[0]+a.x[1])/2;
                    error=Math.max(error,Math.abs(area(b)/area(a)-u));
                }
                return {error,steps:el.layout.sliders[0].steps.length};
            }""")
            assert check['error'] < 1e-10 and check['steps'] == 21, check
        host.locator('button').click()
        assert iframe.count() == 0
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
