"""Check default preview and accessible, persistent reading controls in Chromium."""
import os
from pathlib import Path
from playwright.sync_api import sync_playwright

URL = os.environ.get('MATLIB_TEST_URL', 'http://127.0.0.1:8765')
with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=True)
    page = browser.new_page(viewport={'width': 1360, 'height': 900}, color_scheme='light')
    errors = []
    page.on('pageerror', lambda error: errors.append(str(error)))
    page.goto(URL, wait_until='networkidle')
    page.locator('#openFirst').click()
    page.locator('#docTitle').wait_for(state='visible')
    assert page.locator('#simplified').is_visible()
    assert page.locator('#latexSource').is_hidden()
    assert page.locator('.fragment-toolbar').is_hidden()
    assert page.locator('#togglePreview').inner_text() == 'Pokaż źródło LaTeX'
    original = page.locator('#simplified').evaluate('el => parseFloat(getComputedStyle(el).fontSize)')
    page.evaluate("window.firstFormula = document.querySelector('#simplified .katex')")
    for _ in range(4):
        page.locator('#textSizeUp').click()
    enlarged = page.locator('#simplified').evaluate('el => parseFloat(getComputedStyle(el).fontSize)')
    assert abs(enlarged / original - 1.4) < .01
    assert page.locator('#textSizeReset').inner_text() == '140%'
    assert page.evaluate("window.firstFormula === document.querySelector('#simplified .katex')")
    page.locator('#togglePreview').click()
    assert page.locator('#latexSource').is_visible()
    assert page.locator('.fragment-toolbar').is_visible()
    assert page.locator('#simplified').is_hidden()
    source_size = page.locator('#latexSource').evaluate('el => parseFloat(getComputedStyle(el).fontSize)')
    assert abs(source_size - 16.8) < .1
    page.reload(wait_until='networkidle')
    assert page.locator('#textSizeReset').inner_text() == '140%'
    page.locator('#openFirst').click()
    page.locator('#simplified').wait_for(state='visible')
    assert page.locator('#simplified').is_visible(), 'a new session must default to preview'
    page.locator('#textSizeDown').click()
    assert page.locator('#textSizeReset').inner_text() == '130%'
    page.locator('#textSizeReset').click()
    assert page.locator('#textSizeReset').inner_text() == '100%'
    # Both limits are reachable, with the appropriate button disabled.
    for _ in range(8):
        page.locator('#textSizeUp').click()
    assert page.locator('#textSizeUp').is_disabled()
    page.locator('#textSizeReset').click()
    for _ in range(2):
        page.locator('#textSizeDown').click()
    assert page.locator('#textSizeDown').is_disabled()
    page.locator('#textSizeReset').click()
    for width in (320, 390, 780, 1360):
        page.set_viewport_size({'width': width, 'height': 900})
        switch = page.locator('#themeToggle').bounding_box()
        assert switch and switch['x'] >= 0 and switch['x'] + switch['width'] <= width, (width, switch)
        assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'), width
    page.set_viewport_size({'width': 390, 'height': 844})
    page.locator('#themeToggle').click()
    assert page.locator('html').get_attribute('data-theme') == 'dark'
    page.mouse.move(200, 200)
    page.wait_for_function("getComputedStyle(document.getElementById('themeToggle')).backgroundColor === 'rgb(32, 47, 65)'")
    page.wait_for_function("document.getElementById('explorer').getBoundingClientRect().right <= 0")
    page.screenshot(path=str(Path(os.environ['TEMP']) / 'atlas-reading-controls-mobile.png'))
    page.reload(wait_until='networkidle')
    assert page.locator('html').get_attribute('data-theme') == 'dark'
    assert page.locator('#themeToggle').is_visible()
    assert not errors, errors
    browser.close()
    print('Default preview, optional source, text scaling, limits, reset, persistence and visible mobile theme switch: OK')
