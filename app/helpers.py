import json
import requests

def GetLatestGithubRelease(repo):
    url = 'https://api.github.com/repos/{0}/releases/latest'.format(repo)
    response = requests.get(url)
    data = json.loads(response.text)

    return data['tag_name']
