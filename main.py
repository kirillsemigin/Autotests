import requests
url = "https://petstore.swagger.io/v2/user"
body = {
  "id": 0,
  "username": "Саша",
  "firstName": "Саша",
  "lastName": "Семигин",
  "email": "alex@mail.ru",
  "password": "123456",
  "phone": "89152344358",
  "userStatus": 0
}

response = requests.post(url, json=body )
print(response.text)