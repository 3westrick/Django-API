import requests

endpoint = "http://127.0.0.1:8000/api/products/10/delete/"

res = requests.delete(endpoint)
print(res.status_code)
# print(res.json())
# delete method doesnt return json response, just 204 result code
