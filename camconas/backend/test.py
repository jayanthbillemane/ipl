import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE+"home")
# response = requests.post(BASE+"home")

print(response.json())
