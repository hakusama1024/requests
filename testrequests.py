import requests

url = 'http://172.29.236.100:5000/v3/auth/tokens'

payload = { 'auth': { 'identity': { 'methods': ['password'], 'password': { 'user': { 'name': 'admin', 'domain': { 'id': 'Default' }, 'password': '52e213d062b9f9c56faf1d0e02f8b6aee4045836076be2307c1'}}}}}

headers = {'Content-Type' : 'application/json'}

r = requests.post(url, headers=headers, data=payload)

print r

#curl -i -H "Content-Type: application/json" -d '
#{ "auth": {
#    "identity": {
#      "methods": ["password"],
#      "password": {
#        "user": {
#          "name": "admin",
#          "domain": { "id": "Default" },
#          "password": "52e213d062b9f9c56faf1d0e02f8b6aee4045836076be2307c1"
#        }
#      }
#    }
#  }
#} ' http://172.29.236.100:5000/v3/auth/tokens ; echo 
