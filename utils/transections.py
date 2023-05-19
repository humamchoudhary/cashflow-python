from tinydb import TinyDB,Query
from utils.Exeptions import IncorrectLogin
db = TinyDB('database.json')
user_table = db.table('User')
query = Query()

def newTransection(username,ammount,destination,destination_type,payment_type,mode):
    pass