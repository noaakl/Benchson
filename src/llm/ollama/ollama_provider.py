from llm_provider import LLMProvider
from typing import Any, Dict, List


class OllamaProvider(LLMProvider):
    def __init__(self, model: str, **kwargs):
        super().__init__(**kwargs)
        self.install_dependency("ollama")  # Ensure the package is installed
        import ollama

        self.model = model

    def _generate(
        self, messages: List[Dict[str, str]], parameters: Dict[str, Any] = None
    ) -> str:
        system_prompt = next(
            (m["content"] for m in messages if m["role"] == "system"), None
        )
        user_prompt = " ".join(m["content"] for m in messages if m["role"] == "user")

        params = parameters or {}
        response = ollama.chat(
            model=self.model,
            messages=(
                [{"role": "system", "content": system_prompt}] if system_prompt else []
            ),
            **params
        )
        return response["message"]["content"]
