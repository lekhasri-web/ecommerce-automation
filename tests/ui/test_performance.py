import time
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.logger import get_logger

logger = get_logger(__name__)

def test_homepage_performance(page):
    start_time = time.time()
    homepage = HomePage(page)
    homepage.open_url()
    end_time = time.time()
    duration = end_time - start_time
    assert duration <= 5
    logger.info(f"Homepage loaded in {round(duration,2)}")


def test_loginpage_performance(page):
    start_time = time.time()
    loginpage = LoginPage(page)
    loginpage.navigate()
    end_time = time.time()
    duration = end_time - start_time
    assert duration <= 5
    logger.info(f"loginpage loaded in {round(duration,2)}")


def test_productpage_performance(page):
    start_time = time.time()
    productpage = ProductsPage(page)
    productpage.navigate()
    end_time = time.time()
    duration = end_time - start_time
    assert duration <= 8
    logger.info(f"productpage loaded in {round(duration,2)}")


