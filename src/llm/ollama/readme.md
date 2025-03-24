### **6️⃣ Ollama Provider (Local LLMs)**
The Ollama provider enables running local LLMs using the Ollama framework.

**Configuration Example:**
```json
"llm_provider": {
    "module": "src.llm.ollama.ollama_provider",
    "class": "OllamaProvider",
    "params": {
        "model": "mistral"
    }
}
```

**Required Parameters:**
- `model`: The locally installed LLM to use with Ollama.

---
