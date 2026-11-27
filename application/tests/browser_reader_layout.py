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
    for width, height in ((1934, 877), (1547, 702), (967, 439), (390, 844), (390, 350)):
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
        assert pinned['bottom'] < pinned['viewBottom'], pinned
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
    page.keyboard.press('Escape')
    page.wait_for_function("!document.documentElement.classList.contains('reading-mode')")
    assert_viewport_layout(page)
    page.locator('#textSizeReset').click()

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
    assert 'Materiał stanowi adaptację' in box.inner_text()
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
