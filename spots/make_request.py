import requests  
import json
url = "http://127.0.0.1:8000/upload/"
data = {'results':[{'name':'val1', 'color':'color'}, {'name':'val1', 'color':'color'}]}
headers = {'content-type': 'application/json'}
r=requests.post(url, data=json.dumps(data), headers=headers)
print r.text