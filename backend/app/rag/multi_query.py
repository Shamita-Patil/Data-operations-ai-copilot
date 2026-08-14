def generate_queries(
    query: str,
) -> list[str]:

    query = query.strip()

    return [
        query,
        f"{query} troubleshooting",
        f"{query} root cause",
        f"{query} resolution",
    ]