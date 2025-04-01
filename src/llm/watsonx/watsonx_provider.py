from ..llm_provider import LLMProvider
from typing import Any, Dict, List
import requests


class IBMWatsonXProvider(LLMProvider):
    def __init__(self, api_key, url, model="ibm-mistral-7b", **kwargs):
        super().__init__(**kwargs)
        self.api_key = api_key
        self.url = url
        self.model = model

    def _generate(
        self, messages: List[Dict[str, str]], parameters: Dict[str, Any] = None
    ) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        payload = {"model_id": self.model, "input": messages, **(parameters or {})}
        response = requests.post(self.url, headers=headers, json=payload)
        return response.json().get("output", "")
