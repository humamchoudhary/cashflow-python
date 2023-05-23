from pprint import pprint
from tinydb import TinyDB,Query
from utils.Exeptions import IncorrectLogin
from datetime import datetime

def newTransection(username,destination_type,destination,payment_type,amount,transection,mode):
    db = TinyDB('database.json')
    user_table = db.table('User')
    query = Query()
    if username != destination:

        new_transaction = {
                            "dest_type": destination_type,
                            "destination": destination,
                            "type": payment_type,
                            "amount": amount,
                            "date_time": datetime.now().strftime('%d-%m-%Y %H:%M:%S'),
                            "transection": transection,
                            "mode": mode
                        }
        pprint(new_transaction)
        if destination_type == 'Inter Bank' :
            user_query = query.username == username
            user = user_table.get(user_query)
            if user is None:
                return {'success':False,'message':f"User '{destination}' not found."}
            else:
                if transection == 'incoming':
                    user['balance'] += amount
                elif transection == 'outgoing':
                    if user['balance'] >amount:
                        user['balance'] -= amount
                    else:
                        return{'success':False,'message':'Insufficent balance!'}
                    
                user['transection_log'].insert(new_transaction,0)
                user_table.update(user, user_query)
                return {'success':True,'message':"Transaction Complete"}
           
        elif destination_type == 'Local Bank':
            user_query = query.username == username
            user = user_table.get(user_query)
            
            pprint(user)
            if transection == 'incoming':
                    user['balance'] += amount
            elif transection == 'outgoing':
                if user['balance'] >amount:
                    user['balance'] -= amount
                else:
                    return{'success':False,'message':'Insufficent balance!'}
            user['transection_log'].insert(new_transaction,0)
            user_table.update(user, user_query)

            return {'success':True,'message':"Transaction Complete"}
            
    else:
        return {'success':False,'message':f"Username is same as destination"}



# newTransection('humamch','Inter Bank','humamch2','Misc',12,'incoming','Online transection')