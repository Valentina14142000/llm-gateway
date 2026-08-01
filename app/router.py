def dynamic_route(query: str) -> str:
  # Simple heuristic rule or lightweight classifier for routing
  complex_keywords = [
      "architect",
      "multi-hop",
      "compare",
      "debug",
      "strategy",
      "compliance",
  ]
  is_complex = any(keyword in query.lower() for keyword in complex_keywords)

  if is_complex:
    print("---ROUTER: Routing to Frontier LLM (High-Reasoning Mode)---")
    return "frontier-llm-api"
  else:
    print("---ROUTER: Routing to Self-Hosted Local Model (vLLM Fast Path)---")
    return "local-vllm-instance"