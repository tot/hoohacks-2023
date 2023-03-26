import create_transactions
from dotenv import load_dotenv
import requests
import os
import json, random, time

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


for customer in get_customers():
    customer_id = customer['_id']
    for i in range(10):
        time.sleep(2)
        for account in get_accounts(customer_id):
            time.sleep(2)
            account_id = account['_id']
            #Create Transactions
            create_transactions.createDummyTransaction(api_key, account_id)
