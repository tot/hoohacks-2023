from dotenv import load_dotenv
import requests
import os
import json, random, time

load_dotenv()
api_key = os.getenv("API_KEY")

def get_merchants(api_key):
    return json.loads(requests.get( 
    'http://api.nessieisreal.com/merchants?key={}'.format(api_key),
    headers={'Accept': 'application/json'},
    )._content)

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


def createDummyTransaction(api_key, id):
    url = 'http://api.nessieisreal.com/accounts/'+str(id)+'/purchases?key={}'.format(api_key)

    merchants = get_merchants(api_key)
    merchantID = merchants[random.randint(0,len(merchants))]["_id"]

    cost = random.randint(0, 100)
    payload = {
        "merchant_id": merchantID,
        "medium": "balance",
        "purchase_date": "2023-03-25",
        "amount": cost,
        "status": "completed",
        "description": "filler"
    }

    try:
        response = requests.post( 
            url, 
            data=json.dumps(payload),
            headers={'Content-Type': 'application/json', 'Accept': 'application/json'},timeout=50,
        )
        print(response.content)
    except requests.exceptions.RequestException:
        time.sleep(15)
        createDummyTransaction(api_key,id)

