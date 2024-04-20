import requests
import json

response = requests.get("http://216.10.245.166//Library/GetBook.php",
                        params={'AuthorName': 'Rahul Shetty'}, )

# print(response.text) # output in string formta
# print(type(response.text))
# dict = json.loads(response.text) #
# print(dict[0]['isbn'])

json_res = response.json()  # above code short cut
print(type(json_res))
print(json_res[0]['isbn'])
print(response.status_code)
assert response.status_code == 200
hed = response.headers
assert hed['Content-Type'] == 'application/json;charset=UTF-8'
expect_book = {'book_name': 'Learning Rest API with QA academy', 'isbn': 'BNO121192', 'aisle': '227'}

for res in json_res:
    if res['isbn'] == "BNO121192":
        print(res)
        actual = res
        break   
assert res == expect_book
