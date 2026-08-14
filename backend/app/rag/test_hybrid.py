from backend.app.rag.hybrid_retriever import (
    HybridRetriever,
)


def main():

    retriever = HybridRetriever(
        k=4
    )

    queries = [
        "What is RAG and LangChain?",
        "retrieval",
        "embedding",
    ]

    for query in queries:

        print(
            "\n" + "=" * 80
        )

        print(
            f"QUERY: {query}"
        )

        print(
            "=" * 80
        )

        documents = retriever.invoke(
            query
        )

        print(
            f"Retrieved: {len(documents)}"
        )

        for index, document in enumerate(
            documents,
            start=1,
        ):

            print(
                f"\n--- RESULT {index} ---"
            )

            print(
                document.page_content[:700]
            )

            print(
                "\nMetadata:"
            )

            print(
                document.metadata
            )


if __name__ == "__main__":

    main()