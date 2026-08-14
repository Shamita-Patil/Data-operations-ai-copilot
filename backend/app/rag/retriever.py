from backend.app.rag.embeddings import get_embeddings
from backend.app.rag.vectorstore import VECTORSTORE_PATH
from langchain_chroma import Chroma


def get_retriever(
    k: int = 4,
):

    embeddings = get_embeddings()

    vectorstore = Chroma(
        persist_directory=str(
            VECTORSTORE_PATH
        ),
        embedding_function=embeddings,
    )

    retriever = vectorstore.as_retriever(
        search_kwargs={
            "k": k
        }
    )

    return retriever