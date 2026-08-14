from backend.app.rag.multi_query_retriever import (
    MultiQueryRetriever,
)


def main():

    retriever = MultiQueryRetriever(
        k=4
    )

    query = (
        "Why did my pipeline fail?"
    )

    result = retriever.invoke(
        query
    )

    print(
        "Generated queries:"
    )

    for generated_query in result[
        "queries"
    ]:

        print(
            f"- {generated_query}"
        )

    print(
        f"\nUnique retrieved chunks: "
        f"{len(result['documents'])}"
    )

    for index, document in enumerate(
        result["documents"][:8],
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