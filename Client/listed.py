import requests
from getpass import getpass

auth_endpoint = "http://127.0.0.1:8000/api/auth/"
username = input("Username: ")
password = getpass()
data = {
    'username': username,
    'password': password
}
res = requests.post(auth_endpoint, json=data)
print(res.status_code)
if res.status_code == 200:
    token = res.json()['token']
    headers = {
        'Authorization': f"Bearer {token}"
    }

endpoint = "http://127.0.0.1:8000/api/products/"
res = requests.get(endpoint, headers=headers)
print(res.status_code)
products = res.json()
print(products)
for product in products:
    print(product)
