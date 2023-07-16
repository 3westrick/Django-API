import requests

endpoint = "http://127.0.0.1:8000/api/"
endpoint = "http://127.0.0.1:8000/api/product/"

res = requests.post(endpoint, json={'title': "hell"})
print(res.status_code)
print(res.text)
print(res.json())


res = requests.post(endpoint, json={'des': "hell", 'title': None, 'price': '1q'})
print(res.status_code)
print(res.text)
print(res.json())
