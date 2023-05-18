from flask import Flask, jsonify, make_response,request
import json
from tinydb import TinyDB, Query
from utils.login import login
from utils.signup import signup
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
DB =TinyDB('database.json')
QRY = Query() 

@app.route('/login',methods=['POST'])
def loginRoute():
    request_data = request.data
    request_data = json.loads(request_data.decode('utf-8'))
    print(request_data)
    # request_data = request.args
    return make_response(jsonify(login(request_data['username'],request_data['password'])))

@app.route('/signup')
def signupRoute():
    # request_data = request.data
    # request_data = json.loads(request_data.decode('utf-8'))
    request_data = request.args
    return signup(request_data['username'],request_data['password'],request_data['full_name'],request_data['email'],request_data['gender'])

@app.route('/get_transections')
def transectionsRoute():
    request_data = request.args
    user = request_data['username']
    search = DB.table('User').search(QRY.username == user)
    return search.pop()["transection_log"]


if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)
