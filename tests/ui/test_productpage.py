from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from config import TEST_EMAIL,TEST_PASSWORD
import pytest
from utils.helpers import wait_for_element_page,get_element_text,scroll_to_element

@pytest.mark.regression
def test_withproductpagetitle(page):
    loginpage = LoginPage(page)
    loginpage.navigate()
    loginpage.enter_credentials(TEST_EMAIL,TEST_PASSWORD)
    text = get_element_text(page, ".title.text-center",0)
    assert "features items" in text.lower()

@pytest.mark.regression
def test_withproducts(page):
    loginpage = LoginPage(page)
    loginpage.navigate()
    loginpage.enter_credentials(TEST_EMAIL,TEST_PASSWORD)
    products = wait_for_element_page(page, ".single-products",0)
    expect(products.first).to_be_visible()
    assert products.count() > 0

@pytest.mark.smoke
def test_withoutlogin(page):
    productpage = ProductsPage(page)
    productpage.navigate()
    expect(page.get_by_role("heading",name="All Products")).to_have_text("All Products")
    products = scroll_to_element(page, ".single-products",0)
    expect(products.first).to_be_visible()
    assert products.count() > 0
    


