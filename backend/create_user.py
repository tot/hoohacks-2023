from dotenv import load_dotenv
import os, requests, json, time
import create_transactions,create_merchants
from pymongo import MongoClient



load_dotenv()
api_key = os.getenv("API_KEY")
db_url = os.getenv("DB_URL")
db = MongoClient(db_url).admin
users = db["users"]
accounts = db["accounts"]

#Get List of Customers
def get_customers():
    return json.loads(requests.get( 
    'http://api.nessieisreal.com/customers?key={}'.format(api_key),
    headers={'Accept': 'application/json'},
    )._content)

#Get List of Accounts for customer
def get_accounts(id):
    url = 'http://api.nessieisreal.com/customers/' + id+ '/accounts?key={}'.format(api_key)
    return json.loads(requests.get(url, headers={ 'Accept': 'application/json'}, )._content)


url = "http://api.nessieisreal.com/data?type=Customers&key={}".format(api_key)

payload={}
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

response = requests.delete(url, headers=headers, data=payload)

print(response.content)

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

# Create User
response = requests.post( 
	url, 
	data=json.dumps(payload),
	headers={'Content-Type': 'application/json', 'Accept': 'application/json'},
)
db.users.insert_one(json.loads(response._content)['objectCreated'])
print(response.content)

#Create Merchants

#create_merchants.createMerchants()
for customer in get_customers():
    time.sleep(2)
    customer_id = customer['_id']


    #Create Accounts
    url = 'http://api.nessieisreal.com/customers/' + customer_id + '/accounts?key={}'.format(api_key)

    payload = {
    "type": "Credit Card",
    "nickname": "Credit",
    "rewards": 0,
    "balance": 0,
    }


    #Create Credit Card Account
    response = requests.post(url,data=json.dumps(payload), 
        headers={'Content-Type': 'application/json', 'Accept': 'application/json'} )
    db.accounts.insert_one(json.loads(response._content)['objectCreated'])
    print (response.content)

    payload = {
    "type": "Checking",
    "nickname": "Checking Account",
    "rewards": 0,
    "balance": 0,
    }

    #Create Checking Account
    response = requests.post(url,data=json.dumps(payload), 
        headers={'Content-Type': 'application/json', 'Accept': 'application/json'} )
    db.accounts.insert_one(json.loads(response._content)['objectCreated'])
    print (response.content)


    for i in range(10):
        time.sleep(2)
        for account in get_accounts(customer_id):
            time.sleep(2)
            account_id = account['_id']
            #Create Transactions
            create_transactions.createDummyTransaction(api_key, account_id)



