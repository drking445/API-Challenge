##Code2040 Challenge 1

import json
import requests


pay = {'token' : "802ba928cd3ce9acd90595df2853ee2b", 'github' : 'https://github.com/drking445/API-Challenge'}
r = requests.post('http://challenge.code2040.org/api/register', params=pay)
print(r)
