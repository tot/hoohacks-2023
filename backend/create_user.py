from dotenv import load_dotenv
import os, requests, json
import create_transactions 


load_dotenv()
api_key = os.getenv("API_KEY")


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


url = 'http://api.nessieisreal.com/data?type=customers?key={}'.format(api_key)
response = requests.delete( 
	url, 
	headers={ 'Accept': 'application/json'},
)
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
print(response.content)

for customer in get_customers():
    customer_id = customer['_id']


    #Create Accounts
    url = 'http://api.nessieisreal.com/customers/' + customer_id + '/accounts?key={}'.format(api_key)

    payload = {
    "type": "Credit Card",
    "nickname": "string",
    "rewards": 0,
    "balance": 0,
    }


    #Create Credit Card Account
    response = requests.post(url,data=json.dumps(payload), 
        headers={'Content-Type': 'application/json', 'Accept': 'application/json'} )

    print (response.content)

    payload = {
    "type": "Checking",
    "nickname": "string",
    "rewards": 0,
    "balance": 0,
    }

    #Create Other Accounts
    response = requests.post(url,data=json.dumps(payload), 
        headers={'Content-Type': 'application/json', 'Accept': 'application/json'} )

    print (response.content)


    for i in range(50):
        for account in get_accounts(customer_id):
            print(account)
            account_id = account['_id']
            
            #Create Transactions
            print(create_transactions.createDummyTransaction(api_key, account_id).content)



