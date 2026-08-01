from app.cache import SemanticCache
from app.router import dynamic_route
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="High-Throughput LLM Gateway",
    description=(
        "Enterprise gateway featuring semantic vector caching and dynamic"
        " model routing"
    ),
    version="1.0.0",
)


class PromptRequest(BaseModel):
  query: str


@app.post("/gateway/chat")
async def gateway_chat(request: PromptRequest):
  query = request.query

  # 1. Check Semantic Cache
  cached_response = SemanticCache.lookup(query)
  if cached_response:
    return {
        "query": query,
        "source": "semantic_cache",
        "response": cached_response,
    }

  # 2. Dynamic Route Determination
  selected_route = dynamic_route(query)

  # 3. Simulate LLM Generation (Mocking model response)
  if selected_route == "frontier-llm-api":
    generated_response = (
        f"[Frontier LLM Synthesized Answer]: Deep reasoning analysis for '{query}'."
    )
  else:
    generated_response = (
        f"[Local vLLM Answer]: Fast execution output for '{query}'."
    )

  # 4. Store in Cache for Future Reuse
  SemanticCache.store(query, generated_response)

  return {
      "query": query,
      "source": selected_route,
      "response": generated_response,
  }