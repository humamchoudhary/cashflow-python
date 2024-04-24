from tinydb import TinyDB,Query
from utils.Exeptions import IncorrectLogin

def login(username, password):
    db = TinyDB('database.json')
    user_table = db.table('User')
    query = Query()
    search =user_table.search((query.username == username) & (query.password == password))
    print(user_table)
    if search !=[]:
        return search.pop()
    else: raise IncorrectLogin

# login('humam','123456789')
