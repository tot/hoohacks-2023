from flask import jsonify
from dotenv import load_dotenv
from datetime import datetime
from pymongo import MongoClient
from enum import Enum
import os, requests, json

load_dotenv()
api_key = os.getenv('API_KEY')
db_url = os.getenv('DB_URL')
db = MongoClient(db_url)['admin']
users = db['users']
subscriptions = db['subscriptions']

def get_subscriptions(customer_id):
    user = db.users.find({'_id': customer_id}).next()
    subscriptions = []
    for sub in db['subscriptions'].find({"_id": {"$in": user['subscription_ids']}}):
        sub['_id'] = str(sub['_id'])
        subscriptions.append(sub)
    return  subscriptions

def get_statistics(customer_id):
    user = db.users.find({'_id': customer_id}).next()
    accounts = []
    for acct in db['accounts'].find({"_id": {"$in": user['account_ids']}}):
        acct['stats']['_id'] = acct['_id']
        acct['stats']['type'] = acct['type']
        accounts.append(acct['stats'])
    return accounts

def get_transactions(customer_id):
    transactions = [t for t in db['txns'].find({"buyer_id": customer_id})];
    return transactions

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

def get_merchant_name(merchant_id):
    return json.loads(requests.get( 
	'http://api.nessieisreal.com/merchants/{}?key={}'.format(merchant_id, api_key),
	headers={'Accept': 'application/json'},
    )._content)['name']

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

def log_transactions(customer_id, transactions):
        for transaction in transactions:
            t_id, m_id, _ = transaction['_id'], transaction['merchant_id'], transaction['payer_id']
            date, amt, descr = transaction['purchase_date'], transaction['amount'], transaction['description']
            db.txns.update_one({'_id': transaction['_id']}, {'$set': {'_id': t_id, 'merchant_id': m_id, 'merchant_name': get_merchant_name(m_id), 'buyer_id': customer_id, 'purchase_date': date, 'amount': amt, 'description': descr}}, upsert = True)

def process_customer_data(customer_id):
    user = db.users.find({'_id': customer_id}).next()
    last_accessed = datetime.strptime(user['last_accessed'][1:-1], '%Y-%m-%d %H:%M:%S.%f')
    if datetime.now() or datetime.now() - last_accessed > 86400:
        for account in get_accounts(customer_id):
            transactions = get_transactions(account['_id'])
            process_statistics(user, account, transactions)
            log_transactions(customer_id, transactions)
            count_subscriptions(transactions, customer_id)
        db.users.update_one({'_id': customer_id}, {'$set': {'last_accessed': json.dumps(datetime.now(), indent=4, sort_keys=True, default=str)}})

class TimeInterval(Enum):
    ONE_YEAR = 365 * 24 * 3600
    SIX_MONTHS = 6 * 30 * 24 * 3600
    ONE_MONTH = 30 * 24 * 3600
'''
write db code to check if to datetime strings are exactly the interval apart 
the dates are not necessarily in order
also make enums to represent common intervals like a year, 6-months, and one month
'''
def checkInterval(date1: str, date2: str, interval: TimeInterval) -> bool:
    date_format = "%Y-%m-%d %H:%M:%S.%f"
    datetime1 = datetime.strptime(date1, date_format)
    datetime2 = datetime.strptime(date2, date_format)
    delta = abs(datetime1 - datetime2)
    return delta.total_seconds() == interval.value

def mostRecent(date1: str, date2: str) -> str:
    date_format = "%Y-%m-%d %H:%M:%S.%f"
    datetime1 = datetime.strptime(date1, date_format)
    datetime2 = datetime.strptime(date2, date_format)

    if datetime1 >= datetime2:
        return datetime1.strftime(date_format)
    else:
        return datetime2.strftime(date_format)

'''
write a method that takes date stringss and returns the most recent
'''

def count_subscriptions(transactions, customer_id):
    for i, transaction in enumerate(transactions):
        date = transaction["purchase_date"]
        _id = transaction["merchant_id"]
        name = get_merchant_name(_id)
        cost = transaction["amount"]
        merchants = []
        for j in range(i+1, len(transactions)):
            next_date = transactions[j]["purchase_date"]
            next_name = transactions[j]["merchant_name"]
            if name not in merchants and (checkInterval(date, next_date, TimeInterval.ONE_MONTH) or checkInterval(date, next_date, TimeInterval.SIX_MONTHS) or checkInterval(date, next_date, TimeInterval.ONE_YEAR)):
                q = {"$and": [{"merchant_id": _id},{"cost": cost}]}
                u = {"$set": {    
                    "merchant_name": next_name,
                    "merchant_id": _id,
                    "cost": cost,
                    "last_renewal": mostRecent(date, next_date)
                }}
                sub_id = db["subscriptions"].update_one(q, u, upsert=True).upserted_id
                if sub_id:
                    existing = db.users.find({"_id": customer_id}).next()['subscription_ids']
                    existing.append(sub_id)
                    db.users.update_one({"_id": customer_id}, {'$set': {"subscription_ids": existing}})  
                    merchants.append(name)
                break

test_transactions = [
    {
        "purchase_date": "2021-01-01 00:00:00.000",
        "merchant_name": "Netflix",
        "merchant_id": 1,
        "amount": 10
    },
    {
        "purchase_date": "2021-01-31 00:00:00.000",
        "merchant_name": "Netflix",
        "merchant_id": 1,
        "amount": 10
    },
    {
        "purchase_date": "2021-02-28 00:00:00.000",
        "merchant_name": "Netflix",
        "merchant_id": 1,
        "amount": 10
    },
    {
        "purchase_date": "2021-03-01 00:00:00.000",
        "merchant_name": "Hulu",
        "merchant_id": 2,
        "amount": 20
    },
    {
        "purchase_date": "2021-04-01 00:00:00.000",
        "merchant_name": "Hulu",
        "merchant_id": 2,
        "amount": 20
    },
    {
        "purchase_date": "2021-05-01 00:00:00.000",
        "merchant_name": "Amazon",
        "merchant_id": 3,
        "amount": 40
    }
]