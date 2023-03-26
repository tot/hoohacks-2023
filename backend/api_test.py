import requests
import json 

headers = {"Content-Type": "application/json"}
body = {"customer_id": "641fac5778f6910a15f0e4df"}
response = requests.get("http://127.0.0.1:5000/api/subscriptions", headers=headers, data=json.dumps(body))
print(response)
print(response.json())