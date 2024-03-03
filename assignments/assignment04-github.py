# assignment04-github.py
# Read a file from a repository, then replace all the instances of the text "Andrew" with your name. 
# The program should then commit those changes and push the file back to the repository
# Author: Declan Fox

from github import Github
from config import config as cfg
import requests

# get API key from config file
apikey = cfg["githubkey"]
g = Github(apikey)

# get repository
repo = g.get_repo("decvfox/aprivateone")
#print(repo.clone_url)

# Get the url for test.txt
fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
#print (urlOfFile)

# read the file
response = requests.get(urlOfFile)
contentOfFile = response.text
#print (contentOfFile)

# replace Andrew with Declan
newContents = contentOfFile.replace('Andrew', 'Declan')
#print (newContents)

# push the mpdified content back up to test.txt
gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",newContents,fileInfo.sha)
#print (gitHubResponse)
