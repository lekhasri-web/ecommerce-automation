import pytest
from playwright.sync_api import sync_playwright
import os
from utils.logger import get_logger

logger = get_logger(__name__)

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        # 1. Launch a visible browser\
        headless = os.getenv("CI","false") == "true"
        browser = p.chromium.launch()
        logger.info("browser launched")
        #create a human disguised browser context
        context = browser.new_context()
        page = context.new_page()
        logger.info("new page is launched")

        yield page

        context.close()
        browser.close()
        logger.info("browser is closed")

@pytest.hookimpl(tryfirst=True,hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            page.screenshot(path=f"screenshots/{item.name}.png")
            logger.error(f"Test failed: {item.name} - screenshot captured")
    
