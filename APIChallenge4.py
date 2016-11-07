##Code2040 Challenge 4

import json
import requests


def call():
    pay = {'token' : "802ba928cd3ce9acd90595df2853ee2b"}
   
    r = requests.post('http://challenge.code2040.org/api/prefix', params=pay)
    r.headers['Content-Type: application/json']
    response = r.json()
    prefix = response['prefix']
    array = response['array']
    array2 = []
    for index in range(len(array)):
        
        if not (array[index].startswith(prefix)):
            array2.append(array[index])


 
    pay = {'token' : "802ba928cd3ce9acd90595df2853ee2b"}
    sub = {'array' : array2}
    req = requests.post('http://challenge.code2040.org/api/prefix/validate', json=sub, params=pay)
    
    
    
    
    print(array2)
    print(array)
    print(prefix)

call()
