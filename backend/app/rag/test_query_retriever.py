from backend.app.rag.query_retriever import (
    QueryAwareRetriever,
)


def main():

    retriever = QueryAwareRetriever(
        k=4
    )

    query = (
        "Why isn't my XML thing working?"
    )

    result = retriever.invoke(
        query
    )

    print(
        f"Original query: "
        f"{result['original_query']}"
    )

    print(
        f"Rewritten query: "
        f"{result['rewritten_query']}"
    )

    print(
        f"Retrieved chunks: "
        f"{len(result['documents'])}"
    )

    for index, document in enumerate(
        result["documents"],
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