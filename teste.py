import requests

x = requests.get('http://localhost/howare')
rec = x.json()
print(rec[0]['status'])
