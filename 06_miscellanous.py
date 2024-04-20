import requests

# http://rahulshettyacademy.com
# visit-month  ----- cookies

cookie = {"visit-month": "February"}
response = requests.get("http://rahulshettyacademy.com",allow_redirects=False, cookies=cookie, timeout=1) # send cookies in request
# print(response.history) # If any redirection is happened then it will print
# allow_redirects=False, if any redirect is happening then it will stop
# timeout=1, it will wait for given seconds if api taken to give response
print(response.status_code)

se = requests.session()
se.cookies.update(cookie) # create seesion and pass common cookie to all request
res = se.get("https://httpbin.org/cookies", cookies={"visit-year": "2023"}) # to check cookies availability
print(res.text)