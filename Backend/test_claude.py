import sys
from pathlib import Path

venv_site_packages = Path(__file__).resolve().parent / "venv" / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages"
if venv_site_packages.exists():
    sys.path.insert(0, str(venv_site_packages))

from Agents.retriever import retrieve_documents
from Agents.analyst import generate_answer
question="Explain leave policy"
docs=retrieve_documents(question)
context="\n".join([doc.page_content for doc in docs])
answer=generate_answer(context,question)
print("Answer:",answer)