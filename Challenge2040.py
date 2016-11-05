from datetime import datetime
from datetime import timedelta
import json
import requests


pay = {'token' : "802ba928cd3ce9acd90595df2853ee2b"}
r = requests.post('http://challenge.code2040.org/api/dating', params=pay)
response = r.json()
time = response['datestamp']
interval = response['interval']
print(time)
print(interval)
timeformat = "%Y-%m-%dT%H:%M:%S%fZ"
time2 = datetime.strptime(time, timeformat)
print(time2)
times = time2 + timedelta(seconds = interval+1)
print(times)
x = times.isoformat()

x2 = x
x3 = x2[:len(x)-7]
x4 = x3 + 'Z'
pay = {'token' : "802ba928cd3ce9acd90595df2853ee2b", 'datestamp' : str(x4)}
r = requests.post('http://challenge.code2040.org/api/dating/validate', params=pay)
print(r)


