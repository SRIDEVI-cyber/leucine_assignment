from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create FAISS index
dimension = 384
index = faiss.IndexFlatL2(dimension)

# Store chunk text
documents = []

def split_text(text, chunk_size=500):

    chunks = []

    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])

    return chunks

def add_documents(text):

    chunks = split_text(text)

    embeddings = model.encode(chunks)

    index.add(np.array(embeddings).astype("float32"))

    documents.extend(chunks)

def search_documents(query, k=3):

    query_embedding = model.encode([query])

    distances, indices = index.search(
        np.array(query_embedding).astype("float32"),
        k
    )

    results = []

    for idx in indices[0]:
        if idx < len(documents):
            results.append(documents[idx])

    return "\n\n".join(results)

