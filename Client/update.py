import requests

endpoint = "http://127.0.0.1:8000/api/products/8/update/"
data = {
    "title": 'Super-man 1',
    "price": 5.99,
}
res = requests.put(endpoint, json=data)
print(res.status_code)
print(res.json())
