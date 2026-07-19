import pytest
from playwright.sync_api import sync_playwright
import os
from utils.logger import get_logger

logger = get_logger(__name__)

def pytest_addoption(parser):
    parser.addoption(
        "--browser-name",
        action="store",
        default="chromium",
        help="Browser engine to run tests against: chromium, firefox, or webkit",
    )

@pytest.fixture(scope="function")
def page(request):
    browser_name = request.config.getoption("--browser-name")
    with sync_playwright() as p:
        headless = os.getenv("CI","false") == "true"
        browser_type = getattr(p, browser_name)
        browser = browser_type.launch(headless=headless)
        logger.info(f"{browser_name} browser launched")
        #create a human disguised browser context
        context = browser.new_context(
        viewport={"width": 1280, "height": 720},
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = context.new_page()
        logger.info("new page is launched")

        yield page

        context.close()
        browser.close()
        logger.info("browser is closed")

@pytest.hookimpl(tryfirst=True,hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            try:
                page.screenshot(path=f"screenshots/{item.name}.png", timeout=5000)
            except Exception as e:
                logger.warning(f"Could not capture screenshot for {item.name}: {e}")