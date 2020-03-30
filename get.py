import json, requests
r = requests.get("http://site_a ser_trabalhado")
r.json()
print (r.status_code)
print(r.text)
