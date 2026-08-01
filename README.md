# High-Throughput LLM Gateway 

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/API-FastAPI-green)
![Sentence-Transformers](https://img.shields.io/badge/Embeddings-SentenceTransformers-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

A production-grade middleware gateway designed to optimize enterprise LLM workloads. It combines semantic vector caching to bypass redundant inference calls and dynamic query routing to balance performance and cost between local open-source models and frontier APIs.

---

##  System Architecture & Workflow

```mermaid
graph TD
    A[Incoming Prompt] --> B[Semantic Cache Lookup]
    B -->|"Cache Hit (Similarity >= 0.85)"| C[Instant Cached Response]
    B -->|Cache Miss| D[Dynamic Router Classification]
    D -->|Complex Reasoning| E[Frontier LLM API]
    D -->|Standard Task| F[Local vLLM Model]
    E --> G[Store in Semantic Cache]
    F --> G
    G --> H[API Response]
```

Semantic Caching Layer: Computes dense vector embeddings of incoming queries and matches them against historical requests using cosine similarity, slashing response times to milliseconds.

Dynamic Router: Analyzes query complexity markers to route tasks intelligently between local and frontier models.

High-Throughput Middleware: Built with FastAPI to handle high-concurrency enterprise traffic safely.

##  Technical Stack
API Framework: FastAPI & Uvicorn for asynchronous, high-concurrency request handling.

Vector Embeddings & Similarity: Sentence-Transformers (all-MiniLM-L6-v2) and NumPy for dense vector generation and high-speed cosine similarity matching.

Data Validation & Settings: Pydantic and Pydantic-Settings for robust payload validation and environment configuration.

Networking: HTTPX for asynchronous upstream model routing calls.

