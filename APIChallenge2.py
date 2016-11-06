
import requests
import json
pay = {'token' : "802ba928cd3ce9acd90595df2853ee2b"}
r = requests.post('http://challenge.code2040.org/api/reverse', params=pay)
response = r.json()
string = response['string']
pay = {'token' : "802ba928cd3ce9acd90595df2853ee2b", 'string' : string[::-1]}
r = requests.post('http://challenge.code2040.org/api/reverse/validate', params=pay)

