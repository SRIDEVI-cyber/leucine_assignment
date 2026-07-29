from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Lazy-loaded model
_model = None


def get_model():
    global _model
    if _model is None:
        print("Loading SentenceTransformer model...")
        _model = SentenceTransformer("all-MiniLM-L6-v2")
    return _model


# FAISS index
dimension = 384
index = faiss.IndexFlatL2(dimension)

# Store document chunks
documents = []


def split_text(text, chunk_size=500):
    """
    Split text into chunks of approximately chunk_size characters.
    """
    chunks = []

    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])

    return chunks


def add_documents(text):
    """
    Split document into chunks and add embeddings to FAISS.
    """

    global documents

    chunks = split_text(text)

    if not chunks:
        return

    model = get_model()

    embeddings = model.encode(chunks)

    index.add(np.array(embeddings).astype("float32"))

    documents.extend(chunks)


def search_documents(query, k=3):
    """
    Retrieve top-k relevant document chunks.
    """

    if len(documents) == 0:
        return []

    model = get_model()

    query_embedding = model.encode([query])

    distances, indices = index.search(
        np.array(query_embedding).astype("float32"),
        k
    )

    results = []

    for idx in indices[0]:
        if idx < len(documents):
            results.append(documents[idx])

    return results