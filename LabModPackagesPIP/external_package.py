import requests
#Requesting data from GitHub API
response = requests.get("https://api.github.com")
print(response.json())