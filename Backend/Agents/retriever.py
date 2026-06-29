from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
def retrieve_documents(question):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    db = Chroma(persist_directory="vector_db", embedding_function=embeddings)
    results = db.similarity_search(question, k=5)
    return results