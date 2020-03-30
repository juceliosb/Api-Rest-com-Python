import json, requests
url = "http://site_a ser_trabalhado"
playload = {'modelo': 'Bross', 'marca': 'Honda', 'placa': 'LVF-6689'}
headers = {'content-type': 'application/json'}
r = requests.post(url, data=json.dumps(playload), headers=headers)
print (r.status_code)
print(r.text)
