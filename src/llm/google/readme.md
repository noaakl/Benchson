### ** Google Vertex AI Provider**
This provider integrates with Google’s Vertex AI models.

**Configuration Example:**
```json
"llm_provider": {
    "module": "src.llm.googlevertex.googlevertex_provider",
    "class": "GoogleVertexProvider",
    "params": {
        "project": "your-gcp-project",
        "location": "us-central1",
        "model": "text-bison"
    }
}
```

**Required Parameters:**
- `project`: Google Cloud project ID.
- `location`: Region for Vertex AI.
- `model`: The Vertex AI model to use.

---
