import requests
from playwright.sync_api import expect


def test_first_product_appears_on_ui(page): 

    response = requests.get("https://automationexercise.com/api/productsList")

    product_name = response.json()["products"][0]["name"]

    page.goto("https://automationexercise.com/products")

    expect(page.get_by_text(product_name).first).to_be_visible()

def test_brand_name_visbility(page):

    response = requests.get("https://automationexercise.com/api/brandsList")

    brand_name = response.json()["brands"][0]["brand"]

    page.goto("https://automationexercise.com/")

    expect(page.get_by_role("link", name = brand_name)).to_be_visible()


    



