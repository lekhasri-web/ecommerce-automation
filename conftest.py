import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        # 1. Launch a visible browser
        browser = p.chromium.launch(headless=False)
        #create a human disguised browser context
        context = browser.new_context()
        page = context.new_page()

        yield page

        context.close()
        browser.close()

@pytest.hookimpl(tryfirst=True,hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            page.screenshot(path=f"screenshots/{item.name}.png")
    
