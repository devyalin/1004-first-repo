import requests
response = requests.get ("https://api.github.com/users/avielb/repos")
print (response.json())
result = response.json()
for repo in result:
    print(repo["name"])