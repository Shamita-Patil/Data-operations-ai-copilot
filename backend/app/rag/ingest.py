from backend.app.rag.chunker import chunk_documents
from backend.app.rag.loader import load_pdf
from backend.app.rag.vectorstore import create_vectorstore


PDF_PATH = (
    "backend/uploads/"
    "IP_RAGs_and_LangChain_Part_2.pdf"
)


def ingest_pdf():

    documents = load_pdf(
        PDF_PATH
    )

    print(
        f"Loaded documents: {len(documents)}"
    )

    chunks = chunk_documents(
        documents
    )

    print(
        f"Created chunks: {len(chunks)}"
    )

    create_vectorstore(
        chunks
    )

    print(
        "Vector store created successfully."
    )


if __name__ == "__main__":

    ingest_pdf()