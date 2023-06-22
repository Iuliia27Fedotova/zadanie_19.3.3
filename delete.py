import requests

petId = 9223372036854744271
res = requests.delete(f"https://petstore.swagger.io/v2/pet/{petId}")

print(res.status_code)
print(res.json())
