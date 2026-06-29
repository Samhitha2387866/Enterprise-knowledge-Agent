def create_plan(question):
    plan={
        "query": question,
        "steps": [
            "Retrieve relavant documents from the knowledge base",
            "Analyze the retrieved documents to extract key information",
            "Validate the extracted information against the question",
        ]
    }
    return plan
    