from langchain_google_genai import (
    GoogleGenerativeAIEmbeddings,
)

from backend.app.core.config import settings


def get_embeddings():

    return GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-001",
        google_api_key=settings.gemini_api_key,
    )