def safety_check(query):
    blocked_words=[

    "otp",
    "password",
    "cvv",
    "card number",
    "pin",
    "net banking password"

    ]
    query=query.lower()
    for word in blocked_words:
        if word in query:
            return "Sorry, I cannot process sensitive financial information."
    return None

def domain_check(query):
    banking_keywords=[

    "loan",
    "emi",
    "bank",
    "interest",
    "payment",
    "account",
    "transaction",
    "card",
    "credit",
    "debit",
    "kyc"

    ]
    query=query.lower()
    if not any(word in query for word in banking_keywords):
        return "I am a BFSI assistant. I can only answer banking and financial questions."
    return None