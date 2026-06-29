from Agents.retriever import retrieve_documents
question="Explain leave policy"
docs=retrieve_documents(question)
for doc in docs:
    print("--------------")
    print(doc.page_content[:300])
