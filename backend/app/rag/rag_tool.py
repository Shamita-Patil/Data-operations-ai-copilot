from langchain_core.tools import tool

from backend.app.rag.multi_query_retriever import (
    MultiQueryRetriever,
)


retriever = MultiQueryRetriever(
    k=4
)


@tool
def search_enterprise_knowledge(
    query: str,
) -> str:
    """
    Search enterprise documents for relevant information.
    Use this tool when the answer requires information
    from the organization's indexed documents.
    """

    result = retriever.invoke(query)

    documents = result["documents"]

    if not documents:
        return "No relevant enterprise documents were found."

    formatted_chunks = []

    for index, document in enumerate(
        documents[:8],
        start=1,
    ):

        source = document.metadata.get(
            "source",
            "unknown",
        )

        page = document.metadata.get(
            "page",
            "unknown",
        )

        formatted_chunks.append(
            f"[Source {index}] "
            f"source={source}, "
            f"page={page}\n"
            f"{document.page_content}"
        )

    return "\n\n".join(
        formatted_chunks
    )