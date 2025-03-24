### ** Claude (Anthropic) Provider**
The Claude provider integrates with Anthropic’s Claude models.

**Configuration Example:**
```json
"llm_provider": {
    "module": "src.llm.claude.claude_provider",
    "class": "ClaudeProvider",
    "params": {
        "api_key": "your-api-key",
        "model": "claude-3"
    }
}
```

**Required Parameters:**
- `api_key`: Anthropic API key.
- `model`: The Claude model to use.

---
