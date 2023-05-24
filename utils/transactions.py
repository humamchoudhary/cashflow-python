from datetime import datetime
from tinydb import TinyDB, Query


def newTransaction(
    username, destination_type, destination, payment_type, amount, transaction, mode
):
    db = TinyDB("database.json")
    user_table = db.table("User")
    query = Query()

    if username != destination:
        new_transaction = {
            "dest_type": destination_type,
            "destination": destination,
            "type": payment_type,
            "amount": amount,
            "date_time": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            "transaction": transaction,
            "mode": mode,
        }

        if destination_type == "Inter Bank":
            user_query = query.username == username
            user = user_table.get(user_query)
            if user is None:
                return {"success": False, "message": f"User '{destination}' not found."}
            else:
                current_month = datetime.now().strftime("%B")  # Get the current month
                last_month = user["months"][-1] if user["months"] else None

                # Check if there was a dead month
                if last_month != current_month:
                    user["income"].append(0)
                    user["expense"].append(0)
                    user["months"].append(current_month)

                # Update income and expense lists based on transaction type
                if transaction == "incoming":
                    if last_month == current_month:
                        user["income"][-1] += amount
                    else:
                        user["income"].append(amount)
                    if amount > 100:
                        user["savings"] += user["saving_percent"] * amount / 100
                    else:
                        user["useable_bal"] += amount
                    user["balance"] += amount
                elif transaction == "outgoing":
                    if user["balance"] > amount:
                        user["balance"] -= amount
                        if last_month == current_month:
                            user["expense"][-1] += amount
                        else:
                            user["expense"].append(amount)
                        if amount > 100:
                            user["savings"] -= user["saving_percent"] * amount / 100
                        else:
                            user["useable_bal"] -= amount
                    else:
                        return {"success": False, "message": "Insufficient balance!"}

                user["transaction_log"].insert(0, new_transaction)
                user_table.update(user, user_query)
                return {"success": True, "message": "Transaction Complete"}

        elif destination_type == "Local Bank":
            user_query = query.username == username
            user = user_table.get(user_query)

            current_month = datetime.now().strftime("%B")  # Get the current month
            last_month = user["months"][-1] if user["months"] else None

            # Check if there was a dead month
            if last_month != current_month:
                user["income"].append(0)
                user["expense"].append(0)
                user["months"].append(current_month)

            # Update income and expense lists based on transaction type
            if transaction == "incoming":
                if last_month == current_month:
                    user["income"][-1] += amount
                else:
                    user["income"].append(amount)
                if amount > 100:
                    user["savings"] += user["saving_percent"] * amount / 100
                else:
                    user["useable_bal"] += amount
                user["balance"] += amount

            elif transaction == "outgoing":
                if user["balance"] > amount:
                    user["balance"] -= amount
                    if last_month == current_month:
                        user["expense"][-1] += amount
                    else:
                        user["expense"].append(amount)
                    if amount > 100:
                        user["savings"] -= user["saving_percent"] * amount / 100
                    else:
                        user["useable_bal"] -= amount
                else:
                    return {"success": False, "message": "Insufficient balance!"}

            user["transaction_log"].insert(0, new_transaction)
            user_table.update(user, user_query)

            return {"success": True, "message": "Transaction Complete"}

    else:
        return {"success": False, "message": "Username is the same as destination"}
