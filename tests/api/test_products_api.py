import requests
import pytest

def test_productlist():

    response = requests.get("https://automationexercise.com/api/productsList")

    assert response.status_code == 200
    assert len(response.json()["products"]) > 0, "Product list is empty"

def test_product_body():
    
    response = requests.get("https://automationexercise.com/api/productsList")

    products = response.json()['products']

    for product in products:
        assert "id" in product
        assert "name" in product
        assert "price" in product
        assert "brand" in product
        assert "category" in product
    
def test_brandslist():

    response = requests.get("https://automationexercise.com/api/brandsList")

    assert response.status_code == 200
    assert len(response.json()['brands']) > 0,"This brands list is empty"

def test_brandlist_field():
    
    response = requests.get("https://automationexercise.com/api/brandsList")

    brands = response.json()['brands']

    for brand in brands:
        assert "id" in brand
        assert "brand" in brand

@pytest.mark.xfail(Reason="API search matches on category field, not just product name - site behavior")
def test_searchlist():
    
    response = requests.post("https://automationexercise.com/api/searchProduct",data ={"search_product" : "tops"})

    assert response.status_code == 200
    assert len(response.json()["products"]) > 0,"search list is empty"

    search_product = response.json()["products"] 

    for product in search_product:
        assert "top" in product['name'].lower() , f"Product name '{product['name']}' does not contain the search term 'top'"
    