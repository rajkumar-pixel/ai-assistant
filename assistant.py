from src.similarity import search_dataset
from src.rag import rag_search
from src.guardrails import safety_check,domain_check


def assistant(query):

    # STEP 1 Guardrails safety
    safety=safety_check(query)
    if safety:
        return safety
    
    # STEP 2 Domain check
    domain=domain_check(query)
    if domain:
        return domain

    # STEP 3 Dataset similarity (Tier 1)
    dataset_result=search_dataset(query)
    if dataset_result:
        return dataset_result

    # STEP 4 RAG retrieval (Tier 3)
    financial_keywords=[

    "interest",
    "penalty",
    "foreclosure",
    "policy",
    "rules"

    ]
    if any(word in query.lower() for word in financial_keywords):
        return rag_search(query)

    # STEP 5 fallback response (Tier 2 simplified)
    return "Please contact bank customer support for detailed assistance."