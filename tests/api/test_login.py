import requests
import pytest
from config import BASE_URL,TEST_PASSWORD,TEST_EMAIL


def test_loginapi_valid_Credentials():

    response = requests.post(f"{BASE_URL}/api/verifyLogin",data={"email": TEST_EMAIL, "password": TEST_PASSWORD},timeout=10)
    assert response.status_code == 200
    body = response.json()
    print(response.status_code)
    assert body["responseCode"] == 200
    print(response.text)
    assert body["message"] == "User exists!"

def test_loginapi_invalid_credentials():

    response = requests.post(f"{BASE_URL}/api/verifyLogin",data={"email": "abc@gmail.com", "password" : "2134"},timeout=10)
    assert response.status_code == 200
    body = response.json()
    assert body["responseCode"] == 404
    assert body["message"] == "User not found!"

def test_loginapi_blank_credentials():

    response = requests.post(f"{BASE_URL}/api/verifyLogin",data={"email": "","password": ""},timeout=10)
    assert response.status_code == 200
    body = response.json()
    assert body["responseCode"] == 404
    assert body["message"] == "User not found!"

def test_loginapi_wrong_method():
    
    response = requests.get(f"{BASE_URL}/api/verifyLogin",timeout=10)
    assert response.status_code == 200
    body = response.json()
    assert body["responseCode"] == 405
    assert body["message"] == "This request method is not supported."