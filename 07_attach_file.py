import requests

url = "https://petstore.swagger.io/v2/pet/9843217/uploadImage"
file = {'file': open("C:\\Users\\abhil\\Downloads\\dog.jpg", "rb")}
response = requests.post(url, files=file)
print(response.status_code)
print(response.text)
