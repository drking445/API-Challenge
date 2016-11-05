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
print(str(x4))
print(r)


In [1]: import subprocess

In [2]: print subprocess.check_output('git init', shell=True)

Initialized empty Git repository in /home/parelio/test/.git/

In [3]: print subprocess.check_output('git add .', shell=True)

In [4]: print subprocess.check_output('git commit -m "a commit"', shell=True)

[master (root-commit) 16b6499] Initial commit
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 README.md

