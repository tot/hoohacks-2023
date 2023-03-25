from dotenv import load_dotenv
from datetime import datetime
import os, requests, json

load_dotenv()
api_key = os.getenv('API_KEY')

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
    )._content)

def get_merchant_category(merchant_id):
    return json.loads(requests.get( 
	'http://api.nessieisreal.com/merchants/{}?key={}'.format(merchant_id, api_key),
	headers={'Accept': 'application/json'},
    )._content)['category']

def process_statistics(user, last_accessed, account, transactions):
    current_account = json.loads(user[account['type']])
    categories = json.loads(user['categories'])
    current_account['last_balance'] = current_account['current_balance']
    current_account['current_balance'] = account['balance']
    for transaction in transactions:
        category = get_merchant_category(transaction['merchant_id'])
        categories[category] = categories.get(category, 0) + 1
        current_account['num_purchases'] = current_account.get('num_purchases', 0) + 1
        current_account['total_spent'] = current_account.get('total_spent', 0) + transaction['amount']
        db['users'].update_one(user, {' $set': {'categories': categories} })
        db['users'].update_one(user, {' $set': {account['type']: current_account}})

def log_transactions(transactions):
    for transaction in transactions:
        t_id, m_id, b_id = transaction['_id'], transaction['merchant_id'], transaction['payer_id']
        date, amt, descr = transaction['purchase_date'], transaction['amount'], transaction['description']
        db['txns'].insert_one({'id': t_id, 'merchant_id': m_id, 'buyer_id': b_id, 'purchase_date': date, 'amount': amt, 'description': descr})

def process_customer_data(customer_id):
    user = db['users'].query({'id': customer_id})
    for account in get_accounts(customer_id):
        transactions = get_transactions(account['_id'])
        process_statistics(user, last_accessed, account, transactions)
        log_transactions(transactions)