from pathlib import Path

from langchain_community.vectorstores import Chroma

from backend.app.rag.embeddings import get_embeddings


VECTORSTORE_PATH = Path(
    "backend/app/rag/chroma_db"
)


def create_vectorstore(chunks):

    embeddings = get_embeddings()

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=str(
            VECTORSTORE_PATH
        ),
    )

    return vectorstore