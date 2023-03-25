import requests
import json, random


def get_merchants(api_key):
    return json.loads(requests.get( 
    'http://api.nessieisreal.com/merchants?key={}'.format(api_key),
    headers={'Accept': 'application/json'},
    )._content)

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
        "status": "pending",
        "description": "filler"
    }

    response = requests.post( 
        url, 
        data=json.dumps(payload),
        headers={'Content-Type': 'application/json', 'Accept': 'application/json'},
    )

    return response