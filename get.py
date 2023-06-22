import requests

petId = 9223372036854744271
headers = {'accept': 'application/json'}

res = requests.get(f"https://petstore.swagger.io/v2/pet/{petId}", headers = headers)

print(res.status_code)
print(res.json())

