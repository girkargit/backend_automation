import requests

book = {
    "name": "Learn Appium Automation with python",
    "isbn": "bdrwd",
    "aisle": "113",
    "author": "John foe"
}
hed = {"Content-Type": "application/json"}
addbook_req = requests.post("http://216.10.245.166/Library/Addbook.php", json=book,
                            headers=hed, )  # post request methode
print(addbook_req)
response = addbook_req.json()
print(response, response["ID"])
# ------------------------------**********----------------------------------------
# Delete book API
# del_book = {"ID": "a23h345122332"}
del_book = {"ID": response["ID"]}
delete_req = requests.post("http://216.10.245.166/Library/DeleteBook.php", json=del_book, headers=hed, )
op = delete_req.json()
print(op)
assert "deleted" in op["msg"]
assert delete_req.status_code == 200
