from backend.app.rag.hybrid_retriever import (
    HybridRetriever,
)

from backend.app.rag.multi_query import (
    generate_queries,
)


class MultiQueryRetriever:

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

        queries = generate_queries(
            query
        )

        results = []

        seen = set()

        for generated_query in queries:

            documents = (
                self.retriever.invoke(
                    generated_query
                )
            )

            for document in documents:

                key = (
                    document.metadata.get(
                        "source",
                        ""
                    ),
                    document.metadata.get(
                        "page",
                        ""
                    ),
                    document.page_content,
                )

                if key in seen:
                    continue

                seen.add(key)

                results.append(
                    document
                )

        return {
            "queries": queries,
            "documents": results,
        }