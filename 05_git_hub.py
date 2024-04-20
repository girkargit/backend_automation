import requests

se = requests.session() # Create session with userid and password for once
se.auth = auth=("girkargit", "Gspl$#dc3")

url = "https://api.github.com/users"
# github_res = se.get(url, verify=False, auth=("girkargit", "Gspl$#dc3")) # Instead of this create session once time
github_res = se.get(url, verify=False,)
print(github_res.status_code)

url_2 = "https://api.github.com/users/repos"
github_res = se.get(url_2, verify=False,)
print(github_res.status_code)