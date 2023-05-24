from flask import Flask, jsonify, make_response, request
import json
from tinydb import TinyDB, Query
from utils.login import login
from utils.signup import signup
from flask_cors import CORS
from utils.transactions import newTransaction
from pprint import pprint
from utils.questions import assess_financial_need
import time

app = Flask(__name__)
CORS(app)
DB = TinyDB("database.json")
QRY = Query()


@app.route("/login", methods=["POST"])
def loginRoute():
    request_data = request.data
    request_data = json.loads(request_data.decode("utf-8"))
    # print(request_data)
    # request_data = request.args
    return make_response(
        jsonify(login(request_data["username"], request_data["password"]))
    )


@app.route("/signup", methods=["POST"])
def signupRoute():
    request_data = request.data
    request_data = json.loads(request_data.decode("utf-8"))
    # request_data = request.args
    return signup(
        request_data["username"],
        request_data["password"],
        request_data["name"],
        request_data["email"],
        request_data["gender"],
    )


@app.route("/get_transactions")
def transactionsRoute():
    request_data = request.args
    user = request_data["username"]
    search = DB.table("User").search(QRY.username == user)
    return search.pop()["transaction_log"]


@app.route("/make_transaction", methods=["POST"])
def make_transaction():
    request_data = request.data
    request_data = json.loads(request_data.decode("utf-8"))
    pprint(request_data)

    sender_log = newTransaction(
        request_data["username"],
        request_data["dest_type"],
        request_data["destination"],
        request_data["type"],
        float(request_data["amount"]),
        request_data["transaction"],
        request_data["mode"],
    )
    if sender_log["success"] == True and request_data["dest_type"] == "Inter Bank":
        newTransaction(
            request_data["destination"],
            request_data["dest_type"],
            request_data["username"],
            request_data["type"],
            float(request_data["amount"]),
            "incoming",
            request_data["mode"],
        )
    print(sender_log)
    return make_response(jsonify(sender_log))


@app.route("/unlock_saving")
def unlock():
    request_data = request.args
    text = request_data["reason"]
    amount = float(request_data["amount"])
    request_data["username"]
    if assess_financial_need(text):
        return jsonify(
            {
                "success": True,
                "message": "Savings unlocked.",
            }
        )
    else:
        return jsonify(
            {
                "success": False,
                "message": "Thank you for your information. We will look into it!",
            }
        )


if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
