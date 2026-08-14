from backend.app.rag.retriever import get_retriever


def main():

    retriever = get_retriever(k=4)

    queries = [
        "What is discussed about RAG and LangChain?",
        "What are the main concepts explained in the document?",
        "What does the document say about retrieval?"
    ]

    for query in queries:

        print("\n" + "=" * 80)
        print(f"QUERY: {query}")
        print("=" * 80)

        documents = retriever.invoke(query)

        print(
            f"Retrieved chunks: {len(documents)}"
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
                "\nMETADATA:"
            )

            print(
                document.metadata
            )


if __name__ == "__main__":
    main()