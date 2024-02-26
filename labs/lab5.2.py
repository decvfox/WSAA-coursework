import requests
import json
from config import config as cfg

filename = 'repos_private.json'

url = 'https://api.github.com/repos/decvfox/aprivateone'

apiKey = cfg["githubkey"]

response = requests.get(url, auth=('token',apiKey), verify=False)
print (response.status_code)
repoJSON = response.json()
#print (response.json())

with open(filename, 'w') as fp:
    json.dump(repoJSON, fp, indent=4)
