from typing import Any, Dict, List
from llm_provider import LLMProvider


class HuggingFaceProvider(LLMProvider):
    def __init__(self, model="mistralai/Mistral-7B-Instruct-v0.1", **kwargs):
        super().__init__(**kwargs)
        self.install_dependency("transformers")  # Ensure the package is installed
        from transformers import pipeline

        self.generator = pipeline("text-generation", model=model)

    def _generate(
        self, messages: List[Dict[str, str]], parameters: Dict[str, Any] = None
    ) -> str:
        user_prompt = " ".join(m["content"] for m in messages if m["role"] == "user")

        params = parameters or {}
        response = self.generator(user_prompt, **params)
        return response[0]["generated_text"]
