import requests
import json

status = 'available'

headers = {'accept': 'application/json'}
res = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}", headers=headers)

print(res.status_code)
print(res.json())


res1 = requests.post(f"https://petstore.swagger.io/v2/pet/12354637272829")
headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
data = {
    "id": 0,
    "category": {
       "id": 0,
       "name": "string"
    },
    "name": "doggie",
    "photoUrls": [
      "string"
    ],
    "tags": [
     {
      "id": 0,
      "name": "string"
     }
    ],
    "status": "available"
}

print(res1.status_code)
print(res1.json())


res2 = requests.put(f"https://petstore.swagger.io/v2/pet/12354637272829")
headers2 = {'accept': 'application/json', 'Content-Type': 'application/json'}
data2 = {
    "id": 0,
    "category": {
       "id": 0,
       "name": "string"
    },
    "name": "Pomchik",
    "photoUrls": [
      "string"
    ],
    "tags": [
     {
      "id": 0,
      "name": "string"
     }
    ],
    "status": "available"
}

print(res2.status_code)
print(res2.text)

res3 = requests.delete(f'https://petstore.swagger.io/v2/pet/12354637272829')
headers3 = {'accept': 'application/json'}

print(res3.status_code)
print(res3.text)


