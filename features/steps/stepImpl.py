from behave import *
import requests
from utilities.configuration import *
from utilities.resourse import ApiResourses
from utilities.payload import *


@Given('the book details which needs to be added to library')
def step_impl(context):
    resourse = ApiResourses()
    context.hed = {"Content-Type": "application/json"}
    context.add_url = getconfig()['API']['endpoint'] + resourse.addBook
    context.payload = addbook("sqaw", "4013")


@When('we execute the AddBook PostAPI methode')
def step_impl(context):
    context.response = requests.post(context.add_url, json=context.payload, headers=context.hed, )
    print("||||||||||", context.response)


@Then('book is successfully added')
def step_impl(context):
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", context.response.json())
    context.add = context.response.json()
    context.bookID = context.add["ID"]
    print("#####-----", context.bookID)
    print(context.add)
    assert context.add['Msg'] == "successfully added"


@Given("the book details with {isbn} and {aisle}")
def step_impl(context, isbn, aisle):
    print("--------", isbn, aisle)
    resourse = ApiResourses()
    context.hed = {"Content-Type": "application/json"}
    context.add_url = getconfig()['API']['endpoint'] + resourse.addBook
    context.payload = addbook(isbn, aisle)


@given('I have github auth credential')
def step_impl(context):
    context.se = requests.session()  # Create session with userid and password for once
    context.se.auth = auth = ("girkargit", "Gspl$#dc3")


@when('I hit getrepo API of github')
def step_impl(context):
    resourse = ApiResourses()
    url = resourse.github
    context.response = context.se.get(url, verify=False, )


@then('status code of response should be {statusCode:d}')
def step_impl(context, statusCode):
    print("----**-----", context.response.status_code)
    assert context.response.status_code == statusCode

# behave --no-capture -f allure_behave.formatter:AllureFormatter -o allure_reports