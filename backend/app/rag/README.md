RAG PIPELINE

DOCUMENT INGESTION

Document
   ↓
Loader
   ↓
Chunking
   ↓
Embeddings
   ↓
Vector Store


QUERY PIPELINE

User Query
   ↓
Query Embedding
   ↓
Similarity Search
   ↓
Top-k Chunks
   ↓
LLM
   ↓
Grounded Answer