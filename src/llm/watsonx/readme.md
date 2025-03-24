
### ** WatsonX Provider (IBM)**
This provider connects to IBM’s WatsonX LLM service.

**Configuration Example:**
```json
"llm_provider": {
    "module": "src.llm.watsonx.watsonx_provider",
    "class": "WatsonXProvider",
    "params": {
        "api_key": "your-ibm-api-key",
        "instance_id": "your-watsonx-instance",
        "model": "ibm/granite-13b"
    }
}
```

**Required Parameters:**
- `api_key`: IBM Cloud API key.
- `instance_id`: WatsonX service instance ID.
- `model`: The WatsonX model to use.

---