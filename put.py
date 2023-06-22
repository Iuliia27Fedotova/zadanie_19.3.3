import requests

data = {'id': 0,
        'category': {'id': 0, 'name': 'Русская голубая'},
        'name': 'Буся',
        'photoUrls': ['string'],
        'tags': [{'id': 0, 'name': 'string'}],
        'status': 'available'}

headers = {'accept': 'application/json',
           'Content-Type': 'application/json'}

res = requests.put ('https://petstore.swagger.io/v2/pet', headers=headers, json=data)


print(res.status_code)
print(res.json())