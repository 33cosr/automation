import json

import requests
import selenium
r = requests.post('https://httpbin.org/post', data = {'key':'value'})
print(type(r.json()))
print(json.loads(r.text))