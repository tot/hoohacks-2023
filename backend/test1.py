from dotenv import load_dotenv
import json
import os
import requests 


load_dotenv()
api_key = os.getenv("API_KEY")

def get_customers():
    return json.loads(requests.get( 
    'http://api.nessieisreal.com/customers?key={}'.format(api_key),
    headers={'Accept': 'application/json'},
    )._content)

def get_transactions(account_id):
    return json.loads(requests.get( 
	'http://api.nessieisreal.com/accounts/{}/purchases?key={}'.format(account_id, api_key),
	headers={'Accept': 'application/json'})._content)

def create_deposit_account(customer_id):
    return json.loads(requests.post( 
	'http://api.nessieisreal.com/customers/{}/accounts'.format(customer_id),
	headers={'Accept': 'application/json'})._content)

def get_customer_accounts(customer_id):
    return json.loads(requests.get( 
	'http://api.nessieisreal.com/customers/{}/accounts'.format(customer_id),
	headers={'Accept': 'application/json'})._content)

# Create an account for a customer by ID
def create_deposit_account(customer_id, account_data):
    response = requests.post(
        'http://api.nessieisreal.com/customers/{}/accounts?key={}'.format(customer_id, api_key),
        json=account_data,
        headers={'Accept': 'application/json', 'Content-Type': 'application/json'},
    )

    if response.status_code == 201:
        result = json.loads(response._content)
        return result
    elif response.status_code == 404:
        return {"code": 0, "message": "Customer not found", "fields": "string"}
    else:
        return {"code": -1, "message": "Unknown error", "fields": "string"}




account_data = {
    "type": "Credit Card",
    "nickname": "string",
    "rewards": 0,
    "balance": 0,
    "account_number": "string",
}
customers = get_customers()
customer_id = customers[0]['_id']  # Assuming the first customer's ID

created_account = create_account(customer_id, account_data)
print(created_account)
'''
customers = get_customers()
#print(customers)
customer = customers[0]
#decoded_string = customer.decode("utf-8")
#parsed_dict = json.loads(decoded_string)
print(customers[0]['_id'])
customer_id = customers[0]['_id']
print(get_customer_accounts(customer_id))
#customer_id = parsed_dict["_id"]                         
#print(customer_id)
#print(get_transactions(customer_id))

#print(customers)
#print(type(customers))

binary_string = b'{"code":201,"message":"Account created","objectCreated":{"type":"Credit Card","nickname":"string","rewards":0,"balance":0,"customer_id":"641f501778f6910a15f0e082","_id":"641f594a78f6910a15f0e088"}}'

decoded_string = binary_string.decode("utf-8")
parsed_dict = json.loads(decoded_string)
object_created = parsed_dict["objectCreated"]

print(object_created)
'''