from tinydb import TinyDB,Query
from utils.Exeptions import AccountExists
db = TinyDB('database.json')
user_table = db.table('User')
query = Query()

def signup(username,password,fname,email,gender):
    search = user_table.search((query.username==username )|( query.email==email ))
    if len(search) >0:
        raise AccountExists("Username or email exists!")
    else:
        user_table.insert(
            {
                "username":username,
                "password":password,
                "email":email,
                "gender":gender,
                "full_name":fname,
                "balance":0,
                "currency":"USD",
                "account_number":00000000000000,    # TODO Create a account number generator
                "transection_log":[],
                "Cards":[
                    #TODO: Create a card  generaot
                    {
                        "card_number":00000000000000000,     
                        "cvv":123,
                        "exp_date":"08/23",
                        "card_name":username,
                        "limits": {
                                        "daily": { "date": "13-03-2023", "total": 5000, "left": 4500 },
                                        "monthly": { "month": "03-2023", "total": 100000, "left": 9999500 }
                                    }
                                    

                    }
                ]

            }
            )

# signup('humamch','123456','Muhammad Humam','humamch@gmail.com','M')