import requests

endpoint = "http://127.0.0.1:8000/api/products/6/"
res = requests.get(endpoint)
print(res.status_code)
print(res.json())

endpoint = "http://127.0.0.1:8000/api/products/8/"
res = requests.get(endpoint)
print(res.status_code)
print(res.json())


endpoint = "http://127.0.0.1:8000/api/products/34/"
res = requests.get(endpoint)
print(res.status_code)
print(res.json())
