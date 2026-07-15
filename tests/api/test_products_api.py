import requests
import pytest
from config import BASE_URL

def test_productlist(product_response):


    assert product_response.status_code == 200
    assert len(product_response.json()["products"]) > 0, "product list is empty"

def test_product_body(product_response):
    

    products = product_response.json()['products']

    for product in products:
        assert "id" in product
        assert "name" in product
        assert "price" in product
        assert "brand" in product
        assert "category" in product
    
def test_brandslist(brand_response):


    assert brand_response.status_code == 200
    assert len(brand_response.json()['brands']) > 0,"This brands list is empty"

def test_brandlist_field(brand_response):
    

    brands = brand_response.json()['brands']

    for brand in brands:
        assert "id" in brand
        assert "brand" in brand

@pytest.mark.xfail(reason="API search matches on category field, not just product name - site behavior")
def test_searchlist():
    
    response = requests.post(f"{BASE_URL}/api/searchProduct",data ={"search_product" : "tops"},timeout=10)

    assert response.status_code == 200
    assert len(response.json()["products"]) > 0,"search list is empty"

    search_product = response.json()["products"] 

    for product in search_product:
        assert "top" in product['name'].lower() , f"Product name '{product['name']}' does not contain the search term 'top'"
    