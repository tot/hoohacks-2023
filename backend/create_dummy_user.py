from dotenv import load_dotenv
import os, requests, json

load_dotenv()
api_key = os.getenv("API_KEY")

url = 'http://api.nessieisreal.com/customers?key={}'.format(api_key)
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