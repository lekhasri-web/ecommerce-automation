from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from config import TEST_EMAIL,TEST_PASSWORD

def test_withproductpagetitle(page):
    loginpage = LoginPage(page)
    loginpage.navigate()
    loginpage.enter_credentials(TEST_EMAIL,TEST_PASSWORD)
    expect(page.get_by_role('heading',name="Features Items")).to_have_text("Features Items")

def test_withproducts(page):
    loginpage = LoginPage(page)
    loginpage.navigate()
    loginpage.enter_credentials(TEST_EMAIL,TEST_PASSWORD)
    products = page.locator(".single-products")
    expect(products.first).to_be_visible()
    assert products.count() > 0

def test_withoutlogin(page):
    productpage = ProductsPage(page)
    productpage.navigate()
    expect(page.get_by_role("heading",name="All Products")).to_have_text("All Products")
    products = page.locator(".single-products")
    expect(products.first).to_be_visible()
    assert products.count() > 0
    


