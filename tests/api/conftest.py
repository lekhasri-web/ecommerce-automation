from config import BASE_URL
import requests 
import pytest

@pytest.fixture(scope="session")
def product_response():
    response = requests.get(f"{BASE_URL}/api/productsList",timeout=10)
    return response

@pytest.fixture(scope="session")
def brand_response():
    response = requests.get(f"{BASE_URL}/api/brandsList",timeout=10)
    return response
