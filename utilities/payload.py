import random
import string
from utilities.configuration import *

def addbook(isbn, aisle):
    book = {
        "name": "Learn Appium Automation with python",
        "isbn": isbn,
        "aisle": aisle,
        "author": "John foe"
    }

    return book

def buildpayloadfromDB(query):
    addbody = {}
    row = get_query(query)
    print("****", row)
    addbody['name'] = row[0]
    addbody['isbn'] = row[1]
    addbody['aisle'] = row[2]
    addbody['author'] = row[3]
    print(addbody)
    return addbody


def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters, k=length))
