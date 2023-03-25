from dotenv import load_dotenv
import os, requests, json

load_dotenv()
api_key = os.getenv("API_KEY")

url = 'http://api.nessieisreal.com/customers?key={}'.format(api_key)

response = requests.get( 
	url,
	headers={'Accept': 'application/json'},
)

customers = json.loads(response._content)