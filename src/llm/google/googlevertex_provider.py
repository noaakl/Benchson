from llm_provider import LLMProvider
from typing import Any, Dict, List


class GoogleVertexAIProvider(LLMProvider):
    def __init__(
        self, project_id, location="us-central1", model="gemini-pro", **kwargs
    ):
        super().__init__(**kwargs)
        self.install_dependency(
            "google-cloud-aiplatform"
        )  # Ensure the package is installed
        from google.cloud import aiplatform

        self.project_id = project_id
        self.location = location
        self.model = model

    def _generate(
        self, messages: List[Dict[str, str]], parameters: Dict[str, Any] = None
    ) -> str:
        response = aiplatform.generation.predict(
            model=self.model, contents=messages, **(parameters or {})
        )
        return response.candidates[0].content if response.candidates else ""
