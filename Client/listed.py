import requests

endpoint = "http://127.0.0.1:8000/api/products/"

res = requests.get(endpoint)
print(res.status_code)
products = res.json()
for product in products:
    print(product)
