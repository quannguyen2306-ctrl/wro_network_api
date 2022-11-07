import requests
import json

data = json.loads(requests.get("http://127.0.0.1:8000/").text)
print(data["message"])