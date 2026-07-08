import requests
from playwright.sync_api import expect
from config import BASE_URL


def test_first_product_appears_on_ui(page,product_response): 


    product_name = product_response.json()["products"][0]["name"]

    page.goto(f"{BASE_URL}/products")

    expect(page.get_by_text(product_name).first).to_be_visible()

def test_brand_name_visbility(page,brand_response):


    brand_name = brand_response.json()["brands"][0]["brand"]

    page.goto(BASE_URL)

    expect(page.get_by_role("link", name = brand_name)).to_be_visible()


    



