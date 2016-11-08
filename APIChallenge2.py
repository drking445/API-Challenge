
import json
import requests


payload = {'token' : "802ba928cd3ce9acd90595df2853ee2b"}
r = requests.post('http://challenge.code2040.org/api/reverse', json=payload)

response = r.text

pay = {'token' : "802ba928cd3ce9acd90595df2853ee2b", 'string' : response[::-1]}
r = requests.post('http://challenge.code2040.org/api/reverse/validate', json=pay)



