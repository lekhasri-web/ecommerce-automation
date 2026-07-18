from jsonschema import validate
import requests




response_schema_products = {
       "type" : "object",
       "required" : ["responseCode","products"],
       "properties" : {
        "responseCode" : {"type" : "integer"},
        "products" : {"type" : "array"}
       }
}
product_schema_product_list = {
       "type" : "object",
       "required" : ["id","name","price","brand","category"],
       "properties" : {
          "id" : {"type" : "integer"},
          "name" : {"type" : "string"},
          "price" : {"type" : "string"},
          "brand" : {"type" : "string"},
          "category" : {"type" : "object"}
        }
}
# {"responseCode": 200, "brands": [{"id": 1, "brand": "Polo"}

response_schema_brands = {
    "type" : "object",
    "required" : ["responseCode","brands"],
    "properties" : {
        "responseCode" : {"type" : "integer"},
        "brands" : {"type" : "array"}
    }
}
brand_schema = {
    "type" : "object",
    "required" : ["id","brand"],
    "properties" : {
        "id" : {"type" : "integer"},
        "brand" : {"type" : "string"}
    }
}

def test_product_schema_response(product_response):
    validate(instance=product_response.json(),schema=response_schema_products)

def test_product_item(product_response):
    products = product_response.json()["products"]
    for product in products:
        validate(instance=product,schema=product_schema_product_list)

def test_brand_response(brand_response):
    validate(instance=brand_response.json(),schema=response_schema_brands)

def test_each_brand(brand_response):
    brands = brand_response.json()["brands"]
    for brand in brands:
        validate(instance=brand,schema=brand_schema)


