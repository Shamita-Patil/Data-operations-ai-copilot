from backend.app.rag.retriever import get_retriever


def check_retrieval(
    query: str,
    expected_keyword: str,
):

    retriever = get_retriever(k=4)

    documents = retriever.invoke(query)

    combined_text = " ".join(
        document.page_content.lower()
        for document in documents
    )

    passed = (
        expected_keyword.lower()
        in combined_text
    )

    print(
        f"Query: {query}"
    )

    print(
        f"Expected keyword: {expected_keyword}"
    )

    print(
        f"Retrieval check: {'PASS' if passed else 'FAIL'}"
    )


if __name__ == "__main__":

    check_retrieval(
        query="What is discussed about RAG and LangChain?",
        expected_keyword="RAG",
    )