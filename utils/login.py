from tinydb import TinyDB,Query
from utils.Exeptions import IncorrectLogin
db = TinyDB('database.json')
user_table = db.table('User')
query = Query()

def login(username, password):
    search =user_table.search(query.username == username and query.password == password)
    if search !=[]:
        return search.pop()
    else: raise IncorrectLogin

# login('humam','123456789')
