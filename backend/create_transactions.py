import requests
import json


def createDummyTransaction(api_key, id):
    url = 'http://api.nessieisreal.com/accounts/'+str(id)+'/purchases?key={}'.format(api_key)
    payload = {
        "merchant_id": "string",
        "medium": "balance",
        "purchase_date": "2023-03-25",
        "amount": 0,
        "status": "pending",
        "description": "string"
    }

    response = requests.post( 
        url, 
        data=json.dumps(payload),
        headers={'Content-Type': 'application/json', 'Accept': 'application/json'},
    )

    return response