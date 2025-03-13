from llm_provider import LLMProvider
from typing import Any, Dict, List
import requests


class ClaudeProvider(LLMProvider):
    def __init__(self, api_key, model="claude-2", **kwargs):
        super().__init__(**kwargs)
        self.api_key = api_key
        self.model = model

    def _generate(
        self, messages: List[Dict[str, str]], parameters: Dict[str, Any] = None
    ) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        payload = {"model": self.model, "messages": messages, **(parameters or {})}
        response = requests.post(
            "https://api.anthropic.com/v1/complete", headers=headers, json=payload
        )
        return response.json().get("completion", "")
