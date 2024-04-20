import json

courses = '{"name": "RahulShetty","languages": [ "Java", "Python"]}'
# Loads method parse json string and it returns dictionary
dict = json.loads(courses)
print(dict)
print(dict["languages"])
print(dict["languages"][0])
# ************** Open json file from sys location and read ***************************
with open(".\\data_file\\sample.json") as fp:
    data1 = json.load(fp)
    print(data1)
    print(data1["course_1"]["title"])

# ******* Compare two json *************
with open(".\\data_file\\sample_1.json") as fp:
    data2 = json.load(fp)
    print(data1 == data2)
    assert data1 == data2
