from backend.app.rag.hybrid_retriever import (
    HybridRetriever,
)

from backend.app.rag.query_rewriter import (
    rewrite_query,
)


class QueryAwareRetriever:

    def __init__(
        self,
        k: int = 4,
    ):

        self.retriever = HybridRetriever(
            k=k
        )

    def invoke(
        self,
        query: str,
    ):

        rewritten_query = rewrite_query(
            query
        )

        documents = (
            self.retriever.invoke(
                rewritten_query
            )
        )

        return {
            "original_query": query,
            "rewritten_query": rewritten_query,
            "documents": documents,
        }