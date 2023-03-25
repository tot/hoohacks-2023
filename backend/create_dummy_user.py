import requests
import json

apiKey = '?key=9653f9fc38d2de3202bd566e6369bda3'

url = 'http://api.nessieisreal.com/customers{}'.format(apiKey)
payload = {
  "first_name": "John",
  "last_name": "Doe",
  "address": {
    "street_number": "100",
    "street_name": "University Avenue",
    "city": "Charlottesville",
    "state": "VA",
    "zip": "22901"
  }
}

# Create a Savings Account
response = requests.post( 
	url, 
	data=json.dumps(payload),
	headers={'Content-Type': 'application/json', 'Accept': 'application/json'},
)

print(response)