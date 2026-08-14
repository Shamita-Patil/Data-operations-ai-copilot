import pickle
from pathlib import Path

from backend.app.rag.bm25_retriever import (
    BM25Retriever,
)
from backend.app.rag.retriever import (
    get_retriever,
)


CHUNKS_PATH = Path(
    "backend/app/rag/chunks.pkl"
)


class HybridRetriever:

    def __init__(
        self,
        k: int = 4,
        rrf_k: int = 60,
    ):

        with open(
            CHUNKS_PATH,
            "rb",
        ) as file:

            self.documents = pickle.load(
                file
            )

        self.k = k
        self.rrf_k = rrf_k

        self.semantic_retriever = (
            get_retriever(k=k)
        )

        self.bm25_retriever = BM25Retriever(
            self.documents
        )

    def invoke(self, query: str):

        semantic_results = (
            self.semantic_retriever.invoke(
                query
            )
        )

        keyword_results = (
            self.bm25_retriever.invoke(
                query,
                k=self.k,
            )
        )

        scores = {}

        documents_by_id = {}

        for rank, document in enumerate(
            semantic_results,
            start=1,
        ):

            document_id = id(document)

            documents_by_id[
                document_id
            ] = document

            scores[document_id] = (
                scores.get(
                    document_id,
                    0,
                )
                + 1 / (
                    self.rrf_k + rank
                )
            )

        for rank, document in enumerate(
            keyword_results,
            start=1,
        ):

            document_id = id(document)

            documents_by_id[
                document_id
            ] = document

            scores[document_id] = (
                scores.get(
                    document_id,
                    0,
                )
                + 1 / (
                    self.rrf_k + rank
                )
            )

        ranked_ids = sorted(
            scores,
            key=scores.get,
            reverse=True,
        )

        return [
            documents_by_id[
                document_id
            ]
            for document_id in ranked_ids[
                :self.k
            ]
        ]