from tinydb import TinyDB, Query

# from utils.Exeptions import AccountExists
from utils.QRgen import generate_qr_code
from random import choice
import string


def luhn_algorithm():
    rand_number = "".join(choice(string.digits) for _ in range(13))
    card_number = f"41{rand_number}"
    digits = [int(digit) for digit in str(card_number)]
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]

    total = sum(odd_digits)

    for digit in even_digits:
        total += sum(divmod(digit * 2, 10))

    return ((total * 9) % 10, card_number)


def signup(username, password, fname, email, gender):
    db = TinyDB("database.json")
    user_table = db.table("User")
    query = Query()
    search = user_table.search((query.username == username) | (query.email == email))
    if len(search) > 0:
        return {"success": False, "message": "Username or email exists!"}
        # raise AccountExists("Username or email exists!")
    else:
        user_table.insert(
            {
                "account_number": 1232142132,  # TODO Create a account number generator
                "username": username,
                "password": password,
                "email": email,
                "gender": gender,
                "full_name": fname,
                "balance": 0,
                "savings": 0,
                "saving_percent": 15,
                "useable_bal": 0,
                "currency": "USD",
                # TODO create a graph handler
                "expense": [],
                "income": [],
                "year": "2023",
                "month": "May",
                "date": "17",
                "day": "Wednessday",
                "months": [],
                "transaction_log": [],
                "qr": generate_qr_code({"destination": username}),
                "Cards": [
                    # TODO: Create a card  generaot
                    {
                        "card_number": luhn_algorithm(),
                        "cvv": 123,
                        "exp_date": "08/23",
                        "card_name": fname,
                        "limits": {
                            "daily": {
                                "date": "13-03-2023",
                                "total": 5000,
                                "left": 5000,
                                "spent": 0,
                            },
                            "monthly": {
                                "month": "03-2023",
                                "total": 100000,
                                "left": 100000,
                                "spent": 0,
                            },
                        },
                    }
                ],
            }
        )
        return {"success": True, "message": "Account created successfully"}


# print(signup("humamch3", "123456", "Muhammad Humam", "humamch4@gmail.com", "M"))
