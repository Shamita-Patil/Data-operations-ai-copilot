from backend.app.rag.query_rewriter import (
    rewrite_query,
)


def main():

    queries = [
        "Why isn't my XML thing working?",
        "Why did the XML issue fail?",
        "Tell me about RAG stuff",
    ]

    for query in queries:

        rewritten = rewrite_query(
            query
        )

        print(
            f"\nOriginal : {query}"
        )

        print(
            f"Rewritten: {rewritten}"
        )


if __name__ == "__main__":
    main()