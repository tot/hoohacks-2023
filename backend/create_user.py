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

for customer in get_customers():
    customer_id = customer['_id']
    print(customer_id)


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
    "type": "Banking Card",
    "nickname": "string",
    "rewards": 0,
    "balance": 0,
    }

    #Create Other Accounts
    response = requests.post(url,data=json.dumps(payload), 
        headers={'Content-Type': 'application/json', 'Accept': 'application/json'} )

    print (response.content)


    #Create Transactions
    print(create_transactions.createDummyTransaction(api_key, customer_id).content)



