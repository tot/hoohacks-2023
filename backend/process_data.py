from dotenv import load_dotenv
from datetime import datetime
from pymongo import MongoClient
import os, requests, json

load_dotenv()
api_key = os.getenv('API_KEY')
db_url = os.getenv('DB_URL')
db = MongoClient(db_url)['admin']

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

def process_statistics(user, account, transactions):
    categories = user['categories']
    stats = db.accounts.find({'_id': account['_id']}).next()['stats']
    stats['last_balance'] = stats['current_balance']
    stats['current_balance'] = account['balance']
    for transaction in transactions:
        if db.txns.count_documents({'_id': transaction['_id']}, limit = 1):
            category = get_merchant_category(transaction['merchant_id'])
            categories[category] = categories.get(category, 0) + 1
            stats['num_transactions'] += 1
            stats['total_spent'] += transaction['amount']
    
    db.accounts.update_one({'_id': account['_id']}, {'$set':stats})
    db.users.update_one({'_id': user['_id']}, {'$set': {'categories': categories} })

def log_transactions(transactions):
        for transaction in transactions:
            t_id, m_id, b_id = transaction['_id'], transaction['merchant_id'], transaction['payer_id']
            date, amt, descr = transaction['purchase_date'], transaction['amount'], transaction['description']
            db.txns.update_one({'_id': transaction['_id']}, {'$set': {'_id': t_id, 'merchant_id': m_id, 'buyer_id': b_id, 'purchase_date': date, 'amount': amt, 'description': descr}}, upsert = True)

def find_subcriptions():
    pass

def process_customer_data(customer_id):
    user = db.users.find({'_id': customer_id}).next()
    last_accessed = datetime.strptime(user['last_accessed'][1:-1], '%Y-%m-%d %H:%M:%S.%f')
    if datetime.now() or datetime.now() - last_accessed > 86400:
        db.users.update_one({'last_accessed': last_accessed}, {'$set': {'last_accessed': json.dumps(datetime.now(), indent=4, sort_keys=True, default=str)}})
        for account in get_accounts(customer_id):
            transactions = get_transactions(account['_id'])
            process_statistics(user, account, transactions)
            log_transactions(transactions)
            find_subcriptions()