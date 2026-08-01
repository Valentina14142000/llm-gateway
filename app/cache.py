import numpy as np
from sentence_transformers import SentenceTransformer

# Lazy-loaded model instance
_model = None
CACHE_STORE = []


def get_model():
  global _model
  if _model is None:
    print("---LOADING SENTENCE TRANSFORMER MODEL---")
    _model = SentenceTransformer("all-MiniLM-L6-v2")
  return _model


class SemanticCache:

  @staticmethod
  def get_embedding(text: str) -> np.ndarray:
    model = get_model()
    return model.encode(text)

  @staticmethod
  def lookup(query: str, threshold: float = 0.85):
    if not CACHE_STORE:
      return None

    query_vec = SemanticCache.get_embedding(query)

    for item in CACHE_STORE:
      cached_vec = item["vector"]
      similarity = np.dot(query_vec, cached_vec) / (
          np.linalg.norm(query_vec) * np.linalg.norm(cached_vec)
      )

      if similarity >= threshold:
        print(
            f"---CACHE HIT! Similarity score: {similarity:.4f} (Skipping LLM)"
        )
        return item["response"]

    print("---CACHE MISS! Proceeding to LLM route.")
    return None

  @staticmethod
  def store(query: str, response: str):
    query_vec = SemanticCache.get_embedding(query)
    CACHE_STORE.append(
        {"query": query, "vector": query_vec, "response": response}
    )