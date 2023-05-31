import difflib


keywords = {
    "Health": [
        "medical debt",
        "hospital bills",
        "prescription costs",
        "health insurance coverage gaps",
        "expensive treatments",
        "chronic illness",
        "disability-related expenses",
        "long-term care costs",
        "mental health care expenses",
        "unexpected medical emergencies",
    ],
    "Education": [
        "student loan debt",
        "defaulted student loans",
        "high tuition fees",
        "education-related expenses",
        "inability to pay off student loans",
        "lack of job prospects after graduation",
        "education loan interest rates",
    ],
    "Utilities": [
        "rent arrears",
        "mortgage payment difficulties",
        "utility bill defaults",
        "high housing costs",
        "home repairs and maintenance",
        "utility disconnections",
        "substandard housing",
        "property taxes",
    ],
    "Family Support": [
        "childcare costs",
        "elderly care expenses",
        "alimony or child support obligations",
        "divorce or separation-related financial challenges",
        "financial responsibility for family members",
        "dependents' medical expenses",
    ],
}


def detect_financial_problem(user_input):
    user_input = user_input.lower()
    for domain, keywords in keywords.items():
        for keyword in keywords:
            matcher = difflib.SequenceMatcher(None, user_input, keyword.lower())
            similarity_ratio = matcher.ratio()
            if similarity_ratio >= 0.7:  # Adjust the similarity threshold as needed
                return f"Detected financial problem '{keyword}' in the domain: {domain}"
    return "No financial problem detected"
