import requests
from utilities.configuration import *
from utilities.resourse import ApiResourses
from utilities.payload import *

resourse = ApiResourses()
hed = {"Content-Type": "application/json"}
add_url = getconfig()['API']['endpoint'] + resourse.addBook
delete_url = getconfig()['API']['endpoint'] + resourse.deleteBook
query = "select * from Books"
# --------------------------------------------
# Add book API
addbook_req = requests.post(add_url, json=buildpayloadfromDB(query), headers=hed, )  # post request methode
response = addbook_req.json()
print(response, response["ID"])

del_book = {"ID": response["ID"]}
delete_req = requests.post(delete_url, json=del_book, headers=hed, )
op = delete_req.json()
print(op)
assert "deleted" in op["msg"]
assert delete_req.status_code == 200
