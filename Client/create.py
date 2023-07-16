import requests

endpoint = "http://127.0.0.1:8000/api/products/"

data = {
    'title': "Arad",
    'price': 10000000.99,
}

res = requests.post(endpoint, json=data)
print(res.status_code)
print(res.json())
