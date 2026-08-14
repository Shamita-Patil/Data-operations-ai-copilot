from backend.app.rag.retriever import get_retriever


def main():

    retriever = get_retriever(
        k=4
    )

    query = (
        "What is discussed about "
        "RAG and LangChain?"
    )

    documents = retriever.invoke(
        query
    )

    print(
        f"Retrieved chunks: {len(documents)}"
    )

    for index, document in enumerate(
        documents,
        start=1,
    ):

        print(
            f"\n--- Chunk {index} ---"
        )

        print(
            document.page_content[:1000]
        )

        print(
            "\nMetadata:"
        )

        print(
            document.metadata
        )


if __name__ == "__main__":

    main()