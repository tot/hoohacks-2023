import json
import datetime
import requests
import os
import prompts
from functools import wraps
from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS, cross_origin
from bs4 import BeautifulSoup
from typing import List


db_url = os.getenv("DB_URL")
app = Flask(__name__)
client = MongoClient(db_url)
users = client["users"]

cors = CORS(app)
'''
frontend needs:
needs to be able to get a dump of user stats 
needs customer transaction history 

'''
@app.route('/api/overview', methods=['GET'])
def respond():
    req = request.get_json()
    customer_id = req["customer_id"]
    name = request.args.get("msg", None)
    print(f"Received: {name}")

    response = {}

    if not name:
        response["ERROR"] = "No name found. Please send a name."

    elif str(name).isdigit():
        response["ERROR"] = "The name can't be numeric. Please send a string."
    else:
        response["MESSAGE"] = f"Your message: {name}"

    return jsonify(response)

@app.route('/preprocess',methods = ['POST', 'GET'])
def preprocess():
    query = request.get_json()['query']
    links = request.get_json()['results']
    titles = request.get_json()['titles']
    if links == None or len(links) == 0:
        return jsonify({'message': 'Links are missing!'}), 400
    if titles == None or len(links) == 0:
        return jsonify({'message': 'Titles are missing!'}), 400

    print(request.data)
    df = aggregate.fast_text(query, links, titles)
    result = df.to_json(orient="split")
    parsed = json.loads(result)
    return json.dumps(parsed, indent=4)  

@app.route('/record',methods = ['POST', 'GET'])
def record():
    queries = request.get_json()['query']
    if queries == None or len(queries) == 0:
        return jsonify({'message': 'Queries are missing!'}), 400

    original = queries.pop(0)
    aggregate.store_queries(original, queries)
    return jsonify({'message':'success'})
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