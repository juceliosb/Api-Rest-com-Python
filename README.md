# Api-Rest-com-Python

# Api using the get method
# print (r.status_code) - request status returning in HTTP.
import json, requests
r = requests.get("url")
r.json()
print (r.status_code) 
print(r.text)

# Api using the post method 
import json, requests
url = "http://..."
playload = {'nome': 'Jose', 'cidade': 'atlanta'}
headers = {'content-type': 'application/json'}
r = requests.post(url, data=json.dumps(playload), headers=headers)
print (r.status_code)
print(r.text)

# Api using the put method 
import json, requests
url = "http://..."
playload = {'modelo': 'Jucelio', 'marca': 'ta no ponto', 'placa': 'LVF-6689'}
headers = {'content-type': 'application/json'}
r = requests.put(url, data=json.dumps(playload), headers=headers)
print (r.status_code)
print(r.text)

# Api using the delete method 
import json, requests
r = requests.delete("http://...")
print(r.status_code)
print(r.txt)
