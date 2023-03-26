import json
import datetime
import requests
import os
import prompts
import process_data
from functools import wraps
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from bs4 import BeautifulSoup
from typing import List


db_url = os.getenv("DB_URL")
app = Flask(__name__)

cors = CORS(app)
'''
frontend needs:
needs to be able to get a dump of user stats 
needs customer transaction history 

/api/subscriptions
/api/stats
/api/transactions
/api/openaistuff
/api/recommendations
'''
@app.route('/api/overview', methods=['GET'])
def overview():
    return jsonify(process_data.get_overview)

@app.route('/api/subscriptions',methods = ['POST', 'GET'])
def subscriptions():
    req = request.get_json()
    if "customer_id" not in req:
         return jsonify({'message': 'Customer ID is missing!'}), 400
        
    customer_id = req["customer_id"]
    return jsonify(process_data.get_subscriptions(customer_id))

@app.route('/api/stats',methods = ['POST', 'GET'])
def stats():
    req = request.get_json()
    if "customer_id" not in req:
         return jsonify({'message': 'Customer ID is missing!'}), 400
        
    customer_id = req["customer_id"]
    return jsonify(process_data.get_stats(customer_id))

@app.route('/api/transactions',methods = ['POST', 'GET'])
def transactios():
    req = request.get_json()
    if "customer_id" not in req:
         return jsonify({'message': 'Customer ID is missing!'}), 400
        
    customer_id = req["customer_id"]
    return jsonify(process_data.get_transactions(customer_id))

'''
@app.route('/transactions', methods=['POST'])
def add_transaction():
    transaction = json.loads(request.data)
    transactions.insert_one(transaction)
    return {'result': 'Transaction added'}

@app.route('/transactions/<user_id>', methods=['GET'])
def get_users(user_id):
    user_trans = users.find({'user_id': user_id})
    transaction_list = [transaction for user in user_trans]
    for transaction in transaction_list:
        transaction['_id'] = str(transaction['_id'])
    return {"user_transactions": transaction_list}
'''

@app.route('/account',methods = ['POST', 'GET'])
def getAccount():
    '''
    This should take in an id 
    '''
    req = request.get_json()
    query = req['ID']
    if query == None or len(query) == 0:
        return jsonify({'message': 'Queries are missing!'}), 400

    response = {}
    ranked = []

    return json.dumps(ranked)

@app.route('/rank',methods = ['POST', 'GET'])
def rank():
    '''
    This should take in query and list
    '''
    #query = "water"
    req = request.get_json()
    query = req['query']
    articles = req['articles']
    if query == None or len(query) == 0:
        return jsonify({'message': 'Queries are missing!'}), 400

    response = {}
    ranked = []

    return json.dumps(ranked)

    

if __name__ == '__main__':
    app.run(debug=True)
    #app.run(threaded=True, port=3000)