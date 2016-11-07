##Code2040 Challenge 4

import json
import requests



pay = {'token' : "802ba928cd3ce9acd90595df2853ee2b"}
   
r = requests.post('http://challenge.code2040.org/api/prefix', json=pay)
  
response = r.json()
prefix = response['prefix']
array = response['array']
print(response)
print(prefix)
array2 = []
for index in range(len(array)):
        
    if not (array[index].startswith(prefix)):
        array2.append(array[index])


print(array2) 
requests = {'token' : "802ba928cd3ce9acd90595df2853ee2b", 'array' : array2}

r = requests.post('http://challenge.code2040.org/api/prefix/validate', json=requests)
    
    
    
    
print(array2)
print(array)
print(prefix)


