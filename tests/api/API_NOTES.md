## Endpoint: GET /api/productsList
- Method: GET
- Full URL: https://automationexercise.com/api/productsList
- Response code: 200
- Response structure: {"responseCode": 200, "products": [{"id": 1, "name": "Blue Top", "price": "Rs. 500", "brand": "Polo", "category": {"usertype": {"usertype": "Women"}, "category": "Tops"}}

- Each product has: id, name, price, brand, category, inside category usertype as gender, then category
- What I will test: status code is 200, products list is not empty, each product has required fields

## Endpoint: GET /api/brandsList
- Method: GET
- Full URL: https://automationexercise.com/api/brandsList
- Response code: 200
- Response structure: {"responseCode": 200, "brands": [{"id": 1, "brand": "Polo"}
- Each product has: id, brand
- What I will test: status code is 200, brand list is not empty, each brand has required fields


## Endpoint: POST /api/search_product
- Method: POST
- Full URL:  https://automationexercise.com/api/searchProduct
- Response code: 200
- Response structure: {"responseCode": 200, "products": [{"id": 1, "name": "Blue Top", "price": "Rs. 500", "brand": "Polo", "category":
{"usertype": {"usertype": "Women"}, "category": "Tops"}}

- Each product has: id, name, price ,brand,category -> usertype : gender , category
- What I will test: status code is 200, brand list is not empty, each brand has required fields




