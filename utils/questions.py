import nltk
from tinydb import TinyDB, Query
from collections import Counter

db = TinyDB("database.json")
users = db.table("User")
q = Query()


def question(text, username):
    tokens = nltk.word_tokenize(text)
    tagged_words = nltk.pos_tag(tokens)
    keywords = []
    for word, pos in tagged_words:
        # print(word, pos)
        if pos.startswith("N") or pos.startswith("J"):
            keywords.append(word.lower())
    return assess_financial_need(keywords, username)


def assess_financial_need(keywords, username):
    threshold_keywords = {
        "Health": [
            "medical",
            "hospital",
            "bills",
            "prescription",
            "costs",
            "health",
            "insurance",
            "treatments",
            "chronic",
            "illness",
            "disability",
            "mental",
            "healthcare",
        ],
        "Education": [
            "loan",
            "student",
            "tuition",
            "fees",
            "education",
            "graduation",
        ],
        "Utilities": [
            "rent",
            "mortgage",
            "utility",
            "bill",
            "housing",
            "costs",
            "repairs",
            "maintenance",
            "disconnections",
            "substandard",
            "property",
            "taxes",
        ],
        "Family Support": [
            "childcare",
            "elderly",
            "alimony",
            "divorce",
            "separation",
            "family",
        ],
    }
    confidence_scale = []
    last_transaction_count = []
    keyword_count = 0
    for threshold_keyword in threshold_keywords:
        count = 0
        count += sum(
            Counter(threshold_keywords[threshold_keyword])[item] for item in keywords
        )
        keyword_count += count
        confidence_scale.append(count)
    if keyword_count >= 5:
        userdata = users.search(q.username == username)
        transaction_log = userdata[0]["transaction_log"][:5]
        for key in threshold_keywords:
            count = 0
            for transaction in transaction_log:
                if (
                    transaction["type"] == key
                    and transaction["transaction"] == "outgoing"
                ):
                    count += 1
            last_transaction_count.append(count)
        for logs in last_transaction_count:
            for confidence in confidence_scale:
                if logs > 2 and confidence > 5:
                    return True

        return False
    else:
        return False


# user_input = input("Please provide a paragraph describing your financial situation: ")
# user_keywords = extract_keywords(user_input)
# print(assess_financial_need(user_keywords, "humamch3"))
