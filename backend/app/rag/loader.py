from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader


def load_pdf(pdf_path: str):

    path = Path(pdf_path)

    if not path.exists():
        raise FileNotFoundError(
            f"PDF not found: {pdf_path}"
        )

    loader = PyPDFLoader(
        str(path)
    )

    documents = loader.load()

    return documents