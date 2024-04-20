import requests
from utilities.configuration import getconfig
from utilities.resourse import ApiResourses


def after_scenario(context, scenario):
    print("@@@@@===============", scenario.tags)
    if "library" in scenario.tags:
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        resourse = ApiResourses()
        delete_url = getconfig()['API']['endpoint'] + resourse.deleteBook
        hed = {"Content-Type": "application/json"}
        del_book = {"ID": context.bookID}
        response = requests.post(delete_url, json=del_book, headers=hed, )
        op = response.json()
        print("*****-------", op)
        assert "deleted" in op["msg"]
        assert response.status_code == 200
