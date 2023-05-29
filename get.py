import requests

url = "https://petstore.swagger.io/v2/user/9223372036854745000"

response = requests.get(url, "accept: application/json")
print(response.text)