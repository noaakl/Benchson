# OpenAI LLM Provider

implements LLM Provider for OpenAI LLM.

## usage:

In your config:
```json
    "llm_provider": {
                "module": "src.llm.openai.openai_provider",
                "class": "OpenAIProvider",
                "params": {
                    "api_key": "your-api-key-here",
                    "model": "gpt-4o-mini"
                }
            }
```

**Required Parameters:**
- `api_key`: OpenAI API key.
- `model`: The OpenAI model to use.

---

