def rewrite_query(query: str) -> str:
    """
    Convert a vague user query into a more retrieval-friendly query.
    """

    query = query.strip()

    replacements = {
        "xml thing": "XML ingestion pipeline",
        "xml issue": "XML ingestion pipeline failure",
        "not working": "failure troubleshooting",
        "why did it fail": "failure cause troubleshooting",
        "rag stuff": "RAG retrieval augmented generation concepts",
    }

    rewritten = query.lower()

    for old, new in replacements.items():
        rewritten = rewritten.replace(
            old,
            new,
        )

    return rewritten