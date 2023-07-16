import requests

endpoint = "http://127.0.0.1:8000/api/products/3/"

res = requests.get(endpoint)
print(res.status_code)

print(res.json())

