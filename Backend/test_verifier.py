from Agents.retriever import retrieve_documents
from Agents.analyst import generate_answer
from Agents.verifier import verify_answer
question = "Explain leave policy"
docs = retrieve_documents(question)
context = "\n".join([doc.page_content for doc in docs])
answer = generate_answer(context, question)
validation=verify_answer(answer, docs)
print("Answer:", answer)
print("\nValidation:", validation)