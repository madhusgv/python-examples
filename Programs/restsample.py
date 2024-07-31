import requests
from requests.auth import HTTPBasicAuth

basic = HTTPBasicAuth('user', 'pass')
req = requests.get('https://github.com/madhusgv/CIA/issues', auth=basic)
print(req.content)

req = requests.get('https://github.com/madhusgv/CIA/issues', auth=basic)
print(req)