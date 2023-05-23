# import nltk
import nltk


def extract_keywords(text):
    # Tokenize the text into individual words
    tokens = nltk.word_tokenize(text)

    # Perform part-of-speech tagging to identify nouns and adjectives
    tagged_words = nltk.pos_tag(tokens)

    # Extract keywords based on specific parts of speech
    keywords = []
    for word, pos in tagged_words:
        print(word, pos)
        if pos.startswith("N") or pos.startswith("J"):  # Nouns and adjectives
            keywords.append(word.lower())

    return keywords


def assess_financial_need(keywords):
    threshold_keywords = [
        "financial",
        "burdens",
        "costs",
        "accumulate",
        "treatment",
        "resources",
        "expenses",
        "transportation",
        "accommodation",
        "support",
        "assistance",
        "alleviate",
        "stress",
        "adequate",
        "healthcare",
        "health",
        "challenges",
    ]
    matched_keywords = set(keywords) & set(threshold_keywords)
    print(matched_keywords)
    if len(matched_keywords) > 5:
        return True
    else:
        return False



# user_input = input("Please provide a paragraph describing your financial situation: ")
# user_keywords = extract_keywords(user_input)
# assess_financial_need(user_keywords, threshold_keywords)
