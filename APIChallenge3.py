import json
import requests


def call():
    pay = {'token' : "802ba928cd3ce9acd90595df2853ee2b"}
    r = requests.post('http://challenge.code2040.org/api/haystack', json=pay)
    response = r.json()
    prefix = response['needle']
    array = response['haystack']
    
    i = array.index(prefix)


 
    pay = {'token' : "802ba928cd3ce9acd90595df2853ee2b", 'needle' : i}
    req = requests.post('http://challenge.code2040.org/api/haystack/validate', json=pay)
    
    
    
   

call()
