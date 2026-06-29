from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document
from pdf2image import convert_from_path, pdfinfo_from_path
import pytesseract
from pathlib import Path

document_path = Path(__file__).resolve().parents[2] / "documents"
all_docs = []
if not document_path.exists():
    raise FileNotFoundError(f"Documents directory not found: {document_path}")


def ocr_pdf(file_path, dpi=200):
    """Extract text from a scanned/image PDF using OCR.

    Pages are converted and OCR'd one at a time to keep memory low — loading
    every page of a large PDF as a high-res image at once can exhaust RAM.
    """
    page_count = pdfinfo_from_path(str(file_path))["Pages"]
    docs = []
    for i in range(1, page_count + 1):
        images = convert_from_path(str(file_path), dpi=dpi, first_page=i, last_page=i)
        text = pytesseract.image_to_string(images[0])
        if text.strip():
            docs.append(
                Document(
                    page_content=text,
                    metadata={"source": str(file_path), "page": i - 1, "ocr": True},
                )
            )
    return docs


for file_path in document_path.iterdir():
    if not (file_path.is_file() and file_path.suffix.lower() == ".pdf"):
        continue
    try:
        docs = PyPDFLoader(str(file_path)).load()
        text_chars = sum(len(d.page_content.strip()) for d in docs)
        if text_chars == 0:
            # No text layer -> scanned/image PDF, fall back to OCR.
            print(f"No text layer in {file_path.name}; running OCR…")
            docs = ocr_pdf(file_path)
            print(f"  OCR extracted {len(docs)} page(s) of text.")
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
