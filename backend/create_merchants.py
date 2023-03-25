#Create Merchants

from dotenv import load_dotenv
import os, requests, json
import create_transactions 


load_dotenv()
api_key = os.getenv("API_KEY")

url = 'http://api.nessieisreal.com/merchants?key={}'.format(api_key)

payload = {
  "name": "string",
  "category": "string",
  "address": {
    "street_number": "string",
    "street_name": "string",
    "city": "string",
    "state": "string",
    "zip": "string"
  },
  "geocode": {
    "lat": 0,
    "lng": 0
  }
}

response = requests.post(url,data=json.dumps(payload), 
        headers={'Content-Type': 'application/json', 'Accept': 'application/json'} )

print(response.content)
