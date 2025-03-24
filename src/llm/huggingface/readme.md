### ** Hugging Face Provider**
The Hugging Face provider allows interaction with models hosted on Hugging Face’s API.

**Configuration Example:**
```json
"llm_provider": {
    "module": "src.llm.huggingface.huggingface_provider",
    "class": "HuggingFaceProvider",
    "params": {
        "api_key": "your-huggingface-api-key",
        "model": "bigscience/bloom"
    }
}
```

**Required Parameters:**
- `api_key`: Hugging Face API key.
- `model`: The Hugging Face model to use.

---
