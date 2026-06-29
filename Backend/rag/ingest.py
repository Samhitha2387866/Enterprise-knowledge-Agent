from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
import os
from pathlib import Path

document_path = Path(__file__).resolve().parents[2] / "documents"
all_docs = []
if not document_path.exists():
    raise FileNotFoundError(f"Documents directory not found: {document_path}")

for file_path in document_path.iterdir():
    if file_path.is_file() and file_path.suffix.lower() == ".pdf":
        try:
            loader = PyPDFLoader(file_path)
            docs = loader.load()
            all_docs.extend(docs)
        except Exception as exc:
            print(f"Skipping invalid PDF {file_path.name}: {exc}")

print("Documents loaded:", len(all_docs))
if not all_docs:
    raise SystemExit("No documents were loaded. Check the documents directory and PDF files.")

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
chunks = splitter.split_documents(all_docs)
print("Chunks created:", len(chunks))

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = Chroma.from_documents(chunks, embeddings, persist_directory="vector_db")
print("Vector database created")