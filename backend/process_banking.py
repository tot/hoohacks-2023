from dotenv import load_dotenv
import os, requests, json

load_dotenv()
api_key = os.getenv("API_KEY")

def get_customers():
    return json.loads(requests.get( 
	'http://api.nessieisreal.com/customers?key={}'.format(api_key),
	headers={'Accept': 'application/json'},
    )._content)

def get_accounts(customer_id):
    return json.loads(requests.get( 
	'http://api.nessieisreal.com/customers/{}/accounts?key={}'.format(customer_id, api_key),
	headers={'Accept': 'application/json'},
    )._content)

def get_transactions(account_id):
    return json.loads(requests.get( 
	'http://api.nessieisreal.com/accounts/{}/purchases?key={}'.format(account_id, api_key),
	headers={'Accept': 'application/json'},

def process_statistics(transactions):
    pass
    
def log_transactions(transactions):
    pass

def process_customer_data(customer_id):
    for account in get_accounts(customer_id):
        transactions = get_transactions(account_id)
        process_statistics(transactions)
        log_transactions(transactions)