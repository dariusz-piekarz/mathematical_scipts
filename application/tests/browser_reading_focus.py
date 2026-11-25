"""Check Explorer hiding and real/full-window reading without rebuilding content."""
import os
from pathlib import Path
from playwright.sync_api import sync_playwright

URL = os.environ.get('MATLIB_TEST_URL', 'http://127.0.0.1:8765')
with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=True)
    page = browser.new_page(viewport={'width': 1360, 'height': 900})
    errors = []
    page.on('pageerror', lambda error: errors.append(str(error)))
    page.goto(URL, wait_until='networkidle')
    page.locator('#openFirst').click()
    page.locator('#simplified').wait_for(state='visible')
    initial_width = page.locator('#view-reader').bounding_box()['width']
    page.locator('#showExplorer').click()
    assert page.locator('#explorer').is_hidden()
    assert page.locator('#showExplorer').get_attribute('aria-expanded') == 'false'
    assert page.locator('#view-reader').bounding_box()['width'] > initial_width + 200
    page.reload(wait_until='networkidle')
    assert page.locator('#explorer').is_hidden(), 'desktop preference must persist'
    page.locator('#showExplorer').click()
    assert page.locator('#explorer').is_visible()
    page.locator('#closeExplorer').click()
    assert page.locator('#explorer').is_hidden()
    page.locator('#openFirst').click()
    page.locator('#simplified').wait_for(state='visible')
    page.evaluate("window.readingNode=document.querySelector('#simplified .katex')")
    page.locator('#readingMode').click()
    page.wait_for_function("document.fullscreenElement !== null")
    assert page.locator('.topbar').is_hidden() and page.locator('.tabs').is_hidden()
    assert page.locator('#readingTheme').is_visible()
    assert page.locator('#textSizeUp').is_visible()
    assert page.locator('#view-reader').bounding_box()['width'] == page.viewport_size['width']
    assert page.evaluate("window.readingNode===document.querySelector('#simplified .katex')")
    page.screenshot(path=str(Path(os.environ['TEMP']) / 'atlas-reading-fullscreen.png'))
    page.keyboard.press('Escape')
    page.wait_for_function("!document.documentElement.classList.contains('reading-mode')")
    assert page.locator('.topbar').is_visible()
    assert page.locator('#explorer').is_hidden(), 'leaving focus must preserve Explorer preference'
    # Full-window reading remains usable if native fullscreen is denied.
    page.evaluate("() => {document.querySelector('.app-shell').requestFullscreen=()=>Promise.reject(new Error('denied'));}")
    page.locator('#readingMode').click()
    assert page.locator('.topbar').is_hidden()
    page.locator('#readingTheme').click()
    assert page.locator('#readingTheme').get_attribute('aria-pressed') == page.locator('#themeToggle').get_attribute('aria-pressed')
    page.locator('#readingMode').click()
    assert page.locator('.topbar').is_visible()
    page.set_viewport_size({'width': 390, 'height': 844})
    page.locator('#showExplorer').click()
    assert page.locator('#showExplorer').get_attribute('aria-expanded') == 'true'
    page.locator('#closeExplorer').click()
    assert page.locator('#showExplorer').get_attribute('aria-expanded') == 'false'
    assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
    assert not errors, errors
    browser.close()
    print('Explorer preference, desktop/mobile toggles, native fullscreen, Escape, fallback and reading controls: OK')
